from typing import Optional

class Film:
    def __init__(self, title: str, genre: Optional[str] = None, year: Optional[int] = None, director: Optional[str] = None):
        
        if not title:
            raise ValueError("Film title cannot be empty.")
        self.title: str = title
        self.genre: Optional[str] = genre
        self.year: Optional[int] = year
        self.director: Optional[str] = director
    
    def __str__(self) -> str:
        details = [f"Title: {self.title}"]
        if self.genre:
            details.append(f"Genre: {self.genre}")
        if self.year:
            details.append(f"Year: {self.year}")
        if self.director:
            details.append(f"Director: {self.director}")
        return ", ".join(details)

    def __repr__(self) -> str:
        return f"Film(title='{self.title}', genre='{self.genre}', year={self.year}, director='{self.director}')"