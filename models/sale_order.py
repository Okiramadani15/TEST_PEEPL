from odoo import models, fields
from odoo.exceptions import ValidationError

class SalesOrder (models.Models):
    for order in self: 
        if order.amount_total < 500000:
            raise ValidationError("Minimal order  value adalah 500.000")
        

    return super (SalesOrder, self).action_confirm()