from re import L
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Item 
from.serializers import ItemSerializer


@api_view(['GET'])
def APioverview(request):
    api_urls = {
        'all-items': '/',
        'Search by category': '/?category=category_name',
        'Search by sub category': '/?subcategory=category_name',
        'Add':'/create',
        'Update':'/update/id',
        'Delete':'/item/id/delete'
        
    }
  
    return Response(api_urls) 


@api_view(['POST'])
def add_items(request):
    item = ItemSerializer(data = request.data)
    print(item)
    
    if Item.objects.filter(**request.data).exists():
        raise serializers.ValidationError(' The resource already exists...')
    if item._is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['GET'])
def view_items(request):
    if request.query_params:
        items = Item.objects.filter(**request.query_param.dict())
    else:
        items = Item.objects.all()
        
    if items:
        data = ItemSerializer(items)
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['POST'])
def update_items(request,_id):
    item = Item.objects.get(id=_id)
    data = ItemSerializer(instance = item,data = request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    
@api_view(['DELETE'])
def delete_items(request,_id):
    item = get_object_or_404(Item,id=_id)
    item.delete()
    return Response(status = status.HTTP_202_ACCEPTED)




