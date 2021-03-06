"""factura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'ventas.views.main'),
    url(r'^login/$', 'ventas.views.login_user'),
    url(r'^logout/$', 'ventas.views.logout_user'),
    url(r'^register/$', 'ventas.views.register_user'),
    url(r'^empresa/$',  'ventas.views.index_empresa'),
    url(r'^empresa/add/$', 'ventas.views.add_empresa'),
    url(r'^empresa/edit/(?P<pk>\d+)$', 'ventas.views.edit_empresa'),
    url(r'^empresa/delete/(?P<pk>\d+)$', 'ventas.views.delete_empresa'),
    url(r'^categoria/$',  'ventas.views.index_categoria'),
    url(r'^categoria/add/$', 'ventas.views.add_categoria'),
    url(r'^categoria/edit/(?P<pk>\d+)$', 'ventas.views.edit_categoria'),
    url(r'^categoria/delete/(?P<pk>\d+)$', 'ventas.views.delete_categoria'),
    url(r'^tipodoc/$',  'ventas.views.index_tipodoc'),
    url(r'^tipodoc/add/$', 'ventas.views.add_tipodoc'),
    url(r'^tipodoc/edit/(?P<pk>\d+)$', 'ventas.views.edit_tipodoc'),
    url(r'^tipodoc/delete/(?P<pk>\d+)$', 'ventas.views.delete_tipodoc'),
    url(r'^tipocaja/$',  'ventas.views.index_tipocaja'),
    url(r'^tipocaja/add/$', 'ventas.views.add_tipocaja'),
    url(r'^tipocaja/edit/(?P<pk>\d+)$', 'ventas.views.edit_tipocaja'),
    url(r'^tipocaja/delete/(?P<pk>\d+)$', 'ventas.views.delete_tipocaja'),
    url(r'^cuentabanco/$',  'ventas.views.index_cuentabanco'),
    url(r'^cuentabanco/add/$', 'ventas.views.add_cuentabanco'),
    url(r'^cuentabanco/edit/(?P<pk>\d+)$', 'ventas.views.edit_cuentabanco'),
    url(r'^cuentabanco/delete/(?P<pk>\d+)$', 'ventas.views.delete_cuentabanco'),
    url(r'^formapago/$',  'ventas.views.index_formapago'),
    url(r'^formapago/add/$', 'ventas.views.add_formapago'),
    url(r'^formapago/edit/(?P<pk>\d+)$', 'ventas.views.edit_formapago'),
    url(r'^formapago/delete/(?P<pk>\d+)$', 'ventas.views.delete_formapago'),
    url(r'^banco/$',  'ventas.views.index_banco'),
    url(r'^banco/add/$', 'ventas.views.add_banco'),
    url(r'^banco/edit/(?P<pk>\d+)$', 'ventas.views.edit_banco'),
    url(r'^banco/delete/(?P<pk>\d+)$', 'ventas.views.delete_banco'),
    #url(r'^banco/bulk$',  'ventas.views.bulk_insert'),
    url(r'^tipoimpuesto/$',  'ventas.views.index_tipoimpuesto'),
    url(r'^tipoimpuesto/add/$', 'ventas.views.add_tipoimpuesto'),
    url(r'^tipoimpuesto/edit/(?P<pk>\d+)$', 'ventas.views.edit_tipoimpuesto'),
    url(r'^tipoimpuesto/delete/(?P<pk>\d+)$', 'ventas.views.delete_tipoimpuesto'),    
    url(r'^articulo/$',  'ventas.views.index_articulo'),
    url(r'^articulo/add/$', 'ventas.views.add_articulo'),
    url(r'^articulo/edit/(?P<pk>\d+)$', 'ventas.views.edit_articulo'),
    url(r'^articulo/delete/(?P<pk>\d+)$', 'ventas.views.delete_articulo'),
    url(r'^articulo/search/$', 'ventas.views.search_articulo'),
    url(r'^articulo/searchcode/$', 'ventas.views.search_articulo_codigo'),
    url(r'^cliente/$',  'ventas.views.index_cliente'),
    url(r'^cliente/add/$', 'ventas.views.add_cliente'),
    url(r'^cliente/qadd/$', 'ventas.views.qadd_cliente'),
    url(r'^cliente/edit/(?P<pk>\d+)$', 'ventas.views.edit_cliente'),
    url(r'^cliente/delete/(?P<pk>\d+)$', 'ventas.views.delete_cliente'),
    url(r'^cliente/search/$', 'ventas.views.search_cliente'),
    url(r'^cliente/searchid/$', 'ventas.views.search_cliente_id'),
    url(r'^proveedor/$',  'ventas.views.index_proveedor'),
    url(r'^proveedor/add/$', 'ventas.views.add_proveedor'),
    url(r'^proveedor/edit/(?P<pk>\d+)$', 'ventas.views.edit_proveedor'),
    url(r'^proveedor/delete/(?P<pk>\d+)$', 'ventas.views.delete_proveedor'),
    url(r'^proveedor/search/$', 'ventas.views.search_proveedor'),
    url(r'^proveedor/searchid/$', 'ventas.views.search_proveedor_id'),
    url(r'^factura/$',  'ventas.views.index_factura'),
    url(r'^factura/add/$', 'ventas.views.add_factura'),
    url(r'^factura/edit/(?P<pk>\d+)$', 'ventas.views.edit_factura'),
    url(r'^factura/delete/(?P<pk>\d+)$', 'ventas.views.delete_factura'),
    url(r'^detalle/(?P<pk>\d+)$', 'ventas.views.detalle'),
    url(r'^detalle/delete/(?P<pk>\d+)/(?P<fact>\d+)/$', 'ventas.views.delete_detalle'),    
    url(r'^postext/$',  'ventas.views.postext'),
    url(r'^postext/addline/$',  'ventas.views.add_postext'),
    url(r'^postext/delline/$',  'ventas.views.del_postext'),
    url(r'^postext/addcobro/$',  'ventas.views.add_cobro'),
    url(r'^postext/delcobro/$',  'ventas.views.del_cobro'),
    url(r'^factcompra/$',  'ventas.views.index_factcompra'),
    url(r'^factcompra/add/$', 'ventas.views.add_factcompra'),
    url(r'^factcompra/edit/(?P<pk>\d+)$', 'ventas.views.edit_factcompra'),
    url(r'^factcompra/delete/(?P<pk>\d+)$', 'ventas.views.delete_factcompra'),
    url(r'^detallefc/(?P<pk>\d+)$', 'ventas.views.detallefc'),
    url(r'^detallefc/delete/(?P<pk>\d+)/(?P<fact>\d+)/$', 'ventas.views.delete_detallefc'),    
    url(r'^opencaja/$',  'ventas.views.opencaja'),
    url(r'^closecaja/$',  'ventas.views.closecaja'),
    url(r'^movcaja/$',  'ventas.views.movcaja'),
    url(r'^movcaja/add/$',  'ventas.views.add_movcaja'),
    url(r'^movcaja/sub/$',  'ventas.views.sub_movcaja'),
    url(r'^movcaja/search/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$',  'ventas.views.search_movcaja' ,name='search_mc'),
    url(r'^openturno/$',  'ventas.views.openturno'),
    url(r'^closeturno/$',  'ventas.views.closeturno'),
    url(r'^inventario/$',  'ventas.views.index_inventario'),
    url(r'^inventario/add/$',  'ventas.views.add_inventario'),
    url(r'^inventario/search/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$',  'ventas.views.search_inventario' ,name='search_inv'),
    #url(r'^inventario/search/$',  'ventas.views.search_inventario', name='search_inv'),
    url(r'^reportes/inventario/$',  'ventas.views.rptinventarios'),
    url(r'^reportes/ventas/$',  'ventas.views.ventas'),
    url(r'^reportes/compras/$',  'ventas.views.rptcompras'),
]
