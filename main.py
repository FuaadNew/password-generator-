#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
finalList = []
lettercount = 1
numbercount= 1
symbolcount = 1

for letter in letters:
  if lettercount <= nr_letters:
    
     finalList += random.choice(letters) 
     lettercount+=1
  
for number in numbers:
  if numbercount <= nr_numbers:
    
     finalList += random.choice(numbers)
     numbercount+=1

for symbol in symbols:
  if symbolcount <= nr_symbols:
    
     finalList += random.choice(symbols)
     symbolcount+=1

random.shuffle(finalList)
password = ""

for item in finalList:
  password+=item
  
    
print(f"Your password is {password}")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
