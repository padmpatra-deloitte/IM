from django.urls import path

from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', views.TagViewSet)

urlpatterns = router.urls