from django.test import SimpleTestCase
from django.urls import reverse, resolve
from user_registration.views import *


class TestUrls(SimpleTestCase):
    
    def test_index_url(self):
        url = reverse('user_registration:index')
        # print(resolve(url))
        self.assertEqual(url, '/')
        self.assertEqual(resolve(url).func, index)
        
        
    def test_register_url(self):
        url = reverse('user_registration:register')
        self.assertEqual(url, '/register/')
        self.assertEqual(resolve(url).func, register)
        
        
    def test_user_login_url(self):
        url = reverse('user_registration:user_login')
        self.assertEqual(url, '/user_login/')
        self.assertEqual(resolve(url).func, user_login)
        
    
    def test_user_logout_url(self):
        url = reverse('user_registration:user_logout')
        self.assertEqual(url, '/user_logout/')
        self.assertEqual(resolve(url).func, user_logout)
        
        
    def test_user_profile_url(self):
        user_id = 1
        url = reverse('user_registration:user_profile', args=[user_id])
        self.assertEqual(url, f'/user_profile/{user_id}/')
        self.assertEqual(resolve(url).func, user_profile)
        
        
    def test_change_password_url(self):
        user_id = 1
        url = reverse('user_registration:change_password', args=[user_id])
        self.assertEqual(url, f'/change_password/{user_id}/')
        self.assertEqual(resolve(url).func, change_password)
        
        
    def test_upload_profile_image_url(self):
        user_id = 1
        url = reverse('user_registration:upload_profile_image', args=[user_id])
        self.assertEqual(url, f'/upload_profile_image/{user_id}/')
        self.assertEqual(resolve(url).func, upload_profile_image)
        
        
    def test_update_profile_url(self):
        user_id = 1
        url = reverse('user_registration:update_profile', args=[user_id])
        self.assertEqual(url, f'/update_profile/{user_id}/')
        self.assertEqual(resolve(url).func, update_profile)