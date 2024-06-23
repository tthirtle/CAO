import npyscreen,help

def show_splash():
    npyscreen.notify_wait(title='',message=help.splash_text)

class exit_button(npyscreen.ButtonPress):
    def __init__(self, screen, when_pressed_function=None, *args, **keywords):
        super().__init__(screen, when_pressed_function, *args, **keywords)
    def whenPressed(self):
        if npyscreen.notify_yes_no(title='Question',message="Really quit?") == True:
		pass
        return super().whenPressed()

class main_menu(npyscreen.FormBaseNew):
    def create(self):
        show_splash()
        self.name = "Main Menu"
	self.is_button = self.add(npyscreen.ButtonPress(name="In Store"))
	self.data = self.add(npyscreen.ButtonPress(name="Edit Database"))
	self.config = self.add(npyscreen.ButtonPress(name="Edit Configuration"))
        return super().create()

class is_menu(npyscreen.FormBaseNew):
	def create(self):
		self.name = "In Store Menu"
		self.oos = "Out Of Stock Items"
		self.label = "Create Labels"
		self.order = "Order Generation"
		return super().create()
