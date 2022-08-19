#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: resource.py.py
@time: 2022/8/14 19:44
@desc: 
"""
from import_export import resources, fields, widgets
from import_export.fields import Field

from .models import Question


class QuestionResource(resources.ModelResource):
    delete = fields.Field(widget=widgets.BooleanWidget())

    def for_delete(self, row, instance):
        return self.fields['delete'].clean(row)

    class Meta:
        model = Question
        skip_unchanged = True
        report_skipped = False

        use_bulk = True  # 启用批量导入
        batch_size = 20  # 控制单个查询中创建的对象数量
        # import_id_fields = ('isbn',) # 可以设置 isbn 作为id 字段
        # fields = ('isbn', 'question_text', 'pub_date')  # 字段白名单
        fields = ('id', 'question_text', 'pub_date')  # 字段白名单
        # exclude = ('',) # 字段黑名单
        export_order = ('id', 'pub_date', 'question_text')  # 导出时字段显示顺序

    # def get_export_queryset(self):
    #     """To customise the queryset of the model resource with annotation override"""
    #     return self.Meta.model.objects.all()


class QuestionsWithAllCapsResource(QuestionResource):
    name_all_caps = Field()

    def dehydrate_name_all_caps(self, question):
        return question.question_text.upper()
