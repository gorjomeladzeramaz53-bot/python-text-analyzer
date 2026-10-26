def analyze_text(text: str, target_word: str):
    lower_text = text.lower()
    lower_target = target_word.lower()
    
    words = lower_text.split()
    total_words = len(words)
    
    target_count = 0
    for w in words:
        if w == lower_target:
            target_count += 1
            
    longest_word = ""
    for w in words:
        clean_word = w.strip(".,!?;:\"'")
        if len(clean_word) > len(longest_word):
            longest_word = clean_word
            
    return total_words, target_count, longest_word