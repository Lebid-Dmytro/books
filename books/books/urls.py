from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from book_shop.views import AuthorViewSet, BookViewSet

router = SimpleRouter()

router.register(f'author', AuthorViewSet)
router.register(f'book', BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('book_shop/', include('book_shop.urls')),
    # path('client/', include('client.urls')),
]

urlpatterns += router.urls
