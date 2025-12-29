import pickle
import streamlit as st

movies = pickle.load(open('mov_rec.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

def recommendation(movie_title, top_n=5):
    # Match movie title (case-insensitive)
    matches = movies[
        movies['title'].str.lower() == movie_title.strip().lower()
    ]
    if matches.empty:
        return ["Movie not found"]

    index = matches.index[0]
    # Sort movies by similarity score (highest first)
    distances = sorted(
        list(enumerate(similarity[index])),
        key=lambda x: x[1],
        reverse=True
    )
    # Ensure we don't exceed dataset size
    top_n = min(top_n, len(distances) - 1)

    # Return top N recommended movie titles
    return [
        movies.iloc[i[0]]['title']
        for i in distances[1:top_n+1]
    ]


