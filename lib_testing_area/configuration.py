# ==================== ------------------------ ====================
#                      Configuration declaration
from enum import Enum, auto
import logging

# Utilities
TO_ROUND = 5
FORMATTER = logging.Formatter('%(asctime)s - + %(relativeCreated)d - %(name)s - %(levelname)s - %(message)s')

class JSON_parsable_Enum():
    pass

class JSON_parsable_Dict():
    pass

class SUPPORTED_IMAGE_TYPE(JSON_parsable_Enum, Enum):
    PNG = auto()
    BMP = auto()

class ALGO_TYPE(JSON_parsable_Enum, Enum):
    A_HASH = auto()
    P_HASH = auto()
    P_HASH_SIMPLE = auto()
    D_HASH = auto()
    D_HASH_VERTICAL = auto()
    W_HASH = auto()
    TLSH = auto()
    TLSH_NO_LENGTH = auto()
    ORB = auto()

# Threshold finder
class THRESHOLD_MODE(JSON_parsable_Enum, Enum):
    MIN_WRONG = auto()
    MEDIAN_WRONG = auto()
    MAX_WRONG = auto()
    MAXIMIZE_TRUE_POSITIVE = auto()


# Threshold finder
class PICTURE_SAVE_MODE(JSON_parsable_Enum, Enum):
    TOP3 = auto()
    FEATURE_MATCHES_TOP3 = auto()
    RANSAC_MATRIX = auto()

class Default_configuration(JSON_parsable_Dict):
    def __init__(self):
        # Inputs
        self.SOURCE_DIR = None
        self.GROUND_TRUTH_PATH = None
        self.IMG_TYPE = SUPPORTED_IMAGE_TYPE.PNG
        # Processing
        self.ALGO = ALGO_TYPE.A_HASH
        self.SELECTION_THREESHOLD = None #TODO : To fix and to use, to prevent "forced linked" if none
        # Threshold
        self.THREESHOLD_EVALUATION = THRESHOLD_MODE.MAXIMIZE_TRUE_POSITIVE
        # Output
        self.SAVE_PICTURE_INSTRUCTION_LIST = []
        self.OUTPUT_DIR = None


# ==================== ------------------------ ====================
#                      ORB POSSIBLE CONFIGURATIONS
# See options there : https://docs.opencv.org/trunk/dc/d8c/namespacecvflann.html

class DISTANCE_TYPE(JSON_parsable_Enum, Enum):
    LEN_MIN = auto()
    LEN_MAX = auto()
    # LEN_MEAN = auto() # DOESNT WORK AT ALL
    MEAN_DIST_PER_PAIR = auto()
    MEAN_AND_MAX = auto()

class FILTER_TYPE(JSON_parsable_Enum, Enum):
    # RATIO_BAD = auto() # NOT with KNN # DOESNT WORK WELL
    RATIO_CORRECT = auto() # ONLY with KNN
    FAR_THREESHOLD = auto() # NOT with KNN = THREESHOLD DISTANCE # DOESNT WORK WELL
    #### BASIC_THRESHOLD = auto() # DOESNT WORK WELL
    NO_FILTER = auto()
    RANSAC = auto()

class MATCH_TYPE(JSON_parsable_Enum, Enum):
    STD = auto() # Standard
    KNN = auto()

class DATASTRUCT_TYPE(JSON_parsable_Enum, Enum):
    BRUTE_FORCE = auto()
    # FLANN_KDTREE = auto()  # DOESNT WORK AT ALL
    FLANN_LSH = auto()

class CROSSCHECK(JSON_parsable_Enum, Enum):
    ENABLED = auto()
    DISABLED = auto()
    AUTO = auto()

class POST_FILTER(JSON_parsable_Enum, Enum):
    NONE = auto()
    MATRIX_CHECK = auto()

class ORB_default_configuration(Default_configuration, JSON_parsable_Dict):
    def __init__(self):
        super().__init__()

        self.ORB_KEYPOINTS_NB = 500

        self.DISTANCE = DISTANCE_TYPE.LEN_MAX
        self.FILTER = FILTER_TYPE.NO_FILTER
        self.MATCH = MATCH_TYPE.STD
        self.DATASTRUCT = DATASTRUCT_TYPE.BRUTE_FORCE

        # Facultative depending on upper
        self.MATCH_K_FOR_KNN = 2

        # self.FLANN_KDTREE_INDEX = 0
        # self.FLANN_KDTREE_INDEX_params = dict(algorithm=self.FLANN_KDTREE_INDEX, trees=5)
        # self.FLANN_KDTREE_SEARCH_params = dict(checks=50)

        self.FLANN_LSH_INDEX = 6
        self.FLANN_LSH_INDEX_params = dict(algorithm=self.FLANN_LSH_INDEX, table_number=6, key_size=12, multi_probe_level=1)
        self.FLANN_LSH_SEARCH_params = dict(checks=50)  # or pass empty dictionary
        self.FLANN_LSH_INDEX_params_light = dict(algorithm=self.FLANN_LSH_INDEX, table_number=6)

        # Crosscheck is handled automatically
        self.CROSSCHECK = CROSSCHECK.AUTO

        # RANSAC parameter
        self.RANSAC_ACCELERATOR_THRESHOLD = 65 # Remove farthest matches
        self.POST_FILTER_CHOSEN = POST_FILTER.NONE

# ==================== ------------------------ ====================
#                      BoW ORB POSSIBLE CONFIGURATIONS
#

class BOW_CMP_HIST(JSON_parsable_Enum, Enum):
    CORREL = auto() # Standard
    BHATTACHARYYA = auto()

class BoW_ORB_default_configuration(Default_configuration, JSON_parsable_Dict):
    def __init__(self):
        super().__init__()

        self.ORB_KEYPOINTS_NB = 500

        # BOW SPECIFIC
        self.BOW_SIZE = 100
        self.BOW_CMP_HIST = BOW_CMP_HIST.CORREL


# ==================== ------------------------ ====================
#                        Custom configuration