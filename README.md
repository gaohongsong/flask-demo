# flask-demo

&emsp;&emsp;flask入门样例，从[官方教程](http://docs.jinkan.org/docs/flask/tutorial/index.html)开始练起，并根据实际开发需要，
合理的拆分各个模块，便于代码的维护。

## 1. 目录结构：
   
   - *blueprints*     
   &emsp;&emsp;将业务逻辑分给为多个blueprint（app），以便功能复用和维护
   - *model*     
   &emsp;&emsp;数据库建模文件夹，包括主动建模和被动探测两种方式   
   - *common*     
   &emsp;&emsp;存放通用功能，比如日志、json格式化、db等
   - *commands*     
   &emsp;&emsp;自定义flask指令，比如数据库初始化、ipython-shell等   
   - *static*     
   &emsp;&emsp;存放静态资源文件，css/js等
   - *templates*      
   &emsp;&emsp;存放模板文件、Html文件
   - *config*  
   &emsp;&emsp;各环境配置，包括本地、测试、正式环境及各环境通用配置信息
   - *settings.py*  
   &emsp;&emsp;app配置入口
   - *factory.py*  
   &emsp;&emsp;app工厂
   - *app.py*     
   &emsp;&emsp;app入口

## 2. 数据库

&emsp;&emsp;数据库方面使用`SQLAlchemy`对接`mysql`


