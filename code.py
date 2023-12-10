import random

chars = ["a", "b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","$","*","#","@","!","%","^","&","_","+","=", "A" , "B" , "C", 
"D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
Passwrd = []
Passwrd_no_sc = []

special_chars = ["$","*","#","@","!","%","^","&","_","+","="]
nums = ["1" , "2" , "3" ,"4" , "5" , "6" , "7" , "8" , "9" , "0"]
pins = []
pinww = []

pas_type = input("Do you want a pin or password Pin/Password: ")
if pas_type.upper()=="PASSWORD" or pas_type.upper()=="PWD":
  want_sc = input(str("Do you want special characters? True/False : "))



# If User Does Want Special Characters
if pas_type.upper()=="PASSWORD" or pas_type.upper()=="PWD":
  length = input("How long do you want your password to be ?: ")
  if want_sc == "T" or want_sc == "True" or want_sc == "t":
      def password():
        for i in range(int(length)):
          Passwrd.append(random.choice(chars))
          passw = "".join(Passwrd)
        print("Your password is : " + passw)
      password() 

# If User Doesn't Want Special Characters
  if want_sc == "F" or want_sc == "False" or want_sc == "f":
    for sc_char in special_chars:
      for char in chars:
        if sc_char == char:
          chars.remove(sc_char)
          
# It Runs This Function based on the if statement above
    def password_no_sc():
      for i in range(int(length)): 
        Passwrd_no_sc.append(random.choice(chars)) #adds random chars to a list
        passwe = "".join(Passwrd_no_sc) 
      print("Your password is : " + passwe) # Prints the password sentence to terminal
      
    password_no_sc()


  


if pas_type.upper()=="PIN": 
  length = input("How long do you want your pin to be ?: ")
  def pin():
    for i in range(int(length)):
      pins.append(random.choice(nums))
      pinster = "".join(pins)
    print("Your pin is : " + pinster)

  pin()
  

