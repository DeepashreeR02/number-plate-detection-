import cv2
import numpy as np
import pytesseract
import time
from email.message import EmailMessage
import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "deepashreeram12@gmail.com"
receiver_email = "deepashreeram12@gmail.com"
#password = input("Type your password and press enter: ")
message='mesoln email test'
# Create a secure SSL context
context = ssl.create_default_context()
from googletrans import Translator
import imutils

# adds image processing capabilities
from PIL import Image

# converts the text to speech
import pyttsx3

frameWidth = 640  # Frame Width
franeHeight = 480  # Frame Height

plateCascade = cv2.CascadeClassifier("indian_license_plate.xml")
minArea = 2000
pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, franeHeight)
cap.set(10, 150)
count = 0

while True:
    success, img = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberPlates = plateCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in numberPlates:
        area = w * h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


            #cv2.putText(img, "NumberPlate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            imgRoi = img[y:y + h, x:x + w]

            result = pytesseract.image_to_string(imgRoi)
            if 'R' in result:
                count += 1
                if count == 1:
                    email_subject = "Entry and exit"
                    sender_email_address = "deepashreeram12@gmail.com"
                    receiver_email_address = "deepashreeram12@gmail.com"
                    email_smtp = "smtp.gmail.com"
                    email_password = "mulk btid mmgo deld"

                    message = EmailMessage()
                    message['Subject'] = email_subject
                    message['From'] = sender_email_address
                    message['To'] = receiver_email_address
                    server = smtplib.SMTP(email_smtp, '587')

                    server.ehlo()
                    server.starttls()
                    server.login(sender_email_address, email_password)
                    message.set_content("RJ14CV0002 \n vechile drive test \n Deepashree")
                    server.send_message(message)
                    server.quit()
                if count == 2:
                    count=0
                    amount=1000
                    amount=amount-1000
                    email_subject = "vechile exit port"
                    sender_email_address = "deepashreeram12@gmail.com"
                    receiver_email_address = "deepashreeram12@gmail.com"
                    email_smtp = "smtp.gmail.com"
                    email_password = "mulk btid mmgo deld"

                    message = EmailMessage()
                    message['Subject'] = email_subject
                    message['From'] = sender_email_address
                    message['To'] = receiver_email_address
                    server = smtplib.SMTP(email_smtp, '587')

                    server.ehlo()
                    server.starttls()
                    server.login(sender_email_address, email_password)
                    message.set_content("RJ14CV0002 \n vechile exit \n deepashree \n amount deducted:150 \n")
                    server.send_message(message)
                    server.quit()
                print(result)
                message = result;
                cv2.putText(img, result, (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                cv2.putText(imgRoi, result, (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

            cv2.imshow("ROI", imgRoi)
    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        print("translating")
        result = pytesseract.image_to_string(img)

        #message = result;
        print(result)
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, 'riacheeku')
        # TODO: Send email here
        server.sendmail(sender_email, receiver_email, message)
        if 'H' in result:
             print(result)
             time.sleep(3)
        '''
        tr="translating"
        p = Translator()
        # translates the text into german language
        k = p.translate(tr, dest='english')
        print(k)
        engine = pyttsx3.init()

        # an audio will be played which speaks the test if pyttsx3 recognizes it
        engine.say(k)
        engine.runAndWait()
        '''
        cv2.imwrite("E:/projects 2021/ml projects/ml projects/Number_Plate_Detection-master/Number_Plate_Detection-master/images" + str(
                count) + ".jpg", imgRoi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Scan Saved", (15, 265), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 2)
        cv2.imshow("Result", img)
        cv2.waitKey(500)




