from django.shortcuts import render
from django.http import JsonResponse
from .models import Data
import json


def home(request):
  all_data=Data.objects.all()
  file_list=[]
  for obj in all_data:
    temp=[]
    temp.append(obj.id)
    for key,value in obj.json_data.items():
      temp.append(key)
    file_list.append(temp)
  return render(request,'home.html',{'file_list':file_list})

def show(request,id):
  table=Data.objects.get(id=id)
  table=table.json_data
  return render(request,'show.html',{
    'table':table
  })

def post_data(request):
  file_data = json.loads(request.POST['data'])##this convert json string into python data structure
  Data.objects.create(json_data=file_data)
  return JsonResponse({"message":"ok"})
