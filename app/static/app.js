async function uploadImageForText() {
    const fileInput = document.getElementById('imageInput');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    const response = await fetch('/upload/image/text', {
        method: 'POST',
        body: formData
    });

    const data = await response.json();
    document.getElementById('textResult').innerText = 'Text: ' + data.recognized_text;
}

async function uploadAudioForTranscription() {
    const fileInput = document.getElementById('audioInput');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    const response = await fetch('/upload/audio/transcribe', {
        method: 'POST',
        body: formData
    });

    const data = await response.json();
    document.getElementById('audioResult').innerText = 'Transcription: ' + data.transcription;
}