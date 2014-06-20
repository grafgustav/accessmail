__author__ = 'grafgustav'
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from .EmailItem import EmailItem

Builder.load_file('GUI/overviewLayout.kv')


# The kivy developers themselves are not happy with the list_view. Since we only need about 10 emails at once
# we can just create an own widget adding it x-10 times to the overview
class OverviewLayout(Screen):

    grid = ObjectProperty()

    def __init__(self, **kwargs):
        super(OverviewLayout, self).__init__(**kwargs)
        self.counter = 0
        if self.grid:
            self.test_data()

    #the kivy properties don't always load properly
    #this method observes the property and trigger on_change
    def on_grid(self, instance, value):
        print("Callback called")
        self.test_data()

    # TODO: limit added emails to 8/10 and store rest somewhere else for later use
    # even better: we always only fetch 8/10 emails from the controller and hand over a counter which indicates
    # all_emails[counter*10:(counter+1)*10]
    # Parameter emails is a list of email objects as defined below, maybe adjust getter if different class is used
    def add_emails(self, emails):
        for v in emails:
            print "email added"
            item = EmailItem(name=v.get_name(), email=v.get_email(), subject=v.get_subject())
            self.grid.add_widget(item)

        # testing routines
        # item1 = EmailItem(name="Max Mustermann", email="max.mustermann@web.de", subject="Your photo")
        # item2 = EmailItem(email="dascha.grib@mail.ru", subject="50 Euro")
        # item3 = EmailItem()
        # self.grid.add_widget(item1)
        # self.grid.add_widget(item2)
        # self.grid.add_widget(item3)

    def test_data(self):
        items = [Email(name="Max Mustermann", email="max.mustermann@web.de", subject="Your photo"),
                 Email(email="dascha.grib@mail.ru", subject="50 Euro"),
                 Email()]
        self.add_emails(items)

    def previous_page(self):
        if self.counter > 0:
            self.counter -= 1
        else:
            self.counter = 0
        print(self.counter)

    def next_page(self):
        self.counter += 1
        print(self.counter)

    # responsible to switch between folders
    def switch_to(self, str):
        print("%s pressed" %str)


class Email(object):

    def __init__(self, name="Unknown", email="Unknown", subject="Unknown"):
        self.name = name
        self.email = email
        self.subject = subject

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_subject(self):
        return self.subject
