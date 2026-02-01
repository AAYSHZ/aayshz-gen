# Troubleshooting Guide

## Common Issues and Solutions

### Installation Issues

#### Python Version Error
**Problem:** `Python 3.10+ required`
**Solution:**
```bash
# Install Python 3.10
sudo apt update
sudo apt install python3.10 python3.10-venv
```

#### CUDA Not Found
**Problem:** `CUDA not available`
**Solution:**
```bash
# Check NVIDIA driver
nvidia-smi

# If not working, install CUDA toolkit
# Visit: https://developer.nvidia.com/cuda-downloads
```

### Generation Issues

#### Out of Memory (OOM)
**Problem:** `CUDA out of memory`
**Solutions:**
```bash
# 1. Use smaller model
huggingface-cli download Skywork/SkyReels-V2-I2V-1.3B-540P \
  --local-dir ./models/SkyReels-V2-I2V-1.3B-540P

# 2. Use draft quality
python generate.py --prompt "..." --quality draft

# 3. Shorter videos
python generate.py --prompt "..." --duration 4

# 4. Lower resolution
python generate.py --prompt "..." --resolution 540P
```

#### Slow Generation
**Problem:** Takes too long
**Solutions:**
```bash
# Use draft quality
python generate.py --prompt "..." --quality draft

# Shorter videos
python generate.py --prompt "..." --duration 4

# Check GPU utilization
watch -n 1 nvidia-smi
```

#### Model Not Found
**Problem:** `Model not found`
**Solution:**
```bash
# Download model manually
pip install -U "huggingface_hub[cli]"

# For testing (smallest, 5GB)
huggingface-cli download Skywork/SkyReels-V2-I2V-1.3B-540P \
  --local-dir ./models/SkyReels-V2-I2V-1.3B-540P

# For quality (28GB)
huggingface-cli download Skywork/SkyReels-V2-T2V-14B-540P \
  --local-dir ./models/SkyReels-V2-T2V-14B-540P
```

### Quality Issues

#### Poor Video Quality
**Solutions:**
```bash
# 1. Use best quality
python generate.py --prompt "..." --quality best

# 2. Be more detailed in prompt
python generate.py --prompt "A highly detailed, photorealistic scene of..."

# 3. Try different styles
python generate.py --prompt "..." --style realistic

# 4. Use higher resolution (requires more VRAM)
python generate.py --prompt "..." --resolution 720P
```

#### Video Doesn't Match Prompt
**Solutions:**
1. Be more specific and detailed in your prompt
2. Describe what you want, not what you don't want
3. Include details about lighting, colors, mood
4. Try adjusting the style parameter

### Web UI Issues

#### Port Already in Use
**Problem:** `Port 7860 is already in use`
**Solution:**
```bash
# Kill process on port 7860
lsof -ti:7860 | xargs kill -9

# Or use different port
# Edit web_ui.py and change port number
```

#### Can't Access from Other Devices
**Solution:**
The web UI is already set to `0.0.0.0` which allows access from other devices on your network. Access it at:
```
http://YOUR_IP_ADDRESS:7860
```

### Performance Optimization

#### Maximize Speed
```bash
# Smallest model + draft quality + short videos
python generate.py \
  --prompt "..." \
  --quality draft \
  --duration 4 \
  --resolution 540P
```

#### Maximize Quality
```bash
# Best model + best quality + higher resolution
python generate.py \
  --prompt "..." \
  --quality best \
  --resolution 720P
```

### Hardware Requirements

#### Minimum Setup (Testing)
- GPU: 16GB VRAM (RTX 3090, 4090)
- Model: I2V-1.3B-540P
- Quality: draft
- Duration: 4 seconds

#### Recommended Setup (Production)
- GPU: 24GB+ VRAM (RTX 4090, A5000)
- Model: T2V-14B-540P
- Quality: good
- Duration: 10-15 seconds

#### High-End Setup
- GPU: 40GB+ VRAM (A100)
- Model: T2V-14B-720P
- Quality: best
- Duration: 30+ seconds

## Getting Help

If you still have issues:

1. Check the [GitHub Issues](https://github.com/YOUR_USERNAME/aayshz-video-gen/issues)
2. Search for similar problems
3. Open a new issue with:
   - Your system specs (GPU, RAM, OS)
   - Python version
   - Full error message
   - Command you ran

## Useful Commands

### Check GPU
```bash
nvidia-smi
watch -n 1 nvidia-smi  # Monitor in real-time
```

### Check Disk Space
```bash
df -h
du -sh models/*  # Check model sizes
```

### Check Python Packages
```bash
pip list | grep -E "torch|diffusers|transformers"
```

### Clear Cache
```bash
# Clear HuggingFace cache if space needed
rm -rf ~/.cache/huggingface/hub/*
```

### Test Installation
```bash
# Quick test
python -c "import torch; print(torch.cuda.is_available())"
```

## Still Having Issues?

Open an issue on GitHub with detailed information and we'll help you out!
