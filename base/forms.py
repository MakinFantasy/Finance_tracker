from django import forms
from django.forms import ModelChoiceField

from base.models import Category, Expense, Subscriber


class CategoryForm(forms.ModelForm):
    date_created = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Category
        fields = ['name', 'description', 'date_created']


class CategorySelectorModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.name


class ExpenseForm(forms.ModelForm):
    date_created = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Expense
        fields = ['name', 'description', 'cost', 'category', 'date_created']

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['category'] = CategorySelectorModelChoiceField(
            queryset=Category.objects.all(),
            empty_label='(select category)',
            widget=forms.Select()
        )


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = "__all__"
