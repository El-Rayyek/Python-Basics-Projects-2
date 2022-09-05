'''
task :
Random Password Generator : create a function that generates a random
password , the password must be +7 letters , should contain numbers , upper case
letter , small letter and _ only'''
import random
import string


def random_pass():
    pass_list = list()

    count_of_pass = random.randrange(8,30)
    for x in range(count_of_pass):
        x = random.choice(string.ascii_letters)
        pass_list.append(x)

    for i in range(len(pass_list)//2):
        rand_num = random.randrange(0,len(pass_list))
        pass_list[rand_num] = str(random.randrange(0,9))

    for i in range(len(pass_list)//4):
        rand_ = random.randrange(0,len(pass_list))
        pass_list[rand_] = '_'



    print( "We generate this random password ==> " +"".join(pass_list))


while True:
    random_pass()
    ExiT = input("Do you want to run again [y/n] ? :")
    if ExiT.lower() == 'n':
        break