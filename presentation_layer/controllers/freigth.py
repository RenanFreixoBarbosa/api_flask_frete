from repository_layer.repositories.freight import FreightRepository
from repository_layer.repositories.customer import CustomerRepository
from repository_layer.repositories.driver import DriverRepository
from services_layer.distance import DistanceService

class FreightController:

    def __init__(self):
        self.freight_repository = FreightRepository()
        self.customer_repository = CustomerRepository()
        self.driver_repository = DriverRepository()
        self.distance_service = DistanceService()
        self.valor_por_km = 5.00      # Valor fixo por km

    def create_freight(self, data):
        customer = self.customer_repository.get_by_id(data["customer_id"])
        driver = self.driver_repository.get_by_id(data["driver_id"])

        if not customer or not driver:
            raise ValueError("Cliente ou motorista não encontrado")

        

        #calcular a distância utilizando a API Externa chamando a camada de serviço (service layer) - OMITIDO
        distancia_km = self.distance_service.get_distance(data["cep_retirada"], data["cep_entrega"])

        #criar um método para calcular o valor do frete baseado na distância e no valor por km do motorista
        valor_frete = distancia_km * self.valor_por_km  # Exemplo: valor fixo por km

        freight_data = {
            "customer_id": customer.id,
            "driver_id": driver.id,
            "cep_retirada": data["cep_retirada"],
            "cep_entrega": data["cep_entrega"],
            "distancia_km": distancia_km,
            "valor_frete": valor_frete
        }

        return self.freight_repository.create(freight_data)

    def list_freights(self):
        return self.freight_repository.list_all()
    
    def get_freight_by_id(self, freight_id):
        return self.freight_repository.get_by_id(freight_id)