from database import db
from repository_layer.models.freight import Freight

class FreightRepository:

    def create(self, data):
        freight = Freight(**data)
        db.session.add(freight)
        db.session.commit()
        return freight

    def list_all(self):
        return Freight.query.all()

    def get_by_id(self, freight_id):
        return Freight.query.get(freight_id)
