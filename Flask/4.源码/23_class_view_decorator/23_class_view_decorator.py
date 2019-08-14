from flask import Flask,request,views
from  functools import wraps
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


# 自定义一个装饰器
#需求：查看设置个人信息时，只有检测到用户已经登录了才能查看，若没有登录，则无法查看并给出提示信息
def login_requierd(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        username = request.args.get("username")
        if username and username =='momo':
             return func(*args,**kwargs)
        else:
            return  '请先登录'
    return wrapper

#功能函数  ：能够执行成功的前提条件是 必须先登录【写代码去判断当前用户是否已登录---》放到自定义装饰器】
# 1. 在视图函数中使用自定义装饰器，那么自己定义的装饰器必须放在`app.route`下面。否则这个装饰器就起不到任何作用。
@app.route('/settings/')
@login_requierd
def settings():
    return '这是设置界面'

#2. 在类视图中使用装饰器,需要重写类视图的一个类属性`decorators`，这个类属性是一个列表或者元组都可以，里面装的就是所有的装饰器。
class  ProfileView(views.View):
    decorators = [login_requierd]
    def dispatch_request(self):
        return '这是个人中心界面'

app.add_url_rule('/profile/',view_func=ProfileView.as_view('profile'))

if __name__ == '__main__':
    app.run(debug=True)
