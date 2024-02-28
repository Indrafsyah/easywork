from odoo import models, fields,api

from odoo.exceptions import ValidationError

class Material(models.Model):
    _name = 'material.management.material'
    _description = 'Materials for Sale'

    material_code = fields.Char(string='Material Code', required=True)
    material_name = fields.Char(string='Material Name', required=True)
    material_type = fields.Selection(
        [('fabric', 'Fabric'), ('jeans', 'Jeans'), ('cotton', 'Cotton')],
        string='Material Type',
        required=True,
    )
    material_buy_price = fields.Float(string='Material Buy Price', required=True)
    related_supplier = fields.Many2one('res.partner', string='Related Supplier')


    @api.constrains('material_buy_price')
    def _check_buy_price(self):
        for record in self:
            print(record)
            if record.material_buy_price < 100:
                raise ValidationError("Material Buy Price must be greater than or equal to 100.")
