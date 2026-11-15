from robot_base import fullbot
from pybricks.tools import wait

class music_base(fullbot):
    def __init__(self):
        super().__init__()
        self.notes = {
            # Octave 0
            'C0': 16.35, 'C#0': 17.32, 'D0': 18.35, 'D#0': 19.45, 'E0': 20.6,
            'F0': 21.83, 'F#0': 23.12, 'G0': 24.5, 'G#0': 25.96, 'A0': 27.5,
            'A#0': 29.14, 'B0': 30.87,

            # Octave 1
            'C1': 32.7, 'C#1': 34.65, 'D1': 36.71, 'D#1': 38.89, 'E1': 41.2,
            'F1': 43.65, 'F#1': 46.25, 'G1': 49, 'G#1': 51.91, 'A1': 55,
            'A#1': 58.27, 'B1': 61.74,

            # Octave 2
            'C2': 65.41, 'C#2': 69.3, 'D2': 73.42, 'D#2': 77.78, 'E2': 82.41,
            'F2': 87.31, 'F#2': 92.5, 'G2': 98, 'G#2': 103.83, 'A2': 110,
            'A#2': 116.54, 'B2': 123.47,

            # Octave 3
            'C3': 130.81, 'C#3': 138.59, 'D3': 146.83, 'D#3': 155.56, 'E3': 164.81,
            'F3': 174.61, 'F#3': 185, 'G3': 196, 'G#3': 207.65, 'A3': 220,
            'A#3': 233.08, 'B3': 246.94,

            # Octave 4
            'C4': 261.63, 'C#4': 277.18, 'D4': 293.66, 'D#4': 311.13, 'E4': 329.63,
            'F4': 349.23, 'F#4': 369.99, 'G4': 392, 'G#4': 415.3, 'A4': 440,
            'A#4': 466.16, 'B4': 493.88,

            # Octave 5
            'C5': 523.25, 'C#5': 554.37, 'D5': 587.33, 'D#5': 622.25, 'E5': 659.25,
            'F5': 698.46, 'F#5': 739.99, 'G5': 783.99, 'G#5': 830.61, 'A5': 880,
            'A#5': 932.33, 'B5': 987.77,

            # Octave 6
            'C6': 1046.5, 'C#6': 1108.73, 'D6': 1174.66, 'D#6': 1244.51, 'E6': 1318.51,
            'F6': 1396.91, 'F#6': 1479.98, 'G6': 1567.98, 'G#6': 1661.22, 'A6': 1760,
            'A#6': 1864.66, 'B6': 1975.53,

            # Octave 7
            'C7': 2093, 'C#7': 2217.46, 'D7': 2349.32, 'D#7': 2489, 'E7': 2637,
            'F7': 2793.83, 'F#7': 2959.96, 'G7': 3135.96, 'G#7': 3322.44, 'A7': 3520,
            'A#7': 3729.31, 'B7': 3951,

            # Octave 8
            'C8': 4186, 'C#8': 4434.92, 'D8': 4698.63, 'D#8': 4978, 'E8': 5274,
            'F8': 5587.65, 'F#8': 5919.91, 'G8': 6271.93, 'G#8': 6644.88, 'A8': 7040,
            'A#8': 7458.62, 'B8': 7902.13,
        }

    def is_rest(self, note):
        return note in (None, 'REST', 'R', '-')

    def play(self, note, duration=200):
        if self.is_rest(note):
            self.time.wait(duration)
        elif note in self.notes:
            self.hub.speaker.beep(round(self.notes[note]), duration)

    async def play_async(self, note, duration=200):
        if self.is_rest(note):
            await wait(duration)
        elif note in self.notes:
            # wait=False starts the beep without blocking, then await wait() yields to the robot!
            self.hub.speaker.beep(round(self.notes[note]), duration)
            await wait(duration)


class song_base(music_base):
    def __init__(self, *notes):
        super().__init__()
        self.song = list(notes)

    def play_song(self, default_duration=200, gap=30):
        for item in self.song:
            if isinstance(item, tuple):
                note, duration = item
            else:
                note, duration = item, default_duration

            self.play(note, duration)

            # Only add a tiny separation gap after actual notes, not after rests
            if not self.is_rest(note) and gap > 0:
                self.time.wait(gap)

    async def play_background(self, default_duration=200, gap=25, loop=True):
        while True:
            for item in self.song:
                if isinstance(item, tuple):
                    note, duration = item
                else:
                    note, duration = item, default_duration

                await self.play_async(note, duration)

                if not self.is_rest(note) and gap > 0:
                    await wait(gap)

            if not loop:
                break

haydn_104_opening = song_base(
    # Grand Adagio Fanfare (D - A - D)
    ('D4', 500), ('R', 100), ('A4', 200), ('D5', 600), ('R', 250),
    ('D4', 500), ('R', 100), ('A4', 200), ('F5', 600), ('R', 350),

    # Allegro Main Theme in D major
    ('D5', 300), ('F#5', 150), ('A5', 150), ('D6', 300), ('B5', 150), ('G5', 150),
    ('F#5', 300), ('E5', 150), ('D5', 150), ('E5', 300), ('R', 150),
    ('E5', 300), ('G5', 150), ('B5', 150), ('E6', 300), ('C#6', 150), ('A5', 150),
    ('G5', 300), ('F#5', 150), ('E5', 150), ('D5', 450)
)

haydn_104_finale = song_base(
    # Bar 1-2: D5 - F#5 - A5 - F#5 | D5 - B4 - A4
    ('D5', 220), ('F#5', 220), ('A5', 330), ('F#5', 110),
    ('D5', 220), ('B4', 220), ('A4', 330), ('R', 110),

    # Bar 3-4: D5 - F#5 - A5 - F#5 | E5 - C#5 - D5
    ('D5', 220), ('F#5', 220), ('A5', 330), ('F#5', 110),
    ('E5', 220), ('C#5', 220), ('D5', 330), ('R', 110),

    # Bar 5-6: A5 - F#5 - G5 - E5 | F#5 - D5 - E5 - C#5
    ('A5', 220), ('F#5', 220), ('G5', 220), ('E5', 220),
    ('F#5', 220), ('D5', 220), ('E5', 220), ('C#5', 220),

    # Bar 7-8: D5 - B4 - A4 - G4 | F#4 - E4 - D4
    ('D5', 220), ('B4', 220), ('A4', 220), ('G4', 220),
    ('F#4', 220), ('E4', 220), ('D4', 440)
)

rick_roll = song_base(
    # "Never gonna give you up"
    ('C5', 140), ('D5', 140), ('F5', 140), ('D5', 140),
    ('A5', 380), ('A5', 380), ('G5', 600), ('R', 120),

    # "Never gonna let you down"
    ('C5', 140), ('D5', 140), ('F5', 140), ('D5', 140),
    ('G5', 380), ('G5', 380), ('F5', 380), ('E5', 140), ('D5', 350), ('R', 120),

    # "Never gonna run around and desert you"
    ('C5', 140), ('D5', 140), ('F5', 140), ('D5', 140),
    ('F5', 450), ('G5', 260), ('E5', 350), ('D5', 140), ('C5', 450),
    ('C5', 260), ('G5', 450), ('F5', 700), ('R', 200)
)

final_countdown = song_base(
    # Phrase 1: B5 - A5 - B5 - E5
    ('B5', 130), ('A5', 130), ('B5', 450), ('E5', 450), ('R', 250),

    # Phrase 2: C6 - B5 - C6 - B5 - A5
    ('C6', 130), ('B5', 130), ('C6', 250), ('B5', 250), ('A5', 500), ('R', 250),

    # Phrase 3: C6 - B5 - C6 - E5
    ('C6', 130), ('B5', 130), ('C6', 450), ('E5', 450), ('R', 250),

    # Phrase 4: A5 - G5 - A5 - G5 - F#5 - A5 - G5
    ('A5', 130), ('G5', 130), ('A5', 250), ('G5', 250), ('F#5', 250), ('A5', 250),
    ('G5', 600), ('R', 150),

    # Final Cadence: F#5 - G5 - A5 - G5 - A5 - B5 - A5 - G5 - F#5 - E5 - C6 - B5
    ('F#5', 140), ('G5', 140), ('A5', 420), ('G5', 140), ('A5', 140),
    ('B5', 260), ('A5', 260), ('G5', 260), ('F#5', 260),
    ('E5', 450), ('C6', 450), ('B5', 800), ('R', 250)
)

ants_go_marching = song_base(
    # "The ants go marching one by one, hurrah, hurrah"
    ('A4', 150), ('D5', 300), ('D5', 150), ('D5', 300), ('E5', 150),
    ('F5', 300), ('E5', 150), ('F5', 300), ('D5', 150),
    ('E5', 450), ('C5', 450),
    ('D5', 600), ('R', 150), ('A4', 150),

    # "The ants go marching one by one, hurrah, hurrah"
    ('D5', 300), ('D5', 150), ('D5', 300), ('E5', 150),
    ('F5', 300), ('E5', 150), ('F5', 300), ('D5', 150),
    ('E5', 450), ('C5', 450),
    ('D5', 750), ('R', 150),

    # "The ants go marching one by one, the little one stops to suck his thumb"
    ('F5', 300), ('F5', 150), ('F5', 300), ('G5', 150),
    ('A5', 300), ('A5', 150), ('A5', 450),
    ('G5', 150), ('F5', 300), ('E5', 150), ('F5', 300), ('G5', 150),
    ('A5', 450), ('F5', 300), ('D5', 150),

    # "And they all go marching down to the ground, to get out of the rain"
    ('D5', 150), ('F5', 150), ('A5', 300), ('A5', 150), ('G5', 150), ('F5', 150),
    ('E5', 300), ('C5', 150), ('E5', 300), ('G5', 150),
    ('F5', 300), ('D5', 150), ('E5', 300), ('C5', 150),
    ('D5', 600), ('R', 150),

    # "BOOM! BOOM! BOOM!" (Octave 5 staccato hits so the speaker projects them clearly)
    ('D5', 180), ('R', 120), ('D5', 180), ('R', 120), ('D5', 360), ('R', 300)
)