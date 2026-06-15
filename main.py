import random
import time

def generuj_kierowcow():
    return [
        {"imie": "Verstappen", "boost": 100, "czas": 0.0},
        {"imie": "Norris", "boost": 100, "czas": 0.0},
        {"imie": "Hamilton", "boost": 100, "czas": 0.0},
        {"imie": "Leclerc", "boost": 100, "czas": 0.0},
        {"imie": "Piastri", "boost": 100, "czas": 0.0},
        {"imie": "Sainz", "boost": 100, "czas": 0.0},
        {"imie": "Russell", "boost": 100, "czas": 0.0},
        {"imie": "TY (Gracz)", "boost": 100, "czas": 0.0}
    ]

def oblicz_okrazenie(kierowca, uzyto_boost):
    baza = 80.0
    losowosc = random.uniform(-0.3, 0.3)

    if uzyto_boost and kierowca["boost"] >= 25:
        kierowca["boost"] -= 25
        return baza - 1.5 + losowosc
    else:
        kierowca["boost"] = min(100, kierowca["boost"] + 10)
        return baza + losowosc

def uruchom_symulator():
    LAPS = 10
    kierowcy = generuj_kierowcow()

    print("=== SYMULATOR STRATEGII F1 ===")
    input("Wciśnij ENTER, aby wystartować...")

    for lap in range(1, LAPS + 1):
        print(f"\n=== OKRĄŻENIE {lap}/{LAPS} ===")

        gracz = next(k for k in kierowcy if k["imie"] == "TY (Gracz)")
        print(f"[TWÓJ BOLID] Poziom boostu: {gracz['boost']}%")

       uzyj_boost_gracz = False
        if gracz["boost"] >= 25:
            while True:
                decyzja = input("Czy użyć boostu (-1.5s do czasu)? (t/n): ").strip().lower()
                
                if decyzja == 't':
                    uzyj_boost_gracz = True
                    break
                elif decyzja == 'n':
                    uzyj_boost_gracz = False
                    break
                else:
                    print("Niepoprawny wybór! Wpisz literę 't' (tak) lub 'n' (nie).")

        for k in kierowcy:
            if k["imie"] == "TY (Gracz)":
                stan_boost = uzyj_boost_gracz
            else:
                if k["boost"] > 70:
                    stan_boost = random.random() < 0.6
                elif 30 <= k["boost"] <= 70:
                    stan_boost = random.random() < 0.35
                else:
                    stan_boost = random.random() < 0.15

            k["czas"] += oblicz_okrazenie(k, stan_boost)

        kierowcy_sort = sorted(kierowcy, key=lambda x: x["czas"])

        print("==================================================")
        print(f"{'POZ':<4} | {'KIEROWCA':<12} | {'BOOST':<8} | {'STRATA':<10}")
        print("==================================================")

        lider_time = kierowcy_sort[0]["czas"]
        for i, k in enumerate(kierowcy_sort, 1):
            strata = "LIDER" if i == 1 else f"+{k['czas'] - lider_time:.3f}s"
            tekst_boost = f"{k['boost']}%"
            print(f"{i:<4} | {k['imie']:<12} | {tekst_boost:<8} | {strata:<10}")

        print("==================================================")

        time.sleep(1)

    print("\n================ KONIEC WYŚCIGU ================")
    print(f"WYGRYWA: {kierowcy_sort[0]['imie']}!")


if __name__ == "__main__":
    uruchom_symulator()
