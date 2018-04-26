"""
based on tutorial : http://www.compjour.org/lessons/flask-single-page/hello-tiny-flask-app/
runs on local test server

made to run as small as possible (in one .py file)
to split python stuff into python and html into html, make a /templates folder
and make a file called home.html
"""

from flask import Flask, render_template, request
import json

# dummy input GET
test_input = 'localhost:8000/?content=明日、4月26日（木）のアニメ「ポケットモンスター サン＆ムーン」は1時間スペシャル！ アニメ豪華2本立てのほか、今夏公開の「劇場版ポケットモンスター みんなの物語」に出演する豪華キャストからのスペシャルメッセージも！ お楽しみに！&timestamp=2018-04-25 22:30:10'

# dummy input POST
test_input = {
    'content': '明日、4月26日（木）のアニメ「ポケットモンスター サン＆ムーン」は1時間スペシャル！ アニメ豪華2本立てのほか、今夏公開の「劇場版ポケットモンスター みんなの物語」に出演する豪華キャストからのスペシャルメッセージも！ お楽しみに！',
    'timestamp': '2018-04-25 22:30:10'
}

# dummy output
test_json = {
        'results': [
            {
                'context': '60%',
                'hashtags': [
                    '#pokemon',
                    '#ポケモン',
                    '#pokemon_go',
                    '#matome'
                ],
                'content': [
                    '限定',
                    'オンライン限定',
                    'ポケットモンスター サン&ムーン',
                    'キャスト',
                    'プレミアムフレーム切手セット',
                    'セット',
                    '記念切手',
                    'ポケモンセンター',
                    '劇場版ポケットモンスター みんなの物語'
                ],
                'time': [
                    '1900',
                    '1250',
                    '1350',
                    '1600']
            }],
        'status': 'success'
    }

# instantiate a Flask app class
app = Flask(__name__)
print("app initiated. name of app is: ", __name__)


def prediction_repr():
    pass


def pretty_error(error_text):
    return render_template('error.html', content=error_text), 400


# TODO: authentication for predictive twitter
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


@app.route("/", methods=["GET", "POST"])
def homepage():
    # get gives you a MultiDict() of everything after the question mark
    if request.method == "GET":
        content = request.args.get('content')
        timestamp = request.args.get('timestamp')

        print(content)
        print(timestamp)

        # dummy return
        if content and timestamp:
            # process stuff here
            return json.dumps(test_json)
        else:
            content = "Error 400: got some problem with your GET inputs. them's not getting in."
            return pretty_error(content)

    # dummy for now
    if request.method == "POST":
        data = request.form
        content = data['content']
        timestamp = data['timestamp']

        # dummy return
        if content and timestamp:
            # process stuff here
            return json.dumps(test_json)
        else:
            content = "Error 400: got some problem with your GET inputs. them's not getting in."
            return pretty_error(content)

    return """Hello
    <p>and</p>
    Goodbye World
    """


if __name__ == '__main__':
    app.run(debug=True, port=8000)