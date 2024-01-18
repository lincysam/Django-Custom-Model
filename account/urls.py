from django.urls import path,include
from account.views import UserViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'profile', UserViewset, basename='manage-user')
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),

]