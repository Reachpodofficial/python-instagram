class Image(object):
    
    def __init__(self, url, width, height):
        self.url = url
        self.height = height
        self.width = width

class Media(object):

    def __init__(self, id=None, **kwargs):
        self.id = id
        for key,value in kwargs.iteritems():
            setattr(self, key, value)
    
    def get_high_resolution_url(self):
        return self.images['high_resolution'].url
    
    @classmethod
    def object_from_dictionary(cls, entry):
        new_media = Media(id=entry['id'])
        
        new_media.user = User.object_from_dictionary(entry['user'])
        new_media.images = {}
        for version,version_info in entry['images'].iteritems():
            new_media.images[version] = Image(**version_info)

        new_media.user_has_liked = entry['user_has_liked']
        new_media.like_count = entry['like_count']
        
        new_media.comments = []
        for comment in entry['comments']:
            new_media.comments.append(Comment.object_from_dictionary(comment))

        new_media.created_time = entry['created_time']

        if entry['location']:
            new_media.location = Location.object_from_dictionary(entry['location'])

        new_media.link = entry['link']
        new_media.created_time = entry['created_time']

        return new_media

class Tag(object):
    def __init__(self, name, **kwargs):
        self.name = name
        for key,value in kwargs.iteritems():
            setattr(self, key, value)
        
    @classmethod
    def object_from_dictionary(cls, entry):
        return cls(**entry)

    def __str__(self):
        return "Tag %s" % self.name

class Comment(object):
    def __init__(self, *args, **kwargs):
        for key,value in kwargs.iteritems():
            setattr(self, key, value)

    @classmethod
    def object_from_dictionary(cls, entry):
        user = User.object_from_dictionary(entry['from'])
        message = entry['message']
        created_at = entry['created_time']
        id = entry['id']
        return Comment(id, user, message, created_at)

    def __unicode__(self):
        print "%s said \"%s\"" % (self.user.username, self.message)

class Point(object):
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

class Location(object):
    def __init__(self, id, *args, **kwargs):
        self.id = id
        for key,value in kwargs.iteritems():
            setattr(self, key, value)

    @classmethod
    def object_from_dictionary(cls, entry):
        point = None
        if entry['latitude']:
            point = Point(entry['latitude'],
                          entry['longitude'])
        location = cls(entry['id'],
                       point,
                       name=entry['name'])
        return location
         
class User(object):

    def __init__(self, id, *args, **kwargs):
        self.id = id
        for key,value in kwargs.iteritems():
            setattr(self, key, value)

    @classmethod
    def object_from_dictionary(cls, entry):
        new_user = cls(**entry)
        return new_user

    def __str__(self):
        return "User %s" % self.username

        

