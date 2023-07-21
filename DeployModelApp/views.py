from django.shortcuts import render
from django.http import HttpResponse
import joblib
import numpy as np 



# Create your views here.



def home(request):
  return render(request, 'home.html')


def result(request):
  cls = joblib.load('C:\\Users\\MINISTER JOHN\\Desktop\\Model\\DeployModel\\DecisonTreeModel.pickle')
  lis = []
  lis.append(request.GET['ovulation_day'])
  lis.append(request.GET['length_of_luteal_phase'])

  
  ans = cls.predict([lis])
  integer_ans = np.floor(ans)

  return render(request, 'result.html', {'ans': integer_ans })
