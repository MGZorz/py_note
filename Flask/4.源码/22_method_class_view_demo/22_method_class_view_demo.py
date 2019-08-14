from flask import Flask,views,render_template,request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

#定义一个基于请求方式调度的类视图
# class LoginView(views.MethodView):
#     def get(self):
#         return render_template('login.html')
#     def post(self):
#         #模拟实现
#         #拿到前端页面传过来的  账号  和密码 去数据库做查询操作 查询到 (跳转主页面) ,反之跳转到login.html页面并给出错误提示信息
#         uname = request.form['uname']
#         pwd = request.form['pwd']
#         if  uname=="momo"  and  pwd =="123":
#             return  render_template('index.html')
#         else:
#             return  render_template('login.html',error="用户名或者密码错误")

#改进1
# class LoginView(views.MethodView):
#     def get(self,error=None):
#         return render_template('login.html',error=error)
#     def post(self):
#         #模拟实现
#         #拿到前端页面传过来的  账号  和密码 去数据库做查询操作 查询到 (跳转主页面) ,反之跳转到login.html页面并给出错误提示信息
#         uname = request.form['uname']
#         pwd = request.form['pwd']
#         if  uname=="momo"  and  pwd =="123":
#             return  render_template('index.html')
#         else:
#             return  self.get(error="用户名或者密码错误")
#                 #render_template('login.html',error="用户名或者密码错误")

 # 改进2  :基于调度方法的类视图  ，通常get()方法处理get请求,post()方法处理post请求，为了便于管理,不推荐post方法和get方法互相调用
class LoginView(views.MethodView):
    def __jump(self,error=None):
       return render_template('login.html', error=error)

    def get(self, error=None):
        return  self.__jump()

    def post(self):
        # 模拟实现
        # 拿到前端页面传过来的  账号  和密码 去数据库做查询操作 查询到 (跳转主页面) ,反之跳转到login.html页面并给出错误提示信息
        uname = request.form['uname']
        pwd = request.form['pwd']
        if uname == "momo" and pwd == "123":
            return render_template('index.html')
        else:
            return self.__jump(error="用户名或者密码错误")

#注册类视图
app.add_url_rule("/login/",view_func=LoginView.as_view('mylogin'))

if __name__ == '__main__':
    app.run(debug=True)


