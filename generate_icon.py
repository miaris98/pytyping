import os
from PIL import Image, ImageDraw, ImageFont

def create_app_icon():
    sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]
    images = []

    for size in sizes:
        w, h = size
        img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Rounded rectangle background
        bg_color = (24, 24, 37, 255)
        border_color = (137, 180, 250, 255)
        corner_radius = max(2, int(w * 0.2))
        
        draw.rounded_rectangle([2, 2, w - 3, h - 3], radius=corner_radius, fill=bg_color, outline=border_color, width=max(1, int(w * 0.04)))

        # Draw glowing code bracket </> or lightning symbol
        accent_color = (137, 180, 250, 255) # Cyan
        green_color = (166, 227, 161, 255)  # Green

        # Simple high contrast geometric glyph for code </>
        # Left bracket <
        p1 = (int(w * 0.35), int(h * 0.32))
        p2 = (int(w * 0.22), int(h * 0.50))
        p3 = (int(w * 0.35), int(h * 0.68))
        draw.line([p1, p2, p3], fill=green_color, width=max(1, int(w * 0.06)))

        # Right bracket >
        p4 = (int(w * 0.65), int(h * 0.32))
        p5 = (int(w * 0.78), int(h * 0.50))
        p6 = (int(w * 0.65), int(h * 0.68))
        draw.line([p4, p5, p6], fill=green_color, width=max(1, int(w * 0.06)))

        # Slash /
        p7 = (int(w * 0.58), int(h * 0.30))
        p8 = (int(w * 0.42), int(h * 0.70))
        draw.line([p7, p8], fill=accent_color, width=max(1, int(w * 0.06)))

        images.append(img)

    assets_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
    os.makedirs(assets_dir, exist_ok=True)
    ico_path = os.path.join(assets_dir, "icon.ico")
    images[0].save(ico_path, format="ICO", sizes=[(s[0], s[1]) for s in sizes])
    
    png_path = os.path.join(assets_dir, "icon.png")
    images[0].save(png_path, format="PNG")
    print(f"Generated icon at {ico_path} and {png_path}")

if __name__ == "__main__":
    create_app_icon()

