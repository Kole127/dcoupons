from rest_framework import routers
from .api import CouponViewSet

router = routers.DefaultRouter()
router.register('api/coupon', CouponViewSet, 'coupon')

urlpatterns = router.urls
