from model_load import call_llm
def agent_plus (topic,chapter,lesson):
    prompt = f"""
    你是一名“工程类教材编写专家”，正在编写一门结构严谨的课程。

    【课程主题】
    {topic}

    【本章初始教材】
    {lesson}

    【当前章节】
    {chapter}

    -----------------------------------
    【任务要求（核心）】
    只需要修改核心知识点，以核心知识点为大纲补全知识点的具体内容，如果是核心技术栈需要增加实现代码
    严禁改变其余内容格式，输出修改后的全文
  
    -----------------------------------
    """
    return call_llm(prompt)
