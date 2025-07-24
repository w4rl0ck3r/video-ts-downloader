import requests
import os
import subprocess

# URL base
base_url = "https://vz-4f9a0d3b-3be.b-cdn.net/a58e37e2-bc16-413e-8590-3b5df62385b7/1080p/video"

# Diretórios e nomes
segment_dir = "segments"
list_file = "list.txt"
output_file = "../video_final.mp4"

# Cria diretório
os.makedirs(segment_dir, exist_ok=True)

# Baixar segmentos
index = 0
with open(os.path.join(segment_dir, list_file), "w") as list_f:
    while True:
        ts_url = f"{base_url}{index}.ts"
        filename = f"seg_{index:04}.ts"
        full_path = os.path.join(segment_dir, filename)
        print(f"🔄 Baixando: {ts_url}")

        response = requests.get(ts_url)
        if response.status_code == 200:
            with open(full_path, "wb") as f:
                f.write(response.content)
            list_f.write(f"file '{filename}'\n")
            index += 1
        else:
            print(f"❌ {ts_url} não encontrado (fim da lista).")
            break

print(f"\n✅ Download finalizado. Total de segmentos baixados: {index}")

# Muda para a pasta dos segmentos
os.chdir(segment_dir)

# Concatenar com ffmpeg
print("🎞️  Iniciando concatenação com ffmpeg...")
result = subprocess.run([
    "ffmpeg", "-f", "concat", "-safe", "0",
    "-i", list_file, "-c", "copy", output_file
])

if result.returncode == 0:
    print(f"\n✅ Vídeo final criado com sucesso: {output_file}")
else:
    print("\n❌ Erro ao concatenar os vídeos com ffmpeg.")

