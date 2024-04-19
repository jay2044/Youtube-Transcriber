import yt_dlp as youtube_dl
from pydub import AudioSegment
import speech_recognition as sr


def download_audio(video_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'outtmpl': 'downloaded_audio.%(ext)s',
        'ffmpeg_location': r'C:\PATH_Programs',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
        return "downloaded_audio.wav"


def convert_audio(file_path):
    sound = AudioSegment.from_file(file_path)
    sound = sound.set_frame_rate(16000)  # Set frame rate to 16000 Hz
    sound.export(file_path, format="wav")


# def transcribe_audio(file_path):
#     recognizer = sr.Recognizer()
#     audio_file = sr.AudioFile(file_path)
#
#     with audio_file as source:
#         audio_data = recognizer.record(source, duration=60)
#
#     try:
#         # Using the default API key (no key needed for basic usage)
#         text = recognizer.recognize_google(audio_data)
#         return text
#     except sr.UnknownValueError:
#         return "Google Speech Recognition could not understand audio"
#     except sr.RequestError as e:
#         return f"Could not request results from Google Speech Recognition service; {e}"

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    audio_file = sr.AudioFile(file_path)
    transcript = ""

    with audio_file as source:
        while True:  # Loop over the audio in chunks
            try:
                audio_data = recognizer.record(source, duration=60)  # Read 4-second chunks
                text = recognizer.recognize_google(audio_data)
                print(text)
                transcript += " " + text
            except sr.WaitTimeoutError:
                break  # Exit the loop when the end of the audio file is reached
            except sr.UnknownValueError:
                transcript += " [unintelligible]"
            except sr.RequestError as e:
                return f"Could not request results from Google Speech Recognition service; {e}"

    return transcript


def main(video_url):
    audio_path = download_audio(video_url)
    convert_audio(audio_path)
    transcript = transcribe_audio(audio_path)
    print(transcript)


if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=GazC3A4OQTE"
    main(video_url)
