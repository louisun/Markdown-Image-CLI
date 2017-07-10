# Markdown-Image-CLI 

一款 **Linux** 下的 **Markdown** 命令行工具，用于上传剪切板中的图片到七牛，并返回 **Markdown** 图文本。


## 配置

要用到命令行工具 `xclip` 及七牛 SDK Python 版本。

```bash
sudo apt-get install xclip

pip install qiniu
```

设置 `config.ini` 文件 为你自己的 `domain`, `bucket`, `access_key`, `secret_key`。

## 使用

```python
python Markdown-Image-CLI/main.py
```

推荐使用键盘映射工具, 如在 **Ubuntu** 下，我设置 `Ctrl + Alt + X` 运行上述命令。

![](http://7xj74s.com1.z0.glb.clouddn.com/2017-07-10-15-56-53_r51.png)


我这里用的是 **Ubuntu** 自带截图功能 `copy a screenshot of an area to clipboard`，执行快捷键或运行脚本后，得到 `![](http://7xj74s.com1.z0.glb.clouddn.com/2017-07-10-15-56-53_r51.png)
`，便是上面的图片。 