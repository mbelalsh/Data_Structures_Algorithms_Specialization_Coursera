# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    lis_tup = []
    for i in range(len(weights)):
        data = (weights[i], float(values[i] / weights[i]))
        lis_tup.append(data)
    # print(lis_tup)
    lis_tups = [(k, v) for k, v in sorted(lis_tup, key=lambda x: x[1], reverse=True)]
    # print(lis_tups)
    weight = 0
    value = 0
    # bol = True
    for w1, ratio in lis_tups:
        cap = float(capacity - weight)
        if w1 < cap:
            value += float(ratio) * w1
            weight += w1
            # print(weight)
        else:
            value += (cap / w1) * float(ratio) * w1
            weight += cap
            # print(weight)
        if weight == capacity:
            # bol = False
            return value
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
