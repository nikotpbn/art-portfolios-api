from asyncio import AbstractEventLoop
from portfolio.api.views import ArtViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'arts', ArtViewSet, basename='art')
urlpatterns = router.urls