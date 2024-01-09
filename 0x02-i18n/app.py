from flask import Flask, g, render_template, request
from flask_babel import Babel, _
from typing import Dict

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    ''' config class'''
    LANGUAGES = ["en", "fr"]

    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    ''' Locale from URL parameters '''
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    ''' Locale from user settings '''
    if g.user and 'locale' in g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    ''' Locale from request header '''
    header_locale = request.headers.get('Accept-Language')
    if header_locale:
        header_locale = header_locale.split(',')[0].strip()
        if header_locale in app.config['LANGUAGES']:
            return header_locale

    ''' Default locale '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user(user_id):
    '''function to fetch users from mock db'''
    return users.get(user_id)


@app.before_request
def before_request():
    ''' before request function'''
    user_id = request.args.get('login_as')
    if user_id:
        user_id = int(user_id)
        g.user = get_user(user_id)
    else:
        g.user = None

@app.route('/')
def index():
    ''' a simple route'''
    current_time = get_current_time()
    return render_template('5-index.html', current_time=current_time)

def get_current_time():
    '''function to get the current time based on user's timezone'''
    if g.user and 'timezone' in g.user:
        user_timezone = g.user['timezone']
    else:
        user_timezone = app.config['BABEL_DEFAULT_TIMEZONE']

    # Use your preferred method to get the current time in the specified timezone
    # Here, I'm using the datetime module for demonstration purposes
    from datetime import datetime
    from pytz import timezone

    # Replace 'UTC' with the user's inferred timezone
    utc_now = datetime.utcnow().replace(tzinfo=timezone('UTC'))
    local_time = utc_now.astimezone(timezone(user_timezone))

    # Format the time according to the default format
    formatted_time = local_time.strftime("%b %d, %Y, %I:%M:%S %p")

    return formatted_time


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000")
