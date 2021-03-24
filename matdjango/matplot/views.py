
from django.shortcuts import render
import pandas as pd
import numpy as np
import seaborn as sns
# import matplotlib.colors as mplcol
import matplotlib.pyplot as plt
# Create your views here.
import io
import urllib, base64



def plot_graphs(request):
    print("asdfghjk")

    if request.method == 'POST':
        val = request.POST.get('featured')
        
        
        if(val=="Yes"):
            tag = True
            print(val)
            plt.plot(range(10))
            fig = plt.gcf()
            #convert graph into dtring buffer and then we convert 64 bit code into image
            buf = io.BytesIO()
            fig.savefig(buf,format='png')
            buf.seek(0)
            string = base64.b64encode(buf.read())
            uri =  urllib.parse.quote(string)
            buf.close()
            plt.close()

            return render(request,"base.html",{'tag':tag, 'data':uri})
        else:
            tag = 'NO'
            print(val)
            plt.plot(range(2000))
            fig1 = plt.gcf()
            #convert graph into dtring buffer and then we convert 64 bit code into image
            buf1 = io.BytesIO()
            fig1.savefig(buf1,format='png')
            buf1.seek(0)
            string1 = base64.b64encode(buf1.read())
            uri1 =  urllib.parse.quote(string1)
            buf1.close()
            plt.close()
            return render(request,"base.html",{'tag':tag, 'nimbus':uri1})

    else:
        tag = False
        return render(request,"base.html",{'tag':tag})