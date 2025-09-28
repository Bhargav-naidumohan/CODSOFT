import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample Telugu movie data
data = {
    'title': [
        'RRR', 'Baahubali', 'Pushpa', 'Ala Vaikunthapurramuloo',
        'Sarrainodu', 'Arjun Reddy', 'Geetha Govindam', 'Drushyam'
    ],
    'genre': [
        'Action Drama', 'Action Historical', 'Action Thriller', 'Romantic Comedy',
        'Action Revenge', 'Romantic Drama', 'Romantic Comedy', 'Thriller Drama'
    ]
}

df = pd.DataFrame(data)

# Step 1: Vectorize the genre text
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['genre'])

# Step 2: Compute cosine similarity
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Step 3: Create a reverse mapping of movie titles to indices
indices = pd.Series(df.index, index=df['title'])

# Step 4: Recommendation function
def recommend(title, cosine_sim=cosine_sim):
    if title not in indices:
        return "Movie not found in database."
    
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]  # Top 3 similar movies
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices]

# Example: Recommend movies similar to 'Pushpa'
print("Recommended for 'Pushpa':")
print(recommend('Pushpa'))
