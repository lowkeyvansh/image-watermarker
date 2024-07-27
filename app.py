from PIL import Image, ImageDraw, ImageFont

def add_watermark(image_path, watermark_text, output_path):
    img = Image.open(image_path)
    watermark = Image.new("RGBA", img.size)
    draw = ImageDraw.Draw(watermark, "RGBA")

    font = ImageFont.truetype("arial.ttf", 40)
    text_width, text_height = draw.textsize(watermark_text, font)

    x = img.size[0] - text_width - 10
    y = img.size[1] - text_height - 10
    draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))

    watermarked = Image.alpha_composite(img.convert("RGBA"), watermark)
    watermarked.save(output_path)
    print(f"Watermarked image saved as {output_path}")

image_path = input("Enter path to image: ")
watermark_text = input("Enter watermark text: ")
output_path = input("Enter path to save watermarked image: ")
add_watermark(image_path, watermark_text, output_path)
