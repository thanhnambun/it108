# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta


class Revenue(models.Model):
    """
    Model Revenue - Quản lý doanh thu
    """
    _name = 'revenue.management'
    _description = 'Revenue Management'
    _order = 'date desc'

    date = fields.Date(
        string='Ngày',
        required=True,
        default=fields.Date.today,
        help='Ngày ghi nhận doanh thu',
        index=True
    )
    
    amount = fields.Float(
        string='Số tiền (VNĐ)',
        required=True,
        default=0.0,
        digits=(16, 2),
        help='Số tiền doanh thu'
    )
    
    description = fields.Text(
        string='Mô tả',
        help='Mô tả chi tiết về doanh thu'
    )
    
    category = fields.Selection(
        selection=[
            ('product', 'Bán hàng'),
            ('service', 'Dịch vụ'),
            ('rental', 'Cho thuê'),
            ('other', 'Khác')
        ],
        string='Danh mục',
        default='product',
        help='Danh mục doanh thu'
    )
    
    reference = fields.Char(
        string='Mã tham chiếu',
        help='Mã đơn hàng hoặc hợp đồng'
    )
    
    active = fields.Boolean(
        string='Hoạt động',
        default=True,
        help='Bỏ chọn để ẩn bản ghi'
    )
    
    @api.constrains('amount')
    def _check_amount(self):
        """Kiểm tra số tiền phải > 0"""
        for record in self:
            if record.amount <= 0:
                raise ValidationError('Số tiền doanh thu phải lớn hơn 0!')
    
    @api.constrains('date')
    def _check_date(self):
        """Kiểm tra ngày không được trong tương lai"""
        for record in self:
            if record.date > fields.Date.today():
                raise ValidationError('Ngày doanh thu không thể trong tương lai!')
    
    @api.model
    def total_revenue(self, date_from=None, date_to=None, category=None):
        """
        Tính tổng doanh thu trong khoảng thời gian
        
        Args:
            date_from (date): Ngày bắt đầu
            date_to (date): Ngày kết thúc
            category (str): Danh mục (optional)
        
        Returns:
            dict: {
                'total': Tổng doanh thu,
                'count': Số bản ghi,
                'average': Trung bình,
                'date_from': Ngày bắt đầu,
                'date_to': Ngày kết thúc
            }
        """
        domain = [('active', '=', True)]
        
        if date_from:
            domain.append(('date', '>=', date_from))
        if date_to:
            domain.append(('date', '<=', date_to))
        
        if category:
            domain.append(('category', '=', category))
        
        revenues = self.search(domain)
        
        total = sum(revenues.mapped('amount'))
        count = len(revenues)
        average = total / count if count > 0 else 0.0
        
        return {
            'total': total,
            'count': count,
            'average': average,
            'date_from': date_from or 'N/A',
            'date_to': date_to or 'N/A',
            'category': category or 'Tất cả'
        }
    
    @api.model
    def get_daily_revenue(self, target_date=None):
        """
        Tính tổng doanh thu theo ngày cụ thể
        
        Args:
            target_date (date): Ngày cần tính (mặc định: hôm nay)
        
        Returns:
            dict: Thông tin doanh thu ngày
        """
        if not target_date:
            target_date = fields.Date.today()
        
        return self.total_revenue(date_from=target_date, date_to=target_date)
    
    @api.model
    def get_monthly_revenue(self, year=None, month=None):
        """
        Tính tổng doanh thu theo tháng
        
        Args:
            year (int): Năm
            month (int): Tháng
        
        Returns:
            dict: Thông tin doanh thu tháng
        """
        if not year or not month:
            today = fields.Date.today()
            year = today.year
            month = today.month
        
        date_from = datetime(year, month, 1).date()
        
        if month == 12:
            date_to = datetime(year, 12, 31).date()
        else:
            date_to = (datetime(year, month + 1, 1) - timedelta(days=1)).date()
        
        return self.total_revenue(date_from=date_from, date_to=date_to)
    
    @api.model
    def get_revenue_by_category(self, date_from=None, date_to=None):
        """
        Tính doanh thu theo từng danh mục
        
        Returns:
            list: Danh sách doanh thu theo danh mục
        """
        categories = ['product', 'service', 'rental', 'other']
        results = []
        
        for cat in categories:
            result = self.total_revenue(date_from, date_to, cat)
            result['category_name'] = dict(self._fields['category'].selection).get(cat)
            results.append(result)
        
        return results
