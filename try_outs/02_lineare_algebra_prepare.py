import numpy as np
from icecream import ic


def multiply_matrix():
    a = np.array([[1, 2], [3, 4], [-1, 2]])
    b = np.array([[1, 1, -1]])
    c = np.array([[-2], [2]])
    d = np.array([[2, 4], [4, 2]])

    # multiplications syntax, alles dasselbe resultat
    multiplied = np.dot(a, c)
    ic(multiplied)

    mult = a.dot(d)
    ic(mult)

    m = a @ c
    ic(m)

    # elementweise produkt, identische dimensionen von matrix
    ele = d * d
    ic(ele)


def inverse_matrix_gleichungssystem():
    m = np.array(
        [
            [0, -3, -2],
            [1, -4, -2],
            [-3, 4, 1],
        ]
    )
    m_inv = np.linalg.inv(m)
    sol_arr = np.array([[1], [0], [1]])
    res = m_inv @ sol_arr
    ic(res)


def determinante_matrix():
    a = np.array([[1, 2], [-4, -3]])
    a_det = np.linalg.det(a)
    ic(a_det)
    a_inv = np.linalg.inv(a)
    ic(a_inv)
    einheit_a = a_inv @ a
    ic(einheit_a)
    ic("-")

    b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b_det = np.linalg.det(b)
    rounded_det = np.round(b_det, 10)  # sit quasi null
    ic(rounded_det)
    ic(b_det)
    b_inv = np.linalg.inv(b)
    einheit_b = b_inv @ b
    ic(einheit_b)
    ic(b_inv)
    ic("-")

    c = np.array([[1, 0, 0, 1], [2, 4, 3, 1], [-4, 4, 2, 2], [-1, 0, 0, 2]])
    c_det = np.linalg.det(c)
    ic(c_det)
    c_inv = np.linalg.inv(c)
    ic(c_inv)


def vektor_norm():
    u = np.array([[1], [0]])
    u1 = np.linalg.norm(u, ord=1)
    ic(u1)
    u2 = np.linalg.norm(u, ord=2)
    ic(u2)
    u_inf = np.linalg.norm(u, ord=np.inf)
    ic(u_inf)

    v = np.array([[1], [2], [-4]])
    v1 = np.linalg.norm(v, ord=1)
    ic(v1)
    v2 = np.linalg.norm(v, ord=2)
    ic(v2)
    v_inf = np.linalg.norm(v, ord=np.inf)
    ic(v_inf)
