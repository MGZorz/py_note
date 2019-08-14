from flask import Flask,url_for,render_template
from blueprints.users import users_bp
from blueprints.news import news_bp
from blueprints.cms import cms_bp
app = Flask(__name__)

#注册蓝图
app.register_blueprint(users_bp)
app.register_blueprint(news_bp)
app.register_blueprint(cms_bp)

app.config['SERVER_NAME']="momo.com:5000"

@app.route('/')
def hello_world():
    #url_for反转蓝图注意事项  构建/news/detail/   场景1
    print(url_for('news.detail'))  #url_for('蓝图名称.视图函数名')
    # return 'Hello World!'
    return render_template('index.html')

#有n个模块
#用户模块
#读书模块
#电影模块
#新闻模块

if __name__ == '__main__':
    app.run(debug=True)
