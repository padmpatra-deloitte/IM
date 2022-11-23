from django.urls import path

from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()
         ),
    path('project/<int:id>', views.ProjectDetails.as_view()
         ),
    path('issues/', views.IssueList.as_view()
         ),
    path('issue/<int:id>', views.IssueDetails.as_view()
         ),

]
