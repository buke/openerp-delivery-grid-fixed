# -*- coding: utf-8 -*-
##############################################################################
#
#    QQ field
#    Copyright 2013 wangbuke <wangbuke@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import osv

class delivery_grid(osv.osv):
    _inherit = "delivery.grid"

    def get_price(self, cr, uid, id, order, dt, context=None):
        total = 0
        weight = 0
        volume = 0
        product_uom_obj = self.pool.get('product.uom')
        for line in order.order_line:
            if not line.product_id:
                continue
            q = product_uom_obj._compute_qty(cr, uid, line.product_uom.id, line.product_uos_qty, line.product_id.uom_id.id)
            total += line.price_subtotal or 0.0
            weight += (line.product_id.weight or 0.0) * q
            volume += (line.product_id.volume or 0.0) * q

        return self.get_price_from_picking(cr, uid, id, total,weight, volume, context=context)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
