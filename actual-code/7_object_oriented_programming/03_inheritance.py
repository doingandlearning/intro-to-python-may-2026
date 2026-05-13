class Customer:
  def __init__(self, name, contact_email):
    self.name = name
    self.contact_email = contact_email

  def send_confirmation(self, booking):
    print(f"Sending {booking} confirmation to {self.contact_email}")
  
  def __repr__(self):
    return f"Customer {self.name}"

class PAndO(Customer):
  def __init__(self, name, contact_email, internal_contact):
    super().__init__(name, contact_email)
    self.internal_contact = internal_contact

  def send_confirmation(self, booking):
    print(f"Get sign off from {self.internal_contact}")
    print(f"Send confirmation to {self.contact_email}")


cust1 = Customer("B&Q", "help@bandq.com")
cust2 = PAndO("P&O", "help@pando.com", "jeff@inhere.com")

cust1.send_confirmation("Some booking")
cust2.send_confirmation("Some booking")
print(cust1, cust2)