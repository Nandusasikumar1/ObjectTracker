# _**Python dictionary that can track changes**_


```


Using TrackerDict dictionary, which inherits from original python dictionary 
we can track the changes in any TrackerDict Object.
```
example

```
from ObjectTracker.ChangeTracker import TrackerDict
 #Import TrackerDict like this if you include the cloned repository in your project 

c=TrackerDict({1:3})
c.set_name(name='one') 
c()
#First ,set a name for the instance since this is the first instance,
 I named it "one".You can name it whatever you want.Then call the instance.
 This is for tracking the changes in the instance.

#Now we make a change 

c[66]=44
c()
c.update({4:5,6:8})
c()
for i in range(10,20):
    c[i]=i
    c()
# Whenever you make a change call the instance ( here it is c() ) after the change to track the change.

"""You can create any number of TrackerDict instances.But for each instance 
the name must be unique"""

TrackerDict.label_instance(overwrite=False)

"""Use the class method label_instance after making all the changes 
to save the changes as a json file(changes.json).It has an overwrite parameter 
which has a default value of False.If it is set to True ,only changes
 made in the current execution of the program will be saved and changes 
 during the previous executions saved in the changes.json file will be lost."""

output saved in the json file:

[
  {
    "one": [
      {
        "1": 3
      },
      {
        "1": 3,
        "66": 44
      },
      {
        "1": 3,
        "66": 44,
        "4": 5,
        "6": 8
      },
      {
        "1": 3,
        "66": 44,
        "4": 5,
        "6": 8,
        "10": 10
      },
      {
        "1": 3,
        "66": 44,
        "4": 5,
        "6": 8,
        "10": 10,
        "11": 11
      },
      {
        "1": 3,
        "66": 44,
        "4": 5,
        "6": 8,
        "10": 10,
        "11": 11,
        "12": 12
      },
      {
        "1": 3,
        "66": 44,
        "4": 5,
        "6": 8,
        "10": 10,
        "11": 11,
        "12": 12,
        "13": 13
      },
      {
        "1": 3,
        "66": 44,
        "4": 5,
        "6": 8,
        "10": 10,
        "11": 11,
        "12": 12,
        "13": 13,
        "14": 14
      },
      {
        "1": 3,
        "66": 44,
        "4": 5,
        "6": 8,
        "10": 10,
        "11": 11,
        "12": 12,
        "13": 13,
        "14": 14,
        "15": 15
      },
      {
        "1": 3,
        "66": 44,
        "4": 5,
        "6": 8,
        "10": 10,
        "11": 11,
        "12": 12,
        "13": 13,
        "14": 14,
        "15": 15,
        "16": 16
      },
      {
        "1": 3,
        "66": 44,
        "4": 5,
        "6": 8,
        "10": 10,
        "11": 11,
        "12": 12,
        "13": 13,
        "14": 14,
        "15": 15,
        "16": 16,
        "17": 17
      },
      {
        "1": 3,
        "66": 44,
        "4": 5,
        "6": 8,
        "10": 10,
        "11": 11,
        "12": 12,
        "13": 13,
        "14": 14,
        "15": 15,
        "16": 16,
        "17": 17,
        "18": 18
      },
      {
        "1": 3,
        "66": 44,
        "4": 5,
        "6": 8,
        "10": 10,
        "11": 11,
        "12": 12,
        "13": 13,
        "14": 14,
        "15": 15,
        "16": 16,
        "17": 17,
        "18": 18,
        "19": 19
      }
    ],
    "created_at": "2022-06-29 11:40:54.887133"
  }
]






