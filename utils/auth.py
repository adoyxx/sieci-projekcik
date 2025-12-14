from functools import wraps
from flask import jsonify, request
import config
from typing import Callable


def _check_auth(username: str, password: str) -> bool:
    return username == config.AUTH_USERNAME and password == config.AUTH_PASSWORD


def requires_auth(f: Callable):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not _check_auth(auth.username, auth.password):
            return jsonify({"message": "Authentication required"}), 401
        return f(*args, **kwargs)

    return decorated
