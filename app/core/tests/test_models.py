from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        ##Test creating a user with an email is successful
        email = 'test@gmail.com'
        password = '1234'

        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEquals(user.email,email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_email_normalized(self):
        ##Test the email for new user is normalized
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email,'1234')
        self.assertEqual(user.email, email.lower())
    
    def test_new_user_invalid_email(self):
        ##Test creating user with no email raise error
        with self.assertRaises(ValueError):
            #test user with no email raise error
            get_user_model().objects.create_user(None,'1234')
    
    def test_craete_new_superuser(self):
        #Test creating a new super user
        user = get_user_model().objects.create_superuser(
            'test@gamil.com',
            '1234'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


