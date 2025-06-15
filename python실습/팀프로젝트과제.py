import re

def extract_drug_names(text):
    possible_names = re.findall(r'[A-Z][a-zA-Z0-9\-]{2,}', text)  # 예시: "Tylenol", "Ibuprofen-200"
    return list(set(possible_names))  # 중복 제거
