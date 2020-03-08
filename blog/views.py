from django.shortcuts import render, redirect, get_object_or_404
from blog.models import BlogPost, Comment
# Create your views here.
from blog.forms import CreateBlogPostForm, UpdateBlogPostForm, CommentForm
from account.models import Account 
from django.db.models import Q
from django.http import HttpResponse

def create_blog_view(request):

	context ={}
	user = request.user
	if not user.is_authenticated:
		return redirect('must_authenticate')

	if not user.is_admin:
		return redirect("unauthorized")	

	form = 	CreateBlogPostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		author = Account.objects.filter(email=user.email).first()
		obj.author = author
		obj.save()
		form = CreateBlogPostForm()

	context['form'] = form	

	return render(request,"blog/create_blog.html",context)


def detail_blog_view(request, slug):
	context = {}

	blog_post = get_object_or_404(BlogPost, slug=slug)
	comments = blog_post.comments.filter(active=True, parent__isnull=True)
	if request.POST:
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			parent_object = None
			try:
				parent_id = int(request.POST.get('parent_id'))
			except:
				parent_id = None
			if parent_id:
				parent_object = Comment.objects.get(id=parent_id)
				if parent_object:
					reply_comment = comment_form.save(commit=False)
					reply_comment.parent = parent_object
			new_comment = comment_form.save(commit=False)
			new_comment.post = blog_post
			new_comment.save()
			return redirect('blog:detail',slug)			
	else:
		comment_form = CommentForm()

	context['blog_post'] = blog_post
	context['comments'] = comments
	context['comment_form'] = comment_form

	return render(request, 'blog/detail_blog.html',context)	


def edit_blog_view(request, slug):
	context={}

	user = request.user
	if not user.is_authenticated:
		return redirect("must_authenticate")

	blog_post = get_object_or_404(BlogPost, slug=slug) 

	if blog_post.author != user:
		return redirect("unauthorized")


	if request.POST:
		form = UpdateBlogPostForm(request.POST or None, request.FILES or None,instance=blog_post)
		if form.is_valid():
			obj = form.save(commit=False) # load parameters into form, giving access to cleaned data
			obj.save()
			context['success_message'] = "Post successfully updated"
			blog_post = obj

	form = UpdateBlogPostForm(
			initial = {
				"title": blog_post.title,
				"body": blog_post.body,
				"image": blog_post.image,
			}
		)
	context['form'] = form
	return render(request,'blog/edit_blog.html',context)		


def get_blog_queryset(query=None):
	queryset = []
	queries = query.split(" ") # split string of characters into individual words
	for q in queries:
		posts = BlogPost.objects.filter(
				Q(title__icontains=q) | # Q lookup, icontains removes capitalization
				Q(body__icontains=q)
			).distinct()

		for post in posts:
			queryset.append(post)
	return list(set(queryset)) # set - unique elements, list to send as return value to template
			


