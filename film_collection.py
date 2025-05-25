from typing import Optional

class Film:
    def __init__(self, title: str, genre: Optional[str] = None, year: Optional[int] = None, director: Optional[str] = None):
        
        if not title:
            raise ValueError("Film title cannot be empty.")
        self.title: str = title
        self.genre: Optional[str] = genre
        self.year: Optional[int] = year
        self.director: Optional[str] = director