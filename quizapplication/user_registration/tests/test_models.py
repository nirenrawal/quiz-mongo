from django.test import TestCase
from django.contrib.auth.models import User
from user_registration.models import UserInfo



class TestUserInfoModel(TestCase):
    
    def setUp(self):
        self.user = User.objects.create(
            username = 'noel',
            password = 'noel123'
        )
        
    def test_user_info_model(self):
        user_info = UserInfo.objects.create(
            user = self.user,
            address = 'Japan',
            phone = '99333388',
            profile_image = None
        )
        
        self.assertEqual(user_info.user, self.user)
        self.assertEqual(user_info.address, 'Japan')
        self.assertEqual(user_info.profile_image, None)
        self.assertEqual(str(user_info), 'noel')
        