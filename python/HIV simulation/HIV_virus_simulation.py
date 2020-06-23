# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics 

import random
import pylab
random.seed(0)

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 1
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """

        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """
        probablity = random.random()
        if probablity <= self.getClearProb():
            return True
        else:
            return False

    
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        
        reproduce_var = self.getMaxBirthProb()*(1-popDensity)
        if random.random() <= reproduce_var:
            return SimpleVirus(self.maxBirthProb,self.clearProb)
        else:  
            raise NoChildException


# v1 = SimpleVirus(0.95,0.27)
# print(v1.reproduce(0.02))

        



class Patient(object):
    
    
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """

        self.viruses = viruses
        self.maxPop = maxPop
        self.totalVirPop = len(viruses)


    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses


    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxPop


    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        """

        return len(self.viruses)       


    # def update(self):
    #     """
    #     Update the state of the virus population in this patient for a single
    #     time step. update() should execute the following steps in this order:

    #     - Determine whether each virus particle survives and updates the list
    #     of virus particles accordingly.   
        
    #     - The current population density is calculated. This population density
    #     value is used until the next call to update() 
        
    #     - Based on this value of population density, determine whether each 
    #     virus particle should reproduce and add offspring virus particles to 
    #     the list of viruses in this patient.                    

    #     returns: The total virus population at the end of the update (an
    #     integer)
    #     """
    #     popDensity = self.getTotalPop()/self.getMaxPop()
        
    #     copy_list_viruses = self.getViruses()[:]
    #     # print(copy_list_viruses)
    #     for i in range(len(self.getViruses())):
    #         # print('i =',i)
            
    #         virus = self.getViruses()[i]
    #         if SimpleVirus.doesClear(virus):
    #             copy_list_viruses.pop(copy_list_viruses.index(virus))

    #         else:
    #             if popDensity< 1:
    #                 try:
    #                     v = SimpleVirus.reproduce(virus,popDensity)
                        
                        
    #                 except NoChildException:
    #                     continue
    #                 copy_list_viruses.append(v)
    #             else:
    #                 break    
    #         # popDensity = len(copy_list_viruses)/self.getMaxPop()
    #         # print(copy_list_viruses)
    #     self.viruses = copy_list_viruses
    #     return len(self.viruses)





    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        
        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    
        returns: The total virus population at the end of the update (an
        integer)
        """

        # TODO
        viruses_copy = self.viruses[:]
        for i in viruses_copy:
            if i.doesClear() == True:
                self.viruses.remove(i)
                
        popDensity = len(self.viruses)/self.maxPop
        
        viruses_copy_2 = self.viruses[:]
        for j in viruses_copy_2:
            try:
                j.reproduce(popDensity)
                self.viruses.append(j)
            except NoChildException:
                continue
        return len(self.viruses)




# viruses = [
# SimpleVirus(0.6, 0.01),
# SimpleVirus(0.05, 0.01),
# SimpleVirus(0.12, 0.01),
# SimpleVirus(0.17, 0.84)
# ]
# P1 = Patient(viruses, 8)
# for j in range(10):
    
#     print(P1.update())

                



        



#
# PROBLEM 2
#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb, numTrials):
    import numpy as np
    
    data = np.zeros(300)
    # print(data)
    for i in range(numTrials):
        virus = SimpleVirus(maxBirthProb, clearProb)
        viruses = [virus] * numViruses
        patient = Patient(viruses, maxPop)
        virus_count = []
        for j in range(300):
            patient.update()
            virus_count.append(patient.getTotalPop()) 
            # print('virus_count',virus_count)         
        data = data + virus_count
        # print('data',data)
    data_avg = data/numTrials
    # print('data_avg',data_avg)
    
    pylab.plot(list(data_avg), label=r'Average SimpleVirus Population')
    pylab.xlabel(r'Number of steps')
    pylab.ylabel(r'Virus Population')
    pylab.title(r'Simple Virus Simulation in Patient')
    pylab.legend()
    pylab.show()
    
    




# simulationWithoutDrug(10, 80, 0.1, 0.05,
                        #   1000)


#
# PROBLEM 3
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """   

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)       

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """
        # self.maxBirthProb = maxBirthProb
        # self.clearProb = clearProb
        SimpleVirus.__init__(self,maxBirthProb,clearProb)
        self.resistances = resistances
        self.mutProb = mutProb


        


    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        try:
            return self.resistances[drug]
        except KeyError:
            return False
        


    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.maxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.       

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population       

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """
        def res_update(resistance,mult_prob):
            resistance_copy = resistance.copy()
            
            probab = mult_prob
            for vir in resistance_copy.keys():
                prob = random.random()
                if prob <= probab:
                    if resistance_copy[vir] == True:
                        resistance_copy[vir] = False
                    else:
                        resistance_copy[vir] = True
            return resistance_copy
                    

            

        reproduction_check = []
        for drug in activeDrugs:
            try:
                if self.resistances[drug] == True:
                    reproduction_check.append(1)
            except KeyError:
                break
            # print(drug,reproduction_check)
        reproduce_var = self.getMaxBirthProb()*(1-popDensity)
        # print(reproduce_var,len(activeDrugs)== len(reproduction_check),random.random()<=reproduce_var)
        if len(reproduction_check)== len(activeDrugs) and random.random() <= reproduce_var:
            return ResistantVirus(self.maxBirthProb,self.clearProb,res_update(self.getResistances(),self.mutProb),self.mutProb)
        else:  
            raise NoChildException
# checker code don't disturb 
# print('---------------------------------------------------------------------------------------------------') 
# print('---------------------------------------------------------------------------------------------------')          
# for num in range(10):
#     virus = ResistantVirus(1.0, 0.0, {'drug1':True, 'drug2': True, 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}, 0.9)
#     true = 0
#     false = 0
#     pp = virus.reproduce(0, [])
#     resist = pp.getResistances()
#     for vi in resist.keys():
#         if resist[vi] == True:
#             true += 1
#         else:
#             false +=1
#     print(num,resist,true,false)
#     print('+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+')
# print('-----------------------------------------------------------------------------------------------------')



            

class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """
        Patient.__init__(self,viruses,maxPop)

        self.drug = []


    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """

        if newDrug not in self.drug:
            self.drug.append(newDrug)
        return self.drug


    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """

        return self.drug


    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        
        resist_pop = 0
        for virus in self.viruses:
            drug_check = 0
            # print("--------------------------")
            for drug in drugResist:
                # print(virus,drug,ResistantVirus.isResistantTo(virus,drug))
                if ResistantVirus.isResistantTo(virus,drug):
                    drug_check += 1
                    # print(drug_check)
            if drug_check == len(drugResist):
                # print('i am inside')
                resist_pop += 1
        return resist_pop
                



    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """
        virus_offsprings = []
        virus_copy = self.viruses
        for virus in virus_copy:
            if SimpleVirus.doesClear(virus) == True:
                self.viruses.remove(virus)
        population_density = len(self.viruses)/self.maxPop
        for virus in self.viruses:
            try:
                virus_offsprings.append(ResistantVirus.reproduce(virus,population_density,self.drug))
            except NoChildException:
                continue
        self.viruses = self.viruses+virus_offsprings
        return len(self.viruses)



# virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
# virus2 = ResistantVirus(1.0, 0.0, {"drug1": False, "drug2": True}, 0.0)
# virus3 = ResistantVirus(1.0, 0.0, {"drug1": True, "drug2": True}, 0.0)
# patient = TreatedPatient([virus1, virus2, virus3], 100)
# print(patient.getResistPop(['drug1']),2)    #2
# print(patient.getResistPop(['drug2']),2)    #1
# print(patient.getResistPop(['drug1','drug2']),1)   #1
# print(patient.getResistPop(['drug3']),0)           #0
# print(patient.getResistPop(['drug1', 'drug3']),0)  #1
# print(patient.getResistPop(['drug1','drug2', 'drug3']),0) #0


            







# PROBLEM 4
#
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """

    big_list_v1 = []
    big_list_v2 = []
    

    for id1 in range(numTrials):
        viruses = []
        for id2 in range(numViruses): 
            viruses.append(ResistantVirus(maxBirthProb,clearProb,resistances,mutProb))
        small_list_v1 = []
        time_step_average_for_resist_pop = []
        Patient1 = TreatedPatient(viruses,maxPop)
        for id3 in range(150):
            Patient1.update()
            small_list_v1.append(Patient1.getTotalPop())
            time_step_average_for_resist_pop.append(Patient1.getResistPop(['guttagonol']))
        Patient1.addPrescription('guttagonol')
        for id4 in range(150):
            Patient1.update()
            small_list_v1.append(Patient1.getTotalPop())
            time_step_average_for_resist_pop.append(Patient1.getResistPop(['guttagonol']))
            
            
            
        big_list_v1.append(small_list_v1)
        big_list_v2.append(time_step_average_for_resist_pop)
        #print(id1,big_list_v1,big_list_v2)
        

    data_avg2 = []
    data_avg3 = []
    length = len(big_list_v1[-1])
    for i in range(length):
        data1 = 0
        data2 = 0
        for smalllist in big_list_v1:
            intdex = big_list_v1.index(smalllist)
            data1 += smalllist[i]
            data2 += big_list_v2[intdex][i]
        data_avg2.append(data1/numTrials)
        data_avg3.append(data2/numTrials)
    # print('________',data_avg2)
    # print('+++++++',data_avg3)




    
    
    
    pylab.plot(data_avg2, label=r'Total Virus')
    pylab.plot(data_avg3, label=r'Resistant Virus')
    pylab.xlabel(r'Number of steps')
    pylab.ylabel(r'Virus Population')
    pylab.title(r'Resistant Virus Simulation in Patient')
    pylab.legend()
    pylab.show()

    



simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, 100)
# simulationWithDrug(1, 20, 1.0, 0.0, {"guttagonol": True}, 1.0, 5)
# simulationWithDrug(1, 10, 1.0, 0.0, {}, 1.0, 5) # not working
# simulationWithDrug(75, 100, .8, 0.1, {"guttagonol": True}, 0.8, 1)