class Analyzer():
    
    def __init__(self, Systolic_BP, Diastolic_BP, Heart_Rate, Heart_O2_Level, Body_temp):
        self.Systolic_BP = Systolic_BP
        self.Diastolic_BP = Diastolic_BP
        self.Heart_Rate = Heart_Rate
        self.Heart_O2_Level = Heart_O2_Level
        self.Body_temp = Body_temp

    def Signal_Loss(self, Heart_Rate, Body_temp):
        # Signal loss judgement
        if (Heart_Rate < 60 and Body_temp < 36):
            return True
        return False

    def Shock_Alert(self, Heart_Rate, Body_temp):
        # Shock emergency judgement
        if (Heart_Rate < 60 and Body_temp >= 36):
            return True
        return False
    
    def Oxygen_Supply(self, Heart_O2_Level):
        # Oxygen supply judgement
        if (Heart_O2_Level < 70):
            return True
        return False
    
    def Fever(self, Body_temp):
        # Fever judgement
        if (Body_temp > 37.5):
            return True
        return False
    
    def Hypotension(self, Systolic_BP, Diastolic_BP):
        # Hypotension judgement
        if (Systolic_BP < 90 and Diastolic_BP < 60):
            return True
        return False
    
    def Hypertension(self, Systolic_BP, Diastolic_BP):
        # Hypertension judgement
        if (Systolic_BP > 140 or Diastolic_BP > 90):
            return True
        return False
