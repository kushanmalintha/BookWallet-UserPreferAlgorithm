reading_time = {
    # int
    "morning": '',
    "afternoon": '',
    "evening": '',
    "night": ''
}

book_length = {
    # bool
    "short_stories": '',
    "novellas": '',
    "full_length_novels": ''
}

author = ''

genre = {
    # int
    "romance": '',
    "adventure": '',
    "mystery": '',
    "fantasy": '',
    "historical": '',
    "sci-fic": '',
    "biography": '',
    "horror": '',
    "comic": '',
    "self-help": '',
    "religion": ''
}

sensitivity = {
    # int
    "violence": '',
    "profanity": '',
    "sexual": '',
    "none": ''
}

book_prefer = {
    # bool
    "recommendation": '',
    "top-rated": '',
    "new-release": '',
    "best-seller": '',
    "award-winnig": ''
}

reading_goal = {
    # int
    "entertainment": '',
    "personal-growth": '',
    "cultural-understanding": '',
    "research": '',
    "philosophy": '',
    "educational": '',
    "relaxation": '',
    "professional-development": ''
}

groups = []

book_interaction = {
    # int
    "reviewing-behaviour": '',
    "book-discussions": '',
    "social-sharing": ''
}

adaptation = {
    # bool
    "based-movies": '',
    "no-based-movies": ''
}

# exploration = []

'''
1. Core Preferences (High Impact)
Genre: Directly affects the content a user will see.
Favourite Author: Strong influence on personalization and recommendations.
Book Length: Influences the type of content a user prefers to read (short stories, novellas, novels).
Reading Goal: Helps align the content with the user's objectives, such as entertainment or educational purposes.
Reading Time: Determines when users are likely to read, affecting the timing of recommendations.

2. Content Sensitivity (Moderate Impact)
Sensitivity: Filters out content that might not be suitable for the user based on their tolerance for violence, profanity, etc.
Adaptation: Preferences regarding books based on movies can help curate specific types of content.

3. Engagement Preferences (Moderate to Low Impact)
Book Interaction: Reviewing behavior, discussions, and social sharing can indicate the level of community involvement and influence book recommendations.
Book Groups: Participation in book groups may indicate preferred genres or types of books.
Exploration: Whether a user likes to explore different genres or stick to their favorites.

4. Supplementary Preferences (Low Impact)
Book Preferences (Recommendation, Top-rated, etc.): These are more specific preferences that can fine-tune recommendations but might not drastically change the user experience.
Reading Habit: Helps understand the frequency of content updates required but doesn't directly impact what content is shown.
'''

'''
Buckets:

Genre-Based
Author-Based
Length-Based
Reading Goals
Content Sensitivity
Reading Time
Engagement Preferences
Adaptation Preferences
Exploration Habits
'''

'''
brackets
---------
genre 4/10 threshold
author one bracket for each
length avg
reading length threshold for user
sensitivuty like genre
reading time like genre
group like author
book interaction like genre
adaptation like length
'''

'''
genre variable wlt adala vector space ekak gnnwa, eke angle eka gannawa, meka passe
'''