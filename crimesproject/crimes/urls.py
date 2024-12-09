from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path('execute-sql/', views.execute_sql_query, name='execute_sql_query')
]
