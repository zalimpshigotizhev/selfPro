
function normalizeColor(hex){
    if (typeof hex !== 'string') {
        throw new TypeError('Expected a string');
    }

    // Remove the '#' if it exists
    hex = hex.replace('#', '');

    // Validate the hex color string length
    if (hex.length !== 6) {
        throw new Error('Invalid hex color length. Expected 6 characters.');
    }
    var r = parseInt(hex.substring(0, 2), 16);
    var g = parseInt(hex.substring(2, 4), 16);
    var b = parseInt(hex.substring(4, 6), 16);
    return `rgba(${r},${g},${b}, 0.1)`
}

export default normalizeColor
