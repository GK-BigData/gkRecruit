import pandas as pd
import pymysql
# xlrd模块实现对excel文件内容读取
# xlwt模块实现对excel文件的写入
import xlrd, xlwt
from sqlalchemy import create_engine
from app.common.mycolumns import needcolumns_fields, needcolumns_name
from datetime import datetime

need_columns = {}
for i in range(0, len(needcolumns_name)):
    need_columns[needcolumns_name[i]] = needcolumns_fields[i]
'''
第一种实现结果，从Mysql上提取数据
'''


class ETL():
    def __init__(self):

        self.engine = create_engine('mysql+pymysql://root:gkbigdata123456@192.168.43.33:3306/recruit')
        self.now_time=datetime.now()

    '''
    连接mysql，获得数据，同时将其转为Dataframe
    '''

    def C_replaces(self,lines):
        list2 = ['广州', '深圳', '珠海', '汕头', '佛山', '韶关', '湛江', '肇庆', '江门', '茂名', '惠州', '梅州', '汕尾', '河源', '阳江',
                 '清远', '东莞', '中山', '潮州', '揭阳', '云浮']
        if lines[:2] in list2:
            return lines[:2] + '市'
        else:
            return lines

    def S_replaces(self,need):
        if need == '黑龙江省':
            return need[:3]
        else:
            return need[:2]


    # 得到所需要更改的字段，将其转换成英文
    def etl(self, record,fields, params, params_2):

        sql = 'select * from zs where recordid=%s;'
        #sql_test='select * from t;'

        databases=self.engine
        #databases_test=self.engine_test

        read = pd.read_sql_query(sql, databases,params=[record['id']])
        #read=pd.read_sql_query(sql_test,databases_test)

        # 将数据转化成Dataframe格式
        df = pd.DataFrame(read)
        length_df=len(df)
        #转换字段
        need_fields = list(map(lambda x: need_columns[x], fields))

        #need_fields=['id']
        #params=['填充空值']

        re={}
        for need, param in zip(need_fields,params):
            if  param == '删除空值':
                print(need)
                null=df[df[need]=='']
                df=df.drop(null.index)
                all_length=length_df-len(df)
                re[param+'个数为']=all_length

            #必须为数字
            if param == '填充空值':
                #将数字效值变成Nan
                df[need]=pd.to_numeric(df[need], errors='coerce')
                print(df[need])

                if params_2=='填充0':
                    df[need]=df[need].fillna(0,inplace=True)
                    re['填充0']='成功'

                elif params_2=='填充平均值':
                    print(params_2)
                    df[need]=df[need].fillna(df[need].mean(),inplace=True)
                    re['填充平均值']='成功'

                elif params_2=='填充中位数':
                    print(params_2)
                    df[need]=df[need].fillna(df[need].median(),inplace=True)
                    re['填充中位数']='成功'

            #成市的转换
            if param == '转换城市':
                if need=='student_address':
                    df[need] = df[need].map(self.C_replaces)
                    re['转换城市']='成功'
                else:
                    city='请选择户口所在地（地区名称）'
                    re['转换成市']='失败/未选择需要的字段'
                    return city

            #做地图需要的字段['广东','广西','贵州']
            if param=='转换省份':
                if need=='source_provinces':
                    df[need]=df[need].map(self.S_replaces)
                    re['转换省份']='成功'

            #出生日期
            if param=='时间格式转换':
                if need=='Data_of_birth':
                    df[need]=pd.to_datetime(df[need],format='%Y-%m-%d')
                    re['转换时间格式']='成功'


        self.engine.execute('insert into record(status,time,zsyear,filename) values(%s,%s,%s,%s)','xx',self.now_time,2018,'a.xmls')
        recordid = self.engine.execute('select max(id) from record').first()[0]
        print(recordid)
        df['recordid']=recordid
        re['当前行列数为']=df.shape
        re['recordid']=recordid
        df=df.drop(['id'],axis=1)
        df.to_sql(name='zs',con=self.engine,if_exists='append',index=False,index_label=False)
        print('插入成功!!!')
        print(re)


if __name__ == '__main__':
    fields = ['户口所在地']
    params = ['转换城市']
    params_2=['']
    e = ETL()
    e.etl({'id':1,'zsyear':2018},fields,params,params_2)

