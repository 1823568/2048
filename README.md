# 2048 游戏

这是一个使用 Python 和 Pygame 实现的 2048 游戏。

## Linux 使用方法

### 安装(需要python 3.6 及以上版本)

1. 克隆此仓库：

    ```sh
    git clone https://github.com/1823568/2048
    cd 2048
    ```

2. 创建并激活虚拟环境，并安装依赖项：

    ```sh
    python -m venv venv
    .venv/Scripts/activate
    python -m pip install requirements.txt
    ```

### 运行游戏

在虚拟环境中运行以下命令启动游戏：

```sh
python main.py
```

## Windows 使用方法

下载源码后直接运行目录下 `run.bat` 即可(需要安装python 3.6及以上版本)

## 游戏玩法

- 使用箭头键或者鼠标拖动移动方块。

## 文件结构
2048/
├── main.py                 # 程序入口
├── score_manager.py        # 分数管理模块（扩展）
├── AI_LOG.md               # AI 辅助开发日志
├── README.md               # 项目说明文档
│
├── snd/                    # 核心游戏模块
│   ├── __init__.py         # 包标识
│   ├── constant.py         # 常量配置（颜色、窗口大小）
│   ├── core.py             # 游戏核心逻辑（移动、合并）
│   ├── draw.py             # 图形绘制（方块、数字）
│   └── game.py             # 游戏主类（事件处理）
│
├── requirements.txt        # 依赖列表
├── install_venv.bat        # 虚拟环境安装脚本
├── run.bat                 # 游戏启动脚本
│
└── highscore.json          # 最高分存储文件（运行时生成）

## 许可证

此项目基于 MIT 许可证，详情请参阅 [LICENSE](LICENSE) 文件。

组员完善项目部署使用说明，补充运行注意事项
