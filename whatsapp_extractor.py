# whatsapp analyser by data exxtraction
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords


class WhatsApp:
    def __init__(self,filename):
        self.filename = filename

    def analyse(self):
        # file = open(self.filename,mode='r',encoding='utf8')
        # data = file.read()
        # content = data.splitlines()
        # filter_data = [x for x in content if '<Media omitted>' not in x]

        # Extracting data by name of user
        pat = re.compile(r'^(\d\d\/\d\d\/\d\d\d\d.*?)(?=^^\d\d\/\d\d\/\d\d\d\d|\Z)', re.S | re.M)
        with open(self.filename,encoding='utf8') as f:
            data = [m.group(1).strip().replace('\n', ' ') for m in pat.finditer(f.read())]
        sender = [];message = [];datetime = []
        for row in data:
            datetime.append(row.split('-')[0])

            try:
                # message content is after the first colon
                s = re.search('m - (.*?):', row).group(1)
                sender.append(s)
            except:
                sender.append('')

            try:
                message.append(row.split(': ', 1)[1])
            except:
                message.append('')
        df = pd.DataFrame(zip(datetime,sender,message),columns=['timestamp','sender','message'])
        df['timeframe'] = pd.to_datetime(df.timestamp)
        df = df[df.sender!= ''].reset_index(drop=True)

        # print(df['timeframe'])

        # Counting the number of messages sent by each sender
        count_senders = {}
        for i in range(len(df)):
            if df.sender[i] in count_senders.keys():
                count_senders[df.sender[i]] += 1
            else:
                count_senders[df.sender[i]] = 1
        # print(count_senders)

        # Defining the no pf characters in each message
        df['characters'] = df.message.apply(len)
        # print(df['characters'])

        # defining the number of words in each message
        df['words'] = df.message.apply(lambda x:len(x.split()))
        # print(df['words'])

        # average of number of words and characters sent by each user
        avg_sender = df.groupby('sender').mean().sort_values('characters').round(2)
        # print(avg_sender)

        freq_words = df.message.value_counts().head(20)
        #print(freq_words)

        words = ''
        for i in df.message.values:
            words += '{}'.format(i.lower()) # make words lowercase

        most_freq_words = pd.DataFrame(Counter(words.split()).most_common(20), columns=['word', 'frequency'])
        # print(most_freq_words)

        for i in Counter(words.split()).most_common(60):
            if i[0] not in stopwords.words('english'):
                print(i[0] + ',')

        # find time difference between current and previous message
        df['reply_time'] = (df.timestamp.shift(-1)-df.timestamp).apply(lambda x: x.total_seconds()/60).fillna(np.inf)
        # print(df['reply_time'])

        df['conversation'] = (df.reply_time > 20).cumsum().shift(1).fillna(0).astype(int) + 1

        df3 = df.groupby('conversation').agg({'timestamp':['min','max','count'],
                                              'sender':['first','unique','nunique']})
        df3['duration'] = (df3['timestamp']['max']-df3['timestamp']['min']).apply(lambda x:x.total_seconds()/60)
        print(df3)
        # return df

filename = 'WhatsApp Chat with 💐💐Saipriye 💐💐.txt'
object = WhatsApp(filename).analyse()
print(object)