import requests
import os
import subprocess
import argparse

# Argumentos da linha de comando
parser = argparse.ArgumentParser(description="Baixar segmentos .ts e juntar com ffmpeg.")
parser.add_argument("url", help="URL base do vídeo (sem o número do segmento)")
parser.add_argument("-o", "--output", default="video_final.mp4", help="Nome do arquivo final de saída")
args = parser.parse_args()

# Base URL
base_url = args.url.rstrip('/')  # Remove barra final, se houver

# Diretórios e nomes
segment_dir = "segments"
list_file = "list.txt"
output_file = args.output

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

