import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m',
         'n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M',
         'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','&','*','+']
print("Welcome to Password generator!")
n_letters=int(input("How many letters you want in your password:"))
n_numbers=int(input("How many numbers you want in your password:"))
n_symbols=int(input("How many symbols you want in your password:"))
password_list=[]
for i in range (n_letters):
    char=random.choice(letters)
    password_list.append(char)
for i in range (n_numbers):
    char=random.choice(numbers)
    password_list.append(char)
for i in range (n_symbols):
    char=random.choice(symbols)
    password_list.append(char)
print(password_list)
random.shuffle(password_list)
print(password_list)
password=""
for i in password_list:
    password += i
print("password:",password)




