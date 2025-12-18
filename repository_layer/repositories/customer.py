from database import db
from repository_layer.models.customer import Customer

class CustomerRepository:

    def create(self, data):
        customer = Customer(**data)
        db.session.add(customer)
        db.session.commit()
        return customer

    def list_all(self):
        return Customer.query.all()

    def get_by_id(self, customer_id):
        return Customer.query.get(customer_id)
    
    def delete_by_id(self, customer_id):
        customer = Customer.query.get(customer_id)
        if customer:
            db.session.delete(customer)
            db.session.commit()
            return customer
        return "customer não encontrado"
    
    def update_by_id(self, customer_id, data):
        customer = Customer.query.get(customer_id)
        if customer:
            for key, value in data.items():
                setattr(customer, key, value)
            db.session.commit()
            return customer
        return "customer não encontrado"