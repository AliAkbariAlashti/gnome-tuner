import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk


class TunerView(Gtk.Box):
    def __init__(self):
        super().__init__(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=20,
            valign=Gtk.Align.CENTER,
            halign=Gtk.Align.CENTER,
        )

        title = Gtk.Label(label="GNOME Tuner")
        title.add_css_class("title-1")

        note_label = Gtk.Label(label="A4")
        note_label.add_css_class("title-1")

        frequency_label = Gtk.Label(label="440.0 Hz")

        status_label = Gtk.Label(label="Waiting for microphone...")

        meter = Gtk.Scale.new_with_range(
            Gtk.Orientation.HORIZONTAL,
            -50,
            50,
            1,
        )
        meter.set_value(0)
        meter.set_sensitive(False)
        meter.set_size_request(300, -1)

        self.append(title)
        self.append(note_label)
        self.append(frequency_label)
        self.append(meter)
        self.append(status_label)