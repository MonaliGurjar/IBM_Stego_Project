import cv2
import os
import string
import hashlib
import json

img = cv2.imread("mypic.jpg") # Replace with the correct image path
msg = input("Enter secret message:")
password = input("Enter a passcode:")

d = {}

for i in range(255):
    d[chr(i)] = i

m = 0
n = 0
z = 0

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

cv2.imwrite("encryptedLL.png", img)
os.system("start encryptedLL.png")  # Use 'start' to open the image on Windows

password_hash=hashlib.sha256(password.encode()).hexdigest()
data={
    "hash":password_hash,
    "msgLength":len(msg)
}
with open("config.json","w") as f:
    json.dump(data,f)
print("password hash stored to config.json")