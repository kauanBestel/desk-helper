const { app, BrowserWindow } = require("electron");
const path = require("path");

function createWindow() {
  const win = new BrowserWindow({
    width: 500,
    height: 400,
    alwaysOnTop: true,
    skipTaskbar: false, //aparecer junto dos apps abertos
    webPreferences: {
      preload: path.join(__dirname, "renderer.js"),
      nodeIntegration: true,
      contextIsolation: false,
    },
  });
  win.loadFile("index.html");

  win.on("blur", () => {
    win.setIgnoreMouseEvents(true, { forward: true }); // passa os eventos para o fundo
    win.setOpacity(0.6);
  });

  win.on("focus", () => {
    win.setIgnoreMouseEvents(false);
    win.setOpacity(1);
  });
}

app.whenReady().then(createWindow);
