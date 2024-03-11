import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
sns.set_style('darkgrid')
st.set_page_config(layout="wide")

st.title("Spotify Song Analysis 🎧")

st.subheader("Use this Streamlit app to explore about song!")

# Load the data


spotify_file = st.file_uploader('Select Your Local Spotify Song CSV (default provided)')

@st.cache()
def load_file(spotify_file):
    time.sleep(3)
    if spotify_file is not None:
        df = pd.read_csv(spotify_file)
    else:
        df = pd.read_csv('data.csv')
    return(df)

spotify_df = load_file(spotify_file)


if spotify_file is not None:
     spotify_df = pd.read_csv(spotify_file,index_col=0)
else:
    spotify_df = pd.read_csv('data.csv',index_col=0)
    # st.stop()

col1, col2 = st.columns(2)
with col1:
    # Display the first five rows
    st.subheader("First 5 Rows")
    st.write(spotify_df.head(10))
with col2:
    st.subheader("Descriptive Statistics")
    st.write(spotify_df.describe(include='all'))

# selected_features = st.multiselect(
#     label='Select Audio Features', options=spotify_df.columns[:-3]
# )

selected_artist = st.selectbox('Artist:', ['All'] + list(spotify_df['artist'].unique()))

# selected_song_title = st.text_input('Song Title:')
# if selected_song_title:
#     filtered_df = filtered_df[filtered_df['song_title'].str.contains(selected_artist, case=False)]
# Display visualizations

selected_x_var = st.selectbox('What do want the x variable to be?',
     spotify_df.columns[:-3])
selected_y_var = st.selectbox('What about the y?',
     spotify_df.columns[:-3])


if selected_artist != 'All':
    spotify_df = spotify_df[spotify_df['artist'] == selected_artist]


fig, ax = plt.subplots()
ax = sns.scatterplot(x = spotify_df[selected_x_var],y = spotify_df[selected_y_var],
                     hue=spotify_df['target'],style=spotify_df['target'])
plt.title('Scatterplot of {}'.format(selected_artist))
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
st.pyplot(fig)