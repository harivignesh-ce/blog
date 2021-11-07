from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render


class HomePageView(TemplateView):
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse("article_list"))
        return render(self.request, "home.html")
