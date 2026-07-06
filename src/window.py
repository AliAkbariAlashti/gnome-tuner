import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Adw, Gtk


class MainWindow(Adw.ApplicationWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title("GNOME Tuner")
        self.set_default_size(400, 300)

        self.set_content(
            Gtk.Box(
                orientation=Gtk.Orientation.VERTICAL,
                spacing=12,
                valign=Gtk.Align.CENTER,
                halign=Gtk.Align.CENTER,
            )
        )

        label = Gtk.Label(label="GNOME Tuner (v0.1)")
        self.get_content().append(label)