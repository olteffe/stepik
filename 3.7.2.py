def create_keys(encryption: str, decription: str) -> dict:
    encryption_key, decryption_key = {}, {}

    for idx in range(len(encryption)):
        encryption_key[encryption[idx]] = decription[idx]
        decryption_key[decription[idx]] = encryption[idx]
    return {"encryption": encryption_key, "decryption": decryption_key}


def main():
    original_alphabet, final_alphabet, to_be_encrypted, string_to_decrypt = input(), input(), input(), input()
    keys = create_keys(original_alphabet, final_alphabet)
    result = ["", ""]

    for character in to_be_encrypted:
        result[0] += keys["encryption"][character]
    for character in string_to_decrypt:
        result[1] += keys["decryption"][character]
    print(*result, sep="\n")


if __name__ == "__main__":
    main()
