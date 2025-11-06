from flask import Flask, render_template

app = Flask(__name__)

# Define routes for each page
@app.route('/')
def home():
    """Renders the home page (Projects)."""
    # Pass 'active_page' to the template for navigation highlighting
    return render_template('projects.html', active_page='projects')

@app.route('/blog')
def blog():
    """Renders the blog page."""
    return render_template('blog.html', active_page='blog')

@app.route('/journey')
def journey():
    """Renders the journey page."""
    return render_template('journey.html', active_page='journey')

if __name__ == '__main__':
    # Note: debug=True is for development only.
    app.run(debug=True)