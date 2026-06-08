# 2048 游戏

## 仓库链接
https://github.com/1823568/2048

## 项目简介

本项目是基于 Pygame 开发的 2048 益智游戏，在原版基础上扩展了**分数系统**、**最高分持久化存储**、**关卡系统**等功能。

## 环境要求

| 项目 | 要求 |
|------|------|
| 操作系统 | Windows 10/11 |
| Python 版本 | 3.6 及以上 |
| 依赖库 | pygame, loguru |

## 安装步骤

### 1. 克隆项目
```bash
git clone https://github.com/1823568/2048.git
cd 2048
2. 创建虚拟环境
bash
python -m venv venv
3. 激活虚拟环境
bash
venv\Scripts\activate
4. 安装依赖
bash
pip install pygame loguru
5. 运行游戏
bash
python main.py
游戏操作
操作	说明
↑ ↓ ← → 方向键	移动方块
鼠标拖动	也可以移动方块
扩展功能
功能	说明
分数系统	合并方块时增加对应分数
最高分保存	JSON 文件持久化存储
关卡系统	每100分升1级
异常处理	文件读写错误不会崩溃
文件结构
text
2048/
├── main.py              # 程序入口
├── score_manager.py     # 分数管理模块
├── AI_LOG.md            # AI 辅助开发日志
├── README.md            # 项目说明
├── snd/
│   ├── core.py          # 游戏核心逻辑
│   ├── game.py          # 游戏主类
│   ├── draw.py          # 图形绘制
│   └── constant.py      # 常量配置
├── requirements.txt     # 依赖列表
└── highscore.json       # 最高分存储
许可证
本项目基于 MIT 许可证开源