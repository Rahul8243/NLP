import re

# Raw uncleaned paragraphs
paragraphs = [
    "whoaaaa 😵 this article on AI & ethics issss fireeee!!! i mean, wowww, the way it talks about robotssss takin’ over da world? lollll 😂😂😂 so craaazy! found it at www.robotnews.com//// 4 real, u gotta read ittt!!! @@@ #scarybutcool #futuristicttt",
    "can'tttt evennnn with this new techppp blog... sooo muchhh info jam-packed in one loooong posttttt 😩😩!! but the way itzz writtennn… nahhh bruh. full of typos, emoji overload 🤯💥, and weirddddd punctuationnnn like !!!!!!????!!! find it at www.techmessy.io////",
    "A.I. is changinnn’ da worldd, fam!! 🤖✨ like everyyy single aspect of lifeee—workkk, healthhh, educashun 😂😂😂!! dis article: \"how AI gonna make u smarterrrr\" waz LIT 🔥🔥🔥. got it from www.getsmartai.com//// plzzzz fix the grammerz tho #looolz @@@!!!!",
    "omg omg omg 😱😱!! dat post on generative AI + music just BLEW MY HEADDD OFF!! 🧠💥💥💥 no joke!!! \"beethovennnn with beats\" lol whattt evennnn 😆😆 #nextlevel. saw it on www.genmusic.art//// so so many randomnn letterssss & symbols #@#@# 😵",
    "lolz!!! u ever read sumthing n feel dumberrrr after??? 🤣🤣 this blog on AI bias had soooo manyyyy errorsss, like spellingggg, grammerzz, and weird layout @@@%%%... i had to squinttttt. check dis out: www.wacksource.ai//// but read at ur own risk lololol"
]

def clean_text(text):
    # 1. Lowercasing
    text = text.lower()

    # 2. Removing extra whitespace
    text = re.sub(r'\s+', ' ', text)

    # 3. Handling contractions & slang
    contractions = {
        "can't": "cannot",
        "i <3": "i love",
        "u": "you",
        "ur": "your",
        "gonna": "going to",
        "wanna": "want to",
        "takin’": "taking",
        "takin": "taking",
        "waz": "was",
        "fam": "family",
        "nahhh": "no",
        "plzzzz": "please",
        "lol": "laughing out loud",
        "omg": "oh my god",
        "bruh": "brother"
    }
    for k, v in contractions.items():
        text = re.sub(rf"\b{k}\b", v, text)

    # 4. Removing special characters (keep letters, numbers, .,!? for now)
    text = re.sub(r'[^a-z0-9\s.,!?]', '', text)

    # 5. Reducing duplicate letters (3+ → 2 for emphasis words)
    text = re.sub(r'(.)\1{2,}', r'\1\1', text)

    # 6. Fixing excessive punctuation
    text = re.sub(r'([!?.,])\1+', r'\1', text)

    # 7. Removing URL artifacts
    text = re.sub(r'www\.[a-z0-9.-]+/+', '', text)

    return text.strip()

# Apply cleaning to all paragraphs
cleaned_paragraphs = [clean_text(p) for p in paragraphs]

# Display results
for i, p in enumerate(cleaned_paragraphs, 1):
    print(f"Cleaned Paragraph {i}:\n{p}\n{'-'*80}")
