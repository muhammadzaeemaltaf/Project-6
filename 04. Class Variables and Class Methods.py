class Bank:
    bank = "HBL Ltd"

    @classmethod
    def change_bank_name(cls, name):  # use 'cls' instead of 'self'
        cls.bank = name

    def showName(self):
        print(f"This is {self.bank}")


bank1 = Bank()
bank1.showName()           # Output: This is HBL Ltd

Bank.change_bank_name("Mezan")
bank1.showName()           # Output: This is Mezan
