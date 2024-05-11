<h1 align="center"><b><br>Google Text-to-Speech<b></h1>
 
**Introduction:**
GTTS (Google Text-to-Speech) is a Python library and CLI tool that uses Google Text-to-Speech API to convert text to speech. It allows users to generate speech files directly from text strings or text files.

**Features:**
- **Simple Interface:** GTTS provides a straightforward interface for converting text to speech, making it easy to use for both beginners and advanced users.
 - **Multiple Languages:** It supports multiple languages and accents, allowing users to generate speech in their preferred language.
  - **Flexible Output:** Users can choose to output the speech as audio files in various formats including mp3, wav, and ogg.
  - **Command Line Interface:** GTTS comes with a command line interface, enabling users to convert text to speech directly from the terminal.

 - **Installation:**
To install GTTS, simply use pip:
```bash
pip install gtts
```

**Usage:**
Here's a simple example of using GTTS in Python:
```python
from gtts import gTTS

text = "Hello, welcome to GTTS!"
tts = gTTS(text=text, lang='en')
tts.save("hello.mp3")
```
This code will generate an audio file named "hello.mp3" with the text "Hello, welcome to GTTS!" spoken in English.

**CLI Usage:**
GTTS can also be used from the command line:
```bash
gtts-cli "Hello, welcome to GTTS!" --lang en --output hello.mp3
```
This command will generate the same audio file as the Python example.

**Documentation:**
For more detailed usage instructions and examples, refer to the [official documentation](https://gtts.readthedocs.io/en/latest/).

**Contribution:**
Contributions to GTTS are welcome! Feel free to open issues or submit pull requests on [GitHub]([https://github.com/Blane187/GTTS](https://github.com/Blane187/GTTS/pulls)).

**License:**
GTTS is licensed under the MIT License. See the [LICENSE](https://github.com/Blane187/GTTS/blob/master/LICENSE) file for details.

**Acknowledgements:**
GTTS is developed and maintained by Blane187. Special thanks to Google for providing the Text-to-Speech API.

**Support:**
For any questions, bug reports, or feature requests, please open an issue on [GitHub](https://github.com/Blane187/GTTS/issues).
