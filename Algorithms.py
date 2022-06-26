#Towers of Hanoi:
def hanoi (n, start_pole, end_pole, inter_pole):
    if n >= 1:
        hanoi(n - 1, start_pole, inter_pole, end_pole)
        print('Disk moved from ', start_pole,'to ', end_pole)
        hanoi(n - 1, inter_pole, end_pole, start_pole)

hanoi(3, 'a', 'b', 'c')

