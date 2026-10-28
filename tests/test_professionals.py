"""Validate professional publication gates and generated public pages."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '_gen'))
import professionals as directory


def fixture():
    return dict(slug='perfil-teste',name='Pessoa <Teste>',title='Psicóloga',kind='psicologia',registration='06/123456',formation='Formação de teste',bio='Apresentação de teste',audience='Adultos',modes=['Online'],location='Online',contact_url='https://example.com/contato',email='teste@example.com',relationship='owner',reviewed_on='2026-10-28',consent_publication=True,published=True)


class ProfessionalDirectoryTest(unittest.TestCase):
    def load(self, entries):
        with tempfile.TemporaryDirectory() as temp:
            path=Path(temp)/'profiles.json'
            path.write_text(json.dumps(entries),encoding='utf-8')
            return directory.load_profiles(path)

    def test_incomplete_drafts_are_not_public(self):
        self.assertEqual(self.load([{'published':False,'email':'private@example.com'}]),[])

    def test_publication_requires_consent_and_credentials(self):
        for field,value in [('consent_publication',False),('registration',''),('formation',''),('modes',[])]:
            with self.subTest(field=field):
                p=fixture();p[field]=value
                with self.assertRaises(ValueError): self.load([p])

    def test_rejects_unsafe_paths_contacts_and_duplicates(self):
        for field,value in [('slug','../outside'),('slug','index'),('contact_url','javascript:alert(1)'),('contact_url','https://example.com/?symptoms=private'),('email','x@example.com\nBcc:other@example.com')]:
            with self.subTest(field=field,value=value):
                p=fixture();p[field]=value
                with self.assertRaises(ValueError): self.load([p])
        with self.assertRaises(ValueError): self.load([fixture(),fixture()])

    def test_profile_is_escaped_transparent_and_ad_free(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(directory,'load_profiles',return_value=[fixture()]):
            directory.write_professionals(temp)
            page=(Path(temp)/'profissionais/perfil-teste.html').read_text(encoding='utf-8')
            self.assertIn('Pessoa &lt;Teste&gt;',page)
            self.assertIn('divulgação de serviço próprio',page)
            self.assertIn('CRP 06/123456',page)
            self.assertIn('rel="noopener noreferrer"',page)
            self.assertIn('content="no-referrer"',page)
            self.assertNotIn('pagead2',page)
            self.assertIn('mailto:teste@example.com',page)

    def test_empty_directory_never_invents_a_professional(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(directory,'load_profiles',return_value=[]):
            directory.write_professionals(temp)
            page=(Path(temp)/'profissionais/index.html').read_text(encoding='utf-8')
            self.assertIn('Ainda não há perfis',page)
            self.assertNotIn('care-card',page)
            self.assertNotIn('pagead2',page)
            self.assertIn('https://amorfy.com.br/profissionais/"',page)

if __name__ == '__main__': unittest.main()
