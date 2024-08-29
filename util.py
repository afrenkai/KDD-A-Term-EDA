from collections import Counter
import re
def get_common_words(text_series, num_words=50):
    all_words = ' '.join(text_series).lower()
    all_words = re.findall(r'\b\w+\b', all_words)
    common_words = Counter(all_words).most_common(num_words)
    return common_words