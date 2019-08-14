from  flask  import  Blueprint,render_template
cms_bp = Blueprint('cms',__name__,subdomain='cms')


#子域名的首页
@cms_bp.route('/')
def  hello():
    return  render_template('cms_index.html')

@cms_bp.route('/ok/')
def  ok():
    return  "OK"
