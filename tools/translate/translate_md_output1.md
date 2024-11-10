在 Visual Studio Code (VSCode) 中，目前没有现成的插件可以直接将中文 Markdown 内容转换成英文。不过，你可以通过以下几种方法来实现这一目标：

### 方法一：使用在线翻译工具

1. **复制内容**：将你的中文 Markdown 内容复制到剪贴板。
2. **在线翻译**：使用在线翻译工具，如谷歌翻译（Google Translate）、百度翻译等，将内容翻译成英文。
3. **粘贴回 VSCode**：将翻译后的内容粘贴回 VSCode。

### 方法二：使用 VSCode 插件配合外部翻译服务

虽然没有直接的插件可以完成这一任务，但你可以结合使用一些插件和外部翻译服务来实现自动化翻译。

1. **安装插件**：
   - **Translate**：这是一个可以调用外部翻译服务（如谷歌翻译）的插件。
   - **Markdown Preview Enhanced**：这是一个增强的 Markdown 预览插件，支持多种功能。

2. **安装步骤**：
   - 打开 VSCode。
   - 点击左侧活动栏中的扩展图标（四个方块组成的图标）。
   - 搜索并安装 `Translate` 和 `Markdown Preview Enhanced`。

3. **使用 Translate 插件**：
   - 打开你的 Markdown 文件。
   - 选中需要翻译的中文内容。
   - 使用插件提供的命令进行翻译。通常可以通过右键菜单或命令面板（`Ctrl+Shift+P`）找到翻译命令。

### 方法三：编写脚本自动翻译

如果你熟悉编程，可以编写一个脚本来自动化这个过程。以下是一个使用 Python 和 Google Translate API 的示例：

1. **安装必要的库**：
   ```bash
   pip install googletrans==4.0.0-rc1
   ```

2. **编写脚本**：
   ```python
   from googletrans import Translator
   import re

   def translate_markdown(input_file, output_file):
       translator = Translator()

       with open(input_file, 'r', encoding='utf-8') as file:
           content = file.read()

       # 提取所有的文本内容
       text_blocks = re.findall(r'(?<=\n)(.*?)(?=\n)', content)

       translated_blocks = []
       for block in text_blocks:
           if block.strip():  # 跳过空行
               translation = translator.translate(block, src='zh-cn', dest='en').text
               translated_blocks.append(translation)
           else:
               translated_blocks.append('')

       translated_content = '\n'.join(translated_blocks)

       with open(output_file, 'w', encoding='utf-8') as file:
           file.write(translated_content)

   # 使用示例
   translate_markdown('input.md', 'output.md')
   ```

3. **运行脚本**：
   - 将你的中文 Markdown 文件保存为 `input.md`。
   - 运行脚本，生成的英文内容将保存在 `output.md` 中。

### 方法四：使用 AI 编辑器

一些 AI 编辑器或在线平台（如 DeepL、Grammarly 等）提供了强大的翻译功能，可以将中文内容翻译成英文。你可以将内容复制到这些平台进行翻译，然后再粘贴回 VSCode。

### 总结

虽然 VSCode 没有直接的插件可以将中文 Markdown 内容转换成英文，但通过上述方法，你可以轻松实现这一目标。选择适合你的方法，提高工作效率。希望这些方法对你有帮助！如果有任何问题，请随时告诉我。