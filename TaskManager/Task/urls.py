from django.urls import path
from . import views
urlpatterns = [
    path("tasks/", views.TaskCreateListApiView.as_view(), name = "task-create-list"),
    path("tasks/<int:pk>/", views.TaskRetrieveDeleteUpdateApiView.as_view(), name = "task-crud")
]