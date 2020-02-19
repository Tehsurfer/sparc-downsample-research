
function makeArr(startValue, stopValue, cardinality) {
    var arr = [];
    var step = (stopValue - startValue) / (cardinality - 1);
    for (var i = 0; i < cardinality; i++) {
      arr.push(startValue + (step * i));
    }
    return arr;
  }


  let file_url = './resampled.json'


  fetch(file_url).then(response => response.json()).then( ldata => {

    var x = makeArr(0, ldata.data.length, ldata.data.length)
    var data = [{
        type: "scattergl",
        mode: "lines",
        
        x: x,
        y: ldata.data
    }]
      Plotly.newPlot('myDiv', data)
    })
   