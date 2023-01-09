from django.shortcuts import render
from .models import HomePet
from django.shortcuts import render_to_response, RequestContext, redirect
from .forms import TransportationOrderForm

# Create your views here.


def index(request):
    return render(request, 'home_pets/index.html')


def about(request):
    return render(request, 'home_pets/about.html')


def contacts(request):
    return render(request, 'home_pets/contacts.html')


def news(request):
    return render(request, 'home_pets/news.html')


def volunteering(request):
    return render(request, 'home_pets/volunteering.html')


def transportation(request):
    return render(request, 'home_pets/transportation.html')


def benefit(request):
    return render(request, 'home_pets/benefit.html')


def wards(request):
    pets = HomePet.objects.all()
    return render(request, 'home_pets/wards.html',{'pets': pets})


def tohome(request):
    return render(request, 'home_pets/tohome.html')


def temporarily(request):
    return render(request, 'home_pets/temporarily.html')

# def transportation_order(request):
#     return render(request, 'home_pets/transportation_order.html')

 # @login_required
 def transportation_order(request):
    # Get the context from the request.
    # return render(request, 'home_pets/transportation_order.html')
    context = RequestContext(request)

    # A HTTP POST?
    if request.method == 'POST':
        form = TransportationOrderForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            task = form.save(commit=False)
            # task.usern = request.user
            task.save()

             # Redirect to home (/)
            return redirect('/')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print
            form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = TransportationOrderForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('home_pets/transportation_order.html', {'form': form}, context)
def volunteering_help(request):
    return render(request, 'home_pets/volunteering_help.html')


def financial_support(request):
    return render(request, 'home_pets/financial_support.html')


def food_medicines(request):
    return render(request, 'home_pets/food_medicines.html')

