import pandas as pd
# work in jupiter its not working were
#pd.set_option('display.max_colwidth', None)
jeopardy_file = pd.read_csv('jeopardy.csv')
# if we use print the columns we can see the index and helps us to know what we going to use and study
print(jeopardy_file.columns)

jeopardy_file = jeopardy_file.rename(columns = {' Air Date' : 'Air Date',' Round' : 'Round', ' Category' : 'Category', ' Value' : 'Value',
       ' Question' : 'Question', ' Answer' : 'Answer'})
print(jeopardy_file.columns)
print(jeopardy_file['Round'])

#now we going to create a function that help the find our filter our questions if we need to find the a question
def find_data(data, words):
    find = lambda x: all(word.lower() in x.lower() for word in words)
    return data.loc[data['Question'].apply(find)]

find_questions = find_data(jeopardy_file, ["King","England"])
print(find_questions['Question'])

#we want to aggregate  statistics but we need to convert to floats firts and create a new column 
def convert_float(data, new_column_name, old_column_name):
    data[new_column_name] = data[old_column_name].apply(lambda x: float(x[1:].replace(',','')) if x != "no value" else 0)
    
new_column = convert_float(jeopardy_file, 'Float Value', 'Value')
filters = find_data(jeopardy_file, ['King'])

print(filters["Float Value"].mean())

#we want to return the count of unique answes to all question that contains "king" we going to create a funciton we goping to use value_counts() from panda lib  
def answer_count(data):
    return data['Answer'].value_counts()

print(answer_count(filters))
