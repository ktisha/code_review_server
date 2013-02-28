from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from code_review.views import add_review, all_authors, to_review

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'code_review_server.views.home', name='home'),
    # url(r'^code_review_server/', include('code_review_server.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # add review to database
    (r'^add_review/', add_review),
    (r'^all_authors/', all_authors),
    (r'^to_review/', to_review),
)
