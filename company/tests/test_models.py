from .test_setup import TestSetUp
from company.models import Company


class CompanyModelTest(TestSetUp):

    def test_company_name(self):
        company = Company.objects.get(id=1)
        field_label = Company._meta.get_field('name').verbose_name
        company_name = company.name
        self.assertEquals(Company.objects.count(), 1)
        self.assertEquals(field_label, 'name')
        self.assertEquals(company_name, 'Pharmacie Djerba')

