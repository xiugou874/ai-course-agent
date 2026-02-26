from model_load import call_llm

def agent_summary(chapter, lesson):

    prompt = f"""
请对以下教学内容做“知识摘要”，用于后续课程避免重复。

【章节】
{chapter}

【内容】
{lesson}

要求：
1. 提取核心知识点（3-6条）
2. 用简洁句子表达（每条一行）
3. 不要解释，不要废话
4. 输出格式：
- xxx
- xxx
"""

    return call_llm(prompt)