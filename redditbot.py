# reddit??
import praw
import re
import math
import os

reddit = praw.Reddit('bot')
subreddit = reddit.subreddit("ZomBMage")

def touch(file): #Emulates the touch command in Linux distros
    if not os.path.exists(file):
        open(file, 'w').close()
    return file


def submissions(text, array):
    negative = re.findall("-\d+!", text)
    decimal = re.findall("\d+\.\d+!", text)
    normeal = re.findall(".+\d+!", text)
    normeal = list(filter(None, re.split("!", "".join(normeal))))
    negative = list(filter(None, re.split("!", "".join(negative))))
    decimal = list(filter(None, re.split("!", "".join(decimal))))
    for item in normeal:
        if item in negative:
            array.append("Negative numbers cannot be factorialised.")
        elif item in decimal:
            array.append("Non-integer numbers cannot be factorialised.")
        else:
            try:
                done = math.factorial(int(item))
                if str(done).endswith("000"):
                    done = "~" + str(done)
                done_list.append(str(item) + "! = " + str(done))
            except OverflowError:
                print("", end="")


def string_split(text_input):
    string_one = ().join(re.split(" ", text_input))
    string_two = ().join(re.split(",", string_one))
    return string_two


def reply(content, replied_list):
    content.reply("""
            """.join(replied_list) + """
    \^bleep \^bloop \^i \^am \^a \^bot.
    \^contact \^u/ZomBMage \^about \^questions
    \^I \^am \^a \^testing \^bot""")


if __name__ == "__main__":
    while True:
        for submission in subreddit.hot(limit=5):
            done_list = []

            f = touch("posts_replied_to.txt")
            with open(f, "r") as file:
                replied_to = file.read()
                replied_to = replied_to.split("\n")
                replied_to = list(filter(None, replied_to))
                string = string_split(submission.title)

                if submission.id not in replied_to:
                    submissions(string, done_list)

                string = string_split(submission.selftext)
                if submission.id not in replied_to:
                    submissions(string, done_list)
                    reply(submission, done_list)
                    replied_to.append(submission.id)

            with open("posts_replied_to.txt", "w") as file:
                for post_id in replied_to:
                    file.write("{0}\n".format(post_id))

            for comments in subreddit.comments(limit=10):
                done_list = []
                f = touch("comments_replied_to.txt")
                with open(f, "r") as filec:
                    replied_comment = filec.read()
                    replied_comment = replied_comment.split("\n")
                    replied_comment = list(filter(None, replied_comment))
                    if comments.author.name != "ZomBMageBOT":
                        if comments.id not in replied_comment:
                            string = string_split(comments.body)
                            if submission.id not in replied_to:
                                submissions(string, done_list)
                                reply(comments, done_list)
                                replied_comment.append(comments.id)
                with open("comments_replied_to.txt", "w") as filec:
                    for comment_id in replied_comment:
filec.write('{0}\n'.format(comment_id))
