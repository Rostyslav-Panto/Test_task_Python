from rest_framework.routers import DefaultRouter
from .views import PortfolioView, ImageView, CommentView
from django.conf import settings

from django.conf.urls.static import static

app_name = 'main_page_api'

router = DefaultRouter()
router.register('portfolios', PortfolioView, basename='portfolios')
router.register('images', ImageView, basename='images')
router.register('comment', CommentView, basename='comment')
urlpatterns = router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
