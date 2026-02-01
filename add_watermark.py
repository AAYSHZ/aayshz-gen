#!/usr/bin/env python3
"""Add watermark to videos"""

import cv2
import argparse
from pathlib import Path

def add_watermark(video_path, text="Created with Aayshz", position='bottom-right'):
    """Add watermark to video"""
    
    output_path = str(Path(video_path).parent / f"{Path(video_path).stem}_watermarked.mp4")
    
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.7
    font_thickness = 2
    
    (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, font_thickness)
    
    margin = 20
    if position == 'bottom-right':
        x, y = width - text_width - margin, height - margin
    elif position == 'bottom-left':
        x, y = margin, height - margin
    elif position == 'top-right':
        x, y = width - text_width - margin, text_height + margin
    else:
        x, y = margin, text_height + margin
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        overlay = frame.copy()
        cv2.rectangle(overlay, (x-5, y-text_height-5), (x+text_width+5, y+5), (0,0,0), -1)
        cv2.putText(overlay, text, (x, y), font, font_scale, (255,255,255), font_thickness)
        frame = cv2.addWeighted(overlay, 0.7, frame, 0.3, 0)
        
        out.write(frame)
    
    cap.release()
    out.release()
    print(f"✅ Watermarked: {output_path}")
    return output_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('video', help='Input video')
    parser.add_argument('--text', default='Created with Aayshz')
    parser.add_argument('--position', default='bottom-right',
                       choices=['bottom-right', 'bottom-left', 'top-right', 'top-left'])
    args = parser.parse_args()
    add_watermark(args.video, args.text, args.position)
