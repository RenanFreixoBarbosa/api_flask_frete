from flask import Blueprint, request, jsonify
from presentation_layer.controllers.driver import DriverController

driver_bp = Blueprint(
    "drivers",
    __name__,
    url_prefix="/drivers"
)

controller = DriverController()

@driver_bp.route("/", methods=["POST"])
def create_driver():
    """
    Cria um novo motorista
    ---
    tags:
      - Drivers
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
              example: "Carlos Andrade"
            veiculo:
              type: string
              example: "Caminhão Scania"
            placa:
              type: string
              example: "ABC-1234"
            telefone:
              type: string
              example: "(21)91234-5678"
            servico_ativo:
              type: boolean
              example: false
    responses:
      201:
        description: Motorista criado com sucesso
    """
    data = request.get_json()
    driver = controller.create_driver(data)
    return jsonify({
        "data": {
            "id": driver.id,
            "nome": driver.nome,
            "veiculo": driver.veiculo,
            "placa": driver.placa,
        },"message": "driver criado com sucesso"
    }), 201

@driver_bp.route("/", methods=["GET"])
def list_drivers():
    """
    Lista todos os motoristas
    ---
    tags:
      - Drivers
    responses:
      200:
        description: Lista de motoristas retornada com sucesso
    """
    drivers = controller.list_drivers()
    return jsonify([
        {
            "data": {
                "id": d.id,
                "nome": d.nome,
                "veiculo": d.veiculo,
                "placa": d.placa,
            },"message": "lista de drivers" 
        }
        for d in drivers
    ])

@driver_bp.route("/<int:driver_id>/", methods=["GET"])
def get_driver_by_id(driver_id):
    """
    Busca motorista por ID
    ---
    tags:
      - Drivers
    parameters:
      - name: driver_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Motorista encontrado
      404:
        description: Motorista não encontrado
    """
    driver = controller.get_driver_by_id(driver_id)
    if isinstance(driver, str):
        return jsonify({"message": driver}), 404

    return jsonify({
        "data": {
            "id": driver.id,
            "nome": driver.nome,
            "veiculo": driver.veiculo,
            "placa": driver.placa,
        },"message": "driver encontrado"
    })

@driver_bp.route("/<int:driver_id>/", methods=["DELETE"])
def delete_driver_by_id(driver_id):
    """
    Remove um motorista
    ---
    tags:
      - Drivers
    parameters:
      - name: driver_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Motorista deletado com sucesso
      404:
        description: Motorista não encontrado
    """
    result = controller.delete_driver_by_id(driver_id)
    if isinstance(result, str):
        return jsonify({"message": result}), 404

    return jsonify({
        "data": {
            "id": result.id,
            "nome": result.nome,
            "veiculo": result.veiculo,
            "placa": result.placa,
        },"message": "driver deletado com sucesso"  
    })

@driver_bp.route("/<int:driver_id>/", methods=["PUT"])
def update_driver_by_id(driver_id):
    """
    Atualiza dados do motorista
    ---
    tags:
      - Drivers
    parameters:
      - name: driver_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            nome: {type: string}
            veiculo: {type: string}
            placa: {type: string}
    responses:
      200:
        description: Motorista atualizado com sucesso
      404:
        description: Motorista não encontrado
    """
    data = request.get_json()
    driver = controller.update_driver_by_id(driver_id, data)
    if isinstance(driver, str):
        return jsonify({"message": driver}), 404

    return jsonify({
        "data": {
            "id": driver.id,
            "nome": driver.nome,
            "veiculo": driver.veiculo,
            "placa": driver.placa,
        },"message": "driver atualizado com sucesso"
    })