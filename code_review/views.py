import base64
from django.http import HttpResponse
from django.shortcuts import render_to_response
from code_review.models import Review, MyUser
import json

def add_review(request):
    if request.method == "POST":
        author = request.GET['author']
        commit_no = request.GET['commit_no']
        comment = request.GET['comment']
        file_path = request.GET['file_path']
        start_offset = request.GET['start_offset']
        end_offset = request.GET['end_offset']
        review = Review.objects.create(author=author, commit=commit_no,
                              comment=comment, file_path=file_path,
                              start_offset=start_offset, end_offset=end_offset)
        review.save()
    return HttpResponse("")

def all_authors(request):
    users = MyUser.objects.all()
    return render_to_response("all_authors.html", {"users":users})


# def my_login(request):
#     username = request.GET['userName']
#     password = request.GET['password']
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         if user.is_active:
#             login(request, user)
#             response = {"token": request.session.session_key}
#         else:
#             response = {"error": "User is inactive"}
#     else:
#         response = {"error": "Authentification failed"}
#     return HttpResponse(json.dumps(response),
#                         content_type='application/json',
#                         mimetype='application/json')

def my_login(request):
    username = request.GET['userName']
    password = request.GET['password']
    if request.user.username == username:
        response = {"token": request.session.session_key}
    else:
        response = {"error": "Authentification failed"}
    return HttpResponse(json.dumps(response),
                        content_type='application/json',
                        mimetype='application/json')


def to_review(request):
    user = MyUser.objects.get(user=request.user)
    to_review = user.to_review.all()
    response = []
    for review in to_review:
        data = {}
        data["name"]= review.description
        data["permaId"]= {"id":review.perm_id}
        data["author"]= {"userName" : review.author.user.username}
        data["state"]= review.state
        data["createDate"]= review.date.strftime("%Y-%m-%d")
        response.append(data)
    return HttpResponse(json.dumps({"reviewData": response}), mimetype='application/json')