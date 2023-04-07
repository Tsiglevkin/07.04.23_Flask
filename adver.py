from flask import Flask
from my_views import UserView


application = Flask('app')  # создаем экземпляр класса


application.add_url_rule(  # прописывает роуты для методов
    url='/users/<int:user_id>/',
    view_func=UserView.as_view('current_user'),
    methods=['GET', 'PATCH', 'DELETE']
)

application.add_url_rule(  # прописывает роуты для метода
    url='/users/',
    view_func=UserView.as_view('new_user'),
    methods=['POST']
)


if __name__ == '__main__':
    application.run()



