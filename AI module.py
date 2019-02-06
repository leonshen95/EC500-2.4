
import numpy as np
import DataBaseModule
class AI_module(object):
    def __init__(self, dict):
        self._dict = dict

    def Query_Data_From_Database(self,ID,infoDB):
        ## connect database, query previous one day data from Database
        # Database = database_dict()
        Blood_oxygen=list()
        Blood_pressure = list()
        Pulses= list()
        DataBaseModule.search(ID)
        # Username = input("")
        #get dictionary from database
        for key in infoDB:
            if key== ID:
                pressure = dict.get('blood_pressure')
                oxygen = dict.get('blood_oxygen')
                Pulse = dict.get('blood_pulses')
                Blood_pressure.append(pressure)
                Blood_oxygen.append(Blood_oxygen)
                Pulses.append(Pulse)


        return Blood_oxygen, Blood_pressure, Pulses


    def AI_Module(self,Blood_oxygen, Blood_pressure, Pulses):

        ## AI module do the prediection, The AI module uses previous data
        oxygen=np.array(Blood_oxygen)
        pressure = np.array(Blood_pressure)
        Pulse = np.array(Pulses)
        pressure_predict_result = np.means(pressure)
        oxygen_predict_result=np.means(oxygen)
        Pulse_predict_result = np.means(Pulse)

        return pressure_predict_result, oxygen_predict_result, Pulse_predict_result


    def Feedback(self,Blood_pressure_predict_result, Blood_oxygen_predict_result, Pulse_predict_result):
        lower_BP= 80
        upper_BP= 120
        BP_Alert= 0
        lower_BO = 80
        upper_BO = 120
        BO_Alert = 0
        lower_Pulse = 80
        upper_Pulse = 120
        Pulse_Alert =0
        if(Blood_oxygen_predict_result<lower_BO or Blood_oxygen_predict_result>upper_BO):
            BO_Alert =1
        if(Blood_pressure_predict_result<lower_BP or Blood_pressure_predict_result>upper_BP):
            BP_Alert =1
        if(Pulse_predict_result< lower_Pulse or Pulse_predict_result >upper_Pulse):
            Pulse_Alert =1
        ## feedback the AI prediction restult to the interface
        ## It will turn on the Alert when the statues get worse.
        return BO_Alert,BP_Alert,Pulse_Alert


