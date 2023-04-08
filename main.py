from app import make_app
from errors import HttpError, error_handler
from my_views import UserView, hello


app = make_app()

app.add_url_rule(
    '/users/<int:user_id>',
    view_func=UserView.as_view('current_user'),
    methods=['GET', 'PATCH', 'DELETE']
)

app.add_url_rule(  # прописывает роуты для метода
    '/users/',
    view_func=UserView.as_view('new_user'),
    methods=['POST']
)

app.add_url_rule('/hello/', view_func=hello, methods=['GET'])

app.errorhandler(HttpError)(error_handler)

if __name__ == '__main__':
    app.run()
