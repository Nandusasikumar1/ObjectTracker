
def TrackChanges(self,name):
        instance_track={}
        instance_track[name]=dict(self)
        self.instance_tracker.append(instance_track )
      

