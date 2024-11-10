好的，下面是一个完整的 Python 脚本，它可以遍历指定目录下所有的 `.md` 文件，并将它们翻译成英文的 `.md` 文件。我们将使用 `googletrans` 库来进行翻译。

### 步骤

1. **安装必要的库**：
   ```bash
   pip install googletrans==4.0.0-rc1
   ```

2. **编写脚本**：
   ```python
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
                   print(f"Translation error: {e}")
                   translated_blocks.append(block)  # 保留原内容
           else:
               translated_blocks.append(block)

       translated_content = ''.join(translated_blocks)

       with open(output_file, 'w', encoding='utf-8') as file:
           file.write(translated_content)

   def translate_directory(directory):
       for root, dirs, files in os.walk(directory):
           for file in files:
               if file.endswith('.md'):
                   input_file = os.path.join(root, file)
                   output_file = os.path.join(root, f"translated_{file}")
                   print(f"Translating {input_file} to {output_file}")
                   translate_markdown(input_file, output_file)

   if __name__ == "__main__":
       directory = 'path/to/your/directory'  # 替换为你的目录路径
       translate_directory(directory)
   ```

### 说明

1. **`translate_markdown` 函数**：
   - 读取输入文件的内容。
   - 使用正则表达式 `re.split(r'(\n)', content)` 将内容按行分割，保留换行符。
   - 对每一行进行翻译，如果翻译失败，则保留原内容。
   - 将翻译后的内容写入输出文件。

2. **`translate_directory` 函数**：
   - 使用 `os.walk` 遍历指定目录及其子目录。
   - 查找所有以 `.md` 结尾的文件。
   - 调用 `translate_markdown` 函数将每个 `.md` 文件翻译成英文，并保存为 `translated_` 前缀的新文件。

3. **主程序**：
   - 设置要遍历的目录路径。
   - 调用 `translate_directory` 函数开始翻译。

### 运行脚本

1. 将上述脚本保存为 `translate_md.py`。
2. 修改 `directory` 变量的值为你要遍历的目录路径。
3. 在终端或命令提示符中运行脚本：
   ```bash
   python translate_md.py
   ```

### 注意事项

- **API 限制**：Google Translate API 有请求频率限制，如果文件较多或内容较长，可能需要处理请求频率限制。
- **错误处理**：脚本中添加了基本的错误处理，如果翻译失败，会保留原内容并继续处理其他内容。
- **文件名**：翻译后的文件名前会加上 `translated_` 前缀，以避免覆盖原文件。

希望这个脚本能满足你的需求！如果有任何问题或需要进一步的帮助，请随时告诉我。