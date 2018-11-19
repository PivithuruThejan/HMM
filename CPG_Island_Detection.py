transition_matrix = [
    [0.0000000000, 0.0725193101, 0.1637630296, 0.1788242720, 0.0754545682, 0.1322050994, 0.1267006624, 0.1226380452,
     0.1278950131],
    [0.0010000000, 0.1762237762, 0.2682517483, 0.4170629371, 0.1174825175, 0.0035964036, 0.0054745255, 0.0085104895,
     0.0023976024],
    [0.0010000000, 0.1672435130, 0.3599201597, 0.2679840319, 0.1838722555, 0.0034131737, 0.0073453094, 0.0054690619,
     0.0037524950],
    [0.0010000000, 0.1576223776, 0.3318881119, 0.3671328671, 0.1223776224, 0.0032167832, 0.0067732268, 0.0074915085,
     0.0024975025],
    [0.0010000000, 0.0773426573, 0.3475514486, 0.3759440559, 0.1781818182, 0.0015784216, 0.0070929071, 0.0076723277,
     0.0036363636],
    [0.0010000000, 0.0002997003, 0.0002047952, 0.0002837163, 0.0002097902, 0.2994005994, 0.2045904096, 0.2844305694,
     0.2095804196],
    [0.0010000000, 0.0003216783, 0.0002977023, 0.0000769231, 0.0003016983, 0.3213566434, 0.2974045954, 0.0778441558,
     0.3013966034],
    [0.0010000000, 0.0002477522, 0.0002457542, 0.0002977023, 0.0002077922, 0.2475044955, 0.2455084915, 0.2974035964,
     0.2075844156],
    [0.0010000000, 0.0001768232, 0.0002387612, 0.0002917083, 0.0002917083, 0.1766463536, 0.2385224775, 0.2914165834,
     0.2914155844]
]

chracter_mapper = {
    "A": 1,
    "C": 2,
    "G": 3,
    "T": 4
}


def viterbi(sequence):
    sequence = sequence.upper()

    #probility  values for plus and minus states
    actual_positive_probability = 0
    actual_minus_probability = 0

    # temp probabilities
    temporary_positive_probability = 0
    temporary_negative_probability = 0

    # actual paths for output
    path_plus = ""
    path_minus = ""

    # get initial character
    if len(sequence) == 0:
        return

    # get character index
    positive_index = chracter_mapper[sequence[0]]
    minus_index = positive_index + 4

    # initial probabilities
    actual_positive_probability = transition_matrix[0][positive_index]
    actual_minus_probability = transition_matrix[0][minus_index]

    # last seen state
    previous_positive = positive_index
    previous_negative = minus_index

    for point in range(0, len(sequence)):
        # get the indices for current character
        positive_index = chracter_mapper[sequence[point]]
        minus_index = positive_index + 4

        transition_plus_plus = actual_positive_probability * transition_matrix[previous_positive][positive_index] * 1.0
        transition_plus_minus = actual_positive_probability * transition_matrix[previous_positive][minus_index] * 1.0
        transition_minus_plus = actual_minus_probability * transition_matrix[previous_negative][positive_index] * 1.0
        transition_minus_minus = actual_minus_probability * transition_matrix[previous_negative][minus_index] * 1.0

        # check if it's + --> + or - --> -
        if transition_plus_plus >= transition_minus_plus:
            temporary_positive_probability = transition_plus_plus
            path_plus = path_plus + "+"
        else:
            temporary_positive_probability = transition_minus_plus
            path_plus = path_minus + "+"

        if transition_plus_minus >= transition_minus_minus:
            temporary_negative_probability = transition_plus_minus
            path_minus = path_plus + "-"
        else:
            temporary_negative_probability = transition_minus_minus
            path_minus = path_minus + "-"

        previous_positive = positive_index
        previous_negative = minus_index
        actual_positive_probability = temporary_positive_probability
        actual_minus_probability = temporary_negative_probability

    decoding = ""

    if actual_positive_probability > actual_minus_probability:
        decoding = path_plus
    else:
        decoding = path_minus

    return decoding


file = open("input", "r")
data = file.read().replace("\n", "")
output = viterbi(data).replace("\n", "")
file = open("output.txt", "w+")
file.write(output)
file.close()
