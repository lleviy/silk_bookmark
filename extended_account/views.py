from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from account.mixins import LoginRequiredMixin
from django.views import View

from unsplash_search.views import search_photos_default

from extended_account.models import Appearance
from account.views import SettingsView
from extended_account.forms import SettingsForm, AppearanceForm


class SettingsView(SettingsView):
    form_class = SettingsForm


class AppearanceView(LoginRequiredMixin, View):
    template_name = "account/new_appearance.html"
    form_class = AppearanceForm
    photos_url = search_photos_default()

    def get_initial(self, request):
        initial = {}
        if Appearance.objects.filter(owner=request.user):
            initial["photo_url"] = Appearance.objects.filter(owner=request.user)[0].photo_url
        return initial

    def get(self, request):
        form = self.form_class(initial=self.get_initial(request))
        context = {'form': form, 'photos_url': self.photos_url}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            Appearance.objects.all().delete()
            new_appearance = form.save(commit=False)
            new_appearance.owner = request.user
            new_appearance.save()
            return HttpResponseRedirect(reverse('silk_bookmarks:index'))
        context = {'form': form, 'photos_url': self.photos_url}
        return render(request, self.template_name, context)