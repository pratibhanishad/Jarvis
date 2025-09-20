from LLM.llm import llm1
from LLM.gpt4 import llm2
from BRAIN.MAIN_BRAIN.GOOGLE_BIG_DATA.google_big_data import realtimeDataBrain
from BRAIN.MAIN_BRAIN.GOOGLE_SMALL_DATA.google_small_data import run_queries

def brain(text):
    if "jarvis" in text:
        text = text.replace("jarvis", "")
        text = text.strip()

    if text.startswith(("who is", "search about", "check who is")):
        print(run_queries(text))
    elif "analysis" in text or "check in internet" in text or "analaysis" in text:
        text.replace("analysis","")
        text.replace("check in internet","")
        text.replace("analaysis","")
        print(realtimeDataBrain(text))

    elif text.startswith(("generate","write","make")):
        response = llm2(text[len("generate response for"):].strip())
        print("Jarvis:", response)

    else:
       x = llm1(text)
       print(x)

