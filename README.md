
# 🎥 Ferramenta de Download de Vídeos via HLS (`.ts`)

Esta ferramenta em Python permite realizar o download automático de vídeos segmentados via HLS (arquivos `.ts`), a partir de uma URL base. Foi desenvolvida com foco na plataforma Beducated.com, mas pode ser adaptada para outros sites que utilizem o mesmo padrão de entrega de vídeo.

---

## 🚀 Funcionalidades

- Baixa vídeos segmentados em `.ts` a partir de uma URL base.
- Detecta automaticamente quando o vídeo termina (via erro 404).
- Salva todos os segmentos em uma pasta local organizada.
- Converte com `ffmpeg` em `.mp4`.

---

## 🛠️ Requisitos

- Python 3.x
- Bibliotecas:
  - `requests` (instale com `pip install requests`)
- [FFmpeg](https://ffmpeg.org/) para unir os arquivos `.ts`

---

## 📦 Instalação

Clone este repositório ou baixe o script diretamente.

```bash
git clone https://github.com/w4rl0ck3r/video-ts-downloader.git
cd /video-ts-downloader
```

Instale as dependências:

```bash
pip install requests
```

▶️ Como Usar
Localize a URL base de um dos arquivos .ts, como:

```bash
https://vz-4f9a0d3b-3be.b-cdn.net/ec8271c3-.../480p/video
```

Execute o script com essa URL como argumento:

```bash
python baixar_ts.py "https://vz-4f9a0d3b-3be.b-cdn.net/ec8271c3-.../480p/video"
```

Os segmentos serão baixados para a pasta segments/.


📁 Estrutura do Projeto

```bash

video-ts-downloader/
├── main.py         # Script principal de download
├── README.md            # Documentação
└── segments/            # Arquivos .ts baixados (gerado automaticamente)
```

🚧 Funcionalidades Futuras (Em Desenvolvimento)

 - [x] 🔄 Concatenação automática dos segmentos com FFmpeg
 - [ ] 📄 Suporte a lista de links via planilha `.csv`
 - [ ] 🧾 Suporte a múltiplos downloads simultâneos
 - [ ] 🖥️ Interface gráfica (GUI) para facilitar o uso
 - [ ] 🧠 Detecção de qualidade e resolução disponíveis (480p, 720p, 1080p)
 - [ ] 📦 Empacotamento como instalador .exe (Windows)
 - [ ] 🔐 Suporte a headers de autenticação (cookies, token, referer)
 - [ ] 🌐 Captura automática do .m3u8 e parsing dinâmico

 

🛡️ Aviso Legal
Esta ferramenta foi desenvolvida com fins educacionais e para uso pessoal. O uso para baixar conteúdos protegidos por direitos autorais sem permissão pode violar os termos de uso da plataforma e leis de propriedade intelectual. O autor não se responsabiliza por usos indevidos.
