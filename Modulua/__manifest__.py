{
    'name': 'Ikasleak',
    'version': '1.0',
    'summary': 'Ikasleen datuak bistaratzeko modulua',
    'description': 'Hau modulu bat da ikasleen datuak ikusteko eta PDF bezala deskargatzeko.',
    'author': 'Talde 3',
    'category': 'Custom',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/vista_alumnos.xml',
        'report/report_alumno.xml'
    ],
    'installable': True,
    'application': True,
}
