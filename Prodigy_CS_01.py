import string

# Caesar Cipher Logic
def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    if mode == "decrypt":
        shift = -shift
    
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

# Main CLI application loop
def main():
    while True:
        print("\n--- Caesar Cipher ---")
        print("1. Encrypt Message")
        print("2. Decrypt Message")
        print("3. Clear Screen")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == '1':
            text = input("Enter message you want to encrypt: ")
            shift = input("Enter shift value: ")
            if not shift.isdigit():
                print("Shift value must be an integer.")
                continue
            shift = int(shift)
            result = caesar_cipher(text, shift, mode="encrypt")
            print("Encrypted message:", result)
        
        elif choice == '2':
            text = input("Enter message to decrypt: ")
            shift = input("Enter shift value: ")
            if not shift.isdigit():
                print("Shift value must be an integer.")
                continue
            shift = int(shift)
            result = caesar_cipher(text, shift, mode="decrypt")
            print("Decrypted message:", result)
        
        elif choice == '3':
            print("\033c", end="")  
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Please select a valid option.")

if __name__ == "__main__":
    main()
