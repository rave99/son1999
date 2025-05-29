import pickle
import os

filename = 'score.bin'
scores = []

if os.path.exists(filename):
    with open(filename, 'rb') as f:
        scores = pickle.load(f)
    print("[파일 읽기]")
    print("개인점수:", *scores)
    print("평균:", sum(scores) / len(scores) if scores else 0)
else:
    print("[점수 입력]")
    while True:
        score = int(input(f"#{len(scores)+1}? "))
        if score < 0:
            break
        scores.append(score)
    
    with open(filename, 'wb') as f:
        pickle.dump(scores, f)
    
    print("[점수 출력]")
    print("개인점수:", *scores)
    print("평균:", sum(scores) / len(scores) if scores else 0)
