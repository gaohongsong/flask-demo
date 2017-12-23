# flask-demo

&emsp;&emsp;flask入门样例，从[官方教程](http://docs.jinkan.org/docs/flask/tutorial/index.html)开始练起，并根据实际开发需要，
合理的拆分各个模块，便于代码的维护。

## 1. 目录结构：
   
   - *blueprints*     
   &emsp;&emsp;将业务逻辑分给为多个blueprint（app），以便功能复用和维护
   - *common*     
   &emsp;&emsp;存放通用功能，比如日志、json格式化等
   - *static*     
   &emsp;&emsp;存放静态资源文件，css/js等
   - *templates*      
   &emsp;&emsp;存放模板文件、Html文件
   - *app.py*     
   &emsp;&emsp;app入口
   - *config.py*  
   &emsp;&emsp;app通用配置入口
   - *local_settings.py*  
   &emsp;&emsp;app个性化配置


## 2. 数据库

&emsp;&emsp;数据库方面使用`SQLAlchemy`对接`mysql`


