from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample movie data
movies_by_genre = {
    "Action": ["Mad Max", "John Wick", "Die Hard"],
    "Comedy": ["The Hangover", "Superbad", "Step Brothers"],
    "Drama": ["The Shawshank Redemption", "Forrest Gump", "Fight Club"],
    "Sci-Fi": ["Inception", "Interstellar", "The Matrix"]
}

@app.route('/')
def home():
    genres = list(movies_by_genre.keys())
    return render_template('home.html', genres=genres)

@app.route('/pick', methods=['POST'])
def pick_genre():
    selected_genre = request.form.get('genre')
    return redirect(url_for('show_movies', genre=selected_genre))

@app.route('/movies/<genre>')
def show_movies(genre):
    movie_list = movies_by_genre.get(genre, [])
    return render_template('movies.html', genre=genre, movies=movie_list)

if __name__ == '__main__':
    app.run(debug=True)
