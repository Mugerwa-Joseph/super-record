from django.test import TestCase
from django.core.exceptions import ValidationError
from ..forms import ProductCreationForm, EditProductForm

class RoleCreationFormTest(TestCase):
    def setUp(self):
        self.prod_creater = ProductCreationForm()
        self.prod_creater2 = ProductCreationForm(
            data={
                'name': 'sugar',
                'description': 'This is a stock of kakira sugar',
                'quantity': 10,
                'unit_price': 4000.0
            }
        )

    def test_product_name_field_label(self):
        self.assertFalse(self.prod_creater.fields['name'].label == None)
        self.assertFalse(self.prod_creater.fields['name'].label == 'name')
    
    def test_product_description_field_label(self):
        self.assertFalse(self.prod_creater.fields['description'].label == None)
        self.assertFalse(self.prod_creater.fields['description'].label == 'description')
    
    def test_product_quantity_field_label(self):
        self.assertFalse(self.prod_creater.fields['quantity'].label == None)
        self.assertFalse(self.prod_creater.fields['quantity'].label == 'quantity')
    
    def test_product_unit_price_field_label(self):
        self.assertFalse(self.prod_creater.fields['unit_price'].label == None)
        self.assertFalse(self.prod_creater.fields['unit_price'].label == 'unit_price')

    def test_form_is_valid(self):
        self.assertTrue(self.prod_creater2.is_valid())

    def test_form_is_not_valid(self):
        self.assertFalse(self.prod_creater.is_valid())


class EditProductFormTest(TestCase):
    def setUp(self):
        self.prod_creater = EditProductForm()
        self.prod_creater2 = EditProductForm(
            data={
                'name': 'sugar',
                'description': 'This is a stock of kakira sugar',
                'quantity': 10,
                'unit_price': 4000.0
            }
        )

    def test_product_name_field_label(self):
        self.assertFalse(self.prod_creater.fields['name'].label == None)
        self.assertFalse(self.prod_creater.fields['name'].label == 'name')
    
    def test_product_description_field_label(self):
        self.assertFalse(self.prod_creater.fields['description'].label == None)
        self.assertFalse(self.prod_creater.fields['description'].label == 'description')
    
    def test_product_quantity_field_label(self):
        self.assertFalse(self.prod_creater.fields['quantity'].label == None)
        self.assertFalse(self.prod_creater.fields['quantity'].label == 'quantity')
    
    def test_product_unit_price_field_label(self):
        self.assertFalse(self.prod_creater.fields['unit_price'].label == None)
        self.assertFalse(self.prod_creater.fields['unit_price'].label == 'unit_price')

    def test_form_is_valid(self):
        self.assertTrue(self.prod_creater2.is_valid())

    def test_form_is_not_valid(self):
        self.assertFalse(self.prod_creater.is_valid())