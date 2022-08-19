from django import forms
from django.contrib import admin
# Register your models here.
from django.forms import Textarea
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportActionModelAdmin

from .models import Question, Choice
from .resource import QuestionResource

admin.site.site_header = '后台管理'
admin.site.site_title = '投票应用管理'
admin.site.index_title = '我在后台首页'


class ChoiceInline(admin.StackedInline):
    model = Choice
    classes = ('collapse',)
    extra = 1
    can_delete = True
    show_change_link = True


# # 自定义表单 给日期添加一个自定义验证
# class QuestionAdminForm(forms.ModelForm):
#     def clean_pub_date(self):
#         # do something that validates your data
#         return self.cleaned_data["pub_date"]
#

class RichTextEditorWidget(Textarea):
    pass


@admin.register(Question)
class QuestionAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'question_text', 'pub_date', 'delete')
    list_display_links = ('id', 'question_text',)
    readonly_fields = ('id', )  # 将日期显示为只读,不可修改
    inlines = (ChoiceInline,)  # 指定内联
    save_on_top = True
    ordering = ('id',)
    search_fields = ['question_text']
    list_max_show_all = 10
    list_per_page = 20  # 列表页每页显示多少条目 默认 100
    list_filter = ('question_text', ('delete', admin.BooleanFieldListFilter))  # 更改列表页面右侧侧栏的过滤器

    actions_selection_counter = True  # 默认为True
    resource_class = QuestionResource
    fieldsets = (
        (None, {
            'fields': ('id', 'delete',)
        }),
        ("group", {
            # 'classes': ('collapse',),
            'classes': ('wide',),
            'description': '描述和日期在该组别显示',
            'fields': ('question_text', 'pub_date')
        }),
    )

    # date_hierarchy = 'pub_date'  # 在管理页面会呈现一个基于当前设置字段的日期列表例如:2000 2001 2002 ... 2022
    # list_display = ('id', 'question_text', 'pub_date', 'delete', 'upper_case_question_text', 'colored_question_text')
    # fields = (('id', 'delete'), 'question_text', 'pub_date')  # 新增 和 修改页面表单显示的字段,并且按指定顺序呈现
    # prepopulated_fields = {"slug": ("title",)}  # 主要用途是从一个或多个其他字段自动生成 SlugField 字段的值
    # list_editable = ('question_text', 'delete')  # 在列表页可编辑多行多列
    # actions_on_Top = False  # 控制动作显示位置
    # actions_on_bottom = True
    # empty_value_display = "*****"  # 空值如何显示
    # actions = (create_export_job_action, run_import_job_action)
    # # 显示的文本，与django admin一致
    # run_import_job_action.short_description = '导入 by Celery'
    # create_export_job_action.short_description = '导出 by Celery'

    # @admin.display(description='大写的文本')
    # def upper_case_question_text(self, obj):
    #     return "%s" % obj.question_text.upper()

    # @admin.display(description='Choice选项')
    # def choice_report(self, instance):
    #     return format_html_join(
    #         mark_safe('<br>'),
    #         '{}',
    #         ((line,) for line in instance.get_all_choice_text()),
    #     ) or mark_safe("<span class='errors'>I can't determine this choice_text.</span>")

    # 重写某字段在 新增和修改页面的表单部件
    # formfield_overrides = {
    #     models.CharField: {'widget': RichTextEditorWidget},
    # }


# class MyChoiceAdminForm(forms.ModelForm):
#     class Meta:
#         model = Choice
#         fields = '__all__'
#
#     def clean_choice_text(self):
#         # do something that validates your data
#         text = self.cleaned_data["choice_text"]
#         self.cleaned_data["choice_text"] = text if text.startswith('aaa') else 'bbbbb'
#         return self.cleaned_data["choice_text"]


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['question', 'choice_text', 'votes']
    search_fields = ('question__question_text__iexact',)
    sortable_by = []
    list_filter = (
        ('question', admin.RelatedOnlyFieldListFilter),
    )

    # 当值设置为 False 时，Django 将查看 list_display，如果有 ForeignKey，则调用 select_related()。
    # list_select_related = True  # 当值为 True 时，select_related() 总是会被调用。
    # list_select_related = ('question',)  # 空元组阻止使用select_related
    # radio_fields = {"question": admin.VERTICAL}  # 新增和修改页面 使用单选按钮代替下拉菜单
    # autocomplete_fields = ['question']
    # raw_id_fields = ['question']
    # show_full_result_count = True  # 这个选项被设置为 False，则会显示 99 results (Show all) 这样的文字
    # list_max_show_all = 300   # 当总结果数(99 results)小于或等于此配置时，管理才会在更改列表中显示 “全部显示” 链接
    # # 在管理中 自定义字段验证
    # form = MyChoiceAdminForm
    # view_on_site = False
