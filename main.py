import numpy as np
from scipy.io import wavfile

# TODO: - Some kind of actuation to distinguish contiguous equal notes
#       - Chords..?

# https://www.audiology.org/sites/default/files/ChasinConversionChart.pdf
notes = {
    "C4": 262,
    "D4": 294,
    "E4": 330,
    "F4": 349,
    "G4": 392,
    "A5": 440,
    "B5": 494,
    "C5": 523,
    "D5": 587,
    "E5": 659,
    "F5": 698,
    "G5": 784,
    "A6": 880,
    "B6": 988,
    "C6": 1047
}

# num samples per second
sampling_rate = 44100


def generate_note(note, length):

    # pitch of the note in Hz
    freq = notes[note]

    # length of note in seconds
    duration = .5 * length

    total_samples = np.arange(duration * sampling_rate)
    # https://www.youtube.com/watch?v=lbV2SoeAggU
    waveform = np.sin(2*np.pi*total_samples * freq/sampling_rate) * .3

    return np.int16(waveform * 32767)


wave = np.int16()

with open('mary.txt', 'r') as score:
    for line in score:
        if not line.startswith('#'):
            elems = line.split()

            for elem in elems:
                length = int(elem[0])
                note = elem[1:]

                wave = np.append(wave, generate_note(note, length))

wavfile.write("out.wav", sampling_rate, wave)

# Possible further: interactive keyboard and way to record to txt, replicating tone and timbre of different instruments
