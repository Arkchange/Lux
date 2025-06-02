from google.cloud import texttospeech

text = """
In a box, there were miniature Pokémon from the Eevee evolution family. I had caught several of them, but Flareon refused to be captured.
I saw it walk away in front of me, and I understood that it didn't want to be one of mine.

Then, a Ho-Oh appeared, and by chance, I managed to catch it with a Hyper Ball on the very first try.
A mod came to check the legitimacy of the capture.

After that, I found myself immersed in a Pokémon/Minecraft-like world.
When I entered a cave, it suddenly felt like I was in a horror movie.

The mission: to find the lost adventurer inside the cave.
Luckily, I was able to use Ho-Oh as a flashlight, but fear began to take over me.

It felt like being in Lethal Company, with its endless tunnels and labyrinths.
At one point, while going down a staircase, a wave of terror hit me.

A Weeping Angel—like the ones from Doctor Who—and a zombie appeared.
They didn’t move as long as we looked at them, but we understood we had to run—and the lost person might already be dead.

Panicking, we ran without looking back. Suddenly, a robot from Five Nights at Freddy’s charged at me at full speed—but missed.
Rescue doors were within reach, but my companions got there first and locked them behind them.

Trapped, I died of fear… and then I woke up from the dream.
"""

client = texttospeech.TextToSpeechClient()

input_text = texttospeech.SynthesisInput(text=text)

# Choisir la voix
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    name="en-US-Wavenet-D",  # Voix masculine naturelle
    ssml_gender=texttospeech.SsmlVoiceGender.MALE
)

# Configurer l’audio
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Synthétiser
response = client.synthesize_speech(
    input=input_text,
    voice=voice,
    audio_config=audio_config
)

# Sauvegarder le fichier audio
with open("dream_tiktok_voice.mp3", "wb") as out:
    out.write(response.audio_content)
    print("Audio saved as dream_tiktok_voice.mp3")