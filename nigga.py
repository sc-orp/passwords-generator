from os import system
try:
    from colorama import Fore
except:
    system('pip3 install -U colorama')
    print('colorama wasnt installed. i installed it for you though:)')
import random

print('\n\n\n\n\n')
letters = "abcdefghijklmnopqrstuvwxyz"
lettersUPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
use_numbers = False
use_chars = False

ask_for_numbers = input(Fore.YELLOW + '<!> Should your password contain numbers?: [Y/N] ')
if ask_for_numbers == "y".lower():
    use_numbers = True
    numbers = "0123456789"
    print(Fore.YELLOW + '<!> Ok, i will use numbers.')
else:   
    numbers = ""
    print(Fore.YELLOW + '<!> Ok, i will NOT use numbers.')
    
ask_for_chars = input(Fore.YELLOW + '<!> Should your password contain chars?: [Y/N] ')    
if ask_for_chars == "y".lower():
    use_chars = True
    chars = "[]{}()*:;/,_-@!?"
    print(Fore.YELLOW + '<!> Ok, i will use chats.')
else:   
    chars = ""
    print(Fore.YELLOW + '<!> Ok, i will NOT use chars.')    

if len(numbers) < 1:
    if not len(chars) < 1:
        all = letters + lettersUPPER + chars 
    else:
        all = letters + lettersUPPER
else:
    if not len(chars) < 1:
        all = letters + lettersUPPER + numbers + chars
    else:
        all = letters + lettersUPPER + numbers 


try:
    length = int(input(Fore.YELLOW + '<!> Length of the password? (1-50): '))
except Exception as e:
    print(e)
    
password = "".join(random.sample(all, length))    
    
print('<!> Heres your password: ' + password + '.')
