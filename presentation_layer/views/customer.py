from flask import Blueprint, request, jsonify
from presentation_layer.controllers.customer import CustomerController

customer_bp = Blueprint("customers", __name__, url_prefix="/customers")
controller = CustomerController()

@customer_bp.route("/", methods=["POST"])
def create_customer():
    """
    Cria um novo cliente
    ---
    tags:
      - Customers
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
              example: "João Silva"
            email:
              type: string
              example: "joao@email.com"
            telefone:
              type: string
              example: "11999999999"
    responses:
      201:
        description: Cliente criado com sucesso
    """
    data = request.get_json()
    customer = controller.create_customer(data)
    return jsonify({
        "data": {
            "id": customer.id,
            "nome": customer.nome,
            "email": customer.email,
            "telefone": customer.telefone
        }, "message": "customer criado com sucesso"
    }), 201

@customer_bp.route("/", methods=["GET"])
def list_customers():
    """
    Lista todos os clientes
    ---
    tags:
      - Customers
    responses:
      200:
        description: Lista de clientes retornada com sucesso
    """
    customers = controller.list_customers()
    return jsonify([
        {
            "data": {
                "id": c.id, "nome": c.nome, "email": c.email, "telefone": c.telefone
            }, "message": "lista de customers"
        } for c in customers
    ])

@customer_bp.route("/<int:customer_id>/", methods=["GET"])
def get_customer_by_id(customer_id):
    """
    Busca cliente por ID
    ---
    tags:
      - Customers
    parameters:
      - name: customer_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Cliente encontrado
      404:
        description: Cliente não encontrado
    """
    customer = controller.get_customer_by_id(customer_id)
    if isinstance(customer, str):
        return jsonify({"message": customer}), 404
    if not customer:
        return jsonify({"message": "customer não encontrado"}), 200
    
    return jsonify({
        "data": {
            "id": customer.id, "nome": customer.nome, "email": customer.email, "telefone": customer.telefone
        }, "message": "customer encontrado"
    })

@customer_bp.route("/<int:customer_id>/", methods=["DELETE"])
def delete_customer_by_id(customer_id):
    """
    Deleta um cliente
    ---
    tags:
      - Customers
    parameters:
      - name: customer_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Cliente deletado com sucesso
      404:
        description: Cliente não encontrado
    """
    result = controller.delete_customer_by_id(customer_id)
    if isinstance(result, str):
        return jsonify({"message": result}), 404
    return jsonify({
        "data": {
            "id": result.id, "nome": result.nome, "email": result.email, "telefone": result.telefone
        }, "message": "customer deletado com sucesso"
    })

@customer_bp.route("/<int:customer_id>/", methods=["PUT"])
def update_customer_by_id(customer_id):
    """
    Atualiza um cliente
    ---
    tags:
      - Customers
    parameters:
      - name: customer_id
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
            email: {type: string}
            telefone: {type: string}
    responses:
      200:
        description: Cliente atualizado com sucesso
      404:
        description: Cliente não encontrado
    """
    data = request.get_json()
    customer = controller.update_customer_by_id(customer_id, data)
    if isinstance(customer, str):
        return jsonify({"message": customer}), 404
    return jsonify({
        "data": {
            "id": customer.id, "nome": customer.nome, "email": customer.email, "telefone": customer.telefone
        }, "message": "customer atualizado com sucesso"
    })