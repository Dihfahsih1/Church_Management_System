from django.conf.urls import url
from django.urls import reverse,path
from . import views

urlpatterns=[
#Dashboard and website homepage urls
url(r'^home', views.web, name='index_public'),
url(r'^$', views.index, name='index'),

######################============>CHURCH SYSTEM URLS<=========#####################
url(r'^Expenses/Main-Expenses', views.enter_main_expenses, name='enter_expenditure'),
url(r'^Expenses/Petty-Expenses/', views.enter_petty_expenses, name='enter_sundryexpense'),
url(r'^Expenses/General-Expenses/Enter', views.enter_general_expenses, name='enter-general-expenses'),
url(r'^Allowances/Add/', views.give_allowance, name='give-allowance'),
url(r'^Record-Offerings/', views.Enter_Offerings, name='Enter_Offerings'),
url(r'^RECORD-CASHFLOAT/', views.record_cashfloat, name='record-cashfloat'),
path('Top-Up-Cashfloat/<str:pk>/', views.cashfloat_topup, name='cashfloat_topup'),
url(r'^Revenue/Seeds/Add/', views.add_seeds, name='add-seeds'),
url(r'^Revenues/Tithes/Add', views.recording_tithes, name='Enter_Tithes'),
url(r'^Enter_Pledges/', views.Enter_Pledges, name='Enter_Pledges'),
url(r'^Revenue/Thanks-giving/Add', views.record_thanks_giving,name='record-thanks-giving'),
url(r'^Revenue/Other-Sources/Add', views.record_donations, name='record-donations'),
#group contributions 

url(r'^Revenue/Group/Add', views.record_group_contributions, name='record-group-contribution'),
url(r'^Revenue/Group-Contributions', views.list_group_contributions, name='list-group-contributions'),

url(r'^Pledges/Add-Item/', views.add_Pledge_Items ,name='add-pledge-item'),
url(r'^Employees/Add/', views.employee_register, name='employee-register'),
url(r'^Membership/Register/', views.register_members, name='members-register'),
url(r'^Visitors/Register/', views.register_visitors, name='visitors-register'),
url(r'^print-members', views.print_all_members.as_view(), name='print_all_members'),

# SEARCH ALL ARCHIVED REPORTS
url(r'^pledgesarchivessearch/', views.pledgesarchivessearch, name='pledgesarchivessearch'),
url(r'^offeringsarchivessearch/', views.offeringsarchivessearch, name='offeringsarchivessearch'),
url(r'^Archives/Salaries/', views.salariespaidarchivessearch, name='salariespaidarchivessearch'),
url(r'^Archives/Seeds/', views.seedsarchivessearch, name='seeds-archives-search'),
url(r'^Archives/Building-Renovations/', views.BuildingRenovationarchivessearch, name='BuildingRenovationarchivessearch'),
url(r'^General-Expenses/Archived/', views.general_expenses_archives_search, name='general-expensesarchives-search'),
url(r'^Main-Expenses/Archived/', views.main_expenses_archives_search, name='expensesarchivessearch'),
url(r'^Petty-Cash/Archived/', views.petty_cash_archives_search, name='sundryarchivessearch'),
url(r'^allowancearchivessearch/', views.allowancearchivessearch, name='allowancearchivessearch'),
url(r'^Archives/Other-Sources/', views.donationsarchivessearch, name='donationsarchivessearch'),
url(r'^Archived/Tithes/', views.tithesarchivessearch, name='tithesarchivessearch'),
url(r'^Archives/Thanks-Giving/', views.thanksgivingarchivessearch, name='thanksgivingarchivessearch'),

#EXPENDITURE MODULE URLS
url(r'^Edit/General-Expense/(?P<pk>\d+)', views.edit_general_expense ,name='edit-general-expense'),
url(r'^Main-Expense/Edit/(?P<pk>\d+)', views.edit_main_expense ,name='edit-main-expense'),
url(r'^Petty-Expense/Edit/(?P<pk>\d+)', views.edit_petty_cash ,name='edit-petty-cash'),
url(r'^Reports/Main-Expenses/', views.main_expenses_report, name='expenditurereport'),
url(r'^Reports/General-Expenses/', views.general_expenses_report, name='general-expenses-report'),
url(r'^Reports/Sundry-Report/', views.petty_cash_report, name='sundryreport'),
url(r'^Main-Expenses-Report/pdf/', views.main_expenditure_report_pdf.as_view(), name='mainpdf'),
url(r'^General-Expenses-Archived/(?P<report_month>.+?)/(?P<report_year>.+?)/', views.general_expenses_archived_pdf.as_view(), name='generalarchivepdf'),
url(r'^Main-Expenses-Archived/(?P<report_month>.+?)/(?P<report_year>.+?)/', views.main_expenses_archived_pdf.as_view(), name='mainarchivepdf'),
url(r'^Report/Allowances/', views.allowancereport, name='allowancereport'),
url(r'^Edit/allowance/(?P<pk>\d+)', views.edit_allowance ,name='edit_allowance'),
url(r'^Receipt/Allowance/(?P<pk>\d+)', views.allowancereceipt.as_view() ,name='allowance-receipt'),
url(r'^allowancespdf/', views.allowancespdf.as_view() ,name='allowancespdf'),
url(r'^allowancearchivepdf/(?P<report_month>.+?)/(?P<report_year>.+?)/', views.allowances_archived_pdf.as_view(), name='allowancearchivepdf'),
url(r'^Church-Groups', views.church_groups, name='church-groups'),
url(r'^Home-Cells', views.home_cells, name='home-cells'),
url(r'^Petty-Expenses-Report/pdf/', views.petty_expenditure_report_pdf.as_view(), name='pettypdf'),
url(r'^Archived-Petty-Expenses/pdf/(?P<report_month>.+?)/(?P<report_year>.+?)/', views.petty_expenses_archived_pdf.as_view(), name='archivedpettypdf'),

url(r'^General-Expenses-Report/pdf/', views.general_expenditure_report_pdf.as_view(), name='generalpdf'),
#REVENUE MODULE
url(r'^Revenues/Offerings/Report', views.Offeringsreport, name='Offeringsreport'),
url(r'^edit_offerings/(?P<pk>\d+)', views.edit_offerings ,name='edit-offerings'),
url(r'^offeringspdf/', views.offeringspdf.as_view() ,name='offeringspdf'),
url(r'^offeringsarchivepdf/(?P<report_month>.+?)/(?P<report_year>.+?)/', views.offeringsarchivepdf.as_view(), name='offeringsarchivepdf'),

url(r'^REVENUES/', views.total_revenues, name='total_revenues'),
url(r'^EXPENSES/', views.total_expenses, name='total_expenses'),

#CASHFLOAT
url(r'^CASHFLOAT/LIST', views.cashfloat_lst, name='cashfloat-list'),
url(r'^EDIT-CASHFLOAT/(?P<pk>\d+)', views.edit_cash_float ,name='edit-cashfloat'),

#Seeds Module
url(r'^Revenues/Seeds-Report', views.Seedsreport, name='Seeds-report'),
url(r'^Revenue/Seeds/Edit/(?P<pk>\d+)', views.edit_seed,name='edit-seed'),
url(r'^Receipts/Seed-Offering/(?P<pk>\d+)', views.seed_offering_receipt.as_view() ,name='seed-offering-receipt'),
url(r'^Archives/Seeds/', views.seedsarchivessearch, name='seeds-archives-search'),

#Tithes Module
url(r'^Print/Tithespdf/', views.tithespdf.as_view() ,name='tithespdf'),
url(r'^Tithes/receipt/(?P<pk>\d+)', views.tithesreceipt.as_view() ,name='tithesreceipt'),
url(r'^tithes/archivepdf/(?P<report_month>.+?)/(?P<report_year>.+?)/', views.tithesarchivepdf.as_view(), name='tithesarchivepdf'),
url(r'^Edit/tithes/(?P<pk>\d+)', views.edit_tithes ,name='edit-tithes'),
url(r'^Tithesreport/', views.Tithesreport, name='Tithesreport'),
url(r'^General-Annual-Tithes/', views.Annual_Tithes, name='Annual-Tithes'),


url(r'^Building-Renovations/', views.record_building_collections, name='record-building-collections'),
url(r'^Revenue/Building-Collections/Edit/(?P<pk>\d+)', views.edit_building_collections,name='edit-building-collections'),

url(r'^Revenue/Thanks-Giving/Edit/(?P<pk>\d+)', views.edit_thanks_giving,name='edit-thanks-giving'),
url(r'^Reports/Thanks-giving/List', views.thanks_giving_report,name='thanks-giving-report'),

url(r'^Reports/Other-Sources/List', views.donations_report, name='donations-report'),
url(r'^Revenue/Other-Sources/Edit/(?P<pk>\d+)', views.edit_donation,name='edit-donation'),
url(r'^pledgespdf/', views.pledgespdf.as_view() ,name='pledgespdf'),


# url(r'^Archived/Pledge-Debt/Receipt/(?P<pk>\d+)', views.settled_archived_pledge_receipt.as_view() ,name='settled-pledge-receipt'),
url(r'^Archived/Pledge-Debt/Invoice/(?P<pk>\d+)', views.pledge_debt_invoice.as_view() ,name='pledge-invoice'),
url(r'^pledgesreceipt/(?P<pk>\d+)', views.pledgesreceipt.as_view() ,name='pledgesreceipt'),
#url(r'^sundryarchivepdf/(?P<report_month>.+?)/(?P<report_year>.+?)/', views.sundryarchivepdf.as_view(), name='sundryarchivepdf'),
url(r'^pledgesarchivepdf/(?P<report_month>.+?)/(?P<report_year>.+?)/', views.pledgesarchivepdf.as_view(), name='pledgesarchivepdf'),
#Handling all PKs, IDs
url(r'^Pledges-Made/Invoice/(?P<pk>\d+)', views.pledge_made_invoice.as_view(), name='pledge-made-invoice'),
url(r'^Church-Member/Edit/(?P<pk>\d+)', views.edit_member ,name='edit-member'),
url(r'^Archive/Church-Member/(?P<pk>\d+)', views.archive_member ,name='archive-member'),
url(r'^Un-Archive/Church-Member/(?P<pk>\d+)',views.unarchive_member, name='un-archive-member'),
url(r'^Employee/Delete/(?P<pk>\d+)', views.delete_employee ,name='delete-employee'),
url(r'^Church-Visitor/Edit/(?P<pk>\d+)', views.edit_visitor ,name='edit-visitor'),
url(r'^Church-Visitor/Delete/(?P<pk>\d+)', views.delete_visitor ,name='delete-visitor'),
url(r'^edit_pledges/(?P<pk>\d+)', views.edit_pledges ,name='edit_pledges'),
url(r'^Employee/Edit/(?P<pk>\d+)', views.edit_employee ,name='edit-employee'),
url(r'^Employee/View/(?P<pk>\d+)', views.view_employee ,name='view-employee'),
url(r'^Member/View/(?P<pk>\d+)', views.view_member ,name='view-member'),
url(r'^Pledges-Item/Delete/(?P<pk>\d+)', views.delete_pledge_item ,name='delete-pledge-item'),
url(r'^Pledges-Item/Edit/(?P<pk>\d+)', views.edit_pledge_item ,name='edit-pledge-item'),
url(r'^Pledgesreport/', views.Pledgesreport, name='Pledgesreport'),
url(r'^Building-Renovations-Report/', views.Building_Renovation_report, name='Building-Renovation-report'),

url(r'^Members/Annual-Tithes/(?P<pk>\d+)', views.member_annual_tithes, name='annual-tithes'),
url(r'^Membership/List/', views.members_list, name='members-list'),
url(r'^Archived/Members/List/', views.members_archived, name='members-archived'),
url(r'^Visitors/List/', views.visitors_list, name='visitors-list'),
url(r'^Pledges/Cash/Paid', views.cashing_out_items, name='cashing-out-items'),
url(r'^Pledges-Items-List/', views.list_of_pledge_items, name='list-of-pledge-items'),
url(r'^paying_pledges/(?P<pk>\d+)', views.paying_pledges, name='paying_pledges'),
url(r'^Pledges/Cash-Out/(?P<pk>\d+)', views.pledge_cash_out, name='pledge-cash-out'),
url(r'^Pledges/view/(?P<pledge_pk>\d+)/$', views.pledge_view, name='pledge_view'),

#Employees
url(r'^Employees/List/', views.employee_list, name='employee-list'),
url(r'^Employees/Pay/(?P<pk>\d+)', views.paying_employees, name='pay-employee'),
url(r'^Employees/Salary/Paid/', views.paid_salary, name='paid-salary'),
url(r'^Employees/Salary/Paid-List/', views.current_month_salary_paid, name='current-month-salaries'),
url(r'^Petty-Expenses/Airtime/', views.airtime_data_report, name='airtime-data-report'),
url(r'^Employee/Salary/Delete/(?P<pk>\d+)', views.delete_salary_paid,name='delete-salary-paid'),

########################=======>WEBSITE URLS<=======#################################
url(r'^feedback', views.contact, name='contact'),
url(r'^online-register/$', views.Online_Registration, name='online_registration'),
url(r'^Church/Members', views.membership_wall, name='membership_wall'),
url(r'^Member/Details/(?P<pk>\d+)', views.member_detail, name='member-detail'),
url(r'^Church/Vision', views.abouts_vision, name='abouts_vision'),
url(r'^Church-Mission', views.abouts_mission, name='abouts_mission'),
url(r'^core-values', views.core_values, name='core_values'),
url(r'^church-details', views.church_details, name='church_details'),
url(r'^Pastoral-Team', views.church_pastors, name='church_pastors'),
url(r'^Administrative-Team', views.church_administration, name='church_administration'),

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
url(r'^gallery/image/index/', views.ImageListView.as_view(), name='image_list'),
url(r'^gallery/image/create/$', views.ImageCreateView.as_view(), name='image_create'),
url(r'^gallery/image/update/(?P<image_pk>\d+)/$', views.ImageUpdateView.as_view(), name='image_update'),
url(r'^gallery/image/view/(?P<image_pk>\d+)/$', views.image_view, name='image_view'),
url(r'^gallery/image/delete/(?P<image_pk>\d+)/$', views.image_delete, name='image_delete'),

#News
url(r'^Articles/index/$', views.NewsListView.as_view(), name='news_list'),
url(r'^Articles/$', views.news_wall, name='news_wall'),
url(r'^Articles/add/$', views.NewsCreateView.as_view(), name='news_create'),
url(r'^Articles/update/(?P<news_pk>\d+)/$', views.NewsUpdate, name='news_update'),
url(r'^Articles/view/(?P<news_pk>\d+)/$', views.news_view, name='news_view'),
path('Gospel/<slug:slug>', views.news_detail, name="news_detail"),
url(r'^Articles/delete/(?P<news_pk>\d+)/$', views.news_delete, name='news_delete'),
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
url(r'^administrator/church/add/$', views.churchCreateView, name='church_create'),
url(r'^administrator/church/update/(?P<church_pk>\d+)/$', views.churchUpdateView, name='church_update'),
url(r'^administrator/church/(?P<church_pk>\d+)/view/$', views.church_view, name='church_view'),
url(r'^administrator/church/(?P<church_pk>\d+)/delete/$', views.church_delete, name='church_delete'),

#Ministry
url(r'^Ministry/list/$', views.MinistryListView.as_view(), name='ministry-list'),
url(r'^Ministry/$', views.ministry_wall, name='ministry-wall'),
url(r'^Ministry/add/$', views.MinistryCreateView.as_view(), name='ministry-create'),
url(r'^Ministry/update/(?P<ministry_pk>\d+)/$', views.MinistryUpdateView.as_view(), name='ministry-update'),
url(r'^Ministry/view/(?P<ministry_pk>\d+)/$', views.ministry_view, name='ministry-view'),
url(r'^Ministry/ministry-detail/(?P<ministry_pk>\d+)/$', views.ministry_detail, name='ministry-detail'),

#Projects
url(r'^Projects/index/$', views.ProjectsListView.as_view(), name='projects_list'), 
url(r'^Projects/$', views.projects_wall, name='projects_wall'),
url(r'^Projects/add/$', views.ProjectsCreateView, name='projects_create'),
url(r'^project/edit/(?P<project_pk>\d+)/$', views.ProjectUpdate, name='project_update'),
url(r'^project/view/(?P<project_pk>\d+)/$', views.projects_view, name='projects_view'),
url(r'^project/project-detail/(?P<project_pk>\d+)/$', views.project_detail, name='project_detail'),

url(r'^auto-complete/$', views.Autocomplete.as_view(), name='auto-complete'),
url(r'^theme/$', views.ThemeListView.as_view(), name='theme_list'),
url(r'^theme/activate/(?P<theme_pk>\d+)/$', views.theme_activate, name='theme_activate'),
url(r'^tithes/annual/(?P<pk>\d+)/$', views.member_annual_tithes_pdf.as_view(), name='annual-tithes-pdf'),
url(r'^Membership/Approval/(?P<pk>\d+)/$', views.approve_member, name='approve-member'),
url(r'^Un-Approved-Membership/$', views.un_approved_members_list, name='un-approved-list'),
url(r'^Reject-Membership/(?P<pk>\d+)/$', views.reject_request, name='reject-request'),
path('activate/<str:uidb64>/<str:token>/',views.activate_email, name='activate'), 

#Conference
path('Record-Conference', views.record_annual_conference, name='record_annual_conference'),
path('list-of-conferences', views.list_of_conferences, name='list_of_conferences'),
path('<int:pk>/', views.edit_conference_details, name='edit_conference_details'),
#New Converts
path('New-Converts', views.record_new_convert, name='record_new_convert'),
path('List-New-Converts', views.new_converts_list, name='new_converts_list'),
path('<int:pk>/', views.edit_new_convert, name='edit_new_convert'),

# SUPPORT MODULE
url(r'^Ministry-Support/', views.Supportreport, name='Supportreport'),
url(r'^Revenues/Member-Support/(?P<pk>\d+)', views.record_member_support, name='record-member-support'),
path('Support-Edit/<str:pk>/', views.edit_support, name='edit-support'),
url(r'^Support-receipt/(?P<pk>\d+)', views.supportreceipt.as_view() ,name='supportreceipt'),

path('cells', views.cells, name='cells'),
path('groups', views.groups, name='groups'),


#lwaki oli mulamu
path('lwakiolimulamu_archives/<str:year>',views.lwakiolimulamu_archives,name="lwakiolimulamu_year_archive"),
path('lwaki-oli-mulamu', views.record_lwakiolimulamu, name='record'),
path('lwakiolimulamu', views.lwakiolimulamu_list, name='lwakiolimulamu'),
path('update_lwaki_oli_mulamu<int:pk>/', views.edit_lwakiolimulamu, name='edit_lwakiolimulamu'),
path('list_of_lwakiolimulamu', views.lwakiolimulamu_wall, name='lwakiolimulamu_wall'),
path('lwaki_oli_mulamu_details_<int:pk>/', views.lwakiolimulamu_detail, name='lwakiolimulamu_detail'),

#Blog Module
path('create-blogpost/', views.add_blogpost, name="blog"),
path('blog-posts/', views.list_blogs, name="blogposts"),
path('blogs', views.BlogPosts, name="Blog_Posts"),
path('UCC-Bwaise-Blogs/', views.blog_wall, name="blogs_wall"),
path('blogs/<slug:slug>/', views.BlogPost_detail, name="BlogPost_detail"),

path('search_tagged_blogs/', views.search_tagged_blogs, name="search_tagged_blogs"),

path('tagged_articles/', views.tagged_articles, name="tagged_articles"),

#rest framework urls
path('memebership/api', views.MemberAPIView.as_view())
]
