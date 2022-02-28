class Sources:
    """
    class that defines news sources objects 
    """
    def __init__(self,id,name, description, category, url, country,author):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.url = url
        self.country = country
        self.author = author

class Articles:
    """
    class that defines news article objects
    """
    def __init__(self, title, description, url, urlToImage, publishedAt):
        self.title = title
        self.description =description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
    

