import os
from handmaiden import Handmaiden

if __name__ == '__main__':
    token = os.environ['TOKEN']
    bot = Handmaiden(token)
    bot.run()
