
# Installing Ollama on a Student Machine
A step-by-step guide for Windows, macOS, and Linux.

---

## 1. What Is Ollama?
Ollama lets you download and run Large Language Models (LLMs) locally with no cloud GPU.  
It works offline once models are installed.

---

## 2. System Requirements
### Minimum Requirements
- **8 GB RAM** (16 GB recommended)
- **Windows 10/11**, **macOS 11+**, or a compatible **Linux** distribution
- **3–10 GB free storage**
- GPU optional

---

# 3. Installation Instructions

---

## macOS
### Install with Homebrew (recommended)
```bash
brew install ollama
```

### Start the service
```bash
ollama serve
```

### Check installation
```bash
ollama --version
```

---

## Windows
### Option 1: Installer
1. Download from: https://ollama.com/download/windows  
2. Run the installer  
3. Open PowerShell and verify:
```powershell
ollama --version
```

### Option 2: Winget
```powershell
winget install Ollama.Ollama
```

---

## Linux
### Install (Official Script)
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Start service
```bash
ollama serve
```

---

# 4. Running Your First Model
### Example: Llama 3
```bash
ollama run llama3
```

Use a smaller model if needed:
```bash
ollama run phi3
```

---

# 5. Managing Models
### List installed models
```bash
ollama list
```

### Download a model
```bash
ollama pull mistral
```

### Delete a model
```bash
ollama rm mistral
```

---

# 6. Using Ollama with VS Code
1. Install the “Continue” extension  
2. Start Ollama:
```bash
ollama serve
```
3. Point Continue to `http://localhost:11434`

---

# 7. Troubleshooting

### “Command not found”
- Restart your terminal  
- Reinstall Ollama  

### Low RAM issues
Use small models (e.g., **phi3**, **llama3:8b**)

### Linux service won’t start
```bash
systemctl restart ollama
```

---

# 8. Uninstalling Ollama

### macOS
```bash
brew uninstall ollama
```

### Windows
```powershell
winget uninstall Ollama.Ollama
```

### Linux
```bash
sudo rm -rf /usr/local/bin/ollama ~/.ollama
```

---

# 9. Useful Links
- Website: https://ollama.com  
- Model Library: https://ollama.com/library  
- GitHub: https://github.com/ollama/ollama  
