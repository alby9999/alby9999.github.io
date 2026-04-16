from flask import Flask, render_template, abort, url_for

# ============================================================
# TODO 1.1: Create the Flask app instance
# Assign it to a variable named 'app'
# ============================================================
app = None  # Replace this line


# ------------------------------------------------------------
# Sample data — a list of blog post dictionaries.
# You will use this in your routes and templates.
# ------------------------------------------------------------
posts = [
    {
        'id': 1,
        'title': 'Getting Started with Python',
        'author': 'Alice',
        'date': '2024-09-10',
        'body': 'Python is a versatile, beginner-friendly language used in web development, data science, and automation. In this post we cover installing Python and running your first script.',
        'tags': ['python', 'beginner']
    },
    {
        'id': 2,
        'title': 'Understanding Flask Routes',
        'author': 'Bob',
        'date': '2024-10-05',
        'body': 'Flask routes map URL paths to Python functions. Using the @app.route decorator you can quickly build multi-page web applications without heavy configuration.',
        'tags': ['flask', 'web']
    },
    {
        'id': 3,
        'title': 'Jinja2 Templates Explained',
        'author': 'Alice',
        'date': '2024-10-20',
        'body': 'Jinja2 is the templating engine bundled with Flask. It lets you embed Python-like expressions inside HTML using {{ }} for variables and {% %} for control structures.',
        'tags': ['flask', 'templates', 'jinja2']
    },
]


# ============================================================
# TODO 1.2: Add the route decorator for the home page ('/')
# above this function.
# ============================================================
def index():
    # TODO 2.1: Replace the plain string return below.
    # Use render_template() to render 'index.html'.
    return "Hello, Flask!"


# ============================================================
# TODO 1.3: Add the route decorator for '/about'
# above this function.
# ============================================================
def about():
    # TODO 2.3: Use render_template() to render 'about.html'.
    return "About this blog."


# ============================================================
# TODO 4.1: Add the route decorator for '/post/<int:post_id>'
# above this function.
# ============================================================
def post(post_id):
    # TODO 4.1a: Find the post in the 'posts' list where post['id'] == post_id.

    # TODO 4.1b: If no post was found, call abort(404)

    # TODO 4.1c: Render 'post.html', passing post=post and title=post['title']
    pass


# ============================================================
# TODO 4.4: Register a 404 error handler using
# @app.errorhandler(404) above this function.
# ============================================================
def not_found(error):
    # Return render_template('404.html') with HTTP status code 404
    pass


# ------------------------------------------------------------
# Entry point — runs the development server with debug mode on.
# Do NOT change this block.
# ------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
