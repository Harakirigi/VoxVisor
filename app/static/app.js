
var modal = document.getElementById('modal');
var span = document.getElementsByClassName('close')[0];

async function uploadImageForText() {
    const fileInput = document.getElementById('imageInput');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    const response = await fetch('/upload/image/text', {
        method: 'POST',
        body: formData
    });

    const data = await response.json();


    modal.style.display = "block";
    span.onclick = function() {
        modal.style.display = "none";
    }
    window.onclick = function(event) {
        if (event.target == modal) {
          modal.style.display = "none";
        }
    }

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


    modal.style.display = "block";
    span.onclick = function() {
        modal.style.display = "none";
    }
    window.onclick = function(event) {
        if (event.target == modal) {
          modal.style.display = "none";
        }
    }

    document.getElementById('audioResult').innerText = 'Transcription: ' + data.transcription;
}
