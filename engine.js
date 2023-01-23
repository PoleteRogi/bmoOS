const colors = {
    background: '#d9ffea',
    foreground: '#63bda4'
}

const expressions = {
    neutral: 'assets/bmo-neutral.png',
    happy: 'assets/happy.png',
    disgusted: 'assets/bmo-disgusted.png',
    eyesClosed: 'assets/bmo-eyes-closed.png',
    naughty: 'assets/bmo-naughty',
    oneEye: 'assets/bmo-one-eye.png',
    scared: 'assets/bmo-scared.png',
    serious: 'assets/bmo-serious.png',
    surprised: 'assets/bmo-surprised.png',
    tired: 'assets/bmo-tired.png'
}

let expression = 'neutral'

const canvas = document.getElementById('canvas')
const ctx = canvas.getContext('2d')

function start() {
    _closeEyes()
}

function update() {
    requestAnimationFrame(update)

    _clearScreen() 
    _drawFace()
}

function _closeEyes() {
    setInterval(function() {
        expression = 'eyesClosed'
        setTimeout(function() {
            expression = 'neutral'
        }, 1000)
    }, 10000)
}

function _playStartupSound() {
    playSound('assets/startup.mp3', 1)
}

function playSound(src, volume) {
    const audio = document.createElement('audio')
    audio.src = src
    audio.volume = volume
    audio.play()
}

function drawImage(asset, x, y, width, height) {
    const image = document.createElement('img')
    image.src = asset
    ctx.drawImage(image, 0, 0, image.width, image.height, x, y, width, height)
}

function _drawFace() {
    drawImage(expressions[expression], 0, 0, canvas.width, canvas.height)
}

function _clearScreen() {
    ctx.fillStyle = colors.background;
    ctx.fillRect(0, 0, canvas.width, canvas.height)
}

start()
requestAnimationFrame(update)