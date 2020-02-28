from copy import deepcopy
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import linear_kernel

class recommender():
    def __init__(self, cosine_sim, topic_matrix, url_descs):
        self.cosine_sim = deepcopy(cosine_sim)
        self.topic_matrix = deepcopy(topic_matrix)
        self.url_descs = deepcopy(url_descs)
        
    def recommend_ep(self, title):
        title_idx = self.topic_matrix.index.get_loc(title)
        top_5_idx = list(
            pd.Series(
                self.cosine_sim[title_idx])
            .sort_values(ascending = False)
            .drop(title_idx)
            [:5]
            .index
        )
        
        recs = list(
            self.topic_matrix.iloc[top_5_idx,:]
            .index
        )
        
        tot_recs = self.url_descs.loc[recs,:].rename({1:'desc',2:'url'}, axis='columns')
        
        episodes = []
        descs = []
        urls = []
        for k,v in tot_recs.to_dict('index').items():
            episodes.append(k)
            descs.append(v['desc'])
            urls.append(v['url'])
        res_dict = {'episodes':episodes, 'descs':descs, 'urls':urls}
        return deepcopy(res_dict)
    
    def recommend_topic(self, topic):
        recs = list(
            self.topic_matrix[
                self.topic_matrix.idxmax(axis='columns') == topic
            ].sort_values(topic, ascending=False)
            [:5]
            .index
        )
        
        tot_recs = self.url_descs.loc[recs,:].rename({1:'desc',2:'url'}, axis='columns')
        episodes = []
        descs = []
        urls = []
        for k,v in tot_recs.to_dict('index').items():
            episodes.append(k)
            descs.append(v['desc'])
            urls.append(v['url'])
        res_dict = {'episodes':episodes, 'descs':descs, 'urls':urls}
        return deepcopy(res_dict)
        
    def get_topics(self):
        return list(self.topic_matrix.columns.values)
    
    def get_ep_names(self):
        return list(self.topic_matrix.index.values)