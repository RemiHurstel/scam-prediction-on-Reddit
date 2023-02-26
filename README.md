# scam-prediction-on-Reddit

Authors : Zineb Bouharra, Rémi Hurstel, Ivo Bonetti, Ihssane Ghalas, Chaimaa Akharaze, Maroua El-Arni

Online scams are a prevalent issue on social media platforms such as Reddit. Scammers use deceptive tactics to lure unsuspecting users into fraudulent schemes, resulting in financial loss and other negative consequences. The detection of these scams is a challenging task, as scammers often use subtle language and manipulation techniques to evade detection. Therefore, the problem statement is to develop an effective scam prediction model for Reddit that can accurately identify and alert users to potential scam posts and comments, ultimately reducing the risk of financial harm and improving the overall safety and trustworthiness of the platform.

## Challenge description 
Get started with the [notebook](https://github.com/superjedi94/scam-prediction-on-Reddit/blob/main/reddit_starting_kit.ipynb). It contains : 
1. Problem statement 
2. Data Exploration
3. Pre-processing
4. Baseline Model
5. Evaluation
6. Submission Details 

## Data description

The [Universal Scammer List (USL)](https://www.universalscammerlist.com/) is a list of Reddit users who are banned from participating in certain communities (called subreddits) due to their problematic behavior. The list is maintained by a group of moderators from various subreddits who work together to identify and track problematic users. The purpose of the UBL is to prevent these users from causing harm or disruption in other communities and to provide a tool for moderators to easily identify and ban them.

The data contains information about a subset of these scammers as well as randomly selected users of Reddit. It includes information such as their name, ID, creation date, karma scores, as well as the user's most recent submissions and comments with their content, date and subreddit.

The data was collected using [The Python Reddit API Wrapper (PRAW)](https://praw.readthedocs.io/en/stable/index.html). The keys in the data correspond to the attributes of the objects [Redditor](https://praw.readthedocs.io/en/stable/code_overview/models/redditor.html), [Submission](https://praw.readthedocs.io/en/stable/code_overview/models/submission.html) and [Comment](https://praw.readthedocs.io/en/stable/code_overview/models/comment.html). All submissions and comments made in one of the participating subreddits of the USL were disregarded.

## Submission 
Submissions need to be located in the submissions folder.

To run a specific submission, you can use the ramp-test command line:
ramp-test --submission my_submission

#### Set up

Open a terminal and

1. install the `ramp-workflow` library (if not already done)
  ```
  $ pip install ramp-workflow
  ```
  
2. Follow the ramp-kits instructions from the [wiki](https://github.com/paris-saclay-cds/ramp-workflow/wiki/Getting-started-with-a-ramp-kit)




#### Help
Go to the `ramp-workflow` [wiki](https://github.com/paris-saclay-cds/ramp-workflow/wiki) for more help on the [RAMP](https://ramp.studio) ecosystem.

