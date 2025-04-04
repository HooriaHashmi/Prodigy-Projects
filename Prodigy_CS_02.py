from PIL import Image
import numpy as np
import os

class ImageEncryptionTool:
    def __init__(self):
        self.img = None
        self.img_array = None
        self.encrypted_array = None

    def load_image(self, file_path):
        if not os.path.exists(file_path):
            print("File not found.")
            return

        self.img = Image.open(file_path)
        self.img_array = np.array(self.img)
        print("Image loaded successfully.")

    def encrypt_image(self):
        if self.img_array is None:
            print("No image loaded.")
            return

        self.encrypted_array = (self.img_array + 50) % 256
        encrypted_img = Image.fromarray(self.encrypted_array.astype(np.uint8))
        encrypted_img.save("encrypted_image.png")
        print("Image encrypted and saved as 'encrypted_image.png'.")

    def decrypt_image(self):
        if self.encrypted_array is None:
            print("No encrypted image found.")
            return

        decrypted_array = (self.encrypted_array - 50) % 256
        decrypted_img = Image.fromarray(decrypted_array.astype(np.uint8))
        decrypted_img.save("decrypted_image.png")
        print("Image decrypted and saved as 'decrypted_image.png'.")

    def save_encrypted_image(self, file_path):
        if self.encrypted_array is None:
            print("No encrypted image to save.")
            return

        encrypted_img = Image.fromarray(self.encrypted_array.astype(np.uint8))
        encrypted_img.save(file_path)
        print(f"Encrypted image saved as '{file_path}'.")

def main():
    tool = ImageEncryptionTool()

    while True:
        print("\n--- Image Encryption Tool ---")
        print("1. Load Image")
        print("2. Encrypt Image")
        print("3. Decrypt Image")
        print("4. Save Encrypted Image")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            path = input("Enter image file path: ").strip()
            tool.load_image(path)
        elif choice == "2":
            tool.encrypt_image()
        elif choice == "3":
            tool.decrypt_image()
        elif choice == "4":
            path = input("Enter path to save encrypted image: ").strip()
            tool.save_encrypted_image(path)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
