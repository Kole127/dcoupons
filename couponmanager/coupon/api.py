from coupon.models import Coupon
from rest_framework import viewsets, permissions
from .serializers import CouponSerializer

# Coupon Viewset


class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = CouponSerializer

   # def get_queryset(self):
   #     return self.request.user.coupon.all()

   # def perform_create(self, serializer):
   #     serializer.save(owner=self.request.user)
