import secrets  
import string

#taking input
length = int(input('Enter the length of password: '))       

#def data/and fonct to make passwd and print them
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
all = lower + upper + num + symbols
def creating_pswd():
    pswrd = "".join(secrets.choice(all) for i in range(length))  
    print (pswrd)
    
    print (' ')
    
#fonct for creating multiple password at once
def paswd_main():   
    print (' ')
    num = int(input('how many password do you want to generate ?: '))
    for x in range(num):
        creating_pswd()
        

paswd_main()

#try again ?
question = str(input('Try again Y or N ?: '))

while question == "Y":
    paswd_main()
    question = str(input('Try again Y or N ?: '))
    print (' ')
   
else:
    print (' ')
    input('press ENTER to quit') 
    
    