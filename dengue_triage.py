#pathogen  Transmission dynamics & clinical risk analysis
#target pathogen  : Dengue Virus (DENV)
# Frameworks: WHO guidelines for diagnosis, treatment,  prevention, control
# Author : BMLS/Computational Biophysics  and Portfolio


#parameters  and intial state , intial daily baseline of reported laboratory  confirmed cases(a_1)

intial_cases = 450.0

#transmission factor (R_0)if less than 1 indicates effective vector control measures local vector density

effective_r0 = 0.82

# target days

simulation_days = 30

#WHO Clinical threshold for triage  capacity allocation

WHO_TRIAGE_THRESHOLD = 50.0

case_sequences = []

print("-------------")

print("--DENGUE OUTBREAKS --")

print("--------------")

current_term = intial_cases

for days in range (1, simulation_days +1):

    #store term a_n in tracking array

     case_sequences.append(current_term)

     if current_term >= WHO_TRIAGE_THRESHOLD:


         status_flag =" ALERT : high triage burden "

         print(f" Days{days : 02d} (a_{days : 02d}) : {current_term : 6.2f}cases| [{status_flag}]")

#compute next term  using a_(n+1) = a_n *r0


         current_term = current_term * effective_r0


#Mathematics Limit &Long term analysis (n-> infinity)


print("\n --------")

print(" long term analysis ")

print("------------")

limit_term = case_sequences [0]

for step in range(150):

     limit_term = limit_term *effective_r0

print (f" mathematical limit (lim n-> infinite a_n)) = {limit_term : .6f}")

# WHO policy intenvation and evaluation

if abs (limit_term) < 0.001:

     print("\n [conclusion] : sequence converge to 0")

     print("[WHO directive]: vector controlled shift")

else:

     print("\n [conclusion] : sequence.diverges")

     print("[WHO DIRECTIVE]: Vector control failed . Escalate emergency intervention ")

print("------------")