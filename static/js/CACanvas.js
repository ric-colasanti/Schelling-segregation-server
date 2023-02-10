function rndInt(maxVal) {
    return Math.floor(Math.random() * maxVal);
}

class CACanvas {
    constructor(size, cSize = 40) {
        this.size = size;
        this.cSize = cSize;
        this.buffer = document.createElement("canvas");
        this.buffer.width = this.size * this.cSize;
        this.buffer.height = this.size * this.cSize;
        this.ctx = this.buffer.getContext("2d");
        let visible_canvas = document.getElementById("canvas");
        visible_canvas.width=400
        visible_canvas.height=400
    }

    draw(x, y, cellColor, circle = false, circleColor = "#000000") {
        this.ctx.beginPath();
        this.ctx.rect(x * this.cSize, y * this.cSize, this.cSize, this.cSize)
        this.ctx.fillStyle = cellColor;
        this.ctx.fill();
        if (circle === true) {
            let offset = Math.floor(this.cSize / 2);
            this.ctx.beginPath();
            this.ctx.arc(x * this.cSize + offset, y * this.cSize + offset, offset - 1, 0, 2 * Math.PI)
            this.ctx.fillStyle = circleColor;
            this.ctx.fill();
            this.ctx.strokeStyle = '#000000';
            this.ctx.stroke();
        }
    }
 
    
    drawCircle(x, y,colour,fcolor="black",sz=0,thick=1) {
        let offset = Math.floor(this.cSize / 2)-2;
        this.ctx.beginPath();
        this.ctx.arc(x * this.cSize + offset+sz/2, y * this.cSize + offset+sz/2, offset - (sz+1), 0, 2 * Math.PI)
        this.ctx.fillStyle = colour;
        this.ctx.fill();
        this.ctx.strokeStyle = fcolor;
        this.ctx.lineWidth = thick;
        this.ctx.stroke();
    }

    drawSquare(x, y, colour,width=0,bcolor="black") {
        this.ctx.beginPath();
        this.ctx.rect(x * this.cSize, y * this.cSize, this.cSize, this.cSize)
        this.ctx.fillStyle = colour;
        this.ctx.fill();
        this.ctx.strokeStyle = bcolor;
        this.ctx.lineWidth=width
        this.ctx.stroke();
    }

    drawLine(x1,y1,x2,y2,color= '#000000', thick = 1){
        this.ctx.beginPath();
        this.ctx.strokeStyle = color;
        this.ctx.lineWidth = thick;
        let offset = Math.floor(this.cSize / 2);
        this.ctx.moveTo(x1 * this.cSize+offset, y1 * this.cSize+offset)
        this.ctx.lineTo(x2 * this.cSize+offset, y2 * this.cSize+offset)
        this.ctx.stroke();
        this.ctx.lineWidth=1;
    }

    clear(colour="#ffffff"){
        this.ctx.beginPath();
        this.ctx.rect(0,0, this.buffer.width, this.buffer.height)
        this.ctx.fillStyle = colour;
        this.ctx.fill();
        
    }

    update(canvasID) {
        let visible_canvas = document.getElementById(canvasID);
        let vctx = visible_canvas.getContext("2d");
        vctx.drawImage(this.buffer, 0, 0, this.ctx.canvas.width, this.ctx.canvas.height, 0, 0, vctx.canvas.width, vctx.canvas.height);
    }
}



class Agents {
    constructor() {
        this.list = new Array();
    }
    addAgent(anAgent) {
        this.list.push(anAgent);
    }

    shuffle() {
        let currentIndex = this.list.length,  randomIndex;
      
        // While there remain elements to shuffle.
        while (currentIndex != 0) {
      
          // Pick a remaining element.
          randomIndex = Math.floor(Math.random() * currentIndex);
          currentIndex--;
      
          // And swap it with the current element.
          [this.list[currentIndex], this.list[randomIndex]] = [
            this.list[randomIndex], this.list[currentIndex]];
        }

      }
}