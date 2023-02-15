from odoo import fields, models


class SimpleInvoiceWizard(models.TransientModel):
    _name = "simple.invoice.wizard"
    _description = "Create Simple Invoice Wizard"

    billable_product_id = fields.Many2one(
        "product.product",
        string="Billable Product",
        required=True
    )

    def create_simple_invoice(self):
        if len(self.env.context['active_ids']) != 0:
            active_ids = self.env.context.get('active_ids')
            so_obj = self.env['sale.order']
            sale_orders = so_obj.browse(active_ids)
            so_obj.create_simple_invoice(sale_orders, self.billable_product_id)
        return sale_orders.action_view_invoice()
