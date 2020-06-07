# -*- coding: utf-8 -*-
{
    'name': "Openeducat Semester",

    'summary': """
        This module assists to create semester under openeducat courses""",

    'description': """
        This module assists to create semester under openeducat courses
    """,

    'author': "Numan Ibn Mazid",
    'website': "https://www.facebook.com/numanibnmazid",

    'category': 'Education',
    'version': '13.0.1',

    'depends': ['openeducat_core'],

    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/semester_category.xml',
        'views/semester.xml',
        'views/course.xml',
        # 'data/course_pre_demo.xml',
        # 'data/demo.xml',
        'demo/course_demo.xml',
        'demo/semester_category_demo.xml',
        'demo/semester_demo.xml',
    ],
    'demo': [
        # 'demo/course_demo.xml',
        # 'demo/semester_category_demo.xml',
        # 'demo/semester_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
