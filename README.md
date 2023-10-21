## English:

# Video-to-Audio Converter

Welcome to the `Video-to-Audio Converter` repository, a solution designed for efficient video-to-audio conversion.

### Features:

- **Convert Local Videos:** Place your videos in the `videos` directory, and the script will convert them into MP3 files.
  
- **Convert YouTube Videos:** Add the YouTube links in the `urls.txt` file, and the script will fetch and convert them into MP3 files.

- **Generate Arrays for Transcription:** Utilize the `FilesToArray.exe` tool to generate arrays prepped for transcription with the `whisper` library in Google Colab.

### How to Use:

1. **For Video Conversion:**
   - Store videos in the `videos` directory or insert YouTube URLs in the `urls.txt`.
   - Execute the `convert-video-to-mp3.py` script.
   - The converted MP3 files will be located in the `videos_in_mp3` directory.

2. **For Array Generation:**
   - Launch `FilesToArray.exe`.
   - Click "Open Folder" and choose the `videos_in_mp3` directory.
   - The generated array will display in red. Click on it to copy it to the clipboard.
   
3. **For Google Colab Transcription:**
   - Open the `google_colab_whisper_transcription.ipynb` file in Google Colab.
   - Run the first cell to install necessary dependencies and import required modules.
   - Execute the second cell to initiate the transcription process. Ensure to update the `files` list with the audio file paths you intend to transcribe.

### Notes:

- `ffmpeg` is required to be installed on the system for the conversion process.

---

## Português:

# Video-to-Audio Converter

Seja bem-vindo ao repositório do `Video-to-Audio Converter`, uma solução desenvolvida para realizar a conversão eficiente de vídeos em áudios.

## Características:

- **Converta Vídeos Locais:** Deposite seus vídeos MP4 no diretório `videos` e o script os transformará em arquivos MP3.
  
- **Converta Vídeos do YouTube:** Adicione os links do YouTube no arquivo `urls.txt`, e o script fará o download e a conversão deles para arquivos MP3.

- **Gere Arrays para Transcrição:** Use o `FilesToArray.exe` para criar arrays prontos para serem transcritos com a biblioteca `whisper` no Google Colab.

## Como Usar:

1. **Para Conversão de Vídeos:**
   - Deposite vídeos no diretório `videos` ou adicione URLs do YouTube em `urls.txt`.
   - Rode o script `convert-video-to-mp3.py`.
   - Os arquivos MP3 convertidos estarão no diretório `videos_in_mp3`.

2. **Para Geração de Arrays:**
   - Execute `FilesToArray.exe`.
   - Clique em "Open Folder" e selecione a pasta `videos_in_mp3`.
   - O array gerado será exibido em vermelho; clique nele para copiar para a área de transferência.
   
3. **Para Transcrição no Google Colab:**
   - Abra o arquivo `google_colab_whisper_transcription.ipynb` no Google Colab.
   - Execute a primeira célula para instalar as dependências necessárias e importar os módulos.
   - Rode a segunda célula para iniciar o processo de transcrição. Lembre-se de atualizar a lista `files` com os caminhos dos áudios que deseja transcrever.

## Observações:

- É necessário ter o `ffmpeg` instalado no sistema para a conversão.

---

**Desenvolvido por [Vitor (LinkedIn)](https://www.linkedin.com/in/vitorgithub/) | [GitHub](https://github.com/vitorgithub).*

**FilesToArray.exe desenvolvido por [Tiago (LinkedIn)](https://www.linkedin.com/in/tiago-antonio-8a5b2420b/). | [GitHub](https://github.com/tiago18555)*
