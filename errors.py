from flask import jsonify


class HttpError(Exception):
    """Этот класс нужен для формирования читаемых ошибок"""

    def __init__(self, status_code: int, message: str | list | dict):
        """Этот метод позволяет передавать полезную информацию об ошибке"""

        self.status_code = status_code
        self.message = message


def error_handler(error: HttpError):
    """Метод генерирует ответ для пользователя на основании ошибки"""

    response = jsonify({'status': 'error', 'message': error.message})
    response.status_code = error.status_code
    return response



