# I have created this file - Vivek
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the feedback in text formate
    stfeedback = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercount = request.POST.get('charactercount', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in stfeedback:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        stfeedback = analyzed

    if fullcaps=="on":
        analyzed = ""
        for char in stfeedback:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        stfeedback = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in stfeedback:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        stfeedback = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(stfeedback):
            if not(stfeedback[index] == " " and stfeedback[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        stfeedback = analyzed

    if charactercount == "on":
        char_count = sum(1 for char in stfeedback if not char.isspace())
        params = {'purpose': 'New Line Remover', 'analyzed_text': char_count}

    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charactercount != "on"):
        return HttpResponse("Not Analyzed anything there. Get an Error. Thank You! Try Again!")

    return render(request, 'analyze.html', params)
