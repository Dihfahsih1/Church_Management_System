from django.conf.urls import url

from . import views

urlpatterns=[
url(r'^$', views.web, name='index_public'),
url(r'^Church-System', views.index ,name='index'),
url(r'^feedback', views.contact, name='contact'),
url(r'^membership-online/$', views.OnlineRegistrationView.as_view(), name='online_registration'),
url(r'^Church/Members', views.membership_wall, name='membership_wall'),
url(r'^Church/Vision', views.abouts_vision, name='abouts_vision'),
url(r'^Church-Mission', views.abouts_mission, name='abouts_mission'),
url(r'^Pastoral-Team', views.church_pastors, name='church_pastors'),
url(r'^Administrative-Team', views.church_administration, name='church_administration'),

#EXPENDITURE MODULE URLS
url(r'^Expenses/Main-Expenses', views.enter_main_expenses, name='enter_expenditure'),
url(r'^Expenses/Petty-Expenses/', views.enter_petty_expenses, name='enter_sundryexpense'),
url(r'^Expenses/General-Expenses/Enter', views.enter_general_expenses, name='enter-general-expenses'),

url(r'^Edit/General-Expense/(?P<pk>\d+)', views.edit_general_expense ,name='edit-general-expense'),
url(r'^Main-Expense/Edit/(?P<pk>\d+)', views.edit_main_expense ,name='edit-main-expense'),
url(r'^Petty-Expense/Edit/(?P<pk>\d+)', views.edit_petty_cash ,name='edit-petty-cash'),

url(r'^Reports/Main-Expenses/', views.main_expenses_report, name='expenditurereport'),
url(r'^Reports/General-Expenses/', views.general_expenses_report, name='general-expenses-report'),
url(r'^Reports/Sundry-Report/', views.petty_cash_report, name='sundryreport'),

url(r'^General-Expenses/Archived/', views.general_expenses_archives_search, name='general-expensesarchives-search'),
url(r'^Main-Expenses/Archived/', views.main_expenses_archives_search, name='expensesarchivessearch'),
url(r'^Petty-Cash/Archived/', views.petty_cash_archives_search, name='sundryarchivessearch'),

#Offerings Module
url(r'^Revenues/Offerings/Report', views.Offeringsreport, name='Offeringsreport'),
url(r'^edit_offerings/(?P<pk>\d+)', views.edit_offerings ,name='edit-offerings'),
url(r'^offeringspdf/', views.offeringspdf.as_view() ,name='offeringspdf'),
url(r'^offeringsarchivepdf/', views.offeringsarchivepdf.as_view(), name='offeringsarchivepdf'),
url(r'^Record-Offerings/', views.Enter_Offerings, name='Enter_Offerings'),

#Seeds Module
url(r'^Revenue/Seeds/Add/', views.add_seeds, name='add-seeds'),
url(r'^Revenues/Seeds-Report', views.Seedsreport, name='Seeds-report'),
url(r'^Revenue/Seeds/Edit/(?P<pk>\d+)', views.edit_seed,name='edit-seed'),
url(r'^Receipts/Seed-Offering/(?P<pk>\d+)', views.seed_offering_receipt.as_view() ,name='seed-offering-receipt'),
url(r'^Archives/Seeds/', views.seedsarchivessearch, name='seeds-archives-search'),


url(r'^Enter-Records/Allowances', views.give_allowance, name='give-allowance'),
url(r'^Enter_Pledges/', views.Enter_Pledges, name='Enter_Pledges'),
url(r'^Building-Renovations/', views.record_building_collections, name='record-building-collections'),
url(r'^Enter_Tithes/', views.Enter_Tithes, name='Enter_Tithes'),
url(r'^Revenue/Donations/Add', views.record_donations, name='record-donations'),
url(r'^Reports/Donations/List', views.donations_report, name='donations-report'),
url(r'^Pledges/Add-Item/', views.add_Pledge_Items ,name='add-pledge-item'),

url(r'^allowancereport/', views.allowancereport, name='allowancereport'),




url(r'^allowancespdf/', views.allowancespdf.as_view() ,name='allowancespdf'),
url(r'^expenditurepdf/', views.expenditurepdf.as_view() ,name='expenditurepdf'),
url(r'^pledgespdf/', views.pledgespdf.as_view() ,name='pledgespdf'),
url(r'^tithespdf/', views.tithespdf.as_view() ,name='tithespdf'),





url(r'^expensereceipt/(?P<pk>\d+)', views.expensereceipt.as_view() ,name='expensereceipt'),
url(r'^Archived/Pledge-Debt/Receipt/(?P<pk>\d+)', views.settled_archived_pledge_receipt.as_view() ,name='settled-pledge-receipt'),
url(r'^Archived/Pledge-Debt/Invoice/(?P<pk>\d+)', views.pledge_debt_invoice.as_view() ,name='pledge-invoice'),
url(r'^allowancereceipt/(?P<pk>\d+)', views.allowancereceipt.as_view() ,name='allowancereceipt'),
url(r'^tithesreceipt/(?P<pk>\d+)', views.tithesreceipt.as_view() ,name='tithesreceipt'),
url(r'^pledgesreceipt/(?P<pk>\d+)', views.pledgesreceipt.as_view() ,name='pledgesreceipt'),

url(r'^expenditurearchive/', views.expenditurearchive, name='expenditurearchive'),
url(r'^allowancearchive/', views.allowancearchive, name='allowancearchive'),


url(r'^expenditurearchivepdf/(?P<report_month>.+?)/(?P<report_year>.+?)/', views.expenditurearchivepdf.as_view(), name='expenditurearchivepdf'),
url(r'^allowancearchivepdf/(?P<report_month>.+?)/(?P<report_year>.+?)/', views.allowancearchivepdf.as_view(), name='allowancearchivepdf'),
#url(r'^sundryarchivepdf/(?P<report_month>.+?)/(?P<report_year>.+?)/', views.sundryarchivepdf.as_view(), name='sundryarchivepdf'),
url(r'^pledgesarchivepdf/(?P<report_month>.+?)/(?P<report_year>.+?)/', views.pledgesarchivepdf.as_view(), name='pledgesarchivepdf'),
url(r'^tithesarchivepdf/(?P<report_month>.+?)/(?P<report_year>.+?)/', views.tithesarchivepdf.as_view(), name='tithesarchivepdf'),

#Handling all PKs, IDs
url(r'^Pledges-Made/Invoice/(?P<pk>\d+)', views.pledge_made_invoice.as_view(), name='pledge-made-invoice'),
url(r'^Church-Member/Edit/(?P<pk>\d+)', views.edit_member ,name='edit-member'),
url(r'^Church-Member/Delete/(?P<pk>\d+)', views.delete_member ,name='delete-member'),
url(r'^Employee/Delete/(?P<pk>\d+)', views.delete_employee ,name='delete-employee'),
url(r'^Church-Visitor/Edit/(?P<pk>\d+)', views.edit_visitor ,name='edit-visitor'),
url(r'^Church-Visitor/Delete/(?P<pk>\d+)', views.delete_visitor ,name='delete-visitor'),
url(r'^edit_allowance/(?P<pk>\d+)', views.edit_allowance ,name='edit_allowance'),

url(r'^edit_pledges/(?P<pk>\d+)', views.edit_pledges ,name='edit_pledges'),
url(r'^edit_tithes/(?P<pk>\d+)', views.edit_tithes ,name='edit_tithes'),
url(r'^Employee/Edit/(?P<pk>\d+)', views.edit_employee ,name='edit-employee'),
url(r'^Employee/View/(?P<pk>\d+)', views.view_employee ,name='view-employee'),
url(r'^Member/View/(?P<pk>\d+)', views.view_member ,name='view-member'),
url(r'^Pledge/Delete/(?P<pk>\d+)', views.delete_pledge ,name='delete-pledge'),
url(r'^Pledges-Item/Delete/(?P<pk>\d+)', views.delete_pledge_item ,name='delete-pledge-item'),
url(r'^Pledges-Item/Edit/(?P<pk>\d+)', views.edit_pledge_item ,name='edit-pledge-item'),
url(r'^delete_allowance/(?P<pk>\d+)', views.delete_allowance ,name='delete_allowance'),

#Monthly Report Generation
url(r'^allowancereport/', views.allowancereport, name='allowancereport'),
url(r'^Tithesreport/', views.Tithesreport, name='Tithesreport'),

url(r'^Pledgesreport/', views.Pledgesreport, name='Pledgesreport'),
url(r'^Building-Renovations-Report/', views.Building_Renovation_report, name='Building-Renovation-report'),

#Archived reports search

url(r'^allowancearchivessearch/', views.allowancearchivessearch, name='allowancearchivessearch'),
url(r'^pledgesarchivessearch/', views.pledgesarchivessearch, name='pledgesarchivessearch'),
url(r'^offeringsarchivessearch/', views.offeringsarchivessearch, name='offeringsarchivessearch'),
url(r'^tithesarchivessearch/', views.tithesarchivessearch, name='tithesarchivessearch'),
url(r'^Archives/Salaries/', views.salariespaidarchivessearch, name='salariespaidarchivessearch'),
url(r'^Archives/Seeds/', views.seedsarchivessearch, name='seeds-archives-search'),
url(r'^Archives/Donations/', views.donationsarchivessearch, name='donationsarchivessearch'),
url(r'^Archives/Thanks-Giving/', views.thanksgivingarchivessearch, name='thanksgivingarchivessearch'),
url(r'^Archives/Building-Renovations/', views.BuildingRenovationarchivessearch, name='BuildingRenovationarchivessearch'),

# url(r'^expenditure_report_archive/', views.expenditure_report_archive, name='expenditure_report_archive'),
#membership 

url(r'^Members/Annual-Tithes/(?P<pk>\d+)', views.member_annual_tithes, name='annual-tithes'),
url(r'^Membership/Register/', views.register_members, name='members-register'),
url(r'^Visitors/Register/', views.register_visitors, name='visitors-register'),
url(r'^Membership/List/', views.members_list, name='members-list'),
url(r'^Visitors/List/', views.visitors_list, name='visitors-list'),
url(r'^member_pledges_paid', views.member_pledges_paid, name='member_pledges_paid'),
url(r'^Pledges/Cash/Paid', views.cashing_out_items, name='cashing-out-items'),
url(r'^Pledges/Items/List/', views.list_of_pledge_items, name='list-of-pledge-items'),
url(r'^paying_pledges/(?P<pk>\d+)', views.paying_pledges, name='paying_pledges'),
url(r'^Pledges/Cash-Out/(?P<pk>\d+)', views.pledge_cash_out, name='pledge-cash-out'),
url(r'^Pledges/view/(?P<pledge_pk>\d+)/$', views.pledge_view, name='pledge_view'),
url(r'^Pledges/History/List', views.pledges_paid_list, name='pledges-paid-list'),
# url(r'^Pledges/Paid/Delete/(?P<pk>\d+)/', views.delete_pledges_paid, name='delete-pledges-paid'),
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



url(r'^Employee/Salary/Delete/(?P<pk>\d+)', views.delete_salary_paid,name='delete-salary-paid'),
url(r'^Revenue/Donations/Edit/(?P<pk>\d+)', views.edit_donation,name='edit-donation'),
url(r'^Revenue/Thanks-Giving/Edit/(?P<pk>\d+)', views.edit_thanks_giving,name='edit-thanks-giving'),
url(r'^Revenue/Thanks-giving/Add', views.record_thanks_giving,name='record-thanks-giving'),
url(r'^Reports/Thanks-giving/List', views.thanks_giving_report,name='thanks-giving-report'),

#slider urls
url(r'^frontend/slider/index/$', views.SliderListView.as_view(), name='slider_list'),
url(r'^frontend/slider/add/$', views.SliderCreateView.as_view(), name='slider_create'),
url(r'^frontend/slider/update/(?P<slider_pk>\d+)/$', views.SliderUpdateView.as_view(), name='slider_update'),
url(r'^frontend/slider/view/(?P<slider_pk>\d+)/$', views.slider_view, name='slider_view'),
url(r'^frontend/slider/delete/(?P<slider_pk>\d+)/$', views.slider_delete, name='slider_delete'),

#abouts Urls
url(r'^frontend/about/index/$', views.AboutListView.as_view(), name='about_list'),
url(r'^frontend/about/add/$', views.AboutCreateView.as_view(), name='about_create'),
url(r'^frontend/about/update/(?P<about_pk>\d+)/$', views.AboutUpdateView.as_view(), name='about_update'),
url(r'^frontend/about/view/(?P<about_pk>\d+)/$', views.about_view, name='about_view'),
url(r'^frontend/about/about-detail/(?P<about_pk>\d+)/$', views.about_detail, name='about_detail'),
url(r'^frontend/about/delete/(?P<about_pk>\d+)/$', views.about_delete, name='about_delete'),

#Pages
url(r'^frontend/index/$', views.PageListView.as_view(), name='page_list'),
url(r'^frontend/page/(?P<page_pk>\d+)/$', views.page_wall, name='page_wall'),
url(r'^frontend/add/$', views.PageCreateView.as_view(), name='page_create'),
url(r'^frontend/update/(?P<page_pk>\d+)/$', views.PageUpdateView.as_view(), name='page_update'),
url(r'^frontend/view/(?P<page_pk>\d+)/$', views.page_view, name='page_view'),
url(r'^frontend/delete/(?P<page_pk>\d+)/$', views.page_delete, name='page_delete'),

#Galleries
url(r'^gallery/index/$', views.GalleryListView.as_view(), name='gallery_list'),
url(r'^galleries/$', views.gallery_wall, name='gallery_wall'),
url(r'^gallery/add/$', views.GalleryCreateView.as_view(), name='gallery_create'),
url(r'^gallery/update/(?P<gallery_pk>\d+)/$', views.GalleryUpdateView.as_view(), name='gallery_update'),
url(r'^gallery/delete/(?P<gallery_pk>\d+)/$', views.gallery_delete, name='gallery_delete'),

#Images
url(r'^gallery/image/index/$', views.ImageListView.as_view(), name='image_list'),
url(r'^gallery/image/create/$', views.ImageCreateView.as_view(), name='image_create'),
url(r'^gallery/image/update/(?P<image_pk>\d+)/$', views.ImageUpdateView.as_view(), name='image_update'),
url(r'^gallery/image/view/(?P<image_pk>\d+)/$', views.image_view, name='image_view'),
url(r'^gallery/image/delete/(?P<image_pk>\d+)/$', views.image_delete, name='image_delete'),

#News
url(r'^announcement/news/index/$', views.NewsListView.as_view(), name='news_list'),
url(r'^announcement/news/$', views.news_wall, name='news_wall'),
url(r'^announcement/news/add/$', views.NewsCreateView.as_view(), name='news_create'),
url(r'^announcement/news/update/(?P<news_pk>\d+)/$', views.NewsUpdateView.as_view(), name='news_update'),
url(r'^announcement/news/view/(?P<news_pk>\d+)/$', views.news_view, name='news_view'),
url(r'^announcement/news/news-detail/(?P<news_pk>\d+)/$', views.news_detail, name='news_detail'),
url(r'^announcement/news/delete/(?P<news_pk>\d+)/$', views.news_delete, name='news_delete'),

#events
url(r'^event/index/$', views.EventListView.as_view(), name='event_list'),
url(r'^event/$', views.event_wall, name='event_wall'),
url(r'^event/add/$', views.EventCreateView.as_view(), name='event_create'),
url(r'^event/edit/(?P<event_pk>\d+)/$', views.EventUpdateView.as_view(), name='event_update'),
url(r'^event/view/(?P<event_pk>\d+)/$', views.event_view, name='event_view'),
url(r'^event/event-detail/(?P<event_pk>\d+)/$', views.event_detail, name='event_detail'),
url(r'^event/delete(?P<event_pk>\d+)/$', views.event_delete, name='event_delete'),

#church
url(r'^administrator/church/index/$', views.churchListView.as_view(), name='church_list'),
url(r'^administrator/church/add/$', views.churchCreateView.as_view(), name='church_create'),
url(r'^administrator/church/update/(?P<church_pk>\d+)/$', views.churchUpdateView.as_view(), name='church_update'),
url(r'^administrator/church/(?P<church_pk>\d+)/view/$', views.church_view, name='church_view'),
url(r'^administrator/church/(?P<church_pk>\d+)/delete/$', views.church_delete, name='church_delete'),
]