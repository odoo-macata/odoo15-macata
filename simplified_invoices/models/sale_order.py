from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    def create_simple_invoice(self, sale_orders, product_id):
        invoice_vals = sale_orders[0]._prepare_invoice()
        sol_obj = self.env['sale.order.line']
        invoice_line_vals = []
        for so in sale_orders:
            line_ids = so.mapped("order_line")
            amount = sum(line_ids.mapped("price_subtotal"))
            invoice_line_vals.append(
                (0, 0, sol_obj._prepare_simple_invoice_line(
                    so, product_id, amount, line_ids.ids
                )))
        invoice_vals['invoice_line_ids'] += invoice_line_vals
        move = self.env['account.move'].sudo().with_context(default_move_type='out_invoice').create(invoice_vals)
        return move

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    
    def _prepare_simple_invoice_line(self, so, product_id, amount, line_ids):
        return {
            'name': product_id.display_name + " - " + so.name,
            'product_id': product_id.id,
            'product_uom_id': product_id.uom_id.id,
            'quantity': 1,
            'price_unit': amount,
            'sale_line_ids': [(6, 0, line_ids)],
        }

