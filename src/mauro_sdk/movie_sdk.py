from .core import APItoSDK

class MovieSDK(APItoSDK):
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
      