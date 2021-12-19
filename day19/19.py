from scipy.spatial.distance import cdist, pdist
from itertools import product
import numpy as np

filename = 'data.txt'

with open(filename) as f:
    lines = f.readlines()

scanners = []

for line in lines:
    line = line.strip()
    if line.startswith('---'):
        scanner = []
    elif not line:
        scanner = np.array(scanner)
        scanners.append(scanner)
        scanner = None
    else:
        scanner.append([int(val) for val in line.split(',')])

# add last
if len(scanner):
    scanners.append(scanner)

vectors = [
    np.array((1, 0, 0)),
    np.array((-1, 0, 0)),
    np.array((0, 1, 0)),
    np.array((0, -1, 0)),
    np.array((0, 0, 1)),
    np.array((0, 0, -1)),
]

rotmats = []

for vi, vj in product(vectors, vectors):
    if vi @ vj == 0:
        vk = np.cross(vi, vj)
        rotmat = np.array([vi, vj, vk])
        rotmats.append(rotmat)

assert len(rotmats) == 24

OFFSETS = [np.array((0,0,0))]


def solve(beacons, scanners):
    try_again = []

    for i, other in enumerate(scanners):
        best_rotmat = None
        best_n_matches = 0

        for rotmat in rotmats:
            rotated = other @ rotmat
            dist = cdist(beacons, rotated)
            uniq, counts = np.unique(dist, return_counts=True)
            i_max = counts.argmax()
            n_matches = counts[i_max]
            common_dist = uniq[i_max]

            if n_matches > best_n_matches:
                best_n_matches = n_matches
                best_rotmat = dist, common_dist, rotated

        if best_n_matches < 6:
            try_again.append(other)
            continue

        dist, common_dist, rotated = best_rotmat
        common_beacons = np.argwhere(dist == common_dist)

        from_beacons, from_other = common_beacons.T
        vector = (beacons[from_beacons] - rotated[from_other])[0]

        beacons = np.vstack((beacons, rotated + vector))

        beacons = np.unique(beacons, axis=0)

        OFFSETS.append(vector)

    if len(try_again) > 0:
        beacons = solve(beacons, try_again)

    return beacons


beacons = solve(scanners[0], scanners[1:])

print(f'part 1: {len(beacons)=}')
print(f"part 2: {pdist(OFFSETS, metric='cityblock').max()=}")
