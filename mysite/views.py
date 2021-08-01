from django.http import HttpResponse
from django.shortcuts import  render
def index(request):
    # param = {'name':"madhur"}
    return render(request,'index.html')
def about(request):
    # text = request.GET.get('text',"default")
    # punc = request.GET.get('removepunc',"off")
    # upper = request.GET.get("uppercase","off")
    # extra = request.GET.get("extratext","off")
    text = request.POST.get('text',"default")
    punc = request.POST.get('removepunc',"off")
    upper = request.POST.get("uppercase","off")
    extra = request.POST.get("extratext","off")
    punctuation = ";;:,[]"
  
    if punc == "on":
        analysed = ""
        for i in text:
            if i not in punctuation:
                analysed += i
        text = analysed
        
        # return HttpResponse(f"<h1>hello everyone</h1> {analysed} {punc}")
    if upper == "on":
        
        upper_con = text.upper()
        text = upper_con
        
        # return HttpResponse(f"{upper_con}")

    if extra == "on":
        analysed = ""
        for index,char in enumerate(text):
            if not(text[index] == " " and text[index+1]== " "):
                analysed += char
        # return HttpResponse(f"{analysed}")
        text = analysed
    
    return HttpResponse(f"{text}")
    # return render(request,'about.html')
