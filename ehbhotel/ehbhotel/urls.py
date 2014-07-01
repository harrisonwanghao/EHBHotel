from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ehbhotel.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'kiosk.views.Index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^customer/register/$', 'customers.views.CustomerRegistration'),
    url(r'^customer/login/$', 'customers.views.CustomerLogin'),
    url(r'^customer/logout/$', 'customers.views.CustomerLogout'),
    url(r'^customer/invoice/$', 'customers.views.CustomerInvoice'),
    url(r'^customer/$', 'customers.views.CustomerProfile'),
    url(r'^employee/login/$', 'employee.views.EmployeeLogin'),
    url(r'^employee/logout/$', 'employee.views.EmployeeLogout'),
    url(r'^employee/$', 'employee.views.EmployeeProfile'),
    url(r'^employee/dinner/$', 'employee.views.Menu'),
    url(r'^employee/dinner/preparation/$', 'employee.views.Preparation'),
    url(r'^employee/dinner/dessert/$', 'employee.views.Dessert'),
    url(r'^employee/dinner/main/$', 'employee.views.Main'),
    url(r'^employee/dinner/menu/$', 'employee.views.Menu'),
    url(r'^employee/dinner/starter/$', 'employee.views.Starter'),
    url(r'^addroom/$', 'rooms.views.RoomAdd'),
    url(r'^rooms/$', 'rooms.views.RoomList'),
    url(r'^addproduct/$', 'products.views.ProductAdd'),
    url(r'^products/$', 'products.views.ProductList'),
    url(r'^addreservation/$', 'reservations.views.ReservationAdd'),
    url(r'^reservations/$', 'reservations.views.ReservationList'),
    url(r'^addtransaction/$', 'transactions.views.TransactionAdd'),
    url(r'^transactions/$', 'transactions.views.TransactionList'),
    url(r'^translate/$', 'dinner.views.Translate'),
    url(r'^dinner/$', 'dinner.views.Index'),
    url(r'^dinner/resto/$', 'dinner.views.Resto'),
    url(r'^dinner/menu/$', 'dinner.views.Menu'),
    url(r'^dinner/gallery/$', 'dinner.views.Gallery'),
    url(r'^dinner/info/$', 'dinner.views.Info'),
    url(r'^dinner/contact/$', 'dinner.views.Contact'),
    url(r'^statistics/$', 'statistics.views.Overview'),
    url(r'^kiosk/$', 'kiosk.views.Index'),
    url(r'^contact/$', 'contacts.views.contactview'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()