# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Exam(models.Model):
    """
    Model Exam - Kỳ thi
    Bảng PostgreSQL: school_exam
    """
    _name = 'school.exam'
    _description = 'Exam Management'
    _rec_name = 'subject'
    _order = 'exam_date desc'

    exam_date = fields.Date(
        string='Ngày thi',
        required=True,
        default=fields.Date.today,
        help='Ngày tổ chức kỳ thi',
        index=True
    )
    
    subject = fields.Char(
        string='Môn học',
        required=True,
        help='Tên môn học',
        index=True
    )
    
    school_id = fields.Many2one(
        comodel_name='school.school',
        string='Trường học',
        required=True,
        ondelete='cascade',
        help='Trường tổ chức kỳ thi'
    )
    
    student_ids = fields.Many2many(
        comodel_name='school.student',
        relation='school_exam_student_rel',
        column1='exam_id',
        column2='student_id',
        string='Học viên tham gia',
        help='Danh sách học viên tham gia kỳ thi'
    )
    
    school_name = fields.Char(
        string='Tên trường',
        related='school_id.name',
        readonly=True,
        store=True
    )
    
    student_count = fields.Integer(
        string='Số học viên',
        compute='_compute_student_count',
        store=True
    )
    
    average_score = fields.Float(
        string='Điểm TB kỳ thi',
        compute='_compute_average_score',
        digits=(5, 2)
    )
    
    max_score = fields.Float(
        string='Điểm cao nhất',
        compute='_compute_score_stats',
        digits=(5, 2)
    )
    
    min_score = fields.Float(
        string='Điểm thấp nhất',
        compute='_compute_score_stats',
        digits=(5, 2)
    )
    
    @api.depends('student_ids')
    def _compute_student_count(self):
        for record in self:
            record.student_count = len(record.student_ids)
    
    @api.depends('student_ids.score')
    def _compute_average_score(self):
        """Tính điểm trung bình của kỳ thi"""
        for record in self:
            students_with_score = record.student_ids.filtered(lambda s: s.score > 0)
            if students_with_score:
                record.average_score = sum(students_with_score.mapped('score')) / len(students_with_score)
            else:
                record.average_score = 0.0
    
    @api.depends('student_ids.score')
    def _compute_score_stats(self):
        """Tính điểm cao nhất và thấp nhất"""
        for record in self:
            students_with_score = record.student_ids.filtered(lambda s: s.score > 0)
            if students_with_score:
                scores = students_with_score.mapped('score')
                record.max_score = max(scores)
                record.min_score = min(scores)
            else:
                record.max_score = 0.0
                record.min_score = 0.0
    
    @api.constrains('exam_date')
    def _check_exam_date(self):
        for record in self:
            if record.exam_date > fields.Date.today():
                pass
    
    @api.constrains('student_ids', 'school_id')
    def _check_students_school(self):
        """Kiểm tra học viên phải cùng trường với kỳ thi"""
        for record in self:
            for student in record.student_ids:
                if student.school_id != record.school_id:
                    raise ValidationError(
                        f'Học viên {student.name} không thuộc trường {record.school_id.name}!'
                    )
    
    @api.model
    def create_exam(self, exam_date, subject, school_id, student_ids=None):
        """
        Thêm mới kỳ thi
        """
        vals = {
            'exam_date': exam_date,
            'subject': subject,
            'school_id': school_id,
        }
        if student_ids:
            vals['student_ids'] = [(6, 0, student_ids)]
        
        return self.create(vals)
    
    def update_exam(self, exam_date=None, subject=None, student_ids=None):
        """
        Cập nhật thông tin kỳ thi
        """
        vals = {}
        if exam_date:
            vals['exam_date'] = exam_date
        if subject:
            vals['subject'] = subject
        if student_ids is not None:
            vals['student_ids'] = [(6, 0, student_ids)]
        
        if vals:
            self.write(vals)
        return True
    
    def get_exam_statistics(self):
        """
        Lấy thống kê kỳ thi
        """
        self.ensure_one()
        return {
            'subject': self.subject,
            'exam_date': self.exam_date,
            'school': self.school_name,
            'total_students': self.student_count,
            'average_score': self.average_score,
            'max_score': self.max_score,
            'min_score': self.min_score,
        }
