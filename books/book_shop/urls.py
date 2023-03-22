from django.urls import path

from book_shop import views


urlpatterns = [
    path('book/', views.BookListView.as_view()),
    path('book/<int:pk>/', views.BookDetailView.as_view()),
    path('review/', views.ReviewView.as_view()),
    path('author/', views.AuthorListView.as_view()),
    path('author/<int:pk>', views.AuthorDetailView.as_view()),
    path('rating/', views.AddStarRatingViewSet.as_view()),
    path('order/', views.OrderCreateView.as_view()),
]
