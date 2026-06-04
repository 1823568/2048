# AI 辅助开发日志
## 使用的 AI 工具
- 通义千问

# 提示词记录

# 1. 环境配置
**提示词**：如何安装 pygame 并创建虚拟环境？
**AI 回答摘要**：使用 python -m venv venv 创建虚拟环境，然后 pip install pygame 安装依赖。
**人工修改**：按照回答操作，成功安装,遇到 loguru 缺失，额外执行了 pip install loguru

# 2. 解决依赖缺失
**提示词**：ModuleNotFoundError: No module named 'loguru' 如何解决？
**AI 回答摘要**：运行 pip install loguru 安装该模块。
**人工修改**：直接在终端执行安装命令，问题解决。

# 3. 理解游戏逻辑
**提示词**：解释 2048 游戏的核心移动合并算法
**AI 回答摘要**：通过遍历每一行/列，将非零数字取出，相邻相同则合并（指数+1），再放回原位置。
**人工修改**：理解了代码中 left/right/up/down 函数的实现原理，找到合并位置添加加分代码。

# 4. 分数管理类设计
提示词：设计一个保存最高分到 JSON 的 ScoreManager 类
AI 回答摘要：提供了完整的 ScoreManager 类代码，包含 save_highscore 和 load_highscore 方法。
**人工修改**：在原基础上增加了 get_level() 方法，用于计算关卡（最高分 // 100 + 1）。

# 5. 数据持久化与异常处理
**提示词**：Python 如何用 json 保存和读取数据，并处理异常？
**AI 回答摘要**：使用 try-except 捕获 FileNotFoundError 和 json.JSONDecodeError。
**人工修改**：在 load_highscore 方法中添加了完整的异常处理，避免程序崩溃。

# 6. 在 pygame 中显示文字
提示词：pygame 如何在屏幕上显示分数？
**AI 回答摘要**：使用 pygame.font.Font 创建字体对象，render 方法生成文字表面，blit 绘制到屏幕
**人工修改**：在 game.py 的 flash 方法中添加了分数显示代码，并将当前分数改为黑色显示。

# 7. 调试错误 - 字体找不到
**提示词**：pygame.error: 找不到 'simhei' 字体文件怎么办？
**AI 回答摘要**：使用 pygame.font.Font(None, 36) 使用默认字体，或改用 SysFont。
**人工修改**：将 font = pygame.font.Font('simhei', 36) 改为 font = pygame.font.Font(None, 36)。

# 8. Git 操作
**提示词**：如何 fork 项目并提交到自己的 GitHub？
**AI 回答摘要**：在 GitHub 上点击 Fork 按钮，克隆到本地，修改后执行 git add、git commit、git push。
**人工修改**：按步骤完成了 fork，并进行了多次 commit 提交代码。


# 人工修改总结

 增加当前分数，最高分，关卡选项，满足实验的"关卡"要求 
 将原本AI 推荐使用的白色文字改为黑色文字 使更清晰可见 
 Font('simhei')  Font(None)  避免字体文件不存在错误 
 无异常处理  添加 try-except  满足实验的异常处理要求 

# AI 使用心得

 1.AI 帮助快速搭建了 ScoreManager 类的框架
 2.调试时提供错误解决方案，节省大量时间
 3.需要理解 AI 生成的代码后才能正确集成到项目中
 4.部分 AI 建议需要根据实际项目结构调整