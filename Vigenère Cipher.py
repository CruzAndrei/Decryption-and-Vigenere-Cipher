#Import of modules
import string
import time
import pyfiglet
import colorama
from colorama import Fore
colorama.init(autoreset=True)
#Welcoming the user
print ("-" * 115)
print ("\n\t\tHello there and welcome to a program that uses Vigenère Cipher to Ciphertext a text!!\n\t\t\tCome and help me decrypt this texts and find out its true meaning!!\n")
print ("-" * 115)
enter_cont = input('\n\t\t\t\t\t\t"Enter to Continue"\n')
print ("-" * 115)
#Adding title
name = "Vigenère Cipher"
print(Fore.LIGHTGREEN_EX + name.center(115,"="))
#Alphabet characters, both uppercase and lowercase
alph_char = string.ascii_uppercase + string.ascii_lowercase
#Defining the encryption
def encrypt (text, key):
    text_alph_char = [alph_char.find(i) for i in text]
    key_alp_char= [alph_char.find(i) for i in key]
#key
    key_length = len(key)
#message
    text_length = len(text)
    cipher_text = ""
#Inspection in message and key
    for n in range (text_length) :
        letter = (text_alph_char[n] + key_alp_char[n % key_length]) % len(alph_char)
#Conjoining message and key input to cipher the text
        cipher_text += alph_char[letter]

    return cipher_text
#Defining decrytion
def decrypt(cipher, key):
    cipher_alph_char = [alph_char.find(i) for i in cipher]
    key_alph_char = [alph_char.find(i) for i in key]
#Key
    key_length = len(key)
#Ciphered text
    cipher_length = len(cipher)
#Decrypted text or original text
    plain_text = ""
#Inspection in key and ciphered text
    for n in range(cipher_length):
#Decrypting the ciphered text
        letter = (cipher_alph_char[n] - key_alph_char[n % key_length]) % len(alph_char)
        plain_text += alph_char[letter]

        return plain_text        
#message input and key input
if __name__ == "__main__":

    text = input ("Message: ")
    key = input ("Key: ")

    cipher = encrypt(text,key)
    plaintext = decrypt(cipher,key)    
#print of message, and key input and, the ciphered text and decrypted text
print ("=" * 115,"\n")
print (Fore.GREEN + pyfiglet.figlet_format("Message: " + text, font = 'digital'),'\n')
time.sleep(3)
print (Fore.WHITE + pyfiglet.figlet_format("Key: " + key, font = 'digital'),'\n')
time.sleep(3)
print (Fore.BLUE + pyfiglet.figlet_format("Ciphertext: " + cipher, font = 'digital'),'\n')
time.sleep(3)
print (Fore.MAGENTA + pyfiglet.figlet_format("Message: " + plaintext, font = 'digital'),'\n')

