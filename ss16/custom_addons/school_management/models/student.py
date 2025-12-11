# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Student(models.Model):
    """
    Model Student - Học viên
    Bảng PostgreSQL: school_student
    """
    _name = 'school.student'
    _description = 'Student Management'
    _rec_name = 'name'

    name = fields.Char(
        string='Tên học viên',
        required=True,
        help='Tên học viên',
        index=True
    )
    
    age = fields.Integer(
        string='Tuổi',
        help='Tuổi học viên'
    )
    
    school_id = fields.Many2one(
        comodel_name='school.school',
        string='Trường học',
        required=True,
        ondelete='cascade',
        help='Trường học của học viên'
    )
    
    score = fields.Float(
        string='Điểm thi',
        digits=(5, 2),
        help='Điểm thi của học viên'
    )
    
    school_name = fields.Char(
        string='Tên trường',
        related='school_id.name',
        readonly=True,
        store=True
    )
    
    school_location = fields.Char(
        string='Địa chỉ trường',
        related='school_id.location',
        readonly=True
    )
    
    exam_ids = fields.Many2many(
        comodel_name='school.exam',
        relation='school_exam_student_rel',
        column1='student_id',
        column2='exam_id',
        string='Kỳ thi tham gia'
    )
    
    exam_count = fields.Integer(
        string='Số kỳ thi',
        compute='_compute_exam_count',
        store=True
    )
    
    @api.depends('exam_ids')
    def _compute_exam_count(self):
        for record in self:
            record.exam_count = len(record.exam_ids)
    
    @api.constrains('age')
    def _check_age(self):
        for record in self:
            if record.age and (record.age < 5 or record.age > 100):
                raise ValidationError('Tuổi phải từ 5 đến 100!')
    
    @api.constrains('score')
    def _check_score(self):
        for record in self:
            if record.score and (record.score < 0 or record.score > 10):
                raise ValidationError('Điểm phải từ 0 đến 10!')
    
    @api.model
    def create_student(self, name, school_id, age=None, score=None):
        """
        Thêm mới học viên (theo yêu cầu)
        """
        vals = {
            'name': name,
            'school_id': school_id,
            'age': age,
            'score': score
        }
        return self.create(vals)
    
    def update_student(self, name=None, age=None, school_id=None, score=None):
        """
        Cập nhật thông tin học viên (theo yêu cầu)
        """
        vals = {}
        if name:
            vals['name'] = name
        if age:
            vals['age'] = age
        if school_id:
            vals['school_id'] = school_id
        if score is not None:
            vals['score'] = score
        
        if vals:
            self.write(vals)
        return True
    
    @api.model
    def calculate_average_score(self, student_ids=None):
        """
        Tính điểm trung bình học viên (theo yêu cầu)
        
        Args:
            student_ids: Danh sách ID học viên (None = tất cả)
        
        Returns:
            dict: Thông tin điểm trung bình
        """
        if student_ids:
            students = self.browse(student_ids)
        else:
            students = self.search([])
        
        students_with_score = students.filtered(lambda s: s.score > 0)
        
        if students_with_score:
            total_score = sum(students_with_score.mapped('score'))
            count = len(students_with_score)
            average = total_score / count
        else:
            total_score = 0
            count = 0
            average = 0
        
        return {
            'total_students': len(students),
            'students_with_score': count,
            'total_score': total_score,
            'average_score': round(average, 2)
        }
