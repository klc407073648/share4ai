import os
from googletrans import Translator
import re

def translate_markdown(input_file, output_file):
    translator = Translator()

    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # 提取所有的文本内容
    text_blocks = re.split(r'(\n)', content)

    translated_blocks = []
    for block in text_blocks:
        if block.strip():  # 跳过空行
            try:
                translation = translator.translate(block, src='zh-cn', dest='en').text
                translated_blocks.append(translation)
            except Exception as e:
                print(f"[translate_markdown] Translation error: {e}")
                translated_blocks.append(block)  # 保留原内容
        else:
            translated_blocks.append(block)

    translated_content = ''.join(translated_blocks)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated_content)
    
    print(f"[translate_markdown] Translating {input_file} to {output_file} success.")

def translate_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                input_file = os.path.join(root, file)
                output_file = os.path.join(root, f"translated_{file}")
                print(f"[translate_directory] Translating {input_file} to {output_file}")
                translate_markdown(input_file, output_file)

if __name__ == "__main__":
    directorys = ['D:/code/klc/share4ai/docs/basic/','D:/code/klc/share4ai/docs/resource/']
    for directory in directorys:
        print(f"[main] Translating {directory}")
        translate_directory(directory)