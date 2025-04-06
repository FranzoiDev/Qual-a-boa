from functools import wraps
from flask import request, jsonify
from marshmallow import ValidationError

def validate_schema(schema):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                data = request.get_json()
                schema.load(data)
                return f(*args, **kwargs)
            except ValidationError as err:
                return jsonify({"message": "Validation error", "errors": err.messages}), 400
        return decorated_function
    return decorator 