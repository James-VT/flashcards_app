# cards/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.CardListView.as_view(),
        name="card-list"
    ),
    path(
        "new",
        views.CardCreateView.as_view(),
        name="card-create"
    ),
    path(
        "edit/<int:pk>",
        views.CardUpdateView.as_view(),
        name="card-update"
    ),
    # The below is where the box_num keyword argument comes from.
    # Presumably it's generated from the URL or some built-in Django thing,
    # like the primary key above.
    path(
        "box/<int:box_num>",
        views.BoxView.as_view(),
        name="box"
    ),
]
