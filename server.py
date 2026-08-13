#!/usr/bin/env python3
"""
ReadDocs 本地预览服务器（无缓存版）
每次刷新都读取磁盘最新文件，避免浏览器缓存导致看不到更新。
"""
import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler


class NoCacheHandler(SimpleHTTPRequestHandler):
    """禁用缓存的请求处理器，确保每次都能看到最新内容。"""

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, format, *args):
        # 简化日志输出，只显示请求路径
        sys.stdout.write("  %s\n" % (format % args))


def main():
    port = 8000
    # 默认服务 build/html 目录（脚本位于项目根目录时）
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "build", "html")
    if len(sys.argv) > 1:
        root = sys.argv[1]
    os.chdir(root)

    server = HTTPServer(("0.0.0.0", port), NoCacheHandler)
    print("=" * 50)
    print("  ReadDocs 预览服务器已启动（无缓存模式）")
    print("  目录: %s" % root)
    print("  地址: http://localhost:%d/" % port)
    print("  提示: 修改文档后重新运行 deploy.bat 并刷新浏览器")
    print("  停止: 按 Ctrl + C")
    print("=" * 50)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止。")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
