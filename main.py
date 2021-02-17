from os import path
import csv
import speech_recognition as sr
import pyaudio as aud

r = sr.Recognizer()
micro = sr.Microphone()
name = "lines.csv"
row_index = 0

fileExists = path.exists(name)
if fileExists == False:
    with open(name, "w") as fd:
        fd.write("index,line")
else:
    with open(name, "a") as fd:
        with micro as source:
            print("Parle")
            audio_data = r.listen(source)
            print("End")

        result = r.recognize_google(audio_data, language="fr-FR")
        fd.write(result)

def printCSV(name, row_index):
    with open(name, "r") as fd:
        reader = csv.reader(fd)
        for row in reader:
            if row:
                row_index += 1
                colums = [str(row_index), row[0], row[1]]
                return colums

print (printCSV(name, row_index))
