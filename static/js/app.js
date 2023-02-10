
var draw = function (area) {
  var bCol = "#ffffff";
  caCanvas.clear()
  for(x=0;x<area.length;x++){
    for(y=0;y<area[x].length;y++){
      if(area[x][y]>0){
          let col = "#ff0000";
          if(area[x][y]==1){
              col = "#0000ff";
          }          
          caCanvas.draw(x,y, bCol, true, col);
        }
      }
  };
  caCanvas.update("canvas");
};

console.log("here");
var size = 40;
var caCanvas = new CACanvas(size);
var socket = io.connect();
socket.emit('message', JSON.stringify({size:size,density: 0.9,similar: 0.5}));

//receive details from server
socket.on("data", function (data) {
  draw(data[1]);
});
