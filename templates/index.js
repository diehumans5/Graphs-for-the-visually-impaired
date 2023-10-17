const startButton = document.getElementById('startButton');
const outputDiv = document.getElementById('output');
const recognition = new webkitSpeechRecognition() || new SpeechRecognition();

recognition.interimResults = false;
recognition.continuous = true;

startButton.addEventListener('click', () => {
recognition.start();
startButton.disabled = true;
startButton.textContent = 'Listening...';
});

recognition.onresult = event => {
const result = event.results[event.results.length - 1][0].transcript;
outputDiv.textContent = result;
let utterance = new SpeechSynthesisUtterance();
  utterance.text = result;
  utterance.voice = window.speechSynthesis.getVoices()[0];
window.speechSynthesis.speak(utterance);
};

recognition.onend = () => {
startButton.disabled = false;
startButton.textContent = 'Start Recording';
};

recognition.onerror = event => {
console.error('Speech recognition error:', event.error);
};

recognition.onnomatch = () => {
console.log('No speech was recognized.');
};