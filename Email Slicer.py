'''
task :
Build an email slicer : create a function that takes an email as input and retrieve
the username and domain of the email
'''
import re

def slicer(email):
    email = email.split('@')
    user_name = email[0]
    domain = email[1]
    print(f"The user name is {user_name} and The domain is {domain}")




email = input("Enter your Email Please :")



if re.search("@.+[.]com$",email):
        slicer(email)

else:
    print("Sorry,Enter valid Email")        
 


