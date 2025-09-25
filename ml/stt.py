from openai import OpenAI
client = OpenAI(api_key='')
audio_file= open("output.mp3", "rb")
transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
)

print(transcription.text)