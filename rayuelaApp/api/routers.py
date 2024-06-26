from rest_framework.routers import DefaultRouter
from rayuelaApp.api.viewset import LoginViewSet, RegisterViewSet, ProjectsViewSet, ProjectsWithoutTheUserViewSet

router = DefaultRouter()

router.register(r'login', LoginViewSet, basename='login')
router.register(r'register', RegisterViewSet, basename='register')
router.register(r'projects', ProjectsViewSet, basename='projects')
router.register(r'projects_diff', ProjectsWithoutTheUserViewSet, basename='projects_diff')

urlpatterns = router.urls
