from flask import Blueprint, request, jsonify
from presentation_layer.controllers.freigth import FreightController

freight_bp = Blueprint(
    "freights",
    __name__,
    url_prefix="/freights"
)

controller = FreightController()

@freight_bp.route("/", methods=["POST"])
def create_freight():
    """
    Cria um novo frete
    ---
    tags:
      - Freights
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - customer_id
            - driver_id
            - cep_retirada
            - cep_entrega
          properties:
            customer_id:
              type: integer
              example: 1
            driver_id:
              type: integer
              example: 1
            cep_retirada:
              type: string
              example: "22730120"
            cep_entrega:
              type: string
              example: "22451900"
    responses:
      201:
        description: Frete criado e calculado com sucesso
      400:
        description: Erro de validação ou erro no cálculo de distância
    """
    data = request.get_json()
    try:
        freight = controller.create_freight(data)
        return jsonify({
            "data": {
                "id": freight.id,
                "customer_id": freight.customer_id,
                "driver_id": freight.driver_id,
                "cep_retirada": freight.cep_retirada,
                "cep_entrega": freight.cep_entrega,
                "distancia_km": freight.distancia_km,
                "valor_frete": freight.valor_frete
            }, "message": "frete criado com sucesso"
        }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@freight_bp.route("/", methods=["GET"])
def list_freights():
    """
    Lista todos os fretes realizados
    ---
    tags:
      - Freights
    responses:
      200:
        description: Lista de fretes retornada com sucesso
    """
    freights = controller.list_freights()
    return jsonify([
        {
            "data": {
                "id": f.id,
                "customer_id": f.customer_id,
                "driver_id": f.driver_id,
                "cep_retirada": f.cep_retirada,
                "cep_entrega": f.cep_entrega,
                "distancia_km": f.distancia_km,
                "valor_frete": f.valor_frete
            }, "message": "lista de fretes"
        } for f in freights
    ])

@freight_bp.route("/<int:freight_id>/", methods=["GET"])
def get_freight_by_id(freight_id):
    """
    Obtém detalhes de um frete específico
    ---
    tags:
      - Freights
    parameters:
      - name: freight_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Frete encontrado
      404:
        description: Frete não encontrado
    """
    freight = controller.get_freight_by_id(freight_id)
    if not freight:
        return jsonify({"error": "Frete não encontrado"}), 404
    return jsonify({
        "data": {
            "id": freight.id,
            "customer_id": freight.customer_id,
            "driver_id": freight.driver_id,
            "cep_retirada": freight.cep_retirada,
            "cep_entrega": freight.cep_entrega,
            "distancia_km": freight.distancia_km,
            "valor_frete": freight.valor_frete
        }, "message": "frete encontrado"
    })