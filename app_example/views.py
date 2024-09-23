from django.views.generic import TemplateView

from app_example.forms import StudentForm


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = StudentForm()
        context['form'].fields['changed_value'].initial = 'Valor cambiado'
        context['form'].fields['changed_value'].widget.attrs.update({'disabled': True})
        return context
