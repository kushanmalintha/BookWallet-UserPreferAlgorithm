from home_screen_user import user1, user2, user3, user4, user5, user6, user7, user8, user9, user10, user11, user12, user13, user14, user15, user16, user17, user18, user19, user20
from home_screen_book import book1, book2, book3, book4, book5, book6, book7, book8, book9, book10, book11, book12, book13, book14, book15, book16, book17, book18, book19, book20, book21, book22, book23, book24, book25, book26, book27, book28, book29, book30, book31, book32, book33, book34, book35, book36, book37, book38, book39, book40, book41, book42, book43, book44, book45, book46, book47, book48, book49, book50

# buckets
genre_buckets = {
    'romance': [[], []],
    'adventure': [[], []],
    'mystery': [[], []],
    'fantasy': [[], []],
    'historical': [[], []],
    'sci_fic': [[], []],
    'biography': [[], []],
    'horror': [[], []],
    'comic': [[], []],
    'self_help': [[], []],
    'religion': [[], []]
}

length_bucket = {
    'short_stories': [[], []],
    'novellas': [[], []],
    'full_length_novels': [[], []]
}

reading_goal = {
    'entertainment': [[], []],
    'personal-growth': [[], []],
    'cultural-understanding': [[], []],
    'research': [[], []],
    'philosophy': [[], []],
    'educational': [[], []],
    'relaxation': [[], []],
    'professional-development': [[], []]
}

sensitivity = {
    'violence': [[], []],
    'profanity': [[], []],
    'sexual': [[], []],
    'none': [[], []]
}

reading_time = {
    'morning': [[], []],
    'afternoon': [[], []],
    'evening': [[], []],
    'night': [[], []]
}

book_interaction = {
    'reviewing-behaviour': [[], []],
    'book-discussions': [[], []],
    'social-sharing': [[], []]
}

adaptation = {
    'based-movies': [[], []],
    'no-based-movies': [[], []]
}



# function to add users and books to the buckets
def add_to_bucket(users, books, genre_buckets, length_bucket, reading_goal, sensitivity, 
                  reading_time, book_interaction, adaptation):
    
    # Loop through users and books for genre buckets
    for user in users:
        for genre in genre_buckets:
            if user.genre.get(genre, 0) >= 4:
                genre_buckets[genre][0].append(user)  # Add user to the first list (index 0)
    
    for book in books:
        for genre in genre_buckets:
            if book.genre.get(genre, 0) >= 4:
                genre_buckets[genre][1].append(book)  # Add book to the second list (index 1)
    
    # Length Bucket: Add book if the length attribute exists and equals True
    for user in users:
        if user.book_length.get('short_stories', 0) >= 4:
            length_bucket['short_stories'][0].append(user)
        if user.book_length.get('novellas', 0) >= 4:
            length_bucket['novellas'][0].append(user)
        if user.book_length.get('full_length_novels', 0) >= 4:
            length_bucket['full_length_novels'][0].append(user)
    
    for book in books:
        if book.book_length.get('short_stories', 0):
            length_bucket['short_stories'][1].append(book)
        if book.book_length.get('novellas', 0):
            length_bucket['novellas'][1].append(book)
        if book.book_length.get('full_length_novels', 0):
            length_bucket['full_length_novels'][1].append(book)

    # Reading Goal: Both user and book need to have >= 4
    for user in users:
        for goal in reading_goal:
            if user.reading_goal.get(goal, 0) >= 4:
                reading_goal[goal][0].append(user)
    
    for book in books:
        for goal in reading_goal:
            if book.reading_goal.get(goal, 0) >= 4:
                reading_goal[goal][1].append(book)

    # Sensitivity: Both user and book need >= 4
    for user in users:
        for sensitive in sensitivity:
            if user.sensitivity.get(sensitive, 0) >= 4:
                sensitivity[sensitive][0].append(user)
    
    for book in books:
        for sensitive in sensitivity:
            if book.sensitivity.get(sensitive, 0) >= 4:
                sensitivity[sensitive][1].append(book)

    # Reading Time: Both user and book need >= 4
    for user in users:
        for time in reading_time:
            if user.reading_time.get(time, 0) >= 4:
                reading_time[time][0].append(user)
    
    for book in books:
        for time in reading_time:
            if book.reading_time.get(time, 0) >= 4:
                reading_time[time][1].append(book)

    # Book Interaction: Both user and book need >= 4
    for user in users:
        for interaction in book_interaction:
            if user.book_interaction.get(interaction, 0) >= 4:
                book_interaction[interaction][0].append(user)
    
    for book in books:
        for interaction in book_interaction:
            if book.book_interaction.get(interaction, 0) >= 4:
                book_interaction[interaction][1].append(book)

    # Adaptation: Add book if attribute exists and equals True
    for user in users:
        if user.adaptation.get('based-movies', 0) >= 4:
            adaptation['based-movies'][0].append(user)
        if user.adaptation.get('no-based-movies', 0) >= 4:
            adaptation['no-based-movies'][0].append(user)

    for book in books:
        if book.adaptation.get('based-movies', 0):
            adaptation['based-movies'][1].append(book)
        if book.adaptation.get('no-based-movies', 0):
            adaptation['no-based-movies'][1].append(book)



users = [user1, user2, user3, user4, user5, user6, user7, user8, user9, user10, user11, user12, user13, user14, user15, user16, user17, user18, user19, user20]

books = [book1, book2, book3, book4, book5, book6, book7, book8, book9, book10, book11, book12, book13, book14, book15, book16, book17, book18, book19, book20,
         book21, book22, book23, book24, book25, book26, book27, book28, book29, book30, book31, book32, book33, book34, book35, book36, book37, book38, book39, book40,
         book41, book42, book43, book44, book45, book46, book47, book48, book49, book50]

bucket_dicts = [genre_buckets, length_bucket, reading_goal, sensitivity, reading_time, book_interaction, adaptation]

add_to_bucket(users, books, genre_buckets, length_bucket, reading_goal, sensitivity, reading_time, book_interaction, adaptation)

# Print the results
# print("GENRE BUCKETS:", genre_buckets)
# print("LENGTH BUCKET:", length_bucket)
# print("READING GOAL:", reading_goal)
# print("SENSITIVITY:", sensitivity)
# print("READING TIME:", reading_time)
# print("BOOK INTERACTION:", book_interaction)
# print("ADAPTATION:", adaptation)



# function to get which buckets user and book has
def find_buckets(users, *bucket_dicts):
    # Create dictionaries to store which buckets each user and book are in
    user_buckets = {user: [] for user in users}

    # Iterate over each bucket dictionary
    for bucket_dict in bucket_dicts:
        # Iterate over each attribute in the bucket dictionary
        for attribute, (bucket_users, _) in bucket_dict.items():
            # Check each user in the provided user list
            for user in users:
                if user in bucket_users:
                    user_buckets[user].append(attribute) 
                
    return user_buckets

user_buckets = find_buckets(users, *bucket_dicts)

# print("User Buckets:", user_buckets)



# Function to get books for a user based on the bucket they belong to
def get_user_book_buckets(user, user_buckets, *bucket_dicts):
    # Initialize an empty dictionary to hold the book counts
    book_count = {}

    # Combine all bucket dictionaries into one
    all_buckets = {
        'genre': bucket_dicts[0],
        'length': bucket_dicts[1],
        'goal': bucket_dicts[2],
        'sensitivity': bucket_dicts[3],
        'time': bucket_dicts[4],
        'interaction': bucket_dicts[5],
        'adaptation': bucket_dicts[6]
    }

    # Get the buckets/categories that the user belongs to
    user_categories = user_buckets.get(user, [])

    # Iterate through each bucket the user belongs to
    for category in user_categories:
        bucket_type = None
        # Identify which bucket type the category belongs to
        for btype, buckets in all_buckets.items():
            if category in buckets:
                bucket_type = btype
                break
        
        if bucket_type and category in all_buckets[bucket_type]:  # Ensure category exists in the relevant bucket dict
            # Get the list of books in that category
            books_in_category = all_buckets[bucket_type][category][1]
            
            # Iterate over the books in this category and update the count
            for book in books_in_category:
                if book in book_count:
                    book_count[book] += 1  # Increment if the book is already in the dictionary
                else:
                    book_count[book] = 1  # Add the book to the dictionary if it's new

    # Sort the book count dictionary by count in descending order
    sorted_book_count = dict(sorted(book_count.items(), key=lambda item: item[1], reverse=True))

    return sorted_book_count

# Function to process all users
def process_all_users(user_buckets, *bucket_dicts):
    all_user_book_counts = {}

    # Extract users from the keys of user_buckets
    for user in user_buckets:
        # Get the book counts for the current user, sorted by count
        book_count = get_user_book_buckets(user, user_buckets, *bucket_dicts)
        # Store the result in the all_user_book_counts dictionary
        all_user_book_counts[user] = book_count

    return all_user_book_counts

# Example usage
all_book_counts = process_all_users(user_buckets, *bucket_dicts)
print(all_book_counts)
