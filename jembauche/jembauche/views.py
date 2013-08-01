from django.views.generic import TemplateView

from forms import OfferForm, ContactForm
from models import Job, JobOptions


class HomepageView(TemplateView):

    template_name = 'start.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomepageView, self).get_context_data()
        context['offer_form'] = OfferForm()
        return context

    def get(self, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        return self.render_to_response(context)

class OptionsView(TemplateView):

    template_name = 'options.html'

    def get_context_data(self, *args, **kwargs):
        context = super(OptionsView, self).get_context_data()
        context['offer_form'] = OfferForm(self.request.POST)
        context['contact_form'] = ContactForm(initial=self.request.POST)
        context['offer_data'] = self.request.POST
        return context

    def post(self, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        if (not context['offer_form'].is_valid()):
            self.template_name = 'start.html'
        else:
            job = Job()

            job.title = self.request.POST.get('title')
            job.description = self.request.POST.get('description')

            job.location_code = self.request.POST.get('localisation_code')
            job.location_city = self.request.POST.get('localisation_city')
            job.location_province = self.request.POST.get('localisation_province')
            job.location_country = self.request.POST.get('localisation_country')

            job.company = self.request.POST.get('company')

            job.contract = self.request.POST.get('contract')
            job.function_code = self.request.POST.get('function')
            job.industry_code = self.request.POST.get('industry')

            context['job'] = job

        return self.render_to_response(context)

