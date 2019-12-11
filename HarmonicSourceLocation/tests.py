# from django.test import TestCase


# DATA_INFO={"HOST":"127.0.0.1",
#            "USER":'sa',
#            "PASSWORD":'123456',
#            "DATABASE":'test',
#            "TABLE":"DayLoadRate"
# }
# import pymssql
# connection=pymssql.connect("127.0.0.1","sa","123456","test");
# cursor=connection.cursor();
# param="'' or 1=1"
# cursor.execute("select * from DayLoadRate where data=%d",(param,));

# print(cursor.fetchall())

def singleton(cls):
    _instance = {}
    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton

@singleton
class Person():
    
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
        
p1=Person('NM',12);
p2=Person("KKK",23);
print(p2.name)