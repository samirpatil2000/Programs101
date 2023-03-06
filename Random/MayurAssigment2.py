import pandas as pd

# Read the movie_meta_data.csv file
movie_data = pd.read_csv("movie_meta_data.csv", delimiter="\t")

# Function to group movies by genre
def group_movies_by_genre():
    genres = movie_data["genres"].str.split(", ")
    genre_list = []
    for genre in genres:
        genre_list.extend(genre)
    genre_list = list(set(genre_list))
    movies_by_genre = {genre: [] for genre in genre_list}
    for index, row in movie_data.iterrows():
        for genre in row["genres"].split(", "):
            movies_by_genre[genre].append(row)
    return movies_by_genre

# Function to find the top/bottom n percentile movies according to metascore
def find_movies_by_metascore_percentile(n, top=True):
    movies_by_genre = group_movies_by_genre()
    percentile = int(n * 0.01 * len(movie_data))
    movies_by_percentile = {}
    for genre in movies_by_genre:
        genre_movies = pd.DataFrame(movies_by_genre[genre])
        if top:
            genre_movies = genre_movies.sort_values(by="metascore", ascending=False)
        else:
            genre_movies = genre_movies.sort_values(by="metascore")
        movies_by_percentile[genre] = genre_movies.head(percentile) if top else genre_movies.tail(percentile)
    return movies_by_percentile

# Function to find the top/bottom n percentile movies according to number of IMDb user votes
def find_movies_by_user_votes_percentile(n, top=True):
    movies_by_genre = group_movies_by_genre()
    percentile = int(n * 0.01 * len(movie_data))
    movies_by_percentile = {}
    for genre in movies_by_genre:
        genre_movies = pd.DataFrame(movies_by_genre[genre])
        if top:
            genre_movies = genre_movies.sort_values(by="number of imdb user votes", ascending=False)
        else:
            genre_movies = genre_movies.sort_values(by="number of imdb user votes")
        movies_by_percentile[genre] = genre_movies.head(percentile) if top else genre_movies.tail(percentile)
    return movies_by_percentile


# Find top 10 percentile movies by metascore for each genre
top_metascore_movies = find_movies_by_metascore_percentile(10, top=True)
print(top_metascore_movies)

# Find bottom 10 percentile movies by metascore for each genre
bottom_metascore_movies = find_movies_by_metascore_percentile(10, top=False)
print(bottom_metascore_movies)

# Find top 10 percentile movies by number of IMDb user votes for each genre
top_user_votes_movies = find_movies_by_user_votes_percentile(10, top=True)
print(top_user_votes_movies)

# Find bottom 10 percentile movies by number of IMDb user votes for each genre
bottom_user_votes_movies = find_movies_by_user_votes_percentile(10, top=False)
print(bottom_user_votes_movies)




# 2 ------------------------------------------------------------------------


def get_oscar_winners_by_year(year):
    df = pd.read_csv('movie_meta_data.csv', delimiter='\t')
    oscar_winners = df[df['awards'].str.contains(str(year) + ' Academy Award Winner')]
    return oscar_winners['title'].tolist()

print(get_oscar_winners_by_year(2022))

# 3 ------------------------------------------------------------------------


def get_movies_by_budget(n: int, highest: bool = True):
    """
    Returns a list of n movies with the highest or lowest budget,
    depending on the value of the highest parameter.
    """
    # Load the movie_meta_data.csv file into a DataFrame
    df = pd.read_csv("movie_meta_data.csv")

    # Select the movie_title and budget columns
    df = df[["movie_title", "budget"]]

    # Convert the budget column to a numeric data type
    df["budget"] = pd.to_numeric(df["budget"], errors="coerce")

    # Sort the DataFrame by the budget column in ascending or descending order
    if highest:
        df = df.sort_values(by="budget", ascending=False)
    else:
        df = df.sort_values(by="budget")

    # Select the first n rows of the sorted DataFrame
    df = df.head(n)

    # Return the selected rows as a list of dictionaries
    movies = []
    for i, row in df.iterrows():
        movie = {"movie_title": row["movie_title"], "budget": row["budget"]}
        movies.append(movie)

  
    for movie in movies:
        print(movie)

    return 

get_movies_by_budget()

# 4
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a pandas dataframe
df = pd.read_csv('movie_meta_data.csv')

# Filter out movies with missing IMDb user rating or number of awards
df = df.dropna(subset=['imdb_score', 'awards'])

# Plot the relationship between IMDb user rating and number of awards received
plt.scatter(df['imdb_score'], df['awards'])
plt.xlabel('IMDb user rating')
plt.ylabel('Number of awards received')
plt.title('Relationship between IMDb user rating and number of awards')
plt.show()

# Calculate the correlation between IMDb user rating and number of awards received
corr = df['imdb_score'].corr(df['awards'])
print(f'Correlation between IMDb user rating and number of awards: {corr:.2f}')


# 5
def get_correlation_coeff(movies):
    filtered_df = movies[movies['awards'] != 'unknown'].copy()
    filtered_df['awards'] = filtered_df['awards'].str.split(', ')
    filtered_df['no_of_awards'] = filtered_df['awards'].apply(len)
    
    corr_coeff = filtered_df['imdb user rating'].corr(filtered_df['no_of_awards'])
    
    return corr_coeff



# 6 
import pandas as pd

def get_akas(movie_title, region):
    # Load the movie_meta_data.csv file into a Pandas DataFrame
    df = pd.read_csv("movie_meta_data.csv")
    
    # Filter the rows based on the movie title and region
    mask = (df["title"] == movie_title) & (df["region"] == region)
    filtered_df = df[mask]
    
    # Extract the akas column and convert it to a list
    akas = filtered_df["akas"].tolist()
    
    # Return the list of akas
    return akas


def get_primary_title(movie_title, region):
    # Load the movie_meta_data.csv file into a Pandas DataFrame
    df = pd.read_csv("movie_meta_data.csv")
    
    # Filter the rows based on the movie title and region
    mask = (df["title"] == movie_title) & (df["region"] == region)
    filtered_df = df[mask]
    
    # Extract the akas column and return the first element
    akas = filtered_df["akas"].tolist()
    primary_title = akas[0].split(",")[0]
    
    # Return the primary title
    return primary_title


get_primary_title()


#7  Movies released on, before or after a given year (take year as a parameter) 
import pandas as pd

def movies_by_release_year(year, condition):
    # Load the movie metadata CSV file
    df = pd.read_csv('movie_meta_data.csv')
    
    # Filter the movies based on the given condition
    if condition == 'on':
        filtered_df = df[df['title_year'] == year]
    elif condition == 'before':
        filtered_df = df[df['title_year'] < year]
    elif condition == 'after':
        filtered_df = df[df['title_year'] > year]
    else:
        return "Invalid condition. Please use 'on', 'before' or 'after'"
    
    return filtered_df[['movie_title', 'title_year']]

print(movies_by_release_year(2010, 'on'))

# 8 Which director has made directed most number of oscar winning movies

def director_max_oscar_winners():

    # Load the movie_meta_data.csv file into a pandas dataframe
    df = pd.read_csv('movie_meta_data.csv')

    # Filter the dataframe to include only the rows where the movie has won at least one Oscar
    df = df[df['Oscar_Wins'] > 0]

    # Group the filtered dataframe by director and count the number of unique movies for each director
    director_count = df.groupby('Director')['Movie_Name'].nunique().reset_index()

    # Sort the resulting dataframe in descending order of the count and return the director with the highest count
    most_oscar_director = director_count.sort_values('Movie_Name', ascending=False).iloc[0]['Director']

    print('The director who has directed the most number of Oscar-winning movies is:', most_oscar_director)


director_max_oscar_winners()


# 9 Wrappers

import csv
import json

def wrapper_function(func, args, file_format):
    result = func(*args)
    
    if file_format == "CSV":
        with open("output.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for row in result:
                writer.writerow(row)
    
    elif file_format == "JSON":
        with open("output.json", "w") as file:
            json.dump(result, file)
    
    else:
        return "Invalid file format"
    
    return "Output saved to file"
