import platform
import os
import socket
import subprocess
import time
import atexit
import shutil

music_path = "/sdcard/Music/song.mp3"

# Check if mpv is installed
if not shutil.which("mpv"):
    print("Install mpv first: https://mpv.io/")
    exit(1)

# Start mpv in background (--no-terminal hides output)
os.system(f"mpv --no-terminal \"{music_path}\" &")
mpv_pid = os.popen(f"pgrep -f 'mpv.*{music_path}'").read().strip()

# Kill mpv when script exits
def stop_music():
    if mpv_pid:
        os.system(f"kill {mpv_pid} 2>/dev/null")

atexit.register(stop_music)

# Your script logic
print("🎵 Music is playing in the background...")
for i in range(5):
    print(f"Working... {i+1}")
    time.sleep(1)

print("✅ Script finished. Music stopped.")
arc = None

print(f' •\x1b[38;5;196m ->\x1b[37m CHECKING FOR UPDATES ')
os.system('git pull --quiet')

def main():
    global arc
    architecture = platform.architecture()
    if architecture[0] == '32bit':
        arc = "32BIT"
        exit(f' •\x1b[38;5;196m ->\x1b[37m 32BIT NOT SUPPORTED')
    elif architecture[0] == '64bit':
        arc = "64BIT"
        print(f' •\x1b[38;5;196m ->\x1b[37m 64BIT DETECTED')
        print(f' •\x1b[38;5;196m ->\x1b[37m STARTING Pemba_Bauw ')
        import data.HARRY64
    else:
        arc = "INVALID"
        exit("•\x1b[38;5;196m ->\x1b[37m UNKNOWN DEVICE TYPE")


if __name__ == "__main__":
    main()