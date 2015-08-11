# MelbDjango School Lesson Four

### Assignment 1

**Important:** Check out our first assignment here: https://github.com/melbdjango/melbdjango-assignment

---


Congratulations, you've made it to the git repository for our fourth lesson. Hopefully you also made it to the class
and some of this makes sense to you.

Check our RESOURCES.md for some links we think you'll find handy.


## Homework Checklist

- [x] [Fork this repository][gh-fork]
- [x] Clone the repo to your own machine
- [x] Use the virtualenv you created in previous lesson
- [x] Create forms to create new Projects and Clients (look at our EntryForm to see how to handle ForeignKey relationships)
- [x] Add those forms to your views and templates so that users can create new Clients and Projects
- [x] Add some validation to make sure that start time is in the past
- [x] Validate that the end time is after the start time
- [x] Bonus Points #1: Think about making our form look a little nice with some CSS
- [x] Bonus Points #2: Add the ability to edit existing Projects and Clients

When you've completed some or all of the homework please make a [Pull Request][gh-pr] against this repository. If you submit
your work before Wednesday evening we'll give you feedback before the next class.

If you'd like help, make a Pull Request with your incomplete work and ask a question to @darrenfrenkel, @sesh or
@funkybob.


## Displaying the class slides

Install reveal-md with npm and use that to display the class slides.

```
    npm install -g reveal-md
```

From within the `lesson-four` repo:

```
    cd slides
    reveal-md CLASS.md --theme melbdjango
```

[gh-fork]: https://help.github.com/articles/fork-a-repo/
[gh-pr]: https://help.github.com/articles/using-pull-requests/
[dj-request-response]: https://docs.djangoproject.com/en/1.8/ref/request-response/
[mdn-html]: https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Introduction
