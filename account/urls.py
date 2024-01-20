from django.urls import path,include
from account.views import UserViewset
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'signup', UserViewset, basename='manage-user')
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path("login/",views.LoginView.as_view(), name="login")

]