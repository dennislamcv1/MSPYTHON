from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

posts = []

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/posts', methods=['GET'])
def get_posts():
    # STEP 3: YOUR CODE HERE
    return jsonify(posts)

@app.route('/posts', methods=['POST'])
def create_post():

    data = request.get_json()

    # STEP 4.2: Your code here
    if not data or 'title' not in data or 'content' not in data:
        return jsonify({'error': 'Missing title or content'}), 400
    
    # STEP 4.3: Your code here
    post_id = len(posts) + 1  # Simple way to generate a new ID
    new_post = {
        'id': post_id,
        'title': data['title'],
        'content': data['content']
    }

    # Add the new post to the posts list
    posts.append(new_post)

    return jsonify(new_post), 201

if __name__ == '__main__':
    app.run(debug=True)