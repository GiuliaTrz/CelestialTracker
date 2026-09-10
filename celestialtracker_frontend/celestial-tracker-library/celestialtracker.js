
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

    /**
     * Returns the satellite passes forecast for a given date and location
     * 
     * @param {number} satelliteId Satellite index in the TLE file
     * @param {number} latitude 
     * @param {number} longitude 
     * @param {string} date The date for wich you want to get the satellite passes forecast
     * @param {number} elevation Elevation (in meters) from the wgs84 reference ellipsoid
     * @param {number} horizon_altitude Degrees above the horizon
     */
    async getPredictions(satelliteId, latitude, longitude, date = "", elevation=20.0, horizon_altitude=10.0){
        await this._allowedType(satelliteId, "number");
        await this._allowedType(date, "string");
        await this._allowedType(latitude, "number");
        await this._allowedType(longitude, "number");
        await this._allowedType(elevation, "number");
        await this._allowedType(horizon_altitude, "number");

        var baseCommand = `-s ${satelliteId} --json`;
        var coordinates = `${latitude} ${longitude}`;

        if(date != null && date !== ""){
            if(!await this._checkDateFormat(date)){
                throw new TypeError(`Expected date in format YYYY-MM-DD but got ${date}`);
            }
            baseCommand += ` -d ${date}`;
        }

        if(elevation != null){
            baseCommand += ` -e ${elevation}`;
        }

        if(horizon_altitude != null){
            baseCommand += ` -a ${horizon_altitude}`;
        }

        const command = `${baseCommand} ${coordinates}`;
        console.log(`Executing command: ${command}`);

        const output = await execute(this.executable,command.split(" "));
        return output
    }

    /**
     * Checks if the variable is of the allowed type
     * 
     * @param {*} variable 
     * @param {string} allowedType 
     * @returns true if the variable is of the allowed type, throws a TypeError otherwise
     */
    async _allowedType(variable, allowedType){
        const type = typeof variable;
        if(type != allowedType){
            throw new TypeError(`Expected ${allowedType} but got ${type}`);
        }
        return true;
    }

    async _checkDateFormat(date){
        const regex = /^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$/;
        return regex.test(date);
    }
}


module.exports = { CelestialTracker };