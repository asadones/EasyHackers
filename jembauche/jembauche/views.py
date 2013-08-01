from django.views.generic import TemplateView

from forms import OfferForm, ContactForm


class HomepageView(TemplateView):

    template_name = 'start.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomepageView, self).get_context_data()
        if self.request.method == 'POST':
            context['offer_form'] = OfferForm(self.request.POST)
            context['contact_form'] = ContactForm(initial=self.request.POST)
            context['offer_data'] = self.request.POST
        else:
            context['offer_form'] = OfferForm()
        return context

    def get(self, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        return self.render_to_response(context)

    def post(self, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        if (context['offer_form'].is_valid()):
            self.template_name = 'finalize.html'
        return self.render_to_response(context)

