import requests

__title__ = 'jamendo'
__version__ = '0.0.1'
__author__ = 'Vincent Lark'
__license__ = 'BSD'

class JamendoApi(object):
    """ Jamendo API v3 library """

    def __init__(self, client_id, **kwargs):
        if not client_id:
            raise Exception("You must provide a client_id setting")

        self.client_id = client_id
        self.debug = kwargs['debug'] or False
        self.protocol = kwargs['protocol'] or 'http'
        self.base_url = self.protocol + '://api.jamendo.com/' + (kwargs['version'] or 'v3.0')

    def clean_params(self, params):
        """
        Clean a object params.according to Jamendo policy
         - client_id is set if not specified
         - limit and offset are set if not specified
         - arrays are converted to space-separated strings
        :param {String} The path params.will be used against
        :param {Object} The object params.to clean
        :return {Object} Cleaned object
        """
        return params

    def format_date(self, date):
        """
        Format a Date according to API
        :param {Date} Date to format
        """
        return date.format('%Y-%m-%d')

    def request(self, path, params):
        """
        Main request wrapper
        :param {String} The path to the api endpoint
        :param {Object} A query string object
        :return {Object} The JSON response
        """
        r = requests.get(url=self.base_url, data=params)
        return r.json()

    def track(self, params):
        """
        Wrapper to the /tracks endpoint
        :see http://developer.jamendo.com/v3.0/tracks
        :param {Object} A query string object
        :return {Object} The JSON response
        """
        return self.request('/tracks', params)

    def tracks_file(self, params):
        """
        :see http://developer.jamendo.com/v3.0/tracks/file
        :param {Object} params.A query string object
        :param {Function} callback The request callback(error, response_body)
        :return {Object} The JSON response
        """
        return self.request('/tracks/file', params)

    def albums(self, params):
        """
        :see http://developer.jamendo.com/v3.0/albums
        :param {Object} params.A query string object
        :param {Function} callback The request callback(error, response_body)
        :return {Object} The JSON response
        """
        return self.request('/albums', params)

    def album_tracks(self, params):
        """
        :see http://developer.jamendo.com/v3.0/album/tracks
        :param {Object} params.A query string object
        :param {Function} callback The request callback(error, response_body)
        :return {Object} The JSON response
        """
        return self.request('/album/tracks', params)

    def albums_file(self, params):
        """
        :see http://developer.jamendo.com/v3.0/albums/file
        :param {Object} params.A query string object
        :param {Function} callback The request callback(error, response_body)
        :return {Object} The JSON response
        """
        return self.request('/albums/file', params)

    def albums_musicinfo(self, params):
        """
        :see http://developer.jamendo.com/v3.0/albums/musicinfo
        :param {Object} params.A query string object
        :param {Function} callback The request callback(error, response_body)
        :return {Object} The JSON response
        """
        return self.request('/albums/musicinfo', params)

    def artists(self, params):
        """
        :see http://developer.jamendo.com/v3.0/artists
        :param {Object} params.A query string object
        :param {Function} callback The request callback(error, response_body)
        :return {Object} The JSON response
        """
        return self.request('/artists', params)

    def artist_albums(self, params):
        """
        :see http://developer.jamendo.com/v3.0/artist_albums
        :param {Object} params.A query string object
        :param {Function} callback The request callback(error, response_body)
        :return {Object} The JSON response
        """
        return self.request('/artist/albums', params)

    def artist_tracks(self, params):
        """
        :see http://developer.jamendo.com/v3.0/artist_tracks
        :param {Object} params.A query string object
        :param {Function} callback The request callback(error, response_body)
        :return {Object} The JSON response
        """
        return self.request('/artist/tracks', params)

    def artists_musicinfo(self, params):
        """
        :see http://developer.jamendo.com/v3.0/artists/musicinfo
        :param {Object} params.A query string object
        :param {Function} callback The request callback(error, response_body)
        :return {Object} The JSON response
        """
        return self.request('/artists/musicinfo', params)

    def artists_locations(self, params):
        """
        :see http://developer.jamendo.com/v3.0/artists/locations
        :param {Object} params.A query string object
        :param {Function} callback The request callback(error, response_body)
        :return {Object} The JSON response
        """
        return self.request('/artists/locations', params)

    def concerts(self, params):
        """
        :see http://developer.jamendo.com/v3.0/concerts
        :param {Object} params.A query string object
        :param {Function} callback The request callback(error, response_body)
        :return {Object} The JSON response
        """
        return self.request('/concerts', params)

    def playlists(self, params):
        """
        :see http://developer.jamendo.com/v3.0/playlists
        :param {Object} params.A query string object
        :param {Function} callback The request callback(error, response_body)
        :return {Object} The JSON response
        """
        return self.request('/playlists', params)

    def playlists_tracks(self, params):
        """
        :see http://developer.jamendo.com/v3.0/playlists_tracks
        :param {Object} params.A query string object
        :param {Function} callback The request callback(error, response_body)
        :return {Object} The JSON response
        """
        return self.request('/playlists/tracks', params)

    def playlists_file(self, params):
        """
        :see http://developer.jamendo.com/v3.0/playlists/file
        :param {Object} params.A query string object
        :param {Function} callback The request callback(error, response_body)
        :return {Object} The JSON response
        """
        return self.request('/playlists/file', params)

    def reviews(self, params):
        """
        :see http://developer.jamendo.com/v3.0/reviews
        :param {Object} params.A query string object
        :param {Function} callback The request callback(error, response_body)
        :return {Object} The JSON response
        """
        return self.request('/reviews', params)

    def reviews_albums(self, params):
        """
        :see http://developer.jamendo.com/v3.0/reviews_albums
        :param {Object} params.A query string object
        :param {Function} callback The request callback(error, response_body)
        :return {Object} The JSON response
        """
        return self.request('/reviews/albums', params)

    def radios(self, params):
        """
        :see http://developer.jamendo.com/v3.0/radios
        :param {Object} params.A query string object
        :param {Function} callback The request callback(error, response_body)
        :return {Object} The JSON response
        """
        return self.request('/radios', params)

    def radios_stream(self, params):
        """
        :see http://developer.jamendo.com/v3.0/radios/stream
        :param {Object} params.A query string object
        :param {Function} callback The request callback(error, response_body)
        :return {Object} The JSON response
        """
        return self.request('/radios/stream', params)

    def users(self, params):
        """
        :see http://developer.jamendo.com/v3.0/users
        :param {Object} params.A query string object
        :param {Function} callback The request callback(error, response_body)
        :return {Object} The JSON response
        """
        return self.request('/users', params)

    def users_artists(self, params):
        """
        :see http://developer.jamendo.com/v3.0/users/artists
        :param {Object} params.A query string object
        :param {Function} callback The request callback(error, response_body)
        :return {Object} The JSON response
        """
        return self.request('/users/artists', params)

    def users_albums(self, params):
        """
        :see http://developer.jamendo.com/v3.0/users/albums
        :param {Object} params.A query string object
        :param {Function} callback The request callback(error, response_body)
        :return {Object} The JSON response
        """
        return self.request('/users/albums', params)

    def users_tracks(self, params):
        """
        :see http://developer.jamendo.com/v3.0/users/tracks
        :param {Object} params.A query string object
        :param {Function} callback The request callback(error, response_body)
        :return {Object} The JSON response
        """
        return self.request('/users/tracks', params)

    def users_favorites_artists(self, params):
        """
        :see http://developer.jamendo.com/v3.0/users/artists
        :param {Object} params.A query string object
        :param {Function} callback The request callback(error, response_body)
        :return {Object} The JSON response
        """
        params.relation = 'fan'
        return self.request('/users/artists', params)

    def users_favorites_albums(self, params):
        """
        :see http://developer.jamendo.com/v3.0/users/albums
        :param {Object} params.A query string object
        :param {Function} callback The request callback(error, response_body)
        :return {Object} The JSON response
        """
        params.relation = 'fan'
        return self.request('/users/albums', params)

    def users_favorites_tracks(self, params):
        """
        :see http://developer.jamendo.com/v3.0/users/tracks
        :param {Object} params.A query string object
        :param {Function} callback The request callback(error, response_body)
        :return {Object} The JSON response
        """
        params.relation = 'fan'
        return self.request('/users/tracks', params)

    def autocomplete(self, params):
        """
        :see http://developer.jamendo.com/v3.0/autocomplete
        :param {Object} params.A query string object
        :param {Function} callback The request callback(error, response_body)
        :return {Object} The JSON response
        """
        return self.request('/autocomplete', params)




"""


  var param,
      default_params = {
        limit     : 10,
        offset    : 0,
        format    : 'json',
        client_id : this.client_id,


  object = object || {

  // explicit params
  for (var name in default_params) {
    if (typeof object[name] === 'undefined') {
      object[name] = default_params[name]
    }
  }

  // datebetween params
  if (object.datebetween && util.isArray(object.datebetween) && object.datebetween.length === 2) {

    for (var i = 0 i < 2 i++) {
      // perfect
      if (util.isDate(object.datebetween[i])) {

      // a timestamp (milliseconds)
      } else if (parseInt(object.datebetween[i], 0)) {
        object.datebetween[i] = new Date(object.datebetween[i])

      // an IETF-compliant RFC 2822 timestamps string
      } else {
        object.datebetween[i] = new Date(object.datebetween[i])
      }
    }

    object.datebetween = this.format_date(object.datebetween[0]) + '_' + this.format_date(object.datebetween[1])
  }

  // arrays as strings
  for (var pname in object) {
    if (util.isArray(object[pname])) {
      object[pname] = object[pname].join(' ')
    }
  }

  return object



:param {String} path The path to the api endpoint
:param {Object} params.A query string object
:param {Function} callback The request callback(error, response_body)
:return {Object} The JSON response

  params.= this.clean_params(path, params.|| {})

  var self = this

  var r = request({
    url: this.base_url + path,
    method: 'GET',
    rejectUnauthorized: this.rejectUnauthorized,
    qs: params.
    json: true
  }, function(error, response, body){

    if (error && !response && self.retry) {
      if (self.debug) {
        console.log('network error, retry', error)
      }
      return self.request(path, params)
    }

    if (typeof callback === 'function') {
      callback(error, body)
    }
  })

  return r



Main write request wrapper
:param {String} path The path to the api endpoint
:param {Object} params.A query string object, must contain an access_token member
:param {Function} callback The request callback(error, error_message, warnings)
:return {Object} The JSON response

  params.= params.|| {

  var self = this

  var r = request({
    url: this.base_url + path,
    method: 'POST',
    rejectUnauthorized: this.rejectUnauthorized,
    form: params.
    json: true
  }, function(error, response, body){
    if (error && !response && self.retry) {
      if (self.debug) {
        console.log('network error, retry', error)
      }
      return self.write_request(path, params)
    }

    if (typeof callback === 'function') {
      // http error
      if (error || !response) {
        callback(error, 'network error', null)

      // api error
      } else if (parseInt(response.headers.status, 0) !== 0) {
        callback(response.headers.code, response.headers.error_message, response.headers.warnings)

      // api success ! /me eyebrow
      } else {
        callback(response.headers.code, response.headers.error_message, response.headers.warnings)

      }
    }
  })

  return r





""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def setuser_fan(self, params):
"" "
"" " Use this method to let the user identified by 'userid' become a fan of the artist identified 'artistid' (/users/artists?relation='fan').
"" " Note that if the artist doesn't exist, no error will be raised, but the track will not appear in any read request of api and website.
"" "
:see http://developer.jamendo.com/v3.0/setuser/fan
:param {Object} params.A query string object ( access_token, artist_id are required )
:param {Function} callback The request callback(error, error_message, warnings)
:return {Object} The JSON response
"" "

  return this.write_request('/setuser/fan', params)



def setuser_favorite(self, params):
"" "
"" " Use this method to add a given track to the user's preferites (/users/tracks?relation='preferite') (also called 'Favorites' playlist in Jamendo.com).
"" " Note that if the track doesn't exist, no error will be raised, but the track will not appear in any read request of api and website.
"" "
:see http://developer.jamendo.com/v3.0/setuser/favorite
:param {Object} params.A query string object ( access_token, track_id are required )
:param {Function} callback The request callback(error, error_message, warnings)
:return {Object} The JSON response
"" "

  return this.write_request('/setuser/favorite', params)



def setuser_like(self, params):
"" "
"" " Let this 'userid' like the given 'trackid' (/users/tracks?relation='like').
"" " Note that if the track doesn't exist, no error will be raised, but the track will not appear in any read request of api and website.
"" "
:see http://developer.jamendo.com/v3.0/setuser/like
:param {Object} params.A query string object ( access_token, track_id are required )
:param {Function} callback The request callback(error, error_message, warnings)
:return {Object} The JSON response
"" "

  return this.write_request('/setuser/like', params)



def setuser_dislike(self, params):
"" "
"" " As youtube and many other social web site, on Jamendo is possible to 'like' a track, but also to 'dislike' a track.
"" " This method allow you to such an action.
"" "
:see http://developer.jamendo.com/v3.0/setuser/dislike
:param {Object} params.A query string object ( access_token, track_id are required )
:param {Function} callback The request callback(error, error_message, warnings)
:return {Object} The JSON response
"" "

  return this.write_request('/setuser/dislike', params)




"" " Authorize request wrapper
"" "
"" " The objective of such a request is to ask the user if he agrees to grant some rights to your application.
"" "
:param {Object} params.A query string object
:param {Function} callback The request callback(error, login_url)
:return {Object} The JSON response
"" "

  params.= params.|| {
  params.client_id = this.client_id

  var self = this

  // send authorize request
  var r = request({
    url: this.base_url + '/oauth/authorize',
    method: 'GET',
    rejectUnauthorized: this.rejectUnauthorized,
    qs: parameters
  }, function(error, response, body){
    if (error && !response && self.retry) {
      if (self.debug) {
        console.log('network error, retry', error)
      }
      return self.authorize(params. callback)
    }

    // forward the login url
    callback(null, response.request.href)
  })

  return r



"" " Grant request wrapper
"" "
"" " The main objective of the OAuth2 Grant request is to exchange the authorization code you have received with the OAuth2 Authorize request to get an 'access token'.
"" "
:param {Object} params.A query string object (code is required)
:param {Function} callback The request callback(error, login_url)
:return {Object} The JSON response
"" "

  params.= params.|| {
  params.client_id = this.client_id
  params.client_secret = this.client_secret
  params.grant_type = 'authorization_code'

  if (!params.client_secret) {
    return callback('You must provide a client_secret to the constructor', null)
  }

  if (!params.code) {
    return callback('You must provide a code in params., null)
  }

  var self = this

  // send authorize request
  var r = request({
    url: this.base_url + '/oauth/grant',
    method: 'POST',
    rejectUnauthorized: this.rejectUnauthorized,
    form: params.
    json: true
  }, function(error, response, body){
    if (error && !response && self.retry) {
      if (self.debug) {
        console.log('network error, retry', error)
      }
      return self.grant(params. callback)
    }

    // forward oauth detail
    callback(null, body)
  })

  return r

"""
