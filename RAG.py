from searchcore import search_web
from searchcore import search_arxiv
from searchcore import search_wiki

def retrieve_knowledge(topic):
    web = search_web(topic)
    paper = search_arxiv(topic)
    wiki = search_wiki(topic)

    return f"""
【网页信息】
{web}

【论文信息】
{paper}

【百科信息】
{wiki}
"""