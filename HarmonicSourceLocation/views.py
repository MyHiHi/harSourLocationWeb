# coding:utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
import json
import numpy as np
from django.views.generic import View
from django.conf import settings as SET
from .models import Site, BaseData,Station
from django.db.models import F
from .HarSouLocation import banch, suanfa
from .MultiHarSouLocation.hslocation import porhowlyuu
# 测试获取电流数据的
# ********************
from .SQLServerConnect import SqlServerConn
conn = SqlServerConn()
conn.connect()
Is = conn.getAllI()
Is = [(complex(i[0])) for i in Is]
Is_len = len(Is)
datamatrix1 = np.zeros((Is_len, 1), dtype="complex128")
datamatrix1[:, 0] = Is
Is = datamatrix1
# ********************
# print(MyI.objects.all())

# 页面配置
info = SET.INFO
# 页面命名
INDEX, TOPO2MATRIX = SET.INDEX, SET.TOPO2MATRIX
HarS_NAME, MultiH_NAME = SET.PHAR, SET.PHMULTIHAR
# 数据库连接
# connection = SET.CONNECTION
# 数据库返回的总数据
DATA_BASE = SET.DATA_BASE
HIGH_DATA_BASE = SET.HIGH_DATA_BASE
LOW_DATA_BASE = SET.LOW_DATA_BASE
SAFE_DATA_BASE = SET.SAFE_DATA_BASE
SITE_POST=SET.SITE_POST
# 存储当前转化后的矩阵、
MATRIX = None

# 启动页
class Start(View):
    def get(self, request, *args, **kwargs):
        info.update({'page_name': INDEX["name"]})
        return render_to_response('start.html', context={'info': info})

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('你使用的是%s请求，但是不支持get以外的其他请求！' % request.method)

# 首页


class Index(View):
    def get(self, request, *args, **kwargs):
        info.update({'page_name': INDEX["name"]})
        return render_to_response('index.html', context={'info': info})

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('你使用的是%s请求，但是不支持get以外的其他请求！' % request.method)

# 矩阵转化页


class Topo2Matrix(View):
    def get(self, request, *args, **kwargs):
        info.update({'page_name': TOPO2MATRIX["name"]})
        return render_to_response('topo2Matrix.html', context={'info': info})

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('你使用的是%s请求，但是不支持get以外的其他请求！' % request.method)


class GetMatrix(View):
    def get(self, request, *args, **kwargs):
        # 这是生成的矩阵
        global MATRIX
        matrix = eval(dict(request.GET).get("matrix")[0])
        matr = {}
        for k, v in matrix.items():
            k = int(k)
            matr[k] = {}
            if len(v):
                for n, m in v.items():
                    matr[k].update({int(n): m});
        # graph = {1: {1:0,2: 8, 5: 9},
        #  2: {3: 7},
        #  3: {4: 6},
        #  4: {7: 5},
        #  5: {6: 10},
        #  6: {11: 11, 12: 12},
        #  7: {8: 4, 9: 3},
        #  8: {},
        #  9: {10: 2, 14: 1},
        #  10: {},
        #  11: {},
        #  12: {13: 13},
        #  13: {},
        #  14: {},
        #  }
        
        matrix = banch(matr, 1);
        # 保存/测试
        # matrix = banch(graph, 1);
        MATRIX = matrix
        matrix = matrix.tolist()
        res = {"matrix": matrix}
        return HttpResponse(json.dumps(res))

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('你使用的是%s请求，但是不支持get以外的其他请求！' % request.method)


class GetSourLocation(View):
    def get(self, request, *args, **kwargs):
        # 这是生成的矩阵
        global MATRIX
        iter_num = int(dict(request.GET).get("iter_num")[0])
        print("GHGH:",MATRIX,iter_num)
        c = suanfa(MATRIX, Is, iter_num)
        c=c.tolist();
        print("&YY: ",c)
        # res = 
        # print("最后的结果：", res)
        return HttpResponse(json.dumps({"location":c}))

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('你使用的是%s请求，但是不支持get以外的其他请求！' % request.method)

# 基于正交匹配的谐波源定位


class HarSouLocation(View):
    def get(self, request, *args, **kwargs):
        info.update({'page_name': HarS_NAME})
        return render_to_response('HarSouLocation.html', context={'info': info})

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('你使用的是%s请求，但是不支持get以外的其他请求！' % request.method)

# 多点谐波源定位


class MultiHarSouLocation(View):
    def get(self,request,*args,**kwargs):
        info.update({'page_name':MultiH_NAME})
        stid = int(Station_pcs.get(self, request));
        data=getMultiData(stid)
        # print("stid:", stid)
        # print("DATA_BASE", DATA_BASE)
        return render_to_response('MultiHarSouLocation.html', context={**info,**data})
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('你使用的是%s请求，但是不支持get以外的其他请求！'%request.method)

 
#提取电压值
class Data_pcs(View):
    def get(self,request,*args,**kwargs):
        XX1 = list(BaseData.objects.filter(site=1).values_list("v", flat=True))
        XX2 = list(BaseData.objects.filter(site=2).values_list("v", flat=True))
        XX3 = list(BaseData.objects.filter(site=3).values_list("v", flat=True))
        XX4 = list(BaseData.objects.filter(site=4).values_list("v", flat=True))
        XX5 = list(BaseData.objects.filter(site=5).values_list("v", flat=True))
        XX6 = list(BaseData.objects.filter(site=6).values_list("v", flat=True))
        XX7 = list(BaseData.objects.filter(site=7).values_list("v", flat=True))
        XX8 = list(BaseData.objects.filter(site=8).values_list("v", flat=True))
        XX9 = list(BaseData.objects.filter(site=9).values_list("v", flat=True))
        XX10 = list(BaseData.objects.filter(site=10).values_list("v", flat=True))
        XX11 = list(BaseData.objects.filter(site=11).values_list("v", flat=True))
        XX12 = list(BaseData.objects.filter(site=12).values_list("v", flat=True))
        XX13 = list(BaseData.objects.filter(site=13).values_list("v", flat=True))
        XX14 = list(BaseData.objects.filter(site=14).values_list("v", flat=True))
        XX1 = np.array(XX1).reshape((-1, 1))
        XX2 = np.array(XX2).reshape((-1, 1))
        XX3 = np.array(XX3).reshape((-1, 1))
        XX4 = np.array(XX4).reshape((-1, 1))
        XX5 = np.array(XX5).reshape((-1, 1))
        XX6 = np.array(XX6).reshape((-1, 1))
        XX7 = np.array(XX7).reshape((-1, 1))
        XX8 = np.array(XX8).reshape((-1, 1))
        XX9 = np.array(XX9).reshape((-1, 1))
        XX10 = np.array(XX10).reshape((-1, 1))
        XX11 = np.array(XX11).reshape((-1, 1))
        XX12 = np.array(XX12).reshape((-1, 1))
        XX13 = np.array(XX13).reshape((-1, 1))
        XX14 = np.array(XX14).reshape((-1, 1))
        return XX1, XX2, XX3, XX4, XX5, XX6, XX7, XX8, XX9, XX10, XX11, XX12, XX13, XX14

#前端提交监测点
class Sitepost(View):
    def get(self,request,*args,**kwargs):
        re = eval(request.GET.getlist("site")[0])
        # print("*****************",re)
        SITE_POST = re
        # print("porhowlyuu",SITE_POST)
        XX1, XX2, XX3, XX4, XX5, XX6, XX7, XX8, XX9, XX10, XX11, XX12, XX13, XX14=Data_pcs.get(self,request)
        X = []
        for i in range(len(SITE_POST)):
            locals()['XX' + str(SITE_POST[i])] = SITE_POST[i]
            # print('XX' + str(SITE_POST[i]))
            X.append(eval('XX' + str(SITE_POST[i])))
        X = np.array(X)
        XX = np.array([XX1, XX2, XX3, XX4, XX5, XX6, XX7, XX8, XX9, XX10, XX11, XX12, XX13, XX14])
        matx,locp = porhowlyuu(X, XX)
        locp=locp.tolist()
        loc = []
        for i in locp:
            if i not in loc:
                loc.append(i)
        loc = sorted(loc, reverse=False)
        print("谐波源为：", loc)
        p = json.dumps({"LOCATION": loc})
        return HttpResponse(p)
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('你使用的是%s请求，但是不支持get以外的其他请求！'%request.method)

# 获取前端Station
class Station_pcs(View):
    def get(self,request,*args,**kwargs):
        objects = Station.objects
        st = request.GET.get("station")
        if not st:
            return 1
        else:
            st=eval(st);
            stid = list(objects.filter(stationname=st).values("stationid"));
            stid=stid[0].get("stationid")
            return stid

# Station提交
class Stationpost(View):
    def get(self,request,*args,**kwargs):
        stid = int(Station_pcs.get(self, request));
        p=getMultiData(stid);
        return HttpResponse(json.dumps(p))

# 多点谐波源定位

def getMultiData(stid):
    global DATA_BASE
    global HIGH_DATA_BASE
    global LOW_DATA_BASE
    global SAFE_DATA_BASE
    objects = Site.objects
    DATA_BASE = list(objects.filter(stationid=stid).values())
    HIGH_DATA_BASE = list(objects.filter(stationid=stid).filter(levelV__gt=1000).values())
    LOW_DATA_BASE = list(objects.filter(stationid=stid).filter(levelV__range=(50, 1001)).values())
    SAFE_DATA_BASE = list(objects.filter(stationid=stid).filter(levelV__lt=50).values())
    Station_list = list(Station.objects.values_list("stationname", flat=True));
    return {"DATA_BASE":DATA_BASE,'HIGH_DATA_BASE':HIGH_DATA_BASE,'LOW_DATA_BASE':LOW_DATA_BASE,'SAFE_DATA_BASE':SAFE_DATA_BASE, "STATION": Station_list}

class CreateStation(View):
    def get(self,request,*args,**kwargs):
        info.update({'page_name':""});

        return render_to_response('CreateStation.html', context={})
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('你使用的是%s请求，但是不支持get以外的其他请求！'%request.method)

# 测试页面


class Test(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('test.html', {"name": "PIIII"})

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('你使用的是%s请求，但是不支持get以外的其他请求！' % request.method)
