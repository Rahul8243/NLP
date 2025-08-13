import re

# 1. Find URL in a sentence
text1 = "I love spending time at https://www.xy123z.com/"
urls = re.findall(r'https?://[^\s]+', text1)
print("URL:", urls)


# 2. Get email id from the sentence
text2 = "My email id is xyz111@gmail.com"
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text2)
print("Email:", emails)


# 3. Find hashtags
text3 = "#Sushant is trending now in the world."
hashtags = re.findall(r'#\w+', text3)
print("Hashtags:", hashtags)


# 4. Find mentions in a sentence
text4 = "@Ajit, please help me"
mentions = re.findall(r'@\w+', text4)
print("Mentions:", mentions)


# 5. Find numbers in a sentence
text5 = "8853147 sq. km of area washed away in floods"
numbers = re.findall(r'\d+', text5)
print("Numbers:", numbers)


# 6. Find punctuations in a sentence
text6 = "Corona virus killed #24506 people. #Corona is un(tolerable)"
punctuations = re.findall(r'[^\w\s]', text6)
print("Punctuations:", punctuations)


# 7. Validate PAN Number (Format: 5 caps letters, 4 digits, 1 cap letter)
text7a = "ABCED3193P"
text7b = "lEcGD012eg"
pan_pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
print("PAN Validity 1:", bool(re.match(pan_pattern, text7a)))
print("PAN Validity 2:", bool(re.match(pan_pattern, text7b)))


# 8. Remove repetitive characters from sentence
text8 = "heyyy this is a verrrry loong texttt"
remove_repeats = re.sub(r'(.)\1+', r'\1', text8)
print("Without repeats:", remove_repeats)


# 9. Find Indian mobile numbers (10 digits + start with 6/7/8/9)
text9 = "9990001796 is a phone number of PMO office"
mobiles = re.findall(r'[6-9]\d{9}', text9)
print("Mobile Numbers:", mobiles)


# 10. Extract words starting with a capital letter
text10 = "Ajit Doval is the best National Security Advisor so far."
capital_words = re.findall(r'\b[A-Z][a-zA-Z]*\b', text10)
print("Capitalized Words:", capital_words)
