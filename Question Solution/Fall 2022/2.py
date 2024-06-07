class coffee():
    def __init__(self,name,price):
        self.name = name
        self.price  = price
        
class Magnagement:
    def __init__(self):
        self.menu =[]
        self.orders = []
        self.feedback = {}
        
    def add(self,coffee):
        self.menu.append(coffee)
    
    def displaymenu(self):
        sorted_menu = sorted(self.menu,key=lambda x:x.price)
        for c in sorted_menu:
            print(c.name,c.price)
        
    def takeOrder(self,customerName,coffee,customization):
        for c in self.menu:
            if c.name == coffee:
                orderDetails = {
                    "Customer Name": customerName,
                    "COffee":coffee,
                    "Customization": customization
                }
                self.orders.append(orderDetails)
                order_id = len(self.orders)
                print(f"Order Id: {order_id}. Order Details: {orderDetails}")
                return order_id
        print("COffee Not found")
        return None
    
    def deliver_order(self,id):
        if id>0 and id<=len(self.orders):
            order = self.orders[id-1]
            print(f"Delivering order to {order['Customer Name']}")
            print(f"Order Delivered")
        else:
            print("Invalid id")
    
    def leave_feedback(self, order_id, feedback, rating):
        if 0 < order_id <= len(self.orders):
            self.feedback[order_id] = {"feedback": feedback, "rating": rating}
            print("Feedback recorded.")
        else:
            print("Invalid order ID.")
            
s= Magnagement()
s.add(coffee("Capachino",4.5))
s.add(coffee("cap",5))
s.add(coffee("latto",10))

s.displaymenu()
id = s.takeOrder("KUddus","cap","Extra Milk")
s.deliver_order(id)
s.leave_feedback(id,"Good Coffee",4.5)

