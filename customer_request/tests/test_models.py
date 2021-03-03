from .test_setup import TestSetUp
from customer_request.models import CustomerRequest


class CustomerRequestModelTest(TestSetUp):

    def test_customer_request_name(self):
        customer_request = CustomerRequest.objects.get(id=1)
        field_label = CustomerRequest._meta.get_field('customer_name').verbose_name
        customer_request_name = customer_request.customer_name
        self.assertEquals(CustomerRequest.objects.count(), 1)
        self.assertEquals(field_label, 'customer name')
        self.assertEquals(customer_request_name, 'customer zarzis')

