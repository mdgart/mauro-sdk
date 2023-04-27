BASE_URL = "https://64496f86e7eb3378ca499f9e.mockapi.io"
RESOURCES = {
    "movies": {
        "path": "/movie", 
        "http_methods": ["GET", "POST"], 
        "required_fields": ["title", "description", "genre"]},
    "movie": {
        "path": "/movie/{id}", 
        "http_methods": ["GET", "PUT", "DELETE"]},
    "movie_quotes": {
        "path": "/movie/{id}/quote", 
        "http_methods": ["GET", "POST"], 
        "required_fields": ["author", "quote"]},
    "quotes": {
        "path": "/quote", 
        "http_methods": ["GET"]},
    "quote": {
        "path": "/quote/{id}", 
        "http_methods": ["GET", "PUT", "DELETE"]},
}