LEVELS=['Easy','Medium','Hard']
class AdaptiveEngine:
    def __init__(self,mode='rule'): self.mode=mode
    def decide_next(self,level,recent):
        if not recent: return level,'no_data'
        acc=sum(a['correct'] for a in recent[-3:])/len(recent[-3:])
        avg=sum(a['response_time'] for a in recent[-3:])/len(recent[-3:])
        idx=LEVELS.index(level)
        if acc>=0.8 and avg<10: idx=min(2,idx+1);return LEVELS[idx],'up'
        if acc<=0.5 or avg>15: idx=max(0,idx-1);return LEVELS[idx],'down'
        return level,'stay'
