# Table of Contents

1. [Challenge Summary] (README.md#challenge-summary)
2. [Details of Implementation] (README.md#details-of-implementation)


##Challenge Summary

The insight program had presented me with a project to create a digital-wallet "app" to process a few million lines of transactions between users. The app should contain 3 features:

###Feature 1
When anyone makes a payment to another user, they'll be notified if they've never made a transaction with that user before.

* "unverified: You've never had a transaction with this user before. Are you sure you would like to proceed with this payment?"

###Feature 2
The PayMo team is concerned that these warnings could be annoying because there are many users who haven't had transactions, but are still in similar social networks. 

For example, User A has never had a transaction with User B, but both User A and User B have made transactions with User C, so User B is considered a "friend of a friend" for User A.

For this reason, User A and User B should be able to pay each other without triggering a warning notification since they're "2nd degree" friends. 

<img src="./digital-wallet-master/images/friend-of-a-friend1.png" width="500">

To account for this, PayMo would like you to also implement this feature. When users make a payment, they'll be notified when the other user is outside of their "2nd-degree network".

* "unverified: This user is not a friend or a "friend of a friend". Are you sure you would like to proceed with this payment?"


###Feature 3
More generally, PayMo would like to extend this feature to larger social networks. Implement a feature to warn users only when they're outside the "4th degree friends network".

<img src="./digital-wallet-master/images/fourth-degree-friends2.png" width="600">

In the above diagram, payments have transpired between User

* A and B 
* B and C 
* C and D 
* D and E 
* E and F

Under this feature, if User A were to pay User E, there would be no warning since they are "4th degree friends". 

However, if User A were to pay User F, a warning would be triggered as their transaction is outside of the "4th-degree friends network."

(Note that if User A were to pay User C instead, there would be no warning as they are "2nd-degree" friends and within the "4th degree network") 


##Details of implementation


There are two inputs given; both are stored under the /paymo_input folder. One is "batch_payment.csv". This was used to create a network map mapping all the users to their adjacent neighbours (graphing theory). This was done by creating a python script (InitNetwork.py) to go through each line of the csv file and make a hash table (python dictionary). This dictionary represents the adjacency matrix, or atleast something that is analgous to that. For example if user A has sent money to user B, C, D, and F seen in 4 seperate lines in the batch_payment.csv; the python dictionary will contain the key 'A' with a list (B, C, D, F). The dictionary is stored in a python "pickle".

Once the matrix/network was created. A search algorithm called breadth first search was used to search through the matrix as each line in "stream_payment.csv" is processed (the proscessing is done via script checkpickles.py) This algorithm however was not sufficient to process the lines as some users have incredibly wide networks spanning wide which caused a problem for the breadth first algorithm. Therefore running the breadth first search to completley exhaust 4 degrees (as 4 degrees was the objective of feature 3) in the adjacency matrix would take an extremley long time. If the average number of "friends" each user had was N, the total searches would be an average maximum of N^4 searches. 

The solution to the problem encountered was to do a 2 sided breadth first search algorithm. One starting from the starting user, and the other starting from the end user. The average maximum time would be at most 2(N^2). If 2 degrees from both starting and ending users have been seached entirely, and no common user exists between the two user's visited nodes then the degree of seperation is more than 4 degrees, or no connection between the two users exist. 
