"""
Trevor Murphy
CS 250, Project 3
March 13, 2015
FILE: music.py

Contains the Music class with its appropriate methods
"""
class Music:
    
    def __init__(self, data):
        f = open(data, "r")
        self.numLyst = [int(num) for num in f.read().splitlines()]
        self.notesLyst = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

    def set_beat(self, seconds):
        self.seconds = seconds
    
    def play(self, note, octave, beats):
        lyst = []
        samples = 44100
        midC = 261.62556530 
        
        if octave > 3:
            midC = midC * (2**(octave - 3))
        else:
            midC = midC / (2**(3 - octave))

        n = 3 - self.notesLyst.index(note)
        
        if n > 0:
            freq = midC / ((2**(1/12))**n)
            samplesPerCycle = samples / freq 
        else:
            freq = (midC * ((2**(1/12))**abs(n)))
            samplesPerCycle = samples / freq 

        totalSamples = samples * beats * self.seconds
        
        i = 1
        j = 1
        
        while i < int(samplesPerCycle):
            for items in self.numLyst:
                if i > int(samplesPerCycle):
                    break
                lyst.append(items)
                i += 1
        
        while j < int(totalSamples):
            for items in lyst:
                if j > int(totalSamples):
                    break
                print(items)
                j += 1

    def header(self):
        print("RRAUDIO")
        print("%%")

