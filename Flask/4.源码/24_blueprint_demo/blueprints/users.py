#用户模块  crud
from flask  import  Blueprint,url_for
users_bp= Blueprint('users',__name__,url_prefix='/user')

#跟用户相关的功能

#查看用户信息
@users_bp.route('/profile/')
def  profile():
    print(url_for('news.detail'),'用户')
    return "返回用户的详情"

#设置用户信息
@users_bp.route('/settings/')
def  settings():
    return "这是个人设置中心"



