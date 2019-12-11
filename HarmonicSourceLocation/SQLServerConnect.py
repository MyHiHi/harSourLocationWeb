import os,django
import pymssql
from django.conf import settings as SET
# from .utils import singleton
# 数据库配置****************
data=SET.DATA_INFO
class SqlServerConn():
    
    def __init__(self,host=data.get("HOST",None),user=data.get("USER",None),password=data.get("PASSWORD",None),database=data.get("DATABASE",None)):
        self.host,self.user,self.password,self.database=host,user,password,database;
    def connect(self):
        try:
            self.connection=pymssql.connect(self.host,self.user,self.password,self.database,charset="utf8");
            self.cursor=self.connection.cursor();
            return True;
        except Exception as e:
            print('连接失败： ',e);
            return False;
            
    def fetDataByRows(self,table=data.get("Base_Data_Table"),row=""):
        try:
            if row:
                sql = "select  * from {1} a ".format(row,data.get("Site_Table", None))
            else:
                sql = "select * from {1} a ".format(row,data.get("Site_Table", None))
                #sql="select * from "+str(table);
            self.cursor.execute(sql);
            return [list(i) for i in self.cursor.fetchall()]  
        except Exception as e:
            print("获取数据库数据失败：",e);
            return [];
    def fetHighDataByRows(self,table=data.get("Base_Data_Table"),row=""):
        try:
            if row:
                sql = "select * from {1} a where a.LevelV>1000".format(row,data.get("Site_Table", None))
            else:
                sql = "select * from {1} a where a.LevelV>1000".format(row,data.get("Site_Table", None))
            self.cursor.execute(sql);
            return [list(i) for i in self.cursor.fetchall()]
        except Exception as e:
            print("获取数据库数据失败：",e);
            return [];
    def fetLowDataByRows(self,table=data.get("Base_Data_Table"),row=""):
        try:
            if row:
                sql = "select * from {1} a where a.LevelV>=50 and a.LevelV<=1000".format(row,data.get("Site_Table", None))
            else:
                sql = "select * from {1} a where a.LevelV>=50 and a.LevelV<=1000".format(row,data.get("Site_Table", None))
            self.cursor.execute(sql);
            return [list(i) for i in self.cursor.fetchall()]
        except Exception as e:
            print("获取数据库数据失败：",e);
            return [];
    def fetSafeDataByRows(self,table=data.get("Base_Data_Table"),row=""):
        try:
            if row:
                sql = "select * from {1} a where a.LevelV<50".format(row,data.get("Site_Table", None))
            else:
                sql = "select * from {1} a where a.LevelV<50".format(row,data.get("Site_Table", None))
            self.cursor.execute(sql);
            return [list(i) for i in self.cursor.fetchall()]
        except Exception as e:
            print("获取数据库数据失败：",e)
            return []
    # def fetBaseDataBySite(self,table=data.get("Base_Data_Table"),row=""):
    #     try:
    #         sql = "select V from {1} a where Site_id=1".format(row,data.get("Base_Data_Table", None))
    #         self.cursor.execute(sql)
    #         # return [list(i) for i in self.cursor.fetchall()]
    #         return [list(i) for i in self.cursor.fetchall()]
    #     except Exception as e:
    #         print("获取数据库数据失败：",e)
    #         return []
    # def fetBaseData2BySite(self,table=data.get("Base_Data_Table"),row=""):
    #     try:
    #         sql = "select V from {1} a where Site_id=2".format(row,data.get("Base_Data_Table", None))
    #         self.cursor.execute(sql)
    #         # return [list(i) for i in self.cursor.fetchall()]
    #         return [list(i) for i in self.cursor.fetchall()]
    #     except Exception as e:
    #         print("获取数据库数据失败：",e)
    #         return []
    # 可能有些问题
    def insert_test(self):
        try:
            sql="INSERT INTO {0}(data) VALUES ('%s')".format(data.get("TABLE"));
            print("insert 语句: ",sql)
            self.cursor.executemany(sql,[(str(i),) for i in range(1,1200)]);
            self.connection.commit();
        except Exception as e:
            self.connection.rollback();
            print("插入出错：",e)
    def __del__(self):
        self.cursor.close();
        self.connection.close();
    def close(self):
        try:
            self.cursor.close();
            self.connection.close();
        except Exception as e:
            print ("关闭数据库出错： ",e)



if __name__=="__main__":
    p=SqlServerConn();
    p.connect();
        # print(p.fetDataByRows(row=5));
    print(p.fetSafeDataByRows())
        
        

