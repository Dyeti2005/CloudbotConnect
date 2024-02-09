from .bot_responses import *
import random
import re

class Chatbot:
    def __init__(self):
        self.response_probabilities = {}

    def reply(self, user_input):
        split_user_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
        response = self.check_all_messages(split_user_message)
        return response

    def calculate_message_probability(self, user_message, recognized_words):
        if not recognized_words:
            return 0

        matching_word_count = sum(1 for word in user_message if word in recognized_words)
        matching_percentage = float(matching_word_count) / float(len(recognized_words))
        
        return int(matching_percentage * 100)

    def check_all_messages(self, user_message):

        def update_response_probabilities(bot_response, keywords):
            self.response_probabilities[bot_response] = (
                self.calculate_message_probability(user_message, keywords)
            )
        
        for key, data in options.items():
            current_keywords = data["keywords"]
            response_text = data["response"]

            update_response_probabilities(response_text, current_keywords)
        
        best_matched_response = max(self.response_probabilities, key=self.response_probabilities.get)
 
        if self.response_probabilities[best_matched_response] < 1:
            return ['¿Puedes repetir eso?', 'No estoy seguro de lo que deseas'][random.randrange(2)]

        return best_matched_response