# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random

first_name = input('Enter First Name: ')
last_name = input('Enter Last Name: ')
suffix = input('Enter Suffix(Jr.,Sr,II,III,etc.) if applicable else press enter: ').upper()
print('')
vowels =['a','e','i','o','u']

def user_gen():
    global first_name
    global last_name
    global suffix
    user = ''
    user_add = [
        first_name[:random.randint(1,len(first_name))],
        '_',
        last_name[:random.randint(1,len(last_name))],
        suffix[:3]
        ]
    for i in user_add:
        user += i
        
    return user.replace(' ', '_')
    
username = user_gen()
def pass_gen():
    global username
    username = username.lower()
    pass_word = ''
    for i in username:
        if i in vowels:
            i.replace(i,'')
        else:
            pass_word += i
    pass_word = list(pass_word)
    for time in range(5,10000):
        pass_word = random.sample(pass_word,len(pass_word))
        
    pass_word = ''.join(pass_word).title()
        
    return pass_word
            
incomp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',0,1,2,3,4,5,6,7,8,9,'!','@','#',
          '$','%','^','&','(',')','-','_','=','+']
    
password = pass_gen()

while len(password) < 8:
    uplow = [True,False]
    if (random.choice(uplow)):
        password += str(random.choice(incomp)).upper()
    else:
        password += str(random.choice(incomp)).lower()
    


print('Username: ' + str(username).title())
print('Temp Password: ' + str(password))