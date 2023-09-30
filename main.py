from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from camera4kivy import Preview



class Mybox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.preview = Preview()
        self.preview.connect_camera(enable_analyze_pixels = True)
        self.add_widget(self.preview)
# Replace this with your
# current version


# Defining a class
class MyFirstKivyApp(App):
	# Function that returns
	# the root widget
	def build(self):
		
		# Label with text Hello World is
		# returned as root widget
		return Mybox()


# Here our class is initialized
# and its run() method is called.
# This initializes and starts
# our Kivy application.
MyFirstKivyApp().run()			
