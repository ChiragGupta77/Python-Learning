# Repeating letter identifier
text = input("Enter string:").lower()
text_dict = {}
for alphabet in text:
    if alphabet.isalpha():
        if alphabet in text_dict:
            text_dict[alphabet] += 1
        else:
            text_dict[alphabet] = 1
for i in text_dict:
    if text_dict[i] >= 2:
        print(f"Letter '{i}' is repeated {text_dict[i]} times.")