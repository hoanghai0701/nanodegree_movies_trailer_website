class Movie(object):
    """
    This class represents movie object.
    
    Attributes:
        title (str): Title of the movie
        story_line (str): A short description for the movie
        poster_image_url (str): An URL of the poster image
        trailer_youtube_url (str): An URL of the youtube trailer
    """
    def __init__(self, title, story_line, poster_img_url, trailer_youtube_url):
        self.title = title
        self.story_line = story_line
        self.poster_image_url = poster_img_url
        self.trailer_youtube_url = trailer_youtube_url
