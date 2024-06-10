import pickle
import streamlit as st
import pandas as pd

def recommend(movie):
    # Find the index of the movie
    index = movies[movies['title'] == movie].index[0]
    
    # Adjust index to match similarity matrix size
    index = index if index < len(similarity) else index % len(similarity)
    
    # Calculate the similarity distances
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    # Collect the top 5 recommended movies
    recommended_movies = []
    for i in distances[1:6]:  # Skip the first one as it will be the selected movie itself
        recommended_movies.append(movies.iloc[i[0]].title)
    
    # Return the list of recommended movies
    return recommended_movies

# Load the movies data
movies_dict = pickle.load(open('movie.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Load the similarity data
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Set up the Streamlit app
st.title('Movie Recommender System')

# Create a select box for movie titles
option = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values
)

# Show recommendations when the button is pressed
if st.button('Show Recommendation'):
    recommendations = recommend(option)
    for i in recommendations:
        st.write(i)  # Ensure proper indentation here
