import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import play

audio = None

def upload_file():
    global audio 
    filename = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav")])
    audio = AudioSegment.from_file(filename)

def modify_audio():
    global audio  
    # Modify the audio based on the user's choices
    if var_high_pitch.get():
        audio = audio.set_frame_rate(int(audio.frame_rate * 1.5))
    if var_louder.get():
        audio = audio + 10
    if var_loop.get():
        audio = audio * 3
    

    # Play the modified audio
    play(audio)

root = tk.Tk()

var_high_pitch = tk.BooleanVar()
var_louder = tk.BooleanVar()
var_loop = tk.BooleanVar()

tk.Button(root, text="Upload Audio File", command=upload_file).pack()
tk.Checkbutton(root, text="Make audio high-pitched", variable=var_high_pitch).pack()
tk.Checkbutton(root, text="Make audio louder", variable=var_louder).pack()
tk.Checkbutton(root, text="Loop audio", variable=var_loop).pack()
tk.Button(root, text="Modify Audio", command=modify_audio).pack()

root.mainloop()

