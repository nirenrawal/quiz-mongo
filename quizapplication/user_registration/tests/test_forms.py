from django.test import TestCase
from user_registration.forms import *


class TestUserForm(TestCase):
    
    def test_user_form_is_valid(self):
        form = UserForm(data = {
            'first_name': 'Lionel',
            'last_name': 'Messi',
            'email': 'messi@intermiami.com',
            'username': 'messi',
            'password': 'messi123'
        })
        
        self.assertTrue(form.is_valid())
        
    def test_user_form_is_not_valid(self):
        form = UserForm(data = {
            'first_name': 'Lionel',
            'last_name': 'Messi',
            'email': 'messi@intermiami.com',
            'username': 'messi',
            'password': ''
        })
        
        self.assertEqual(len(form.errors), 1)
        self.assertFalse(form.is_valid())
        
        
class TestUserInfoForm(TestCase):
    
    def test_user_info_form_is_valid(self):
        form = UserForm(data = {
            'username': 'messi',
            'password': 'messi123',
            'address': 'Odense',
            'phone': '22334455',
            'profile_image': None
        })
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())
        
    def test_user_info_form_is_not_valid(self):
        form = UserForm(data = {})
        
        self.assertEqual(len(form.errors), 2)
        self.assertFalse(form.is_valid())