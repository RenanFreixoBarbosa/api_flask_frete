import requests

class DistanceService:
    BASE_URL = "http://calc:5001/distance/"

    def get_distance(self,cep_origem,cep_destino) -> float:
        
        payload = {
            "cep_origem": cep_origem,
            "cep_destino": cep_destino
        }

        response = requests.post(self.BASE_URL, json=payload)

        if response.status_code != 200:
            raise ValueError("Não foi possível obter a distância")

        data = response.json()
        return data["distancia_km"]
