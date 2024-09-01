import random
import sys
import pyperclip



for i in range(1, len(sys.argv)):

  if sys.argv[i] == "char":
    length = sys.argv[i+1] 
    pass

chars = ["a", "b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","$","*","#","@","!","%","^","&","_","+","=", "A" , "B" , "C", 
"D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
Passwrd = []
Passwrd_no_sc = []

special_chars = ["$","*","#","@","!","%","^","&","_","+","="]
nums = ["1" , "2" , "3" ,"4" , "5" , "6" , "7" , "8" , "9" , "0"]
pins = []
pinww = []


# Default password generation

def password(CHARlength):
  for i in range(int(CHARlength)):
    Passwrd.append(random.choice(chars))
    passw = "".join(Passwrd)
  print("Your password is : " + passw)
  pyperclip.copy(passw)


      
# Password function for no special characters 

def password_no_sc(CHARlength):

  for sc_char in special_chars:
    for char in chars:
      if sc_char == char:
        chars.remove(sc_char)

  for i in range(int(CHARlength)):

    Passwrd_no_sc.append(random.choice(chars)) #adds random chars to a list
    passwe = "".join(Passwrd_no_sc) 
  print("Your password is : " + passwe) # Prints the password sentence to terminal
  pyperclip.copy(passwe)
  

#  Pin generation

def pin(CHARlength):

  for i in range(int(CHARlength)):
    pins.append(random.choice(nums))
    pinster = "".join(pins)
  print(f"{pinster} Copied to clipboard successfully")
  pyperclip.copy(pinster)

  

for i in range(1, len(sys.argv)):

  if sys.argv[i] == "--pin":
    pin(length)

  if sys.argv[i] == "--pin" and "sc" in sys.argv:
    print("\"sc\" is only for password generation")

  elif sys.argv[i] == "--pass" and "sc" in sys.argv:
    password(length) 

  elif sys.argv[i] == "--pass" and "sc" not in sys.argv:
    password_no_sc(length)

  if sys.argv[i] == "sc":
    want_sc = "T"

