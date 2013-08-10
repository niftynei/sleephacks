#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import upconnect
import cgi
import logging
import os

# tools for encryption

app_name = "Sleep Hacker"

# your keys go here

app_config = {
    'UP_API_CLIENT_ID': os.environ['UP_API_CLIENT_ID']
    'UP_API_SECRET': os.environ['UP_API_SECRET']
}

class MainHandler(webapp2.RequestHandler):

    def _up_provider(self):
        return upconnect.UPProvider(app_config['UP_API_CLIENT_ID'], app_config['UP_API_SECRET'])

    def _token(self):
        token = self.request.cookies.get('token', None)

        return token

    def get(self):
        
        token = self._token();

        if not token:
            self.redirect('/connect')
            return

        # read the user and display
        up = self._up_provider()
        
        user = up.read(token, 'users/@me')

        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<html><b>Hello %s!</b></html>' % user['data']['first'])


class ConnectHandler(MainHandler):

    def get(self):
        up = self._up_provider()
        redirect = 'http://127.0.0.1:8080/authorize'
        url = up.get_connect_url(redirect, 'basic_read move_read move_write')

        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('''
<html>
<b>Conneting!</b>
<p><a href="%s">click me</a></p>
</html>
''' % url)
        

class AuthorizeHandler(MainHandler):

    def get(self):
        up = self._up_provider()
        code = cgi.escape(self.request.get('code'))
        token = up.get_user_token(code)
        ct = str(token['access_token'])
        
        self.response.headers.add_header('Set-Cookie', 'token=%s' % ct)
        self.redirect('/')



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/connect', ConnectHandler),
    ('/authorize', AuthorizeHandler)
], debug=True)
