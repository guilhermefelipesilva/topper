from snippets.models import Snippet
import pytest

@pytest.mark.django_db
def test_save():
    
    snippet = Snippet(code='js: alert(oi)')
    snippet.save()
    print(snippet.code)
    assert snippet.code == "js: alert(oi)"


from django.test import TestCase


class TestSnippet(TestCase):

    def setUp(self):
        self.snippet = Snippet(code='print "pytest da hora"\n')
        self.snippet.save()

    def test_save(self):
        print(self.snippet.code)
        self.assertEqual(self.snippet.code, 'print "pytest da hora"\n')
