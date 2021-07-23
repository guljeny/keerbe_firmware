const { app, BrowserWindow } = require('electron');

function createWindow () {
  let win = new BrowserWindow({
    width: 1200,
    height: 680,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
      enableRemoteModule: true,
    }
  });

  win.loadFile('./dist/index.html');
}

app.on('ready', createWindow);
