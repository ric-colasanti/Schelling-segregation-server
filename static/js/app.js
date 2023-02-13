var draw = function (area) {
  var bCol = "#ffffff";
  caCanvas.clear();
  for (x = 0; x < area.length; x++) {
    for (y = 0; y < area[x].length; y++) {
      if (area[x][y] == 1) {
        caCanvas.draw(x, y, bCol, true, "#ff0000");
      }
      if (area[x][y] == 2) {
        caCanvas.draw(x, y, bCol, true, "#0000ff");
      }
    }
  }
  caCanvas.update("canvas");
};

var setVals = function () {
  likeness = Number(document.getElementById("alike").value);
  density = Number(document.getElementById("pop").value);
  document.getElementById("alikelable").innerHTML = parseFloat(likeness)
    .toFixed(1)
    .toLocaleString();
  document.getElementById("poplable").innerHTML = parseFloat(density)
    .toFixed(1)
    .toLocaleString();
  likeness = likeness / 100;
  density = density / 100;
};

var run = function () {
  if (running == 1) {
    running = 2;
    let but = (document.getElementById("running").innerHTML = " Run ");
    socket.emit("stop");
  } else if (running == 2) {
    running = 1;
    let but = (document.getElementById("running").innerHTML = "Stop");
    console.log("restart");
    socket.emit("restart");
  } else if (running == 0) {
    running = 1;
    let but = (document.getElementById("running").innerHTML = "Stop");
    socket.emit(
      "message",
      JSON.stringify({ size: size, density: density, likeness: likeness })
    );
  }
};


var plot = function(iterations){

  var data = [{
      x: time,
      y: happy,
      name: "Happy",
      mode: "lines",
      type: "scatter",
      line: {
      color:"green"
      }
    },{x: time,
    y: unhappy,
    name: "Unhappy",
    mode: "lines",
    type: "scatter",
    line: {
    color:"orange"
    }
  }];
    
    // Define Layout
    var layout = {
      xaxis: {range: [0, ((Math.floor(iterations/10))+1)*10], title: "Time"},
      yaxis: {range: [0, size*size], title: "People"},
      title: "Happiness"
    };
    
    // Display using Plotly
    Plotly.newPlot("myPlot", data, layout);
}

var size = 40;
var caCanvas = new CACanvas(size);
var socket = io.connect();
var likeness = 0.4;
var density = 0.95;
var running = 0;
var iteration =0;
var happy =[]
var unhappy =[]
var time = []

//receive details from server
socket.on("data", function (data) {
  time.push(iteration)
  happy.push(data[1])
  unhappy.push(data[2])
  plot(iteration)
  draw(data[0]);
  iteration++
});
