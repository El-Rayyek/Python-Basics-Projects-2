'''
task :
Currency converter : create a python script that takes a money with currency sign
and convert it to some other currencies , the code should be like the game we did
befor
'''

from time import sleep


class Currency_Converter():
    def __init__(self):
        while True:
        
            print("""
Welcome in our Currency converter program:
        - This is kinds of currencies we can from/to change it :
            1-USD
            2-EU
            3-EGP
            4-SAR
            5-GBP
            
            """)
            from_currency = (input("Press number of currency (from) :"))
            to_currency   = (input("Press number of currency (to)   :"))
            value         = int(input("Enter the amount of money :"))
            
            if from_currency == to_currency :
                print("Forbidden Enter The same Currency in (from/to) Entrance")
                sleep(2)
                continue
            currency_dict = {'1':'USD','2':'EU','3':'EGP','4':'SAR','5':'GBP'}
            for k,v in currency_dict.items():
                if k == from_currency:
                    for key,val in currency_dict.items():
                        if key == to_currency:
                            if int(k)<int(key):
                                z = True
                                func = f"self.{v}_{val}"
                                method = eval(func)
                                method(value,z)
                                
                            else:
                                z = False
                                func = f"self.{val}_{v}"
                                method = eval(func)
                                method(value,z)
            ExiT = input("Do you want to do another operation [y/n]? :")     
            if ExiT.lower() == 'n':
                print("Good bye  ^_^")
                break
            

    def USD_EU(self,x,z=True):
            if z is True:
                EU =  0.9993 * x
                print(f"{x} USD = {EU} EU")
            else:
                USD = 1.0007 * x
                print(f"{x} EU = {USD} USD")            
    def USD_EGP(self,x,z=True):
            if z is True:
                EGP =  19.26 * x
                print(f"{x} USD = {EGP} EGP")
            else:
                USD = 0.052 * x
                print(f"{x} EGP = {USD} USD")
    def USD_SAR(self,x,z=True):
            if z is True:
                SAR =  3.76 * x
                print(f"{x} USD = {SAR} SAR")
            else:
                USD = 0.27 * x
                print(f"{x} SAR = {USD} USD")
    def USD_GBP(self,x,z=True):
            if z is True:
                GBP =  0.87 * x
                print(f"{x} USD = {GBP} GBP")
            else:
                USD = 1.15 * x
                print(f"{x} GBP = {USD} USD")
    def EU_EGP(self,x,z=True):
            if z is True:
                EGP =  19.14 * x
                print(f"{x} EU = {EGP} EGP")
            else:
                EU = 0.0523 * x
                print(f"{x} EGP = {EU} EU")
    def EU_SAR(self,x,z=True):
            if z is True:
                SAR =  3.74 * x
                print(f"{x} EU = {SAR} SAR")
            else:
                EU = 0.2673 * x
                print(f"{x} SAR = {EU} EU")
    def EU_GBP(self,x,z=True):
            if z is True:
                GBP =  0.864587 * x
                print(f"{x} EU = {GBP} GBP")
            else:
                EU = 1.16013 * x
                print(f"{x} GBP = {EU} EU")
    def EGP_SAR(self,x,z=True):
            if z is True:
                SAR =  0.20 * x
                print(f"{x} EGP = {SAR} SAR")
            else:
                EGP = 5.13 * x
                print(f"{x} SAR = {EGP} EGP")
    def EGP_GBP(self,x,z=True):
            if z is True:
                GBP =  0.045 * x
                print(f"{x} EGP = {GBP} GBP")
            else:
                EGP = 22.12 * x
                print(f"{x} GBP = {EGP} EGP")
    def SAR_GBP(self,x,z=True):
            if z is True:
                GBP =  0.23 * x
                print(f"{x} SAR = {GBP} GBP")
            else:
                SAR = 4.31 * x
                print(f"{x} GBP = {SAR} SAR")







g = Currency_Converter()
