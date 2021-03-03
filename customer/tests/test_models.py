from .test_setup import TestSetUp
from customer.models import Customer


class CustomerModelTest(TestSetUp):

    def test_customer_name(self):
        customer = Customer.objects.get(id=1)
        field_label = Customer._meta.get_field('name').verbose_name
        customer_name = customer.name
        self.assertEquals(Customer.objects.count(), 1)
        self.assertEquals(field_label, 'name')
        self.assertEquals(customer_name, 'customer zarzis')

