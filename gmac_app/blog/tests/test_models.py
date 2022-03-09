from django.test import TestCase
from wagtail.tests.utils import WagtailPageTests
from wagtail.tests.utils.form_data import nested_form_data, streamfield

from home.models import HomePage
from blog.models import BlogPage


class BlogPageTests(WagtailPageTests):
    def test_can_create_blog_page_under_home(self):
        self.assertCanCreate(HomePage, HomePage)

    def test_can_create_blog_page(self):
        # Can create blog page with the required data
        root_page = HomePage.objects.first()
        self.assertCanCreate(
            root_page,
            BlogPage,
            nested_form_data({"title": "About us"}),
        )
