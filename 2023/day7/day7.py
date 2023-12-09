from collections import Counter


class Hand:

    def __init__(self, value, bid):
        c = Counter(value)
        self.value = value
        self.nb_pairs = len([e for e in list(c.values()) if e >= 2]) # No of hand having min 2 same cards
        self.type = max(c.values()) # Length of the longest jand of same card
        self.bid = int(bid)

    def __gt__(self, other):
        if self.type == other.type:
            if self.nb_pairs != other.nb_pairs:
                return self.nb_pairs > other.nb_pairs
            for s, o in zip(self.value, other.value):
                if val_card.index(s) != val_card.index(o):
                    return val_card.index(s) > val_card.index(o)
        return self.type > other.type

    def __str__(self):
        return f"{self.value}  : nb pairs={self.nb_pairs} bid={self.bid}"


class HandJoker:

    def __init__(self, value, bid):
        c = Counter(value)
        self.value = value
        self.nb_pairs = len([e for e in list(c.values()) if e >= 2])
        self.type = max(c.values())
        self.bid = int(bid)
        # default for j
        self.value_j = value
        self.type_j = max(c.values())
        self.nb_pairs_j = len([e for e in list(c.values()) if e >= 2])

        letters_wo_j = [l for l in list(value) if l != 'J']
        if len(letters_wo_j) > 0 and 'J' in self.value:
            letters_wo_j = sorted(letters_wo_j, key=lambda x: val_card_p2.index(x)) # sort by cards
            letters_wo_j = sorted(letters_wo_j, key=lambda x: self.value.count(x)) # sort by no in hand
            best_value_letter = letters_wo_j[-1]
            self.value_j = self.value.replace("J", best_value_letter)
            c = Counter(self.value_j)
            self.type_j = max(c.values())
            self.nb_pairs_j = len([e for e in list(c.values()) if e >= 2])

    def __str__(self):
        return f"{self.value}|{self.value_j} : nb pairs={self.nb_pairs_j}  max_pair={self.type_j}"

    def __gt__(self, other):
        if self.type_j != other.type_j:
            return self.type_j > other.type_j

        if self.nb_pairs_j != other.nb_pairs_j:
            return self.nb_pairs_j > other.nb_pairs_j

        for s, o in zip(self.value, other.value):
            if val_card_p2.index(s) != val_card_p2.index(o):
                return val_card_p2.index(s) > val_card_p2.index(o)

if __name__ == "__main__":
    liste_input = [e.replace('\n', '').split(' ') for e in open("input.txt", "r").readlines()]
    val_card = 'AKQJT98765432'[::-1]
    val_card_p2 = 'AKQT98765432J'[::-1]
    liste_hands1 = [Hand(l[0], l[1]) for l in liste_input]
    liste_hands2 = [HandJoker(l[0], l[1]) for l in liste_input]

    sorted_l1 = sorted(liste_hands1)
    sorted_l2 = sorted(liste_hands2)

    print("star 1 : ", sum((i + 1) * hand.bid for i, hand in enumerate(sorted_l1)))
    print("star 2 : ", sum((i + 1) * hand.bid for i, hand in enumerate(sorted_l2)))

