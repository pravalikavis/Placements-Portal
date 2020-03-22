from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests
from django.http import HttpResponseRedirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from placementsportal.models import *
def home(request):
    response_for_students = requests.get('http://www.bhageerathreddy.com/mrnd-hackathon/2018/api/students')
    students = response_for_students.json()
    paginator = Paginator(students["message"], 25)
    page = request.GET.get('page')
    students_per_page = paginator.get_page(page)
    response_for_courses=requests.get('http://www.bhageerathreddy.com/mrnd-hackathon/2018/api/courses')
    courses=response_for_courses.json()
    db_students=Students.objects.all()
    return render(request, 'student_detail.html', {'students':students_per_page ,'courses':courses["message"],'db_students':db_students})
def sync(request,pk):
    marks=[]
    marks_id=[]
    response_for_students = requests.get('http://www.bhageerathreddy.com/mrnd-hackathon/2018/api/students')
    students = response_for_students.json()
    for dict in students["message"]:
        if dict["id"]==pk:
            for dict_marks in dict["top_three_subjects"]:
                marks.append(dict_marks["marks"])
                marks_id.append(dict_marks["course_id"])

            db=Students(stu_id=pk,last_synced=datetime.datetime.now(),name=dict["name"],gender=dict["gender"],college=dict["college"],city=dict["city"],facebook_url=dict["facebook_url"],profile_picture=dict["profile_picture"],dept_id=dict["dept_id"],sub1_id=marks_id[0],sub2_id=marks_id[1],sub3_id=marks_id[2],sub1=marks[0],sub2=marks[1],sub3=marks[2])


            db.save()
    return HttpResponseRedirect('/')
