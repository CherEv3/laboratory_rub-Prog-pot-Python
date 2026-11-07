import math
MATERIALS = {
    "1": ("сталь", 80),
    "2": ("алюминий", 250),
    "3": ("чугун", 60),
}


def read_float(prompt: str, lo: float, hi: float) -> float:
    """Запрашивает число с проверкой диапазона [lo, hi]."""
    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            value = float(raw)
        except ValueError:
            print("  Ошибка: введите число.")
            continue
        if lo <= value <= hi:
            return value
        print(f"  Ошибка: значение должно быть в диапазоне {lo}..{hi}.")


def read_int(prompt: str, lo: int, hi: int) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("  Ошибка: введите целое число.")
            continue
        if lo <= value <= hi:
            return value
        print(f"  Ошибка: значение должно быть в диапазоне {lo}..{hi}.")


def processing_type(t: float) -> str:
    if t < 1:
        return "чистовая"
    if t <= 3:
        return "получистовая"
    return "черновая"


def main() -> None:
    print("Меню: 1 — сталь (V=80 м/мин), 2 — алюминий (V=250 м/мин), 3 — чугун (V=60 м/мин)")
    while True:
        choice = input("Выберите материал (1/2/3): ").strip()
        if choice in MATERIALS:
            break
        print("  Ошибка: введите 1, 2 или 3.")

    material, v = MATERIALS[choice]

    d = read_float("Введите D — диаметр фрезы, мм (5..200): ", 5, 200)
    z = read_int("Введите z — число зубьев (1..20): ", 1, 20)
    sz = read_float("Введите Sz — подача на зуб, мм/зуб (0.01..0.5): ", 0.01, 0.5)
    t = read_float("Введите t — глубина резания, мм (0.1..10): ", 0.1, 10)

    n = 1000 * v / (math.pi * d)
    s_min = sz * z * n
    mrr = t * (d / 2) * s_min / 1000

    print()
    print("Материал:", material)
    print(f"n = {n:.1f} об/мин")
    print(f"Sмин = {s_min:.1f} мм/мин")
    print(f"MRR = {mrr:.1f} см³/мин")
    print("Тип обработки:", processing_type(t))


if __name__ == "__main__":
    main()
