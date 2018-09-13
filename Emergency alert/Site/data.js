window.dataSet = [
    ["Tiger Nixon", "System Architect", "Edinburgh", "5421", "2011/04/25", "$320,800"],
];

function init() {
        window.wsurl = "ws://localhost:8000/"
}

function doConnect() {
        websocket = new WebSocket(window.wsurl);
        websocket.onopen = function (evt) { onOpen(evt) };
        websocket.onclose = function (evt) { onClose(evt) };
        websocket.onerror = function (evt) { onError(evt) };
    }

function onOpen(evt) {
        writeToScreen("connected\n");
}

function onClose(evt) {
        writeToScreen("disconnected\n");
}

function onMessage(evt) {
    writeToScreen("response: " + evt.data + '\n');
    dataSet.push("");
}

function onError(evt) {
        writeToScreen('error: ' + evt.data + '\n');
        websocket.close();
}

function writeToScreen(message) {
        document.myform.outputtext.value += message
        document.myform.outputtext.scrollTop = document.myform.outputtext.scrollHeight;
}

window.addEventListener("load", init, false);
window.addEventListener("load", doConnect, false);

function doDisconnect() {
        websocket.close();
}