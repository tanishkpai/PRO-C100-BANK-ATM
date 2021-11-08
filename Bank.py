class Atm:
    def __init__(self,account,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
        self.Account = account
     

    def check_balance(self):
        print("Your balance is :-")
        print("Rupees = 1,00,000")
    
    def withdrawl1(self,Rupees):
        new_amount = 100 - Rupees
        print("You have withdrawn amount "+str(Rupees) + ". Your remaining balance is "+ str(new_amount))


def main():
    print("Welcome to Gringotts Bank! The wizards and witchs bank")
    Account = input("Please enter your acount image or number: ")
    Card_number = input("Insert your key number:- ")
    pin_number  = input("Enter your pin number:- ")

    new_user =  Atm(Account,Card_number,pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.Withdrawl")
    activity = int(input("Enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        print("1. Add Rupees")
        choose = int(input("1. Add Rupees"))
        if (choose == 1):
           Rupees = int(input("Enter the amount:- "))
           new_user.withdrawl1(Rupees)
    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()