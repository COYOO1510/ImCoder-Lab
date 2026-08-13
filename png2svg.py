import base64
import io
from PIL import Image

src = "e:/ReadDocs/ReadDocs/source/_static/images/logo.png"
dst = "e:/ReadDocs/ReadDocs/source/_static/images/logo.svg"

im = Image.open(src)
w, h = im.size
buf = io.BytesIO()
im.save(buf, format="PNG")
b64 = base64.b64encode(buf.getvalue()).decode()

svg = (
    '<svg xmlns="http://www.w3.org/2000/svg" '
    'xmlns:xlink="http://www.w3.org/1999/xlink" '
    'width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
    '<image width="{w}" height="{h}" '
    'xlink:href="data:image/png;base64,{b64}"/>'
    '</svg>'
).format(w=w, h=h, b64=b64)

with open(dst, "w", encoding="utf-8") as f:
    f.write(svg)

print("已生成 logo.svg, 尺寸 %dx%d" % (w, h))
