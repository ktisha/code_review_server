# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from code_review.models import Review, User


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
    users = User.objects.all()
    return render_to_response("all_authors.html", {"users":users})