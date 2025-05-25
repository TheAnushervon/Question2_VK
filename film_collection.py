from typing import Dict, Optional
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

class FilmCollection:
    
    def __init__(self) -> None:
       
        self._films: Dict[str, Film] = {}

    def add_film(self, film: Film) -> bool:
        if film.title in self._films:
            print(f"Error: Film with title '{film.title}' already exists in the collection.")
            return False
        self._films[film.title] = film
        print(f"Film '{film.title}' added to the collection.")
        return True

    def remove_film(self, title: str) -> bool:
        if title in self._films:
            del self._films[title]
            print(f"Film '{title}' removed from the collection.")
            return True
        print(f"Error: Film with title '{title}' not found in the collection.")
        return False
    
    def find_film_by_title(self, title: str) -> Optional[Film]:
        return self._films.get(title)

    def list_all_films(self) -> None:
        if not self._films:
            print("The film collection is empty.")
            return
        print("\n--- Film Collection ---")
        for i, film in enumerate(self._films.values(), 1):
            print(f"{i}. {film}")
        print("----------------------")