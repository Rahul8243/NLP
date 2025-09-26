import re

text1 = "I love spending time at https://www.xy123z.com/"
urls = re.findall(r'https?://[^\s]+', text1)
print("URL:", urls)


text2 = "My email id is xyz111@gmail.com"
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text2)
print("Email:", emails)


text3 = "#Sushant is trending now in the world."
hashtags = re.findall(r'#\w+', text3)
print("Hashtags:", hashtags)


text4 = "@Ajit, please help me"
mentions = re.findall(r'@\w+', text4)
print("Mentions:", mentions)

text5 = "8853147 sq. km of area washed away in floods"
numbers = re.findall(r'\d+', text5)
print("Numbers:", numbers)

text6 = "Corona virus killed #24506 people. #Corona is un(tolerable)"
punctuations = re.findall(r'[^\w\s]', text6)
print("Punctuations:", punctuations)


text7a = "ABCED3193P"
text7b = "lEcGD012eg"
pan_pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
print("PAN Validity 1:", bool(re.match(pan_pattern, text7a)))
print("PAN Validity 2:", bool(re.match(pan_pattern, text7b)))

text8 = "heyyy this is a verrrry loong texttt"
remove_repeats = re.sub(r'(.)\1+', r'\1', text8)
print("Without repeats:", remove_repeats)

text9 = "9990001796 is a phone number of PMO office"
mobiles = re.findall(r'[6-9]\d{9}', text9)
print("Mobile Numbers:", mobiles)

text10 = "Ajit Doval is the best National Security Advisor so far."
capital_words = re.findall(r'\b[A-Z][a-zA-Z]*\b', text10)
print("Capitalized Words:", capital_words)
