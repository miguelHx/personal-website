Title: Starting a New Blog
Date: 2018-12-18 07:20
Modified: 2018-12-18 07:20
Category: Personal
Tags: pelican, blogging, github-pages
Slug: starting-a-new-blog
Author: Miguel Hernandez
Summary: My thoughts on starting a new blog

I’m eager to share my thoughts through blogging.
My aim is to write posts on topics such as programming tutorials, thoughts about a particular technology, and whatever else comes to mind.

I started this blog using [Pelican](http://docs.getpelican.com/en/stable/), a static site generator written in Python.  The site is hosted on Github Pages.  Github Pages hosts static websites for free and it is
[fast](https://www.savjee.be/2017/10/Static-website-hosting-who-is-fastest/).

Pelican supports Markdown, which is really nice.  In general, it makes it straightforward for a developer to build a blog easily, assuming you are comfortable with the command line and Python.

Here's a random Python code snippet that draws a snowflake using Python's turtle library (it has nothing to do with this post. Just wanted to demonstrate how a code block looks using markdown):
```python
from turtle import Turtle
t = Turtle()
t.speed(0)
b = 180
for c in range(5):
 	a = 9*c
 	for i in range(100):
 		t.circle(i,a)
 		t.right(b)
 		t.circle(i,a)
 		t.right(b)
 		t.circle(i,a)
 		t.right(b)
 		t.circle(i,a)
input('Press any key to continue...')
```

