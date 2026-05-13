class Customer:
  def __init__(self, name, contact_email):
    self.name = name
    self.contact_email = contact_email

  def send_confirmation(self, booking):
    print(f"Sending {booking} confirmation to {self.contact_email}")
  
  def __repr__(self):
    return f"Customer {self.name}"