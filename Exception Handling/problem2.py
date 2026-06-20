'''
An ecommerce company wants to validate 
order processing 
The system should accept:
1.product stock 
2.payment status 
3.delivery address 
raise exception if :
1.stock unavailable 
2.payment failed 
3.address is empty
if all validation pass:
print("Order succesfully placed") 
'''
class OutOfStockError(Exception):
    pass
class PaymentFailedError(Exception):
    pass
class InvalidAddressError(Exception):
    pass
class Order:
    def __init__(
        self,
        stock,
        payment_status,
        address
        ):
        self.stock = stock
        self.payment_status = payment_status
        self.address = address  
    def place_order(self):
        try:
            if self.stock <=0:
                raise OutOfStockError("Product unavailable") 
            if not self.payment_status:
                raise PaymentFailedError("Payment is failed")
            if self.address.strip() == "" :
                raise InvalidAddressError("Address cannot be empty")
            print("Order placed successfully") 
        except OutOfStockError as e:
            print(e)
        except PaymentFailedError as e:
            print(e)
        except InvalidAddressError as e:
            print(e)   
stock = int(input("Enter stock:"))
payment = input("Payment successful (Yes/NO):").lower()
address = input("enter address")

payment_status = payment == "yes"
obj = Order(
    stock,
    payment_status,
    address
)
obj.place_order()
            