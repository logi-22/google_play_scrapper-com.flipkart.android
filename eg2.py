import pandas as pd
from google_play_scraper import Sort, reviews

result, continuation_token = reviews(
    'com.flipkart.android',
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.NEWEST, # defaults to Sort.NEWEST
    # defaults to 100
    count=200,
    #filter_score_with=5 # defaults to None(means all score)
)

print(result)
df=pd.DataFrame(result)
#df.to_csv(f"flipkart_reviews.csv",index=False)
df.to_excel(f"flipkart_reviews2.xlsx",index=False)
print(df)
result_df=pd.read_excel("flipkart_reviews2.xlsx")

#1.distribution of reviews
distributed_reviews=df['score'].value_counts()
print(f"Distributed Reviews:\n",distributed_reviews)

#2.number of upvotes
total_count=df['thumbsUpCount'].sum()
print("\nThe Total number of upvotes\n:",total_count)

#4.longest review
df['content_length']=df['content'].str.len()
longest_review=df.loc[df['content_length'].idxmax()]
print(f"Longest Review:\n",longest_review['content'])

#5.How frequently do users review the app?
df['at']=pd.to_datetime(df['at'])
df['date']=df['at'].dt.date
frequency_of_review=df['date'].value_counts().sort_index()
print(f"Frequency of Review:\n",frequency_of_review)

#6.When are reviews most commonly submitted?
df['hour']=df['at'].dt.hour
most_common_time=df['hour'].value_counts().idxmax()
print(f"Most common time:\n",most_common_time)

#7.What is the overall sentiment of the app?
sentiment=df['score'].mean()
overall_sentiment="Positive" if sentiment>3 else "Negative"
print(f"Overall Sentiment:\n",overall_sentiment)
