# Overview

Here I'm looking at the 1976-2020 US election data. You can download it [here](https://www.kaggle.com/datasets/tunguz/us-elections-dataset) from Kaggle.

I'm using the python pandas module to convert the csv into a dataframe object and filter through it.

Given the recent US election (I'm doing this November 2024) I wanted to see how US voters behave and why people vote the way that they do.
Its quite a complicated question, so I'm just looking at a few metrics to get an overview of the history.


[Software Demo Video](https://youtu.be/ERALdrpaf4U)

# Data Analysis Results

I wanted to know which states were the most volitile, and which states have their voting preferences change the most over time. The answer to both is West Virginia- It went from a strong democratic state to one of the strongest republican strongholds in a realitively short time. Who knows what caused this change? The fact that West Virginia is both is perhaps a flaw in how I'm calculating my numbers; I'm just looking at the difference between the most support for a party and the least. Perhaps a better method would be to look at the difference between each voting year and his neighbors. Some states do have large differences though, like Utah, which is the slowest changing state but higher than average volatility.

The results suggest that states like West Virginia have either had a mass exodus/influx of people, or the parties have changed their platform more to appeal to them. Other states like Utah have not changed their pattern that much but are willing to change their vote for a particular candidate, like Mitt Romney from their state.

Making conclusions is a lot tougher than just looking at a dataset, but I would guess that the parties have divided themselves by urban/rural lines. The states that have become more Democratic are quite urban and wealthy (California, DC) wheras the states that have become more Republican and poor (West Virginia, Alabama). I can't easily see a pattern for which states have the most volatile (or rather, most easily convinced) voters.

# Development Environment

This was developed in Visual Studio Code.

I'm using Python with the Pandas module.

# Useful Websites
Most of the help I used came from the Pandas user guides.
* [Pandas.dataframe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
* [Pandas IO Tools](https://pandas.pydata.org/docs/user_guide/io.html)

# Future Work

There are a million things that could be done to get a different perspective on US elections.
* I think my measure of volatility is poor, and I couldn't glean much from it. It would take some thinking to determine a better way to calculate the numbers.
* A fun idea would be to use an AI api to give some guesses on why the data looks like it does; like why did everyone hate Bob Dole?
* Ideally I would project the numbers onto a map with shaded colors and could see them change over time...