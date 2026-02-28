#Order Status
"""
    Pending  processing   Shipped    Delivered    Cancelled
        1       2           3           4           5

"""
from enum import Enum

class orderStatus(Enum):
    PENDING=1
    PROCESSING=2
    SHIPPED=3
    DELIVERED=4
    CANCLLED=5

class Order:
    def __init__(self,order_id,customer_name):
        self.order_id=order_id
        self.customer_name=customer_name
        self.status=orderStatus.PENDING

    def update_status(self,New_status):
        if isinstance(New_status,orderStatus):
            self.status=New_status
            print(f"Order {self.order_id} update to {self.status.name}")
        else:
            print("invalid Status")
    
    def display(self):
        print(f"order Id: {self.order_id}")
        print(f"Customer: {self.customer_name}")
        print(f"Status: {self.status.name}")

order1=Order(1001,"Adam")
order1.display()
order1.update_status(orderStatus.SHIPPED)