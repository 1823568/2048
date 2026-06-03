"""
分数管理模块 - 满足数据持久化、面向对象、异常处理要求
"""
import json
import os

class ScoreManager:
    """管理游戏分数和关卡的类"""
    
    def __init__(self, filename="highscore.json"):
        self.filename = filename
        self.current_score = 0
        self.highscore = self.load_highscore()
    
    def add_score(self, points):
        """增加当前分数"""
        self.current_score += points
        if self.current_score > self.highscore:
            self.highscore = self.current_score
            self.save_highscore(self.highscore)
        return self.current_score
    
    def get_current_score(self):
        return self.current_score
    
    def get_highscore(self):
        return self.highscore
    
    def get_level(self):
        """根据最高分计算关卡（每100分升1级）"""
        return self.highscore // 100 + 1
    
    def reset_current_score(self):
        """重置当前分数（新游戏时调用）"""
        self.current_score = 0
    
    def save_highscore(self, score):
        """保存最高分到文件"""
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump({"highscore": score}, f)
            return True
        except Exception as e:
            print(f"保存失败: {e}")
            return False
    
    def load_highscore(self):
        """从文件加载最高分"""
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("highscore", 0)
        except FileNotFoundError:
            return 0
        except json.JSONDecodeError:
            return 0