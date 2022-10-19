from django.urls import path, include
from rest_framework import routers
from journals import views

router = routers.DefaultRouter()
router.register(r'journal', views.JournalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
