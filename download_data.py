import pandas as pd
import json
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

def convert_json_to_df(json_file_path):
    data = pd.read_json(json_file_path)
    data = data.T.reset_index()
    list_name = []
    list_comment_karma = []
    list_link_karma = []
    list_type = []
    list_body = []
    list_subreddit = []
    for i in range(len(data)):
        comments = data['comments'][i]
        submissions = data['submissions'][i]
        for j in range(len(comments)):
            list_name.append(data['name'][i])
            list_comment_karma.append(data['comment_karma'][i])
            list_link_karma.append(data['link_karma'][i])
            list_type.append('comment')
            list_body.append(comments[j]['body'])
            list_subreddit.append(comments[j]['subreddit'])
            
        for k in range(len(submissions)):
            list_name.append(data['name'][i])
            list_comment_karma.append(data['comment_karma'][i])
            list_link_karma.append(data['link_karma'][i])
            list_type.append('submission')
            list_body.append(submissions[k]['title'] + " : " + submissions[k]['body'])
            list_subreddit.append(submissions[k]['subreddit'])
    list_columns = ['name', 'comment_karma', 'link_karma', 'type', 'body', 'subreddit']
    df = pd.DataFrame(columns=list_columns)
    df['name'] = list_name
    df['comment_karma'] = list_comment_karma
    df['link_karma'] = list_link_karma
    df['type'] = list_type
    df['body'] = list_body
    df['subreddit'] = list_subreddit
    return df

df = convert_json_to_df("data/redditor_personnalities_0.json")
for i in range(1,21):
    df = pd.concat([df, convert_json_to_df("data/redditor_personnalities_" + str(i) + ".json")], ignore_index=True)

df.to_csv('data/redditor.csv',index=False)

with open('data/redditor_personnalities_dict__.json') as mon_fichier:
    file_y = json.load(mon_fichier)
df_y = pd.json_normalize(file_y).T.reset_index()
df_y.columns = ['name', 'personality']
df_y.to_csv('data/dict.csv',index=False)

df2 = convert_json_to_df("data/redditor_info_scammer_5.json")
df2.to_csv('data/scammer.csv',index=False)

T=[1]*len(df2)
df2['label'] = T

df=pd.read_csv('data/redditor.csv')
T1=[0]*len(df)
df['label'] = T1

df__=pd.concat([df,df2], ignore_index=True)
df__= shuffle(df__)

train, test = train_test_split(df__, test_size=0.2, random_state=42)
train.to_csv('data/train.csv',index=False)
test.to_csv('data/test.csv',index=False)