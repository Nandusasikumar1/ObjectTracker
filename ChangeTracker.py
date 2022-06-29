import json
from datetime import datetime
import os

class TrackerDict(dict):
    count=0
    instance_tracker=[]
    instances={}
    name=None

    def SaveChanges(self,name:str):

        if self.append(self.instance_tracker)!=dict(self):
            self.TrackChanges(name)
          
    def append(self,appending_list:list):
        
        try:
            return appending_list[-1]
        except:
            pass

    def TrackChanges(self,name):

        instance_track={}
        instance_track[name]=dict(self)
        self.instance_tracker.append(instance_track )

    @classmethod
    def label_instance(cls,overwrite=False):
        
        for i in cls.instance_tracker:
            for change_index, change in (i.items()):
                if change_index not in cls.instances:
                    cls.instances[change_index]=[]
                cls.instances[change_index].append(change)
        
        if overwrite==True:

            with open('changes.json','w') as file:
                cls.instances.update({'created_at':str(datetime.now())}) 
                json.dump([cls.instances],file,ensure_ascii=False,indent=2)
        
        elif overwrite==False:

            try:
                with  open('changes.json','r') as file:
                    cls.instances.update({'created_at':str(datetime.now())})  
                    json_list=json.load(file)
                    json_list.append(cls.instances)
                    with open('changes.json','w')as file1:
                        json.dump(json_list,file1,ensure_ascii=False,indent=2)

            except:
                with open('changes.json','w') as file:
                    cls.instances.update({'created_at':str(datetime.now())}) 
                    json.dump([cls.instances],file,ensure_ascii=False,indent=2)
        else:

            raise Exception('Only Boolean values are acceptable')
        
        return cls.instances
    
    @classmethod
    def remove_json(cls):
        os.remove('changes.json')
    
    def set_name(self,name):
        self.name=name
        return name

    def __call__(self,track=True):
        if track==True:
            self.SaveChanges(self.name)
           
           
        