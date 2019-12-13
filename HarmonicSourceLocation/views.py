# coding:utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse, JsonResponse
import json
from django.views.generic import View  
from django.conf import settings as SET
from .models import Site,BaseData
#页面配置
info=SET.INFO
#页面命名
INDEX,TOPO2MATRIX=SET.INDEX,SET.TOPO2MATRIX
HarS_NAME,MultiH_NAME=SET.PHAR,SET.PHMULTIHAR
#数据库连接
connection=SET.CONNECTION
#数据库返回的总数据
DATA_BASE=SET.DATA_BASE
HIGH_DATA_BASE=SET.HIGH_DATA_BASE
LOW_DATA_BASE=SET.LOW_DATA_BASE
SAFE_DATA_BASE=SET.SAFE_DATA_BASE

#启动页
class Start(View):
    def get(self,request,*args,**kwargs):
        info.update({'page_name':INDEX["name"]});
        return render_to_response('start.html',context={'info':info})
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('你使用的是%s请求，但是不支持get以外的其他请求！'%request.method) 

# 首页
class Index(View):
    def get(self,request,*args,**kwargs):
        info.update({'page_name':INDEX["name"]});
        return render_to_response('index.html',context={'info':info})
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('你使用的是%s请求，但是不支持get以外的其他请求！'%request.method)

# 矩阵转化页    
class Topo2Matrix(View):
    def get(self,request,*args,**kwargs):
        info.update({'page_name':TOPO2MATRIX["name"]});
        return render_to_response('topo2Matrix.html',context={'info':info});
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('你使用的是%s请求，但是不支持get以外的其他请求！'%request.method) 

#基于正交匹配的谐波源定位
class HarSouLocation(View):
    def get(self,request,*args,**kwargs):
        info.update({'page_name':HarS_NAME});
        return render_to_response('HarSouLocation.html',context={'info':info});
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('你使用的是%s请求，但是不支持get以外的其他请求！'%request.method) ;

# 多点谐波源定位
class MultiHarSouLocation(View):
    def get(self,request,*args,**kwargs):
        info.update({'page_name':MultiH_NAME})
        global DATA_BASE
        global HIGH_DATA_BASE
        global LOW_DATA_BASE
        global SAFE_DATA_BASE
        objects=Site.objects;
        DATA_BASE=list(objects.values());
        HIGH_DATA_BASE=list(objects.filter(levelV__gt = 1000).values());
        LOW_DATA_BASE=list(objects.filter(levelV__range=(50,1001)).values());
        SAFE_DATA_BASE=list(objects.filter(levelV__lt=50).values());
        return render_to_response('MultiHarSouLocation.html', context={'info':info,"DATA_BASE":DATA_BASE,'HIGH_DATA_BASE':HIGH_DATA_BASE,'LOW_DATA_BASE':LOW_DATA_BASE,'SAFE_DATA_BASE':SAFE_DATA_BASE})
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('你使用的是%s请求，但是不支持get以外的其他请求！'%request.method) ;
    
#测试页面     
class Test(View):
    def get(self,request,*args,**kwargs):
        return render_to_response('test.html',{"name":"PIIII"})
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('你使用的是%s请求，但是不支持get以外的其他请求！'%request.method) 
    