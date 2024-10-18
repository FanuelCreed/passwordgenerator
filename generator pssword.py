import random
letter = ['A','B','c','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','v','w','x','y','z']
number = [0,1,2,3,4,5,6,7,8,9]
symbol =['!','@','#','$','$','&','-']

print("welcome to password generaation")

num_letter = int(input("How many letters do you want..."))
num_number = int(input("How many numbers do you want..."))
num_symbol = int(input("How many symbol do you want..."))

password_letters = random.sample(letter, num_letter)
password_number = random.sample(number, num_number)
password_symbol = random.sample(symbol, num_symbol)
# pssword = random.sample(letter, num_letter + number, num_letter + symbol, num_symbol)

password_list = num_letter + num_number + num_symbol
random.shuffle=(int(len(password_list)))
print (Generated, password)