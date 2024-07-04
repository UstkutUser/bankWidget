def mask_card(card_number: str) -> str:
    """Функция максирует номер карты"""
    masked_number = card_number[:6] + len(card_number[6:-4]) * "*" + card_number[-4:]
    return " ".join(
        [
            masked_number[i : i + 4]
            for i in range(0, len(card_number), len(card_number) // 4)
        ]
    )


def mask_account(bank_aсcount: str) -> str:
    """Функция максирует номер счета"""
    return "*" * 2 + bank_aсcount[-4:]


if __name__ == "__main__":
    print(mask_card("1234567891234356"))
    print(mask_account("73654108430135874305"))
