# -*- coding: utf-8 -*-
{
    'name' : "Purchase Advance Payment odoo",
    "author": "Edge Technologies",
    'version': '13.0.1.0',
    'live_test_url': "https://youtu.be/CQz-7-6cjgE",
    "images":['static/description/main_screenshot.png'],
    'summary': 'Vendor Advance Payment for purchase order Advance Payment purchase Advance Payment Allocation Supplier Advance expense advance payment Vendor Payment Adjustment Account Advance Payment apply advance payment on invoice make advance payment for vendor bills.',
    'description' : """ This app help to user, make advance payment and posted journal entries from purchase order, also maintain Advance Payment History in Purchase.

Purchase Advance Payment
Customer Advance payment 
Odoo Advance Payment for purchase order
payment in Advance Payment purchase Advance Payment
so Advance Payment po Advance Payment
payment before
payment first
first payment 
Advance Payments 
Advance Payment Allocation
Supplier Advance Payments different payment 
Advance Payment Allocation expense advance and submit expense claim
Customer and Vendor Payment Adjustment
Account Advance Payment
Customer payment Advance
Supplier/Vendor Advance payment
Supplier Advance payment
Vendor Advance payment Supplier Advance Payments Management
Vendor Advance payment
advance payment on Purchase Orders
Payment of vendor/supplier on Purchase Order
advance payment
apply advance payment on invoice
make advance payment for invoices
add advance payment for vendor bills
make advance payment for customer invoice
customer advance payment link agaist invoice
reconcile advance payment agaist outstanding invoice
pay before purchase

Advance Payment is necessary feature for any ERP System. 
Odoo Doesn't have feature to add Advance Payment of Invoice from Purchase. 
This app help to user to make advance payment from Purchase Order which creates posted journal entries from after the payment done.
This apps also maintain Advance Payment History in Purchase Order in Odoo accounting.
Advance payment history on purchase order


     """,
    "license" : "OPL-1",
    'depends' : ['purchase','account','sh_message'],
    'data': [
                'security/advance_payment_group.xml',
                'security/ir.model.access.csv',
                'views/purchase_order_view.xml',
                'wizard/purchase_advance_payment_wizard.xml',
             ],
    'installable': True,
    'auto_install': False,
    'price': 7,
    'currency': "EUR",
    'category': 'Accounting',
}
