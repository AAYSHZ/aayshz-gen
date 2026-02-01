#!/usr/bin/env python3
"""
Aayshz AI Video Generator - Web Interface
"""

import gradio as gr
import os
import subprocess
from pathlib import Path

def generate_video(prompt, image, duration, quality, style):
    """Generate video"""
    
    if not prompt:
        return None, "❌ Please provide a prompt"
    
    cmd = ["python", "generate.py", "--prompt", prompt]
    
    if image is not None:
        temp_img = "temp_input.jpg"
        image.save(temp_img)
        cmd.extend(["--image", temp_img])
    
    if duration > 4:
        cmd.append("--long")
    
    cmd.extend([
        "--duration", str(duration),
        "--quality", quality,
        "--style", style,
        "--output", "./outputs"
    ])
    
    log = f"🚀 Generating video...\n"
    log += f"Prompt: {prompt}\n"
    log += f"Settings: {duration}s, {quality}, {style}\n\n"
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
        log += result.stdout
        if result.stderr:
            log += "\n" + result.stderr
        
        # Find latest video
        videos = list(Path("./outputs").glob("*.mp4"))
        if videos:
            latest = max(videos, key=lambda p: p.stat().st_mtime)
            return str(latest), log
        else:
            return None, log + "\n❌ No video generated"
    except Exception as e:
        return None, log + f"\n❌ Error: {str(e)}"

# Create interface
with gr.Blocks(title="Aayshz AI Video Generator", theme=gr.themes.Soft()) as demo:
    
    gr.Markdown("""
    # 🎬 Aayshz AI Video Generator
    ### Generate unlimited AI videos on your own hardware
    """)
    
    with gr.Row():
        with gr.Column():
            prompt = gr.Textbox(
                label="Video Description",
                placeholder="Describe your video in detail...",
                lines=4
            )
            
            image = gr.Image(
                label="Input Image (Optional - for Image-to-Video)",
                type="pil"
            )
            
            with gr.Row():
                duration = gr.Slider(4, 30, value=4, step=1, label="Duration (seconds)")
                quality = gr.Radio(["draft", "good", "best"], value="good", label="Quality")
            
            style = gr.Dropdown(
                ["cinematic", "anime", "realistic", "fantasy", "documentary"],
                value="cinematic",
                label="Style"
            )
            
            generate_btn = gr.Button("🎬 Generate Video", variant="primary", size="lg")
        
        with gr.Column():
            output_video = gr.Video(label="Generated Video")
            output_log = gr.Textbox(label="Log", lines=12, interactive=False)
    
    generate_btn.click(
        fn=generate_video,
        inputs=[prompt, image, duration, quality, style],
        outputs=[output_video, output_log]
    )
    
    gr.Markdown("""
    ---
    ### 💡 Tips:
    - Be detailed in your prompts
    - Start with 4-second videos for testing
    - Use 'draft' quality for quick previews
    - Upload an image to animate it
    
    **Made with 💜 - Generate unlimited videos on your hardware!**
    """)

if __name__ == "__main__":
    os.makedirs("./outputs", exist_ok=True)
    demo.launch(server_name="0.0.0.0", server_port=7860)
