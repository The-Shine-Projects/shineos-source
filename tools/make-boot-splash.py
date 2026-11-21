#!/usr/bin/env python3
"""Build ShineOS's 640x480 live boot splash from the supplied project logo."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

root = Path(__file__).resolve().parents[1]
logo_path = root / 'config/includes.chroot/usr/share/grub/themes/shineos/shineos-logo.png'
out = root / 'config/bootloaders/splash.png'
image = Image.new('RGB', (640, 480))
pixels = image.load()
for y in range(480):
    t = y / 479
    color = (int(10 + 5*t), int(15 + 9*t), int(32 + 18*t))
    for x in range(640):
        pixels[x, y] = color
logo = Image.open(logo_path).convert('RGBA')
logo.thumbnail((152, 152), Image.Resampling.LANCZOS)
image.paste(logo, ((640-logo.width)//2, 92), logo)
draw = ImageDraw.Draw(image)
font_path = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
font = ImageFont.truetype(font_path, 34)
label = 'SHINEOS'
bounds = draw.textbbox((0, 0), label, font=font)
draw.text(((640-(bounds[2]-bounds[0]))//2, 278), label, font=font, fill=(245, 248, 255))
small = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 16)
label = 'THE SHINE PROJECT'
bounds = draw.textbbox((0, 0), label, font=small)
draw.text(((640-(bounds[2]-bounds[0]))//2, 327), label, font=small, fill=(180, 194, 220))
image.save(out, format='PNG', optimize=True)
