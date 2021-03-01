import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

print(res.status_code)  # prints status 200 is good

print(res.raise_for_status())  # checks for any error

print(len(res.text))  # length of downloaded response

print(res.text[:500])  # slice printing 500 first words

play_file = open('Romeo_and_Juliet.txt', 'wb')

for chunk in res.iter_content(10000):
    play_file.write(chunk)

play_file.close()
