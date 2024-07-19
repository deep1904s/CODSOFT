import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = {
    'User': ['User1', 'User1', 'User2', 'User2', 'User3'],
    'Item': ['Movie1', 'Movie2', 'Movie1', 'Movie3', 'Book1'],
    'Genre': ['Action, Drama', 'Crime, Drama', 'Action, Drama', 'Crime, Drama', 'Fiction'],
    'Rating': [5, 4, 3, 5, 4]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer(tokenizer=lambda x: x.split(', '))
item_vectors = vectorizer.fit_transform(df['Genre'])

item_similarity = cosine_similarity(item_vectors)

def recommend_items_for_all_users(user_data, item_similarity, num_recommend=5):
    all_recommend = {}


    for user in user_data['User'].unique():
        user_interactions = user_data[user_data['User'] == user]
        liked_items = user_interactions[user_interactions['Rating'] >= 4]['Item']
        
        recommendations = []
        for item in liked_items:
            item_idx = df[df['Item'] == item].index[0]
            similar_items = sorted(list(enumerate(item_similarity[item_idx])), key=lambda x: x[1], reverse=True)
            
            for idx, sim_score in similar_items[1:num_recommend+1]:
                recommended_item = df.loc[idx, 'Item']
                if recommended_item not in liked_items and recommended_item not in recommendations:
                    recommendations.append(recommended_item)
        
        all_recommend[user] = recommendations[:num_recommend]
    
    return all_recommend


all_user_recommend= recommend_items_for_all_users(df, item_similarity)

print("RECOMMENDATION SYSTEM")
for user, recommendations in all_user_recommend.items():
    print(f"Recommendations for '{user}':")
    print(recommendations)
    print()