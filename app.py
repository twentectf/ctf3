from flask import Flask, render_template, send_from_directory, make_response, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/robots.txt')
def robots():
    return send_from_directory('static', 'robots.txt')

@app.route('/supersecretadminonlyandonlyadmin.html')
def admin():
    feedback="Sorry, this page is only accessible by admin"
    user_cookie = request.cookies.get('user')
    if user_cookie is None:
        # Set the cookie if it doesn't exist
        response = make_response(render_template('supersecretadminonlyandonlyadmin.html', feedback=feedback))
        response.set_cookie('user', 'c3R1ZGVudA==')
    
    elif user_cookie == 'YWRtaW4=':
        feedback="Twente{4dm1n_C00k1e_Ch4ll3ng3}"
        response = make_response(render_template('supersecretadminonlyandonlyadmin.html', feedback=feedback))

    elif user_cookie == 'c3R1ZGVudA==':
        response = make_response(render_template('supersecretadminonlyandonlyadmin.html', feedback=feedback))
    else:
        # In case of any other value, reset the cookie to 'c3R1ZGVudA=='
        response = make_response(render_template('supersecretadminonlyandonlyadmin.html', feedback=feedback))
        response.set_cookie('user', 'c3R1ZGVudA==')
    return response

if __name__ == '__main__':
    app.run()
