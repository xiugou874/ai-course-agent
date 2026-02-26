from searchcore import retrieve_knowledge, clean_knowledge

def agent_research(chapter, topic):
    raw = retrieve_knowledge(topic, chapter)
    clean = clean_knowledge(raw)
    return clean