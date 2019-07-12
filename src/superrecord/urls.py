from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import index
from accounts import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('accounts/user/', user_views.user, name='user'),
    path('accounts/home/', user_views.home, name='home'),
    path('accounts/signup/', user_views.SignUpView.as_view(), name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('accounts/product/', user_views.product, name='product'),
    path('accounts/purchase/', user_views.purchase, name='purchase'),
    path('accounts/sales/', user_views.sales, name='sales'),
    path('accounts/expense/', user_views.expense, name='expense'),
    path('accounts/setting/', user_views.setting, name='setting'),
]
