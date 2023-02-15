# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Simplified Invoices",
    "summary": """
        This module simplifies billing for 
        multiple sales orders.
    """,
    "author": "Perez Gabriela",
    "maintainers": ["PerezGabriela"],
    "website": "https://github.com/gabbiiperez",
    "license": "AGPL-3",
    "category": "Sale",
    "version": "15.0.1.0.0",
    "installable": True,
    "application": False,
    "depends": [
        "sale",
        "account"
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizard/simple_invoice_wizard.xml",
        "views/sale_order_view.xml"
    ],
}
