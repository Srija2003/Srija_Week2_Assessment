class payment:
    def process_payment(self,message):
        print(f"{message}")
        
    def CreditCard(self,message,credit):
        print(f"{message},{credit}")
        
    def Paypal_payment(self,message,paypal):
        print(f"{message},{paypal}")
    
    def bitcoin_payment(Self,message,bitcoin):
        print(f"{message},{bitcoin}")
p=payment()
p.process_payment("payment")
p.CreditCard("payment method","credit")
p.Paypal_payment("payment method","paypal")
p.bitcoin_payment("payment method","bitcoin")