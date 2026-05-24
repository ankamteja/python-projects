def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    if mode == 'decrypt':
        shift = -shift
        
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
            
    return result

def main():
    print("--- Caesar Cipher Program ---")
    
    while True:
        mode = input("\nDo you want to (E)ncrypt, (D)ecrypt, or (Q)uit?: ").strip().lower()
        
        if mode in ['q', 'quit']:
            print("Goodbye!")
            break
        elif mode in ['e', 'encrypt']:
            action = 'encrypt'
        elif mode in ['d', 'decrypt']:
            action = 'decrypt'
        else:
            print("Invalid choice. Please enter E, D, or Q.")
            continue
            
        message = input(f"Locate the text to {action}: ")
        
        try:
            shift = int(input("Enter the shift key (a number, e.g., 3): "))
        except ValueError:
            print("Invalid shift key. Please enter a whole number.")
            continue
            
        output = caesar_cipher(message, shift, action)
        print(f"\nResulting Text: {output}")
        print("-" * 30)

if __name__ == "__main__":
    main()