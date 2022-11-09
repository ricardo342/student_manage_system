# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: forms
@time:2022/11/9
@Author:majiaqin 170479
@Desc:提交数据表单
'''
from django import forms

from student.models import Student

# class StudentForm(forms.Form):
#     name = forms.CharField(label='姓名', max_length=128)
#     sex = forms.ChoiceField(label='性别', choices=Student.SEX_ITEMS)
#     profession = forms.CharField(label='职业', max_length=128)
#     email = forms.EmailField(label='邮箱', max_length=128)
#     qq = forms.CharField(label='QQ', max_length=128)
#     phone = forms.CharField(label='手机', max_length=128)

class StudentForm(forms.ModelForm):
    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        '''增加QQ字段的纯数字校验'''
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字!')

        return int(cleaned_data)

    class Meta:
        model = Student
        fields = {
            'name', 'sex', 'profession',
            'email', 'qq', 'phone'
        }