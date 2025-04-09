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



function openPage(pageName, elmnt, color) {
    // Hide all elements with class="tabcontent" by default */
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Remove the background color of all tablinks/buttons
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].style.backgroundColor = "";
    }
  
    // Show the specific tab content
    document.getElementById(pageName).style.display = "block";
  
    // Add the specific color to the button used to open the tab content
    elmnt.style.backgroundColor = color;
  }
  
  // Get the element with id="defaultOpen" and click on it
  document.getElementById("defaultOpen").click();
  