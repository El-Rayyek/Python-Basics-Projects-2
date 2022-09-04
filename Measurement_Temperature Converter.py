'''
task :
Make a temperature/measurement converter. Write a script that can convert
Fahrenheit to Celcius and back, or inches to centimeters and back, etc
'''

from lib2to3.pygram import pattern_symbols


class Converter():
    def __init__(self):
        print('''
Welcome in our Converter Program
    We can convert :
            1-Temperature (Fahrenheit to Celcius) or back.
            2-Measurement (Inches to Centimeters) or back.
        ''')
        inpt = int(input("Press 1 or 2 to choose kind of converter :"))
        if inpt == 1:
            inpt1 = int(input("""
Press (1) to convert Fahrenheit to Celcius.
press (2) to convert Celcius to Fahrenhiet."""))
            if inpt1 == 1:
                degree = int(input("Enter Fahrenheit Degree :"))
                self.fah_cel(degree)
            else:
                degree = int(input("Enter Celcius Degree :"))
                self.cel_fah(degree)

        if inpt == 2:
            inpt2 = int(input("""
Press (1) to convert Inches to Centimeters.
press (2) to convert Centimeters to Inches."""))
            if inpt2 == 1:
                degree = int(input("Enter Inches Degree :"))
                self.inch_cent(degree)
            else:
                degree = int(input("Enter Centimeters Degree :"))
                self.cent_inch(degree)
    
    def fah_cel(self,degree):
        cel =  5/9*(degree-32)
        print("{:.2f}".format(cel) , "Celcius")
    def cel_fah(self,degree):
        fah = degree * (9/5) + 32
        print("{:.2f}".format(fah), "Fahrenheit")
    def inch_cent(self,degree):
        inch = degree * 2.54
        print("{:.2f}".format(inch) , "Inches")
    def cent_inch(self,degree):
        cent = degree / 2.54
        print("{:.2f}".format(cent),"Centimeters")


converter = Converter()
