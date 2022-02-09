from socket import getprotobyname


class neuron():
    def __init__(self):
        self.lam = 0.01
        self.wi = [ 0.1, -0.5, 0.5 ]

        self.sample = [
                [1, 0, 0], 
                [1, 0, 1],
                [1, 1, 0],
                [1, 1, 1]
            ]

        self.results = [0, 0, 0, 1]

    def train(self, epoch):
        for j in range(epoch):
            for i in range(4):
                y = self.wi[0] * self.sample[i][0] + self.wi[1] * self.sample[i][1] + self.wi[2] * self.sample[i][2]
                e = self.results[i] - y
                for k in range(3):
                    self.wi[k] += self.lam * e * self.sample[i][k]

            if j // 100 == 0:
                print(self.control())

    def control(self):
        sumE = 0
        for i in range(4):
            y = self.wi[0] * self.sample[i][0] + self.wi[1] * self.sample[i][1] + self.wi[2] * self.sample[i][2]
            e = self.results[i] - y
            sumE += e*e/2

        return sumE/4

    def getProbabilities(self, x1 = None, x2 = None):
        if x1 is not None and x2 is not None:
            return x1 * self.wi[1] + x2 * self.wi[2]

        y = []
        for i in range(4):
            y.append(self.sample[i][1] * self.wi[1] + self.sample[i][2] * self.wi[2])
        return y

    def checkResult(self, y):
        # y = self.getProbabilities()
        if isinstance(y, list):
            results = []
            for el in y:
                results.append(1 if el > 0.5 else 0)
            return results
        else:
            return 1 if y > 0.5 else 0


    # def drawGraph():



neu = neuron()
neu.train(500)
# E = neu.control()
# y = neu.check()
yb = neu.getProbabilities(1, 1)
y = neu.checkResult(yb)
print(y)