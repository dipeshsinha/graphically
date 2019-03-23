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
@csrf_exempt
def bar(request):
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
            plt.bar(arrx,arry, color=col, width=x['lwidth'])

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
@csrf_exempt
def hist(request):
    if request.method == 'POST':
        try:
            x = json.loads(request.body)
            arrx = x['x']
            range = x['range']
            if x['col'] == '':
                col = 'green'
            else:
                col = x['col']
            plt.clf()
            if len(range) == 1:
                plt.hist(arrx, rwidth=x['width'], color=col)
            else :
                plt.hist(arrx, bins=range, rwidth=x['width'], color=col)

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
@csrf_exempt
def pie(request):
    if request.method == 'POST':
        try:
            x = json.loads(request.body)
            arrx = x['x']
            arry = x['y']
            # if x['lcol'] == '':
            #     col = 'green'
            # else:
            #     col = x['lcol']
            plt.clf()
            plt.pie(arrx, labels=arry, autopct='%0.1f%%', radius=1.2, explode=x['exp'])

            # if x['xlabel'] != '':
            #     plt.xlabel(x['xlabel'])
            # if x['ylabel'] != '':
            #     plt.ylabel(x['ylabel'])
            # if x['gname'] != '':
            #     plt.title(x['gname'])

            plt.savefig('plot.png', dpi=int(x['quality']))
            with open('plot.png', 'rb') as imageFile:
                data = base64.b64encode(imageFile.read()).decode()
            response = json.dumps([{'image': data}])
        except:
            response = json.dumps([{'error': 'unable to create graph'}])
        return HttpResponse(response, content_type = 'text/json')