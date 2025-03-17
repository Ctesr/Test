import os
from PIL import Image
import sys


def remove_transparency_and_crop(image_path, output_path):
    try:
        with Image.open(image_path) as img:
            # 仅处理带透明通道的图像
            if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                # 转换为RGBA确保透明度信息可用
                rgba_img = img.convert('RGBA')

                # 获取有效像素的边界框
                bbox = rgba_img.getbbox()

                if bbox:
                    # 执行裁剪操作
                    cropped = rgba_img.crop(bbox)
                else:
                    # 处理全透明图像：创建1x1透明像素
                    cropped = Image.new('RGBA', (1, 1), (0, 0, 0, 0))

                # 保持原始格式（如果支持透明）或强制保存为PNG
                if img.format in ('PNG', 'WEBP'):
                    cropped.save(output_path, format=img.format)
                else:
                    cropped.save(output_path, format='PNG')  # 非透明格式强制转PNG
            else:
                # 对于非透明图像，直接保存原图
                img.save(output_path)

    except Exception as e:
        print(f"Error processing {image_path}: {str(e)}")


def process_folder(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.webp')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # 确保输出格式正确
            if not output_path.lower().endswith(('.png', '.webp')):
                output_path = os.path.splitext(output_path)[0] + '.png'

            remove_transparency_and_crop(input_path, output_path)
            print(f"Processed: {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python transparent_crop.py <input_folder> <output_folder>")
    else:
        input_folder = sys.argv[1]
        output_folder = sys.argv[2]
        process_folder(input_folder, output_folder)
