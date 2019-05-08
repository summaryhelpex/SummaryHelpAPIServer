from django.shortcuts import render

import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
def getsummary(article):

    return 'summary of ' + str(article)


def view(request):
@csrf_exempt
def ajax_view(request):

    data = request.POST.get('article', None)

    print(request.POST.get('article'))
    context = {'article' : data}
    return JsonResponse(context,json_dumps_params = {'ensure_ascii': True})

def ajax_view(request, *args, **kwargs):
    
    return JsonResponse({'a':'sujafdsfasjdnfkljsadfnlksjadfksdafsdaklf'})