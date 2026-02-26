import time
from ddgs import DDGS
from model_load import call_llm
import re

# 🔥 Step1: LLM改写搜索query
def rewrite_query(topic, chapter):
    prompt = f"""
将以下课程章节转换为适合搜索引擎的英文关键词。

主题: {topic}
章节: {chapter}

要求：
1. 输出3条英文搜索短语
2. 不要解释
3. 每行一条

示例：
machine learning fundamentals
neural network training methods
deep learning applications
"""
    res = call_llm(prompt)
    return [q.strip() for q in res.split("\n") if len(q.strip()) > 5]


# 🔥 Step2: 真正搜索
def search_web(query, max_results=3):
    results = []


    try:
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=max_results):
                results.append(r.get("body", ""))
    except Exception as e:
        print("⚠️ 搜索失败:", e)

    return results


# 🔥 Step3: 汇总知识
def retrieve_knowledge(topic, chapter):
    queries = rewrite_query(topic, chapter)

    all_results = []

    for q in queries:
        print(f"   🌐 搜索: {q}")
        res = search_web(q)
        all_results.extend(res)

        time.sleep(2)  # 防429

    # 去重 + 截断
    unique = clean_knowledge(all_results)


    return unique

def clean_knowledge(results):
    """
    把搜索结果 → 转换成“可用于课程生成”的干净知识
    """

    cleaned = []

    for text in results:

        # 1️⃣ 去时间/日期
        text = re.sub(r'\b\w+\s\d{1,2},\s\d{4}\b', '', text)

        # 2️⃣ 去 URL
        text = re.sub(r'http\S+', '', text)

        # 3️⃣ 去奇怪符号
        text = re.sub(r'[^a-zA-Z0-9\u4e00-\u9fa5，。,. ]', '', text)

        # 4️⃣ 压缩空格
        text = re.sub(r'\s+', ' ', text).strip()

        # 1️⃣ 去 markdown 符号
        text = re.sub(r"[#*`>-]", "", text)

        # 2️⃣ 去 prompt 残留（你现在最大的问题）
        blacklist = [
            "课程主题", "本章初始教材", "必须是新内容",
            "教学目标", "核心知识点", "总结", "作业或思考题"
        ]
        for b in blacklist:
            text = text.replace(b, "")

        # 5️⃣ 长度过滤（太短=垃圾）
        if len(text) > 80:
            cleaned.append(text)

    # 去重
    cleaned = list(set(cleaned))

    # 截断（避免prompt爆炸）
    cleaned = cleaned[:5]

    return "\n".join(cleaned)

