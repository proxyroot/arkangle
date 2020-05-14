from django.urls import path
from search.views import HomePageView

app_name = "search"

urlpatterns = [
    path("", HomePageView.as_view()),
]
