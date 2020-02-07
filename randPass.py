import random
import time
from datetime import datetime

c_l = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

s_l = [i.lower() for i in c_l]

num = ['0','1','2','3','4','5','6','7','8','9']
sym = ['@','#',"$","%","^","&","*","|","(",")","?","{","}","[","]","/","-","_"]

char = [c_l,s_l,num,sym]
pass_l =int(input("Enter the length of the password: "))
password = ""
print("-------------------Choose your password type------------------------")
time.sleep(0.4)
print("1 - Letters Symbols and Numbers")
time.sleep(0.4)
print("2 - Only letters with numbers")
time.sleep(0.4)
print("3 - Only letters")
time.sleep(0.4)
print("4 - Numbers with Symbols")
time.sleep(0.4)
print("5 - Only Numbers")
time.sleep(0.4)
print("6 - Only Symbols")
print("--------------------------------------------------------------------")
choice = int(input())
if choice==1:
    pass
elif choice==2:
    char.remove(sym)
elif choice==3:
    char.remove(sym)
    char.remove(num)
elif choice==4:
    char.remove(s_l)
    char.remove(c_l)
elif choice==5:
    char.remove(s_l)
    char.remove(c_l)
    char.remove(sym)
elif choice==6:
    char.remove(num)
    char.remove(s_l)
    char.remove(c_l)
else:
    print("Wrong Input---Literally you are blind.")

for i in range(pass_l):
    random_char_num = random.randint(0,len(char)-1)
    random_char = char[random_char_num]
    random_char_num1 = random.randint(0,len(random_char)-1)
    random_char1 = random_char[random_char_num1]
    password+=random_char1
print("--------------------------------------------------------------------")
print("Generating....")
print("\n")
time.sleep(1.2)
print("Your generated password is ",password)
print("--------------------------------------------------------------------")
file=open('password.txt','a')
m=str(datetime.now())
d=m.rsplit(".")
d=d[0]

file.write(f"{d} >>> password generated is ----->  {password}  <-----\n\n")
file.close()
print("Password stored in password.txt(at the current directory which you are running this program)")
