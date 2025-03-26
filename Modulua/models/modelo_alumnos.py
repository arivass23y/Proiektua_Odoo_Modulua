from odoo import models, fields

class MiModelo(models.Model):
    _name = 'mi.alumnos'
    _description = 'Alumnos'

    izena = fields.Char(string='Izena', required=True)
    abizena = fields.Char(string='Abizena')
    email = fields.Char(string='Emaila')
    adina = fields.Integer(string='Adina')
    kurtsoa = fields.Char(string='Kurtsoa')

   # Función para exportar a PDF
    def pdf_exportatu(self):
        try:
            report_action = self.env['ir.actions.report'].search([('name', '=', 'Txostenak Ikasleak')], limit=1)
           
            if not report_action:
                raise ValueError("No se encontró la acción del reporte.")
            return report_action.report_action(self)
        
        except Exception as e:
            raise ValueError(f"Ocurrió un error al intentar obtener el reporte: {e}")
