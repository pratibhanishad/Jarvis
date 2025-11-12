from AUTOMATION.COMMON_AUTOMATION.COMMON_OPEN.open import*
from AUTOMATION.COMMON_AUTOMATION.COMMON_CLOSE.close import*


def common_cmd(text):

    # You need logic to extract "notepad" from "open notepad"
    if "close" in text or "band kar do" in text:
         close()
    else:
        pass