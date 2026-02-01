# Quick Start Guide

Get started with Aayshz AI Video Generator in 5 minutes!

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/aayshz-video-gen.git
cd aayshz-video-gen

# 2. Run installer
bash install.sh

# 3. Activate environment
source venv/bin/activate
```

## Your First Video

### Text-to-Video
```bash
python generate.py --prompt "A beautiful sunset over the ocean"
```

### Image-to-Video
```bash
python generate.py --image your_photo.jpg --prompt "The person smiles"
```

### Web Interface
```bash
python web_ui.py
# Open browser to http://localhost:7860
```

## Common Commands

### Quick test (fast)
```bash
python generate.py --prompt "A cat playing" --quality draft
```

### High quality
```bash
python generate.py --prompt "A dragon flying" --quality best
```

### Long video (30s)
```bash
python generate.py --long --duration 30 --prompt "Space journey"
```

### Different styles
```bash
python generate.py --prompt "Magical forest" --style fantasy
python generate.py --prompt "City at night" --style cinematic
python generate.py --prompt "Character design" --style anime
```

## Example Prompts

**Good prompts are detailed:**

❌ Bad: "A cat"
✅ Good: "A fluffy orange tabby cat with green eyes, sitting on a windowsill in warm afternoon sunlight, grooming its paw"

**Try these:**
```bash
# Nature
python generate.py --prompt "A waterfall in a lush rainforest with mist rising and sunbeams filtering through the canopy"

# Urban
python generate.py --prompt "A busy Tokyo street at night with neon signs, rain on pavement, and people with umbrellas"

# Fantasy
python generate.py --prompt "A wizard casting a glowing spell in an ancient stone tower filled with magical artifacts"

# Animals
python generate.py --prompt "A majestic eagle soaring over snow-capped mountains under a clear blue sky"
```

## Next Steps

- Check [USER_GUIDE.md](USER_GUIDE.md) for complete documentation
- See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) if you have issues
- Read [ADVANCED.md](ADVANCED.md) for advanced features

## Tips

1. Start with 4-second videos for testing
2. Use `--quality draft` for quick previews
3. Be detailed in your prompts
4. Try different styles to find what you like
5. Longer videos take more time and VRAM

**Happy creating! 🎬**
