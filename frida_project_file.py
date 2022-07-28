#!/usr/bin/env python
# coding: utf-8

# # Frida Kahlo Exhibition
# 
# You've been hired to work on a retrospective of Frida Kahlo's work at a major museum. Your job is to put together the audio tour, but in order to do that you need to create a list of each painting featured in the exhibit, the date it was painted, and its spot in the tour. 
# 
# Use your knowledge of Python lists to create a master list of each painting, its date, and its audio tour ID. 
# 

# ## Task 1
# First, create a list called `paintings` and add the following titles to it:
# 
# `The Two Fridas, My Dress Hangs Here, Tree of Hope, Self Portrait With Monkeys`
# 

# In[13]:


paintings = ["The Two Fridas", "My Dress Hangs Here", "Tree of Hope", "Self Portrait With Monkeys"]


# ## Task 2
# 
# Next, create a second list called `dates` and give it the following values:
# `1939, 1933, 1946, 1940`

# In[14]:


dates = [1939, 1933, 1946, 1940]


# ## Task 3 
# It doesn't do much good to have the paintings without their dates, and vice versa. 
# Zip together the two lists so that each painting is paired with its date and resave it to the `paintings` variable. Make sure to convert the zipped object into a list using the `list()` function. Print the results to the terminal to check your work. 

# In[15]:


paintings = list(zip(paintings, dates))
print(paintings)


# ## Task 4
# There were some last minute additions to the show that we need to add to our list. Append the following paintings to our `paintings` list then re-print to check they were added correctly:
# - 'The Broken Column', 1944
# - 'The Wounded Deer', 1946
# - 'Me and My Doll', 1937
# 
# Hint: Make sure to append each painting individually and that you're appending them as tuples, not lists. 

# In[16]:


paintings.append(("The Broken Column", 1944))
paintings.append(("The Wounded Deer", 1946))
paintings.append(("Me and My Doll", 1937))

print(paintings)


# ## Task 5
# Since each of these paintings is going to be in the audio tour, they each need a unique identification number.
# But before we assign them a number, we first need to check how many paintings there are in total.
# 
# Find the length of the `paintings` list.

# In[17]:


len(paintings)


# ## Task 6
# Use the `range` method to generate a list of identification numbers that starts at 1 and is equal in length to our list of items. 
# Save the list to the variable `audio_tour_number` and check your work by printing the list.

# In[18]:


audio_tour_number = list(range(1, 8))
print(audio_tour_number)


# ## Task 7 
# 
# We're finally read to create our master list. 
# Zip the `audio_tour_number` list to the `paintings` list and save it as `master_list`.
# 
# Hint: Make sure to convert the zipped object into a list using the `list()` function.

# In[19]:


master_list = list(zip(audio_tour_number, paintings))


# ## Task 8 
# Print the `master_list` to the terminal.

# In[20]:


print(master_list)

