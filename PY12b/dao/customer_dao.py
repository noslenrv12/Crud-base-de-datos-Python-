from dto.customer_dto import CustomerDTO
from dao.db_connection import DBConnection

class CustomerDAO:
    def __init__(self):
        self.connection = DBConnection().connect()
        if self.connection is None:
            raise Exception("Failed to connect to the database.")

    def create_customer(self, customer):
        cursor = self.connection.cursor()
        cursor.callproc("InsertCustomer", (
            customer.customer_name, 
            customer.contact_name, 
            customer.address, 
            customer.city, 
            customer.postal_code, 
            customer.country
        ))
        self.connection.commit()
        cursor.close()

    def read_customer(self, customer_id):
        cursor = self.connection.cursor()
        cursor.callproc("ReadCustomer", (customer_id,))
        
        # Assuming the procedure returns a single result set
        customer = None
        for result in cursor.stored_results():
            row = result.fetchone()
            if row:
                customer = CustomerDTO(*row)
        
        cursor.close()
        return customer

    def update_customer(self, customer):
        cursor = self.connection.cursor()
        cursor.callproc("UpdateCustomer", (
            customer.customer_id, 
            customer.customer_name, 
            customer.contact_name, 
            customer.address, 
            customer.city, 
            customer.postal_code, 
            customer.country
        ))
        self.connection.commit()
        cursor.close()

    def delete_customer(self, customer_id):
        cursor = self.connection.cursor()
        cursor.callproc("DeleteCustomer", (customer_id,))
        self.connection.commit()
        cursor.close()
