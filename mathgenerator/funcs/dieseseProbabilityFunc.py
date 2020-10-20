from .__init__ import *
import sympy


def diseaseProbabilityFunc():

    P_disease= 2*random.random()
    true_positive= random.random()+90
    true_negative= random.random()+95

    def BayesFormula(P_disease, true_positive, true_negative):
        P_notDisease= 100-P_disease
        false_positive= 100-true_negative
        false_negative= 100-false_positive
        P_plus= (P_disease/100.)*(true_positive/100.)+(P_notDisease/100.)*(false_positive/100.)
        P_disease_plus=((true_positive/100.)*(P_disease/100.))/P_plus

        return P_disease_plus

    problem= "Someone tested positive for a nasty disease which only {0:.2f}% of population have. " \
    "Test sensitivity(true positive) is equal to SN= {1:.2f}% whereas test specificity(true negative) SP= {2:.2f}%." \
    "What is the probability that this guy really have that diesese?".format(P_disease, true_positive, true_negative )
    
    # answer= P_disease_plus= probability of having diesese given positive test result
    answer= format(100*BayesFormula(P_disease, true_positive, true_negative), '.2f')
    answer= str(answer)+"%"

    return problem, answer