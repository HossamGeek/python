import webbrowser
from random import choice

def random_func():

	random_page_generator = ['http://www.google.com',
                         'http://www.youtube.com']
	webbrowser.open(choice(random_page_generator), new=2)

random_func()
