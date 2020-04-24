from app import app, db
from app.models import User, Post

# The following function in microblog.py creates a shell context that adds the database 
# instance and models to the shell session:
# will be useful when flask shell command is used as we will not need to make imports of db and User,Post
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}