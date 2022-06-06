class ATM:
    Amount = 10000 #Your Ammount

    def Ammount(self):
        return self.Amount
    def cash_out(self,X):
        self.Amount = self.Amount - X
        return self.Amount
    def Add(self,add):
        self.Amount = self.Amount + add
        return self.Amount
    def Transfer(self,trns):
        self.Amount = self.Amount - trns
        return self.Amount



user = ATM()
while True:
    print("--------------------Welcome To Royals Group Of Bank----------------")
    sec = int(input("Enter The Pass Code\n :-"))
    if sec == 9088: #Your Bank Passcode
        while True:
            print("Welcome to farhan's Bank")
            print("1)Balance \n2)Add Money \n 3)Cash Out\n 4)Transfer Money\n 5)Quit")
            But = int(input("Enter Your Choice ="))
            if But == 5:
                break
            elif But == 1:
                print(f"Balance Update ={user.Ammount()}")
                continue
            elif But == 2:
                x = int(input("How much -"))
                print(f"Successfully Add Money {user.Ammount()} to {user.Add(x)}")
                continue
            elif But == 3:
                x = int(input("How much -"))
                print(f"Successfully cash out {user.Ammount()} to {user.Cash_out(x)}")
                continue
            elif But == 4:
                x = int(input("How much -"))
                print(f"Successfully Transfer {user.Ammount()} to {user.Transfer(x)}")
                continue
    else:
        print("Wrong Passcode")
        continue

