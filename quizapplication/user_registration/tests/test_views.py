from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from user_registration.models import *
from user_registration.views import *



class TestIndexView(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.index = reverse('user_registration:index')
    
    def test_index_view(self):
        self.client
        response = self.client.get(self.index)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_registration/index.html')
        
        
        
class TestUserProfile(TestCase):
    
    def setUp(self):
        self.user = User.objects.create(
            username = 'user1', 
            password = 'password1',
        )
        self.user_info = UserInfo.objects.create(
            user = self.user,
            address = 'myaddress',
            phone = '23423423',   
        )
        
        
    def test_user_profile_view_with_authorized_user(self):
        self.client.force_login(self.user)
        url = reverse('user_registration:user_profile', args=[self.user.id])
        response = self.client.get(url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_registration/user_profile.html')
        self.assertContains(response, self.user_info.address)
        self.assertContains(response, self.user_info.phone)
        self.assertEqual(response.context['user'], self.user)
        self.assertEquals(response.context['user_info'], self.user_info)
    
    
    def test_user_profile_view_with_unauthorized_user(self):
        url = reverse('user_registration:user_profile', args=[self.user.id])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 302)
        expected = reverse('user_registration:user_login') + '?next=' + url
        self.assertRedirects(response, expected)
        
        # print(f'this is Response{response}')
        # print(f'this is expected url {expected}')
        
        
class TestUserLoginView(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            username = 'user1', 
            password = 'password1',
        )
        
    def test_user_login(self):
        url = reverse('user_registration:user_login') 
        response = self.client.post(url, {
            'username': 'user1',
            'password': 'password1',
        })
        self.assertEqual(response.status_code, 200)
        
        
    def test_user_login_with_invalid_credentials(self):
        url = reverse('user_registration:user_login')
        response = self.client.post(url, {
            'username': 'user1', 
            'password': 'wrongpassword'
            })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid login detail.")
        
        
        
class TestRegisterView(TestCase):
    
    def setUp(self):
        self.client = Client()
    
    def test_register_view(self):
        data = {
            'username': 'Neymar',
            'password': 'password',
            'email': 'neymar@neymar.com',
            'address': 'koebenhavn',
            'phone': '22334455',
        }
        response = self.client.post(reverse('user_registration:register'), data)
        self.assertRedirects(response, reverse('user_registration:user_login'))
        self.assertTrue(UserInfo.objects.filter(address='koebenhavn').exists())
        self.assertTrue(User.objects.filter(username='Neymar').exists())
        
        
class TestLogoutView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='Neymar', password='mypassword')
        
    def test_logout(self):
        self.client.login(username='Neymar', password='mypassword')
        url = reverse('user_registration:user_logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertNotIn('_auth_user_id', self.client.session)