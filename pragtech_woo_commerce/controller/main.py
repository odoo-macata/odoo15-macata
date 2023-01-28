from odoo import http, _, modules
import logging
import json
from werkzeug.exceptions import Forbidden, NotFound
import phonenumbers
import datetime
import time
from odoo.http import request, JsonRequest, Response
from odoo.tools import date_utils
import pytz
from odoo.tools import ustr
import requests
import base64
_logger = logging.getLogger(__name__)


class WoocommerceController(http.Controller):

    @http.route(['/woocommerce_order_create'], type='json', auth='public', csrf=False)
    def woocommerce_order_create(self,**kwargs):
        data = request.jsonrequest
        request.env['sale.order'].sudo().woo_order_create(data)

    @http.route(['/woocommerce_order_update'], type='json', auth='public', csrf=False)
    def woocommerce_order_create(self, **kwargs):
        data = request.jsonrequest
        request.env['sale.order'].sudo().woo_order_update(data)
