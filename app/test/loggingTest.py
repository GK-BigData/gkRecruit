# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/7/30 上午10:13 
# BY    :FormatFa
# 日志casein


import logging

print(type(__name__))
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,filename='base.log')



logger.info('info日志测试')
logger.debug('debug 条')
logger.warning('警告')

try:
    result = 10/0
except Exception as e:
    logger.error('失败',exc_info=True)