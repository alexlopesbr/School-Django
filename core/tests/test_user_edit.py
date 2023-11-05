from django.test import TestCase
from django.urls import reverse

from core.models import CustomUser
from staff.forms import UserForm


class UserEditViewTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            email='email@test.com',
            first_name='test_user',
            role='student'
        )

        session = self.client.session
        session['user_id'] = str(self.user.id)
        session.save()

    def test_get_user_edit_view(self):
        response = self.client.get(reverse('staff_user_edit'))

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], UserForm)
        self.assertEqual(response.context['user'], self.user)

    def test_user_edit_post_valid_form(self):
        user_data = {
            'email': self.user.email,
            'first_name': 'Updated Name',
            'role': 'student',
        }
        response = self.client.post(reverse('staff_user_edit'), user_data)
        self.assertRedirects(response, reverse('staff_user_list'))

        updated_user = CustomUser.objects.get(id=self.user.id)
        self.assertEqual(updated_user.first_name, 'Updated Name')

    def test_user_edit_post_invalid_form(self):
        invalid_user_data = {
            'first_name': '',
        }
        response = self.client.post(reverse('staff_user_edit'), invalid_user_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)
        self.assertTrue(response.context['form'].errors)
