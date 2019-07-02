# -*- coding: utf-8 -*-
{
    'name': "My Academy",

    'summary': """Manage Trainings and Preprations""",

    'description': """
        My Academy module for managing trainings and different exam preprations:
            - Training courses
            - Training sessions
            - Exam Prepration
            - Test Prepration
            - Attendees registration
            
    """,

    'author': "Muhammad Ahsan",
    'website': "http://zawster.wordpress.com",

    'category': 'Education',
    'version': '1.1',

    'depends': ['base'],
    # Always Loaded
    'data' : [
        'security/ir.model.access.csv',
        'views/school.xml'
    ],

    'installable': True,
    'application': False,
    'auto_install': False,

}
