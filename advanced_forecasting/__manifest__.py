'name': 'Advanced Sales Forecasting',
    'version': '1.3',
    'summary': 'Advanced sales forecasting using Prophet in Odoo 18',
    'description': """
        This module provides advanced sales forecasting using the Prophet library,
        with a wizard for interactive forecast generation, a printable report, and a dashboard view.
    """,
    'author': 'Kamal',
    'category': 'Sales',
    'depends': ['base', 'sale_management', 'report'],
    'module_type': 'official',
    'data': [
        'security/ir.model.access.csv',
        'views/forecasting_views.xml',
        'wizards/forecast_wizard.xml',
        'reports/forecast_report.xml',
    ],
    'installable': True,
    'application': True,
}