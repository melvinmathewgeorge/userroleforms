from django.urls import path
from users.views import register_user_view, login_user_view, logout_user_view,student_page_view,staff_page_view,admin_page_view,editor_page_view, user_redirect_view

app_name='users'
urlpatterns = [
    path('', register_user_view, name='register_user'),
    path('login-user/', login_user_view, name='login_user'),
    path('logout-user/', logout_user_view, name='logout_user'),
    path('student_page/', student_page_view, name='student_page'),
    path('staff_page/', staff_page_view, name='staff_page'),
    path('admin_page/', admin_page_view, name='admin_page'),
    path('editor_page/', editor_page_view, name='editor_page'),
    path('redirect/', user_redirect_view, name='user_redirect')
]
