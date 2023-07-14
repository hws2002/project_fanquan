# 泛圈 project 仓库

# 项目介绍
该repo是2023年泛圈项目的仓库，包含前端和后端代码。  
前段使用react，后端使用django和django rest framework。
详细的开发文档(notion)： https://chocolate-vanadium-ef9.notion.site/APP-f20ad60b0a97476ba71d96a1211ff785?pvs=4  
## **How to use**
1. download/clone this project
2. make a virtual environment and download the packages in requirements.txt
```bash
pip install -r requirements.txt
```
(also you can use global environment, but it is 'highly recommended' to use virtual environment)
if you have installed new dependencies, please update requirements.txt
```bash
pip freeze > requirements.txt
```
3. run the project
```bash
# start frontend
npm run dev
# start Django development server
python manage.py runserver <port> 
```
if you encountered "ModuleNotFoundError: No module named '<modulename>'" error, please check the Python environment that Django is currently using.
```bash
which python
```
will output the current Python environment. If you already installed other python version in your computer, django may use the wrong python version. 
4. open your browser and visit http://localhost:{port}
