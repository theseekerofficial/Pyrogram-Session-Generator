# 🔐 Pyrogram Session String Generator

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org)
[![Pyrogram](https://img.shields.io/badge/Pyrogram-Latest-green.svg)](https://pyrogram.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-@MrUnknown114-blue.svg)](https://t.me/MrUnknown114)

> A simple, secure, and user-friendly tool to generate Pyrogram session strings for Telegram bots and userbots.

## 🌟 Features

- **🔒 Secure**: All operations are performed locally with no data stored
- **🚀 Fast**: Quick session generation with minimal setup
- **🛡️ Safe**: Comprehensive error handling and input validation
- **💻 Cross-platform**: Works on Windows, macOS, and Linux
- **🔐 2FA Support**: Full support for Two-Factor Authentication
- **📱 Phone Verification**: Supports international phone numbers
- **⚡ In-memory**: No temporary files or session data left behind

## 🎯 Use Cases

- Creating session strings for Telegram bots
- Setting up userbots for automation
- Managing multiple Telegram accounts programmatically
- Educational purposes for learning Pyrogram

## 📋 Prerequisites

Before running the script, ensure you have:

1. **Python 3.7+** installed on your system
2. **API credentials** from [my.telegram.org](https://my.telegram.org/apps)
3. **Active Telegram account** with phone number access

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/theseekerofficial/Pyrogram-Session-Generator.git
cd Pyrogram-Session-Generator
```

### 2. Install Dependencies

#### Create virtual environment
```bash
python3 -m venv venv
```

#### Activate it
```bash
source venv/bin/activate
```

#### Install requirements
```bash
pip install -r requirements.txt
```

### 3. Get Your API Credentials

1. Visit [my.telegram.org](https://my.telegram.org/apps)
2. Log in with your phone number
3. Create a new application
4. Note down your `API ID` and `API Hash`

### 4. Run the Generator

```bash
python3 pyrogram_session_gen.py
```

## 📖 How It Works

The script follows these steps:

1. **Credential Input**: Prompts for API ID and API Hash
2. **Phone Verification**: Requests your phone number
3. **Code Verification**: Sends and verifies the SMS/Telegram code
4. **2FA Check**: Handles Two-Factor Authentication if enabled
5. **Session Export**: Generates and displays your session string

## 🎮 Usage Example

After running the script, you'll see an interactive prompt:

```
🚀 Pyrogram Session String Generator
============================================================
🔑 Get your API credentials from https://my.telegram.org/apps
============================================================
Enter your API ID: 12345678
Enter your API Hash: abcdef1234567890abcdef1234567890
Enter your phone number (with country code, e.g., +1234567890): +1234567890
📱 Sending verification code...
Enter the verification code: 12345
```

### Using the Generated Session String

```python
from pyrogram import Client

# Replace with your actual session string
session_string = "BQABcd123..."

app = Client(
    "my_account", 
    session_string=session_string
)

@app.on_message()
async def hello(client, message):
    await message.reply("Hello from Pyrogram!")

app.run()
```

## 🔧 Configuration

The script uses these default settings:

- **Client Name**: `session_generator`
- **Memory Mode**: `in_memory=True` (no files created)
- **Connection**: Automatic connect/disconnect handling

## 🛡️ Security Features

### Input Validation
- ✅ API ID format verification
- ✅ Phone number format checking
- ✅ Non-empty input validation

### Error Handling
- 🔍 **ApiIdInvalid**: Invalid API credentials
- 📱 **PhoneNumberInvalid**: Incorrect phone format
- 🔐 **SessionPasswordNeeded**: 2FA detection
- ⏱️ **FloodWait**: Rate limiting protection
- 🚫 **PhoneCodeInvalid**: Wrong verification code

### Privacy Protection
- 🗑️ No session files saved to disk
- 🔒 In-memory processing only
- 🚫 No logging of sensitive data

## 📱 Supported Formats

### Phone Numbers
```
✅ +1234567890
✅ +44123456789
✅ +91987654321
❌ 1234567890 (auto-corrected to +1234567890)
```

### API Credentials
```
✅ API ID: Numeric (8-10 digits)
✅ API Hash: 32-character hexadecimal string
```

## 🚨 Troubleshooting

### Common Issues

**❌ "Invalid API ID"**
- Verify your API ID from my.telegram.org
- Ensure it's a numeric value

**❌ "Invalid phone number"**
- Include country code (e.g., +1 for US)
- Use international format

**❌ "Flood wait"**
- Too many requests; wait before retrying
- The script will show wait time

**❌ "Invalid verification code"**
- Check SMS or Telegram app for code
- Code expires after a few minutes

**❌ "Invalid 2FA password"**
- Enter your cloud password correctly
- Check for typos or caps lock

### Getting Help

If you encounter issues:

1. Check the error message for specific guidance
2. Verify your API credentials are correct
3. Ensure your phone number is accessible
4. Try again after any flood wait periods

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **🐛 Bug Reports**: Open an issue with details
2. **💡 Feature Requests**: Suggest improvements
3. **🔧 Pull Requests**: Submit code improvements
4. **📚 Documentation**: Help improve the README

### Development Setup

```bash
git clone https://github.com/theseekerofficial/Pyrogram-Session-Generator.git
cd Pyrogram-Session-Generator
pip install -r requirements.txt
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

- This tool is for educational and legitimate purposes only
- Keep your session strings private and secure
- Don't share session strings with untrusted parties
- Follow Telegram's Terms of Service
- The author is not responsible for misuse of this tool

## 🙏 Acknowledgments

- **[Pyrogram](https://pyrogram.org)** - Modern Telegram MTProto API framework
- **[Telegram](https://telegram.org)** - For the amazing platform
- **The Community** - For feedback and contributions

## 📞 Support

- **Telegram**: [@MrUnknown114](https://t.me/MrUnknown114)
- **Issues**: [GitHub Issues](https://github.com/theseekerofficial/Pyrogram-Session-Generator/issues)
- **Discussions**: [GitHub Discussions](https://github.com/theseekerofficial/Pyrogram-Session-Generator/discussions)

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

Made with ❤️ by [The Seeker](https://t.me/MrUnknown114)

</div>
