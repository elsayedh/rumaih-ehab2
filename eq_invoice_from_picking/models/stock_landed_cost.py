# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright 2019 EquickERP
#
##############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime , timedelta, date
from odoo.exceptions import UserError

class stocklandaccount(models.Model):
    _inherit = "account.move"

    def button_create_landed_costs(self):
        """Create a `stock.landed.cost` record associated to the account move of `self`, each
        `stock.landed.costs` lines mirroring the current `account.move.line` of self.
        """
        self.ensure_one()
        landed_costs_lines = self.line_ids.filtered(lambda line: line.is_landed_costs_line)

        landed_costs = self.env['stock.landed.cost'].create({
            'vendor_bill_id': self.id,
            'picking_ids' :self.stock_picking_ids,
            'cost_lines': [(0, 0, {
                'product_id': l.product_id.id,
                'name': l.product_id.name,
                'account_id': l.product_id.product_tmpl_id.get_product_accounts()['stock_input'].id,
                'price_unit': l.currency_id._convert(l.price_subtotal, l.company_currency_id, l.company_id,
                                                     l.move_id.date),
                'split_method': 'equal',
            }) for l in landed_costs_lines],
        })
        action = self.env.ref('stock_landed_costs.action_stock_landed_cost').read()[0]
        return dict(action, view_mode='form', res_id=landed_costs.id, views=[(False, 'form')])


# class StockLandCostTotal(models.Model):
#     _inherit = "stock.landed.cost"



