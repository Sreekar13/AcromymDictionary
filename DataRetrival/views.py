from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from DataRetrival.models import AC_DICT
import pymysql
# Create your views here.
# from 


def Home(request):
	value=request.POST.get('key')
    #Connection to the SQL database
	conn=pymysql.connect("localhost","Sreekar","<Password>","acronym_dictionary")
	if not value:
		value="wel"
	try:
		print(value)
		crsr=conn.cursor()
		crsr.execute("SELECT full_form from AC_DICT where abbreviation=%s",value)
	except pymysql.Error as err:
		print(err)

	a=""
	context={}
	if crsr:
		for i in crsr:
			a=i[0]
			context={'key_index':a}
	else:
		a="Not a valid acronym. Sorry!"
		context={'key_index':a}
	return render(request, 'DataRetrival/index.html',context)

