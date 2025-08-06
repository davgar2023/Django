
from rest_framework import routers
from .api import projectViewSet

router = routers.DefaultRouter()

router.register('api/projects', projectViewSet, basename='projects')

urlpatterns = router.urls
