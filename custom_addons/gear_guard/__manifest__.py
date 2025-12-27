{
    'name': "GearGuard",
    'summary': "The Ultimate Maintenance Tracker",
    'description': """
        Hackathon Project:
        - Manage Equipment & Teams
        - Track Maintenance Requests (Corrective/Preventive)
    """,
    'author': "Your Name",
    'category': 'Manufacturing/Maintenance',
    'version': '1.0',
    'depends': ['base', 'mail', 'hr'], # We need Mail for chatter and HR for departments
    'data': [
        'security/ir.model.access.csv',
        'views/equipment_views.xml',
        'views/team_views.xml',
        'views/maintenance_request_views.xml',
        'views/menu.xml',
    ],
    'application': True, # Makes it appear as a main App on the dashboard
}