from home_screen_user import user1, user2
from home_screen_book import book1, book2

# bar method

# reading time

def reading_time(morning_user, afternon_user, evening_user, night_user, 
                 morning_book, afternon_book, evening_book, night_book):
    return ((abs(morning_user-morning_book)+abs(afternon_user-afternon_book)+abs(evening_user-evening_book)+abs(night_user-night_book))/(morning_user+afternon_user+evening_user+night_user))*100

# bar method bool

# book length

def book_length(short_story_user, novel_user, full_length_novel_user, 
                short_story_book, novel_book, full_length_novel_book):
    
    # List of user preferences and corresponding book availability
    user_preferences = [short_story_user, novel_user, full_length_novel_user]
    book_types = [short_story_book, novel_book, full_length_novel_book]
    
    # Calculate the sum of user preferences for book types that are True
    matching_preferences = sum(user_pref for user_pref, book in zip(user_preferences, book_types) if book)
    
    # Calculate the sum of all user preferences
    total_user_preferences = sum(user_preferences)
    
    # Return the ratio of matching preferences to total preferences
    return (matching_preferences / total_user_preferences)*100

# book prefer

def book_prefer(recommendation_user, top_rated_user, new_release_user, best_seller_user, award_winnig_user,
                recommendation_book, top_rated_book, new_release_book, best_seller_book, award_winnig_book):
    user_preferences = [recommendation_user, top_rated_user, new_release_user, best_seller_user, award_winnig_user]
    book_types = [recommendation_book, top_rated_book, new_release_book, best_seller_book, award_winnig_book]
    matching_preferences = sum(user_pref for user_pref, book in zip(user_preferences, book_types) if book)
    total_user_preferences = sum(user_preferences)
    return (matching_preferences / total_user_preferences)*100

# adaptation

def adaptation(based_movies_user, no_based_movies_user,
               based_movies_book, no_based_movies_book):
    user_preferences = [based_movies_user, no_based_movies_user]
    book_types = [based_movies_book, no_based_movies_book]
    matching_preferences = sum(user_pref for user_pref, book in zip(user_preferences, book_types) if book)
    total_user_preferences = sum(user_preferences)
    return (matching_preferences / total_user_preferences)*100

# bar method 2

# genre

def genre(romance_user, adventure_user, mystery_user, fantasy_user, historical_user,
          sci_fic_user, biography_user, horror_user, comic_user, self_help_user, religion_user,
          romance_book, adventure_book, mystery_book, fantasy_book, historical_book,
          sci_fic_book, biography_book, horror_book, comic_book, self_help_book, religion_book):
    
    # Lists of user preferences and corresponding book genres
    user_preferences = [romance_user, adventure_user, mystery_user, fantasy_user, historical_user,
                        sci_fic_user, biography_user, horror_user, comic_user, self_help_user, religion_user]
    
    book_genres = [romance_book, adventure_book, mystery_book, fantasy_book, historical_book,
                   sci_fic_book, biography_book, horror_book, comic_book, self_help_book, religion_book]
    
    # Calculate the sum of absolute differences and the sum of max values
    sum_abs_diff = sum(abs(book - user) for book, user in zip(book_genres, user_preferences))
    sum_max_values = sum(max(book, user) for book, user in zip(book_genres, user_preferences))
    
    # Return the ratio of the sum of absolute differences to the sum of max values
    return 100 - (sum_abs_diff / sum_max_values)*100

# book sensitivity

def sensitivity(violence_user, profanity_user, sexual_user, none_user,
                violence_book, profanity_book, sexual_book, none_book):
    
    # Lists of user preferences and corresponding book genres
    user_preferences = [violence_user, profanity_user, sexual_user, none_user]
    
    book_genres = [violence_book, profanity_book, sexual_book, none_book]
    
    # Calculate the sum of absolute differences and the sum of max values
    sum_abs_diff = sum(abs(book - user) for book, user in zip(book_genres, user_preferences))
    sum_max_values = sum(max(book, user) for book, user in zip(book_genres, user_preferences))
    
    # Return the ratio of the sum of absolute differences to the sum of max values
    return 100 - (sum_abs_diff / sum_max_values)*100

# reading goal

def reading_goal(entertainment_user, personal_growth_user, cultural_understanding_user, research_user,
                 philosophy_user, educational_user, relaxation_user, professional_development_user,
                 entertainment_book, personal_growth_book, cultural_understanding_book, research_book,
                 philosophy_book, educational_book, relaxation_book, professional_development_book):
    
    user_goals = [entertainment_user, personal_growth_user, cultural_understanding_user, research_user,
                  philosophy_user, educational_user, relaxation_user, professional_development_user]
    
    book_attributes = [entertainment_book, personal_growth_book, cultural_understanding_book, research_book,
                       philosophy_book, educational_book, relaxation_book, professional_development_book]
    
    sum_abs_diff = sum(abs(book - user) for book, user in zip(book_attributes, user_goals))
    sum_max_values = sum(max(book, user) for book, user in zip(book_attributes, user_goals))
    
    return 100 - (sum_abs_diff / sum_max_values)*100

# bool

# author

def author(author_user, author_book):
    if author_book in author_user:
        return 100
    else:
        return 0
    
# groups

def group(group_user, group_book):
    if any(user_group in group_book for user_group in group_user):
        return 100
    else:
        return 0

# accuracy

def accuracy(user, book):
    # Reading Time
    reading_time_result = reading_time(
        user.reading_time["morning"], user.reading_time["afternoon"],
        user.reading_time["evening"], user.reading_time["night"],
        book.reading_time["morning"], book.reading_time["afternoon"],
        book.reading_time["evening"], book.reading_time["night"]
    )
    print("Reading Time Similarity Score:", reading_time_result)
    
    # Book Length
    book_length_result = book_length(
        user.book_length["short_stories"], user.book_length["novellas"], user.book_length["full_length_novels"],
        book.book_length["short_stories"], book.book_length["novellas"], book.book_length["full_length_novels"]
    )
    print("Book Length Similarity Score:", book_length_result)
    
    # Book Preferences
    book_prefer_result = book_prefer(
        user.book_prefer["recommendation"], user.book_prefer["top-rated"], user.book_prefer["new-release"],
        user.book_prefer["best-seller"], user.book_prefer["award-winnig"],
        book.book_prefer["recommendation"], book.book_prefer["top-rated"], book.book_prefer["new-release"],
        book.book_prefer["best-seller"], book.book_prefer["award-winnig"]
    )
    print("Book Preference Similarity Score:", book_prefer_result)
    
    # Adaptation
    adaptation_result = adaptation(
        user.adaptation["based-movies"], user.adaptation["no-based-movies"],
        book.adaptation["based-movies"], book.adaptation["no-based-movies"]
    )
    print("Adaptation Similarity Score:", adaptation_result)
    
    # Genre Preferences
    genre_result = genre(
        user.genre["romance"], user.genre["adventure"], user.genre["mystery"], user.genre["fantasy"],
        user.genre["historical"], user.genre["sci-fic"], user.genre["biography"], user.genre["horror"],
        user.genre["comic"], user.genre["self-help"], user.genre["religion"],
        book.genre["romance"], book.genre["adventure"], book.genre["mystery"], book.genre["fantasy"],
        book.genre["historical"], book.genre["sci-fic"], book.genre["biography"], book.genre["horror"],
        book.genre["comic"], book.genre["self-help"], book.genre["religion"]
    )
    print("Genre Similarity Score:", genre_result)
    
    # Sensitivity
    sensitivity_result = sensitivity(
        user.sensitivity["violence"], user.sensitivity["profanity"], user.sensitivity["sexual"], user.sensitivity["none"],
        book.sensitivity["violence"], book.sensitivity["profanity"], book.sensitivity["sexual"], book.sensitivity["none"]
    )
    print("Sensitivity Similarity Score:", sensitivity_result)
    
    # Reading Goals
    reading_goal_result = reading_goal(
        user.reading_goal["entertainment"], user.reading_goal["personal-growth"], user.reading_goal["cultural-understanding"],
        user.reading_goal["research"], user.reading_goal["philosophy"], user.reading_goal["educational"],
        user.reading_goal["relaxation"], user.reading_goal["professional-development"],
        book.reading_goal["entertainment"], book.reading_goal["personal-growth"], book.reading_goal["cultural-understanding"],
        book.reading_goal["research"], book.reading_goal["philosophy"], book.reading_goal["educational"],
        book.reading_goal["relaxation"], book.reading_goal["professional-development"]
    )
    print("Reading Goal Similarity Score:", reading_goal_result)
    
    # Author Match
    author_result = author(user.authors, book.author)
    print("Author Similarity Score:", author_result)
    
    # Group Match
    group_result = group(user.groups, book.groups)
    print("Group Similarity Score:", group_result)

    # Calculate final accuracy
    up = (15*reading_time_result)+(60*book_length_result)+(55*author_result)+(60*genre_result)+(50*sensitivity_result)+(20*book_prefer_result)+(55*reading_goal_result)+(35*group_result)+(45*adaptation_result)
    down = 15+60+55+60+50+20+55+35+45
    accuracy_result = up / down
    print("Final Accuracy Score:", accuracy_result)

    return accuracy_result

if __name__ == '__main__':
    print('user1:\n')
    accuracy(user1, book1)
    print('user2:\n')
    accuracy(user2,book2)