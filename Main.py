from gi.repository import Gtk
# help from http://python-gtk-3-tutorial.readthedocs.org/en/latest/builder.html
#import Gtk.builder

builder = Gtk.Builder()

builder.add_from_file("MainWindow.glade")

MainWindow = builder.get_object("MainWindow")
ToggleServerBtn = builder.get_object("ToggleServerOn")


# check signals->[handler] column  in glade object properties bar
# to determine the function names.
# all handlers take 2 variables.
class Handler():
# define functions here
    def on_MainWindow_destroy(self, *args):
        Gtk.main_quit(*args)
        quit
        return 1
    def on_ToggleServerOn_toggled(self, *args): 
        if ToggleServerBtn.get_active(): #get active is boolean! toggle button
            print("hello World - Pressed Down!")
        else:
            print("Pressed Pressed Up!")
        return 1


#Handler is the class above.
builder.connect_signals(Handler())

#Display window once loaded.
MainWindow.show_all()

Gtk.main()
