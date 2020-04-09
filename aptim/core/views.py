from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

class IndexTemplateView(LoginRequiredMixin, TemplateView):
  #onli authenticated users can interact with application
  def get_template_names(self):
    template_name="index.html"
    return template_name