from django.core.cache import cache
from django.test import TestCase

from core.cache import CachedData
from core.models import CustomUser


class UserListViewTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            email='email@test.com',
            first_name='test_user',
            role='student'
        )

    def test_cached_data(self):
        # Create an instance of CachedData
        user_liste_cached = CachedData(
            'cached_users_test',
            CustomUser,
            300
        ).cache_model()

        # Verify that the data is in the cache
        self.assertIsNotNone(cache.get('cached_users_test'))

        # Comparing the cached data with the actual data from the database
        actual_data = list(CustomUser.objects.all())
        self.assertEqual(user_liste_cached, actual_data)

    def tearDown(self):
        cache.clear()
