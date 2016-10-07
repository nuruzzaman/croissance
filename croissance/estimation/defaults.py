
CURVE_MINIMUM_DURATION_HOURS = 5

PHASE_MINIMUM_SIGNAL_NOISE_RATIO = 1.0
PHASE_MINIMUM_DURATION_HOURS = 1.5
PHASE_MINIMUM_SLOPE = 0.005

PHASE_RANK_EXCLUDE_BELOW = 33
PHASE_RANK_WEIGHTS = {
    'SNR': 50,
    'duration': 30,
    'slope': 10,
    # TODO add 1 - start?
}


# NOTE these defaults are good for fast growing bacteria such as E.coli:

MINIMUM_VALID_OD = 0.05
MINIMUM_VALID_SLOPE = 0.05
MINIMUM_DATA_HOURS = 5
RESAMPLE_POINTS_PER_HOUR = 6
PHASE_MIN_DELTA_LOG_OD = 0.20
PHASE_MIN_DELTA_OD = 0.25
MINIMUM_PHASE_LENGTH = 2

MINOR_PHASE_MERGING_THRESHOLD = 0.10 # in percent
