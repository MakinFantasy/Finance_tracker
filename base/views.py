from datetime import datetime, timezone
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from django.core.mail import send_mail

from .forms import CategoryForm, ExpenseForm, SubscribeForm
from .models import Category, Expense, Subscriber


# Create your views here.


def index(request):
    expenses = Expense.objects.all()
    categories = Category.objects.all()
    data = {
        'categories': categories,
        'expenses': expenses,
    }

    return render(request, "home.html", context=data)

# Categories views


def get_categories(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, "categories.html", context=context)


def category(request, pk):
    cat = Category.objects.get(id=pk)
    expenses = Expense.objects.filter(category=cat)
    return render(request, "ex_by_cat.html", context={"category": cat, "expenses": expenses})


def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_categories')
    else:
        form = CategoryForm()
    return render(request, 'categories_create.html', {'form': form})


def update_category(request, pk):
    cat = get_object_or_404(Category, id=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=cat)
        if form.is_valid():
            form.save()
            return redirect('category', pk=cat.id)
    else:
        form = CategoryForm(instance=cat)
    return render(request, 'cat_edit.html', {"form": form})


def delete_category(request, pk):
    cat = get_object_or_404(Category, id=pk)
    cat.delete()
    return redirect('get_categories')
# Expenses views


def get_expenses(request):
    expenses = Expense.objects.all()
    context = {'expenses': expenses}
    return render(request, 'expenses.html', context=context)


def create_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.category = Category.objects.get(id=request.POST['category'])
            form.save()
        return redirect('get_expenses')
    else:
        form = ExpenseForm()
    return render(request, 'expense_create.html', {'form': form})


def update_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('get_expenses')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expense_edit.html', {"form": form})


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if expense:
        expense.delete()
        return redirect('get_expenses')
    else:
        return JsonResponse({'status': 'error'}, status=status.HTTP_400_BAD_REQUEST)


# Monthly
def get_monthly_report(request):
    categories = Category.objects.all()
    context = {
        'data': {},
        'month': datetime.now().strftime("%B"),
    }
    month = context['month']
    print(context.items())
    for cat in categories:
        print(cat.date_created.month)
        expenses_cost = list(Expense.objects.filter(category=cat).filter(date_created__month=datetime.now().month).values_list('cost'))
        summary = 0
        for exp in expenses_cost:
            summary += exp[0]
        context['data'][cat.name] = summary

    print(context)
    return render(request, 'report.html', context=context)


# subscribers

def subscribe(request):
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SubscribeForm()
    return render(request, 'subscribe.html', {'form': form})


def get_emails():
    emails = []
    for mail in Subscriber.objects.all():
        emails.append(mail.email)
    print(emails)
    return emails


def get_max_cost_per_category():
    categories = Category.objects.all()
    context = {
        'data': {},
    }
    for cat in categories:
        expenses_cost = list(Expense.objects.filter(category=cat).filter(date_created__month=datetime.now().month).values_list('cost'))
        summary = 0
        for exp in expenses_cost:
            summary += exp[0]
        context['data'][cat.name] = summary
    return context


def get_max_category(context):
    max_sum = ['', 0]
    for cat in context['data']:
        if int(context['data'][cat]) > max_sum[1]:
            max_sum[0] = cat
            max_sum[1] = context['data'][cat]
    return max_sum


def send_mass_mail(request):
    data = get_max_category(get_max_cost_per_category())
    cost = data[1]
    cat = data[0]
    send_mail(
        'New monthly report',
        'Тратишь сликом много на {}. Целых {}!!'.format(cat, cost),
        'beingp0z1t1v3@gmail.com',
        get_emails()
    )
    return render(request, 'emails_success.html')
