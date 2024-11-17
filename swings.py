# Which state has the most voters that have switched at least once? (Ie. volatility)
# Which state has changed the most over time (Ie. shift)

import pandas

PATH = "1976-2020-president.csv"
dataframe = pandas.read_csv(PATH)

# Remove writins from the data as there are some anomolies due to people writing in names that were already on the ballot
dataframe = dataframe.loc[lambda df: (df["writein"] == False), :] 

def abs(num):
    if (num < 0):
        num *= -1
    return num

def get_average_vote(dataframe, state, party):
    # Gets the average vote percentage in the dataset. Ie. if 40% of Alabamians voted democrat in 2016 and 45% did in 2020
    # then the average vote for those two years is 42.5%. It calculates it like you would expect...
    stateVotes = get_entries_for_state(dataframe, state)
    partyVotes = get_entries_for_party(stateVotes, party)
    percents = []
    for index in partyVotes.index:
        percent = partyVotes.at[index, "candidatevotes"] / partyVotes.at[index, "totalvotes"]
        percents.append(percent)
    percentsSeries = pandas.Series(percents)
    return percentsSeries.mean()

def get_states(dataframe):
    # Gets a list of all the states in the dataset. This is the states you would expect and also the district of columbia.
    stateList = []
    for entry in dataframe["state"]:
        if (entry not in stateList):
            stateList.append(entry)
    
    return stateList

def get_entries_for_state(dataframe, state):
    # Filters for one state.
    entries = dataframe.loc[lambda df: (df["state"] == state), :]
    return entries

def get_entries_for_party(dataframe, party):
    # Filters for one party.
    entries = dataframe.loc[lambda df: (df["party_simplified"] == party), :]
    return entries

def get_entries_from_years(dataframe, start, stop):
    # Filters by what year the election took place.
    entries = dataframe.loc[lambda df: ((df["year"] >= start)), :]
    entries = entries.loc[lambda df: ((df["year"] <= stop)), :]
    return entries

def get_spread(dataframe, state, party):
    # Approximates the number of voters in a state that have switched their votes at least once since 1976. 
    # Takes the highest support percentage the party has recieved and the lowest and subtracts them.
    min = 1
    max = 0
    stateVotes = get_entries_for_state(dataframe, state)
    partyVotes = get_entries_for_party(stateVotes, party)
    for index in partyVotes.index:
        percent = partyVotes.at[index, "candidatevotes"] / partyVotes.at[index, "totalvotes"]
        if (percent < min):
            min = percent
        if (percent > max):
            max = percent
    return max - min

def output_spread_for_all_states(dataframe):
    # Outputs a summary of the spreads of all the states.
    # Only considers the two main parties, and adds them together to dampen the effect of third parties.
    states = get_states(dataframe)
    max = 0
    min = 100
    maxState = ""
    minState = ""

    print("==============================")
    for state in states:
        result = 100*get_spread(dataframe, state, "REPUBLICAN")
        result += 100*get_spread(dataframe, state, "DEMOCRAT")
        result /= 2
        if (result < min):
            min = result
            minState = state
        if (result > max):
            max = result
            maxState = state
       # print(state + ": " + get_spread(dataframe, state, "REPUBLICAN"))
        print(f"{state}: {result:.1f}%")
    print("==============================")
    print(f"MAX: {maxState} {max:.1f}%")
    print(f"MIN: {minState} {min:.1f}%")

def output_state_spread_by_year_groupings(dataframe, cutoff):
    # Attempts to rank states by how much their voting prefrences have changed from before the cutoff to afterwards.
    dataframe_1 = get_entries_from_years(dataframe, 1976, cutoff-1)
    dataframe_2 = get_entries_from_years(dataframe, cutoff, 2020)
    states = get_states(dataframe)
    max = 0
    min = 100
    maxState = ""
    minState = ""
    print("==============================================")
    print(f"======1976 to {cutoff-1}========={cutoff} to 2020=======")
    for state in states:
        rep_1 = get_average_vote(dataframe_1, state, "REPUBLICAN") * 100
        rep_2 = get_average_vote(dataframe_2, state, "REPUBLICAN") * 100
        dem_1 = get_average_vote(dataframe_1, state, "DEMOCRAT") * 100
        dem_2 = get_average_vote(dataframe_2, state, "DEMOCRAT") * 100
        difference_1 = abs(rep_1 - rep_2)
        difference_2 = abs(dem_1 - dem_2)
        result = (difference_1 + difference_2)/2
        if (max < result):
            max = result
            maxState = state
        if (min > result):
            min = result
            minState = state
        print(f"{state}: {result:.1f}% -- REPUBLICAN {rep_1:.1f}% to {rep_2:.1f}% -- DEMOCRAT {dem_1:.1f}% to {dem_2:.1f}%")
    print(f"======1976 to {cutoff-1}========={cutoff} to 2020=======")
    print(f"MAX: {maxState} {max:.1f}%")
    print(f"MIN: {minState} {min:.1f}%")

def output_state_summary(dataframe, state, party):
    stateVotes = get_entries_for_state(dataframe, state)
    partyVotes = get_entries_for_party(stateVotes, party)
    print(f"===== {state} ===== {party} =====")
    for index in partyVotes.index:
        year = partyVotes.at[index, "year"]
        percent = (partyVotes.at[index, "candidatevotes"] / partyVotes.at[index, "totalvotes"]) * 100
        candidate = partyVotes.at[index, "candidate"]
        print(f"{year} - {percent:.1f}% - {candidate}")


# ========= Put function calls down below ===========

output_state_summary(dataframe, "DISTRICT OF COLUMBIA", "DEMOCRAT")



# ===================================================
