from users import User

class VotingSystem:
    parties = {"TVK": 0, "BJP": 0, "DMK": 0}
    @classmethod
    def vote(cls, user, choice):
        if user.has_voted:
            return False, "You have already voted."
        if choice in cls.parties:
            cls.parties[choice] += 1
            user.has_voted = True
            return True, "Vote cast successfully."
        else:
            return False, "Invalid party choice."
    @classmethod
    def get_results(cls):
        return cls.parties
