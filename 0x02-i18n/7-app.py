#!/usr/bin/env python3
''' Basic Babel setup'''
from flask import Flask, g, render_template, request
from flask_babel import Babel, _
from babel import support
from typing import Dict
import pytz


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


@babel.timezoneselector
def get_timezone():
    ''' Find timezone parameter in URL parameters '''
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.UnknownTimeZoneError:
            pass

    ''' Find time zone from user settings '''
    if g.user and 'timezone' in g.user:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.UnknownTimeZoneError:
            pass

    ''' Default to UTC '''
    return 'UTC'


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
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000")
