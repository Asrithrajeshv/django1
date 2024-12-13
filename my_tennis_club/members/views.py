from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())


def testing(request):
  mydata = Member.objects.filter(lastname='Refsnes', id=2).values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
# Create your views here.

def greeting_view(request):
    def determine_greeting():
        # Logic to decide the greeting type
        # Example: Return 1 for "Hello", 2 for "Welcome", or default to 3
        import datetime
        current_hour = datetime.datetime.now().hour
        if current_hour < 12:
            return 1  # Morning: "Hello"
        elif current_hour < 18:
            return 2  # Afternoon: "Welcome"
        else:
            return 3  # Evening/Night: "Goodbye"

    greeting_value = determine_greeting()  # Call the function
    template = loader.get_template('greeting_template.html')  # Load template
    context = {
        'greeting': greeting_value,  # Pass the greeting value to the template
    }
    return HttpResponse(template.render(context, request))