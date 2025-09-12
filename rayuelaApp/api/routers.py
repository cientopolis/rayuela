from rest_framework.routers import DefaultRouter
from rayuelaApp.api.viewset import (LoginViewSet, RegisterViewSet, ProjectsViewSet, ProjectsWithoutTheUserViewSet,
                                    VolunteerViewSet, CheckinViewset, ProjectCollectionTasksViewSet, CollectionTaskViewSet)

router = DefaultRouter()

router.register(r'login', LoginViewSet, basename='login')
router.register(r'register', RegisterViewSet, basename='register')
router.register(r'projects', ProjectsViewSet, basename='projects')
router.register(r'projects_diff', ProjectsWithoutTheUserViewSet, basename='projects_diff')
router.register(r'project_collection_tasks', ProjectCollectionTasksViewSet, basename='project_collection_tasks')
router.register(r'volunteers', VolunteerViewSet, basename='volunteers')
router.register(r'checkin', CheckinViewset, basename='checkin')
router.register(r'collection_tasks', CollectionTaskViewSet, basename='collection_tasks')

urlpatterns = router.urls
