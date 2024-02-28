from odoo import http
from odoo.http import request
import json
import logging

_logger = logging.getLogger(__name__)

from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')  # Customize the format as needed
        return super(DateTimeEncoder, self).default(obj)

class MaterialController(http.Controller):

    # Get all materials
    @http.route('/api/materials', type='http', auth='public', methods=['GET'], csrf=False)
    def get_materials(self,**kw):
        materials = request.env['material.management.material'].search([]).read()
        return json.dumps(materials, cls=DateTimeEncoder)

    # Get materials by id
    @http.route('/api/materials/<int:material_id>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_material(self, material_id, **kw):
        material = request.env['material.management.material'].browse(material_id).read()
        return json.dumps(material, cls=DateTimeEncoder)

    # Create Materials
    @http.route('/api/materials/create', type='json', auth='public', methods=['POST'], csrf=False)
    def create_material(self, **kw):
        
        if 'material_code' not in kw:
            return json.dumps({'error': 'Material Code is mandatory'})

        # Create the new material with the mandatory fields set
        new_material = request.env['material.management.material'].create({
            'material_code': kw['material_code'],
            'material_name': kw.get('material_name'),
            'material_type': kw.get('material_type'),
            'material_buy_price': kw.get('material_buy_price'),
            'related_supplier': kw.get('related_supplier'),
        })

        return json.dumps({'id': new_material.id})

    # Update Materials
    @http.route('/api/materials/update/<int:material_id>', type='json', auth='public', methods=['POST'], csrf=False)
    def update_material(self, material_id, **kw):
        material_check = request.env['material.management.material'].browse(material_id).read()
        if not material_check:
             return json.dumps({'success': False, 'error': 'Material ID Not Found'})
        else:
            material = request.env['material.management.material'].browse(material_id)
            material.write({
            'material_code': kw.get('material_code'),
            'material_name': kw.get('material_name'),
            'material_type': kw.get('material_type'),
            'material_buy_price': kw.get('material_buy_price'),
            'related_supplier': kw.get('related_supplier'),
        })
        return json.dumps({'id': material.id})

    # Delete Materials
    @http.route('/api/materials/delete/<int:material_id>', type='json', auth='public', methods=['POST'], csrf=False)
    def delete_material(self, material_id, **kw):

        material_check = request.env['material.management.material'].browse(material_id).read()
        if not material_check:
             return json.dumps({'success': False, 'error': 'Material ID Not Found'})
        else:
            material = request.env['material.management.material'].browse(material_id)
            material.unlink()
            return json.dumps({'success': True})
