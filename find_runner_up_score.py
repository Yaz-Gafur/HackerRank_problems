def find_runner_up_score(scores):
    max_score = float('-inf')
    runner_up_score = float('-inf')

    for score in scores:
        if score > max_score:
            runner_up_score = max_score
            max_score = score 
        elif score > runner_up_score and score != runner_up_score:
            runner_up_score = score

        return runner_up_score


if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))
    
    runner_up = find_runner_up_score(scores)
    print(runner_up)
