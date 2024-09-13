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
    return (sum_abs_diff / sum_max_values)*100

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
    return (sum_abs_diff / sum_max_values)*100

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
    
    return (sum_abs_diff / sum_max_values)*100

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
    
# example1

reading_time_result = reading_time(5, 3, 2, 6, 3, 4, 6, 7)
print("Reading Time Similarity Score:", reading_time_result)
book_length_result = book_length(4, 2, 4, False, True, True)
print("Book Length Similarity Score:", book_length_result)
book_prefer_result = book_prefer(8, 7, 6, 7, 5, True, True, False, True, True)
print("Book Preference Similarity Score:", book_prefer_result)
adaptation_result = adaptation(7, 3, True, False)
print("Adaptation Similarity Score:", adaptation_result)
genre_result = genre(3, 8, 5, 9, 2, 7, 2, 1, 1, 3, 2, 2, 1, 3, 0, 5, 9, 0, 1, 0, 0, 0)
print("Genre Similarity Score:", genre_result)
sensitivity_result = sensitivity(5, 4, 3, 2, 5, 2, 1, 3)
print("Sensitivity Similarity Score:", sensitivity_result)
reading_goal_result = reading_goal(9, 6, 4, 3, 2, 3, 8, 2, 8, 3, 5, 6, 2, 7, 6, 4)
print("Reading Goal Similarity Score:", reading_goal_result)
author_result = author(["J.K. Rowling", "George R.R. Martin", "Stephen King", "Agatha Christie", "J.R.R. Tolkien"], "George Orwell")
print("Author Similarity Score:", author_result)
group_result = group(["Fantasy", "Adventure"], ["Dystopian Readers", "Classic Literature"])
print("Group Similarity Score:", group_result)


def accuracy(reading_time_result, book_length_result, book_prefer_result,adaptation_result,
             genre_result, sensitivity_result, reading_goal_result, author_result, group_result):
    up = (15*reading_time_result)+(60*book_length_result)+(60*author_result)+(60*genre_result)+(50*sensitivity_result)+(20*book_prefer_result)+(55*reading_goal_result)+(40*group_result)+(45*adaptation_result)
    down = reading_goal_result+book_length_result+author_result+genre_result+sensitivity_result+book_prefer_result+reading_goal_result+group_result+adaptation_result
    return up/down

accuracy_result = accuracy(reading_time_result, book_length_result, book_prefer_result,adaptation_result,genre_result, sensitivity_result, reading_goal_result, author_result, group_result)
print("Accuracy:",accuracy_result)