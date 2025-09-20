import sys
import threading
import time
import pyttsx3
from textblob import TextBlob

# ---------- Detect Emotion from Text ----------
def detect_emotion(text):
    text_lower = text.lower()

    emotion_keywords = {
        "ecstatic": ['ecstatic'],
        "overjoyed": ['overjoyed'],
        "elated": ['elated'],
        "joyful": ['joyful'],
        "happy": ['happy'],
        "cheerful": ['cheerful'],
        "content": ['content'],
        "pleased": ['pleased'],
        "neutral": ['neutral'],
        "indifferent": ['indifferent'],
        "unhappy": ['unhappy'],
        "sad": ['sad'],
        "mournful": ['mournful'],
        "despondent": ['despondent'],
        "melancholy": ['melancholy'],
        "depressed": ['depressed'],
        "devastated": ['devastated'],
        "hopeful": ['hopeful'],
        "optimistic": ['optimistic'],
        "grateful": ['grateful'],
        "inspired": ['inspired'],
        "amused": ['amused'],
        "calm": ['calm'],
        "confused": ['confused'],
        "disappointed": ['disappointed'],
        "frustrated": ['frustrated'],
        "anxious": ['anxious'],
        "overwhelmed": ['overwhelmed'],
        "guilty": ['guilty'],
        "disgusted": ['disgusted'],
        "repulsed": ['repulsed'],
        "detached": ['detached'],
    }

    for emotion, keywords in emotion_keywords.items():
        if any(word in text_lower for word in keywords):
            return emotion

    return "unknown"


# ---------- Get Emotion from Sentiment Score ----------
def get_emotion(sentiment):
    if sentiment > 0.7:
        return "ecstatic", (220, 1.5)
    elif 0.6 <= sentiment <= 0.7:
        return "overjoyed", (180, 1.4)
    elif 0.5 <= sentiment < 0.6:
        return "elated", (190, 1.3)
    elif 0.4 <= sentiment < 0.5:
        return "joyful", (180, 1.2)
    elif 0.3 <= sentiment < 0.4:
        return "happy", (170, 1.1)
    elif 0.2 <= sentiment < 0.3:
        return "cheerful", (160, 1.0)
    elif 0.1 <= sentiment < 0.2:
        return "content", (150, 0.9)
    elif 0.05 <= sentiment < 0.1:
        return "pleased", (140, 0.8)
    elif -0.05 <= sentiment < 0.05:
        return "neutral", (130, 1)
    elif -0.1 <= sentiment < -0.05:
        return "indifferent", (120, 1)
    elif -0.2 <= sentiment < -0.1:
        return "unhappy", (110, 1)
    elif -0.3 <= sentiment < -0.2:
        return "sad", (100, 1)
    elif -0.4 <= sentiment < -0.3:
        return "mournful", (100, 1)
    elif -0.5 <= sentiment < -0.4:
        return "despondent", (170, 1)
    elif -0.6 <= sentiment < -0.5:
        return "melancholy", (170, 0.1)
    elif -0.7 <= sentiment < -0.6:
        return "depressed", (60, 1)
    elif sentiment <= -0.7:
        return "devastated", (180, 1)
    elif 0.5 <= sentiment < 0.6:
        return "hopeful", (175, 1.3)
    elif 0.4 <= sentiment < 0.5:
        return "optimistic", (165, 1.2)
    elif 0.3 <= sentiment < 0.4:
        return "grateful", (155, 1.1)
    elif 0.2 <= sentiment < 0.3:
        return "inspired", (145, 1.0)
    elif 0.1 <= sentiment < 0.2:
        return "amused", (135, 0.9)
    elif 0.05 <= sentiment < 0.1:
        return "calm", (125, 0.8)
    elif -0.05 <= sentiment < 0.05:
        return "confused", (115, 0.8)
    elif -0.1 <= sentiment < -0.05:
        return "disappointed", (105, 0.9)
    elif -0.2 <= sentiment < -0.1:
        return "frustrated", (100, 0.5)
    elif -0.3 <= sentiment < -0.2:
        return "anxious", (85, 0.8)
    elif -0.4 <= sentiment < -0.3:
        return "overwhelmed", (100, 1)
    elif -0.5 <= sentiment < -0.4:
        return "guilty", (100, 1)
    elif -0.6 <= sentiment < -0.5:
        return "disgusted", (100, 1)
    elif -0.7 <= sentiment < -0.6:
        return "repulsed", (100, 1)
    elif sentiment <= -0.7:
        return "detached", (150, 0.8)


# ---------- Track Emotion Phrases ----------
def track_emotion_phrases(text):
    text = text.lower()

    emotion_map = {
        "love": [
            'love', 'romance', 'affection', 'passion', 'adoration', 'devotion', 'warmth', 'amour', 'infatuation',
            'desire', 'attraction', 'yearning', 'admiration', 'enchantment', 'sweetheart', 'heartfelt', 'tender',
            'embrace', 'cherish', 'butterfly', 'sweetness', 'amorous', 'sentiment', 'woo', 'serene', 'hug', 'kiss',
            'whisper', 'yearn', 'lovers', 'connection', 'affinity', 'magnetic', 'attracted', 'beloved', 'emotion',
            'fond', 'harmony', 'sympathy', 'infatuated', 'enamored', 'darling', 'tenderly', 'suitor', 'heartwarming',
            'softness', 'heartthrob', 'amicable', 'attachment', 'honeyed', 'admirer', 'lovestruck', 'warmhearted',
            'companionate', 'exotic', 'wooing', 'nurturing', 'stargazing', 'whispers', 'romeo', 'juliet', 'emblazoned',
            'fancy', 'allure', 'rapture', 'fantasy', 'longing', 'alluring', 'savor', 'spark', 'enchanted', 'elan',
            'rapt', 'eloquence', 'devoted', 'unspoken', 'affectionate', 'magnetism', 'quixotic'
        ],
        "happy": [
            'happy', 'joyful', 'pleased', 'content', 'cheerful', 'delighted', 'euphoric', 'merry', 'upbeat', 'radiant',
            'sunny', 'ecstatic', 'buoyant', 'lighthearted', 'vibrant', 'carefree', 'satisfied', 'optimistic',
            'whimsical', 'playful', 'jubilant', 'grateful', 'spirited', 'enthusiastic', 'exhilarated', 'gleeful',
            'hopeful', 'peppy', 'zestful', 'jocular', 'sprightly', 'jolly', 'blithe', 'pleasurable', 'chipper',
            'jaunty', 'chirpy', 'zippy'
        ],
        "content": [
            'peaceful', 'serene', 'tranquil', 'calm', 'satisfied', 'relaxed', 'at ease', 'reassured', 'placid',
            'soothed', 'undisturbed', 'gratified', 'composed', 'assured', 'repose', 'comforted', 'untroubled',
            'quieted', 'restful', 'eased', 'serenity', 'easeful', 'balanced', 'stillness', 'heartsease', 'pacified',
            'halcyon', 'pacification', 'equanimity', 'centred', 'unperturbed', 'contentedness', 'contentment',
            'satisfaction', 'steady', 'hushed', 'replenished', 'mild'
        ],
        "neutral": [
            'neutral', 'indifferent', 'calm', 'composed', 'unaffected', 'dispassionate', 'objective', 'uninvolved',
            'unperturbed', 'unresponsive', 'stoic', 'imperturbable', 'nonchalant', 'aloof', 'distant', 'equanimous',
            'balanced', 'unflappable', 'cool-headed', 'serene', 'tranquil', 'unconcerned', 'unexcitable', 'unimpressed',
            'unworried', 'nonplussed', 'matter-of-fact', 'untouched', 'unbiased', 'detached', 'unprejudiced',
            'disinterested', 'Matter-of-fact'
        ],
        "sad": [
            'sad', 'unhappy', 'mournful', 'disheartened', 'dejected', 'downhearted', 'dismal', 'despondent', 'forlorn',
            'gloomy', 'dreary', 'woeful', 'cheerless', 'heartbroken', 'somber', 'down in the dumps', 'downcast',
            'low-spirited', 'miserable', 'glum', 'sullen', 'wretched', 'regretful', 'lamenting', 'grief-stricken',
            'tearful', 'funereal', 'tragic', 'lachrymose', 'weepy', 'morbid', 'anguished', 'heavyhearted'
        ],
        "angry": [
            'angry', 'irate', 'furious', 'enraged', 'agitated', 'irritated', 'wrathful', 'livid', 'maddened',
            'exasperated', 'annoyed', 'provoked', 'irked', 'fuming', 'outraged', 'hostile', 'fierce', 'resentful',
            'tempestuous', 'stormy', 'choleric', 'vexed', 'bitter', 'offended', 'cross', 'huffy', 'upset',
            'tumultuous', 'spiteful', 'rancorous', 'sour', 'irritable', 'testy', 'petulant', 'peeved', 'incensed',
            'infuriated', 'inflamed', 'burning', 'wrath', 'hostility', 'hot-tempered', 'out of control'
        ]
    }

    for emotion, words in emotion_map.items():
        if any(word in text for word in words):
            return emotion

    return None

def print_animated_message(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.050)  # Adjust the sleep duration for the animation speed
    print()

# Core speech logic
def speakbasic(text):
    try:
        rate = 300
        engine = pyttsx3.init()
        engine.setProperty(name='rate', value=rate)

        voices = engine.getProperty('voices')
        engine.setProperty(name='voice', value=voices[1].id)  # You can change index for different voice

        # Sentiment Analysis
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        emotion, (adjusted_rate, adjusted_volume) = get_emotion(sentiment)

        tracked_emotion = track_emotion_phrases(text)
        if tracked_emotion:
            emotion = tracked_emotion

        # Adjust speech characteristics based on emotion
        engine.setProperty(name='rate', value=adjusted_rate)
        engine.setProperty(name='volume', value=adjusted_volume)

        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        pass

# Speak with animation in threads
def fspeak(text):
    speak_thread = threading.Thread(target=speakbasic, args=(text,))
    speak_thread.start()

    print_thread = threading.Thread(target=print_animated_message, args=(f"F.R.I.D.A.Y : {text}",))
    print_thread.start()

    speak_thread.join()
    print_thread.join()

