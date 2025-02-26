import cv2
import os
import string
import hashlib
import json

img = cv2.imread("encryptedLL.png") # Replace with the correct image path

with open("config.json","r") as f:
    data=json.load(f)

msgLength = data["msgLength"]
password = input("Enter passcode for Decryption:")
hashedCode = data["hash"]

verifyPassHash = hashlib.sha256(password.encode()).hexdigest()

if verifyPassHash!=hashedCode:
    print("YOU ARE NOT auth")
else:
    c = {}
    for i in range(255):
        c[i] = chr(i)

    message = ""
    n = 0
    m = 0
    z = 0

    for i in range(msgLength):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
        
    print("Decryption message:", message)