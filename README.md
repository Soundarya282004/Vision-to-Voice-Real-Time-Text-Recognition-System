# Vision-to-Voice-Real-Time-Text-Recognition-System
it uses a webcam to detect text in real time, converts the detected text into digital text using OCR (Tesseract), and then reads it aloud using text-to-speech.

🧠 What This Project Does (Short Description for GitHub)

This project uses a webcam to detect text in real time, converts the detected text into digital text using OCR (Tesseract), and then reads it aloud using text-to-speech.

It combines Computer Vision + OCR + Speech Synthesis to help users hear printed text.

⚙️ Requirements

Install these Python libraries before running:

pip install opencv-python pytesseract pygame gTTS mutagen

🔹 Install Tesseract OCR Engine (Important!)

This project will NOT work without Tesseract installed on your system.

▶ Windows

Download from:
https://github.com/tesseract-ocr/tesseract

Install it

Add this line in your code before using pytesseract:

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

▶ Linux (Ubuntu)
sudo apt install tesseract-ocr

▶ Mac
brew install tesseract

▶ How to Run the Project

Save your file as main.py

Make sure your webcam is connected

Open terminal in the project folder

Run:

python main.py

🎥 How It Works (Step-by-Step)

You can put this in GitHub under “Working” section.

Captures Live Video
The webcam continuously captures frames using OpenCV.

Preprocessing the Image

Converts frame to grayscale

Applies thresholding

Uses dilation to highlight text regions

Text Detection

Finds contours (possible text areas)

Draws green rectangles around detected regions

OCR (Text Recognition)

Each detected region is passed to Tesseract OCR

Extracted text is stored

Text-to-Speech Conversion

Recognized text is converted into speech using Google Text-to-Speech (gTTS)

Audio is saved as voice.mp3

Audio Playback

The MP3 file is played using pygame

The program waits until audio finishes before continuing

Exit

Note: Press Q to close the camera and stop the program

⌨️ Controls
Key	Action
Q	Quit the application
