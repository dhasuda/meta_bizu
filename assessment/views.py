from django.shortcuts import render
from assessment.forms import OpinionForm, ItemForm, UserProfileForm, UserForm
from assessment.models import Item, Opinion
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
    return render(request, 'assessment/index.html')

def home(request):
    return render(request, 'assessment/home.html',)

def search(request):
    return render(request, 'assessment/search.html',)

def successful_register(request):
    return render(request, 'assessment/successful_register.html',)


def add_review_itemPage(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)

        name = form['name'].value()
        return add_review_opinionPage(request, name)

    else:
        form = ItemForm()
    return render(request, 'assessment/add_review_itemPage.html', {'form': form})

def add_review_opinionPage(request, name):
    global globalVar
    if name:
        globalVar = name
    itemNameUsed = globalVar

    if request.method == 'POST':
        form = OpinionForm(request.POST)
        if form.is_valid():
            print (itemNameUsed)
            item = Item.objects.get(name=itemNameUsed)
            rank = form['rank'].value()
            description = form['description'].value()
            opinion = Opinion(item=item, rank=rank, description=description)
            opinion.save()
            return successful_register(request)

    context_dict = {}
    context_dict['item_name'] = name

    if not Item.objects.filter(name=name).exists():
        item = Item(name=name)
        item.save()


    form = OpinionForm()
    context_dict['form'] = form
    return render(request, 'assessment/add_review_opinionPage.html', context_dict)



def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

            return index(request)


    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'assessment/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )





def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect("/home")
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'assessment/login.html', {})
