from django.test import TestCase
from django.contrib.auth import get_user_model
from wagtail.tests.utils import WagtailPageTests
from wagtail.tests.utils.form_data import nested_form_data, streamfield, inline_formset
from wagtail.images.tests.utils import Image, get_test_image_file

from home.models import HomePage
from blog.models import BlogPage


class BlogPageTests(WagtailPageTests):
    def setUp(self):
        # Create an image for tests
        self.image = Image.objects.create(
            title="Test image",
            file=get_test_image_file(),
        )
        self.user = get_user_model().objects.create_superuser(
            email="test@test.com", password="test"
        )

    def test_can_create_blog_page_under_home(self):
        self.assertCanCreateAt(HomePage, HomePage)

    def test_can_create_blog_page(self):
        # Can create blog page with the required data
        self.client.force_login(self.user)
        root_page = HomePage.objects.first()
        data = nested_form_data(
            {"title": "About us", "read_length": 2, "head_image": ""}
        )
        self.assertCanCreate(root_page, BlogPage, data)
