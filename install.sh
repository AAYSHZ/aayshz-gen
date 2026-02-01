#!/bin/bash

# Aayshz AI Video Generator - Installation Script
set -e

echo "╔══════════════════════════════════════════════════════╗"
echo "║     🎬 Aayshz AI Video Generator Installation       ║"
echo "╚══════════════════════════════════════════════════════╝"
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Check Python
echo "Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 not found${NC}"
    exit 1
fi

python_version=$(python3 --version 2>&1 | grep -oP '\d+\.\d+')
if [ "$(printf '%s\n' "3.10" "$python_version" | sort -V | head -n1)" != "3.10" ]; then
    echo -e "${RED}❌ Python 3.10+ required. Found: $python_version${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Python $python_version${NC}"

# Check GPU
echo "Checking for NVIDIA GPU..."
if command -v nvidia-smi &> /dev/null; then
    echo -e "${GREEN}✅ GPU detected:${NC}"
    nvidia-smi --query-gpu=name,memory.total --format=csv,noheader
else
    echo -e "${YELLOW}⚠️  No NVIDIA GPU detected${NC}"
    echo "This tool requires a CUDA-capable GPU."
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Create venv
echo -e "\nCreating virtual environment..."
python3 -m venv venv
source venv/bin/activate
echo -e "${GREEN}✅ Virtual environment created${NC}"

# Upgrade pip
echo -e "\nUpgrading pip..."
pip install --upgrade pip setuptools wheel > /dev/null
echo -e "${GREEN}✅ Pip upgraded${NC}"

# Install PyTorch
echo -e "\nInstalling PyTorch with CUDA support..."
echo "This may take several minutes..."
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
echo -e "${GREEN}✅ PyTorch installed${NC}"

# Install dependencies
echo -e "\nInstalling dependencies..."
pip install -r requirements.txt
echo -e "${GREEN}✅ Dependencies installed${NC}"

# Clone SkyReels-V2 if not present
if [ ! -d "SkyReels-V2" ]; then
    echo -e "\nCloning SkyReels-V2..."
    git clone https://github.com/SkyworkAI/SkyReels-V2
    echo -e "${GREEN}✅ SkyReels-V2 cloned${NC}"
fi

# Create directories
echo -e "\nCreating directories..."
mkdir -p outputs models
echo -e "${GREEN}✅ Directories created${NC}"

# Make scripts executable
chmod +x generate.py web_ui.py add_watermark.py

# Download model (optional)
echo -e "\n╔══════════════════════════════════════════════════════╗"
echo "║     Model Download (Optional)                        ║"
echo "╚══════════════════════════════════════════════════════╝"
echo ""
echo "Download a model now?"
echo "1) SkyReels-V2-I2V-1.3B-540P (~5GB, Image-to-Video)"
echo "2) SkyReels-V2-T2V-14B-540P (~28GB, Text-to-Video)"
echo "3) Skip (download manually later)"
echo ""
read -p "Choice (1-3): " model_choice

case $model_choice in
    1)
        echo -e "\nDownloading I2V-1.3B model..."
        pip install -U "huggingface_hub[cli]"
        huggingface-cli download Skywork/SkyReels-V2-I2V-1.3B-540P \
            --local-dir ./models/SkyReels-V2-I2V-1.3B-540P
        echo -e "${GREEN}✅ Model downloaded${NC}"
        ;;
    2)
        echo -e "\nDownloading T2V-14B model (~28GB)..."
        pip install -U "huggingface_hub[cli]"
        huggingface-cli download Skywork/SkyReels-V2-T2V-14B-540P \
            --local-dir ./models/SkyReels-V2-T2V-14B-540P
        echo -e "${GREEN}✅ Model downloaded${NC}"
        ;;
    *)
        echo "Skipped. Download models later with:"
        echo "  huggingface-cli download Skywork/MODEL_NAME --local-dir ./models/MODEL_NAME"
        ;;
esac

echo ""
echo "╔══════════════════════════════════════════════════════╗"
echo "║     ✅ Installation Complete!                        ║"
echo "╚══════════════════════════════════════════════════════╝"
echo ""
echo -e "${GREEN}Ready to generate videos!${NC}"
echo ""
echo "Quick Start:"
echo "  1. Activate: source venv/bin/activate"
echo "  2. Generate: python generate.py --prompt 'your idea'"
echo "  3. Web UI: python web_ui.py"
echo ""
echo "See README.md for full documentation."
echo ""
