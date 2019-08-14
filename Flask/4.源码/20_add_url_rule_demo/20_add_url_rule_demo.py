from flask import Flask,url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    #构建url  ：/list/
    #研究app.add_url_rule()方法，若方法中【没有加】上endpoint时，可通过原来的函数名构建url，即url_for('原函数名')
    # print(url_for('my_list'))
    #研究app.add_url_rule()方法，若方法中【加上】endpoint时，不能再通过原来的函数名构建url，而需要endpoint的值才行
    # 即url_for('endpoint值')
    # print(url_for('mli'))

    #构建url：/profile/
    # print(url_for('profile'))
    print(url_for('pf'))  #@app.route('/profile/',endpoint='pf')
    return 'Hello World!'

# @app.route('/profile/')
@app.route('/profile/',endpoint='pf')
def  profile():
    return  "个人信息"


def my_list():
    return "我是列表页"

#通过app对象的add_url_rule方法 来完成url与视图函数的映射
# app.add_url_rule('/list/',view_func=my_list)
app.add_url_rule('/list/',endpoint='mli',view_func=my_list)


#讨论：add_url_rule()方法  与@app.route()装饰器的关系
#结论：@app.route()装饰器 底层就是借助于add_url_rule()方法来实现的


if __name__ == '__main__':
    app.run(debug=True)
