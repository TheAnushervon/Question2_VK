from typing import Dict, Iterator, Optional, List 

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

    def __iter__(self) -> Iterator[Film]:
        return FilmCollectionIterator(self._films)

    def __len__(self) -> int:
        return len(self._films)

    def list_all_films(self) -> None:
        if not self._films:
            print("The film collection is empty.")
            return
        print("\n--- Film Collection ---")
        for i, film in enumerate(self):  
            print(f"{i + 1}. {film}")
        print("----------------------")

class FilmCollectionIterator:
    def __init__(self, films_dict: Dict[str, Film]):
        self._film_titles: List[str] = list(films_dict.keys())  
        self._films_dict_ref: Dict[str, Film] = films_dict     
        self._index: int = 0

    def __iter__(self) -> Iterator[Film]:
        return self

    def __next__(self) -> Film:
        if self._index < len(self._film_titles):
            film_title = self._film_titles[self._index]
            film = self._films_dict_ref[film_title]  
            self._index += 1
            return film
        raise StopIteration