from django.views.generic import TemplateView

from datetime import datetime, timedelta
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

            job.company = self.request.POST.get('name_company')

            job.contract = self.request.POST.get('contract')
            job.function_code = self.request.POST.get('function')
            job.industry_code = self.request.POST.get('industry')

            job.end_date = datetime.now() + timedelta(30)
            job.state = 0

            job.save()

            context['job'] = job

        return self.render_to_response(context)

class FinalizeView(TemplateView):

    template_name = 'finalize.html'

    def get_context_data(self, *args, **kwargs):
        context = super(FinalizeView, self).get_context_data()
        job = Job.objects.get(pk=kwargs['job_id'])
        context['job'] = job
        context['contact_form'] = ContactForm(initial={'name_company': job.company})
        return context

    def post(self, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        job = context['job']
        options = {}
        for key in (
                'schools',
                'pe',
                'monster',
                'keljob',
                'rjobs',
            ):
            if self.request.POST.get(key) == '1':
                job_option = JobOptions()
                job_option.job_id = job
                job_option.option_data = key
                job_option.save()
                options[key] = True
            else:
                try:
                    job_option = JobOptions.objects.get(job_id=job.id, option_data=key)
                    job_option.delete()
                except JobOptions.DoesNotExist:
                    pass
                options[key] = False

        context['options'] = options

        context['price'] = 10
        if options['schools']:
            context['price'] += 10
        if options['pe']:
            context['price'] += 10
        if options['keljob']:
            context['price'] += 99
        if options['monster']:
            context['price'] += 99
        if options['rjobs']:
            context['price'] += 99

        job.state = 1
        job.save()
        return self.render_to_response(context)


class EndView(TemplateView):

    template_name = 'end.html'

    def get_context_data(self, *args, **kwargs):
        context = super(JobView, self).get_context_data()
        job = Job.objects.get(pk=kwargs['job_id'])
        context['job'] = job
        return context


class JobView(TemplateView):

    template_name = 'view.html'

    def get_context_data(self, *args, **kwargs):
        context = super(JobView, self).get_context_data()
        job = Job.objects.get(pk=kwargs['job_id'])
        context['job'] = job
        return context
