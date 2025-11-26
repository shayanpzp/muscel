# workout/forms.py
from django import forms

ACTIVITY_CHOICES = [
    ("very_low", "خیلی کم (نا توان حرکتی)"),
    ("low", "کم (کارمند یا خانه دار)"),
    ("medium", "متوسط (پیاده‌روی)"),
    ("high", "زیاد (شنا)"),
    ("very_high", "خیلی زیاد (فوتبال)"),
]

DISEASE_CHOICES = [
    ("thyroid", "کم کاری تیرویید"),
    ("gout", "نقرس"),
    ("hypertension", "فشار خون بالا"),
    ("heart", "بیماری های قلبی"),
    ("fatty_liver", "کبد چرب"),
    ("diabetes", "دیابت"),
]

class QuestionnaireForm(forms.Form):
    first_name = forms.CharField(label="نام", max_length=100, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"نام"}))
    last_name = forms.CharField(label="نام خانوادگی", max_length=100, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"نام خانوادگی"}))
    weight = forms.FloatField(label="وزن (کیلوگرم)", widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":"مثلاً 75"}))
    height = forms.FloatField(label="قد (سانتی‌متر)", widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":"مثلاً 175"}))
    age = forms.IntegerField(label="سن", widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":"مثلاً 30"}))
    activity = forms.ChoiceField(label="میزان فعالیت", choices=ACTIVITY_CHOICES, widget=forms.Select(attrs={"class":"form-control"}))
    diseases = forms.MultipleChoiceField(label="بیماری‌ها (در صورت وجود)", choices=DISEASE_CHOICES, required=False, widget=forms.CheckboxSelectMultiple())