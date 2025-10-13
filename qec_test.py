# qec_test.py

import numpy as np

# Example: Trinary (qutrit) repetition code (majority vote)
def encode_qutrit(data):
    """Encodes a single trit as a repetition code."""
    return [data, data, data]

def introduce_error(codeword, pos, error_trit):
    """Introduce a trit-flip error at position pos."""
    codeword = codeword.copy()
    codeword[pos] = error_trit
    return codeword

def decode_qutrit(codeword):
    """Decode using majority vote (trit)."""
    # For qutrits, majority vote using numpy bincount
    counts = np.bincount(codeword, minlength=3)
    return np.argmax(counts)

def test_qec_no_error():
    data = 2
    encoded = encode_qutrit(data)
    decoded = decode_qutrit(encoded)
    assert decoded == data, f"No error: decoded={decoded} != original={data}"

def test_qec_with_error():
    data = 1
    encoded = encode_qutrit(data)
    # Introduce a single trit-flip error at position 0
    for error_trit in [0, 2]:
        if error_trit == data:
            continue
        corrupted = introduce_error(encoded, 0, error_trit)
        decoded = decode_qutrit(corrupted)
        assert decoded == data, f"Error: decoded={decoded} != original={data} (corrupted={corrupted})"

if __name__ == "__main__":
    test_qec_no_error()
    test_qec_with_error()
    print("All QEC trinary repetition code tests pass.")
