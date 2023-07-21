# **泛圈 project 仓库**

# **项目介绍**
该repo是2023年泛圈项目的仓库，包含前端和后端代码。  
前段使用react，后端使用django和django rest framework。
[详细的开发文档(notion)](https://chocolate-vanadium-ef9.notion.site/APP-f20ad60b0a97476ba71d96a1211ff785?pvs=4)  

## **How to use**
1. download/clone this project
2. make a virtual environment and download the packages in requirements.txt  
(本人使用了conda，不是python的 virtualenv，所以以下命令可能不适用于virtualenv。)
```bash
```bash
pip install -r requirements.txt
npm install
```  
(also you can use global environment, but it is 'highly recommended' to use virtual environment)  
if you have installed new dependencies, please update requirements.txt
```bash
pip freeze > requirements.txt
```  
3. (only once)配置数据库  
修改project_fanquan/settings.py 中下面部分，对接您想要的数据库  
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_fanquan',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'fanquanadmin',
        'PASSWORD': 'admin123',
    }
}
```
4. run the project
```bash
# start frontend
npm run dev
# start Django development server
python manage.py makemigrations # only after making migrations
python manage.py migrate # only after making migrations
python manage.py runserver <port> 
```  
if you encountered "ModuleNotFoundError: No module named '<modulename>'" error, please check the Python environment that Django is currently using.
```bash
which python
```
will output the current Python environment. If you already installed other python version in your machine, django may use the wrong python version. 
5. open your browser and visit http://localhost:{port}
