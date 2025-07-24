import requests
import os
import subprocess
import argparse
import shutil

# Argumentos da linha de comando
parser = argparse.ArgumentParser(description="Baixar segmentos .ts e juntar com ffmpeg.")
parser.add_argument("url", help="URL base do vídeo (sem o número do segmento)")
parser.add_argument("-o", "--output", default="video_final.mp4", help="Nome do arquivo final de saída")
args = parser.parse_args()

# Diretórios e nomes
base_url = args.url.rstrip('/')
segment_dir = "segments"
output_dir = "output"
list_file = "list.txt"
output_file = args.output

# Cria diretórios
os.makedirs(segment_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

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

# Muda para o diretório de segmentos
os.chdir(segment_dir)

# Concatenar com ffmpeg
print("🎞️  Iniciando concatenação com ffmpeg...")
result = subprocess.run([
    "ffmpeg", "-f", "concat", "-safe", "0",
    "-i", list_file, "-c", "copy", output_file
])

# Pós-processamento
if result.returncode == 0:
    print(f"\n✅ Vídeo final criado com sucesso: {output_file}")

    # Move vídeo para pasta output/
    final_path = os.path.join("..", output_dir, output_file)
    shutil.move(output_file, final_path)
    print(f"📂 Vídeo movido para: {final_path}")

    # Limpa arquivos temporários
    print("🧹 Limpando arquivos temporários...")
    os.remove(list_file)
    for f in os.listdir():
        if f.endswith(".ts"):
            os.remove(f)
    print("✅ Limpeza concluída.")
else:
    print("\n❌ Erro ao concatenar os vídeos com ffmpeg.")

