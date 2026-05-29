# Yoimi — AbemaTV / U-Next 视频下载工具

基于 [yuu](https://github.com/noaione/yuu)（已归档）和 [Yoimi](https://github.com/hiyama283/Yoimi) 的修改版。

## 解决的问题

- **多线程下载** — 4 线程并发下载 .ts 分片（过高并发会被日本 CDN 重置连接）
- **自动重试** — 每个分片失败重试 3 次（含渐进式等待 2s/4s），全部下载完后等 5s 再重试失败的分片一轮
- **网络超时保护** — 15 秒超时 + urllib3 传输层重试，应对不稳定网络
- **断点续传** — 下载中断后加 `--resume` 可跳过已下载的分片，不必从头开始

## 安装

**需要 Python 3.10+**

```bash
# 克隆仓库
git clone https://github.com/windmet/abema-downloader
cd Yoimi

# 安装依赖
pip install -r requirements.txt
```

## 用法

```bash
# 查看帮助
python yoimi.py -h

# 下载 AbemaTV 视频（默认最高画质 1080p）
python yoimi.py download "https://abema.tv/video/episode/xxx"

# 指定清晰度
python yoimi.py download "https://abema.tv/video/episode/xxx" -r 720p

# 查看可用清晰度
python yoimi.py download "https://abema.tv/video/episode/xxx" -R

# 断点续传（下载中断后重新运行）
python yoimi.py download "https://abema.tv/video/episode/xxx" --resume

# 下载后自动封装为 mp4（需要 ffmpeg）
python yoimi.py download "https://abema.tv/video/episode/xxx" --mux

# 详细日志
python yoimi.py download "https://abema.tv/video/episode/xxx" -v
```

**U-Next 需要登录：**

```bash
python yoimi.py download "https://video.unext.jp/play/xxx" --username 邮箱 --password 密码
```

## 国内访问 AbemaTV 注意事项

1. **日本原生 IP**（机房 IP 会被封锁）
2. **关闭 IPv6**（Windows 在网络设置中取消勾选 IPv6，macOS 在系统偏好设置中关闭）
3. **代理设为全局模式**（规则/分流模式可能被检测到）
4. 本工具模拟 Android 设备请求，不会触发额外的浏览器特征检测

## 依赖

- `requests` — HTTP 请求
- `click` — 命令行参数解析
- `tqdm` — 进度条
- `m3u8` — HLS 播放列表解析
- `pycryptodome` — AES 解密
- `beautifulsoup4` + `lxml` — U-Next 页面解析（仅 U-Next 需要）

## 免责声明

本工具只负责下载已合法获取访问权限的视频流。请遵守当地法律及视频平台的服务条款。

## 待优化项

- **动态并发调节** — 当检测到大量 `ConnectionResetError` 时自动降低并发数（如 4→2→1），网络恢复后再升回去，而不是写死 4 线程
- **SSL 兼容选项** — CDN 对部分 TLS 版本/密码套件不兼容，可增加 `--no-ssl-verify` 或切换底层 TLS 适配器
- **自动检测 IPv6** — 启动时检测 IPv6 是否开启并给出提示
- **文件名校验** — Windows 文件名最长 255 字符，下载前对超长文件名做裁剪
- **ffmpeg 自动下载** — 如果本地没装 ffmpeg 但需要 mux 功能时，自动下载便携版
- **批量下载稳定性** — 下多集时某一集失败不应影响后续任务
- **GYAO! / Aniplus / U-Next 兼容性测试** — 目前只在 AbemaTV 上实机测试过
- **aria2 集成** — 使用 aria2 替代 requests 下载分片，CDN 兼容性更好且支持断点续传
- **下载队列进度持久化** — 退出后记录下载进度，避免临时文件被清理

## 引用

本工具基于以下项目修改：

- [yuu](https://github.com/noaione/yuu)（已归档） — 原始项目，2019 年起停止维护
- [Yoimi](https://github.com/hiyama283/Yoimi) — 基于 yuu 的改进版
