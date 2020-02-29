from copy import deepcopy
import pandas as pd
import numpy as np
import pandas.io.sql as pd_sql
import psycopg2 as pg

class recommender():
    def __init__(self, sql_conn):
        # cosine_sim query
        query = '''
        select *
        from cosine_sim
        '''
        
        # pull from sql and convert columns
        self.cosine_sim = pd_sql.read_sql(query, sql_conn)
        self.cosine_sim.columns = self.cosine_sim.columns.astype(int)
        
        # rec_df (topic_matrix) query
        query = '''
        select *
        from rec_df
        '''
        
        # get table, set index to podcast title column,
        # delete the name of the index
        self.topic_matrix = pd_sql.read_sql(query, sql_conn)
        self.topic_matrix = self.topic_matrix.set_index('index')
        # print('Topic matrix name: ',self.topic_matrix.index)
        # del self.topic_matrix.index.name
        
        # url_descs query
        query = '''
        select *
        from url_descs
        '''
        
        # original iloc index pushed up to 'level_0',
        # sort on and delete level_0
        self.url_descs = pd_sql.read_sql(query, sql_conn).sort_values('level_0')
        self.url_descs = self.url_descs.set_index('level_0').fillna('').set_index('index')
        # del self.url_descs.index.name
    
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