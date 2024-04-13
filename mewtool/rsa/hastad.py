from mewtool.number.util import nth_root, crt


def hastad_find_message(pair: tuple[int, int], e: int) -> int:
    """Broadcast attack to recover the plaintext from a pair of ciphertext and public key.

    Args:
        pair: tuple of ciphertext and modulo (c, n)
        e: public exponent

    Returns:
        int: The plaintext
    """

    assert len(pair) > 2, "At least 3 pairs are required"

    crt_result = crt(pair)
    result = nth_root(crt_result, e)

    # Do an assertion
    c, n = pair[0]
    assert pow(result, e, n) == c, "Failed to recover the plaintext"

    return result
