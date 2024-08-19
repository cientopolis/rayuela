from rest_framework.routers import DefaultRouter
from rayuelaApp.api.viewset import LoginViewSet, RegisterViewSet, ProjectsViewSet, ProjectsWithoutTheUserViewSet
from rayuelaApp.api.viewset import JoinDisjoinTheProjectViewSet, CheckinViewset

router = DefaultRouter()

router.register(r'login', LoginViewSet, basename='login')
router.register(r'register', RegisterViewSet, basename='register')
router.register(r'projects', ProjectsViewSet, basename='projects')
router.register(r'projects_diff', ProjectsWithoutTheUserViewSet, basename='projects_diff')
router.register(r'join_the_project', JoinDisjoinTheProjectViewSet, basename='join_the_project')
router.register(r'disjoin_the_project', JoinDisjoinTheProjectViewSet, basename='disjoin_the_project')
router.register(r'checkin', CheckinViewset, basename='checkin')

urlpatterns = router.urls
