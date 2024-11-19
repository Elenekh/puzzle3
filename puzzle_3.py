import random
#1
suits = ["H", "C", "D", "S"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

card_deck = []

#2
for suit in suits:
   for rank in ranks:
      card_deck.append(f"{rank} of {suit}")

random.shuffle(card_deck)

#3
magic_cards = []

for i in range(5):
   magic_cards.append(card_deck.pop())

#4
rank_suits_index = {}

for card in magic_cards:
   rank, suit  = card.split(" of ")
   rank_index = ranks.index(rank)
   if suit not in rank_suits_index:
      rank_suits_index[suit] = []
   rank_suits_index[suit].append((rank_index, card))

#5
best_pair = None
first_card = None
hidden_card = None
best_distance = None

#6
for suit, positions in rank_suits_index.items():
   if len(positions) > 1:
      for i in range(len(positions)):
        for j in range(i+1, len(positions)):
           
           #extracting cards position, and the card
           card_position_i, card_i = positions[i]
           card_position_j, card_j = positions[j]

           distance_1 = abs(card_position_i - card_position_j) % 13
           distance_2 = abs(card_position_j - card_position_i) % 13

           distance = min(distance_1, distance_2)

           if 1 <= distance <= 6:
              rank_i = card_i.split(" ")[0]
              rank_j = card_j.split(" ")[0]

              if ranks.index(rank_i) < ranks.index(rank_j):
                   first_card = card_i
                   hidden_card = card_j
              else:
                   first_card = card_j
                   hidden_card = card_i

        if best_distance is None or distance < best_distance:
           best_pair = (first_card, hidden_card)
           best_distance = distance 
           chosen_suit = suit

#7
magic_cards.remove(first_card)
magic_cards.remove(hidden_card)

# 8
remaining_cards = magic_cards
sorted_cards = sorted(remaining_cards)
S, M, L = sorted_cards

# 9
def encode_cards(S, M, L):
    if [S, M, L] == sorted([S, M, L]):
        encoded_value = 1
    elif [S, L, M] == sorted([S, L, M]):
        encoded_value = 2
    elif [M, S, L] == sorted([M, S, L]):
        encoded_value = 3
    elif [M, L, S] == sorted([M, L, S]):
        encoded_value = 4
    elif [L, S, M] == sorted([L, S, M]):
        encoded_value = 5
    else:
        encoded_value = 6

    return encoded_value, S, M, L

# 10
encoded_value, smallest, middle, largest = encode_cards(S, M, L)

# Assuming encoded_value will correspond to one of the predefined encoded orders
# Instead of storing the cards, store their indices
encoded_orders = {
    1: [0, 1, 2],  # Order [first, second, third] for sorted S, M, L
    2: [0, 2, 1],  # Order [first, third, second]
    3: [1, 0, 2],  # Order [second, first, third]
    4: [1, 2, 0],  # Order [second, third, first]
    5: [2, 0, 1],  # Order [third, first, second]
    6: [2, 1, 0],  # Order [third, second, first]
}

# Now, find the encoded order based on the encoded value
encoded_order = encoded_orders[encoded_value]
encoded_cards = [remaining_cards[i] for i in encoded_order]

#11
print(f"The first card is: {first_card}")
print(f"The encoded cards are: {encoded_cards}")
print(f"Encoded order value: {best_distance} ")

guess = input("What is the hidden card?: ")

if guess == hidden_card:
   print("Congratulations!!!")
else: 
   print(f"Sorry, the correct hidden card was: {hidden_card}")