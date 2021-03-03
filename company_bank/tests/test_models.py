from .test_setup import TestSetUp
from company.models import Company
from company_bank.models import CompanyBank


class CompanyModelTest(TestSetUp):

    def test_company_bank(self):
        company_bank = CompanyBank.objects.get(id=1)
        field_label = CompanyBank._meta.get_field('company_id').verbose_name
        company_bank_ifsc = company_bank.ifsc
        self.assertEquals(CompanyBank.objects.count(), 1)
        self.assertEquals(field_label, 'company id')
        self.assertEquals(int(company_bank_ifsc), 12423)

