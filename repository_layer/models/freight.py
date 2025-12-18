from database import db

class Freight(db.Model):
    __tablename__ = "freights"

    id = db.Column(db.Integer, primary_key=True)

    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    driver_id = db.Column(db.Integer, db.ForeignKey("drivers.id"), nullable=False)

    cep_retirada = db.Column(db.String(10), nullable=False)
    cep_entrega = db.Column(db.String(10), nullable=False)

    distancia_km = db.Column(db.Float, nullable=False)
    valor_frete = db.Column(db.Float, nullable=False)
