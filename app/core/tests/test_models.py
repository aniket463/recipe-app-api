from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@gmail.com',password='test1234'):
    return get_user_model().objects.create_user(email,password)


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
    


    def test_tag_str(self):
        #Test the tag string representation
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )
        self.assertEqual(str(tag), tag.name)
    

    def test_ingredient_str(self):
        #Test the ingredent string representation
        ingredient = models.Ingredient.objects.create(
            user = sample_user(),
            name='Cucumber'
        )
        self.assertEqual(str(ingredient), ingredient.name)
    
    def test_recipe_str(self):
        #Test the recipe string representaions
        recipe = models.Recipe.objects.create(
            user = sample_user(),
            title = 'Streak and mushroom sauce',
            time_minutes = 5,
            price = 5.00
        )
        self.assertEqual(str(recipe),recipe.title)


