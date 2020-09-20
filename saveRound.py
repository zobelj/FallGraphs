import pandas as pd

def saveRound(data):
    df = pd.DataFrame(data).transpose()
    #with open("./data.csv", "a", newline='\n') as f:
    df.to_csv("./data.csv", mode="a", header=False, encoding="utf-8", index=False)

    return