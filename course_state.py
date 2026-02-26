class CourseState:
    def __init__(self):
        self.used_knowledge = set()   # 全局去重
        self.chapter_summaries = []   # 每章摘要
        self.history_text = ""        # 历史压缩

    def add_knowledge(self, texts):
        for t in texts:
            self.used_knowledge.add(t)

    def is_used(self, text):
        return text in self.used_knowledge

    def add_summary(self, summary):
        self.chapter_summaries.append(summary)
        self._update_history()

    def _update_history(self):
        # 压缩历史（防止爆token）
        self.history_text = "\n".join(self.chapter_summaries[-5:])