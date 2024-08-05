from django.urls import path
from user.views import(
    CreateUserView,
    CreateSuperUserView,
    UpdateUserView,
    DeleteUserView,
    CreateAddressView,
    UpdateAddressView,
    DeleteAddressView,
)

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='register-user'),
    path('create/superuser/', CreateSuperUserView.as_view(), name='create-superuser'),
    path('update/<int:pk>/', UpdateUserView.as_view(), name='update-user'),
    path('delete/<int:pk>/', DeleteUserView.as_view(), name='delete-user'),
    path('address/create/', CreateAddressView.as_view(), name='create-address'),
    path('address/update/<int:pk>', UpdateAddressView.as_view(), name='update-address'),
    path('addres/delete/<int:pk>/', DeleteAddressView.as_view(), name='delete-address'),
]