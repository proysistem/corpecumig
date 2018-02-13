from django.shortcuts import render


# class IndexView(TemplateView):
#    template_name = 'inicio/index.html'
#    config = None


def IndexView(request):

    context = {}
    template = 'inicio/index.html'
    return render(request, template, context)


def nosotros(request):

    context = {}
    template = 'inicio/nosotros.html'
    return render(request, template, context)


def proyecto(request):

    context = {}
    template = 'inicio/proyecto.html'
    return render(request, template, context)
