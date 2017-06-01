#reddit??
import praw, re, math
reddit = praw.Reddit('bot')
subreddit = reddit.subreddit("ZomBMage")
while True:
    while True:
        for submission in subreddit.hot(limit=5):
            donelist = []
            with open("posts_replied_to.txt", "r") as file:
                replied_to = file.read()
                replied_to = replied_to.split("\n")
                replied_to = list(filter(None, replied_to))
                string = submission.title
                string = ("").join(re.split(" ", string))
                string = ("").join(re.split(",", string))
                if submission.id not in replied_to:
                    negative = re.findall("-\d+!", string)
                    decimal = re.findall("\d+\.\d+!", string)
                    normeal = re.findall(".+\d+!", string)
                    normeal = list(filter(None, re.split("!", "".join(normeal))))
                    negative = list(filter(None, re.split("!", "".join(negative))))
                    decimal = list(filter(None, re.split("!", "".join(decimal))))
                    for item in normeal:
                        if item in negative:
                            donelist.append("Negative numbers cannot be factorialised.")
                        elif item in decimal:
                            donelist.append("Non-integer numbers cannot be factorialised.")
                        else:
                            try:
                                done = math.factorial(int(item))
                                if str(done).endswith("000") == True:
                                        done = "~" + str(done)
                                donelist.append(str(item)+"! = "+str(done))
                            except:
                                print("",end="")
                #postbody time!
                string = submission.selftext
                string = ("").join(re.split(" ", string))
                string = ("").join(re.split(",", string))
                if submission.id not in replied_to:
                    negative = re.findall("-\d+!", string)
                    decimal = re.findall("\d+\.\d+!", string)
                    normeal = re.findall(".+\d+!", string)
                    normeal = list(filter(None, re.split("!", "".join(normeal))))
                    negative = list(filter(None, re.split("!", "".join(negative))))
                    decimal = list(filter(None, re.split("!", "".join(decimal))))
                    for item in normeal:
                        if item in negative:
                            donelist.append("Negative numbers cannot be factorialised.")
                        elif item in decimal:
                            donelist.append("Non-integer numbers cannot be factorialised.")
                        else:
                            try:
                                done = math.factorial(int(item))
                                if str(done).endswith("000") == True:
                                        done = "~" + str(done)
                                donelist.append(str(item)+"! = "+str(done))
                            except:
                                print("",end="")
                        submission.reply("""
    
        """.join(donelist)+"""

\^bleep \^bloop \^i \^am \^a \^bot.


\^contact \^u/ZomBMage \^about \^questions


\^I \^am \^a \^testing \^bot""")
                        replied_to.append(submission.id)
                        with open("posts_replied_to.txt", "w") as file:
                            for post_id in replied_to:
                                file.write(post_id + "\n")
                else:
                    print("",end="")
                
            for comments in subreddit.comments(limit=10):
                donelist = []
                with open("comments_replied_to.txt", "r") as filec:
                    replied_comment = filec.read()
                    replied_comment = replied_comment.split("\n")
                    replied_comment = list(filter(None, replied_comment))
                    if comments.author.name != "ZomBMageBOT":
                        if comments.id not in replied_comment:
                            string = re.split(",", comments.body)
                            string = ("").join(re.split(" ", string))
                            string = ("").join(re.split(",", string))
                            if submission.id not in replied_to:
                                negative = re.findall("-\d+!", string)
                                decimal = re.findall("\d+\.\d+!", string)
                                normeal = re.findall(".+\d+!", string)
                                normeal = list(filter(None, re.split("!", "".join(normeal))))
                                negative = list(filter(None, re.split("!", "".join(negative))))
                                decimal = list(filter(None, re.split("!", "".join(decimal))))
                                for item in normeal:
                                    if item in negative:
                                        donelist.append("Negative numbers cannot be factorialised.")
                                    elif item in decimal:
                                        donelist.append("Non-integer numbers cannot be factorialised.")
                                    else:
                                        try:
                                            done = math.factorial(int(item))
                                            if str(done).endswith("000") == True:
                                                    done = "~" + str(done)
                                            donelist.append(str(item)+"! = "+str(done))
                                        except:
                                            print("",end="")
                                comments.reply("""

        """.join(donelist)+"""

\^bleep \^bloop \^i \^am \^a \^bot.


\^contact \^u/ZomBMage \^about \^questions


\^I \^am \^a \^testing \^bot""")
                            replied_comment.append(comments.id)
                            with open("comments_replied_to.txt", "w") as filec:
                                for comment_id in replied_comment:
                                    filec.write(comment_id + "\n")
            
