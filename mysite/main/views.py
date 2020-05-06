from django.shortcuts import render
# from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse
from django.http import HttpResponse
from .models import Tutorial, Question
from .forms import UploadForm
# from .models import Document
# from .forms import DocumentForm
# landing page


def upload_view(request):
    context = {}
    form = UploadForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, 'main/upload.html', context)


def mainpage(request):
    return render(request=request,
                  template_name="main/mainpage.html",
                  context={"tutorials": Tutorial.objects.all})


def catchall(request, slug):
    return render(request=request,
                  template_name='main/show_tutorial.html',
                  context={"tutorials": Tutorial.objects.all,
                           "questions": Question.objects.all, "slug": slug},
                  )
