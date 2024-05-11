import argparse
from gtts import gTTS
import os

def text_to_speech(text, output_name='output', lang='en', format='mp3', voice=None):
    tts = gTTS(text=text, lang=lang)

    if voice:
        tts.save(f'{output_name}.{format}')
        os.system(f'ffmpeg -i {output_name}.{format} -f mp3 -ab 192000 -ar 44100 {output_name}_voice.mp3')
        os.remove(f'{output_name}.{format}')
        os.system(f'ffmpeg -i {output_name}_voice.mp3 -acodec pcm_u8 -ar 22050 {output_name}.wav')
        os.remove(f'{output_name}_voice.mp3')
    else:
        tts.save(f'{output_name}.{format}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert text to speech.')
    parser.add_argument('text', type=str, help='Text to convert to speech')
    parser.add_argument('--output', type=str, default='output', help='Output file name without extension (default: output)')
    parser.add_argument('--lang', type=str, default='en', help='Language (default: en)')
    parser.add_argument('--format', type=str, default='mp3', help='Output file format (default: mp3)')
    parser.add_argument('--voice', action='store_true', help='Apply voice modification')

    args = parser.parse_args()

    text_to_speech(args.text, args.output, args.lang, args.format, args.voice)
