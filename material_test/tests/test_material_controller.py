from odoo.tests import HttpCase
import json

class TestMaterialController(HttpCase):

    def test_get_materials(self):
        response = self.url_open('/api/materials')
    
        self.assertEqual(response.status_code, 200)

        materials = json.loads(response.text)
        print("Finish Testing 'get_materials'===================",response)

        return response

    def test_get_material(self):
        material_id = 29  
        response = self.url_open(f'/api/materials/{material_id}')
       
        self.assertEqual(response.status_code, 200)
        material = json.loads(response.text)
        print("Finish Testing 'get_materials By Id'===================",response)
        return response


    def test_create_material(self):
        material_data = {
            "jsonrpc": "2.0",
            "params": {
                "material_code": "D-009",
                "material_name": "Sample Fabric",
                "material_type": "fabric",
                "material_buy_price": 190.00,
                "related_supplier": 10
            }
        }

        response = self.url_open('/api/materials/create', headers={"Content-Type": "application/json"}, data=json.dumps(material_data))
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.text)
        print("Finish 'create_material By ID'===================",response)
        return response


    def test_update_material(self):
        material_id = 29
        update_data = {
            "material_code": "D-0091212",
            "material_name": "Sample Fabric",
            "material_type": "fabric",
            "material_buy_price": 1200.00,
            "related_supplier": 14
        }

        response = self.url_open(f'/api/materials/update/{material_id}', headers={"Content-Type": "application/json"}, data=json.dumps(update_data))
        self.assertEqual(response.status_code, 200)

        result = json.loads(response.text)

        print("Finish 'update_material By ID'===================",response)
        return response


    def test_delete_material(self):
        material_id = 29

        request_data = {
            'method': 'DELETE',
            'headers': {"Content-Type": "application/json"},
        }

        response = self.url_open(f'/api/materials/delete/{material_id}', headers={"Content-Type": "application/json"}, data=json.dumps(request_data))
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.text)
        print("Finish 'delete_material By ID'===================",response)
        return response
