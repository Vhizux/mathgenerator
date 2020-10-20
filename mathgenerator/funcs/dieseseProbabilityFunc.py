from .__init__ import *
import sympy


def dieseseProbabilityFunc():

    P_diesese= 2*random.random()
    true_positive= random.random()+90
    true_negative= random.random()+95

    def BayesFormula(P_diesese, true_positive, true_negative):
        P_notDiesese= 100-P_diesese
        false_positive= 100-true_negative
        false_negative= 100-false_positive
        P_plus= (P_diesese/100.)*(true_positive/100.)+(P_notDiesese/100.)*(false_positive/100.)
        P_diesese_plus=((true_positive/100.)*(P_diesese/100.))/P_plus

        return P_diesese_plus

    problem= "Someone tested positive for a nasty diesese which only {0:.2f}% of population have. Test sensitivity(true positive) is equal to SN= {1:.2f}% whereas test specificity(true negative) SP= {2:.2f}%. What is the probability that this guy really have that diesese?".format(P_diesese, true_positive, true_negative )
    
    # answer= P_diesese_plus= probability of having diesese given positive test result
    answer= format(100*BayesFormula(P_diesese, true_positive, true_negative), '.2f')
    answer= str(answer)+"%"

    return problem, answer