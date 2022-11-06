from portfolio.api.views import (
        ArtViewSet
    )
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('arts', ArtViewSet, basename='art')

app_name = 'arts'

urlpatterns = router.urls