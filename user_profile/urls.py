from django.urls import path
from user_profile.views import CreateprofileView, UpdateProfileView

urlpatterns = [
    path('create/', CreateprofileView.as_view(), name='create-profile'),
    path('update/<int:pk>/', UpdateProfileView.as_view(), name='update-profile'),
]