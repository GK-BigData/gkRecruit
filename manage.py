# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/6/25 上午10:15 

from flask_script import Manager

from flask_migrate import Migrate,MigrateCommand

from app import create_app,db


# 创建app
app = create_app()

dfgdg=123456
# 脚本管理
manager = Manager(app)


migrate = Migrate(app,db)
#添加数据库迁移到脚本管理
manager.add_command('db',MigrateCommand)

if __name__=='__main__':
    manager.run()
