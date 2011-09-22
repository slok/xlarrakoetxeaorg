from django import forms
from haystack.forms import SearchForm
from django.contrib.auth.models import User

def _admin_users_in_choices():
    """
        gets all the admin users from auth_user
    """
    #We need to catch and pass this error because auth_user table isn't created before this and fails when it checks,
    #the exception thrwon is: "django.db.utils.DatabaseError: no such table: auth_user"
    try:
        raw_users = User.objects.all()
        users = [('', '')]
        for i in raw_users:
            full_name = i.username
            users.append((full_name, full_name))
            
    except django.db.utils.DatabaseError:
        pass
        
    return users


class EntrySearchForm(SearchForm):
    
    author = forms.ChoiceField( choices = _admin_users_in_choices(), 
                            widget=forms.Select(),
                            required=False)
    #BUG WITH TWO DATES IN WHOOSH, USE ONE INSTEAD
    start_date = forms.DateField(required=False)
    #end_date = forms.DateField(required=False)

    def search(self):
        
        # First, store the SearchQuerySet received from other processing.
        sqs = super(EntrySearchForm, self).search()

        if self.is_valid():  
            # Check to see if a start_date was chosen.
            if self.cleaned_data['author']:
                sqs = sqs.filter(author=self.cleaned_data['author'])
            
            # Check to see if a start_date was chosen.
            if self.cleaned_data['start_date']:
                sqs = sqs.filter(pub_date__gte=self.cleaned_data['start_date'])

            # Check to see if an end_date was chosen.
            #if self.cleaned_data['end_date']:
            #    sqs = sqs.filter(pub_date__lte=self.cleaned_data['end_date'])

        return sqs
