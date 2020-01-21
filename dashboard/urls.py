from django.conf.urls import url

from . import views

urlpatterns=[
url(r'^$', views.index ,name='index'),
url(r'^enter_expenditure/', views.enter_expenditure, name='enter_expenditure'),
url(r'^enter_sundryexpense', views.enter_sundryexpense ,name='enter_sundryexpense'),
url(r'^Enter-Records/Allowances', views.give_allowance, name='give-allowance'),
url(r'^Enter_Pledges/', views.Enter_Pledges, name='Enter_Pledges'),
url(r'^Enter_Tithes/', views.Enter_Tithes, name='Enter_Tithes'),
url(r'^Revenue/Donations/Add', views.record_donations, name='record-donations'),
url(r'^Reports/Donations/List', views.donations_report, name='donations-report'),
url(r'^Enter_Offerings/', views.Enter_Offerings, name='Enter_Offerings'),
url(r'^Pledges/Add-Item/', views.add_Pledge_Items ,name='add-pledge-item'),
url(r'^sundryreport', views.sundryreport ,name='sundryreport'),
url(r'^allowancereport/', views.allowancereport, name='allowancereport'),
url(r'^expenditurereport/', views.expenditurereport, name='expenditurereport'),
url(r'^Expenses/General-Expenses/Enter', views.enter_general_expenses, name='enter-general-expenses'),
url(r'^Expenses/General-Expenses/List', views.general_expenses_report, name='general-expenses-report'),
#generate pdfs
url(r'^allowancespdf/', views.allowancespdf.as_view() ,name='allowancespdf'),
url(r'^sundrypdf/', views.sundrypdf.as_view() ,name='sundrypdf'),
url(r'^expenditurepdf/', views.expenditurepdf.as_view() ,name='expenditurepdf'),
url(r'^pledgespdf/', views.pledgespdf.as_view() ,name='pledgespdf'),
url(r'^tithespdf/', views.tithespdf.as_view() ,name='tithespdf'),
url(r'^offeringspdf/', views.offeringspdf.as_view() ,name='offeringspdf'),

url(r'^expensereceipt/(?P<pk>\d+)', views.expensereceipt.as_view() ,name='expensereceipt'),
url(r'^allowancereceipt/(?P<pk>\d+)', views.allowancereceipt.as_view() ,name='allowancereceipt'),
url(r'^sundryreceipt/(?P<pk>\d+)', views.sundryreceipt.as_view() ,name='sundryreceipt'),
url(r'^offeringsreceipt/(?P<pk>\d+)', views.offeringsreceipt.as_view() ,name='offeringsreceipt'),
url(r'^tithesreceipt/(?P<pk>\d+)', views.tithesreceipt.as_view() ,name='tithesreceipt'),
url(r'^pledgesreceipt/(?P<pk>\d+)', views.pledgesreceipt.as_view() ,name='pledgesreceipt'),
url(r'^Receipts/Seed-Offering/(?P<pk>\d+)', views.seed_offering_receipt.as_view() ,name='seed-offering-receipt'),

url(r'^expenditurearchive/', views.expenditurearchive, name='expenditurearchive'),
url(r'^allowancearchive/', views.allowancearchive, name='allowancearchive'),
url(r'^sundryarchive/', views.sundryarchive, name='sundryarchive'),

url(r'^expenditurearchivepdf/(?P<report_month>.+?)/(?P<report_year>.+?)/', views.expenditurearchivepdf.as_view(), name='expenditurearchivepdf'),
url(r'^allowancearchivepdf/(?P<report_month>.+?)/(?P<report_year>.+?)/', views.allowancearchivepdf.as_view(), name='allowancearchivepdf'),
url(r'^sundryarchivepdf/(?P<report_month>.+?)/(?P<report_year>.+?)/', views.sundryarchivepdf.as_view(), name='sundryarchivepdf'),
url(r'^pledgesarchivepdf/(?P<report_month>.+?)/(?P<report_year>.+?)/', views.pledgesarchivepdf.as_view(), name='pledgesarchivepdf'),
url(r'^offeringsarchivepdf/(?P<report_month>.+?)/(?P<report_year>.+?)/', views.offeringsarchivepdf.as_view(), name='offeringsarchivepdf'),
url(r'^tithesarchivepdf/(?P<report_month>.+?)/(?P<report_year>.+?)/', views.tithesarchivepdf.as_view(), name='tithesarchivepdf'),

url(r'^edit_payment/(?P<pk>\d+)', views.edit_payment ,name='edit_payment'),
url(r'^Church-Member/Edit/(?P<pk>\d+)', views.edit_member ,name='edit-member'),
url(r'^Church-Member/Delete/(?P<pk>\d+)', views.delete_member ,name='delete-member'),
url(r'^Church-Visitor/Edit/(?P<pk>\d+)', views.edit_visitor ,name='edit-visitor'),
url(r'^Church-Visitor/Delete/(?P<pk>\d+)', views.delete_visitor ,name='delete-visitor'),
url(r'^delete_payment/(?P<pk>\d+)', views.delete_payment ,name='delete_payment'),
url(r'^edit_allowance/(?P<pk>\d+)', views.edit_allowance ,name='edit_allowance'),
url(r'^edit_offerings/(?P<pk>\d+)', views.edit_offerings ,name='edit_offerings'),
url(r'^edit_pledges/(?P<pk>\d+)', views.edit_pledges ,name='edit_pledges'),
url(r'^edit_tithes/(?P<pk>\d+)', views.edit_tithes ,name='edit_tithes'),
url(r'^Employee/Edit/(?P<pk>\d+)', views.edit_employee ,name='edit-employee'),
url(r'^Employee/View/(?P<pk>\d+)', views.view_employee ,name='view-employee'),
url(r'^Member/View/(?P<pk>\d+)', views.view_member ,name='view-member'),
url(r'^Pledges-Item/Delete/(?P<pk>\d+)', views.delete_pledge_item ,name='delete-pledge-item'),
url(r'^Pledges-Item/Edit/(?P<pk>\d+)', views.edit_pledge_item ,name='edit-pledge-item'),

url(r'^delete_allowance/(?P<pk>\d+)', views.delete_allowance ,name='delete_allowance'),
url(r'^edit_sundry/(?P<pk>\d+)', views.edit_sundry ,name='edit_sundry'),
url(r'^delete_sundry/(?P<pk>\d+)', views.delete_sundry ,name='delete_sundry'),

url(r'^allowancereport/', views.allowancereport, name='allowancereport'),
url(r'^Tithesreport/', views.Tithesreport, name='Tithesreport'),
url(r'^Offeringsreport/', views.Offeringsreport, name='Offeringsreport'),
url(r'^Pledgesreport/', views.Pledgesreport, name='Pledgesreport'),
url(r'^expenditurereport/', views.expenditurereport, name='expenditurereport'),


url(r'^Expenses/General/Archived/', views.generalexpensesarchivessearch, name='general-expensesarchives-search'),
url(r'^expensesarchivessearch/', views.expensesarchivessearch, name='expensesarchivessearch'),
url(r'^allowancearchivessearch/', views.allowancearchivessearch, name='allowancearchivessearch'),
url(r'^sundrysarchivessearch/', views.sundryarchivessearch, name='sundryarchivessearch'),
url(r'^pledgesarchivessearch/', views.pledgesarchivessearch, name='pledgesarchivessearch'),
url(r'^offeringsarchivessearch/', views.offeringsarchivessearch, name='offeringsarchivessearch'),
url(r'^tithesarchivessearch/', views.tithesarchivessearch, name='tithesarchivessearch'),
url(r'^Archives/Salaries/', views.salariespaidarchivessearch, name='salariespaidarchivessearch'),
url(r'^Archives/Seeds/', views.seedsarchivessearch, name='seeds-archives-search'),
url(r'^Archives/Donations/', views.donationsarchivessearch, name='donationsarchivessearch'),
url(r'^Archives/Thanks-Giving/', views.thanksgivingarchivessearch, name='thanksgivingarchivessearch'),

# url(r'^expenditure_report_archive/', views.expenditure_report_archive, name='expenditure_report_archive'),
#membership
url(r'^Membership/Register/', views.register_members, name='members-register'),
url(r'^Visitors/Register/', views.register_visitors, name='visitors-register'),
url(r'^Membership/List/', views.members_list, name='members-list'),
url(r'^Visitors/List/', views.visitors_list, name='visitors-list'),
url(r'^member_pledges_paid', views.member_pledges_paid, name='member_pledges_paid'),
url(r'^Pledges/Items/List/', views.list_of_pledge_items, name='list-of-pledge-items'),
url(r'^paying_pledges/(?P<pk>\d+)', views.paying_pledges, name='paying_pledges'),
url(r'^Pledges/view/(?P<pledge_pk>\d+)/$', views.pledge_view, name='pledge_view'),
url(r'^Pledges/History/List', views.pledges_paid_list, name='pledges-paid-list'),
url(r'^Pledges/Archived/Debts', views.archived_pledge_debts, name='archived-pledge-debts'),
url(r'^Pledges/Archived/Settling-Debt/(?P<pk>\d+)', views.settle_pledge_debt, name='settle-pledge-debt'),
url(r'^Pledges/Archived/Debt_settling', views.member_settle_pledge_debt, name='member-settle-pledge-debt'),
url(r'^Pledges/Archived/Delete-Bad-debt/(?P<pk>\d+)', views.delete_bad_debt, name='delete-bad-debt'),
url(r'^Incomes/Total/', views.total_monthly_incomes, name='total-monthly-incomes'),

#Employees
url(r'^Employees/Add/', views.employee_register, name='employee-register'),
url(r'^Employees/List/', views.employee_list, name='employee-list'),
url(r'^Employees/Pay/(?P<pk>\d+)', views.paying_employees, name='pay-employee'),
url(r'^Employees/Salary/Paid/', views.paid_salary, name='paid-salary'),
url(r'^Employees/Salary/Paid-List/', views.current_month_salary_paid, name='current-month-salaries'),
url(r'^Petty-Expenses/Airtime/', views.airtime_data_report, name='airtime-data-report'),
url(r'^Revenue/Seeds/Add/', views.add_seeds, name='add-seeds'),
url(r'^Reports/Seeds/List', views.Seedsreport, name='Seeds-report'),
url(r'^Revenue/Seeds/Edit/(?P<pk>\d+)', views.edit_seed,name='edit-seed'),
url(r'^Revenue/Donations/Edit/(?P<pk>\d+)', views.edit_donation,name='edit-donation'),
url(r'^Revenue/Thanks-Giving/Edit/(?P<pk>\d+)', views.edit_thanks_giving,name='edit-thanks-giving'),
url(r'^Revenue/Thanks-giving/Add', views.record_thanks_giving,name='record-thanks-giving'),
url(r'^Reports/Thanks-giving/List', views.thanks_giving_report,name='thanks-giving-report'),
]