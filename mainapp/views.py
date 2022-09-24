from django.shortcuts import render
import pandas as pd
from django.core.files.storage import FileSystemStorage
import plotly.graph_objects as go
# from django.core.
# Create your views here.

def index(request):
	if request.method == 'POST':
		file = request.FILES['myfile']
		
		df = pd.read_csv(file)
		print(df)
		storage = FileSystemStorage()
		temp_file = storage.save('media/abc.csv', file)
		file_url = storage.url(temp_file)
		fig = go.Figure(data=[go.Candlestick(x=df['DATE'],
                open=df['OPEN'],
                high=df['HIGH'],
                low=df['LOW'],
                close=df['CLOSE'])])

		fig.show()
		return render(request,"index.html")
	return render(request,"index.html")
		


