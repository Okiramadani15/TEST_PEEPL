from odoo import models, fields

class Project(models.Model):
    _inherit = 'project.project'

    lokasi_project = fields.Text(string="lokasi project")
    source_aplikasi_pendukung = fields.char(string="source_aplikasi_pendukung")
    daftar_perkerja_remote= fields.Serialized(string="daftar pekerja remote")
