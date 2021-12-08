def get_signals(filename):
    signal_patterns = []
    with open(filename, 'r') as file:
        for line in file:
            signals = []
            a, b = line.strip().split('|')
            signals.append(a.split())
            signals.append(b.split())
            signal_patterns.append(signals)
    return signal_patterns

def parte1(signal_patterns):
    conta = 0
    for signal in signal_patterns:
        for s in signal[1]:
            if len(s) <= 4 or len(s) == 7:
                conta += 1
    print(conta)


def parte2(signal_patterns):
    print('TODO')


filename = 'input.txt'
signals = get_signals(filename)
parte1(signals)
