from typing import List
from util import read_input


class Solver:
    def __init__(self, raw_data: List[str]):
        self.left = []
        self.right = []
        for line in raw_data:
            ids = line.split()
            self.left.append(int(ids[0]))
            self.right.append(int(ids[1]))
        self.left.sort()
        self.right.sort()

    def get_total_distance(self) -> int:
        distance = 0
        for i in range(0, len(self.left)):
            distance += abs(self.left[i] - self.right[i])

        return distance
    
    def get_similar_distance(self) -> int:
        similarity = 0
        right_counts = {}
        for id in self.right:
            if id in right_counts:
                right_counts[id] = right_counts[id] + 1
            else:
                right_counts[id] = 1
        
        for id in self.left:
            if id in right_counts:
                similarity += id * right_counts[id]

        return similarity


if __name__ == "__main__":
    sample_data = [
        "3   4",
        "4   3",
        "2   5",
        "1   3",
        "3   9",
        "3   3"
    ]
    solver = Solver(sample_data)
    print(solver.get_total_distance())

    solver = Solver(read_input("inputs/day1_historian_hysteria_input.txt"))
    print(solver.get_total_distance())

    solver = Solver(sample_data)
    print(solver.get_similar_distance())

    solver = Solver(read_input("inputs/day1_historian_hysteria_input.txt"))
    print(solver.get_similar_distance())
