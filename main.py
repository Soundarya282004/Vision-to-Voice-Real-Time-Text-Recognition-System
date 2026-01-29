import cv2
import pytesseract
import pygame
import time
from gtts import gTTS
from mutagen.mp3 import MP3

vs = cv2.VideoCapture(0)

while True:
    ret, img = vs.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)

    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
    dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    im2 = img.copy()

    text1 = ''
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cropped = im2[y:y + h, x:x + w]

        text = pytesseract.image_to_string(cropped).strip()
        text1 += ' ' + text

    cv2.imshow('Image to voice', im2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        vs.release()
        cv2.destroyAllWindows()
        break

    text1 = text1.strip()
    if text1:
        print('\n ------------------------Recognized Text------------------------ \n')
        print(text1)
        myobj = gTTS(text=text1, lang='en', slow=False)
        myobj.save("voice.mp3")
        print('\n ------------------------Audio Playback------------------------ \n')
        song = MP3("voice.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("voice.mp3")
        pygame.mixer.music.play()
        time.sleep(song.info.length)
        pygame.quit()