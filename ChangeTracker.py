from ObjectTracker import track
import json
from datetime import datetime


class TrackerDict(dict):
    count=0
    instance_tracker=[]
    instances={}
    
    
    def SaveChanges(self,name:str):
        if self.append(self.instance_tracker)!=dict(self):
            track.TrackChanges(self,name)
            # track.label_instance(self)
      
    
    def append(self,appending_list:list):
        
        try:
            return appending_list[-1]
        except:
            pass
    
    @classmethod
    def label_instance(cls):

        for i in cls.instance_tracker:
            for change_index, change in (i.items()):
                if change_index not in cls.instances:
                    cls.instances[change_index]=[]
                cls.instances[change_index].append(change)

        try:
            
            with  open('changes.json','r') as file:
                cls.instances=cls.instances|{'created_at':str(datetime.now())} 
                json_list=json.load(file)
                json_list.append(cls.instances)
                with open('changes.json','w')as file1:
                    json.dump(json_list,file1,ensure_ascii=False,indent=2)

        except:
            with open('changes.json','w') as file:
            # json.dump({'created_at':str(datetime.now())},file)  
                cls.instances=cls.instances|{'created_at':str(datetime.now())} 
                json.dump([cls.instances],file,ensure_ascii=False,indent=2)
        
        return cls.instances

    def __call__(self,name,track=True):

        if track==True:
            self.SaveChanges(name)
           
         
    


