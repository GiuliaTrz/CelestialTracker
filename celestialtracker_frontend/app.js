const lblState = document.getElementById("lblState");

const States = {
    STANDBY: 1,
    COMPUTING: 2,
    TLE_UPDATE: 3,
    ERROR: 4,
};

var currentState = States.STANDBY;

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
    }
}