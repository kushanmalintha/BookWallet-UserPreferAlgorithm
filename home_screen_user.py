class User:
    def __init__(self, name, reading_time, book_length, authors, genre, sensitivity, 
                 book_prefer, reading_goal, groups, book_interaction, 
                 adaptation, reading_habit):
        self.name = name
        self.reading_time = reading_time
        self.book_length = book_length
        self.authors = authors
        self.genre = genre
        self.sensitivity = sensitivity
        self.book_prefer = book_prefer
        self.reading_goal = reading_goal
        self.groups = groups
        self.book_interaction = book_interaction
        self.adaptation = adaptation
        self.reading_habit = reading_habit

    def __repr__(self):
        return self.name

    # Getter and Setter for Reading Time
    def set_reading_time(self, key, value):
        self.reading_time[key] = value

    def get_reading_time(self, key):
        return self.reading_time.get(key)

    # Getter and Setter for Book Length
    def set_book_length(self, key, value):
        self.book_length[key] = value

    def get_book_length(self, key):
        return self.book_length.get(key)

    # Getter and Setter for Authors
    def set_authors(self, authors):
        self.authors = authors

    def get_authors(self):
        return self.authors

    # Getter and Setter for Genre
    def set_genre(self, key, value):
        self.genre[key] = value

    def get_genre(self, key):
        return self.genre.get(key)

    # Getter and Setter for Sensitivity
    def set_sensitivity(self, key, value):
        self.sensitivity[key] = value

    def get_sensitivity(self, key):
        return self.sensitivity.get(key)

    # Getter and Setter for Book Preferences
    def set_book_prefer(self, key, value):
        self.book_prefer[key] = value

    def get_book_prefer(self, key):
        return self.book_prefer.get(key)

    # Getter and Setter for Reading Goals
    def set_reading_goal(self, key, value):
        self.reading_goal[key] = value

    def get_reading_goal(self, key):
        return self.reading_goal.get(key)

    # Getter and Setter for Groups
    def set_groups(self, groups):
        self.groups = groups

    def get_groups(self):
        return self.groups

    # Getter and Setter for Book Interaction
    def set_book_interaction(self, key, value):
        self.book_interaction[key] = value

    def get_book_interaction(self, key):
        return self.book_interaction.get(key)

    # Getter and Setter for Adaptation
    def set_adaptation(self, key, value):
        self.adaptation[key] = value

    def get_adaptation(self, key):
        return self.adaptation.get(key)

    # Getter and Setter for Reading Habit
    def set_reading_habit(self, key, value):
        self.reading_habit[key] = value

    def get_reading_habit(self, key):
        return self.reading_habit.get(key)


user1 = User(
    name = "user1",
    reading_time={"morning": 5, "afternoon": 3, "evening": 2, "night": 6},
    book_length={"short_stories": 4, "novellas": 2, "full_length_novels": 4},
    authors=["J.K. Rowling", "George R.R. Martin", "Stephen King", "Agatha Christie", "J.R.R. Tolkien"],
    genre={"romance": 3, "adventure": 8, "mystery": 5, "fantasy": 9, "historical": 2, "sci-fic": 7,
           "biography": 2, "horror": 1, "comic": 1, "self-help": 3, "religion": 2},
    sensitivity={"violence": 5, "profanity": 4, "sexual": 3, "none": 2},
    book_prefer={"recommendation": 8, "top-rated": 7, "new-release": 6, "best-seller": 7, "award-winnig": 5},
    reading_goal={"entertainment": 9, "personal-growth": 6, "cultural-understanding": 4, "research": 3,
                  "philosophy": 2, "educational": 3, "relaxation": 8, "professional-development": 2},
    groups=["Fantasy", "Adventure"],
    book_interaction={"reviewing-behaviour": 6, "book-discussions": 5, "social-sharing": 4},
    adaptation={"based-movies": 7, "no-based-movies": 3},
    reading_habit={"daily": 7, "weekly": 2, "monthly": 1}
)

user2 = User(
    name = "user2",
    reading_time={"morning": 2, "afternoon": 4, "evening": 6, "night": 3},
    book_length={"short_stories": 3, "novellas": 4, "full_length_novels": 3},
    authors=["Stephen King"],
    genre={"romance": 5, "adventure": 6, "mystery": 7, "fantasy": 4, "historical": 3, "sci-fic": 5,
           "biography": 2, "horror": 8, "comic": 1, "self-help": 2, "religion": 2},
    sensitivity={"violence": 6, "profanity": 5, "sexual": 6, "none": 3},
    book_prefer={"recommendation": 5, "top-rated": 8, "new-release": 6, "best-seller": 9, "award-winnig": 7},
    reading_goal={"entertainment": 8, "personal-growth": 5, "cultural-understanding": 3, "research": 2,
                  "philosophy": 3, "educational": 2, "relaxation": 7, "professional-development": 3},
    groups=["Horror", "Thriller"],
    book_interaction={"reviewing-behaviour": 7, "book-discussions": 6, "social-sharing": 6},
    adaptation={"based-movies": 8, "no-based-movies": 2},
    reading_habit={"daily": 5, "weekly": 4, "monthly": 1}
)

user3 = User(
    name = "user3",
    reading_time={"morning": 4, "afternoon": 5, "evening": 3, "night": 4},
    book_length={"short_stories": 5, "novellas": 3, "full_length_novels": 2},
    authors=["George R.R. Martin"],
    genre={"romance": 2, "adventure": 7, "mystery": 5, "fantasy": 9, "historical": 4, "sci-fic": 3,
           "biography": 1, "horror": 2, "comic": 1, "self-help": 1, "religion": 1},
    sensitivity={"violence": 7, "profanity": 6, "sexual": 7, "none": 3},
    book_prefer={"recommendation": 6, "top-rated": 8, "new-release": 5, "best-seller": 7, "award-winnig": 4},
    reading_goal={"entertainment": 9, "personal-growth": 4, "cultural-understanding": 5, "research": 2,
                  "philosophy": 2, "educational": 2, "relaxation": 6, "professional-development": 3},
    groups=["Fantasy", "Adventure"],
    book_interaction={"reviewing-behaviour": 5, "book-discussions": 4, "social-sharing": 3},
    adaptation={"based-movies": 9, "no-based-movies": 1},
    reading_habit={"daily": 6, "weekly": 3, "monthly": 1}
)

user4 = User(
    name = "user4",
    reading_time={"morning": 3, "afternoon": 5, "evening": 4, "night": 6},
    book_length={"short_stories": 2, "novellas": 4, "full_length_novels": 4},
    authors=["Agatha Christie", "Arthur Conan Doyle", "Edgar Allan Poe", "J.D. Salinger", "Ray Bradbury"],
    genre={"romance": 7, "adventure": 4, "mystery": 9, "fantasy": 2, "historical": 3, "sci-fic": 1,
           "biography": 2, "horror": 2, "comic": 1, "self-help": 2, "religion": 1},
    sensitivity={"violence": 4, "profanity": 3, "sexual": 2, "none": 1},
    book_prefer={"recommendation": 7, "top-rated": 6, "new-release": 5, "best-seller": 8, "award-winnig": 4},
    reading_goal={"entertainment": 7, "personal-growth": 4, "cultural-understanding": 3, "research": 2,
                  "philosophy": 2, "educational": 3, "relaxation": 6, "professional-development": 2},
    groups=["Mystery", "Classic"],
    book_interaction={"reviewing-behaviour": 6, "book-discussions": 5, "social-sharing": 4},
    adaptation={"based-movies": 6, "no-based-movies": 4},
    reading_habit={"daily": 4, "weekly": 5, "monthly": 3}
)

user5 = User(
    name = "user5",
    reading_time={"morning": 2, "afternoon": 3, "evening": 7, "night": 5},
    book_length={"short_stories": 3, "novellas": 3, "full_length_novels": 6},
    authors=["John Grisham", "Dan Brown", "Michael Connelly", "James Patterson", "Lee Child"],
    genre={"romance": 6, "adventure": 5, "mystery": 7, "fantasy": 4, "historical": 3, "sci-fic": 6,
           "biography": 3, "horror": 3, "comic": 2, "self-help": 4, "religion": 2},
    sensitivity={"violence": 5, "profanity": 4, "sexual": 5, "none": 3},
    book_prefer={"recommendation": 6, "top-rated": 8, "new-release": 7, "best-seller": 9, "award-winnig": 6},
    reading_goal={"entertainment": 8, "personal-growth": 5, "cultural-understanding": 4, "research": 3,
                  "philosophy": 2, "educational": 2, "relaxation": 7, "professional-development": 3},
    groups=["Thriller", "Legal Drama"],
    book_interaction={"reviewing-behaviour": 7, "book-discussions": 6, "social-sharing": 5},
    adaptation={"based-movies": 7, "no-based-movies": 3},
    reading_habit={"daily": 5, "weekly": 3, "monthly": 2}
)

user6 = User(
    name = "user6",
    reading_time={"morning": 4, "afternoon": 6, "evening": 5, "night": 3},
    book_length={"short_stories": 2, "novellas": 5, "full_length_novels": 3},
    authors=["Margaret Atwood", "Neil Gaiman", "Isabel Allende", "Chimamanda Ngozi Adichie", "Salman Rushdie"],
    genre={"romance": 4, "adventure": 5, "mystery": 6, "fantasy": 7, "historical": 4, "sci-fic": 5,
           "biography": 4, "horror": 1, "comic": 1, "self-help": 3, "religion": 2},
    sensitivity={"violence": 3, "profanity": 2, "sexual": 3, "none": 5},
    book_prefer={"recommendation": 8, "top-rated": 6, "new-release": 7, "best-seller": 5, "award-winnig": 8},
    reading_goal={"entertainment": 6, "personal-growth": 7, "cultural-understanding": 8, "research": 5,
                  "philosophy": 3, "educational": 4, "relaxation": 5, "professional-development": 3},
    groups=["Contemporary", "Historical Fiction"],
    book_interaction={"reviewing-behaviour": 5, "book-discussions": 7, "social-sharing": 6},
    adaptation={"based-movies": 5, "no-based-movies": 5},
    reading_habit={"daily": 6, "weekly": 2, "monthly": 2}
)

user7 = User(
    name = "user7",
    reading_time={"morning": 6, "afternoon": 4, "evening": 3, "night": 2},
    book_length={"short_stories": 4, "novellas": 3, "full_length_novels": 3},
    authors=["J.R.R. Tolkien", "C.S. Lewis", "L.E. Modesitt Jr.", "Brandon Sanderson", "Patrick Rothfuss"],
    genre={"romance": 5, "adventure": 8, "mystery": 3, "fantasy": 9, "historical": 2, "sci-fic": 6,
           "biography": 2, "horror": 1, "comic": 1, "self-help": 2, "religion": 1},
    sensitivity={"violence": 4, "profanity": 3, "sexual": 2, "none": 7},
    book_prefer={"recommendation": 7, "top-rated": 8, "new-release": 5, "best-seller": 6, "award-winnig": 5},
    reading_goal={"entertainment": 9, "personal-growth": 3, "cultural-understanding": 2, "research": 1,
                  "philosophy": 1, "educational": 2, "relaxation": 7, "professional-development": 2},
    groups=["Fantasy", "Epic Fantasy"],
    book_interaction={"reviewing-behaviour": 4, "book-discussions": 3, "social-sharing": 2},
    adaptation={"based-movies": 9, "no-based-movies": 1},
    reading_habit={"daily": 5, "weekly": 3, "monthly": 2}
)

user8 = User(
    name = "user8",
    reading_time={"morning": 5, "afternoon": 4, "evening": 3, "night": 6},
    book_length={"short_stories": 6, "novellas": 2, "full_length_novels": 2},
    authors=["Stephen King", "Clive Barker", "Anne Rice", "H.P. Lovecraft", "Paul Tremblay"],
    genre={"romance": 2, "adventure": 3, "mystery": 5, "fantasy": 4, "historical": 3, "sci-fic": 2,
           "biography": 1, "horror": 8, "comic": 2, "self-help": 1, "religion": 1},
    sensitivity={"violence": 7, "profanity": 5, "sexual": 6, "none": 2},
    book_prefer={"recommendation": 4, "top-rated": 5, "new-release": 6, "best-seller": 3, "award-winnig": 4},
    reading_goal={"entertainment": 5, "personal-growth": 2, "cultural-understanding": 1, "research": 1,
                  "philosophy": 1, "educational": 1, "relaxation": 4, "professional-development": 1},
    groups=["Horror", "Gothic Fiction"],
    book_interaction={"reviewing-behaviour": 3, "book-discussions": 2, "social-sharing": 1},
    adaptation={"based-movies": 8, "no-based-movies": 2},
    reading_habit={"daily": 4, "weekly": 2, "monthly": 3}
)

user9 = User(
    name = "user9",
    reading_time={"morning": 2, "afternoon": 3, "evening": 7, "night": 5},
    book_length={"short_stories": 3, "novellas": 3, "full_length_novels": 6},
    authors=["George R.R. Martin", "J.K. Rowling", "Patrick Rothfuss", "J.R.R. Tolkien", "Terry Pratchett"],
    genre={"romance": 6, "adventure": 7, "mystery": 5, "fantasy": 9, "historical": 4, "sci-fic": 5,
           "biography": 3, "horror": 1, "comic": 2, "self-help": 4, "religion": 2},
    sensitivity={"violence": 5, "profanity": 4, "sexual": 5, "none": 3},
    book_prefer={"recommendation": 8, "top-rated": 7, "new-release": 6, "best-seller": 9, "award-winnig": 6},
    reading_goal={"entertainment": 8, "personal-growth": 5, "cultural-understanding": 4, "research": 3,
                  "philosophy": 2, "educational": 2, "relaxation": 7, "professional-development": 3},
    groups=["Fantasy", "Epic Fantasy"],
    book_interaction={"reviewing-behaviour": 6, "book-discussions": 5, "social-sharing": 4},
    adaptation={"based-movies": 7, "no-based-movies": 3},
    reading_habit={"daily": 5, "weekly": 3, "monthly": 2}
)

user10 = User(
    name = "user10",
    reading_time={"morning": 3, "afternoon": 6, "evening": 5, "night": 4},
    book_length={"short_stories": 4, "novellas": 2, "full_length_novels": 4},
    authors=["Suzanne Collins", "Veronica Roth", "Dystopian Fiction Author", "Margaret Atwood", "Ally Condie"],
    genre={"romance": 5, "adventure": 6, "mystery": 4, "fantasy": 4, "historical": 3, "sci-fic": 7,
           "biography": 3, "horror": 2, "comic": 2, "self-help": 3, "religion": 2},
    sensitivity={"violence": 4, "profanity": 3, "sexual": 4, "none": 4},
    book_prefer={"recommendation": 7, "top-rated": 6, "new-release": 5, "best-seller": 8, "award-winnig": 5},
    reading_goal={"entertainment": 7, "personal-growth": 4, "cultural-understanding": 3, "research": 2,
                  "philosophy": 2, "educational": 2, "relaxation": 5, "professional-development": 3},
    groups=["Dystopian", "Science Fiction"],
    book_interaction={"reviewing-behaviour": 5, "book-discussions": 4, "social-sharing": 3},
    adaptation={"based-movies": 6, "no-based-movies": 4},
    reading_habit={"daily": 4, "weekly": 4, "monthly": 2}
)

user11 = User(
    name = "user11",
    reading_time={"morning": 4, "afternoon": 4, "evening": 6, "night": 4},
    book_length={"short_stories": 2, "novellas": 3, "full_length_novels": 5},
    authors=["Jane Austen", "Charles Dickens", "Leo Tolstoy", "Emily Brontë", "F. Scott Fitzgerald"],
    genre={"romance": 8, "adventure": 3, "mystery": 4, "fantasy": 3, "historical": 7, "sci-fic": 2,
           "biography": 3, "horror": 1, "comic": 1, "self-help": 1, "religion": 1},
    sensitivity={"violence": 2, "profanity": 2, "sexual": 3, "none": 8},
    book_prefer={"recommendation": 5, "top-rated": 7, "new-release": 4, "best-seller": 6, "award-winnig": 7},
    reading_goal={"entertainment": 6, "personal-growth": 5, "cultural-understanding": 7, "research": 4,
                  "philosophy": 3, "educational": 3, "relaxation": 6, "professional-development": 2},
    groups=["Classics", "Historical Fiction"],
    book_interaction={"reviewing-behaviour": 4, "book-discussions": 6, "social-sharing": 3},
    adaptation={"based-movies": 4, "no-based-movies": 6},
    reading_habit={"daily": 5, "weekly": 3, "monthly": 2}
)

user12 = User(
    name = "user12",
    reading_time={"morning": 6, "afternoon": 5, "evening": 4, "night": 3},
    book_length={"short_stories": 7, "novellas": 1, "full_length_novels": 2},
    authors=["Isaac Asimov", "Arthur C. Clarke", "Philip K. Dick", "Ursula K. Le Guin", "William Gibson"],
    genre={"romance": 3, "adventure": 6, "mystery": 4, "fantasy": 5, "historical": 2, "sci-fic": 9,
           "biography": 1, "horror": 2, "comic": 2, "self-help": 1, "religion": 1},
    sensitivity={"violence": 3, "profanity": 3, "sexual": 4, "none": 6},
    book_prefer={"recommendation": 5, "top-rated": 6, "new-release": 4, "best-seller": 3, "award-winnig": 5},
    reading_goal={"entertainment": 5, "personal-growth": 3, "cultural-understanding": 2, "research": 4,
                  "philosophy": 2, "educational": 2, "relaxation": 5, "professional-development": 2},
    groups=["Science Fiction", "Classic Science Fiction"],
    book_interaction={"reviewing-behaviour": 4, "book-discussions": 2, "social-sharing": 3},
    adaptation={"based-movies": 7, "no-based-movies": 3},
    reading_habit={"daily": 4, "weekly": 4, "monthly": 2}
)

user13 = User(
    name = "user13",
    reading_time={"morning": 2, "afternoon": 6, "evening": 7, "night": 5},
    book_length={"short_stories": 4, "novellas": 4, "full_length_novels": 2},
    authors=["Margaret Atwood", "Kurt Vonnegut", "Chuck Palahniuk", "Jeff VanderMeer", "Neil Gaiman"],
    genre={"romance": 2, "adventure": 5, "mystery": 6, "fantasy": 5, "historical": 2, "sci-fic": 7,
           "biography": 1, "horror": 3, "comic": 2, "self-help": 2, "religion": 1},
    sensitivity={"violence": 6, "profanity": 4, "sexual": 5, "none": 3},
    book_prefer={"recommendation": 4, "top-rated": 5, "new-release": 6, "best-seller": 7, "award-winnig": 5},
    reading_goal={"entertainment": 7, "personal-growth": 4, "cultural-understanding": 3, "research": 2,
                  "philosophy": 2, "educational": 2, "relaxation": 5, "professional-development": 2},
    groups=["Speculative Fiction", "Contemporary Fiction"],
    book_interaction={"reviewing-behaviour": 5, "book-discussions": 4, "social-sharing": 4},
    adaptation={"based-movies": 6, "no-based-movies": 4},
    reading_habit={"daily": 3, "weekly": 5, "monthly": 3}
)

user14 = User(
    name = "user14",
    reading_time={"morning": 7, "afternoon": 4, "evening": 5, "night": 2},
    book_length={"short_stories": 3, "novellas": 2, "full_length_novels": 5},
    authors=["John Green", "Rainbow Rowell", "David Levithan", "Jennifer Niven", "E. Lockhart"],
    genre={"romance": 8, "adventure": 4, "mystery": 3, "fantasy": 3, "historical": 2, "sci-fic": 2,
           "biography": 1, "horror": 1, "comic": 1, "self-help": 2, "religion": 1},
    sensitivity={"violence": 2, "profanity": 2, "sexual": 3, "none": 8},
    book_prefer={"recommendation": 7, "top-rated": 5, "new-release": 4, "best-seller": 6, "award-winnig": 4},
    reading_goal={"entertainment": 8, "personal-growth": 3, "cultural-understanding": 2, "research": 1,
                  "philosophy": 1, "educational": 2, "relaxation": 7, "professional-development": 1},
    groups=["Young Adult", "Contemporary"],
    book_interaction={"reviewing-behaviour": 4, "book-discussions": 5, "social-sharing": 4},
    adaptation={"based-movies": 5, "no-based-movies": 5},
    reading_habit={"daily": 2, "weekly": 6, "monthly": 2}
)

user15 = User(
    name = "user15",
    reading_time={"morning": 4, "afternoon": 6, "evening": 5, "night": 5},
    book_length={"short_stories": 5, "novellas": 2, "full_length_novels": 3},
    authors=["Liane Moriarty", "Gillian Flynn", "Paula Hawkins", "Tana French", "Shari Lapena"],
    genre={"romance": 4, "adventure": 5, "mystery": 8, "fantasy": 3, "historical": 2, "sci-fic": 3,
           "biography": 2, "horror": 1, "comic": 2, "self-help": 1, "religion": 1},
    sensitivity={"violence": 6, "profanity": 5, "sexual": 7, "none": 2},
    book_prefer={"recommendation": 6, "top-rated": 7, "new-release": 5, "best-seller": 6, "award-winnig": 5},
    reading_goal={"entertainment": 7, "personal-growth": 3, "cultural-understanding": 2, "research": 2,
                  "philosophy": 2, "educational": 2, "relaxation": 5, "professional-development": 3},
    groups=["Thriller", "Mystery"],
    book_interaction={"reviewing-behaviour": 6, "book-discussions": 5, "social-sharing": 3},
    adaptation={"based-movies": 6, "no-based-movies": 4},
    reading_habit={"daily": 3, "weekly": 4, "monthly": 3}
)

user16 = User(
    name = "user16",
    reading_time={"morning": 5, "afternoon": 3, "evening": 6, "night": 4},
    book_length={"short_stories": 6, "novellas": 1, "full_length_novels": 3},
    authors=["Stephen King", "James Patterson", "Dean Koontz", "Michael Connelly", "Harlan Coben"],
    genre={"romance": 3, "adventure": 5, "mystery": 8, "fantasy": 2, "historical": 2, "sci-fic": 4,
           "biography": 1, "horror": 7, "comic": 2, "self-help": 1, "religion": 1},
    sensitivity={"violence": 8, "profanity": 7, "sexual": 6, "none": 2},
    book_prefer={"recommendation": 6, "top-rated": 7, "new-release": 4, "best-seller": 5, "award-winnig": 5},
    reading_goal={"entertainment": 8, "personal-growth": 2, "cultural-understanding": 3, "research": 1,
                  "philosophy": 2, "educational": 2, "relaxation": 5, "professional-development": 2},
    groups=["Horror", "Thriller"],
    book_interaction={"reviewing-behaviour": 6, "book-discussions": 3, "social-sharing": 2},
    adaptation={"based-movies": 7, "no-based-movies": 3},
    reading_habit={"daily": 4, "weekly": 4, "monthly": 2}
)

user17 = User(
    name = "user17",
    reading_time={"morning": 3, "afternoon": 5, "evening": 7, "night": 3},
    book_length={"short_stories": 3, "novellas": 4, "full_length_novels": 3},
    authors=["J.K. Rowling", "J.R.R. Tolkien", "George R.R. Martin", "Brandon Sanderson", "Patrick Rothfuss"],
    genre={"romance": 4, "adventure": 7, "mystery": 5, "fantasy": 8, "historical": 2, "sci-fic": 3,
           "biography": 1, "horror": 2, "comic": 2, "self-help": 1, "religion": 1},
    sensitivity={"violence": 5, "profanity": 3, "sexual": 2, "none": 10},
    book_prefer={"recommendation": 4, "top-rated": 6, "new-release": 5, "best-seller": 4, "award-winnig": 5},
    reading_goal={"entertainment": 8, "personal-growth": 3, "cultural-understanding": 4, "research": 1,
                  "philosophy": 2, "educational": 2, "relaxation": 6, "professional-development": 1},
    groups=["Fantasy", "Epic Fantasy"],
    book_interaction={"reviewing-behaviour": 5, "book-discussions": 4, "social-sharing": 5},
    adaptation={"based-movies": 6, "no-based-movies": 4},
    reading_habit={"daily": 2, "weekly": 6, "monthly": 2}
)

user18 = User(
    name = "user18",
    reading_time={"morning": 7, "afternoon": 4, "evening": 5, "night": 3},
    book_length={"short_stories": 5, "novellas": 2, "full_length_novels": 3},
    authors=["Gillian Flynn", "Paula Hawkins", "Tana French", "Lisa Jewell", "Shari Lapena"],
    genre={"romance": 3, "adventure": 5, "mystery": 8, "fantasy": 3, "historical": 1, "sci-fic": 2,
           "biography": 1, "horror": 2, "comic": 1, "self-help": 2, "religion": 1},
    sensitivity={"violence": 6, "profanity": 5, "sexual": 7, "none": 2},
    book_prefer={"recommendation": 5, "top-rated": 6, "new-release": 4, "best-seller": 5, "award-winnig": 3},
    reading_goal={"entertainment": 7, "personal-growth": 3, "cultural-understanding": 2, "research": 1,
                  "philosophy": 1, "educational": 2, "relaxation": 6, "professional-development": 1},
    groups=["Thriller", "Mystery"],
    book_interaction={"reviewing-behaviour": 6, "book-discussions": 4, "social-sharing": 3},
    adaptation={"based-movies": 5, "no-based-movies": 5},
    reading_habit={"daily": 2, "weekly": 5, "monthly": 3}
)

user19 = User(
    name = "user19",
    reading_time={"morning": 4, "afternoon": 6, "evening": 4, "night": 6},
    book_length={"short_stories": 6, "novellas": 3, "full_length_novels": 1},
    authors=["Stephen King", "Harlan Coben", "James Patterson", "Michael Connelly", "Lee Child"],
    genre={"romance": 3, "adventure": 4, "mystery": 7, "fantasy": 2, "historical": 2, "sci-fic": 3,
           "biography": 2, "horror": 6, "comic": 2, "self-help": 1, "religion": 1},
    sensitivity={"violence": 7, "profanity": 5, "sexual": 6, "none": 2},
    book_prefer={"recommendation": 6, "top-rated": 5, "new-release": 4, "best-seller": 6, "award-winnig": 3},
    reading_goal={"entertainment": 8, "personal-growth": 3, "cultural-understanding": 2, "research": 2,
                  "philosophy": 1, "educational": 1, "relaxation": 5, "professional-development": 1},
    groups=["Thriller", "Suspense"],
    book_interaction={"reviewing-behaviour": 5, "book-discussions": 3, "social-sharing": 2},
    adaptation={"based-movies": 6, "no-based-movies": 4},
    reading_habit={"daily": 3, "weekly": 4, "monthly": 3}
)

user20 = User(
    name = "user20",
    reading_time={"morning": 6, "afternoon": 3, "evening": 5, "night": 6},
    book_length={"short_stories": 2, "novellas": 4, "full_length_novels": 4},
    authors=["Margaret Atwood", "Chimamanda Ngozi Adichie", "Arundhati Roy", "Zadie Smith", "Toni Morrison"],
    genre={"romance": 5, "adventure": 3, "mystery": 4, "fantasy": 2, "historical": 6, "sci-fic": 1,
           "biography": 2, "horror": 1, "comic": 1, "self-help": 3, "religion": 1},
    sensitivity={"violence": 4, "profanity": 3, "sexual": 2, "none": 8},
    book_prefer={"recommendation": 3, "top-rated": 7, "new-release": 4, "best-seller": 2, "award-winnig": 6},
    reading_goal={"entertainment": 5, "personal-growth": 6, "cultural-understanding": 8, "research": 2,
                  "philosophy": 3, "educational": 3, "relaxation": 4, "professional-development": 1},
    groups=["Literary Fiction", "Contemporary"],
    book_interaction={"reviewing-behaviour": 4, "book-discussions": 6, "social-sharing": 5},
    adaptation={"based-movies": 3, "no-based-movies": 7},
    reading_habit={"daily": 2, "weekly": 4, "monthly": 4}
)
