import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class PersonalizeRecommendations:
    def __init__(self, articles):
        self.articles = articles
        self.tfidf_matrix = self._create_tfidf_matrix()
    
    def _create_tfidf_matrix(self):
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(self.articles['content'])
        return tfidf_matrix
    
    def get_recommendations(self, article_index, num_recommendations=5):
        cosine_sim = linear_kernel(self.tfidf_matrix, self.tfidf_matrix)
        sim_scores = list(enumerate(cosine_sim[article_index]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:num_recommendations+1]
        article_indices = [i[0] for i in sim_scores]
        return self.articles.iloc[article_indices]

# Sample usage:
# articles = pd.read_csv('news_articles.csv')
# personalize = PersonalizeRecommendations(articles)
# recommended_articles = personalize.get_recommendations(0)