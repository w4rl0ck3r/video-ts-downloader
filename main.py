import requests
import os

# URL base — onde os arquivos estão
base_url = "https://vz-4f9a0d3b-3be.b-cdn.net/ec8271c3-4d54-4c5a-9f70-2ac913b7364d/480p/video"

# Pasta para salvar os arquivos
os.makedirs("segments", exist_ok=True)

# Número inicial do segmento
index = 0

while True:
    ts_url = f"{base_url}{index}.ts"
    filename = f"segments/seg_{index:04}.ts"
    print(f"🔄 Baixando: {ts_url}")

    response = requests.get(ts_url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        index += 1
    else:
        print(f"❌ {ts_url} não encontrado (fim da lista).")
        break

print(f"\n✅ Download finalizado. Total de segmentos baixados: {index}")

