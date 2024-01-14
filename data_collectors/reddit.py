import praw
from praw.reddit import Submission
from typing import List

from config.settings import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET


class RedditClient:
    def __init__(self, user_agent: str = 'DefaultClient/0.1 by FitnessMemeGenerator'):
        self.reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                                  client_secret=REDDIT_CLIENT_SECRET,
                                  user_agent=user_agent)

    def get_top_posts(self, subreddit: str, limit: int = None) -> List[Submission]:
        page = self.reddit.subreddit(subreddit)
        return list(page.hot(limit=limit))
