import os
import sys
import subprocess
import yt_dlp
from pydub import AudioSegment

# 🎯 1. Sanal ortam kurulumu
def ensure_virtualenv():
    if not os.path.exists("venv"):
        print("[🔧] Sanal ortam oluşturuluyor...")
        subprocess.check_call([sys.executable, "-m", "venv", "venv"])
        print("[✔] Sanal ortam oluşturuldu.")

    pip_path = os.path.join("venv", "Scripts" if os.name == "nt" else "bin", "pip")
    print("[📦] Bağımlılıklar kuruluyor...")
    subprocess.check_call([pip_path, "install", "-r", "requirements.txt"])
    print("[✔] Tüm bağımlılıklar yüklendi.")

# 🎯 2. Yeniden sanal ortam içinde çalıştır
def re_run_inside_venv():
    if os.environ.get("VENV_ACTIVE") != "1":
        python_path = os.path.join("venv", "Scripts" if os.name == "nt" else "bin", "python")
        os.environ["VENV_ACTIVE"] = "1"
        subprocess.check_call([python_path, *sys.argv])
        sys.exit()

# 🎯 3. YouTube indir + WAV dönüştür
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

# 🎯 4. Demucs ile vokal ayır
def separate_vocals_with_demucs(wav_file_path, title, output_dir="separated"):
    command = [
        "demucs",
        "--two-stems", "vocals",
        "--out", output_dir,
        wav_file_path
    ]
    subprocess.run(command)

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

# 🚀 5. Ana çalıştırma kısmı
if __name__ == "__main__":
    ensure_virtualenv()
    re_run_inside_venv()

    youtube_link = "https://www.youtube.com/watch?v=_NoTqg152B0"
    wav_file, title = download_youtube_audio(youtube_link)
    separate_vocals_with_demucs(wav_file, title)
