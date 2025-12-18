from database import db

class Driver(db.Model):
    __tablename__ = "drivers"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    veiculo = db.Column(db.String(100), nullable=False)
    placa = db.Column(db.String(20), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    servico_ativo = db.Column(db.Boolean, default=True, nullable=False)
