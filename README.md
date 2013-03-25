R-stat
======

R-stat delivers the front page of internet right to your front door!  Well, to 
your commandline at least.  Passing optional arguments to R-stat will return 
data from posts on the super awesome website http://www.reddit.com.

There are a variety options you can supply depending on what you'd like to see.
If you want to know what time of day your favorite subreddit is rife with activity,
R-stat is able to give you a graph of the time all the recent posts were made.
This graph data is converted to your local time so you know when to be checking.

Maybe people on your subreddit share a ton of images.  R-stat can check for image
data and download.

Just the same R-stat can format the basic data from which ever sub you'd like and
print it to your terminal.

There are a couple of modules not included in python's standard library and they
will need to be installed first.

You can:

    pip install requests

As for the matplotlib module, there are some issues with pip-install apparently.  If
you have apt installed, you could go this route.

    sudo apt-get install python-matplotlib 


Here's a small sample of R-stat output:

    ./rstat.py -ScatU
    Which sub-reddit do you want statistics for?: learnpython

    /r/learnpython/ --->

    -------------------------------------------
    How to put multiple print statements into one line including multiple variables?
        Author: JaruJaru
        Time Posted: Thu Feb 28 00:45:44 2013
        Url: http://www.reddit.com/r/learnpython/comments/19dqpo/how_to_put_multiple_print_statements_into_one/
        Total Comments: 3
    -------------------------------------------
    Unit testing with root priviledges
        Author: demizer
        Time Posted: Wed Feb 27 17:25:45 2013
        Url: http://www.reddit.com/r/learnpython/comments/19cti6/unit_testing_with_root_priviledges/
        Total Comments: 2
    -------------------------------------------
    New to programming, having trouble printing for loops in functions [Windows, python 3.3.0]
        Author: luiginut
        Time Posted: Wed Feb 27 16:39:50 2013
        Url: http://www.reddit.com/r/learnpython/comments/19cprr/new_to_programming_having_trouble_printing_for/
        Total Comments: 9
    -------------------------------------------

