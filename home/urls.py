from django.urls import path

from home import views

app_name = "home"

urlpatterns = [
    path('', views.Numero1.as_view(), name="numero1.9"),
    path('numero2.9/', views.Numero2.as_view(), name="numero2.9"),
    path('numero3.9/', views.Numero3.as_view(), name="numero3.9"),
    path('numero4.9/', views.Numero4.as_view(), name="numero4.9"),
    path('numero5.9/', views.Numero5.as_view(), name="numero5.9"),
    path('numero6.9/', views.Numero6.as_view(), name="numero6.9"),
    path('numero7.9/', views.Numero7.as_view(), name="numero7.9"),
    path('numero8.9/', views.Numero8.as_view(), name="numero8.9"),
    path('numero9.9/', views.Numero9.as_view(), name="numero9.9"),
    path('numero10.9/', views.Numero10.as_view(), name="numero10.9"),
]
