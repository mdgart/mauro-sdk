from .core import APItoSDK

class MovieSDK(APItoSDK):
    """This class create a SDK for the following API:

    /movie
    /movie/{id}
    /movie/{id}/quote
    /quote
    /quote/{id}

    It inherits from the APItoSDK class, which is a wrapper for the requests library. 
    It has methods for creating, reading, updating and deleting movies and quotes.

    Constructor:
    -----------
    __init__(self, api_key: str) -> None:
        Initializes the SDK with the given api_key.

    Methods:
    --------
    create_movie(title: str, description: str, genre: str) -> dict:
        Creates a new movie with the given title, description, and genre.

    get_all_movies() -> dict:
        Returns a list of all movies.

    get_movie_by_id(id: int) -> dict:
        Returns the movie with the given ID.

    update_movie(id: int, title: str = None, description: str = None, genre: str = None) -> dict:
        Updates the movie with the given ID with the given title, description, and/or genre.

    delete_movie(id: int) -> None:
        Deletes the movie with the given ID.

    get_quotes_by_movie_id(id: int) -> dict:
        Returns a list of quotes for the movie with the given ID.

    create_quote(id: int, author: str, quote: str) -> dict:
        Creates a new quote for the movie with the given ID, with the given author and quote.

    get_all_quotes() -> dict:
        Returns a list of all quotes.

    get_quote_by_id(id: int) -> dict:
        Returns the quote with the given ID.

    update_quote(id: int, author: str = None, quote: str = None) -> dict:
        Updates the quote with the given ID with the given author and/or quote.

    delete_quote(id: int) -> None:
        Deletes the quote with the given ID.
    """



    def create_movie(self, title, description, genre):
        return self.create("movies", {"title": title, 
                                      "description": description, 
                                      "genre": genre})
    
    def get_all_movies(self):
        return self.get_all("movies")
    
    def get_movie_by_id(self, id):
        return self.get_by_id("movie", id)
    
    def update_movie(self, id, title=None, description=None, genre=None):
        return self.update("movie", id, {"title": title, 
                                         "description": description, 
                                         "genre": genre})
    
    def delete_movie(self, id):
        return self.delete("movie", id)
    
    def get_quotes_by_movie_id(self, id):
        return self.get_by_id("movie_quotes", id)   
    
    def create_quote(self, id, author, quote):
        return self.create("movie_quotes", {"author": author, 
                                            "quote": quote}, id)
    
    def get_all_quotes(self):
        return self.get_all("quotes")
    
    def get_quote_by_id(self, id):
        return self.get_by_id("quote", id)

    def update_quote(self, id, author=None, quote=None):
        return self.update("quote", id, {"author": author, 
                                         "quote": quote})

    def delete_quote(self, id):
        return self.delete("quote", id)

    def get_all_quotes(self):
        return self.get_all("quotes")
      