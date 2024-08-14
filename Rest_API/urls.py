from rest_framework import routers
from .api import project_view_set


router = routers.DefaultRouter()

router.register('api/projects', project_view_set, 'projects' )

urlpatterns = router.urls

