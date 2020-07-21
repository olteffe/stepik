bio_a = int(input())
inf_b = int(input())
pieces_d = bio_a
while pieces_d % inf_b != 0:
    pieces_d += bio_a
print(pieces_d)
