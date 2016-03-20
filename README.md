# Todo #
* Familiarize myself with the code base
* Pull in pre-existing python/flask server

# Goals #
Software tools to help track:

* Productivity:
    * Computer activity
    * Phone activity
* Health:
    * Weight
* Location:
* Goals:
* Tasks:

# Design Overview #
* Server that stores data, securely
    * If data sits on a third party site (Withings, Fitbit, Android Sleepbot,
      Moves), pull it local. You own the data.
    * Data scheme is smart, so you can cross-cut.
* Web site that allows you to view your data.
    * Choose what you'd like to publicly share
    * Section off what is private

# Tech Choices #
* C# for Windows based activity tracking
    * System Tray.
* Node webserver; node is most popular.
* SQLite DB; want to have structured data for joining.
* Android tracker

# Notes on Subtrees #
<code>Win.Api</code> comes from a separate repo, and is included via subtree
merging.

To access the subtree, add the remote:

    git remote add -f Win.Api git@github.com:phillipwei/Win.Api

To add the subtree:

    git subtree add --prefix cs/Win.Api Win.Api master --squash

To update:

    git subtree pull --prefix cs/Win.Api Win.Api master --squash

To push back:

    git subtree push --prefix cs/Win.Api Win.Api master
