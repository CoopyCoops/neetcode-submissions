class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = []
        cars = sorted(list(zip(position, speed)), reverse=True)
        for i in range(len(cars)):
            time = (target - cars[i][0])/cars[i][1]
            if len(times) == 0 or time > times[-1]:
                times.append(time)
        return len(times)

        