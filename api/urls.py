from rest_framework.routers import DefaultRouter
from .views import PortfolioView

app_name = 'main_page_api'

router = DefaultRouter()
router.register('portfolios', PortfolioView, basename='portfolios')

urlpatterns = router.urls
