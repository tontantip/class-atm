## create class ATM
class ATM:
## function init sign-in [name , money open account, name of bank]
    def __init__(self, name, balance, bank):
        self.name = name
        self.balance = balance
        self.bank = bank
    
## function check balance
    def check_balance(self):
        print(f"Your balance: {self.balance} THB")

## function deposit input money for deposit      
    def deposit(self, money):
        self.balance += money
        print(f'Your just deposit money: {money} THB.') 

## funtion withdraw cash input money for withdraw cash
    def draw(self, money):
        if self.balance >= money:
            self.balance -= money
            print(f'Your just drawwith money: {money} THB.')
        else:
            print(f'Your not have enough.')

## function transfer to use with function transfer money to receiver
    def transfer_to(self,name,money):
        self.balance += money
        print(f'You just transfer {money} to {self.name}')

## function transfer from sender to receiver input name of receiver and money for transfer          
    def transfer(self,name,money):
        if self.balance >= money:
            name.transfer_to(name,money)
            self.balance -= money
        else:
            print(f'Your not have enough to transfer.')

## function pay bill for pay bill from balance    
    def pay_bill(self, serial, money):
        if self.balance >= money:
            self.balance -= money
            print(f"Your just pay bill {money} to {serial}")
        else:
            print(f'Your not have enough to pay bill.')
