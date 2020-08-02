========
Nude-Man
========

************
What is It?
************
Nude-Man is a command-line based utility that can scan a given directory (and it's sub-directories) for images that are deemed "Not Safe for Work" (NSFW) identify said images, and then move them to a specified directory for safe (and discreet) keeping!

**********************
How? Are You a Wizard?
**********************
No, silly. I'm a programmer that knows how to query online APIs. The one I made this program query (or; upload your images to) can be found at `DeepAI.org <https://deepai.org>`_. This is also where you can get the API key that you'll need in order for the program to work.

***************
Getting Started
***************
If you bear in mind that Nude-Man is still in development, and you may encounter bugs you can use the program by following these steps:

1. Install Poetry: ``python3 -m pip install poetry``

2. Download the program from GitLab: ``git clone https://gitlab.com/tayjaybabee/nude-man.git``

3. Enter the program directory

4. Use Poetry to install program deps: ``poetry install``

5. Build using Poetry: ``poetry build``

6. Enter the build directory

7. Install the available .whl file: ``python3 -m pip install nude-man<version>.whl``

8. Run Nude-Man once: ``nude-man -s .``

9. A new directory and a config file was created when you did this, usually in '/home/USER/Inspyre-Softworks/Nude-Man' in that directory you will find run/conf. Edit nude-man.conf as needed.

10. Navigate to the directory you  want to start your scan in, and scan: ``nude-man -s . -o /home/user/Pictures/Private``
