from asyncio.windows_events import NULL
from multiprocessing import context
from pipes import Template
from re import template
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import *
from .forms import *
import pandas as pd
import numpy as np
from django.shortcuts import redirect, render
import math
import json
from django.views.generic import TemplateView
import statistics 
import os
from django.core.exceptions import ValidationError
ratamape=""
class UploadView(CreateView):
    model = Upload
    
    fields = ['upload_file', ]
    success_url = reverse_lazy('tabel')
                
    def get_context_data(self, **kwargs):
                
        context = super().get_context_data(**kwargs)
        context['documents'] = Upload.objects.all()       
        return context
def input(request):
    form = DForm
    tabel = Tabel.objects.all()
    maks=''
    minim=''
    dmaks=''
    dmin=''
    ba=''
    bb=''
    jd=''
    bk=''
    ra=''
    lin=''
    status=0
    bal1=[]
    bbl1=[]
    bal2=[]
    bbl2=[]
    mid=[]
    jum=0
    suku=[]
    varis=[]
    vari=[]
    datbanding=[]
    datbanding2=[]
    datper=[]
    n=[]
    mat=[]
    matw=[]
    klsin=""
    dfz=""
    ratamape=""
    if request.method == 'POST':
        status=1
        form = DForm(request.POST)
        for j in tabel:
            n.append(j.data)
            maks=max(n)
            minim=min(n)
            
        if form.is_valid():
            dmaks=form.cleaned_data['d2']
            dmin=form.cleaned_data['d1']
            status=2
            ba= maks+dmaks
            bb=minim-dmin
            ra=ba-bb
            jd=len(n)
            bk=int(round(1+3.32*math.log10(jd),0))
            lin=int(round(ra/bk,0))
            for m in range(bk):
                bal1.append(lin)
            bal1[0]=bb
            for b in range(len(bal1)):
                jum=jum+bal1[b]
                bal2.append(jum)
            for m in range(bk):
                bbl1.append(lin)
            bbl1[0]=bb+lin
            jum=0
            for b in range(len(bbl1)):
                jum=jum+bbl1[b]
                bbl2.append(jum)
            for c in range(len(bbl2)):
                for d in range(len(bal2)):
                    if c==d:
                        ave=int(round(np.average((bbl2[c],bal2[d])),0))
                        mid.append(ave)        
            for i in n:
                for j in range(len(bbl2)):
                    for k in range(len(bal2)):
                        if  j==k:
                            if i >= bal2[k] and i < bbl2[j]:
                                g = 'A'+str(k+1)
                                vari.append(g)
            for i,d in enumerate(bbl2):
                k = 'U'+str(i+1)
                g = 'A'+str(i+1)
                suku.append(k)
                varis.append(g)
            per=[]
            tabel = Tabel.objects.all()
            for i,d in enumerate(tabel):
                for j in range(len(vari)):
                    if i==j:
                        d.ket1=vari[j]
                        datbanding.append(vari[j])
                        d.save()       
                for k in range(len(vari)):
                    if i+1==k:
                        vari.append(vari[-1])
                        d.ket2=vari[k]
                        datbanding2.append(vari[k])
                        d.save()
            ka=[]
            bar = [0 for i in range(len(varis))]
            mat = [bar.copy() for i in range(len(varis))]
            matw = []
            for i in range(1,len(datbanding)):
                for j in range(1,len(datbanding2)):
                    if i==j:
                        ka.append(datbanding[i]+datbanding2[j])
            print(ka)
            for j in range(len(mat)):
                for l in range(len(mat)):
                    for i in range(len(ka)):
                        ps=ka[i][1]
                        pk=ka[i][-1]
                        p=mat[(int(ps)-1)][(int(pk)-1)]
                        p+=1/len(varis)**2
                        mat[(int(ps)-1)][(int(pk)-1)]=p
            for j in range(len(mat)):
                df = pd.DataFrame(mat[j])
                for i in df:
                    df[i]=round(df[i],2)
                    df[i]=df[i].astype(int)
                    pembagi=df[i].sum()
                    if pembagi==0:
                        pembagi=1
                    df[i]=df[i]*mid
                    per.append(int(round(df[i].sum()/pembagi,0)))
            for i,d in enumerate(tabel):
                for w in range(len(datbanding)):
                    if i==w:
                        b=int(datbanding[w][-1])-1
                        d.peramalan=per[b]
                        datper.append(per[b])
                        d.save()
                for k in range(1,len(n)):
                    for l in range(1, len(datper)):
                        if i==k==l:
                            d.akurasi=round((abs(n[k]-datper[l]))/n[k]*100,2)
                            d.save()
            for l in range(len(mat)):
                matw.append(mat[l])
                for j in range(len(mat[l])):
                    mat[l][j]=int(round(mat[l][j],2))
                    for k in range(len(varis)):
                        if j==k:
                            if mat[l][j]>0:
                                matw[l][j]=str(mat[l][j])+varis[k]
            a=[]
            s=[]
            for j in range(len(matw)):
                a.append(set(matw[j]))
            for c in range(len(a)):
                try:
                    a[c].remove(0)
                    s.append(','.join(a[c]))
                except:
                    s.append(','.join(a[c]))
            try:    
                tabel=Tabel.objects.all().values()[1:len(tabel)]
                df=pd.DataFrame(tabel)
                df=df.akurasi.tolist()
                for a in range(len(df)):
                    df[a]=float(df[a])
            except:
                df=[0.0]
            jumlah=sum(df)
            pm=len(df)
            ratamape=round(jumlah/pm,2)
            ratarata=Rata.objects.all()
            if len(ratarata)==0:
                Rata.objects.create(
                    rata=ratamape,
                )
            else:
                Rata.objects.update(
                    rata=ratamape,
                )
            dfz=Defuzzyfikasi.objects.all()
            klsin=KelasInt.objects.all()
            for a in range(len(varis)):
                dfzz=Defuzzyfikasi(
                    cr=varis[a],
                    ns=s[a],
                    peram=per[a],
                )
                dfzz.save()
                klsi=KelasInt(
                    ki=suku[a],
                    batasatas=bal2[a],
                    batasbawah=bbl2[a],
                    midpoint=mid[a],
                )
                klsi.save()

    context={'maks':maks, 'minim':minim, 'dmaks':dmaks,
    'form':form,'dmin':dmin, 'ba':ba, 'bb':bb, 'jd':jd,'klsin':klsin,
    'bk':bk,'lin':lin, 'ra':ra, 'bal2':bal2, 'bbl2':bbl2,'dfz':dfz,
    'mid':mid, 'suku':suku, 'datbanding':datbanding,
    'mat':mat,'ratamape':ratamape, 'status':status}
    return render(request, 'app/proses.html', context)

def hapustabel(request):
    if request.method == 'POST':
        Tabel.objects.all().delete()
        Rata.objects.all().delete()
        Defuzzyfikasi.objects.all().delete()
        KelasInt.objects.all().delete()
        Upload.objects.all().delete()
        os.remove('media/data.xlsx')
    return redirect('tabel')
def tabel(request):
    tabel = Tabel.objects.all()
    try:
        df =pd.read_excel('media/data.xlsx',sheet_name=0)
    except:
        return redirect('fileupload')
    status=0
    if request.method == 'POST':
        for m in df.index:
            Tabel.objects.create(
                no=m+1,
                data=df['DTG'][m],
                tanggal=df['DATE'][m]
                )
        return redirect('tabel')
    ratarata=Rata.objects.all()
    jd=len(tabel)
    rt=len(ratarata)
    if jd>0:
        status=1
    if rt>0:
        status=2

    
    context={'tabel':tabel, 'status':status, 'jd':jd,'rata':ratarata}
    return render(request, 'app/tabel.html' ,context)

def chart(request):
    tabel1=Tabel.objects.all()
    tabel2=Tabel.objects.all().values()[1:len(tabel1)]
    df=pd.DataFrame(tabel2)
    label=df.tanggal.tolist()
    dataa=df.data.tolist()
    dataa2=df.peramalan.tolist()
    context={'label':label,'dataa':dataa, 'dataa2':dataa2}
    return render(request, 'app/chart.html' ,context)


