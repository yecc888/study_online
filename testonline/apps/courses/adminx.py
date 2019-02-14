__author__ = 'yecc'
__date__ = '2019/2/12 12:53'

import xadmin
from .models import CourseResource, Course, Lesson, Video


class CourseAdmin(object):
    list_display = ['name', 'students', 'favour_num', 'click_num',
                    'image', 'desc', 'add_time', 'detail', 'degree', 'learn_times']
    list_filter = ['name', 'students', 'favour_num', 'click_num',
                   'image', 'desc', 'detail', 'degree', 'learn_times']
    search_fields = ['name', 'students', 'favour_num', 'click_num',
                     'image', 'desc', 'add_time', 'detail', 'degree', 'learn_times']
    refresh_times = (3, 5)


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    list_filter = ['course', 'name']
    search_fields = ['course', 'name', 'add_time']
    refresh_times = (3, 5)


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    list_filter = ['lesson', 'name']
    search_fields = ['lesson', 'name', 'add_time']
    refresh_times = (3, 5)


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    list_filter = ['course', 'name', 'download']
    search_fields = ['course', 'name', 'download', 'add_time']
    refresh_times = (3, 5)


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
