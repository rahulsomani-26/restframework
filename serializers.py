
from django.db.models import fields
from rest_framework import serializers
from .models import Item
  
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('category', 'subcatgeory', 'name', 'amount')
        # verbose_name_plural = 'items'
        # verbose_name = 'item'