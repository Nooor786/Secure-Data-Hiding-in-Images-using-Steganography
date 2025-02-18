import cv2
import os

# Load image
image = cv2.imread("/Users/noorshaik/Downloads/untitled folder 5/tajmahajnight.jpg")  # Ensure the image path is correct

# User input for message and password
secret_message = input("Enter the secret message: ")
passcode = input("Enter a passcode: ")

# Character encoding and decoding dictionaries
char_to_pixel = {chr(i): i for i in range(256)}
pixel_to_char = {i: chr(i) for i in range(256)}

# Embedding message into image
row, col, channel = 0, 0, 0
for char in secret_message:
    image[row, col, channel] = char_to_pixel[char]
    row = (row + 1) % image.shape[0]
    col = (col + 1) % image.shape[1]
    channel = (channel + 1) % 3

# Save encrypted image
cv2.imwrite("encrypted_image.jpg", image)
os.system("start encrypted_image.jpg")  # Open image (Windows-specific)

# Decryption
decoded_message = ""
row, col, channel = 0, 0, 0
entered_passcode = input("Enter passcode for decryption: ")

if entered_passcode == passcode:
    for _ in range(len(secret_message)):
        decoded_message += pixel_to_char[image[row, col, channel]]
        row = (row + 1) % image.shape[0]
        col = (col + 1) % image.shape[1]
        channel = (channel + 1) % 3
    print("Decrypted message:", decoded_message)
else:
    print("Authentication failed! Access denied.")
