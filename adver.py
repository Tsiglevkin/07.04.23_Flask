from flask import Flask, jsonify
from flask.views import MethodView
from models import Session, User

application = Flask('app')  # создаем экземпляр класса


class HttpError(Exception):
    """Этот класс нужен для формирования читаемых ошибок"""

    def __init__(self, status_code: int, message: str | list | dict):
        """Этот метод позволяет передавать полезную информацию об ошибке"""
        self.status_code = status_code
        self.message = message


@application.errorhandler(HttpError)
def error_handler(error: HttpError):
    """Метод генерирует ответ для пользователя на основании ошибки"""
    response = jsonify({'status': 'error', 'message': error.message})
    response.status_code = error.status_code
    return response


def get_user(user_id: int, session: Session) -> User:
    """Позволяет получить пользователя по id или возвращает ошибку"""
    user = session.get(User, user_id)
    if user is None:
        raise HttpError(404, 'user not found.')
    return user


class UserView(MethodView):  # создаем класс с методами CRUD

    def get(self, user_id: int):
        with Session() as session:
            user = get_user(user_id=user_id, session=session)
            response = jsonify({
                'id': user.id,
                'name': user.name
            })
            return response

    def post(self):
        pass

    def patch(self, user_id: int):
        pass

    def delete(self, user_id: int):
        pass


application.add_url_rule(
    url='/users/<int:user_id>/',
    view_func=UserView.as_view('current_user'),
    methods=['GET', 'PATCH', 'DELETE']
)
application.add_url_rule('/users/', view_func=UserView.as_view('new_user'), methods=['POST'])


if __name__ == '__main__':
    application.run()



