const { Socket } = require("net");
const socket = new Socket();

socket.connect({ host: "192.168.0.106", port: 4444 });