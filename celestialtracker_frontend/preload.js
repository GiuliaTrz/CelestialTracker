const { contextBridge, ipcRenderer } = require('electron/renderer')

contextBridge.exposeInMainWorld('electronAPI', {
  loadSatellites: () => ipcRenderer.invoke('load-satellites'),
  getPredictions: (satelliteId, latitude, longitude, date) => ipcRenderer.invoke('getPredictions', satelliteId, latitude, longitude, date)
})