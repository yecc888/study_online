__author__ = 'yecc'
__date__ = '2019/2/12 13:54'

import xadmin
from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['desc', 'name', 'add_time']
    list_filter = ['desc', 'name']
    search_fields = ['desc', 'name', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['desc', 'name', 'add_time', 'click_nums', 'fav_nums',
                    'image', 'address', 'city', 'students', 'course_nums',
                    ]
    list_filter = ['desc', 'name', 'click_nums', 'fav_nums',
                   'image', 'address', 'city', 'students', 'course_nums',
                   ]
    search_fields = ['desc', 'name', 'add_time', 'click_nums', 'fav_nums',
                     'image', 'address', 'city', 'students', 'course_nums',
                     ]


class TeacherAdmin(object):
    list_display = ['org', 'name', 'add_time', 'click_nums', 'fav_nums',
                    'image', 'work_years', 'work_company', 'work_position', 'age',
                    'points']
    list_filter = ['org', 'name', 'click_nums', 'fav_nums',
                   'image', 'work_years', 'work_company', 'work_position', 'age',
                   'points']
    search_fields = ['org', 'name', 'add_time', 'click_nums', 'fav_nums',
                     'image', 'work_years', 'work_company', 'work_position', 'age',
                     'points']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
