from django.http import HttpResponse
from django.shortcuts import render
import joblib
import pandas as pd

def home(request):
    return  render(request, "home.html")

def result(request):
    svc = joblib.load('finalized_model.sav') 
    lis = []
    lis.append(request.GET["RI"])
    lis.append(request.GET["Na"])
    lis.append(request.GET["Mg"])
    lis.append(request.GET["Al"])
    lis.append(request.GET["Si"])
    lis.append(request.GET["K"])
    lis.append(request.GET["A"])
    lis.append(request.GET["B"])

    data = {'channel1': [0.00034], 'channel2': [-0.00006],'channel3':[-0.00006], 'channel4': [-0.00018], 'channel5': [0.00017],'channel6':[-0.00009],'channel7': [-0.00004], 'channel8': [-0.00017]} 
    test = pd.DataFrame(data)
    test1=pd.DataFrame(lis)
    test['channel1'][0]=test1[0][0]
    test['channel2'][0]=test1[0][1]
    test['channel3'][0]=test1[0][2]
    test['channel4'][0]=test1[0][3]
    test['channel5'][0]=test1[0][4]
    test['channel6'][0]=test1[0][5]
    test['channel7'][0]=test1[0][6]
    test['channel8'][0]=test1[0][7]

    test = test.apply(lambda x : x*1000)

    x=test['channel1'][0]
    min_list=pd.Series(x)
    max_list=pd.Series(x)
    rms_list=pd.Series(x)
    SSI_list=pd.Series(x)
    abs_diffs_signal_list=pd.Series(x)
    ptp_list=pd.Series(x)
    Signal_1 = pd.DataFrame(
    {'min': min_list,
     'max': max_list,
     'rms': rms_list,
     'SSI': SSI_list,
     'abs_diffs_signal':abs_diffs_signal_list,
     'ptp':ptp_list
    })

    x=test['channel2'][0]
    min_list=pd.Series(x)
    max_list=pd.Series(x)
    rms_list=pd.Series(x)
    SSI_list=pd.Series(x)
    abs_diffs_signal_list=pd.Series(x)
    ptp_list=pd.Series(x)

    Signal_2 = pd.DataFrame(
    {'min': min_list,
     'max': max_list,
     'rms': rms_list,
     'SSI': SSI_list,
     'abs_diffs_signal':abs_diffs_signal_list,
     'ptp':ptp_list
    })

    x=test['channel3'][0]
    min_list=pd.Series(x)
    max_list=pd.Series(x)
    rms_list=pd.Series(x)
    SSI_list=pd.Series(x)
    abs_diffs_signal_list=pd.Series(x)
    ptp_list=pd.Series(x)
    Signal_3 = pd.DataFrame(
        {'min': min_list,
        'max': max_list,
        'rms': rms_list,
        'SSI': SSI_list,
        'abs_diffs_signal':abs_diffs_signal_list,
        'ptp':ptp_list
        })

    x=test['channel4'][0]
    min_list=pd.Series(x)
    max_list=pd.Series(x)
    rms_list=pd.Series(x)
    SSI_list=pd.Series(x)
    abs_diffs_signal_list=pd.Series(x)
    ptp_list=pd.Series(x)
    Signal_4 = pd.DataFrame(
        {'min': min_list,
        'max': max_list,
        'rms': rms_list,
        'SSI': SSI_list,
        'abs_diffs_signal':abs_diffs_signal_list,
        'ptp':ptp_list
        })

    x=test['channel5'][0]
    min_list=pd.Series(x)
    max_list=pd.Series(x)
    rms_list=pd.Series(x)
    SSI_list=pd.Series(x)
    abs_diffs_signal_list=pd.Series(x)
    ptp_list=pd.Series(x)
    Signal_5 = pd.DataFrame(
        {'min': min_list,
        'max': max_list,
        'rms': rms_list,
        'SSI': SSI_list,
        'abs_diffs_signal':abs_diffs_signal_list,
        'ptp':ptp_list
        })

    x=test['channel6'][0]
    min_list=pd.Series(x)
    max_list=pd.Series(x)
    rms_list=pd.Series(x)
    SSI_list=pd.Series(x)
    abs_diffs_signal_list=pd.Series(x)
    ptp_list=pd.Series(x)
    Signal_6 = pd.DataFrame(
        {'min': min_list,
        'max': max_list,
        'rms': rms_list,
        'SSI': SSI_list,
        'abs_diffs_signal':abs_diffs_signal_list,
        'ptp':ptp_list
        })

    x=test['channel7'][0]
    min_list=pd.Series(x)
    max_list=pd.Series(x)
    rms_list=pd.Series(x)
    SSI_list=pd.Series(x)
    abs_diffs_signal_list=pd.Series(x)
    ptp_list=pd.Series(x)
    Signal_7 = pd.DataFrame(
        {'min': min_list,
        'max': max_list,
        'rms': rms_list,
        'SSI': SSI_list,
        'abs_diffs_signal':abs_diffs_signal_list,
        'ptp':ptp_list
        })

    x=test['channel8'][0]
    min_list=pd.Series(x)
    max_list=pd.Series(x)
    rms_list=pd.Series(x)
    SSI_list=pd.Series(x)
    abs_diffs_signal_list=pd.Series(x)
    ptp_list=pd.Series(x)
    Signal_8 = pd.DataFrame(
        {'min': min_list,
        'max': max_list,
        'rms': rms_list,
        'SSI': SSI_list,
        'abs_diffs_signal':abs_diffs_signal_list,
        'ptp':ptp_list
        })

    temp1=pd.concat([ Signal_1, Signal_2,Signal_3, Signal_4,Signal_5, Signal_6,Signal_7, Signal_8], keys={ 'channel1' : Signal_1, 'channel2' : Signal_2,'channel3':Signal_3,'channel4':Signal_4,'channel5':Signal_5,'channel6':Signal_6,'channel7':Signal_7,'channel8':Signal_8 },axis=1)
 
    ans = svc.predict(temp1)
    return  render(request, "result.html", {'ans':ans})