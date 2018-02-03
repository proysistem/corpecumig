from django.shortcuts import render


# class IndexView(TemplateView):
#    template_name = 'inicio/index.html'
#    config = None


def home(request):

    context = {}
    template = 'inicio/index.html'
    return render(request, template, context)
