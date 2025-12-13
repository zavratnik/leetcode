from typing import Dict


class Problem299:
    def getHint(self, secret: str, guess: str) -> str:
        mapa = {}

        for s in secret:
            mapa[s] = mapa.get(s, 0) + 1

        bulls = 0
        temp = ""

        for i in range(len(guess)):
            if secret[i] == guess[i]:
                bulls += 1
                mapa[secret[i]] -= 1
            else:
                temp += guess[i]

        cows = 0

        for t in temp:
            if t in mapa and mapa[t] > 0:
                mapa[t] -= 1
                cows += 1

        ans = str(bulls) + "A" + str(cows) + "B"
        return ans
    

if __name__ == "__main__":
    solution = Problem299()

    print(solution.getHint("1807", "7810"))  # 1A3B
    print(solution.getHint("1123", "0111"))  # 1A1B
