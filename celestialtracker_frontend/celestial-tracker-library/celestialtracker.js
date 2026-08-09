
const {execute} = require("./executor")

/** CelestialTracker command used to get the satellite list */
const LIST_SATELLITE_COMMAND = "-l --json";


class CelestialTracker {
    /**
     * CelestialTracker constructor
     * @param {string} executable The CelestialTracker executable file
     */
    constructor(executable){
        this.executable = executable;
    }

    /**
     * Shows satellites contained in the TLE file
     * @returns JSON object containing the satellites in the TLE file
     */
    async listSatellites(){
        const output = await execute(this.executable,LIST_SATELLITE_COMMAND.split(" "));
        return output
    }

    async getPredictions(satelliteId, latitude, longitude, elevation, horizon_altitude){
        
    }
}


module.exports = { CelestialTracker };