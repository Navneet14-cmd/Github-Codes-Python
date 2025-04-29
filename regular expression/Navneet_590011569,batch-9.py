# Develop a secure and user-friendly voting system that allows eligible voters to cast their votes digitally while ensuring the following requirements:- 
# Voter validation: Verify if the voter is registered using their voter ID.
# Age restriction: Ensure that only individuals aged 18 or above are eligible to vote.- Vote timing: Restrict voting to the designated date.
# Unique votes: Prevent voters from casting multiple votes.
# Party selection: Allow voting only for valid, predefined political parties.
# Feedback on invalid attempts: Handle errors gracefully, such as invalid IDs, incorrect voting dates, or unauthorized multiple voting attempts.
# Display results: Summarize and present the voting results to show the total votes for each party.
# Enhanced security: Implement a lockout mechanism after a certain number of invalid attempts."

import time
current=time.strftime("%Y-%m-%d")
voterID=[1423, 1555, 1232, 5532, 9012]
voting=[]
parties=["XYZ", "ABC", "FGH"]

class InvalidVoter(Exception):
    pass
class InvalidDate(Exception):
    pass
class MultipleVoteError(Exception):
    pass
class InvalidPartyInput(Exception):
    pass
class AgeRestrictionError(Exception):
    pass

class Voter:
    def __init__(self, name, id, age):
        self.name=name
        self.id=id
        self.age=age

    def check(self):
        if self.id in voterID:
            pass
        else:
            raise InvalidVoter("The voter is not registered.")
    
    def check_age(self):
        if (self.age >= 18):
            pass
        else:
            raise AgeRestrictionError("You must be 18 or older to vote.")
    
    def checktime(self,time):
        if current==time:
            pass
        else:
            raise InvalidDate("Your voting day is not today.\n")
        
    def party(self,party):
        if party in parties:
            self.party=party
        else:
            raise InvalidPartyInput("Such Party Does Not Exist.\n")
    
    def vote(self):
        for voter in voting:
            if (voter.id==self.id and voter.name==self.name):
                raise MultipleVoteError("You have already voted once.\n")
        voting.append(self)
        print(f"{self.name} has successfully voted for {self.party}.\n")

def display_results():
    party_votes={party:0 for party in parties}
    for voter in voting:
        party_votes[voter.party] += 1
    print("Voting Results:")
    for party, votes in party_votes.items():
        print(f"{party}: {votes} votes")
    
try:
    invalid_attempts = 0
    while True:
        voter_name=input("Kindly Enter Your Name: \n")
        voter_ID=int(input("Kindly Enter Your ID: \n"))
        voter_age=int(input("Kindly Enter Your Age: \n"))
        voter1=Voter(voter_name, voter_ID, voter_age)
        voter1.check()
        voter1.check_age()
        times=input("Kindly Enter Your Voting Date (Year-Month-Day format): \n")
        voter1.checktime(times)
        part=input("Which party do you want to vote for: \n")
        voter1.party(part)
        voter1.vote()
        cont=input("Do you want to continue voting? (yes/no): ").strip().lower()
        if (cont!='yes'):
            display_results()
            break
except (InvalidVoter, InvalidDate, MultipleVoteError, InvalidPartyInput, AgeRestrictionError) as e:
    print(e)
    invalid_attempts +=1
    if invalid_attempts >=3:
        print("Too many invalid attempts. Access locked.")
finally:
    print("Thanks for using the voting machine.")