import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-Us'.format(movie_id))
    data = response.json()
    # st.text(data)
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


movies_list = pickle.load(open("movies_dict.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    similar_movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    titles_list = []
    posters_list = []
    for movie in similar_movies_list:
        movies_id = movies_df.iloc[movie[0]].movie_id
        titles_list.append(movies_df.iloc[movie[0]].title)
        posters_list.append(fetch_poster(movies_id))

    return titles_list, posters_list



movies_df = pd.DataFrame(movies_list)

st.title("Movie Recommender System")

selected_movie = st.selectbox("Choose a movie", movies_df["title"].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])


# 8265bd1679663a7ea12ac168da84d2e8
# https://api.themoviedb.org/3/movie/65?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-Us