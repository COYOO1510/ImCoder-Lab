"""批量压缩 ReadDocs 文档图片。

用法:
    python compress_images.py                 # 无损优化（转 RGB + optimize），输出到 images/compressed/
    python compress_images.py --apply         # 直接覆盖原文件（会先备份到 images/backup/）
    python compress_images.py --quality 256   # 有损量化到 256 色（适合图表/截图，体积更小）
    python compress_images.py --max-width 1600  # 超过该宽度则等比缩小

说明:
    - 无损: 去除冗余 alpha 通道(RGBA->RGB) + PNG optimize, 画质完全不变
    - 量化: 将颜色数限制到 --quality 个, 图表/框图类体积大幅下降, 照片可能轻微色带
"""
import argparse
import os
import shutil
from PIL import Image

IMG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "source", "_static", "images")


def compress(path, out_path, quality=None, max_width=None):
    im = Image.open(path)
    # 去除冗余 alpha 通道
    if im.mode == "RGBA":
        alpha = im.getchannel("A")
        if alpha.getextrema() == (255, 255):
            im = im.convert("RGB")
        elif quality:
            im = im.convert("RGB")  # 量化不支持 alpha
    # 等比缩小
    if max_width and im.width > max_width:
        h = round(im.height * max_width / im.width)
        im = im.resize((max_width, h), Image.LANCZOS)
    # 保存
    kwargs = {"optimize": True}
    if quality:
        im = im.quantize(colors=quality, method=Image.MEDIANCUT).convert("RGB")
        kwargs = {"optimize": True}
    im.save(out_path, "PNG", **kwargs)
    return os.path.getsize(out_path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="直接覆盖原文件(自动备份)")
    ap.add_argument("--quality", type=int, default=None, help="有损量化颜色数, 如 256")
    ap.add_argument("--max-width", type=int, default=None, help="超过该宽度则等比缩小")
    args = ap.parse_args()

    os.makedirs(os.path.join(IMG_DIR, "compressed"), exist_ok=True)
    backup = os.path.join(IMG_DIR, "backup")
    if args.apply:
        os.makedirs(backup, exist_ok=True)

    total_before = total_after = 0
    print(f"{'文件':<35}{'原始':>10}{'压缩后':>10}{'节省':>8}")
    print("-" * 68)
    for name in sorted(os.listdir(IMG_DIR)):
        if not name.lower().endswith(".png"):
            continue
        src = os.path.join(IMG_DIR, name)
        dst = os.path.join(IMG_DIR, "compressed", name)
        before = os.path.getsize(src)
        after = compress(src, dst, args.quality, args.max_width)
        total_before += before
        total_after += after
        saved = (1 - after / before) * 100
        print(f"{name:<35}{before:>9,}{after:>9,}{saved:>7.1f}%")

        if args.apply:
            shutil.copy2(src, os.path.join(backup, name))
            shutil.copy2(dst, src)

    print("-" * 68)
    print(f"{'合计':<35}{total_before:>9,}{total_after:>9,}{(1 - total_after / total_before) * 100:>7.1f}%")
    if args.apply:
        print(f"\n已覆盖原文件, 备份在: {backup}")
    else:
        print(f"\n预览结果输出到: {os.path.join(IMG_DIR, 'compressed')}")
        print("确认无误后, 用 --apply 覆盖原文件")


if __name__ == "__main__":
    main()
