from rest_framework.routers import DefaultRouter
from rayuelaApp.api.viewset import UserViewSet, ProjectViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='users')
router.register(r'projects', ProjectViewSet, basename='projects')

urlpatterns = router.urls
