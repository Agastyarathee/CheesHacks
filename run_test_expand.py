
from sentence_transformers import SentenceTransformer, util

# Load a pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download the stopwords list (only once)
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

"""## Non-Open ended question """

from sklearn.feature_extraction.text import TfidfVectorizer
from sentence_transformers import SentenceTransformer, util

# Define keywords or attribute phrases
attributes = {
    "teamwork": ["joint work", "networking", "collaboration", "cooperative", "partnership", "coordinate", "support", "collective effort", "mutual", "team effort"],
    "community_service": ["awareness", "community", "volunteer", "outreach", "giving back", "charity", "society", "non-profit", "social impact", "public benefit"],
    "leadership": ["inspire", "initiative", "motivated", "achieving", "leader", "responsible", "excel", "succeed", "evolve", "future"],
    "eagerness_to_learn": ["interest", "passion", "curious", "challenge", "learn", "grow", "knowledge", "explore", "develop", "innovation"],
    "critical_thinking": ["analysis", "problem-solving", "decision-making", "evaluate", "strategy", "analytical", "critical thinking", "reasoning", "logic", "insight"]
}

for i in attributes:
    print(len(attributes[i]))

# Load a pre-trained sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to score a description
def club_score(description, attributes):
    scores = {}
    desc_embedding = model.encode(description, convert_to_tensor=True)

    for attr, phrases in attributes.items():
        attr_embeddings = model.encode(phrases, convert_to_tensor=True)
        similarity = util.cos_sim(desc_embedding, attr_embeddings)
        scores[attr] = similarity.mean().item()  # Average similarity score

    return scores

# Example description
description = '''The Health Entrepreneurs and Leaders is a prehealth student organization established at the University of Wisconsin-Madison in 2020. As prehealth students, we identified the gaps and disparities in our community and the medical field. HEAL is our legacy to become the change that goes beyond addressing the issue but pushes forward to act upon them at the core of the issues. We understand healthcare policy and insurance are crucial factors that affect healthcare affordability and accessibility, which HEAL focuses on addressing. Beyond this, the cornerstone of HEAL is to address problems in healthcare at all levels, including but not limited to the federal, state, hospital administration, healthcare providers/professionals, patients, etc. HEAL is structured to be a center for all pre-health students to attain resources and mentorship to grow and develop in their path to pursuing and entering the health field. HEAL understands the benefits and advocates for the diversity of people, backgrounds, and minds to improve the future of medicine.'''
# Assess the description
scores = club_score(description, attributes)
print(scores)

"""## Open_Ended Question """

import re
import numpy as np

# Example club descriptions and user input
club_descriptions = [
    "Aa Dekhen Zara (ADZ) is an annual South Asian Dance competition hosted by the students of the University of Wisconsin-Madison. We host talented Bollywood-Fusion dance teams.",
    "The Alexander Hamilton Society (AHS) is a non-partisan organization focused on foreign policy and national security international relations.",
    "The American Medical College of Pharmacy (AMCP) provides opportunities to learn about managed care pharmacy, improving patient outcomes through clinical and business knowledge.",
    "Acacia is a social fraternity dedicated to human service. We are dedicated to bettering the community we are a part of and sharing a brotherhood we will remember for the rest of our lives. We are a fraternity that is focused on the strength of brotherhood. By selecting key members of the Madison community, we build a brotherhood dedicated to human service for both the community and ourselves. These members are selected through the IFC-regulated RUSH process in which members are first bid followed by a pledge process. We are a non-hazing fraternity built on the idea that disrespect to any possible future member or person is strictly against our goals and morals. All leaders of the Acacia Fraternity are elected by the active members and must be students of the University of Wisconsin-Madison."
]
user_input = ["I love dancing, especially Bollywood-style dance, and I am interested in pursuing a career in international relations."]

# Filter sentence to make similarity scores more relevant
def filter_sentence(sentence):
    # Step 1: Tokenize the sentence into words
    words = word_tokenize(sentence)

    # Step 2: Get the list of stopwords in English
    stop_words = set(stopwords.words('english'))

    # Step 3: Remove stopwords from the sentence
    filtered_words = [word for word in words if word.lower() not in stop_words]

    # Step 4: Reconstruct the sentence without stopwords
    filtered_sentence = ' '.join(filtered_words)

    # Output the result
    return filtered_sentence

# Define religious and cultural keywords for filtering
religious_keywords = [
    "church", "christian", "jesus", "bible", "god", "faith", "prayer", "cross", "christianity", 
    "mosque", "islam", "allah", "quran", "muslim", "jewish", "torah", "synagogue", "shabbat", "kosher", 
    "buddhist", "temple", "buddhism", "hindu", "vedic", "karma", "yoga", "guru", "religion", "spirituality"
]

# Function to classify user preferences (religion and culture)
def classify_user_profile(user_input):
    user_profile = {
        "religious_preference": "",
        "cultural_preference": ""
    }

    # Check for religious or cultural preferences
    if any(keyword in user_input.lower() for keyword in religious_keywords):
        if "christian" in user_input.lower():
            user_profile["religious_preference"] = "Christian"
        elif "muslim" in user_input.lower():
            user_profile["religious_preference"] = "Muslim"
        elif "jewish" in user_input.lower():
            user_profile["religious_preference"] = "Jewish"
        elif "hindu" in user_input.lower():
            user_profile["religious_preference"] = "Hindu"
        elif "buddhist" in user_input.lower():
            user_profile["religious_preference"] = "Buddhist"
    return user_profile

# Function to filter out inappropriate clubs based on user profile
def filter_inappropriate_matches(club_descriptions, user_profile):
    religious_preference = user_profile.get("religious_preference", "").lower()

    # Filter out clubs with religious or cultural keywords based on user preferences
    filtered_clubs = []
    for desc in club_descriptions:
        # Check if the description contains any of the religious keywords
        contains_religion = any(keyword in desc.lower() for keyword in religious_keywords)

        # If the club description contains a religious keyword and conflicts with the user's preference, exclude it
        if contains_religion and religious_preference and religious_preference not in desc.lower():
            continue  # Skip this club as it conflicts with user's religion/culture preference
        
        # If no conflict, add the club description to the list
        filtered_clubs.append(desc)

    return filtered_clubs

# Finding relevant clubs
def interest_similarity(club_descriptions, user_input):
    clubs = []
    user_profile = classify_user_profile(user_input)
    filtered_clubs = filter_inappropriate_matches(club_descriptions, user_profile)  # Filter clubs first
    
    for i in range(len(filtered_clubs)):
        mean = []
        sentences = re.split(r'[.!?]', filtered_clubs[i])
        sentences = [s.strip() for s in sentences if s.strip()]
        for a in range(len(sentences)):
            sentences[a] = filter_sentence(sentences[a])

            user_embedding = model.encode(user_input, convert_to_tensor=True)
            club_embedding = model.encode(sentences[a], convert_to_tensor=True)
            cosine_similarity = util.cos_sim(user_embedding, club_embedding)
            mean.append(cosine_similarity)

        if np.mean(np.array(mean)) >= 0.2:
            clubs.append([i, np.mean(np.array(mean))])
    return clubs

print(interest_similarity(club_descriptions, user_input))

# Getting relevant club titles
def matching_clubs(club_titles, club_descriptions, user_input):
    club_names = []
    indices = interest_similarity(club_descriptions, user_input)
    for i in range(len(indices)):
        club_names.append([club_titles[indices[i][0]], str(indices[i][1] * 100) + "%"])
    return club_names

