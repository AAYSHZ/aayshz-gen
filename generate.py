#!/usr/bin/env python3
"""
Aayshz AI Video Generator
Simple interface for SkyReels-V2 video generation
"""

import os
import sys
import argparse
from pathlib import Path

# Check if SkyReels is available
try:
    # Import will work after installation
    pass
except ImportError:
    print("⚠️  SkyReels-V2 not found. Please run install.sh first.")
    sys.exit(1)

BANNER = """
╔══════════════════════════════════════════════════════╗
║     🎬 Aayshz AI Video Generator                    ║
║     Generate unlimited videos on your hardware       ║
╚══════════════════════════════════════════════════════╝
"""

def main():
    print(BANNER)
    
    parser = argparse.ArgumentParser(
        description='Generate AI videos from text or images',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate.py --prompt "A cat playing piano"
  python generate.py --image photo.jpg --prompt "Person smiling"
  python generate.py --long --duration 30 --prompt "Space journey"
        """
    )
    
    parser.add_argument('--prompt', type=str, required=True,
                       help='Text description of the video')
    parser.add_argument('--image', type=str, default=None,
                       help='Input image for image-to-video')
    parser.add_argument('--long', action='store_true',
                       help='Enable long video generation')
    parser.add_argument('--duration', type=int, default=4,
                       choices=[4, 10, 15, 30, 60],
                       help='Video duration in seconds')
    parser.add_argument('--quality', choices=['draft', 'good', 'best'],
                       default='good', help='Quality preset')
    parser.add_argument('--style', type=str, default='cinematic',
                       help='Video style (cinematic, anime, realistic, etc.)')
    parser.add_argument('--output', type=str, default='./outputs',
                       help='Output directory')
    parser.add_argument('--watermark', action='store_true',
                       help='Add watermark to video')
    parser.add_argument('--seed', type=int, default=None,
                       help='Random seed for reproducibility')
    parser.add_argument('--resolution', choices=['540P', '720P'],
                       default='540P', help='Video resolution')
    
    args = parser.parse_args()
    
    # Map settings
    duration_map = {4: 97, 10: 257, 15: 377, 30: 737, 60: 1457}
    quality_map = {
        'draft': {'steps': 20, 'guidance': 5.0},
        'good': {'steps': 30, 'guidance': 6.0},
        'best': {'steps': 50, 'guidance': 7.0}
    }
    
    num_frames = duration_map[args.duration]
    preset = quality_map[args.quality]
    enhanced_prompt = f"{args.style} style, {args.prompt}"
    
    os.makedirs(args.output, exist_ok=True)
    
    # Build command to call original SkyReels scripts
    if args.long:
        script = "generate_video_df.py"
        model_id = f"Skywork/SkyReels-V2-DF-14B-{args.resolution}"
        base_frames = 121 if args.resolution == '720P' else 97
        
        cmd = [
            f"python3 {script}",
            f"--model_id {model_id}",
            f"--resolution {args.resolution}",
            "--ar_step 0",
            f"--base_num_frames {base_frames}",
            f"--num_frames {num_frames}",
            "--overlap_history 17",
            f"--prompt \"{enhanced_prompt}\"",
            "--addnoise_condition 20",
            "--offload"
        ]
        
        if args.image:
            cmd.append(f"--image {args.image}")
            
    else:
        script = "generate_video.py"
        
        if args.image:
            model_id = f"Skywork/SkyReels-V2-I2V-14B-{args.resolution}"
            shift = 5.0
            guidance = 5.0
        else:
            model_id = f"Skywork/SkyReels-V2-T2V-14B-{args.resolution}"
            shift = 8.0
            guidance = preset['guidance']
        
        cmd = [
            f"python3 {script}",
            f"--model_id {model_id}",
            f"--resolution {args.resolution}",
            f"--num_frames {num_frames}",
            f"--prompt \"{enhanced_prompt}\"",
            f"--guidance_scale {guidance}",
            f"--shift {shift}",
            f"--inference_steps {preset['steps']}",
            "--offload"
        ]
        
        if args.image:
            cmd.append(f"--image {args.image}")
    
    if args.seed:
        cmd.append(f"--seed {args.seed}")
    
    cmd.append(f"--outdir {args.output}")
    
    print(f"\n📝 Prompt: {enhanced_prompt}")
    print(f"⚙️  Settings: {args.duration}s, {args.quality} quality, {args.resolution}")
    print(f"\n🚀 Generating... This may take several minutes.\n")
    
    # Execute
    exit_code = os.system(" ".join(cmd))
    
    if exit_code == 0:
        print("\n✅ Video generated successfully!")
        print(f"📁 Saved to: {args.output}\n")
        
        if args.watermark:
            print("🎨 Adding watermark...")
            videos = list(Path(args.output).glob("*.mp4"))
            if videos:
                latest = max(videos, key=lambda p: p.stat().st_mtime)
                os.system(f"python3 add_watermark.py {latest}")
    else:
        print("\n❌ Generation failed. Check the output above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
