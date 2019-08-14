#新闻模块   crud
from flask  import  Blueprint,render_template,url_for
# news_bp = Blueprint('news',__name__,url_prefix='/news')  #常规
news_bp = Blueprint('news',__name__,url_prefix='/news',template_folder='news_page',static_folder='news_static')

#n个功能
#查询所有的新闻信息
@news_bp.route('/newslist/')
def  news_list():
    # return "返回所有的新闻信息"
    #url_for反转蓝图注意事项  构建/news/detail/   场景3
    print(url_for('news.detail'))
    return  render_template('news_list.html')


#查询某新闻信息详情
@news_bp.route('/detail/')
def  detail():
    return "新闻详情"