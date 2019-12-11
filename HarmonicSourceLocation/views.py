# coding:utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse, JsonResponse
import json
from django.views.generic import View  
from .SQLServerConnect import *
from django.conf import settings as SET

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
        DATA_BASE=json.dumps({"res": DATA_BASE})
        HIGH_DATA_BASE = json.dumps({"res": HIGH_DATA_BASE})
        LOW_DATA_BASE = json.dumps({"res": LOW_DATA_BASE})
        SAFE_DATA_BASE = json.dumps({"res": SAFE_DATA_BASE});
        print("多点定位数据：",DATA_BASE,HIGH_DATA_BASE)
        return render_to_response('MultiHarSouLocation.html', context={'info':info,'DATA_BASE':DATA_BASE,'HIGH_DATA_BASE':HIGH_DATA_BASE,'LOW_DATA_BASE':LOW_DATA_BASE,'SAFE_DATA_BASE':SAFE_DATA_BASE})
        # return render_to_response('MultiHarSouLocation.html',context={'info':info});
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('你使用的是%s请求，但是不支持get以外的其他请求！'%request.method) ;
    
# 连接sqlServer，非页面
class Connect2SQL(View):
    def get(self,request,*args,**kwargs):
        global connection
        yes,no=json.dumps({"res":1}),json.dumps({"res":0})
        try:
            database=dict(request.GET).get("database",None)
            database=database[0]
            connection=SqlServerConn(database=database)
            px=connection.connect();
            # connection.insert_test();
            if px:
                global DATA_BASE
                global HIGH_DATA_BASE
                global LOW_DATA_BASE
                global SAFE_DATA_BASE
                # global XX1
                #global XX2
                DATA_BASE=connection.fetDataByRows()
                HIGH_DATA_BASE = connection.fetHighDataByRows()
                LOW_DATA_BASE = connection.fetLowDataByRows()
                SAFE_DATA_BASE = connection.fetSafeDataByRows()
                # XX1 = connection.fetBaseDataBySite().tolist
                #XX2 = connection.fetBaseData2BySite().tolist
                #print("XX1: ", XX1)
                #print("XX2: ", XX2)
                #rst=porhowlyuu(XX1, XX2)
                return HttpResponse(yes)
            else:return HttpResponse(no)
        except Exception as e:
            print("错误：",e)
            return HttpResponse(no)
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('你使用的是%s请求，但是不支持get以外的其他请求！'%request.method)
    
#测试页面     
class Test(View):
    def get(self,request,*args,**kwargs):
        return render_to_response('test.html',{"name":"PIIII"})
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('你使用的是%s请求，但是不支持get以外的其他请求！'%request.method) 
    