from django.urls import path
from .views import ProspectsViews

urlpatterns = [
    path('prospect-list/', ProspectsViews.as_view()),
    path('prospect-list/<int:id>', ProspectsViews.as_view()),
]
