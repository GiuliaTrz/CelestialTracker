const { contextBridge, ipcRenderer } = require('electron/renderer')

contextBridge.exposeInMainWorld('electronAPI', {
  loadSatellites: () => ipcRenderer.invoke('load-satellites')
})