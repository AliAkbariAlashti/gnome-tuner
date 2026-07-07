import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk, GLib

from src.services.fake_tuner import FakeTuner


def create_tuner():
    """Prefer the real microphone tuner, fall back to the simulated one."""
    try:
        from src.services.mic_tuner import MicTuner

        return MicTuner()
    except Exception as error:
        print(f"Microphone unavailable ({error}); using simulated tuner")
        return FakeTuner()


class TunerView(Gtk.Box):
    def __init__(self):
        super().__init__(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=20,
            valign=Gtk.Align.CENTER,
            halign=Gtk.Align.CENTER,
        )

        self.tuner = create_tuner()

        title = Gtk.Label(label="GNOME Tuner")
        title.add_css_class("title-1")

        self.note_label = Gtk.Label(label="--")
        self.note_label.add_css_class("title-1")

        self.frequency_label = Gtk.Label(label="--- Hz")

        self.status_label = Gtk.Label(label="Starting...")

        self.meter = Gtk.Scale.new_with_range(
            Gtk.Orientation.HORIZONTAL,
            -50,
            50,
            1,
        )
        self.meter.set_size_request(300, -1)

        self.append(title)
        self.append(self.note_label)
        self.append(self.frequency_label)
        self.append(self.meter)
        self.append(self.status_label)

        GLib.timeout_add(300, self.update_tuner)

    def update_tuner(self):
        data = self.tuner.get_reading()

        if data is None:
            self.note_label.set_label("--")
            self.frequency_label.set_label("--- Hz")
            self.meter.set_value(0)
            self.status_label.set_label("Listening...")
            return True

        self.note_label.set_label(data["note"])

        self.frequency_label.set_label(
            f'{data["frequency"]:.1f} Hz'
        )

        self.meter.set_value(data["cents"])

        cents = data["cents"]

        if abs(cents) <= 3:
            status = "In Tune"
        elif cents < 0:
            status = "Flat"
        else:
            status = "Sharp"

        self.status_label.set_label(status)

        return True