from django.conf.urls import url
from .views import RulesView

app_name = 'users'
urlpatterns = [
    url(r'^reglement/$', RulesView.as_view(), name='rules_view'),
    # url(r'^events/$', planning_calendar_events, name='planning_calendar_events'),
    # url(r'^page/(?P<pk>\d+)/plan/$', ChangePagePlanning.as_view(), name='planning_calendar_plan_page'),
]
