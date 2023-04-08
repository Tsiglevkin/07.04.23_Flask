from flask.views import MethodView
from models import Session, User, Advertisement
from errors import HttpError
from flask import jsonify, request
from schema import validate, CreateUser, UpdateUser, CreateAdvertisement, UpdateAdvertisement
from hashlib import md5
from sqlalchemy.exc import IntegrityError


def get_user(user_id: int, session: Session) -> User:
    """Позволяет получить пользователя по id или возвращает ошибку"""
    user = session.get(User, user_id)
    if user is None:
        raise HttpError(404, 'user not found.')
    return user


class UserView(MethodView):  # создаем класс с методами CRUD
    """Viewset для модели пользователя"""

    def get(self, user_id: int):
        with Session() as session:
            user = get_user(user_id=user_id, session=session)
            response = jsonify({
                'id': user.id,
                'name': user.name
            })
            return response

    def post(self):
        json_data = validate(json_data=request.json, model_class=CreateUser)  # валидируем данные.

        #  делаем хэширование пароля при помощи md5
        password = json_data.get('user_pass')  # достаем пароль из json
        encode_password = password.encode()  # переводим в байты
        hashed_password = md5(encode_password).hexdigest()  # хэшируем
        json_data['user_pass'] = hashed_password  # сохраняем хэш на месте пришедшего пароля

        with Session() as session:
            new_user = User(**json_data)
            session.add(new_user)
            try:
                session.commit()
            except IntegrityError as error:
                raise HttpError(409, 'user already exists.')
            return jsonify({'id': new_user.id, 'name': new_user.name})

    def patch(self, user_id: int):
        pass

    def delete(self, user_id: int):
        pass


class AdvertisementView(MethodView):
    """Viewset для объявлений"""

    def get(self):
        pass

    def post(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass


def hello():
    return jsonify({'message': 'hello'})
