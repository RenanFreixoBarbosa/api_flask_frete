from repository_layer.repositories.customer import CustomerRepository

class CustomerController:

    def __init__(self):
        self.repository = CustomerRepository()

    def create_customer(self, data):
        return self.repository.create(data)

    def list_customers(self):
        return self.repository.list_all()
    
    def get_customer_by_id(self, customer_id):
        return self.repository.get_by_id(customer_id)
    
    def delete_customer_by_id(self, customer_id):
        return self.repository.delete_by_id(customer_id)
    
    def update_customer_by_id(self, customer_id, data):
        return self.repository.update_by_id(customer_id, data)