import json

if __name__ == "__main__":
    with open('./emoji-list.json') as emoji_list:
      data = json.load(emoji_list)
      print(data)