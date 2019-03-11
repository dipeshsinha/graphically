from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
import matplotlib.pyplot as plt
import base64

@csrf_exempt
def line(request):
    if request.method == 'POST':
        try:
            x = json.loads(request.body)
            arrx = x['x']
            arry = x['y']
            if x['lcol'] == '':
                col = 'green'
            else:
                col = x['lcol']
            plt.clf()
            plt.plot(arrx,arry, color=col,
             linewidth=x['lwidth'],
             alpha=x['opacity'], 
             linestyle=x['linestyle'], 
             marker=x['marker'], 
             markerfacecolor=x['mcolor'], markersize=x['msize'])

            if x['xlabel'] != '':
                plt.xlabel(x['xlabel'])
            if x['ylabel'] != '':
                plt.ylabel(x['ylabel'])
            if x['gname'] != '':
                plt.title(x['gname'])

            plt.savefig('plot.png', dpi=int(x['quality']))
            with open('plot.png', 'rb') as imageFile:
                data = base64.b64encode(imageFile.read()).decode()
            response = json.dumps([{'image': data}])
        except:
            response = json.dumps([{'error': 'unable to create graph'}])
        return HttpResponse(response, content_type = 'text/json')