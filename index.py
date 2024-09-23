import random


suits = ['CORAZÓN', 'TRÉBOL', 'DIAMANTE', 'ESPADA']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
value_map = {str(i): i for i in range(2, 11)}
value_map.update({'A': [1, 11], 'J': 10, 'Q': 10, 'K': 10})


def create_deck():
    return [(value, suit) for suit in suits for value in values]

def calculate_hand_value(hand):
    value = 0
    ace_count = 0
    
    for card in hand:
        if card[0] in value_map:
            if isinstance(value_map[card[0]], list):
                ace_count += 1
                value += value_map[card[0]][1]  
            else:
                value += value_map[card[0]]
    
    while value > 21 and ace_count:
        value -= 10  
        ace_count -= 1
    
    return value


def play_blackjack():
    print("¡Bienvenido al Blackjack!")
    player_name = input("Introduce tu nombre: ")
    player_chips = 100

    while player_chips > 0:
        print(f"\nTienes {player_chips} fichas.")
        bet = int(input(f"{player_name}, ¿cuántas fichas deseas apostar? "))

        if bet > player_chips:
            print("No tienes suficientes fichas.")
            continue

        deck = create_deck()
        random.shuffle(deck)

        
        player_hand = [deck.pop(), deck.pop()]
        house_hand = [deck.pop(), deck.pop()]

        print(f"\nMano de {player_name}: {player_hand} (valor: {calculate_hand_value(player_hand)})")
        print(f"Mano de la casa: [{house_hand[0]}, ?]")

        
        while True:
            if calculate_hand_value(player_hand) == 21:
                print("¡Tienes Blackjack! Ganaste.")
                player_chips += bet * 1.5  
                break

            action = input("¿Deseas pedir una carta (P) o plantarte (S)? ").strip().upper()
            if action == 'P':
                player_hand.append(deck.pop())
                print(f"\nMano de {player_name}: {player_hand} (valor: {calculate_hand_value(player_hand)})")
                if calculate_hand_value(player_hand) > 21:
                    print("Te has pasado de 21. ¡Perdiste!")
                    player_chips -= bet
                    break
            elif action == 'S':
                break

        
        if calculate_hand_value(player_hand) <= 21:
            print(f"\nMano de la casa: {house_hand} (valor: {calculate_hand_value(house_hand)})")
            while calculate_hand_value(house_hand) <= 16:
                house_hand.append(deck.pop())
                print(f"Mano de la casa: {house_hand} (valor: {calculate_hand_value(house_hand)})")

            if calculate_hand_value(house_hand) > 21:
                print("La casa se ha pasado de 21. ¡Ganaste!")
                player_chips += bet
            else:
                player_value = calculate_hand_value(player_hand)
                house_value = calculate_hand_value(house_hand)
                if player_value > house_value:
                    print("¡Ganaste!")
                    player_chips += bet
                elif player_value < house_value:
                    print("La casa ganó. ¡Perdiste!")
                    player_chips -= bet
                else:
                    print("Empate. Te devuelven tu apuesta.")

    print("Gracias por jugar!")

if __name__ == "__main__":
    play_blackjack()

