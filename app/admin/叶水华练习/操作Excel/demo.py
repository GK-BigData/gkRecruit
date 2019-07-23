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
        #self.engine_test = create_engine('mysql+pymysql://root:gkbigdata123456@10.50.10.16:3306/test')

        # self.conn = pymysql.connect(
        #     host='10.50.10.16',
        #     port=3306,
        #     user='root',
        #     passwd='gkbigdata123456',
        #     db='test',
        #     charset='utf8',
        #     use_unicode=True
        # )
        self.now_time=datetime.now()

    '''
    连接mysql，获得数据，同时将其转为Dataframe
    '''

    def tra(self,lines):
        list2 = ['广州', '深圳', '珠海', '汕头', '佛山', '韶关', '湛江', '肇庆', '江门', '茂名', '惠州', '梅州', '汕尾', '河源', '阳江',
                 '清远', '东莞', '中山', '潮州', '揭阳', '云浮']
        if lines[:2] in list2:
            return lines[:2] + '市'
        else:
            return lines

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

            '''
            if param == '填充空值':
                #将无效值变成Nan
                df[need]=pd.to_numeric(df[need], errors='coerce')
                print(df[need])
                if params_2=='填充0':
                    pass

                elif params_2=='填充平均值':
                    print(params_2)
                    fill_avg_value=df[need].fillna(df[need].mean(),inplace=True)

                elif params_2=='填充中位数':
                    print(params_2)
                    fill_median_value=df[need].fillna(df[need].median(),inplace=True)
                    print(fill_median_value)
            '''
            if param == '转换城市':
                if need=='student_address':
                    df[need] = df[need].map(self.tra)
                    re['转换城市']='成功'


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

