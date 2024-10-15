from odoo import models, fields, api

class RepairOrder(models.Model):
    _name = 'repair.order'
    _description = 'Repair Order'

    name = fields.Char(string='Order Name', required=True)
    date = fields.Date(string='Date', required=True, default=fields.Date.context_today)
    product_id = fields.Many2one('product.template', string='Product', required=True)
    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    customer_address = fields.Char(string='Customer Address', related='customer_id.contact_address', readonly=True)
    total = fields.Float(string='Total', compute='_compute_total', store=True)

    order_line_ids = fields.One2many('repair.order.line', 'repair_order_id', string='Order Lines')

    @api.depends('order_line_ids.price_subtotal')
    def _compute_total(self):
        for order in self:
            order.total = sum(line.price_subtotal for line in order.order_line_ids)

class RepairOrderLine(models.Model):
    _name = 'repair.order.line'
    _description = 'Repair Order Line'

    product_id = fields.Many2one('product.template', string='Product', required=True)
    description = fields.Char(string='Description')
    quantity = fields.Integer(string='Quantity', required=True, default=1)
    unit_price = fields.Float(string='Unit Price', required=True)
    price_subtotal = fields.Float(string='Price Subtotal', compute='_compute_price_subtotal', store=True)

    repair_order_id = fields.Many2one('repair.order', string='Repair Order', ondelete='cascade')

    @api.depends('quantity', 'unit_price')
    def _compute_price_subtotal(self):
        for line in self:
            line.price_subtotal = line.quantity * line.unit_price
