## How to run

### Requirements:
Although I ran this with Python 2.7.10 any of the latest version would work. If you don't have Python use this link         https://www.python.org/downloads/

Then clone this repo or copy the files. To run the code, you will need an int amount and a file with the gifts. I have an example file uploaded to check the format:

    Candy Bar, 500
    Paperback Book, 700
    Detergent, 1000
    Headphones, 1400
    Earmuffs, 2000
    Bluetooth Stereo, 6000

First column being names, second being prices. 

If your gifts file was filename.txt and your gift card amount was 5000 , here's how you'd run it:

    Python giftCard.py filename.txt 5000
    ['Earmuffs', 2000]
    ['Headphones', 1400]
    
 
 (change giftCard.py to giftCardBonus.py for the bonus question)
 
 ## How I solved it and Runtime. 
 
 Given that there could be many rows, a brute force solution was pretty much out of the question as it would give a very poor runtime. Here we know that the list of prices is sorted and so, we can use that to our advantage. 
 
We start pointing at the bottom of the list (most expensive item) and top of the list (cheapest item). We check what the total price would be with the current combo of items. If the current combo costs more than our budget then we move our bottom pointer a notch up to get a cheaper item. If the current combo costs less, this means we have room to spend more and move a notch lower on the top pointer for a more expensive item. 

We keep moving inwards, each time keeping track of the least difference from our budget and storing that combination of items. In the end, we either have a best combination (or more, but doesn't matter here) or none. 

### runtime
This way by starting at both ends and moving inwards we traverse the list only once and our runtime is O(N). 


### Bonus Question

With a three way split one way to approach is it to use the same algorithim that we used for two elements but on N different subsets of the list. For instance the third option starts at the bottom. Now for the other two options, we will use the same method of moving inwards (while the third option is fixed). Then we move the third option one step and do the same.

### runtime for bonus

Here the third option has to go only once through the list, which is N but for every time it goes through the list the O(N) algorithim is being called so in this case our runtime will be O(N^2).



NOTE: In in the interest of time/purpose of this question I have not containerized this or deployed it to any service. Of course, I am happy to discuss how this can be deployed in a better manner. 
