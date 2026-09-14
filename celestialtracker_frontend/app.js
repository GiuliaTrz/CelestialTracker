const lblState = document.getElementById("lblState");
const txtbLatitude = document.getElementById("txtbLatitude");
const txtbLongitude = document.getElementById("txtbLongitude");
const txtbDate = document.getElementById("txtbDate");
const menuSelectSatellite = document.getElementById("menuSelectSatellite");

const States = {
    STANDBY: 1,
    COMPUTING: 2,
    TLE_UPDATE: 3,
    ERROR: 4,
    LOADING_SATELLITES: 5
};

var currentState = States.STANDBY;
var satellites = [];

loadSatellites();

/**
 * This method updates the state label with the given class and inner HTML.
 * @param {string} classValue 
 * @param {string} innerhtml 
 */
function setStateHTML(classValue, innerhtml) {
    lblState.classList.add(classValue);
    lblState.innerHTML = innerhtml;
}

/**
 * Update the application state and the label accordingly.
 * @param {number} newState 
 */
function setState(newState) {
    currentState = newState
    lblState.classList.remove("pill--idle", "pill--success", "pill--update", "pill--error");
    
    switch (currentState) {
        case States.STANDBY:
            setStateHTML("pill--idle",'<i class="bi bi-broadcast"></i> Standby');
            break;
        case States.COMPUTING:
            setStateHTML("pill--computing", '<i class="bi bi-gear"></i> COMPUTING');
            break;
        case States.TLE_UPDATE:
            setStateHTML("pill--update", '<i class="bi bi-arrow-clockwise"></i> Updating');
            break;
        case States.ERROR:
            setStateHTML("pill--error", '<i class="bi bi-exclamation-triangle"></i> Error');
            break;
        case States.LOADING_SATELLITES:
            setStateHTML("pill--computing", '<i class="bi bi-cloud-arrow-down"></i> Loading satellites...');
            break;
    }
}

/**
 * Load the list of satellites and populate the select element.
 */
function loadSatellites() {
    console.info("Loading satellites...");
    setState(States.LOADING_SATELLITES);
    window.electronAPI.loadSatellites().then((output) => {
        if(output.rc == 0){ // Successful
            console.info("Satellites loaded successfully.");
            console.info(output.stdout);
            satellites = JSON.parse(output.stdout);
            populateSatelliteSelect();
            setState(States.STANDBY);
        }else{ // Failed
            console.error("Failed to load satellites.");
            console.error(output.stderr);
            setState(States.ERROR);
        }
    }).catch((error) => {
        console.error("Error while loading satellites:", error);
        setState(States.ERROR);
    });
}

/**
 * Populate the satellite select element with the loaded satellites.
 * 
 * value is set to the index of the satellite, 
 * while the text is set to the satellite name.
 */
function populateSatelliteSelect() {
    menuSelectSatellite.innerHTML = '';
    for(var i = 0; i < satellites.length; i++){
        const option = document.createElement("option");
        option.value = i;
        option.textContent = satellites[i];
        menuSelectSatellite.appendChild(option);
    } 
}

function onClickComputePasses(){
    const latitude = txtbLatitude.value;
    const longitude = txtbLongitude.value;
    const date = txtbDate.value;
    console.info(isNumber(latitude));
    console.info(isNumber(longitude));
    alert(latitude +" " + longitude + " " +  date);

}

/**
  * Checks if the variable is a number
  * 
  * @param {*} variable 
  * @returns true if the variable is a number
  */
 function isNumber(variable){
    const regex=/^(0|[1-9]\d*)(\.\d+)?$/;
    return regex.test(variable);
 }
