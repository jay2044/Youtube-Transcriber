# YouTube Audio Transcriber

This project allows you to download audio from YouTube videos, convert it for optimal speech recognition, and transcribe it using Google's Speech Recognition service.

## Requirements

- Python 3.x
- `yt_dlp` for downloading audio from YouTube.
- `pydub` for audio manipulation.
- `speech_recognition` for converting speech to text.

## Setup

1. **Install Required Libraries**

   ```bash
   pip install yt-dlp pydub speechrecognition
   ```

2. Ensure FFmpeg is installed and its path is correctly set in the script:
   ```python
   'ffmpeg_location': r'C:\YOUR_PATH'

## Usage

1. Run the script with a YouTube video URL to download the audio, convert and transcribe it:

   ```python
   python main.py
   ```

   Replace `your_script_name.py` with the name of your Python script.

2. Modify the `video_url` in the script or adapt the `main` function to accept URLs as arguments for dynamic usage.

## Function Descriptions

- `download_audio(video_url)`: Downloads the best audio stream available from the provided YouTube URL and saves it as a WAV file.

- `convert_audio(file_path)`: Converts the audio file to a format suitable for speech recognition (16000 Hz, mono).

- `transcribe_audio(file_path)`: Transcribes the audio file using Google's Speech Recognition API, handling exceptions and chunking audio if necessary for long files.

## Notes

- The script currently handles errors such as unrecognizable speech and API request failures.
- Ensure you have the necessary permissions to use audio content from YouTube videos.

## Contributing

Contributions to the project are welcome. Please ensure you follow the existing coding style and add comments where necessary.


### Additional Notes
- **Modification for Dynamic Input**: You might want to modify the `main` function to accept command-line arguments for the YouTube URL, which would make the script more flexible for different users or use cases.
- **Error Handling**: The script includes basic error handling, but you could expand this as needed, especially if you plan to handle a wide range of exceptions or add more complex logging.
- **Performance Considerations**: If the script is intended for use with very long videos or high volumes of requests, consider adding more robust performance handling features, like rate limiting or asynchronous processing.