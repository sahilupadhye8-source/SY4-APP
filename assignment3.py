class CreditCardPayment:
    def pay(self, amount):
        print(f"Paid using Credit Card.")

class DebitCardPayment:
    def pay(self, amount):
        print(f"Paid using Debit Card.")

class UpiPayment:
    def pay(self, amount):
        print(f"Paid using UPI.")

class CashPayment:
    def pay(self, amount):
        print(f"Paid using Cash.")


class PaymentProcess:
    def __init__(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
            self.strategy.pay(amount)


print("Select Payment Method")
print("1. Credit Card")
print("2. Debit Card")
print("3. UPI")
print("4. Cash")

choice = int(input("Enter choice: "))
amount = float(input("Enter amount: "))

if choice == 1:
    strategy = CreditCard()
elif choice == 2:
    strategy = DebitCard()
elif choice == 3:
    strategy = UPI()
elif choice == 4:
    strategy = Cash()
else:
    print("Invalid Choice")
    exit()


processor = PaymentProcess(strategy)
processor.process_payment(amount)                
   

