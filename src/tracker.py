import time
class Tracker:
    def __init__(self): self.logs=[]
    def log(self,q,c,t,d): self.logs.append({'question':q,'correct':c,'response_time':t,'difficulty':d,'timestamp':time.time()})
    def summary(self):
        if not self.logs: return {}
        total=len(self.logs);correct=sum(l['correct'] for l in self.logs)
        avg=sum(l['response_time'] for l in self.logs)/total
        by={}
        for l in self.logs:
            by.setdefault(l['difficulty'],{'count':0,'correct':0})
            by[l['difficulty']]['count']+=1; by[l['difficulty']]['correct']+=int(l['correct'])
        for k,v in by.items(): v['accuracy']=v['correct']/v['count']
        return {'total':total,'correct':correct,'accuracy':correct/total,'avg_time':avg,'by_level':by}
