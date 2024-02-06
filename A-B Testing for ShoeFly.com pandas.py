import codecademylib3
import pandas as pd
import numpy as np

#see how table 
ad_clicks = pd.read_csv('ad_clicks.csv')
#print(ad_clicks.head(10))

#how many views which ad platfomor utm have
utm_source = ad_clicks.groupby('utm_source').count().reset_index()
#print(utm_source)


#not working
#ad_clicks['is_click'] = ad_clicks.apply(lambda click: True if click.ad_click_timestamp != None else False, axis=1)
#~ is a NOT operation and isnull tste if the value is if row is null or not
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
#print(ad_clicks.head(10))

clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()
#print(clicks_by_source)
#print(ad_clicks.head(10))
experimental_group = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()

experimental_group_pivot = experimental_group.pivot(columns='is_click', index='experimental_group',values='user_id').reset_index()
#print(experimental_group_pivot)

a_clicks= ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks= ad_clicks[ad_clicks.experimental_group == 'B']

aclicks = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
bclicks= b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()

#print(aclicks)

# For each group (a_clicks and b_clicks), calculate the percent of users who clicked on the ad by day.
a_clicks = a_clicks.groupby(['day','is_click']).user_id.count().reset_index()
print(a_clicks)
a_clicks = a_clicks.pivot(columns='is_click', index='day', values='user_id').reset_index()
print(a_clicks)
a_clicks['percent'] = 100*a_clicks[True] / (a_clicks[True]+a_clicks[False])
print(a_clicks)
b_clicks = b_clicks.groupby(['day','is_click']).user_id.count().reset_index()
b_clicks = b_clicks.pivot(columns='is_click', index='day', values='user_id').reset_index()
b_clicks['percent'] = 100*b_clicks[True] / (b_clicks[True]+b_clicks[False])
print(b_clicks)







