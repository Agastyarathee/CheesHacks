import csv
from collections import Counter

# Function to load events from the CSV
def load_events_from_csv(file_path):
    events = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            events.append({
                'name': row['name'],  # Name of the event
                'description': row['description'],  # Event description
                'date_time': row['date_time'],  # Event date/time
                'url': row['url']  # Event URL
            })
    return events

# Function to get user input responses
def get_user_input():
    questions = [
        "Do you enjoy sports?",
        "Do you like cultural events?",
        "Do you enjoy food and social gatherings?",
        "Are you interested in health or wellness topics?",
        "Do you like religious or spiritual events?"
    ]
    
    responses = []
    for question in questions:
        answer = input(f"{question} (yes/no): ").strip().lower()
        responses.append(answer == 'yes')  # Store True for 'yes', False for 'no'
    
    return responses

# Function to generate personality keywords based on user input
def generate_personality_keywords(responses):
    # Define keywords for each question (you can adjust this to suit the type of events)
    keywords = {
        0: ['sports', 'athletics', 'game', 'competition'],  # "Do you enjoy sports?"
        1: ['culture', 'international', 'tradition', 'performance', 'dance'],  # "Do you like cultural events?"
        2: ['food', 'dinner', 'social', 'gathering', 'potluck'],  # "Do you enjoy food and social gatherings?"
        3: ['health', 'wellness', 'symposium', 'healthcare'],  # "Are you interested in health or wellness topics?"
        4: ['religion', 'spiritual', 'church', 'bible', 'worship']  # "Do you like religious or spiritual events?"
    }
    
    personality_keywords = []
    for i, response in enumerate(responses):
        if response:
            personality_keywords.extend(keywords[i])  # Add corresponding keywords if answer is 'yes'
    
    return personality_keywords

# Function to score events based on how well they match the user's personality
def score_events(events, personality_keywords):
    event_scores = []
    
    for event in events:
        # Tokenize the event description and count matches with personality keywords
        description_words = event['description'].lower().split()
        description_counter = Counter(description_words)
        
        # Calculate the score for the event based on matching keywords
        score = sum(description_counter[word] for word in personality_keywords)
        event_scores.append((event['name'], event['description'], score, event['url'], event['date_time']))
    
    # Sort events by score in descending order
    event_scores.sort(key=lambda x: x[2], reverse=True)
    return event_scores

# Main function to run the program
def main():
    events = load_events_from_csv('event_details.csv')  # Load events from the event_details.csv file
    responses = get_user_input()  # Get the user's responses
    personality_keywords = generate_personality_keywords(responses)  # Generate personality keywords
    event_scores = score_events(events, personality_keywords)  # Score the events based on user responses
    
    # Display the events that match the user's preferences
    print("\nBased on your responses, these events are a good match for you:")
    for event_name, event_description, score, event_url, event_date in event_scores:
        if score > 0:  # Only show events that have a non-zero match score
            print(f"\nEvent: {event_name}")
            print(f"Description: {event_description[:200]}...")  # Show a snippet of the description
            print(f"Date/Time: {event_date}")
            print(f"URL: {event_url}")
            print(f"Match Score: {score}")

# Run the program
if __name__ == "__main__":
    main()
