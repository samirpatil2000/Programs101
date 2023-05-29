const math = require('math');

const CENTRE_POINT_X = 19.021799917866176
const CENTRE_POINT_Y = 72.87008087597307

const RADIUS = 300 // radius in meters


function functionPointInsideOrNot(x, y){
    var result = (CENTRE_POINT_X - x) ** 2 + (CENTRE_POINT_Y - y) ** 2
    return math.sqrt(result)
}

console.log(functionPointInsideOrNot(19.034163663763668, 72.85948103715276), "ee")