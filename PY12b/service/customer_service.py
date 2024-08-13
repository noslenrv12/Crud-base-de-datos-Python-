from dao.customer_dao import CustomerDAO
from dto.customer_dto import CustomerDTO

class CustomerService:
    def __init__(self):
        self.customer_dao = CustomerDAO()

    def create_customer(self, customer_name, contact_name, address, city, postal_code, country):
        customer = CustomerDTO(None, customer_name, contact_name, address, city, postal_code, country)
        self.customer_dao.create_customer(customer)

    def get_customer(self, customer_id):
        return self.customer_dao.read_customer(customer_id)

    def update_customer(self, customer_id, customer_name, contact_name, address, city, postal_code, country):
        customer = CustomerDTO(customer_id, customer_name, contact_name, address, city, postal_code, country)
        self.customer_dao.update_customer(customer)

    def delete_customer(self, customer_id):
        self.customer_dao.delete_customer(customer_id)
