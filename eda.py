import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re
from collections import Counter
from util import get_common_words
from wordcloud import WordCloud
import scipy.stats as stats

def get_common_words(text_series, num_words=50):
    all_words = ' '.join(text_series).lower()
    all_words = re.findall(r'\b\w+\b', all_words)
    common_words = Counter(all_words).most_common(num_words)
    return common_words 



df = pd.read_csv('data/train.csv')
df_info = df.info()
df_head = df.head()
df_info, df_head
train_nl_lens = df['question'].apply(lambda x: len(x.split()))
plt.figure(figsize=(12, 6))
plt.hist(train_nl_lens, bins=50, alpha=0.7, label='Train Outputs')
plt.title('Distribution of Natural Language Query Lengths')
plt.xlabel('Number of Words')
plt.ylabel('Frequency')
plt.legend()
plt.show()
train_sql_lens = df['sql'].apply(lambda x: len(x.split()))
plt.figure(figsize=(12, 6))
plt.hist(train_sql_lens, bins=50, alpha=0.7, label='Train Inputs')
plt.title('Distribution of SQL Query Lengths')
plt.xlabel('Number of Words')
plt.ylabel('Frequency')
plt.legend()
plt.show()

df['question_len'] = df['question'].apply(len)
question_len_stats = df['question_len'].describe()
question_len_stats
df['sql_len'] = df['sql'].apply(len)
sql_len_stats = df['sql_len'].describe()
sql_len_stats
dupes = df.duplicated().sum()
dupes
df = df.drop_duplicates()


common_words_question = get_common_words(df['question'])
common_words_question
common_words_sql = get_common_words(df['sql'])
common_words_sql
query_types = df['sql'].str.extract(r'(\bSELECT\b|\bINSERT\b|\bUPDATE\b|\bDELETE\b|\bJOIN\b)', expand=False)
query_type_counts = query_types.value_counts()

print("\nDistribution of SQL Query Types in the Training Set:")
print(query_type_counts)

plt.figure(figsize=(10, 6))
query_type_counts.plot(kind='bar', color='orange')
plt.title('Distribution of SQL Query Types in the Training Set')
plt.xlabel('SQL Query Type')
plt.ylabel('Frequency')
plt.show()
# Identify outliers in input length
input_length_outliers = df['question_len' > 'question_len'.quantile(0.99)]

print(f"Number of input length outliers: {len(input_length_outliers)}")

# Display a few examples of outliers
print("\nExamples of input length outliers:")
print(input_length_outliers.head())

question_wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(df['question']))
sql_wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(df['sql']))
plt.figure(figsize=(15, 7))

plt.subplot(1, 2, 1)
plt.imshow(question_wordcloud, interpolation='bilinear')
plt.title('WordCloud for Questions')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(sql_wordcloud, interpolation='bilinear')
plt.title('WordCloud for SQL Queries')
plt.axis('off')

plt.show()

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.boxplot(df['question_len'], patch_artist=True, boxprops=dict(facecolor='skyblue'))
plt.title('Boxplot of Question Lengths')
plt.ylabel('Length of Questions')
plt.subplot(1, 2, 2)
plt.boxplot(df['sql_len'], patch_artist=True, boxprops=dict(facecolor='lightgreen'))
plt.title('Boxplot of SQL Query Lengths')
plt.ylabel('Length of SQL Queries')

plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
stats.probplot(df['question_len'], dist="norm", plot=plt)
plt.title('Q-Q Plot for Question Lengths')
plt.subplot(1, 2, 2)
stats.probplot(df['sql_len'], dist="norm", plot=plt)
plt.title('Q-Q Plot for SQL Query Lengths')
plt.tight_layout()
plt.show()
