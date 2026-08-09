const { spawn } = require('node:child_process');

/**
 * Executes a binary file with the specified cli arguments
 * 
 * Example: 
 *   - Command: ping -n 3 google.it
 *   - execute("ping",['google.it', '-n','3']);
 * @param {string} path the file to execute
 * @param {string array} arguments command line arguments 
 * @returns 
 */
function execute(path, args) {
    return new Promise((resolve, reject) => {
        const command = spawn(path, args);
        let stdout = '';
        let stderr = '';
        
        command.stdout.on('data', (data) => {stdout += data.toString();});
        command.stderr.on('data', (data) => {stderr += data.toString();});
        command.on('error', (err) => {reject(err);});

        command.on('close', (code) => {
            resolve({
                stdout,
                stderr,
                rc: code
            });
        });
    });
}


module.exports = { execute };