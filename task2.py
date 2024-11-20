from PIL import Image
import numpy as np

# Encrypt function
def encrypt_image(image_path, encryption_key=5):
    # Open the image
    img = Image.open(image_path)
    # Convert the image to RGB (if it's not already in RGB mode)
    img = img.convert('RGB')
    
    # Get the image pixels as a numpy array
    pixels = np.array(img)
    
    # Perform pixel manipulation (e.g., add a value to each RGB component)
    encrypted_pixels = pixels + encryption_key
    encrypted_pixels = np.clip(encrypted_pixels, 0, 255)  # Ensure values are in the valid range [0, 255]
    
    # Create the encrypted image
    encrypted_image = Image.fromarray(encrypted_pixels.astype(np.uint8))
    
    return encrypted_image

# Decrypt function
def decrypt_image(encrypted_image, encryption_key=5):
    # Convert the encrypted image to a numpy array
    encrypted_pixels = np.array(encrypted_image)
    
    # Reverse the encryption (subtract the encryption key)
    decrypted_pixels = encrypted_pixels - encryption_key
    decrypted_pixels = np.clip(decrypted_pixels, 0, 255)  # Ensure values are in the valid range [0, 255]
    
    # Create the decrypted image
    decrypted_image = Image.fromarray(decrypted_pixels.astype(np.uint8))
    
    return decrypted_image

# Main function
def main():
    # User input for the image path
    image_path = input("Enter the path to the image file you want to encrypt: ")
    
    # Encrypt the image
    encrypted_image = encrypt_image(image_path, encryption_key=5)
    encrypted_image.show()  # Display the encrypted image
    
    # Save the encrypted image
    encrypted_image_path = "encrypted_image.png"
    encrypted_image.save(encrypted_image_path)
    print("Encrypted image saved as {}".format(encrypted_image_path))  # Use .format() for string formatting
    
    # Ask if the user wants to decrypt the image
    decrypt_choice = input("Do you want to decrypt the image? (y/n): ").lower()
    if decrypt_choice == 'y':
        # Decrypt the image
        decrypted_image = decrypt_image(encrypted_image, encryption_key=5)
        decrypted_image.show()  # Display the decrypted image
        
        # Save the decrypted image
        decrypted_image_path = "decrypted_image.png"
        decrypted_image.save(decrypted_image_path)
        print("Decrypted image saved as {}".format(decrypted_image_path))  # Use .format() for string formatting
    else:
        print("Decryption skipped.")

# Run the main function
if __name__ == "__main__":
    main()
