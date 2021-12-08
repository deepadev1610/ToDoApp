from django.urls import path
from .views import CustomLoginView, RegisterPage, ReorderToDo, ToDoDelete, ToDoList, ToDoDetail, ToDoCreate, ToDoUpdate
from .models import Todo
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'
    ),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', ToDoList.as_view(), name='todos'),
    path('todo/<int:pk>/', ToDoDetail.as_view(), name='todo'),
    path('todo-create/', ToDoCreate.as_view(), name='create-todo'),
    path('todo-update/<int:pk>/', ToDoUpdate.as_view(), name='edit-todo'),
    path('todo-delete/<int:pk>/', ToDoDelete.as_view(), name='delete-todo'),
    path('todo-reorder/', ReorderToDo.as_view(), name='reorder-todo'),
    
]