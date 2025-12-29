import pickle
import streamlit as st

# Load movie data and similarity matrix
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.75rem 2rem;
        border-radius: 10px;
        border: none;
        font-size: 1.1rem;
        font-weight: 600;
        transition: all 0.3s ease;
        margin-top: 1rem;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 16px rgba(102, 126, 234, 0.3);
    }
    .movie-card {
        background: linear-gradient(135deg, #667eea22 0%, #764ba222 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 0.75rem 0;
        border-left: 4px solid #667eea;
        transition: all 0.3s ease;
    }
    .movie-card:hover {
        transform: translateX(10px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .movie-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: #667eea;
        margin: 0;
    }
    .header-container {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea11 0%, #764ba211 100%);
        border-radius: 20px;
        margin-bottom: 2rem;
    }
    .subtitle {
        color: #666;
        font-size: 1.1rem;
        margin-top: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="header-container">
        <h1>🎬 Movie Recommender System</h1>
        <p class="subtitle">Discover your next favorite movie based on your preferences</p>
    </div>
""", unsafe_allow_html=True)

# Main content
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    movie_list = movies['title'].values
    selected_movie = st.selectbox(
        "🔍 Type or select a movie from the dropdown",
        movie_list,
        help="Start typing to search for a movie"
    )
    
    if st.button('✨ Show Recommendations'):
        with st.spinner('Finding perfect matches for you...'):
            recommendations = recommend(selected_movie)
            
            st.markdown("---")
            st.markdown("### 🌟 Top 5 Recommendations for You:")
            
            for idx, movie in enumerate(recommendations, 1):
                st.markdown(f"""
                    <div class="movie-card">
                        <p class="movie-title">{idx}. {movie}</p>
                    </div>
                """, unsafe_allow_html=True)
            
            # Add a fun fact or tip
            st.markdown("---")
            st.info("💡 **Tip:** Try selecting different movies to explore various genres and styles!")

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #888; padding: 1rem;">
        <p>Powered by collaborative filtering • Made with ❤️ using Streamlit</p>
    </div>
""", unsafe_allow_html=True)

   





