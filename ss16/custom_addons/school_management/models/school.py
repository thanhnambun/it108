# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class School(models.Model):
    """
    Model School - Trường học
    Bảng PostgreSQL: school_school
    """
    _name = 'school.school'
    _description = 'School Management'
    _rec_name = 'name'

    name = fields.Char(
        string='Tên trường',
        required=True,
        help='Tên trường học',
        index=True
    )
    
    location = fields.Char(
        string='Địa chỉ',
        help='Địa chỉ trường học'
    )
    
    start_date = fields.Date(
        string='Ngày thành lập',
        help='Ngày thành lập trường học'
    )
    
    student_ids = fields.One2many(
        comodel_name='school.student',
        inverse_name='school_id',
        string='Học viên'
    )
    
    exam_ids = fields.One2many(
        comodel_name='school.exam',
        inverse_name='school_id',
        string='Kỳ thi'
    )
    
    student_count = fields.Integer(
        string='Số học viên',
        compute='_compute_student_count',
        store=True
    )
    
    exam_count = fields.Integer(
        string='Số kỳ thi',
        compute='_compute_exam_count',
        store=True
    )
    
    average_score = fields.Float(
        string='Điểm TB trường',
        compute='_compute_average_score',
        digits=(5, 2)
    )
    
    @api.depends('student_ids')
    def _compute_student_count(self):
        for record in self:
            record.student_count = len(record.student_ids)
    
    @api.depends('exam_ids')
    def _compute_exam_count(self):
        for record in self:
            record.exam_count = len(record.exam_ids)
    
    @api.depends('student_ids.score')
    def _compute_average_score(self):
        """Tính điểm trung bình của tất cả học viên trong trường"""
        for record in self:
            students_with_score = record.student_ids.filtered(lambda s: s.score > 0)
            if students_with_score:
                record.average_score = sum(students_with_score.mapped('score')) / len(students_with_score)
            else:
                record.average_score = 0.0
    
    @api.model
    def create_school(self, name, location=None, start_date=None):
        """
        Thêm mới trường học (theo yêu cầu)
        """
        vals = {
            'name': name,
            'location': location,
            'start_date': start_date
        }
        return self.create(vals)
    
    def update_school(self, name=None, location=None, start_date=None):
        """
        Cập nhật thông tin trường học (theo yêu cầu)
        """
        vals = {}
        if name:
            vals['name'] = name
        if location:
            vals['location'] = location
        if start_date:
            vals['start_date'] = start_date
        
        if vals:
            self.write(vals)
        return True
