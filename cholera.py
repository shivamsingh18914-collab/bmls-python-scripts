# Cholera  transmission  dynamics & clinical risk analysis . Target  Pathogen :Vibrio cholerae
#Framework : WHO guidelines for diagnosis , treatment, prevention and control
#Author : BMLS/ Computational biophysics portfolio

#parameters and intial state
# intial daily baseline of reported laboratory confirmed cases (a_1)

intial_cases = 350.0

# Transmission Parameters (R_0) if it is < 1 , it shows effective control of vector

effective_r0 = 0.75

#days to target

simulation_time = 25

#WHO CLINICAL TRIAGE THRESHOLD  allocation for triage capacity

WHO_TRIAGE_THRESHOLD = 25.0

case_sequences = []

#sequence generation (a_n calculation)

print("------------")

print("--CHOLERA OUTBREAK --")

print("-------------")

current_term = intial_cases

for day in range(1,simulation_time +1):

    #store term a_n in tracking array

    case_sequences.append (current_term)

    if current_term >= WHO_TRIAGE_THRESHOLD:

        status =" CRITICAL:open cholera treatment center"

    else:

        status = " STABLE : local health  center capacity "

    print(f" Day {day :02d} (a_{day : 02d}): {current_term : 6.2f} cases| [{status}]")

#recurrence relation:a_(n+1) = a_n *r0

    current_term = current_term * effective_r0

#limit evaluation (n -> infinite )

    limit_term = case_sequences[0]

    for step in range(150):


       limit_term = limit_term * effective_r0

    print(f" mathematical limit (lim ->inf a_n) = {limit_term :.6f}")

#WHO policy intervation and evaluation

if abs(limit_term) < 0.01:


       print("\n [conclusion] : converge to 0")

       print("[WHO DIRECTIVE]: waterborne disease controlled, shift to routine monitor")
else:

    print("\n [conclusion] : diverge")

    print("[WHODIRECTIVE] : waterborne disease control failed,Escalated Emergency