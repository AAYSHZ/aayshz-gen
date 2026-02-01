# 🎬 Aayshz AI Video Generator

**Generate unlimited AI videos on your own hardware - completely free and open source!**

Built on top of [SkyReels-V2](https://github.com/SkyworkAI/SkyReels-V2), this is a simplified, user-friendly interface for creating stunning AI-generated videos from text descriptions or images.

## ⚡ Quick Start

```bash
# 1. Clone this repository
git clone https://github.com/YOUR_USERNAME/aayshz-video-gen.git
cd aayshz-video-gen

# 2. Run the one-command installer
bash install.sh

# 3. Generate your first video!
python generate.py --prompt "A cat playing piano in a jazz club"
```

## ✨ Features

- 🎥 **Text-to-Video** - Create videos from text descriptions
- 🖼️ **Image-to-Video** - Animate your images
- ⏱️ **Flexible Duration** - 4 seconds to 60+ seconds
- 🎨 **Multiple Styles** - Cinematic, anime, realistic, fantasy
- 🌐 **Web Interface** - Easy browser-based UI
- 🏷️ **Custom Watermarks** - Add your branding
- 💻 **100% Local** - Runs on your own hardware
- 🆓 **Completely Free** - No API costs, no limits

## 🖥️ Requirements

**Hardware:**
- NVIDIA GPU with 16GB+ VRAM (RTX 3090, 4090, A100, etc.)
- 32GB+ RAM
- 50GB+ free storage

**Software:**
- Linux (Ubuntu 20.04+ recommended)
- Python 3.10+
- CUDA 11.8 or 12.1+

## 📦 Installation

### Automatic Installation (Recommended)

```bash
bash install.sh
```

This will:
- Create virtual environment
- Install all dependencies
- Download AI models (optional)
- Set up everything automatically

### Manual Installation

```bash
# Create virtual environment
python3.10 -m venv venv
source venv/bin/activate

# Install PyTorch with CUDA
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Install other dependencies
pip install -r requirements.txt

# Download models
huggingface-cli download Skywork/SkyReels-V2-I2V-1.3B-540P --local-dir ./models/SkyReels-V2-I2V-1.3B-540P
```

## 🚀 Usage

### Command Line

**Basic text-to-video:**
```bash
python generate.py --prompt "A sunset over the ocean"
```

**High quality with style:**
```bash
python generate.py \
  --prompt "A dragon flying over mountains" \
  --quality best \
  --style fantasy
```

**Animate an image:**
```bash
python generate.py \
  --image photo.jpg \
  --prompt "The person smiles and waves"
```

**Long video (30 seconds):**
```bash
python generate.py \
  --long \
  --duration 30 \
  --prompt "A cinematic journey through space"
```

### Web Interface

```bash
python web_ui.py
```

Then open your browser to `http://localhost:7860`

## 📖 Documentation

- [Quick Start Guide](docs/QUICKSTART.md)
- [Complete User Guide](docs/USER_GUIDE.md)
- [Advanced Features](docs/ADVANCED.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md)

## 🎨 Examples

### Text-to-Video
```bash
python generate.py --prompt "A graceful white swan swimming in a peaceful lake at dawn, with mist rising from the water and soft golden sunlight filtering through trees"
```

### Image-to-Video
```bash
python generate.py --image portrait.jpg --prompt "The person's expression changes from serious to a warm smile, eyes lighting up with joy"
```

### Style Examples
```bash
# Cinematic
python generate.py --prompt "A hero walking through ruins" --style cinematic

# Anime
python generate.py --prompt "Magical girl transformation" --style anime

# Realistic
python generate.py --prompt "Wildlife documentary of lions" --style realistic
```

## ⚙️ Command Options

| Option | Description | Default |
|--------|-------------|---------|
| `--prompt` | Video description (required) | - |
| `--image` | Input image for I2V | None |
| `--duration` | Length: 4, 10, 15, 30, 60 seconds | 4 |
| `--quality` | draft, good, or best | good |
| `--style` | cinematic, anime, realistic, etc. | cinematic |
| `--long` | Enable long video mode | False |
| `--watermark` | Add watermark | False |
| `--seed` | Random seed | random |
| `--output` | Output directory | ./outputs |

## 💾 Available Models

| Model | Size | VRAM | Best For |
|-------|------|------|----------|
| I2V-1.3B-540P | ~5GB | 14.7GB | Image-to-Video, testing |
| T2V-14B-540P | ~28GB | 43GB | Text-to-Video, quality |
| DF-14B-540P | ~28GB | 51GB | Long videos (30s+) |
| T2V-14B-720P | ~28GB | 60GB+ | Highest quality |

See [models documentation](docs/MODELS.md) for details.

## 🔧 Performance Tips

**For faster generation:**
```bash
python generate.py --prompt "..." --quality draft
```

**For best quality:**
```bash
python generate.py --prompt "..." --quality best --duration 4
```

**For long videos:**
```bash
python generate.py --long --duration 30 --prompt "..."
```

## 🐛 Troubleshooting

### Out of Memory
```bash
# Use smaller model or draft quality
python generate.py --prompt "..." --quality draft
```

### Slow Generation
```bash
# Start with 4-second videos
python generate.py --prompt "..." --duration 4
```

### Model Download Issues
```bash
# Manual download
huggingface-cli download Skywork/SkyReels-V2-I2V-1.3B-540P \
  --local-dir ./models/SkyReels-V2-I2V-1.3B-540P
```

See [Troubleshooting Guide](docs/TROUBLESHOOTING.md) for more help.

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is based on [SkyReels-V2](https://github.com/SkyworkAI/SkyReels-V2).

**Components:**
- SkyReels-V2 AI Model: Skywork AI (original license applies)
- This interface and scripts: MIT License (see LICENSE)

Please review the original SkyReels-V2 license for model usage terms.

## 🙏 Credits

- **SkyReels-V2** - The amazing AI model by [Skywork AI](https://github.com/SkyworkAI)
- **Diffusers** - Model integration by [Hugging Face](https://github.com/huggingface/diffusers)
- **Gradio** - Web interface framework

## 🌟 Star History

If this project helps you, please ⭐ star it on GitHub!

## 📧 Support

- 📖 [Documentation](docs/)
- 🐛 [Issues](https://github.com/YOUR_USERNAME/aayshz-video-gen/issues)
- 💬 [Discussions](https://github.com/YOUR_USERNAME/aayshz-video-gen/discussions)

## 🎉 Showcase

Share your creations! Tag us or open a discussion to show what you've made.

---

**Made with 💜 for the open-source AI community**

*Generate unlimited AI videos on your own hardware - no limits, no costs!*
