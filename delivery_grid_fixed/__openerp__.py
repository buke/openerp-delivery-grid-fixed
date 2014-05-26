# -*- coding: utf-8 -*-
##############################################################################
#
#    Fixed delivery grid get_price
#    Copyright 2014 wangbuke <wangbuke@gmail.com>
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
{
    'name': 'Fixed delivery grid get_price',
    'version': '0.1',
    'category' : 'Sales Management',
    'description': """
Fixed delivery grid get_price

功能： 修复 delivery 计算价格问题

问题：

    delivery 计算价格时，假如是按照重量计算。默认重量计算规则是，订单行的数量 × 产品重量
    这在不修改订单行计量单位时，是没有问题的。
    但如果此时修改计量单位，计算规则就有问题了，没有考虑计量单位的换算。

重现方法：

    安装 delivery 自行测试

""",
    'author': 'wangbuke@gmail.com',
    'website': 'http://buke.github.io',
    'depends': ['delivery'],
    'installable': True,
    'images': [],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
