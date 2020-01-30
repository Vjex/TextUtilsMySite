# I have created this file- Vishal Verma

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # params for sending variable to the template
    params = {'name': 'Vishal', 'place': 'Mars'}
    return render(request, 'index.html', params)


def about(request):
    return HttpResponse('<h1>Vishal Verma</h1> '
                        '<a href="https://www.youtube.com/channel/UCkUoosKezTXrM4Uc4I_aE4g?view_as=subscriber"> '
                        'Click To see My Channel </a>')


def removePunc(request):
    # Getting the text from calling page
    valueGot = request.POST.get('querryName', 'defaultValue')
    checkBoxPunc = request.POST.get('checkPunc', 'off')
    checkUpper = request.POST.get('checkUpper', 'off')
    checkNewLine = request.POST.get('checkNewLine', 'off')
    checkExtraSpace = request.POST.get('checkExtraSpace', 'off')
    # print(valueGot)
    # print(checkBoxPunc)
    if checkBoxPunc == "on":
        removedpunctext = ""
        punct_Str = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        for char in valueGot:
            if char not in punct_Str:
                removedpunctext = removedpunctext + char
        # params = {'purpose':'Remove Puntuation', 'punc': removedpunctext}

        valueGot=removedpunctext

        # return render(request, 'removedPuncTemp.html', params)

    if checkUpper == "on":
        text = ""
        for char in valueGot:
                text = text + char.upper()
        # params = {'purpose':'UPPER CASE', 'punc': text}
        valueGot=text
        # return render(request, 'removedPuncTemp.html', params)

    if checkNewLine == "on":
        text = ""
        for char in valueGot:
           if char != "\n" and char != "\r":
               text = text+char
        # params = {'purpose':'Remove New Line', 'punc': text}
        valueGot=text

        # return render(request, 'removedPuncTemp.html', params)
    if checkExtraSpace == "on":
        text = ""
        for index, char in enumerate(valueGot):
            if not (valueGot[index] == " " and valueGot[index + 1] == " "):
                text = text + char
        # params = {'purpose': 'Remove Extra Space', 'punc': text}
        valueGot=text

        # return render(request, 'removedPuncTemp.html', params)

    if checkBoxPunc != "on" and checkUpper != "on" and checkNewLine != "on" and checkExtraSpace != "on" :
        return HttpResponse('<h1>Error! Ckeck Box Not Checked. </h1> ')

    params = {'purpose': 'Analyse Text', 'punc': valueGot}
    return render(request, 'removedPuncTemp.html', params)

