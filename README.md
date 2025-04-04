# Prodigy-Projects
Caesar Cipher Project
The Caesar Cipher is a basic method of secret writing. It’s named after Julius Caesar, who reportedly used it to send confidential messages to his generals.

How it works:
Choose a shift value (also called a key). This is the number of positions each letter in the message will move.
Shift each letter of your message by that number forward in the alphabet.
If a letter reaches the end of the alphabet (like ‘Z’), it wraps around to the beginning (like ‘A’).

Why it’s simple:
It only shifts letters.
It doesn’t hide the structure of words or sentences.
It’s easy to crack with modern techniques

Image Encryption Tool – Console Version (No GUI)
The Image Encryption Tool is a command-line application that allows users to encrypt and decrypt images by modifying the pixel data. It runs entirely in the terminal and does not use any graphical user interface.

 How It Works
1. Image Loading
The user provides the path to an image file, which the program loads into memory. The image is then converted into a format that allows numerical manipulation of its pixel data.

2. Encryption Process
The encryption involves shifting the color values (RGB) of each pixel in the image by a fixed amount. This shift scrambles the visual content of the image, making it unrecognizable. The process ensures that color values remain within the acceptable range.

3. Decryption Process
Decryption reverses the pixel shift applied during encryption. By applying the inverse of the original shift, the image is restored to its original appearance. This only works correctly if the same shift value is used.

4. Saving Results
Both the encrypted and decrypted images are saved as new files. This allows the user to view, share, or store the transformed images separately from the original.

