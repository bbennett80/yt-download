from pytube import YouTube
import pandas as pd

link = input('Paste the link of the video: ')
print('\n')

yt = YouTube(link)
print(f'Preparing "{yt.title}" for download.', '\n')

response = input('Is this correct? Y/N  ')
print('\n')

if response.lower() == 'y':
    stream = yt.streams.filter()

    table = []

    for i in stream:
        tag = str(i)
        tags = tag.replace('<', '').replace('>', '').replace('Stream: ', '').replace('"', '').replace(' ', ',')
        tags_df = tags.split(',')
        table.append(tags_df)


    df = pd.DataFrame(data=table)
    df = df.drop(columns=[3, 4, 5, 6, 7])
    df = df.rename(columns={0: "Tag", 1: "Type", 2: "Resolution"})
    df['Tag'] = df['Tag'].str.replace('itag=', '')
    df['Type'] = df['Type'].str.replace('mime_type=', '')
    df['Resolution'] = df['Resolution'].str.replace('res=', '').str.replace('abr=', '')

    print(df.to_string(index=False), '\n')
    

    itag = input('Enter tag number: ')
    print('\n')
    print(f'Downloading "{yt.title}"...', '\n')
    yt.streams.get_by_itag(itag).download()
    print('Download complete:)')
else:
    print('Exiting program')
