#!/usr/bin/env python3

import os.path
from mido import MidiFile
from time import sleep
import subprocess
import argparse


def note_to_frequency(note):
    """
    Convert a MIDI note into a frequency (given in Hz)
    """
    return round(440 * 2**((note - 69) / 12))


def frequency_to_key(frequency):
    """
    Convert a frequency (given in Hz) into a key press
    """
    notes = {
        1864: "j",
        1760: "8",
        1568: "5",
        1397: "4",
        1319: "3",
        1175: "2",
        1047: "8",
        988: "7",
        932: "j",
        880: "6",
        831: "h",
        784: "5",
        740: "g",
        698: "4",
        659: "3",
        622: "f",
        587: "2",
        554: "d",
        523: "1",
        494: "t",
        466: "c",
        440: "r",
        415: "x",
        392: "e",
        370: "z",
        349: "w",
        330: "q",
        311: "l",
        294: "0",
        277: "k",
        262: "9",
        247: "s",
        233: ".",
        220: "a",
        208: "m",
        196: "p",
        185: "n",
        175: "o",
        165: "i",
        156: "b",
        147: "u",
        139: "v",
        131: "y",
    }

    return notes.get(frequency,
                     f"\t\t keystroke NOT FOUND, frequency: {frequency}")


def play_midi(filename):
    # Import the MIDI file
    midi_file = MidiFile(filename)
    if midi_file.type == 3:
        print("Unsupported type.")
        exit(3)

    # Wait 3 seconds to switch window
    sleep(3)

    # Play the MIDI file
    for message in midi_file.play():
        if hasattr(message, "velocity"):
            if int(message.velocity) > 0:
                key = frequency_to_key(note_to_frequency(message.note))
                subprocess.run(f'/usr/bin/ydotool type -d 512 {key}', shell=True)


def main():
    parser = argparse.ArgumentParser(prog='BardPlay', description='Play Music as the Bard in FFXIV')
    parser.add_argument('filename', help='Path to the midi file to play')

    args = parser.parse_args()
    if os.path.exists(args.filename):
        play_midi(args.filename)
    else:
        print(f'Invalid file: {args.filename}')


if __name__ == '__main__':
    main()
