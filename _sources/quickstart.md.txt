# 快速开始

欢迎使用 ReadDocs！本指南将帮助你是的是的是的是的是多少大萨达四大四大四大四大。

## 环境要求

- Python 3.8+
- Sphinx 文档生成器

## 安装

```bash
pip install sphinx myst-parser sphinx-rtd-theme
```

## 构建文档

在项目根目录下运行：

```bash
# Windows
.\make.bat html

# Linux/Mac
make html
```

构建完成后，HTML 文档将生成在 `build/html/` 目录下。

## 本地预览

打开 `build/html/index.html` 即可在浏览器中预览文档。

## 编写文档

ReadDocs 同时支持以下格式：

- **reStructuredText** (`.rst`) — Sphinx 原生格式，功能最全面
- **Markdown** (`.md`) — 通过 MyST 解析器支持，编写更简洁

### Markdown 示例

```markdown
# 标题

这是一段**粗体**和*斜体*文字。

- 列表项 1
- 列表项 2

| 列1 | 列2 |
|-----|-----|
| A   | B   |
```

### 插入图片

Markdown 中插入图片非常简单：

```markdown
![描述文字](图片路径)
```

效果如下：

![ReadDocs Banner](_static/images/readdocs-banner.svg)
