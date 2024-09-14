class Book:
    def __init__(self, name, reading_time, book_length, author, genre, sensitivity, 
                 book_prefer, reading_goal, groups, book_interaction, adaptation):
        self.name = name
        self.reading_time = reading_time
        self.book_length = book_length
        self.author = author
        self.genre = genre
        self.sensitivity = sensitivity
        self.book_prefer = book_prefer
        self.reading_goal = reading_goal
        self.groups = groups
        self.book_interaction = book_interaction
        self.adaptation = adaptation

    def __repr__(self):
        return self.name

    # Getters and Setters for reading_time
    def get_reading_time(self, key):
        return self.reading_time.get(key)

    def set_reading_time(self, key, value):
        self.reading_time[key] = value

    # Getters and Setters for book_length
    def get_book_length(self, key):
        return self.book_length.get(key)

    def set_book_length(self, key, value):
        self.book_length[key] = value

    # Getters and Setters for author
    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    # Getters and Setters for genre
    def get_genre(self, key):
        return self.genre.get(key)

    def set_genre(self, key, value):
        self.genre[key] = value

    # Getters and Setters for sensitivity
    def get_sensitivity(self, key):
        return self.sensitivity.get(key)

    def set_sensitivity(self, key, value):
        self.sensitivity[key] = value

    # Getters and Setters for book_prefer
    def get_book_prefer(self, key):
        return self.book_prefer.get(key)

    def set_book_prefer(self, key, value):
        self.book_prefer[key] = value

    # Getters and Setters for reading_goal
    def get_reading_goal(self, key):
        return self.reading_goal.get(key)

    def set_reading_goal(self, key, value):
        self.reading_goal[key] = value

    # Getters and Setters for groups
    def get_groups(self):
        return self.groups

    def add_group(self, group):
        self.groups.append(group)

    def remove_group(self, group):
        self.groups.remove(group)

    # Getters and Setters for book_interaction
    def get_book_interaction(self, key):
        return self.book_interaction.get(key)

    def set_book_interaction(self, key, value):
        self.book_interaction[key] = value

    # Getters and Setters for adaptation
    def get_adaptation(self, key):
        return self.adaptation.get(key)

    def set_adaptation(self, key, value):
        self.adaptation[key] = value


book1 = Book(
    name="book1",
    reading_time={"morning": 3, "afternoon": 4, "evening": 6, "night": 7},
    book_length={"short_stories": False, "novellas": True, "full_length_novels": True},
    author="George Orwell",
    genre={"romance": 2, "adventure": 1, "mystery": 3, "fantasy": 0, "historical": 5,
           "sci-fic": 9, "biography": 0, "horror": 1, "comic": 0, "self-help": 0, "religion": 0},
    sensitivity={"violence": 5, "profanity": 2, "sexual": 1, "none": 3},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": False, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 8, "personal-growth": 3, "cultural-understanding": 5,
                  "research": 6, "philosophy": 2, "educational": 7, "relaxation": 6,
                  "professional-development": 4},
    groups=["Dystopian Readers", "Classic Literature"],
    book_interaction={"reviewing-behaviour": 8, "book-discussions": 9, "social-sharing": 7},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book2 = Book(
    name="book2",
    reading_time={"morning": 6, "afternoon": 5, "evening": 7, "night": 4},
    book_length={"short_stories": True, "novellas": False, "full_length_novels": True},
    author="J.K. Rowling",
    genre={"romance": 0, "adventure": 9, "mystery": 8, "fantasy": 10, "historical": 0,
           "sci-fic": 1, "biography": 0, "horror": 3, "comic": 0, "self-help": 0, "religion": 0},
    sensitivity={"violence": 4, "profanity": 1, "sexual": 0, "none": 5},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": False, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 9, "personal-growth": 4, "cultural-understanding": 6,
                  "research": 3, "philosophy": 2, "educational": 5, "relaxation": 8,
                  "professional-development": 1},
    groups=["Fantasy Lovers", "Young Adult Fiction"],
    book_interaction={"reviewing-behaviour": 9, "book-discussions": 8, "social-sharing": 6},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book3 = Book(
    name="book3",
    reading_time={"morning": 5, "afternoon": 3, "evening": 7, "night": 2},
    book_length={"short_stories": False, "novellas": False, "full_length_novels": True},
    author="Agatha Christie",
    genre={"romance": 1, "adventure": 0, "mystery": 10, "fantasy": 0, "historical": 3,
           "sci-fic": 0, "biography": 2, "horror": 1, "comic": 0, "self-help": 0, "religion": 0},
    sensitivity={"violence": 4, "profanity": 1, "sexual": 2, "none": 3},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": False, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 8, "personal-growth": 3, "cultural-understanding": 5,
                  "research": 6, "philosophy": 2, "educational": 7, "relaxation": 6,
                  "professional-development": 4},
    groups=["Mystery Fans", "Classic Literature"],
    book_interaction={"reviewing-behaviour": 8, "book-discussions": 9, "social-sharing": 7},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book4 = Book(
    name="book4",
    reading_time={"morning": 2, "afternoon": 5, "evening": 8, "night": 4},
    book_length={"short_stories": True, "novellas": True, "full_length_novels": False},
    author="Isaac Asimov",
    genre={"romance": 0, "adventure": 2, "mystery": 1, "fantasy": 3, "historical": 0,
           "sci-fic": 10, "biography": 1, "horror": 0, "comic": 0, "self-help": 0, "religion": 0},
    sensitivity={"violence": 3, "profanity": 2, "sexual": 1, "none": 4},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": True, 
                 "best-seller": False, "award-winnig": False},
    reading_goal={"entertainment": 7, "personal-growth": 4, "cultural-understanding": 6,
                  "research": 8, "philosophy": 2, "educational": 7, "relaxation": 5,
                  "professional-development": 3},
    groups=["Sci-Fi Enthusiasts", "Future Visions"],
    book_interaction={"reviewing-behaviour": 7, "book-discussions": 6, "social-sharing": 5},
    adaptation={"based-movies": False, "no-based-movies": True}
)

book5 = Book(
    name="book5",
    reading_time={"morning": 4, "afternoon": 6, "evening": 7, "night": 3},
    book_length={"short_stories": False, "novellas": False, "full_length_novels": True},
    author="J.R.R. Tolkien",
    genre={"romance": 1, "adventure": 10, "mystery": 2, "fantasy": 10, "historical": 2,
           "sci-fic": 0, "biography": 1, "horror": 0, "comic": 0, "self-help": 0, "religion": 0},
    sensitivity={"violence": 6, "profanity": 1, "sexual": 0, "none": 3},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": False, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 10, "personal-growth": 2, "cultural-understanding": 5,
                  "research": 4, "philosophy": 3, "educational": 4, "relaxation": 7,
                  "professional-development": 2},
    groups=["Epic Fantasy", "High Fantasy"],
    book_interaction={"reviewing-behaviour": 9, "book-discussions": 8, "social-sharing": 6},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book6 = Book(
    name="book6",
    reading_time={"morning": 5, "afternoon": 4, "evening": 6, "night": 7},
    book_length={"short_stories": True, "novellas": False, "full_length_novels": True},
    author="Stephen King",
    genre={"romance": 1, "adventure": 3, "mystery": 7, "fantasy": 3, "historical": 0,
           "sci-fic": 2, "biography": 1, "horror": 10, "comic": 0, "self-help": 0, "religion": 0},
    sensitivity={"violence": 10, "profanity": 8, "sexual": 7, "none": 2},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": True, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 9, "personal-growth": 3, "cultural-understanding": 4,
                  "research": 5, "philosophy": 2, "educational": 3, "relaxation": 8,
                  "professional-development": 1},
    groups=["Horror Aficionados", "Suspense Readers"],
    book_interaction={"reviewing-behaviour": 8, "book-discussions": 7, "social-sharing": 6},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book7 = Book(
    name="book7",
    reading_time={"morning": 2, "afternoon": 5, "evening": 6, "night": 5},
    book_length={"short_stories": True, "novellas": True, "full_length_novels": False},
    author="Jane Austen",
    genre={"romance": 10, "adventure": 1, "mystery": 3, "fantasy": 0, "historical": 8,
           "sci-fic": 0, "biography": 2, "horror": 0, "comic": 0, "self-help": 0, "religion": 1},
    sensitivity={"violence": 2, "profanity": 1, "sexual": 1, "none": 6},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": False, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 8, "personal-growth": 5, "cultural-understanding": 7,
                  "research": 3, "philosophy": 2, "educational": 6, "relaxation": 7,
                  "professional-development": 1},
    groups=["Classic Romance", "Historical Fiction"],
    book_interaction={"reviewing-behaviour": 7, "book-discussions": 6, "social-sharing": 5},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book8 = Book(
    name="book8",
    reading_time={"morning": 3, "afternoon": 7, "evening": 4, "night": 6},
    book_length={"short_stories": False, "novellas": True, "full_length_novels": True},
    author="Margaret Atwood",
    genre={"romance": 2, "adventure": 3, "mystery": 5, "fantasy": 4, "historical": 6,
           "sci-fic": 9, "biography": 1, "horror": 2, "comic": 0, "self-help": 0, "religion": 1},
    sensitivity={"violence": 4, "profanity": 3, "sexual": 5, "none": 4},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": True, 
                 "best-seller": False, "award-winnig": True},
    reading_goal={"entertainment": 6, "personal-growth": 5, "cultural-understanding": 8,
                  "research": 7, "philosophy": 3, "educational": 5, "relaxation": 6,
                  "professional-development": 2},
    groups=["Dystopian Fiction", "Modern Classics"],
    book_interaction={"reviewing-behaviour": 6, "book-discussions": 7, "social-sharing": 5},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book9 = Book(
    name="book9",
    reading_time={"morning": 1, "afternoon": 3, "evening": 5, "night": 7},
    book_length={"short_stories": False, "novellas": True, "full_length_novels": True},
    author="Neil Gaiman",
    genre={"romance": 2, "adventure": 6, "mystery": 5, "fantasy": 9, "historical": 1,
           "sci-fic": 4, "biography": 1, "horror": 7, "comic": 3, "self-help": 0, "religion": 0},
    sensitivity={"violence": 5, "profanity": 3, "sexual": 4, "none": 5},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": False, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 7, "personal-growth": 4, "cultural-understanding": 5,
                  "research": 6, "philosophy": 3, "educational": 5, "relaxation": 8,
                  "professional-development": 2},
    groups=["Urban Fantasy", "Gothic Fiction"],
    book_interaction={"reviewing-behaviour": 7, "book-discussions": 6, "social-sharing": 5},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book10 = Book(
    name="book10",
    reading_time={"morning": 2, "afternoon": 6, "evening": 5, "night": 4},
    book_length={"short_stories": True, "novellas": True, "full_length_novels": False},
    author="F. Scott Fitzgerald",
    genre={"romance": 8, "adventure": 2, "mystery": 4, "fantasy": 0, "historical": 7,
           "sci-fic": 0, "biography": 2, "horror": 0, "comic": 0, "self-help": 0, "religion": 0},
    sensitivity={"violence": 3, "profanity": 2, "sexual": 5, "none": 6},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": False, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 9, "personal-growth": 4, "cultural-understanding": 6,
                  "research": 3, "philosophy": 3, "educational": 4, "relaxation": 7,
                  "professional-development": 2},
    groups=["Classic American Literature", "Jazz Age Fiction"],
    book_interaction={"reviewing-behaviour": 6, "book-discussions": 7, "social-sharing": 5},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book11 = Book(
    name="book11",
    reading_time={"morning": 4, "afternoon": 5, "evening": 6, "night": 3},
    book_length={"short_stories": False, "novellas": False, "full_length_novels": True},
    author="Dan Brown",
    genre={"romance": 2, "adventure": 9, "mystery": 9, "fantasy": 0, "historical": 8,
           "sci-fic": 2, "biography": 1, "horror": 1, "comic": 0, "self-help": 0, "religion": 3},
    sensitivity={"violence": 6, "profanity": 2, "sexual": 2, "none": 3},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": True, 
                 "best-seller": True, "award-winnig": False},
    reading_goal={"entertainment": 8, "personal-growth": 3, "cultural-understanding": 6,
                  "research": 7, "philosophy": 2, "educational": 5, "relaxation": 6,
                  "professional-development": 4},
    groups=["Thriller Enthusiasts", "Historical Mysteries"],
    book_interaction={"reviewing-behaviour": 8, "book-discussions": 7, "social-sharing": 6},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book12 = Book(
    name="book12",
    reading_time={"morning": 3, "afternoon": 4, "evening": 7, "night": 5},
    book_length={"short_stories": True, "novellas": False, "full_length_novels": True},
    author="John Green",
    genre={"romance": 9, "adventure": 4, "mystery": 3, "fantasy": 2, "historical": 1,
           "sci-fic": 1, "biography": 0, "horror": 0, "comic": 0, "self-help": 0, "religion": 0},
    sensitivity={"violence": 2, "profanity": 1, "sexual": 3, "none": 8},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": True, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 9, "personal-growth": 7, "cultural-understanding": 4,
                  "research": 2, "philosophy": 2, "educational": 3, "relaxation": 8,
                  "professional-development": 1},
    groups=["Young Adult Fiction", "Contemporary Romance"],
    book_interaction={"reviewing-behaviour": 7, "book-discussions": 8, "social-sharing": 7},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book13 = Book(
    name="book13",
    reading_time={"morning": 6, "afternoon": 4, "evening": 3, "night": 7},
    book_length={"short_stories": False, "novellas": True, "full_length_novels": True},
    author="George R.R. Martin",
    genre={"romance": 2, "adventure": 10, "mystery": 4, "fantasy": 10, "historical": 5,
           "sci-fic": 1, "biography": 1, "horror": 2, "comic": 0, "self-help": 0, "religion": 1},
    sensitivity={"violence": 9, "profanity": 8, "sexual": 7, "none": 3},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": False, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 10, "personal-growth": 3, "cultural-understanding": 6,
                  "research": 4, "philosophy": 2, "educational": 3, "relaxation": 7,
                  "professional-development": 1},
    groups=["Epic Fantasy", "High Fantasy"],
    book_interaction={"reviewing-behaviour": 8, "book-discussions": 7, "social-sharing": 6},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book14 = Book(
    name="book14",
    reading_time={"morning": 3, "afternoon": 5, "evening": 4, "night": 8},
    book_length={"short_stories": False, "novellas": False, "full_length_novels": True},
    author="J.K. Rowling",
    genre={"romance": 5, "adventure": 8, "mystery": 4, "fantasy": 10, "historical": 2,
           "sci-fic": 1, "biography": 1, "horror": 0, "comic": 0, "self-help": 0, "religion": 0},
    sensitivity={"violence": 3, "profanity": 1, "sexual": 2, "none": 8},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": True, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 9, "personal-growth": 4, "cultural-understanding": 5,
                  "research": 2, "philosophy": 2, "educational": 4, "relaxation": 7,
                  "professional-development": 1},
    groups=["Fantasy Fiction", "Young Adult"],
    book_interaction={"reviewing-behaviour": 9, "book-discussions": 8, "social-sharing": 7},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book15 = Book(
    name="book15",
    reading_time={"morning": 2, "afternoon": 6, "evening": 5, "night": 7},
    book_length={"short_stories": True, "novellas": True, "full_length_novels": False},
    author="Harper Lee",
    genre={"romance": 3, "adventure": 2, "mystery": 4, "fantasy": 0, "historical": 9,
           "sci-fic": 0, "biography": 1, "horror": 0, "comic": 0, "self-help": 0, "religion": 1},
    sensitivity={"violence": 4, "profanity": 1, "sexual": 2, "none": 7},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": False, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 8, "personal-growth": 5, "cultural-understanding": 7,
                  "research": 3, "philosophy": 2, "educational": 4, "relaxation": 6,
                  "professional-development": 2},
    groups=["Classic Literature", "Southern Fiction"],
    book_interaction={"reviewing-behaviour": 7, "book-discussions": 6, "social-sharing": 5},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book16 = Book(
    name="book16",
    reading_time={"morning": 4, "afternoon": 7, "evening": 3, "night": 6},
    book_length={"short_stories": False, "novellas": False, "full_length_novels": True},
    author="Isaac Asimov",
    genre={"romance": 1, "adventure": 7, "mystery": 4, "fantasy": 2, "historical": 0,
           "sci-fic": 10, "biography": 1, "horror": 0, "comic": 0, "self-help": 0, "religion": 0},
    sensitivity={"violence": 3, "profanity": 1, "sexual": 1, "none": 9},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": False, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 6, "personal-growth": 3, "cultural-understanding": 4,
                  "research": 8, "philosophy": 2, "educational": 5, "relaxation": 6,
                  "professional-development": 2},
    groups=["Science Fiction", "Classic Sci-Fi"],
    book_interaction={"reviewing-behaviour": 8, "book-discussions": 6, "social-sharing": 5},
    adaptation={"based-movies": False, "no-based-movies": True}
)

book17 = Book(
    name="book17",
    reading_time={"morning": 5, "afternoon": 3, "evening": 6, "night": 4},
    book_length={"short_stories": True, "novellas": False, "full_length_novels": False},
    author="Margaret Atwood",
    genre={"romance": 4, "adventure": 2, "mystery": 5, "fantasy": 7, "historical": 6,
           "sci-fic": 8, "biography": 2, "horror": 1, "comic": 0, "self-help": 0, "religion": 1},
    sensitivity={"violence": 6, "profanity": 4, "sexual": 3, "none": 7},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": False, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 7, "personal-growth": 5, "cultural-understanding": 6,
                  "research": 3, "philosophy": 3, "educational": 5, "relaxation": 6,
                  "professional-development": 2},
    groups=["Dystopian Fiction", "Speculative Fiction"],
    book_interaction={"reviewing-behaviour": 7, "book-discussions": 5, "social-sharing": 4},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book18 = Book(
    name="book18",
    reading_time={"morning": 1, "afternoon": 2, "evening": 5, "night": 9},
    book_length={"short_stories": False, "novellas": True, "full_length_novels": True},
    author="Agatha Christie",
    genre={"romance": 3, "adventure": 4, "mystery": 10, "fantasy": 0, "historical": 5,
           "sci-fic": 1, "biography": 2, "horror": 2, "comic": 0, "self-help": 0, "religion": 0},
    sensitivity={"violence": 5, "profanity": 1, "sexual": 2, "none": 8},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": False, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 9, "personal-growth": 4, "cultural-understanding": 5,
                  "research": 3, "philosophy": 2, "educational": 4, "relaxation": 7,
                  "professional-development": 2},
    groups=["Classic Mysteries", "Detective Fiction"],
    book_interaction={"reviewing-behaviour": 8, "book-discussions": 7, "social-sharing": 6},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book19 = Book(
    name="book19",
    reading_time={"morning": 7, "afternoon": 4, "evening": 2, "night": 5},
    book_length={"short_stories": False, "novellas": True, "full_length_novels": True},
    author="J.R.R. Tolkien",
    genre={"romance": 1, "adventure": 10, "mystery": 3, "fantasy": 10, "historical": 4,
           "sci-fic": 0, "biography": 1, "horror": 0, "comic": 0, "self-help": 0, "religion": 0},
    sensitivity={"violence": 4, "profanity": 2, "sexual": 1, "none": 8},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": False, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 10, "personal-growth": 4, "cultural-understanding": 5,
                  "research": 3, "philosophy": 2, "educational": 3, "relaxation": 8,
                  "professional-development": 1},
    groups=["High Fantasy", "Epic Fantasy"],
    book_interaction={"reviewing-behaviour": 9, "book-discussions": 7, "social-sharing": 6},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book20 = Book(
    name="book20",
    reading_time={"morning": 2, "afternoon": 3, "evening": 6, "night": 8},
    book_length={"short_stories": True, "novellas": True, "full_length_novels": False},
    author="Orson Scott Card",
    genre={"romance": 2, "adventure": 8, "mystery": 4, "fantasy": 7, "historical": 3,
           "sci-fic": 9, "biography": 1, "horror": 0, "comic": 0, "self-help": 0, "religion": 0},
    sensitivity={"violence": 5, "profanity": 2, "sexual": 2, "none": 7},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": False, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 8, "personal-growth": 4, "cultural-understanding": 5,
                  "research": 7, "philosophy": 2, "educational": 4, "relaxation": 6,
                  "professional-development": 3},
    groups=["Science Fiction", "Young Adult"],
    book_interaction={"reviewing-behaviour": 7, "book-discussions": 6, "social-sharing": 5},
    adaptation={"based-movies": False, "no-based-movies": True}
)

book21 = Book(
    name="book21",
    reading_time={"morning": 6, "afternoon": 5, "evening": 4, "night": 7},
    book_length={"short_stories": False, "novellas": True, "full_length_novels": True},
    author="Stephen King",
    genre={"romance": 2, "adventure": 4, "mystery": 6, "fantasy": 5, "historical": 3,
           "sci-fic": 4, "biography": 1, "horror": 9, "comic": 0, "self-help": 1, "religion": 0},
    sensitivity={"violence": 8, "profanity": 6, "sexual": 5, "none": 3},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": True, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 9, "personal-growth": 4, "cultural-understanding": 3,
                  "research": 2, "philosophy": 2, "educational": 3, "relaxation": 6,
                  "professional-development": 2},
    groups=["Horror Fiction", "Thriller"],
    book_interaction={"reviewing-behaviour": 8, "book-discussions": 7, "social-sharing": 6},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book22 = Book(
    name="book22",
    reading_time={"morning": 4, "afternoon": 6, "evening": 3, "night": 7},
    book_length={"short_stories": True, "novellas": False, "full_length_novels": True},
    author="Dan Brown",
    genre={"romance": 3, "adventure": 10, "mystery": 8, "fantasy": 1, "historical": 8,
           "sci-fic": 2, "biography": 1, "horror": 1, "comic": 0, "self-help": 1, "religion": 2},
    sensitivity={"violence": 6, "profanity": 3, "sexual": 4, "none": 7},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": True, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 8, "personal-growth": 5, "cultural-understanding": 6,
                  "research": 7, "philosophy": 3, "educational": 4, "relaxation": 5,
                  "professional-development": 3},
    groups=["Thriller", "Mystery"],
    book_interaction={"reviewing-behaviour": 7, "book-discussions": 6, "social-sharing": 5},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book23 = Book(
    name="book23",
    reading_time={"morning": 3, "afternoon": 5, "evening": 6, "night": 4},
    book_length={"short_stories": False, "novellas": True, "full_length_novels": True},
    author="Malcolm Gladwell",
    genre={"romance": 1, "adventure": 2, "mystery": 2, "fantasy": 0, "historical": 3,
           "sci-fic": 0, "biography": 9, "horror": 0, "comic": 0, "self-help": 8, "religion": 1},
    sensitivity={"violence": 2, "profanity": 1, "sexual": 1, "none": 8},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": True, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 5, "personal-growth": 8, "cultural-understanding": 6,
                  "research": 7, "philosophy": 4, "educational": 5, "relaxation": 4,
                  "professional-development": 6},
    groups=["Non-Fiction", "Self-Help"],
    book_interaction={"reviewing-behaviour": 6, "book-discussions": 5, "social-sharing": 4},
    adaptation={"based-movies": False, "no-based-movies": True}
)

book24 = Book(
    name="book24",
    reading_time={"morning": 2, "afternoon": 4, "evening": 7, "night": 6},
    book_length={"short_stories": True, "novellas": True, "full_length_novels": False},
    author="Neil Gaiman",
    genre={"romance": 3, "adventure": 6, "mystery": 4, "fantasy": 9, "historical": 2,
           "sci-fic": 4, "biography": 1, "horror": 3, "comic": 2, "self-help": 1, "religion": 1},
    sensitivity={"violence": 4, "profanity": 3, "sexual": 2, "none": 6},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": False, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 8, "personal-growth": 4, "cultural-understanding": 5,
                  "research": 4, "philosophy": 3, "educational": 3, "relaxation": 6,
                  "professional-development": 2},
    groups=["Fantasy Fiction", "Graphic Novels"],
    book_interaction={"reviewing-behaviour": 7, "book-discussions": 6, "social-sharing": 5},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book25 = Book(
    name="book25",
    reading_time={"morning": 5, "afternoon": 4, "evening": 2, "night": 7},
    book_length={"short_stories": True, "novellas": False, "full_length_novels": True},
    author="J.K. Rowling",
    genre={"romance": 5, "adventure": 9, "mystery": 6, "fantasy": 10, "historical": 2,
           "sci-fic": 1, "biography": 1, "horror": 1, "comic": 0, "self-help": 0, "religion": 0},
    sensitivity={"violence": 3, "profanity": 1, "sexual": 2, "none": 9},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": True, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 10, "personal-growth": 3, "cultural-understanding": 4,
                  "research": 1, "philosophy": 2, "educational": 2, "relaxation": 7,
                  "professional-development": 1},
    groups=["Fantasy Fiction", "Young Adult"],
    book_interaction={"reviewing-behaviour": 8, "book-discussions": 7, "social-sharing": 6},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book26 = Book(
    name="book26",
    reading_time={"morning": 4, "afternoon": 7, "evening": 3, "night": 6},
    book_length={"short_stories": False, "novellas": True, "full_length_novels": True},
    author="Tolkien",
    genre={"romance": 3, "adventure": 10, "mystery": 2, "fantasy": 10, "historical": 4,
           "sci-fic": 1, "biography": 2, "horror": 1, "comic": 0, "self-help": 0, "religion": 0},
    sensitivity={"violence": 4, "profanity": 1, "sexual": 1, "none": 8},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": False, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 10, "personal-growth": 3, "cultural-understanding": 4,
                  "research": 3, "philosophy": 2, "educational": 2, "relaxation": 6,
                  "professional-development": 1},
    groups=["High Fantasy", "Epic Fantasy"],
    book_interaction={"reviewing-behaviour": 8, "book-discussions": 7, "social-sharing": 5},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book27 = Book(
    name="book27",
    reading_time={"morning": 2, "afternoon": 6, "evening": 7, "night": 5},
    book_length={"short_stories": True, "novellas": True, "full_length_novels": False},
    author="Isaac Asimov",
    genre={"romance": 2, "adventure": 8, "mystery": 3, "fantasy": 1, "historical": 2,
           "sci-fic": 10, "biography": 1, "horror": 1, "comic": 0, "self-help": 0, "religion": 0},
    sensitivity={"violence": 5, "profanity": 2, "sexual": 1, "none": 8},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": False, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 7, "personal-growth": 4, "cultural-understanding": 5,
                  "research": 8, "philosophy": 3, "educational": 6, "relaxation": 5,
                  "professional-development": 2},
    groups=["Science Fiction", "Classic Sci-Fi"],
    book_interaction={"reviewing-behaviour": 6, "book-discussions": 5, "social-sharing": 4},
    adaptation={"based-movies": False, "no-based-movies": True}
)

book28 = Book(
    name="book28",
    reading_time={"morning": 3, "afternoon": 6, "evening": 5, "night": 4},
    book_length={"short_stories": False, "novellas": True, "full_length_novels": True},
    author="Ray Bradbury",
    genre={"romance": 2, "adventure": 6, "mystery": 3, "fantasy": 8, "historical": 2,
           "sci-fic": 9, "biography": 1, "horror": 5, "comic": 0, "self-help": 0, "religion": 1},
    sensitivity={"violence": 6, "profanity": 3, "sexual": 2, "none": 6},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": False, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 8, "personal-growth": 4, "cultural-understanding": 5,
                  "research": 6, "philosophy": 4, "educational": 5, "relaxation": 6,
                  "professional-development": 2},
    groups=["Dystopian Fiction", "Science Fiction"],
    book_interaction={"reviewing-behaviour": 7, "book-discussions": 6, "social-sharing": 5},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book29 = Book(
    name="book29",
    reading_time={"morning": 3, "afternoon": 5, "evening": 6, "night": 4},
    book_length={"short_stories": False, "novellas": False, "full_length_novels": True},
    author="J.R.R. Tolkien",
    genre={"romance": 2, "adventure": 9, "mystery": 1, "fantasy": 10, "historical": 4,
           "sci-fic": 1, "biography": 0, "horror": 1, "comic": 0, "self-help": 0, "religion": 2},
    sensitivity={"violence": 6, "profanity": 1, "sexual": 1, "none": 8},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": False, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 10, "personal-growth": 3, "cultural-understanding": 4,
                  "research": 2, "philosophy": 3, "educational": 2, "relaxation": 5,
                  "professional-development": 1},
    groups=["Epic Fantasy", "High Fantasy"],
    book_interaction={"reviewing-behaviour": 8, "book-discussions": 7, "social-sharing": 6},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book30 = Book(
    name="book30",
    reading_time={"morning": 2, "afternoon": 4, "evening": 7, "night": 6},
    book_length={"short_stories": True, "novellas": True, "full_length_novels": False},
    author="George R.R. Martin",
    genre={"romance": 4, "adventure": 9, "mystery": 6, "fantasy": 10, "historical": 4,
           "sci-fic": 1, "biography": 0, "horror": 2, "comic": 0, "self-help": 0, "religion": 1},
    sensitivity={"violence": 8, "profanity": 6, "sexual": 7, "none": 3},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": True, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 9, "personal-growth": 4, "cultural-understanding": 6,
                  "research": 3, "philosophy": 2, "educational": 4, "relaxation": 5,
                  "professional-development": 1},
    groups=["Epic Fantasy", "Dark Fantasy"],
    book_interaction={"reviewing-behaviour": 8, "book-discussions": 7, "social-sharing": 6},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book31 = Book(
    name="book31",
    reading_time={"morning": 5, "afternoon": 3, "evening": 6, "night": 4},
    book_length={"short_stories": False, "novellas": True, "full_length_novels": True},
    author="Margaret Atwood",
    genre={"romance": 4, "adventure": 5, "mystery": 7, "fantasy": 2, "historical": 6,
           "sci-fic": 8, "biography": 2, "horror": 1, "comic": 0, "self-help": 1, "religion": 0},
    sensitivity={"violence": 4, "profanity": 3, "sexual": 3, "none": 6},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": False, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 7, "personal-growth": 6, "cultural-understanding": 7,
                  "research": 6, "philosophy": 3, "educational": 5, "relaxation": 4,
                  "professional-development": 2},
    groups=["Dystopian Fiction", "Science Fiction"],
    book_interaction={"reviewing-behaviour": 7, "book-discussions": 6, "social-sharing": 5},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book32 = Book(
    name="book32",
    reading_time={"morning": 4, "afternoon": 6, "evening": 5, "night": 3},
    book_length={"short_stories": True, "novellas": False, "full_length_novels": True},
    author="J.D. Salinger",
    genre={"romance": 6, "adventure": 4, "mystery": 3, "fantasy": 1, "historical": 2,
           "sci-fic": 0, "biography": 2, "horror": 1, "comic": 0, "self-help": 1, "religion": 0},
    sensitivity={"violence": 2, "profanity": 4, "sexual": 3, "none": 8},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": False, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 6, "personal-growth": 7, "cultural-understanding": 5,
                  "research": 2, "philosophy": 3, "educational": 4, "relaxation": 5,
                  "professional-development": 2},
    groups=["Classic Literature", "Modern Classics"],
    book_interaction={"reviewing-behaviour": 6, "book-discussions": 5, "social-sharing": 4},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book33 = Book(
    name="book33",
    reading_time={"morning": 3, "afternoon": 7, "evening": 5, "night": 2},
    book_length={"short_stories": False, "novellas": False, "full_length_novels": True},
    author="Neil Gaiman",
    genre={"romance": 4, "adventure": 6, "mystery": 7, "fantasy": 9, "historical": 2,
           "sci-fic": 3, "biography": 2, "horror": 4, "comic": 0, "self-help": 1, "religion": 0},
    sensitivity={"violence": 5, "profanity": 3, "sexual": 2, "none": 7},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": True, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 9, "personal-growth": 5, "cultural-understanding": 6,
                  "research": 2, "philosophy": 3, "educational": 3, "relaxation": 7,
                  "professional-development": 1},
    groups=["Fantasy Fiction", "Contemporary Fantasy"],
    book_interaction={"reviewing-behaviour": 7, "book-discussions": 6, "social-sharing": 5},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book34 = Book(
    name="book34",
    reading_time={"morning": 6, "afternoon": 5, "evening": 3, "night": 4},
    book_length={"short_stories": True, "novellas": True, "full_length_novels": False},
    author="Stephen King",
    genre={"romance": 3, "adventure": 6, "mystery": 4, "fantasy": 5, "historical": 3,
           "sci-fic": 2, "biography": 1, "horror": 10, "comic": 0, "self-help": 0, "religion": 0},
    sensitivity={"violence": 8, "profanity": 5, "sexual": 7, "none": 4},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": True, 
                 "best-seller": True, "award-winnig": False},
    reading_goal={"entertainment": 8, "personal-growth": 4, "cultural-understanding": 3,
                  "research": 2, "philosophy": 2, "educational": 2, "relaxation": 6,
                  "professional-development": 1},
    groups=["Horror Fiction", "Suspense"],
    book_interaction={"reviewing-behaviour": 8, "book-discussions": 7, "social-sharing": 6},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book35 = Book(
    name="book35",
    reading_time={"morning": 4, "afternoon": 6, "evening": 3, "night": 7},
    book_length={"short_stories": False, "novellas": True, "full_length_novels": True},
    author="Jane Austen",
    genre={"romance": 10, "adventure": 2, "mystery": 3, "fantasy": 1, "historical": 7,
           "sci-fic": 0, "biography": 1, "horror": 0, "comic": 0, "self-help": 0, "religion": 2},
    sensitivity={"violence": 2, "profanity": 1, "sexual": 3, "none": 9},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": False, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 9, "personal-growth": 4, "cultural-understanding": 8,
                  "research": 3, "philosophy": 2, "educational": 3, "relaxation": 7,
                  "professional-development": 1},
    groups=["Romance", "Classic Literature"],
    book_interaction={"reviewing-behaviour": 6, "book-discussions": 5, "social-sharing": 4},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book36 = Book(
    name="book36",
    reading_time={"morning": 2, "afternoon": 4, "evening": 6, "night": 5},
    book_length={"short_stories": True, "novellas": True, "full_length_novels": True},
    author="Agatha Christie",
    genre={"romance": 2, "adventure": 4, "mystery": 10, "fantasy": 1, "historical": 3,
           "sci-fic": 1, "biography": 1, "horror": 2, "comic": 0, "self-help": 0, "religion": 1},
    sensitivity={"violence": 4, "profanity": 2, "sexual": 3, "none": 8},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": False, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 10, "personal-growth": 3, "cultural-understanding": 4,
                  "research": 2, "philosophy": 1, "educational": 2, "relaxation": 5,
                  "professional-development": 1},
    groups=["Mystery", "Crime Fiction"],
    book_interaction={"reviewing-behaviour": 8, "book-discussions": 7, "social-sharing": 6},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book37 = Book(
    name="book37",
    reading_time={"morning": 5, "afternoon": 6, "evening": 4, "night": 2},
    book_length={"short_stories": False, "novellas": True, "full_length_novels": True},
    author="Dan Brown",
    genre={"romance": 2, "adventure": 9, "mystery": 7, "fantasy": 1, "historical": 6,
           "sci-fic": 2, "biography": 1, "horror": 1, "comic": 0, "self-help": 0, "religion": 3},
    sensitivity={"violence": 6, "profanity": 3, "sexual": 4, "none": 7},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": True, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 9, "personal-growth": 4, "cultural-understanding": 5,
                  "research": 7, "philosophy": 3, "educational": 4, "relaxation": 6,
                  "professional-development": 2},
    groups=["Thriller", "Mystery"],
    book_interaction={"reviewing-behaviour": 7, "book-discussions": 6, "social-sharing": 5},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book38 = Book(
    name="book38",
    reading_time={"morning": 3, "afternoon": 5, "evening": 6, "night": 4},
    book_length={"short_stories": True, "novellas": False, "full_length_novels": True},
    author="J.K. Rowling",
    genre={"romance": 6, "adventure": 8, "mystery": 4, "fantasy": 10, "historical": 2,
           "sci-fic": 1, "biography": 1, "horror": 1, "comic": 0, "self-help": 0, "religion": 2},
    sensitivity={"violence": 3, "profanity": 2, "sexual": 2, "none": 9},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": True, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 10, "personal-growth": 3, "cultural-understanding": 4,
                  "research": 2, "philosophy": 2, "educational": 2, "relaxation": 7,
                  "professional-development": 1},
    groups=["Fantasy Fiction", "Young Adult"],
    book_interaction={"reviewing-behaviour": 8, "book-discussions": 7, "social-sharing": 6},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book39 = Book(
    name="book39",
    reading_time={"morning": 4, "afternoon": 6, "evening": 5, "night": 5},
    book_length={"short_stories": True, "novellas": False, "full_length_novels": True},
    author="Isaac Asimov",
    genre={"romance": 2, "adventure": 7, "mystery": 3, "fantasy": 6, "historical": 1,
           "sci-fic": 10, "biography": 1, "horror": 1, "comic": 0, "self-help": 0, "religion": 1},
    sensitivity={"violence": 3, "profanity": 2, "sexual": 1, "none": 10},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": True, 
                 "best-seller": True, "award-winnig": False},
    reading_goal={"entertainment": 8, "personal-growth": 3, "cultural-understanding": 5,
                  "research": 7, "philosophy": 2, "educational": 4, "relaxation": 5,
                  "professional-development": 1},
    groups=["Science Fiction", "Classic Sci-Fi"],
    book_interaction={"reviewing-behaviour": 7, "book-discussions": 6, "social-sharing": 5},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book40 = Book(
    name="book40",
    reading_time={"morning": 3, "afternoon": 4, "evening": 7, "night": 6},
    book_length={"short_stories": False, "novellas": True, "full_length_novels": True},
    author="Margaret Atwood",
    genre={"romance": 3, "adventure": 5, "mystery": 6, "fantasy": 7, "historical": 4,
           "sci-fic": 8, "biography": 2, "horror": 1, "comic": 0, "self-help": 1, "religion": 0},
    sensitivity={"violence": 6, "profanity": 4, "sexual": 5, "none": 5},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": True, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 9, "personal-growth": 5, "cultural-understanding": 7,
                  "research": 4, "philosophy": 3, "educational": 3, "relaxation": 6,
                  "professional-development": 2},
    groups=["Dystopian Fiction", "Speculative Fiction"],
    book_interaction={"reviewing-behaviour": 7, "book-discussions": 7, "social-sharing": 6},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book41 = Book(
    name="book41",
    reading_time={"morning": 5, "afternoon": 5, "evening": 5, "night": 5},
    book_length={"short_stories": False, "novellas": True, "full_length_novels": True},
    author="J.R.R. Tolkien",
    genre={"romance": 4, "adventure": 9, "mystery": 2, "fantasy": 10, "historical": 3,
           "sci-fic": 1, "biography": 1, "horror": 1, "comic": 0, "self-help": 0, "religion": 0},
    sensitivity={"violence": 5, "profanity": 2, "sexual": 2, "none": 9},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": False, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 10, "personal-growth": 4, "cultural-understanding": 6,
                  "research": 3, "philosophy": 2, "educational": 2, "relaxation": 7,
                  "professional-development": 1},
    groups=["Epic Fantasy", "High Fantasy"],
    book_interaction={"reviewing-behaviour": 8, "book-discussions": 7, "social-sharing": 6},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book42 = Book(
    name="book42",
    reading_time={"morning": 6, "afternoon": 6, "evening": 4, "night": 4},
    book_length={"short_stories": True, "novellas": True, "full_length_novels": True},
    author="Haruki Murakami",
    genre={"romance": 7, "adventure": 5, "mystery": 6, "fantasy": 8, "historical": 2,
           "sci-fic": 4, "biography": 1, "horror": 3, "comic": 0, "self-help": 2, "religion": 1},
    sensitivity={"violence": 5, "profanity": 4, "sexual": 6, "none": 5},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": True, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 9, "personal-growth": 5, "cultural-understanding": 6,
                  "research": 4, "philosophy": 4, "educational": 3, "relaxation": 7,
                  "professional-development": 2},
    groups=["Contemporary Fiction", "Magical Realism"],
    book_interaction={"reviewing-behaviour": 7, "book-discussions": 6, "social-sharing": 5},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book43 = Book(
    name="book43",
    reading_time={"morning": 4, "afternoon": 4, "evening": 6, "night": 6},
    book_length={"short_stories": False, "novellas": True, "full_length_novels": True},
    author="C.S. Lewis",
    genre={"romance": 5, "adventure": 8, "mystery": 3, "fantasy": 9, "historical": 2,
           "sci-fic": 1, "biography": 1, "horror": 1, "comic": 0, "self-help": 1, "religion": 3},
    sensitivity={"violence": 4, "profanity": 2, "sexual": 2, "none": 8},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": False, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 9, "personal-growth": 4, "cultural-understanding": 5,
                  "research": 2, "philosophy": 3, "educational": 2, "relaxation": 7,
                  "professional-development": 1},
    groups=["Christian Fiction", "Fantasy"],
    book_interaction={"reviewing-behaviour": 6, "book-discussions": 5, "social-sharing": 4},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book44 = Book(
    name="book44",
    reading_time={"morning": 6, "afternoon": 4, "evening": 5, "night": 5},
    book_length={"short_stories": True, "novellas": True, "full_length_novels": True},
    author="Alice Munro",
    genre={"romance": 5, "adventure": 4, "mystery": 6, "fantasy": 2, "historical": 3,
           "sci-fic": 1, "biography": 3, "horror": 1, "comic": 0, "self-help": 2, "religion": 1},
    sensitivity={"violence": 3, "profanity": 2, "sexual": 4, "none": 9},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": False, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 8, "personal-growth": 5, "cultural-understanding": 6,
                  "research": 2, "philosophy": 2, "educational": 3, "relaxation": 7,
                  "professional-development": 2},
    groups=["Contemporary Fiction", "Short Stories"],
    book_interaction={"reviewing-behaviour": 6, "book-discussions": 5, "social-sharing": 4},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book45 = Book(
    name="book45",
    reading_time={"morning": 3, "afternoon": 5, "evening": 6, "night": 5},
    book_length={"short_stories": True, "novellas": False, "full_length_novels": True},
    author="Ruth Ware",
    genre={"romance": 3, "adventure": 4, "mystery": 9, "fantasy": 2, "historical": 3,
           "sci-fic": 1, "biography": 1, "horror": 1, "comic": 0, "self-help": 1, "religion": 0},
    sensitivity={"violence": 6, "profanity": 3, "sexual": 5, "none": 6},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": True, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 9, "personal-growth": 4, "cultural-understanding": 5,
                  "research": 3, "philosophy": 2, "educational": 2, "relaxation": 6,
                  "professional-development": 1},
    groups=["Thriller", "Mystery"],
    book_interaction={"reviewing-behaviour": 7, "book-discussions": 6, "social-sharing": 5},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book46 = Book(
    name="book46",
    reading_time={"morning": 4, "afternoon": 6, "evening": 4, "night": 5},
    book_length={"short_stories": True, "novellas": False, "full_length_novels": True},
    author="John Green",
    genre={"romance": 8, "adventure": 6, "mystery": 3, "fantasy": 4, "historical": 2,
           "sci-fic": 1, "biography": 1, "horror": 1, "comic": 0, "self-help": 2, "religion": 1},
    sensitivity={"violence": 3, "profanity": 3, "sexual": 4, "none": 9},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": True, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 9, "personal-growth": 5, "cultural-understanding": 4,
                  "research": 2, "philosophy": 2, "educational": 3, "relaxation": 6,
                  "professional-development": 1},
    groups=["Young Adult", "Contemporary Fiction"],
    book_interaction={"reviewing-behaviour": 7, "book-discussions": 6, "social-sharing": 5},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book47 = Book(
    name="book47",
    reading_time={"morning": 5, "afternoon": 4, "evening": 5, "night": 6},
    book_length={"short_stories": False, "novellas": True, "full_length_novels": True},
    author="Chimamanda Ngozi Adichie",
    genre={"romance": 6, "adventure": 5, "mystery": 3, "fantasy": 3, "historical": 7,
           "sci-fic": 1, "biography": 3, "horror": 1, "comic": 0, "self-help": 2, "religion": 1},
    sensitivity={"violence": 4, "profanity": 3, "sexual": 5, "none": 6},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": True, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 8, "personal-growth": 5, "cultural-understanding": 8,
                  "research": 3, "philosophy": 2, "educational": 4, "relaxation": 6,
                  "professional-development": 2},
    groups=["Literary Fiction", "Contemporary Fiction"],
    book_interaction={"reviewing-behaviour": 7, "book-discussions": 6, "social-sharing": 5},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book48 = Book(
    name="book48",
    reading_time={"morning": 6, "afternoon": 6, "evening": 5, "night": 3},
    book_length={"short_stories": False, "novellas": True, "full_length_novels": True},
    author="Tom Robbins",
    genre={"romance": 6, "adventure": 7, "mystery": 4, "fantasy": 8, "historical": 2,
           "sci-fic": 3, "biography": 1, "horror": 1, "comic": 2, "self-help": 1, "religion": 1},
    sensitivity={"violence": 3, "profanity": 4, "sexual": 6, "none": 7},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": False, 
                 "best-seller": True, "award-winnig": False},
    reading_goal={"entertainment": 9, "personal-growth": 4, "cultural-understanding": 5,
                  "research": 2, "philosophy": 3, "educational": 2, "relaxation": 6,
                  "professional-development": 1},
    groups=["Literary Fiction", "Contemporary Fiction"],
    book_interaction={"reviewing-behaviour": 7, "book-discussions": 6, "social-sharing": 5},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book49 = Book(
    name="book49",
    reading_time={"morning": 5, "afternoon": 5, "evening": 5, "night": 5},
    book_length={"short_stories": False, "novellas": True, "full_length_novels": True},
    author="N.K. Jemisin",
    genre={"romance": 4, "adventure": 6, "mystery": 3, "fantasy": 9, "historical": 2,
           "sci-fic": 5, "biography": 1, "horror": 2, "comic": 0, "self-help": 1, "religion": 1},
    sensitivity={"violence": 5, "profanity": 4, "sexual": 4, "none": 7},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": True, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 8, "personal-growth": 4, "cultural-understanding": 6,
                  "research": 3, "philosophy": 3, "educational": 3, "relaxation": 6,
                  "professional-development": 2},
    groups=["Fantasy", "Speculative Fiction"],
    book_interaction={"reviewing-behaviour": 7, "book-discussions": 6, "social-sharing": 5},
    adaptation={"based-movies": True, "no-based-movies": False}
)

book50 = Book(
    name="book50",
    reading_time={"morning": 4, "afternoon": 6, "evening": 4, "night": 6},
    book_length={"short_stories": False, "novellas": True, "full_length_novels": True},
    author="Toni Morrison",
    genre={"romance": 6, "adventure": 4, "mystery": 5, "fantasy": 2, "historical": 8,
           "sci-fic": 1, "biography": 2, "horror": 1, "comic": 0, "self-help": 2, "religion": 1},
    sensitivity={"violence": 6, "profanity": 4, "sexual": 5, "none": 6},
    book_prefer={"recommendation": True, "top-rated": True, "new-release": False, 
                 "best-seller": True, "award-winnig": True},
    reading_goal={"entertainment": 7, "personal-growth": 6, "cultural-understanding": 8,
                  "research": 3, "philosophy": 2, "educational": 3, "relaxation": 5,
                  "professional-development": 2},
    groups=["Literary Fiction", "Historical Fiction"],
    book_interaction={"reviewing-behaviour": 8, "book-discussions": 7, "social-sharing": 5},
    adaptation={"based-movies": True, "no-based-movies": False}
)
