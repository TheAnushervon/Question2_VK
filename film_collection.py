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

    def find_films(self, query: str, search_by: str = "title") -> List[Film]:
        results: List[Film] = []
        query_lower = query.lower()

        for film in self._films.values():
            if search_by == "title" and query_lower in film.title.lower():
                results.append(film)
            elif search_by == "genre" and film.genre and query_lower in film.genre.lower():
                results.append(film)
            elif search_by == "year" and film.year and query == str(film.year):
                results.append(film)
            elif search_by == "director" and film.director and query_lower in film.director.lower():
                results.append(film)
        return results
    
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

if __name__ == "__main__":
   
    cinema_collection = FilmCollection()

   
    film1 = Film(title="Inception", genre="Sci-Fi", year=2010, director="Christopher Nolan")
    film2 = Film(title="The Shawshank Redemption", genre="Drama", year=1994, director="Frank Darabont")
    film3 = Film(title="Pulp Fiction", genre="Crime", year=1994, director="Quentin Tarantino")
    film4 = Film(title="The Dark Knight", genre="Action", year=2008, director="Christopher Nolan")
    film5 = Film(title="Forrest Gump", genre="Drama", year=1994, director="Robert Zemeckis")

    cinema_collection.add_film(film1)
    cinema_collection.add_film(film2)
    cinema_collection.add_film(film3)
    cinema_collection.add_film(film4)
    
  
    cinema_collection.add_film(Film(title="Inception", genre="Thriller"))

   
    print("\nListing all films:")
    cinema_collection.list_all_films()

  
    print("\nIterating through films:")
    for film in cinema_collection:
        print(f"- {film.title}")

   
    print("\nFinding 'Pulp Fiction':")
    found_film = cinema_collection.find_film_by_title("Pulp Fiction")
    if found_film:
        print(f"Found: {found_film}")
    else:
        print("Film not found.")

    print("\nFinding 'Avatar' (should not be found):")
    found_film_non_existent = cinema_collection.find_film_by_title("Avatar")
    if found_film_non_existent:
        print(f"Found: {found_film_non_existent}")
    else:
        print("Film 'Avatar' not found.")

   
    print("\nSearching for films directed by 'Christopher Nolan':")
    nolan_films = cinema_collection.find_films(query="Christopher Nolan", search_by="director")
    if nolan_films:
        for film in nolan_films:
            print(film)
    else:
        print("No films found by that director.")

    print("\nSearching for films with genre 'Drama':")
    drama_films = cinema_collection.find_films(query="Drama", search_by="genre")
    if drama_films:
        for film in drama_films:
            print(film)
    else:
        print("No films found with that genre.")

    print("\nSearching for films from year '1994':")
    films_1994 = cinema_collection.find_films(query="1994", search_by="year")
    if films_1994:
        for film in films_1994:
            print(film)
    else:
        print("No films found from that year.")

   
    print("\nRemoving 'The Dark Knight':")
    cinema_collection.remove_film("The Dark Knight")
    cinema_collection.remove_film("The Dark Knight") 

    
    print("\nListing all films after removal:")
    cinema_collection.list_all_films()

    print(f"\nNumber of films in collection: {len(cinema_collection)}")

  
    try:
        invalid_film = Film(title="")
        cinema_collection.add_film(invalid_film)
    except ValueError as e:
        print(f"\nError creating film: {e}")

    
    cinema_collection.add_film(film5)
    cinema_collection.list_all_films()