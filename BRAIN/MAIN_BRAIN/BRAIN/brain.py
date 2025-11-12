from LLM.llm import llm1
from LLM.gpt4 import llm2
from BRAIN.MAIN_BRAIN.GOOGLE_BIG_DATA.google_big_data import *
from BRAIN.MAIN_BRAIN.GOOGLE_SMALL_DATA.google_small_data import *

def brain(text):
    if "jarvis" in text:
        text = text.replace("jarvis", "").strip()

    if text.startswith(("who is", "search about", "check who is")):
        answer = deep_answer(text)
        print("Jarvis:", answer)
        return answer

    elif "analysis" in text or "check in internet" in text:
        text = text.replace("analysis", "").replace("check in internet", "").strip()
        answer = search_brain(text)
        print("Jarvis:", answer)
        return answer

    elif text.startswith(("generate", "write", "make")):
        response = llm2(text[len("generate response for"):].strip())
        print("Jarvis:", response)
        return response

    else:
        x = llm1(text)
        print("Jarvis:", x)
        return x
