from pydub import AudioSegment
from pydub.playback import play

# First, we're loading two audio files
audio = AudioSegment.from_file("audio1.wav")
drum_beat = AudioSegment.from_file("audio2.wav")

# Next, we're making the voice in the audio sound higher-pitched
# We do this by increasing the frame rate of the audio
high_pitched_audio = audio.set_frame_rate(int(audio.frame_rate * 1.5))

# Now, we're making the audio louder
# We do this by increasing the volume of the audio by 10 dB
louder_audio = audio + 10

# Here, we're making the audio repeat 3 times
looped_audio = audio * 3

# In this step, we're combining the audio with a drum beat
# The two sounds will play at the same time
overlapped_audio = audio.overlay(drum_beat, position=0)

# Finally, we're playing each modified audio segment
# You should hear the high-pitched audio, the louder audio, the looped audio, and the overlapped audio
play(high_pitched_audio)
play(louder_audio)
play(looped_audio)
play(overlapped_audio)

