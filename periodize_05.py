
def main():
    frm=int(input("Enter FRM: "))
    workouts = [Light(frm=frm), Medium(frm=frm), Heavy(frm=frm), Light(frm=frm)]
    for workout in workouts:
        workout.periodize()

        
class Workout:
    def __init__(self, frm: int=0):
        self.frm=frm
        
    def periodize(self):
        raise NotImplementedError()
        
class Light(Workout):
    
    def periodize(self):
        print({'Set1':[int(self.frm*0.85*0.6), 12],  'Set2':[self.frm*0.85*0.80,  12],  'Set3':[self.frm*0.85, 8]})
        
class Medium(Workout):
    
    def periodize(self):
        print({'Set1':[self.frm*0.93*0.55,  9],  'Set2':[self.frm*0.93*0.70,  9], 'Set3':[self.frm*0.93*0.85,  9],
        'Set4':[self.frm*0.93,  6]})
        
class Heavy(Workout):
    
    def periodize(self):
        print({'Set2':[self.frm*0.5, 6], 'Set2':[self.frm*0.6,  6],  'Set3':[self.frm*0.7,  6],  'Set4':[self.frm*0.8,  6],
        'Set5':[self.frm*0.9,  6],  'Set6':[self.frm,  4]})
        
        
