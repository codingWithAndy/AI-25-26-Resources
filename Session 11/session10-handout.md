# Installing Ollama on a Student Machine

A step-by-step guide for Windows, macOS, and Linux.

------------------------------------------------------------------------

## 1. What Is Ollama?

Ollama is a tool that allows you to download and run Large Language
Models (LLMs) locally on your computer.\
It requires no cloud GPU and works offline once models are installed.

------------------------------------------------------------------------

## 2. System Requirements

### Minimum Requirements

-   **8 GB RAM** (16 GB recommended)
-   **Windows 10/11**, **macOS 11+**, or a compatible **Linux**
    distribution\
-   **3--10 GB free storage** depending on model size
-   GPU optional

------------------------------------------------------------------------

# 3. Installation Instructions

------------------------------------------------------------------------

## macOS

### Install with Homebrew (recommended)

``` bash
brew install ollama
```

### Start the service

``` bash
ollama serve
```

### Check installation

``` bash
ollama --version
```

------------------------------------------------------------------------

## Windows

### Option 1: Installer (recommended)

1.  Download from: https://ollama.com/download/windows\
2.  Run the `.exe` installer\
3.  Click through setup\
4.  Open PowerShell and verify:

``` powershell
ollama --version
```

### Option 2: Winget

``` powershell
winget install Ollama.Ollama
```

------------------------------------------------------------------------

## Linux

### Ubuntu / Debian / Fedora (Official Script)

``` bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Arch Linux (AUR)

``` bash
yay -S ollama-bin
```

### Start service

``` bash
ollama serve
```

------------------------------------------------------------------------

# 4. Running Your First Model

### Example: Llama 3

``` bash
ollama run llama3
```

Or run an 8B version:

``` bash
ollama run llama3:8b
```

Press **Ctrl + C** to exit a session.

------------------------------------------------------------------------

# 5. Managing Models

### List installed models

``` bash
ollama list
```

### Download a model

``` bash
ollama pull mistral
```

### Delete a model

``` bash
ollama rm mistral
```

------------------------------------------------------------------------

# 6. Optional: Using Ollama with VS Code

1.  Install the "Continue" extension\
2.  Start the Ollama backend:

``` bash
ollama serve
```

3.  Configure the extension to use `http://localhost:11434`

------------------------------------------------------------------------

# 7. Troubleshooting

### "Command not found"

-   Close and reopen terminal\
-   Reinstall Ollama

### Low RAM issues

Use a smaller model:

``` bash
ollama run phi3
```

### Service won't start (Linux)

``` bash
systemctl restart ollama
```

------------------------------------------------------------------------

# 8. Uninstalling Ollama

### macOS

``` bash
brew uninstall ollama
```

### Windows

``` powershell
winget uninstall Ollama.Ollama
```

### Linux

``` bash
sudo rm -rf /usr/local/bin/ollama ~/.ollama
```

------------------------------------------------------------------------

# 9. Useful Links

-   Website: https://ollama.com\
-   Model Library: https://ollama.com/library\
-   GitHub: https://github.com/ollama/ollama
