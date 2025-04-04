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

This Python program creates a simple Password Complexity Checker using the Tkinter library for a graphical user interface (GUI). Its purpose is to evaluate a password entered by the user and check if it meets specific strength criteria. If the password fails any of these checks, the program provides feedback to guide the user in improving their password.

Key Features and Functionality:
Password Input:

The user is prompted to enter a password into a password entry field. The password is masked by default (using the show="*" option) to keep it secure while typing.

Check Password Strength:

When the user clicks the Check Password Strength button, the program evaluates the password based on a series of conditions and criteria. It checks for:

Minimum Length: The password must be at least 8 characters long.

Uppercase Letter: The password must contain at least one uppercase letter (A-Z).

Lowercase Letter: The password must contain at least one lowercase letter (a-z).

Digit: The password must contain at least one numeric digit (0-9).

Special Character: The password should ideally contain at least one special character (like !@#$%^&*()).

Feedback Messages:

Depending on the password's complexity, the program provides feedback:

Red text is used for errors, indicating what the password is missing (e.g., "Password must contain at least one uppercase letter").

Orange text is used to indicate moderate feedback (e.g., missing special characters).

Green text is used for a strong password, indicating success (e.g., "Your password is strong!").

User-Friendly Interface:

The GUI is built with Tkinter, offering an easy-to-use interface with clear instructions, input fields, and results.

The window is sized to be comfortable and responsive, with a title that reflects the tool's purpose: "Password Complexity Checker".

