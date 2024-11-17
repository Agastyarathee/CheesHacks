#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sentence_transformers import SentenceTransformer, util

# Load a pre-trained model


# In[2]:


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download the stopwords list (only once)
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')



# ##Non-Open ended question

# In[60]:


from sklearn.feature_extraction.text import TfidfVectorizer
from sentence_transformers import SentenceTransformer, util


# Define keywords or attribute phrases

# Example description



# Load a pre-trained sentence transformer model

# Function to score a description
def club_score(description, attributes):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    scores = {}
    desc_embedding = model.encode(description, convert_to_tensor=True)

    for attr, phrases in attributes.items():
        attr_embeddings = model.encode(phrases, convert_to_tensor=True)
        similarity = util.cos_sim(desc_embedding, attr_embeddings)
        scores[attr] = similarity.mean().item()  # Average similarity score

    return scores



# Assess the description
def match_clubs(club_descriptions,user_attributes):
  matching_clubs = {}
  filtered_matching_clubs = {}
  attributes = { #WARNING: Words are subjected to change
    "teamwork": ["joint work","networking", "collaboration", "cooperative", "partnership", "coordinate","support", "collective effort","mutual", "team effort"], # "cooperation", "team", "collaboration", "group work", "mutual support", "collective effort", "synergy", "shared responsibility", "coordination", "joint effort", "supportive environment", "team spirit", "interdependence", "togetherness", "cooperation across teams", "team-based", "group dynamics"
    "community_service": ["awareness","community", "volunteer", "outreach", "giving back", "charity","society","non-profit","social impact","public benefit"], # "charity", "social impact", "community engagement","helping others", "civic responsibility", "social responsibility", "philanthropy", "mission trips", "voluntary service", "empowerment", "public service", "nonprofit work", "community involvement", "advocacy"
    "leadership": ["inspire", "initiative", "motivated", "achieving","leader", "responsible","excel", "succeed", "evolve","future",], # "leadership", "leader", "inspire", "mentor", "guide", "decision-making", "visionary","responsibility", "motivator", "manager", "influence", "coach", "authority", "empower", "director", "organizer", "strategic thinking", "leadership development", "leading by example"
    "eagerness_to_learn": ["interest","passion","curious","challenge", "learn", "grow", "knowledge","explore","develop", "innovation"], #"learning", "curiosity", "knowledge-seeking", "growth mindset", "self-improvement", "development", "education", "exploration", "adaptability", "open-mindedness", "lifelong learning", "innovation","self-driven", "intellectual curiosity", "new experiences", "skill-building", "challenging oneself","personal growth", "exploration of new ideas", "knowledge expansion"
    "critical_thinking": ["analysis", "problem-solving", "decision-making", "evaluate", "strategy", "analytical","critical thinking","reasoning","logic","insight"] # "problem-solving", "analysis", "critical thinking", "reasoning", "evaluation", "decision-making", "strategy","logic", "objectivity", "judgment", "reflection", "inquiry", "debate", "data analysis", "questioning assumptions","cognitive skills", "thoughtful consideration", "synthesis", "problem resolution", "insight"
}
  #remove this part later
  for i in attributes:
    print(len(attributes[i]))

  for i in range(len(club_descriptions)):
    categories = ["teamwork", "community_service", "leadership", "eagerness_to_learn", "critical_thinking"]
    scores = dict(sorted(club_score(club_descriptions[i], attributes).items(), key=lambda item: item[1]))
    print(scores) #remove this later
    for attr in range(len(user_attributes)):
      if (user_attributes[attr]) and scores[categories[attr]] > 0.1:
        matching_clubs[i] = scores[categories[attr]]

  if len(matching_clubs) <= 4:
    for j in matching_clubs:
      if len(filtered_matching_clubs) == 2:
        break
      if matching_clubs[j] > 0.1:
        filtered_matching_clubs[j] = matching_clubs[j]
  elif len(matching_clubs) <= 8:
    for j in matching_clubs:
      if len(filtered_matching_clubs) == 3:
        break
      if matching_clubs[j] > 0.12:
        filtered_matching_clubs[j] = matching_clubs[j]
  elif len(matching_clubs) > 8:
    for j in matching_clubs:
      if len(filtered_matching_clubs) == 5:
        break
      if matching_clubs[j] > 0.15:
        filtered_matching_clubs[j] = matching_clubs[j]

  sorted_dict = dict(sorted(filtered_matching_clubs.items(), key=lambda item: item[1]))
  return list(sorted_dict.keys())[::-1]



# ##Open_Ended Question

# In[57]:


import re
import numpy as np



#filtering sentence to make similarity scores more relevent
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

#finding relevent clubs
#TODO: Might need to split a group of sentences into individual sentences and check mean of similarity score for each sentence
def interest_similarity(club_descriptions, user_input):
  model = SentenceTransformer('all-MiniLM-L6-v2')
  unfiltered_clubs = {}
  filtered_clubs = {}
  for i in range(len(club_descriptions)):
    mean = []
    sentences = re.split(r'[.!?]', club_descriptions[i])
    sentences = [s.strip() for s in sentences if s.strip()]
    for a in range(len(sentences)):
      sentences[a] = filter_sentence(sentences[a])

      user_embedding = model.encode(user_input, convert_to_tensor=True)
      club_embedding = model.encode(sentences[a], convert_to_tensor=True)
      cosine_similarity = util.cos_sim(user_embedding, club_embedding)
      mean.append(cosine_similarity)
    unfiltered_clubs[i] = np.mean(np.array(mean))

  if len(unfiltered_clubs) <= 4:
    for j in unfiltered_clubs:
      if len(filtered_clubs) == 2:
        break
      if unfiltered_clubs[j] > 0.12:
        filtered_clubs[j] = unfiltered_clubs[j]
  elif len(unfiltered_clubs) <= 8:
    for j in unfiltered_clubs:
      if len(filtered_clubs) == 3:
        break
      if unfiltered_clubs[j] > 0.15:
        filtered_clubs[j] = unfiltered_clubs[j]
  elif len(unfiltered_clubs) > 8:
    for j in unfiltered_clubs:
      if len(filtered_clubs) == 5:
        break
      if unfiltered_clubs[j] > 0.2:
        filtered_clubs[j] = unfiltered_clubs[j]

  sorted_dict = dict(sorted(filtered_clubs.items(), key=lambda item: item[1]))
  return list(sorted_dict.keys())[::-1]







# #Final Implementation

# In[58]:


def indicesOfMatchingClubs(club_descriptions, teamwork,community_service,leadership,learning,critical_thinking,hobbies,club_wants):
  questions = {"teamwork": teamwork,
          "community_service": community_service,
          "leadership": leadership,
          "learning": learning,
          "critical_thinking": critical_thinking,
          "hobbies": hobbies,
          "club_wants": club_wants
          }
  user_input = [questions["hobbies"] + ". " + questions["club_wants"]]
  user_attributes = [questions["teamwork"],questions["community_service"],questions["leadership"],questions["learning"],questions["critical_thinking"]]

  return list(np.unique(np.array((interest_similarity(club_descriptions, user_input) + match_clubs(club_descriptions, user_attributes)))))

def listOfMatchingClubs(event_descriptions,club_titles,club_descriptions, teamwork,community_service,leadership,learning,critical_thinking,hobbies,club_wants):
  finalClubs = {}
  print("IN LIST OF MATCHING CLUBS")
  try:
    for i in indicesOfMatchingClubs(club_descriptions, teamwork,community_service,leadership,learning,critical_thinking,hobbies,club_wants):
      finalClubs[club_titles[i]] = event_descriptions[i]
  except Exception as e:
    print(f"An error occurred: {e}")
  print(finalClubs)
  return finalClubs