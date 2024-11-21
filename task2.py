
from colorama import Fore
from PIL import Image
import numpy as np


def XOREncrypt(path, key):
    try:
        XORimg = Image.open(path)
        image_array = np.array(XORimg)
        for index, values in enumerate(image_array):
            image_array[index] = values ^ key

        XOR_enc_img = Image.fromarray(image_array)
        XOR_enc_img.save("XOREncrypt.png")
        print(Fore.GREEN + "Encryption Successfull!")
        print(Fore.GREEN + "Exiting...!")
        
    except Exception:
        print(Fore.RED + "Error caught : ", Exception.__name__)
        print(Fore.RED + "Exiting...")
        

def XORDecrypt(path, key):
    try:
        XOR_img = Image.open(path)
        img_array = np.array(XOR_img)
        for index, values in enumerate(img_array):
            img_array[index] = values ^ key

        XOR_dec_img = Image.fromarray(img_array)
        XOR_dec_img.save("XORDecrypt.png")

        print(Fore.GREEN + "Encryption Done...")
        print(Fore.GREEN + "Exiting...")
        
    except Exception:
        print(Fore.RED + "Error caught : ", Exception.__name__)
        print(Fore.RED + "Exiting...")

def encrypt_image(path, key):
    try:
        img = Image.open(path)
        pixel = np.array(img)
        
        for index, value in enumerate(pixel):
            pixel[index] = value + 256 - (key + 1)
        enc_img = Image.fromarray(pixel)
        enc_img.save("enc_image.png")
        print(Fore.GREEN + "Encryption Successfull!")
        print(Fore.GREEN + "Exiting")
    except Exception:
        print(Fore.RED + "Error: ", Exception.__name__)
        print(Fore.RED + "Exiting...")
        
               

def decrypt_image(path, key):
    try:
        enc = Image.open(path)
        encPixel = np.array(enc)
        for index, value in enumerate(encPixel):
            encPixel[index] = value + 256 + (key + 1)
        dec_img = Image.fromarray(encPixel)
        dec_img.save("dec_image.png")
        print(Fore.GREEN + "Decryption Successfull!")
        print(Fore.GREEN + "Exiting...")
        
    except Exception:
        print(Fore.RED + "Error caught : ", Exception.__name__)
        print(Fore.RED + "Exiting...")
        

filePath = input('Enter path of Image : ')
key = int(input('Enter Key for encryption of Image : '))
print('The path of file : ', filePath)
print('Key for encryption : ', key)

while True:
    print("\nPixel Manipulator for Image Encryption/Decryption")
    print("\n1. Encryption")
    print("\n2. Decryption")
    choice = int(input("Enter the choice: "))
    
    if choice == 1:
        print("\n 1. Pixel Manipulation")
        print("\n 2. Image Encryption")
        choice1 = int(input("Enter the choice: "))
        
        if choice1 == 1:
            encrypt_image(filePath, key)
            break
        
        elif choice1 == 2:
            XOREncrypt(filePath, key)
            break
        else:
            print(Fore.YELLOW + "Invalid option!!")
            print(Fore.YELLOW + "Exiting...")
            break
        
    elif choice == 2:
        print("\n 1. Pixel Manipulation")
        print("\n 2. Image Decryption(Only applicable on XOR Encrypted image. And the key should be same as that of encryption.)")
        choice2 = int(input("Enter the choice: "))
        
        if choice2 == 1:
            decrypt_image(filePath, key)
            break
        elif choice2 == 2:
            XORDecrypt(filePath, key)
            break
        else:
            print(Fore.YELLOW + "Invalid option!!")
            print(Fore.YELLOW + "Exiting...")

    else:
        print(Fore.YELLOW + "\nInvalid option.")
        print(Fore.RED + "Exiting...")
        break
