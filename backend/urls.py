from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    # path('',views.index),
    # path('dashboard',views.dashboard),
    # path('systemadmin',views.systemAdmin),
    # path('login',views.login),
    # path('actionLogin',views.actionLogin),
    # path('actionLogout',views.actionLogout),
    # path('test',views.test, name='sss'),
    path('getSports',views.SportList.as_view()),
    path('getCompetitions',views.CompetitionList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
