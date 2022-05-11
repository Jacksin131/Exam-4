#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import need packages
import pandas as pd


# In[2]:


# function that prints the the total possible and observed kmers in a string with their respective occurances
def number_kmers(string, k):
   # creates a dictionary of each possible substring and their respective number of occurances
    counts = {}
    kmers_num = len(string)-k+1
    for i in range(kmers_num):
        kmer = string[i:i+k]
        
        if kmer not in counts:
            counts[kmer] = 0
        counts[kmer] +=1   
    print(counts)
    
    # prints the total possible kmers
    values = []
    for i in counts:
        values.append(counts.get(i))
    print('Possible kmers total =', sum(values))
    print(' ')
    # prints the observed substrings with the total
    mers = []
    for i in counts:
        mers.append(str(i))
    print(mers)
    print('Observed kmers total =', len(mers))
    
    return


# In[3]:


# a function that returns just the total number of possible and observed kmers aswell as k
def raw_kmers(string, k):
   # creates a dictionary of each possible substring and their respective number of occurances
    counts = {}
    kmers_num = len(string)-k+1
    for i in range(kmers_num):
        kmer = string[i:i+k]
        
        if kmer not in counts:
            counts[kmer] = 0
        counts[kmer] +=1   
        
    # saves the total possible kmers
    values = []
    for i in counts:
        values.append(counts.get(i))
    x = sum(values)

    
    # saves the observed substrings with the total
    mers = []
    for i in counts:
        mers.append(str(i))
    y = len(mers) 
        
    return k,y,x


# In[4]:


# fucntion that creates a dataframe populated with each kmer's respective observed and possible total
def dataframe_kmers(string, k):
    # creating the empty dataframe
    df = pd.DataFrame(columns=["K", "Observed Kmers", "Possible Kmers"])
    # populating the dataframe
    for i in range(1, k+1):
        to_add = raw_kmers(string, i)
        df.loc[i] = to_add
    
    df = df.set_index('K')
    
    return df

    


# In[5]:


# fucntion to calculate linguistic complexity 
def lin_complex(string, k):
    df = dataframe_kmers(string, k)
    lin_comp = (df["Observed Kmers"].sum())/(df['Possible Kmers'].sum())
    lin_comp = round(lin_comp, 3)
    return lin_comp


# In[6]:


# fucntion that creates a dataframe populated with each kmer's 
# respective observed and possible total as well as ligustic complexity
def full_kmers(string, k):
    # creating the empty dataframe
    df = pd.DataFrame(columns=["K", "Observed Kmers", "Possible Kmers"])
    df1 = pd.DataFrame(columns=['Linguistic Complexity'])                           
    # populating the dataframe
    for i in range(1, k+1):
        to_add = raw_kmers('ATTTGGATT', i)
        lc = lin_complex(string, i)
        df.loc[i] = to_add
        df1.loc[i] = lc
        
    df2 = pd.concat([df,df1], axis=1)
    df2 = df2.set_index('K')
    return df2


# In[7]:


def main (string, k):
    x = number_kmers(string,k) # tests the number_kmers fucntion
    y = full_kmers(string, k)
    # tests the raw_kmers, dataframe_kmers, lin_complex, and full_kmers since they build on top of each other
    return x,y


# In[8]:


main('ATTTGGATT', 9)

