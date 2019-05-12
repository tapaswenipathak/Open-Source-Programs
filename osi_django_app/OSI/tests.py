from django.test import TestCase
from django.shortcuts import reverse
from .models import soc, osc, univ_soc_woc

# Create your tests here.

class HomePageTest(TestCase):

    def test_index_page_request(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'OSI/index.html')

class SocPageTest(TestCase):

    def test_soc_page_request(self):
        response = self.client.get(reverse('soc'))
        self.assertEqual(response.status_code, 200)

    def test_soc_page_returns_correct_html(self):
        response = self.client.get(reverse('soc'))
        self.assertTemplateUsed(response, 'OSI/soc.html')

    def test_can_save_a_new_soc(self):
        self.client.post(reverse('soc-create'), {'title':'test','homepage':'https://www.test.com'})
        self.assertEqual(soc.objects.count(), 1)

    def test_does_contain_soc_without_being_published(self):
        self.client.post(reverse('soc-create'), {'title':'test','homepage':'https://www.test.com'})
        response = self.client.get(reverse('soc'))
        self.assertNotContains(response, 'test')

    def test_does_contain_soc_after_being_published(self):
        self.client.post(reverse('soc-create'), {'title':'test','homepage':'https://www.test.com','publish':True})
        response = self.client.get(reverse('soc'))
        self.assertNotContains(response, 'test')

class OscPageTest(TestCase):

    def test_osc_page_request(self):
        response = self.client.get(reverse('osc'))
        self.assertEqual(response.status_code, 200)

    def test_osc_page_returns_correct_html(self):
        response = self.client.get(reverse('osc'))
        self.assertTemplateUsed(response, 'OSI/osc.html')

    def test_can_save_a_new_osc(self):
        self.client.post(reverse('osc-create'), {'title':'test','homepage':'https://www.test.com', 'awards':'some random award'})
        self.assertEqual(osc.objects.count(), 1)

    def test_does_contain_osc_without_being_published(self):
        self.client.post(reverse('osc-create'), {'title':'test','homepage':'https://www.test.com', 'awards':'some random award'})
        response = self.client.get(reverse('osc'))
        self.assertNotContains(response, 'test')

    def test_does_contain_osc_after_being_published(self):
        self.client.post(reverse('osc-create'), {'title':'test','homepage':'https://www.test.com', 'awards':'some random award','publish':True})
        response = self.client.get(reverse('osc'))
        self.assertNotContains(response, 'test')

class U_Soc_Woc_PageTest(TestCase):

    def test_usocwoc_page_request(self):
        response = self.client.get(reverse('u-soc-woc'))
        self.assertEqual(response.status_code, 200)

    def test_usocwoc_page_returns_correct_html(self):
        response = self.client.get(reverse('u-soc-woc'))
        self.assertTemplateUsed(response, 'OSI/u-soc-woc.html')

    def test_can_save_a_new_usocwoc(self):
        self.client.post(reverse('u_woc_soc-create'), {'title':'test','homepage':'https://www.test.com', 'awards':'some random award'})
        self.assertEqual(univ_soc_woc.objects.count(), 1)

    def test_does_contain_usocwoc_without_being_published(self):
        self.client.post(reverse('u_woc_soc-create'), {'title':'test','homepage':'https://www.test.com', 'awards':'some random award'})
        response = self.client.get(reverse('u-soc-woc'))
        self.assertNotContains(response, 'test')

    def test_does_contain_usocwoc_after_being_published(self):
        self.client.post(reverse('u_woc_soc-create'), {'title':'test','homepage':'https://www.test.com', 'awards':'some random award','publish':True})
        response = self.client.get(reverse('u-soc-woc'))
        self.assertNotContains(response, 'test')

class FormRedirectsTests(TestCase):

    def test_soc_create_from_redirects_after_post_request(self):
        response = self.client.post(reverse('soc-create'), {'title':'test','homepage':'https://www.test.com'})
        self.assertRedirects(response, reverse('soc'))

    def test_osc_create_from_redirects_after_post_request(self):
        response = self.client.post(reverse('osc-create'), {'title':'test','homepage':'https://www.test.com', 'awards':'some random award'})
        self.assertRedirects(response, reverse('osc'))

    def test_usocwoc_create_from_redirects_after_post_request(self):
        response = self.client.post(reverse('u_woc_soc-create'), {'title':'test','homepage':'https://www.test.com', 'awards':'some random award'})
        self.assertRedirects(response, reverse('u-soc-woc'))
