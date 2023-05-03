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
#Conjoining message and key input to cipher the text
#Defining decrytion
#Inspection in key and ciphered text
#Decrypting the ciphered text
#message input and key input
#print of message, and key input and, the ciphered text and decrypted text