import requests
import os
import subprocess
import argparse
import shutil

# Set args
parser = argparse.ArgumentParser(description="Download all segments .ts and join ffmpeg.")
parser.add_argument("url", help="Base URL vídeo (without segment index)")
parser.add_argument("-o", "--output", default="output.mp4", help="Name of output file")
args = parser.parse_args()

# Dir names
base_url = args.url.rstrip('/')
segment_dir = "segments"
output_dir = "output"
list_file = "list.txt"
output_file = args.output

# Make dirs
os.makedirs(segment_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

# Download segments
index = 0
with open(os.path.join(segment_dir, list_file), "w") as list_f:
    while True:
        ts_url = f"{base_url}{index}.ts"
        filename = f"seg_{index:04}.ts"
        full_path = os.path.join(segment_dir, filename)
        print(f"🔄 Downloading: {ts_url}")

        response = requests.get(ts_url)
        if response.status_code == 200:
            with open(full_path, "wb") as f:
                f.write(response.content)
            list_f.write(f"file '{filename}'\n")
            index += 1
        else:
            print(f"❌ {ts_url} not found (end of list).")
            break

print(f"\n✅ Download complete. Total of segments: {index}")

# Change to segment_dir
os.chdir(segment_dir)

# Concat ffmpeg
print("🎞️  Starting concatenation with ffmpeg...")
result = subprocess.run([
    "ffmpeg", "-f", "concat", "-safe", "0",
    "-i", list_file, "-c", "copy", output_file
])


if result.returncode == 0:
    print(f"\n✅ Concatenation succeeded: {output_file}")

    # Move video to output/
    final_path = os.path.join("..", output_dir, output_file)
    shutil.move(output_file, final_path)
    print(f"📂 Video moved to: {final_path}")

    # Delete temp files
    print("🧹 Deleting temp files...")
    os.remove(list_file)
    for f in os.listdir():
        if f.endswith(".ts"):
            os.remove(f)
    print("✅ All clear.")
else:
    print("\n❌ Error ffmpeg.")

