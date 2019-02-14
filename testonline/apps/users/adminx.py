__author__ = 'yecc'
__date__ = '2019/2/11 19:42'
import xadmin
from xadmin import views
from .models import EmailVerfyRecord, Banner


class BaseSetting(object):
    """基础配置"""
    enable_themes = True  # 打开主题
    use_bootswatch = True


class GlobalSettings(object):
    """全局配置"""
    site_title = '测试学习在线系统'
    site_footer = 'Yecc Tester'
    menu_style = 'accordion'


class EmailVerfyRecordAdmin(object):
    list_display = ['code', 'email', 'send_tpye', 'send_time']
    list_filter = ['code', 'email', 'send_tpye']
    search_fields = ['code', 'email', 'send_tpye', 'send_time']
    refresh_times = (3, 5)


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'add_time', 'index']
    list_filter = ['title', 'image', 'url', 'index']
    search_fields = ['title', 'image', 'url', 'add_time', 'index']
    refresh_times = (3, 5)


xadmin.site.register(EmailVerfyRecord, EmailVerfyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
