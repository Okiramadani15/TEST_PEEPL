from odoo import models, fields
from odoo.exceptions import ValidationError

class SalesOrder (models.Models):
    _inherit = 'sale.order'

    def action_confirm(self):
       for order in self: 
          if order.amount_total < 500000:
              raise ValidationError("Minimal order  value adalah 500.000")
        

          return super (SalesOrder, self).action_confirm()
