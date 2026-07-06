import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Gtk, Adw

from src.window import MainWindow


class TunerApp(Adw.Application):
    def __init__(self):
        super().__init__(application_id="io.github.gnome_tuner")

    def do_activate(self):
        win = MainWindow(application=self)
        win.present()


def main():
    app = TunerApp()
    app.run()