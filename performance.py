
import time

class Performance:
    def __init__(self, saltik, ):
        self._saltik = saltik

    def accuracy(self, algo):
        correct_candidates = 0 # parameter for candidate accuracy
        best_candidates = 0 # parameter for best match accuracy 
        N = 0
        runtime = 0
        for word in self._saltik: 
            for typo in self._saltik[word]:
                typo = typo['typo']
                N=N+1
                start_time = time.time()
                candidates = algo.get_candidates(typo,2)
                end_time = time.time()
                if word == candidates[0]:
                    best_candidates=best_candidates+1
                if word in candidates:
                    correct_candidates=correct_candidates+1
                runtime = runtime + (end_time-start_time)
        best_acc = (best_candidates/N) * 100
        candidate_acc = (correct_candidates/N) * 100
        return {"best accuracy: ":best_acc,"candidate accuracy: ":candidate_acc,"total_time: ":runtime }