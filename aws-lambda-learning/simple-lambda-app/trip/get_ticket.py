import json

tickets = [
    {
        "ticket": {
            "id": 123,
            "city": "Medellín",
            "state": "Antioquia",
            "country": "Colombia",
            "status": "IN_PROGRESS",
        },
        "payment": {
            "method": "CREDIT_CARD",
            "number": 4100231245124745,
            "name": "STIVEN RAMIREZ",
            "cvv": 123,
        },
    },
    {
        "ticket": {
            "id": 456,
            "city": "Bogotá",
            "state": "Cundinamarca",
            "country": "Colombia",
            "status": "FINISHED",
        },
        "payment": {
            "id": 456,
            "method": "CREDIT_CARD",
            "number": 4100789545611215,
            "name": "JULIAN RAMIREZ",
            "cvv": 456,
        },
    },
    {
        "ticket": {
            "id": 789,
            "city": "Cali",
            "state": "Valle del Cauca",
            "country": "Colombia",
            "status": "FINISHED",
        },
        "payment": {
            "id": 789,
            "method": "CREDIT_CARD",
            "number": 4100789645611235,
            "name": "SOBEIDA ARANGO",
            "cvv": 789,
        },
    },
]


def lambda_handler(event, context):
    ticket_id = event.get("pathParameters").get("ticket_id")
    ticket = list(filter(lambda t: t.get("ticket").get("id") == ticket_id, tickets))
    if not ticket:
        return {"statusCode": 404, "success": False, "data": "Ticket not found"}
    data = {**ticket[0]}
    return {"statusCode": 200, "success": True, "data": json.dumps(data)}
