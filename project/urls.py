from django.urls import path

from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('project', views.ProjectViewSet)
router.register('issue', views.IssueViewSet)

urlpatterns = router.urls

#  [
#     path('projects/', views.ProjectList.as_view()
#          ),
#     path('project/<int:pk>', views.ProjectDetails.as_view()
#          ),
#     path('issues/', views.IssueList.as_view()
#          ),
#     path('issue/<int:pk>', views.IssueDetails.as_view()
#          ),

# ]
