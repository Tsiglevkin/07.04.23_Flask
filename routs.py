from adver import application
from my_views import UserView

application.add_url_rule(
    '/users/<int:user_id>/',
    view_func=UserView.as_view('current_user'),
    methods=['GET', 'PATCH', 'DELETE']
)

application.add_url_rule(  # прописывает роуты для метода
    '/users/',
    view_func=UserView.as_view('new_user'),
    methods=['POST']
)
