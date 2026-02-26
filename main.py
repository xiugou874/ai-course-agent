from Agent1 import agent_plan
from Agent2 import agent_research
from Agent3 import agent_teach
from Agent4 import agent_summary
from Agent5 import agent_plus

def clean_chapters(plan_text):
    """只保留真正的章节标题"""
    lines = plan_text.split("\n")
    chapters = []

    for line in lines:
        line = line.strip()

        # 过滤垃圾行
        if len(line) < 5:
            continue
        if line.startswith(("#", "-", "*")):
            continue

        chapters.append(line)

    return chapters


def generate_course(topic):
    # print("📌 规划课程结构...")
    plan = agent_plan(topic)

    # print("\n📊 课程结构：\n", plan)

    chapters = clean_chapters(plan)

    full_course = ""
    history =""
    course_dict = {}

    cache = {}  # 🔥 避免重复检索

    for ch in chapters:
        # print(f"\n🔍 检索：{ch}")

        if ch in cache:
            knowledge = cache[ch]
        else:
            knowledge = agent_research(ch,topic)
            cache[ch] = knowledge

        # print(f"📘 生成教案：{ch}")
        lesson = agent_teach(topic,ch, knowledge,history,chapters)
        lesson = clean_text(lesson)
        lesson = agent_plus(topic, ch, lesson)

        full_course += f"\n\n===== {ch} =====\n\n{lesson}"
        history += agent_summary(ch,lesson)

        course_dict[ch] = {
            "knowledge": knowledge,
            "lesson": lesson
        }

    # ✅ 保存 txt
    # with open("course.txt", "w", encoding="utf-8") as f:
    #     f.write(full_course)
    #
    # ✅ 保存 json（关键）
    # with open("course.json", "w", encoding="utf-8") as f:
    #     json.dump(course_dict, f, ensure_ascii=False, indent=2)
    #
    # print("\n✅ 已保存：course.txt + course.json")

    return full_course


def main():
    result = generate_course("具身智能课程")
    print(result)

import markdown

def save_html(content, filename="course.html"):
    html = markdown.markdown(content)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

import re

def clean_text(text):
    # 去 markdown
    text = re.sub(r'[#*`>-]+', '', text)
    return text.strip()


if __name__ == "__main__":
    main()