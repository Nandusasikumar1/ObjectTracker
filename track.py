def TrackChanges(self):

        self.count+=1
        instance_track={}
        instance_track[self.count]=dict(self)
        self.instance_tracker.append(instance_track )
      
def label_instance(self):

    count_instance=0

    for i in self. instance_tracker:
        for change_index, change in (i.items()):
            if change_index==1:
                count_instance+=1
                self.instances['instance-'+str(count_instance)]=[]
                self.instances['instance-'+str(count_instance)].append(change)
            else:
                self.instances['instance-'+str(count_instance)].append(change)

