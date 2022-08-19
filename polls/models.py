import datetime

from django.db import models
# Create your models here.
from django.urls import reverse
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField("问题描述", max_length=200)
    pub_date = models.DateTimeField("发布日期")
    delete = models.BooleanField("是否删除", default=False)

    class Meta:
        db_table = 'question'
        verbose_name = '问题'
        verbose_name_plural = '问题'

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        """
        判断是否是最近一天之内的question
        """
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)

    # @admin.display(description='带颜色的文本')
    # def colored_question_text(self):
    #     return format_html(
    #         '<span style="color: #00ff00;">{}</span>',
    #         self.question_text,
    #     )

    def get_all_choice_text(self):
        return [choice.choice_text for choice in self.choice_set.all()]

    # # import-export-celery 配置导出类
    # @classmethod
    # def import_resource_classes(cls):
    #     return {
    #         "questions": ("Questions resource", QuestionResource)
    #     }
    #
    # @classmethod
    # def export_resource_classes(cls):
    #     return {
    #         "questions": ("Questions resource", QuestionResource),
    #         "questions_all_caps": (
    #             "questions with all caps column resource",
    #             QuestionsWithAllCapsResource,
    #         ),
    #     }


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField("选项描述", max_length=200)
    votes = models.IntegerField("投票", default=0)

    class Meta:
        db_table = 'choice'
        verbose_name = '选项'
        verbose_name_plural = '选项'

    def __str__(self):
        return self.choice_text

    def get_absolute_url(self):
        return reverse('polls:choice-detail', kwargs={'pk': self.pk})

# class QuestionResource(resources.ModelResource):
#     delete = fields.Field(widget=widgets.BooleanWidget())
#
#     def for_delete(self, row, instance):
#         return self.fields['delete'].clean(row)
#
#     class Meta:
#         model = Question
#         skip_unchanged = True
#         report_skipped = False
#
#         use_bulk = True  # 启用批量导入
#         batch_size = 20  # 控制单个查询中创建的对象数量
#         # import_id_fields = ('isbn',) # 可以设置 isbn 作为id 字段
#         # fields = ('isbn', 'question_text', 'pub_date')  # 字段白名单
#         fields = ('id', 'question_text', 'pub_date')  # 字段白名单
#         # exclude = ('',) # 字段黑名单
#         export_order = ('id', 'pub_date', 'question_text')  # 导出时字段显示顺序
#
#     def get_export_queryset(self):
#         """To customise the queryset of the model resource with annotation override"""
#         return self.Meta.model.objects.all()
#
#
# class QuestionsWithAllCapsResource(QuestionResource):
#     name_all_caps = fields.Field()
#
#     def dehydrate_name_all_caps(self, question):
#         return question.question_text.upper()
