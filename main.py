import yt_dlp
import os
import subprocess
from pydub import AudioSegment
import shutil

def download_youtube_audio(youtube_url, output_folder="downloads"):
    os.makedirs(output_folder, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=True)
        title = info['title']
        mp3_path = os.path.join(output_folder, f"{title}.mp3")
        wav_path = mp3_path.replace('.mp3', '.wav')

        sound = AudioSegment.from_mp3(mp3_path)
        sound.export(wav_path, format="wav")

        print(f"[✔] WAV olarak kaydedildi: {wav_path}")
        return wav_path, title

def separate_vocals_with_demucs(wav_file_path, title, output_dir="separated"):
    command = [
        "demucs",
        "--two-stems", "vocals",
        "--out", output_dir,
        wav_file_path
    ]
    subprocess.run(command)

    # Dosya adlarını düzenle
    original_folder = os.path.join(output_dir, "htdemucs", title)
    vocals_path = os.path.join(original_folder, "vocals.wav")
    no_vocals_path = os.path.join(original_folder, "no_vocals.wav")

    new_vocals_name = os.path.join(original_folder, f"{title}_vocals.wav")
    new_no_vocals_name = os.path.join(original_folder, f"{title}_no_vocals.wav")

    if os.path.exists(vocals_path):
        os.rename(vocals_path, new_vocals_name)
    if os.path.exists(no_vocals_path):
        os.rename(no_vocals_path, new_no_vocals_name)

    print(f"[🎤] Ses ayrımı tamamlandı: {new_vocals_name}, {new_no_vocals_name}")

# 🔽 Kullanım örneği
youtube_link = "https://www.youtube.com/watch?v=_NoTqg152B0"
wav_file, title = download_youtube_audio(youtube_link)
separate_vocals_with_demucs(wav_file, title)
