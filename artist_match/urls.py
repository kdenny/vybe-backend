from django.conf.urls import url

from artist_match import views

urlpatterns = [
    url(r'^create_artist/$', views.CreateArtist.as_view()),
    url(r'^load_artists/$', views.ArtistListView.as_view()),
    # url(r'^swipe/$', views.Swipe.as_view()),
    # url(r'^view_matches/$', views.ApartmentsListView.as_view()),
    # url(r'^match/(?P<match_id>[0-9]+)/$', views.PackagesListView.as_view()),
    # url(r'^messages/(?P<message_id>[0-9]+)/$', views.PackagesListView.as_view()),
]