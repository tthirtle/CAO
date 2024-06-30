"""Text Based UI using npyscreen based off of ncurses"""
import npyscreen, help, func

def show_splash_screen():
    npyscreen.notify_wait(title="",message=help.splash_msg)
    return

def is_empty(field):
    if field.value == "" or field.value == None:
        return True
    return False

class back_button(npyscreen.ButtonPress):
    """Go back to the previous window"""
    def __init__(self, screen, when_pressed_function=None, *args, **keywords):
        super().__init__(screen, when_pressed_function, *args, **keywords)
        self.name = "Back"
        self.label_width = len(self.name)+2
    def whenPressed(self):
        self.find_parent_app().switchFormPrevious()
        return super().whenPressed()

# Main Menu Options

class exit_button(npyscreen.ButtonPress):
    def __init__(self, screen, when_pressed_function=None, *args, **keywords):
        super().__init__(screen, when_pressed_function, *args, **keywords)
        self.name = "Exit"
        self.label_width = len(self.name)+2
    def whenPressed(self):
        if npyscreen.notify_yes_no(title='Question',message=help.exit_msg) == True:
            self.find_parent_app().setNextForm(None)
            self.find_parent_app().switchFormNow()
        return super().whenPressed()

class in_store_button(npyscreen.ButtonPress):
    def __init__(self, screen, when_pressed_function=None, *args, **keywords):
        super().__init__(screen, when_pressed_function, *args, **keywords)
        self.name = "In-Store"
        self.label_width = len(self.name)+2
    def whenPressed(self):
        return super().whenPressed()
    
class config_button(npyscreen.ButtonPress):
    def __init__(self, screen, when_pressed_function=None, *args, **keywords):
        super().__init__(screen, when_pressed_function, *args, **keywords)
        self.name = "Program Configuration"
        self.label_width = len(self.name)+2
    def whenPressed(self):
        self.find_parent_app().setNextForm('CONFIG')
        self.find_parent_app().switchFormNow()
        return super().whenPressed()

class dbase_button(npyscreen.ButtonPress):
    def __init__(self, screen, when_pressed_function=None, *args, **keywords):
        super().__init__(screen, when_pressed_function, *args, **keywords)
        self.name = "Database Editor"
        self.label_width = len(self.name)+2
    def whenPressed(self):
        return super().whenPressed()

class main_menu(npyscreen.FormBaseNew):
    """Main Menu"""
    def create(self):
        """Run once at startup"""
        show_splash_screen()
        self.name = "Main Menu" #Window Title
        self.help = help.main_menu_help
        self.add(in_store_button) #In Store Menu (Need to first select store)
        self.add(config_button)
        self.add(dbase_button)
        self.add(exit_button)
        return super().create()

class config_form(npyscreen.ActionFormV2):
    """Program Configuration Menu"""
    OK_BUTTON_TEXT = "Save"
    def create(self):
        self.name = "Program Configuration"
        self.help = help.config_help
        self.comp = self.add(npyscreen.TitleText,name="Company Name")
        self.dbase = self.add(npyscreen.TitleFilenameCombo,name = "Database file")
        self.report_dir = self.add(npyscreen.TitleFilenameCombo,name="Report directory",select_dir=True)
        return super().create()
    def pre_edit_loop(self):
        self.comp.value = str(func.get_comp())
        self.dbase.value = str(func.get_dbase())
        self.report_dir.value = str(func.get_report_dir())
        return super().pre_edit_loop()
    def on_cancel(self):
        if npyscreen.notify_yes_no(title="Question",message=help.cancel_msg) == True:
            self.find_parent_app().switchFormPrevious()
        return super().on_cancel()
    def on_ok(self):
        if is_empty(self.comp) or is_empty(self.dbase) or is_empty(self.report_dir):
            npyscreen.notify_confirm(title="ERROR!",message=help.empty_msg)
            return
        func.save_config(self.comp.value,self.dbase.value,self.report_dir.value)
        self.find_parent_app().switchFormPrevious()
        return super().on_ok()
    
class store_form_base(npyscreen.ActionFormV2):
    def create(self):
        self.store_name = self.add(npyscreen.TitleText,name="Name")
        self.num = self.add(npyscreen.TitleText,name="Number")
        self.tel = self.add(npyscreen.TitleText,name="Telephone")
        self.add1 = self.add(npyscreen.TitleText,name="Address")
        self.add2 = self.add(npyscreen.Textfield)
        self.city = self.add(npyscreen.TitleText,name="City")
        self.state = self.add(npyscreen.TitleCombo,name='State',values=func.get_all_states())
        self.zip = self.add(npyscreen.TitleText,name='Zip Code')
        return super().create()

class contact_form_base(npyscreen.ActionFormV2):
    def create(self):
        self.con1 = self.add(npyscreen.TitleFixedText,name='Person 1')
        self.name1 = self.add(npyscreen.TitleText,name='Name')
        self.title1 = self.add(npyscreen.TitleText,name='Title')
        self.con2 = self.add(npyscreen.TitleFixedText,name="Person 2")
        self.name2 = self.add(npyscreen.TitleText,name='Name')
        self.title2 = self.add(npyscreen.TitleText,name='Title')
        self.con3 = self.add(npyscreen.TitleFixedText,name="Person 3")
        self.name3 = self.add(npyscreen.TitleText,name='Name')
        self.title3 = self.add(npyscreen.TitleText,name='Title')
        self.notes = self.add(npyscreen.MultiLineEditableTitle,name='Notes/Comments')
        self.help = help.contact_help
        return super().create()
    def on_ok(self):
        npyscreen.notify_confirm(str(type(self.notes.values)))
        npyscreen.notify_confirm(self.notes.values)
        return super().on_ok()

class app(npyscreen.NPSAppManaged):
    """App class - Main Container"""
    def onStart(self):
        func.load_config()
        """Set forms"""
        # self.addForm('MAIN',main_menu)
        self.addForm('CONFIG',config_form)
        self.addForm('MAIN',contact_form_base)
        return super().onStart()

if __name__ == '__main__':
    a = app()
    a.run()