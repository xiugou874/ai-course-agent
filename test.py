from searchcore import retrieve_knowledge
from Agent3 import agent_teach
from Agent1 import agent_plan
from Agent5 import agent_plus
topic="具身智能"
chapters=agent_plan(topic)
print(chapters)
for chapter in chapters:
    knowledge=retrieve_knowledge(topic, chapter)
    lesson = agent_teach(topic,chapter, knowledge,"",chapters)
    print(lesson)
    lesson2 =agent_plus(topic,chapter,lesson)
    print(lesson2)