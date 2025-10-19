from django.urls import path

from . import views

app_name = "courses"

urlpatterns = [
    path(
        "<slug:course_id>/lessons/<slug:lesson_id>",
        views.lesson_detail_view,
        name="lesson_detail",
    ),
    path("<slug:course_id>/", views.course_detail_view, name="detail"),
    path("", views.course_list_view, name="list"),
]
