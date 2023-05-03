#Welcoming the user
print ("=" * 115)
print ("\n\t\tHello there and welcome! This is a program to decode specific symbols into a character.\n\t\t\t\t\tCome and help me decrypt this texts\n")
print ("=" * 115)
#Import of modules
import colorama
import pyfiglet
from colorama import Fore
colorama.init(autoreset=True)
enter_cont = input('\n\t\t\t\t\t  "Enter to Continue"\n')
print ("=" * 115)
#Asking user for inputs to their data
input_str = input("\nType in your data here: ")
output_str = ""
#Table of values
print(Fore.BLUE + "Symbol *".ljust(105,"-") + "Vowel a")
print(Fore.MAGENTA + "Symbol &".ljust(105,"-") + "Vowel e")
print(Fore.BLUE + "Symbol #".ljust(105,"-") + "Vowel i")
print(Fore.MAGENTA + "Symbol +".ljust(105,"-") + "Vowel o")
print(Fore.BLUE + "Symbol !".ljust(105,"-") + "Vowel u")
print ("=" * 115)
#Inspection of each character
for i in range(len(input_str)):
#Substition for * is working
    if input_str[i] == "*":
        output_str += "a"
#Subtitution for & is working
    elif input_str[i] == "&":
        output_str += "e"
#Subtitution for # is working
    elif input_str[i] == "#":
        output_str += "i"
#Subtitution for + is working
    elif input_str[i] == "+":
        output_str += "o"
#Subtitution for ! is working
    elif input_str[i] == "!":
        output_str += "u"        
    else:
        output_str += input_str[i]
#Print output is working
print(pyfiglet.figlet_format(output_str, font = "bubble" ))