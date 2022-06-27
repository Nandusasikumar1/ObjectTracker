# _**Python dictionary that can track changes**_


```


Using TrackerDict dictionary, which inherits from original python dictionary 
we can track the changes in any TrackerDict Object.
```
example

```
from ObjectTracker.ChangeTracker import TrackerDict
 #Import TrackerDict like this if you include the cloned repository in your project 

c=TrackerDict({1:5})
c('one') #Call the  instance with a name since this is the first instance I named it "one".You can name it whatever you want.This is for tracking the changes in the instance.

#Now we make a change 

c[1]=2
c('one') # Use the same name when you call the instance since we are making changes to the same instance.If you create another instance, use a different name.

d=TrackerDict({4:5,6:7})
d('two')
d[77]=3
d('two')
del d[4]
d('two') # Since we created another instance it's name must be differrent from other instances


  """ Use the class method label_instance to return all the changes during the current execution of the program.
 It must be called in order to create 'changes.json' file .Changes in previous executions will be stored in 'changes.json' file"""
 
 print(TrackerDict.label_instance())

 output : {'one': [{1: 5}, {1: 2}], 'two': [{4: 5, 6: 7}, {4: 5, 6: 7, 77: 3}, {6: 7, 77: 3}], 'created_at': '2022-06-27 20:33:43.180260'}

```






