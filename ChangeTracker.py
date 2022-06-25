from ObjectTracker import track
import json

class mydict(dict):
    count=0
    instance_tracker=[]
    instances={}
    
    
    def SaveChanges(self):
        if self.append(self.instance_tracker)!=dict(self):
            track.TrackChanges(self)
            track.label_instance(self)
      
    
    def append(self,appending_list:list):
        
        try:
            return appending_list[-1]
        except:
            pass
    
    def __call__(self,track=True):

        if track==True:
            self.SaveChanges()
        with open('changes.json','w') as file:   
            json.dump(self.instances,file)
         
    


