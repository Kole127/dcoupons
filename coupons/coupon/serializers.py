from rest_framework import serializers
from coupon.models import Coupon

# Coupon Serializer


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'
