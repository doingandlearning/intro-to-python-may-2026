from . import Customer

class PAndO(Customer):
  def __init__(self, name, contact_email, internal_contact):
    super().__init__(name, contact_email)
    self.internal_contact = internal_contact

  def send_confirmation(self, booking):
    print(f"Get sign off from {self.internal_contact}")
    print(f"Send confirmation to {self.contact_email}")
