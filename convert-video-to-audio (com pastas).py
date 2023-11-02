import os
from moviepy.editor import *

def converter_videos_para_mp3():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    input_folder = os.path.join(script_directory, 'videos')

    if not os.path.exists(input_folder):
        raise Exception("A pasta 'videos' não existe no mesmo diretório do script.")

    output_folder = os.path.join(script_directory, 'videos_in_mp3')

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    valid_video_exts = ['.mp4', '.ts', '.mkv']

    for root, dirs, files in os.walk(input_folder):
        for filename in files:
            file_ext = os.path.splitext(filename)[1]

            if file_ext in valid_video_exts:
                file_path = os.path.join(root, filename)
                relative_path = os.path.relpath(file_path, input_folder)
                output_path = os.path.join(output_folder, relative_path)
                output_path = os.path.splitext(output_path)[0] + '.mp3'

                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                print(f"Convertendo {filename} para MP3...")
                audio = AudioFileClip(file_path)
                audio.write_audiofile(output_path, codec='mp3')

    print("\nConversão concluída!")

if __name__ == "__main__":
    try:
        converter_videos_para_mp3()
        print("\nOperação de conversão concluída!")
    except Exception as e:
        print(f"Erro: {e}")