from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'tasks', views.TaskViewSet, base_name='tasks')
router.register(r'tags', views.TagsViewSet, base_name='tags')
urlpatterns = router.urls