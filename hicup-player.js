let audioFiles = [];
let currentSongIndex = 0;
let shuffledIndexes = [];
const audio = new Audio();

audio.addEventListener('ended', function() {
    if (currentSongIndex < audioFiles.length - 1) {
        currentSongIndex++;
    } else {
        currentSongIndex = 0;
    }
    audio.src = URL.createObjectURL(audioFiles[currentSongIndex]);
    audio.play();
    updateDisplay();
});

document.getElementById('play').addEventListener('click', function() {
    if (audio.paused) {
        audio.play();
        updateDisplay();
    } else {
        audio.pause();
        updateDisplay('Paused');
    }
});

document.getElementById('prev').addEventListener('click', function() {
    if (currentSongIndex > 0) {
        currentSongIndex--;
        audio.src = URL.createObjectURL(audioFiles[currentSongIndex]);
        audio.play();
        updateDisplay();
    }
});

document.getElementById('next').addEventListener('click', function() {
    if (currentSongIndex < audioFiles.length - 1) {
        currentSongIndex++;
        audio.src = URL.createObjectURL(audioFiles[currentSongIndex]);
        audio.play();
        updateDisplay();
    }
});

document.getElementById('shuffle').addEventListener('click', function() {
    shuffleArray(shuffledIndexes);
    currentSongIndex = 0;
    audio.src = URL.createObjectURL(audioFiles[shuffledIndexes[currentSongIndex]]);
    audio.play();
    updateDisplay();
});

document.getElementById('file-input').addEventListener('change', function(event) {
    audioFiles = Array.from(event.target.files);
    shuffledIndexes = [...Array(audioFiles.length).keys()];
    resetAudio();
});

function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

function resetAudio() {
    if (audioFiles.length > 0) {
        currentSongIndex = 0;
        audio.src = URL.createObjectURL(audioFiles[currentSongIndex]);
        audio.play();
        updateDisplay();
    } else {
        audio.src = '';
        updateDisplay('Hicup Music Player');
    }
}

function updateDisplay(text = '') {
    document.getElementById('screen').innerText = text || `Now Playing: ${audioFiles[currentSongIndex].name}`;
}
