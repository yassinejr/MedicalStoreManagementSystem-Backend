from .test_setup import TestSetUp
from company.models import Company
from company_account.models import CompanyAccount


class CompanyModelTest(TestSetUp):

    def test_company_account(self):
        company_account = CompanyAccount.objects.get(id=1)
        field_label = CompanyAccount._meta.get_field('company_id').verbose_name
        company_account_transaction_type = company_account.transaction_type
        self.assertEquals(CompanyAccount.objects.count(), 1)
        self.assertEquals(field_label, 'company id')
        self.assertEquals(company_account_transaction_type, 'Debit')

