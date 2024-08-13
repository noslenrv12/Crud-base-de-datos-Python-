class CustomerDTO:
    def __init__(self, customer_id=None, customer_name=None, contact_name=None, address=None, city=None, postal_code=None, country=None):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.contact_name = contact_name
        self.address = address
        self.city = city
        self.postal_code = postal_code
        self.country = country
