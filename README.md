# English:

## Video-to-Audio Converter

Welcome to the `Video-to-Audio Converter` repository, a solution developed to efficiently convert videos into audios.

## Features:

- **Convert Local Videos:** Deposit your videos in the `videos` directory, and the program will transform them into MP3 files.

- **Convert YouTube Videos:** Add YouTube links to the `urls.txt` file, and the script will download and convert them into MP3 files.

- **Generate Arrays for Transcription:** Use the `FilesToArray.exe` tool to create arrays ready for transcription using the `whisper` library on Google Colab.

## Initial Setup:

1. Download Python from [Python Downloads](https://www.python.org/downloads/).

2. During the Python installation, check the following options:
   - [x] Use admin privileges when installing py.exe 
   - [x] Add python.exe to PATH

3. Clone the repository: [https://github.com/vitorgithub/audio-processing-suite](https://github.com/vitorgithub/audio-processing-suite).

4. Access the `ffmpeg` and `FilesToArray` folders and follow the instructions in the txt file.

## Google Colab Initial Setup:

1. Visit the [Google Colab](https://colab.research.google.com/) website and select "New Notebook".

2. Click the "File" button in the upper left corner -> Open notebook -> Upload -> Select the `google-colab-whisper_transcription.ipynb` file from the repository.

## Step by Step on How to Transcribe Videos:

1. Download the videos.

2. Place the videos in the "videos" folder.

3. Access the "initial installations (prerequisites)" folder within the repository and follow the instructions.

4. Run the `convert-video-to-mp3.exe` file.

5. Access Google Colab -> Click on "files" on the left side of the website -> Drag all .mp3 files into the `sample_data` folder.

6. Go back to the local repository you cloned from GitHub -> Run the `FilesToArray.exe` file -> Click "Open Folder" -> Select the `videos_in_mp3` folder -> Click on the text.

7. Go back to Google Colab and replace the content in your CTRL C with what's in the location of `files = [ "./sample_data/...]`.

8. Select "Runtime" -> "Restart and run all".

## Notes:

- It's necessary to have `ffmpeg` installed on your system for conversion.

---

# Português:

## Video-to-Audio Converter

Seja bem-vindo ao repositório do `Video-to-Audio Converter`, uma solução desenvolvida para realizar a conversão eficiente de vídeos em áudios.

## Características:

- **Converta Vídeos Locais:** Deposite seus vídeos no diretório `videos`, e o programa os transformará em arquivos MP3.
  
- **Converta Vídeos do YouTube:** Adicione os links do YouTube no arquivo `urls.txt`, e o script fará o download e a conversão deles para arquivos MP3.

- **Gere Arrays para Transcrição:** Use o `FilesToArray.exe` para criar arrays prontos para serem transcritos com a biblioteca `whisper` no Google Colab.

## Configuração Inicial:

1. Baixar Python no site [Python Downloads](https://www.python.org/downloads/).
   
2. No instalador do Python, marque as opções:
   - [x] Use admin privileges when installing py.exe 
   - [x] Add python.exe to PATH

3. Faça um git clone do repositório: [https://github.com/vitorgithub/audio-processing-suite](https://github.com/vitorgithub/audio-processing-suite).

4. Acesse as pastas `ffmpeg` e `FilesToArray` e siga as instruções do arquivo txt.

## Configuração Inicial do Google Colab:

1. Acesse o site [Google Colab](https://colab.research.google.com/) e selecione "New Notebook".

2. Clique no botão "Arquivo" no canto superior esquerdo -> Abrir notebook -> Upload -> Selecione o arquivo `google-colab-whisper_transcription.ipynb` que está no repositório.

## Passo a Passo de Como Transcrever os Vídeos:

1. Realize o download dos vídeos.

2. Insira os vídeos na pasta "videos".

3. Acesse a pasta "instalações iniciais (pré-requisitos)" dentro do repositório e siga as instruções.

4. Execute o arquivo `convert-video-to-mp3.exe`.

5. Acesse o Google Colab -> Clique em "arquivos" no lado esquerdo do site -> Arraste todos os arquivos .mp3 dentro da pasta `sample_data`.

6. Volte ao repositório local que você clonou do GitHub -> Execute o arquivo `FilesToArray.exe` -> Clique em "Open Folder" -> Selecione a pasta `videos_in_mp3` -> Clique no texto.

7. Retorne ao Google Colab e substitua o conteúdo do seu CTRL C pelo que está no local de `files = [ "./sample_data/...]`.

8. Selecione "Ambiente de execução" -> "Reiniciar e executar tudo".

## Observações:

- É necessário ter o `ffmpeg` instalado no sistema para a conversão.


---

**Desenvolvido por [Vitor (LinkedIn)](https://www.linkedin.com/in/vitorgithub/) | [GitHub](https://github.com/vitorgithub).*

**FilesToArray.exe desenvolvido por [Tiago (LinkedIn)](https://www.linkedin.com/in/tiago-antonio-8a5b2420b/). | [GitHub](https://github.com/tiago18555)*
