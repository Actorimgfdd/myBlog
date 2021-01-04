from django.urls import path
from articles import views
# from .views import index,about,contact,detail


urlpatterns = [
    path('list/',views.index,name="list"),
    path('detail/<int:pk>',views.detail,name="detail"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about")
]