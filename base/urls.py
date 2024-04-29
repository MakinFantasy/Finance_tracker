from django.urls import path

from base import views
# from base.views import CategoryCreateAPIView

urlpatterns = [
    path('', views.index, name='index'),
    path('expense/all', views.get_expenses, name='get_expenses'),
    path('expense/create', views.create_expense, name='create_expense'),
    path('expense/update/<int:pk>', views.update_expense, name='update_expense'),
    path('expense/delete/<int:pk>', views.delete_expense, name='delete_expense'),

    path('category/all', views.get_categories, name='get_categories'),
    path('category/<int:pk>', views.category, name='category'),
    path('category/create', views.create_category, name='create_category'),
    path('category/update/<int:pk>', views.update_category, name='update_category'),
    path('category/delete/<int:pk>', views.delete_category, name='delete_category'),

    path('report/', views.get_monthly_report, name='get_monthly_report'),

    path('subscribe/', views.subscribe, name='subscribe'),
    path('send/', views.send_mass_mail, name='send_mass_mail'),
]
