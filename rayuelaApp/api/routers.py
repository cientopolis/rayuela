from rest_framework.routers import DefaultRouter
from rayuelaApp.api.viewset import RayuelaUserViewSet, ProjectViewSet, LoginViewSet, RegisterViewSet, LogoutViewSet

router = DefaultRouter()

router.register(r'users', RayuelaUserViewSet, basename='users')
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'login', LoginViewSet, basename='login')
router.register(r'register', RegisterViewSet, basename='register')
# router.register(r'logout', LogoutViewSet, basename='logout')

urlpatterns = router.urls
