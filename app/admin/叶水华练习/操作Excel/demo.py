import pandas as pd
import pymysql
# xlrd模块实现对excel文件内容读取
# xlwt模块实现对excel文件的写入
import xlrd, xlwt
from sqlalchemy import create_engine
from app.common.mycolumns import needcolumns_fields, needcolumns_name

need_columns = {}
for i in range(0, len(needcolumns_name)):
    need_columns[needcolumns_name[i]] = needcolumns_fields[i]
'''
第一种实现结果，从Mysql上提取数据
'''


class ETL():
    def __init__(self):

        self.engine = create_engine('mysql+pymysql://root:gkbigdata123456@10.50.10.16:3306/recruit')
        self.conn = pymysql.connect(
            host='10.50.10.16',
            port=3306,
            user='root',
            passwd='gkbigdata123456',
            db='test',
            charset='utf8',
            use_unicode=True
        )

    '''
    连接mysql，获得数据，同时将其转为Dataframe
    '''

    # 得到所需要更改的字段，将其转换成英文
    def etl(self, fields, params, params_2):

        sql = 'select * from zs;'

        databases=self.engine

        read = pd.read_sql_query(sql, databases)
        # 将数据转化成Dataframe格式
        df = pd.DataFrame(read)

        #转换字段
        need_fields = list(map(lambda x: need_columns[x], fields))

        '''
        数据类似
        ['专业1','政治面貌']
        ['删除空值','填充空值']
        '''
        for need, param in zip(need_fields,params):

            if  param == '删除空值':
                counts = df[df[need]=='']
                print('-------------------')
                print('该列的空值个数为：', len(counts))
                df=df.drop(counts.index,axis=0)

                df.to_sql('')


            if param == '填充空值':
                a = 'sdsd'
                print(a)

            if param == '':
                pass






if __name__ == '__main__':
    fields = ['专业1', '民族']
    params = ['删除空值', '填充空值']

    e = ETL()
    e.etl(fields,params,params_2='')
