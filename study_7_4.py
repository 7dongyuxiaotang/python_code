import logging

# logging.basicConfig(
# 1、日志输出位置：1、终端 2、文件
# filename=r'd:\python\学习语法文件夹\导入文件文件夹\access.log', # 不指定，默认打印到终端

# 2、日志格式
# format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',

# 3、时间格式
# datefmt='%Y-%m-%d %H:%M:%S %p',

# 4、日志级别
# critical => 50

# error => 40
# warning => 30
# info => 20
# debug => 10
#     level=30,
# )

# logging.warning('警报警报')


#
import settings
from logging import config, getLogger

config.dictConfig(settings.LOGGING_DIC)
logger1 = getLogger('测试开发')

logger1.info('测')
