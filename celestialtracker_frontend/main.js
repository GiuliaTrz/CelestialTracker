const { app, BrowserWindow } = require('electron/main')

const {CelestialTracker} = require("./celestial-tracker-library/celestialtracker")

const createWindow = () => {
    const win = new BrowserWindow({
        width: 1200,
        height: 650,
        minWidth: 1200,
        minHeight: 650,
    })

    win.loadFile('index.html')
}

app.whenReady().then(() => {
    createWindow()

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createWindow()
        }
    })
})

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit()
    }
})

async function main() {
    /*
    const tracker = new CelestialTracker("C:\\Progetti\\Python\\CelestialTracker\\dist\\main.exe");
    const output = await tracker.listSatellites();
    if(output.rc == 0){
        console.info(output.stdout);
    }else{
        console.error(output.stderr);
    }

    console.info("-----");
    const output1 = await tracker.getPredictions(0, 1,1);
    if(output1.rc == 0){
        console.info(output1.stdout);
    }else{
        console.error(output1.stderr);
    }
    */
}
main();