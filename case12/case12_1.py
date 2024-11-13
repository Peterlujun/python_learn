def is_valid_fish_count(initial_fish):
    remaining_fish = initial_fish
    for step in range(1, 5):
        # 检查剩余的鱼的数量是否满足条件
        if (remaining_fish + 1) % (step + 1) == 0:
            remaining_fish -= (remaining_fish + 1) // (step + 1)
        else:
            return False
    # 最终条件：第五次操作后剩余11条鱼
    return remaining_fish == 11

def find_initial_fish_count():
    fish_count = 23  # 从23条鱼开始
    while True:
        if is_valid_fish_count(fish_count):
            return fish_count
        fish_count += 2  # 增加2，因为鱼的条数是奇数

if __name__ == "__main__":
    initial_fish = find_initial_fish_count()
    print(f"原来鱼缸中共有{initial_fish}条金鱼.")
