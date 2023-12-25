from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Report, InputData, ReportInputData
from .forms import EditingForm
# Create your views here.

def index(request):
    reports_list = Report.objects.order_by('id')
    template = loader.get_template('reports/index.html')
    context = {
        'reports_list': reports_list
    }
    return HttpResponse(template.render(context, request))

def report(request, report_id):
    reports_list = Report.objects.order_by('id')
    report = Report.objects.get(pk=report_id)
    data = ReportInputData.objects.filter(idRerport=report_id)
    template = loader.get_template('reports/report.html')
    Q = calculateQ(data)    
    updatedData = addNullsInData(data)
    context = {
        'reports_list': reports_list,
        'mainReport': report,
        'data': updatedData,
        'Q': Q
    }
    return HttpResponse(template.render(context, request))

def editorForm(request, report_id):
    if request.method == "POST":    
        form = EditingForm(request.POST)
        if form.is_valid():
            report = Report.objects.get(id=report_id)
            report.name = request.POST.get('name')
            report.surname = request.POST.get('surname')
            report.dateReport = request.POST.get('dateReport') 
            report.save()
            
            return redirect('reports/index.html')
    else:
        form = EditingForm()

    return render(request, 'reports/form.html', {'form': form})

def addNullsInData(data):
    for d in data:
        if d.idInputData.startTemperature == None:
            d.idInputData.startTemperature = 0
        if d.idInputData.endTemperature == None:
            d.idInputData.endTemperature = 0
        if d.idInputData.weigth == None:
            d.idInputData.weigth = 0
        if d.idInputData.thremalCapacity == None:
            d.idInputData.thremalCapacity = 0

    return data

def calculateQ(data):
    startTemperature = int()
    endTemperature = int()
    c = int()
    m = int()
    Q = int()
    for d in data:
        if d.idInputData.startTemperature != None:
            startTemperature = d.idInputData.startTemperature
        if d.idInputData.endTemperature != None:
            endTemperature = d.idInputData.endTemperature
        if d.idInputData.weigth != None:
            m = d.idInputData.weigth
        if d.idInputData.thremalCapacity != None:
            c = d.idInputData.thremalCapacity
    if startTemperature != None and endTemperature != None and c != None and m != None:
        Q += c*m*(endTemperature - startTemperature)
    return Q
