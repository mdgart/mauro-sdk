from src.mauro_sdk.core import APItoSDK
from src.mauro_sdk.movie_sdk import MovieSDK
import unittest
import time

# write tests for MovieSDK app
class TestMovieSDK(unittest.TestCase):

    def setUp(self):
        time.sleep(1) # This is a hack to avoid throttling from mockapi.io
        self.api = MovieSDK("some_api_key")  # mockapi doens't require an api key

    def test_create_movie(self):
        self.assertEqual(
            self.api.create_movie("Test Movie One", "Test Description", "Test Genre")["title"], 
            "Test Movie One"
        )
        self.assertEqual(
            self.api.create_movie("Test Movie Two", "Test Description", "Test Genre")["title"], 
            "Test Movie Two"
        )

    def test_get_all_movies(self):
        self.assertGreater(len(self.api.get_all_movies()), 0)   

    def test_get_movie_by_id(self):
        self.assertEqual(self.api.get_movie_by_id(1)["id"], "1")
        self.assertEqual(self.api.get_movie_by_id(2)["id"], "2")

    def test_update_movie(self):
        self.assertEqual(
            self.api.update_movie(1, title="New Title")["title"], 
            "New Title"
        )
        self.assertEqual(
            self.api.update_movie(1, description="New Description")["description"], 
            "New Description"
        )
        self.assertEqual(
            self.api.update_movie(1, genre="New Genre")["genre"], 
            "New Genre"
        )

    def test_create_quote(self):
        self.assertEqual(
            self.api.create_quote(1, "Test Author", "Test Quote one")["author"], 
            "Test Author"
        )
        self.assertEqual(
            self.api.create_quote(2, "Test Author", "Test Quote two")["quote"], 
            "Test Quote two"
        )

    
    def test_get_quotes_by_movie_id(self):
        self.assertEqual(self.api.get_quotes_by_movie_id(1)[0]["author"], "Test Author")
        self.assertEqual(self.api.get_quotes_by_movie_id(2)[0]["quote"], "Test Quote two")

    def test_delete_movie(self):
        new_movie = self.api.create_movie("Test Movie", "Test Description", "Test Genre")
        self.assertEqual(self.api.delete_movie(int(new_movie["id"]))['id'], new_movie["id"])

    def test_get_all_quotes(self):
        self.assertGreater(len(self.api.get_all_quotes()), 0)

    def test_get_quote_by_id(self):
        self.assertEqual(self.api.get_quote_by_id(1)["id"], "1")

    def test_update_quote(self):
        self.assertEqual(
            self.api.update_quote(1, author="New Author")["author"], 
            "New Author"
        )
        self.assertEqual(
            self.api.update_quote(1, quote="New Quote")["quote"], 
            "New Quote"
        )

    def test_delete_quote(self):
        new_quote = self.api.create_quote(1, "Test Author", "Test Quote")
        self.assertEqual(self.api.delete_quote(int(new_quote["id"]))['id'], new_quote["id"])


# wtite tests for APItoSDK app
class TestAPItoSDK(unittest.TestCase):
    def setUp(self):
        time.sleep(1) # This is a hack to avoid throttling from mockapi.io
        self.api = APItoSDK("some_api_key")  # mockapi doens't require an api key

    def test_create_movie(self):
        self.assertEqual(
            self.api.create("movies", {"title": "Test Movie One", "description": "Test Description", "genre": "Test Genre"})["title"], 
            "Test Movie One"
        )
        self.assertEqual(
            self.api.create("movies", {"title": "Test Movie Two", "description": "Test Description", "genre": "Test Genre"})["title"], 
            "Test Movie Two"
        )

    def test_get_all_movies(self):
        self.assertGreater(len(self.api.get_all("movies")), 0)

    def test_get_movie_by_id(self):
        self.assertEqual(self.api.get_by_id("movie", 1)["id"], "1")
        self.assertEqual(self.api.get_by_id("movie", 2)["id"], "2")

    def test_update_movie(self):
        self.assertEqual(
            self.api.update("movie", 1, {"title": "New Title"})["title"], 
            "New Title"
        )
        self.assertEqual(
            self.api.update("movie", 1, {"description": "New Description"})["description"], 
            "New Description"
        )

    def test_create_quote(self):
        self.assertEqual(
            self.api.create("movie_quotes", {"author": "Test Author", "quote": "Test Quote one"}, 1)["author"], 
            "Test Author"
        )
        self.assertEqual(
            self.api.create("movie_quotes", {"author": "Test Author", "quote": "Test Quote two"}, 2)["quote"], 
            "Test Quote two"
        )

    def test_get_quotes_by_movie_id(self):
        self.assertEqual(self.api.get_by_id("movie_quotes", 1)[0]["author"], "Test Author")
        self.assertEqual(self.api.get_by_id("movie_quotes", 2)[0]["quote"], "Test Quote two")

    def test_delete_movie(self):
        new_movie = self.api.create("movies", {"title": "Test Movie", "description": "Test Description", "genre": "Test Genre"})
        self.assertEqual(self.api.delete("movie", int(new_movie["id"]))['id'], new_movie["id"])

    def test_get_all_quotes(self):
        self.assertGreater(len(self.api.get_all("quotes")), 0)

    def test_get_quote_by_id(self):
        self.assertEqual(self.api.get_by_id("quote", 1)["id"], "1")

    def test_update_quote(self):
        self.assertEqual(
            self.api.update("quote", 1, {"author": "New Author"})["author"], 
            "New Author"
        )
        self.assertEqual(
            self.api.update("quote", 1, {"quote": "New Quote"})["quote"], 
            "New Quote"
        )   

    def test_delete_quote(self):
        new_quote = self.api.create("movie_quotes", {"author": "Test Author", "quote": "Test Quote"}, 1)
        self.assertEqual(self.api.delete("quote", int(new_quote["id"]))['id'], new_quote["id"]) 


if __name__ == '__main__':
    unittest.main()