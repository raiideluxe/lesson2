import numpy as np

def closest(vecs, v, r):
    target_atom = vecs[v]
    count = 0
    for atom in vecs:
        distance = np.linalg.norm(target_atom - atom)
        if distance < r and not np.array_equal(target_atom, atom):
            count += 1
    return count

r = 2.5
v = 1
vecs = np.array([
[1.0, 0.0, 2.0],
[-1.0, 0.5, 2.0],
[-2.0, 1.5, 0.0],
[2.5, -1.2, -0.5],
[1.5, 0.2, -0.2]
])
print(closest(vecs, v, r)) # Вернет 2

r = 0.1
v = 0
vecs = np.array([[0.71, 0.7, 0.22, 0.98, 0.01],
[0.25, 0.43, 0.78, 0.2, 0.86]])
print(closest(vecs, v, r))