-- Write your MySQL query statement below
SELECT TWEET_ID 
FROM TWEETS
WHERE char_length(CONTENT) >15
