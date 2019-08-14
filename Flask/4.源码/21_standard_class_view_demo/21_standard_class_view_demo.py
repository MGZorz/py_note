from flask import Flask,views,url_for,jsonify,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

#定义一个类视图
class  ListView(views.View):
    def dispatch_request(self):
        return "这是List列表"

#注册类视图,如果没有指定`endpoint`，那么就可以使用`as_view(视图名字)`中指定的视图名字来作为反转。
# app.add_url_rule('/list/',view_func=ListView.as_view('my_list'))
#注册类视图,若注册url时，有指定endpoint，就不能再使用as_view（）方法中的名称 来构建url，而要使用endpoint的值来构建url
app.add_url_rule('/list/',endpoint='mlist',view_func=ListView.as_view('my_list'))


with  app.test_request_context():
       #注册类视图时,如果没有指定`endpoint`，那么就可以使用`as_view(视图名字)`中指定的视图名字来作为反转。构建url
       # print(url_for('my_list'))
       #若注册url时，有指定endpoint，就不能再使用as_view（）方法中的名称 来构建url，而要使用endpoint的值来构建url
       print(url_for('mlist'))

#类视图的好处:继承
#需求1：以后有 好几个url，都需要返回json对象的格式
class  ListView2(views.View):
    def  getData(self):
        raise  NotImplementedError

    def  dispatch_request(self):
        return  jsonify(self.getData())

class  JSONView(ListView2):
    def getData(self):
        return {'uname':'momo','age':'22'}


class  JSONView2(ListView2):
    def getData(self):
        return {'bname':'水浒传','price':'89'}
app.add_url_rule('/json/',view_func=JSONView.as_view('my_json'))
app.add_url_rule('/json2/',view_func=JSONView2.as_view('my_json2'))


#需求2：有好几个url，跳转到到不同的页面时，会带一个相同的参数过去
#登录功能
# class   LoginView(views.View):
#     def dispatch_request(self):
#         return    render_template('login.html',ads="茅台酒   998")
#
# #注册功能
# class   RegisterView(views.View):
#     def dispatch_request(self):
#        return    render_template('register.html',ads="茅台酒   998")


#改进：突出类视图的好处
class  ADSView(views.View):
    def  __init__(self):
        super(ADSView, self).__init__()
        self.context={
            'ads':'机器人  人工智能'
        }

#登录功能
class   LoginView(ADSView):
    def dispatch_request(self):
        self.context.update({'pid':'好牛的一本书'})
        return    render_template('login.html',**self.context)

#注册功能
class   RegisterView(ADSView):
    def dispatch_request(self):
       self.context.update({'pid': '好吃的水果'})
       return    render_template('register.html',**self.context)
app.add_url_rule('/login/',view_func=LoginView.as_view('login'))
app.add_url_rule('/register/',view_func=RegisterView.as_view('register'))

if __name__ == '__main__':
    app.run(debug=True)
