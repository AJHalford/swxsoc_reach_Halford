import pytest

import swxsoc_reach.util.util as util
from swxsoc_reach import _test_files_directory
from swxsoc_reach.io import read_file

TIME = "2024-04-06T12:06:21"
TIME_FORMATTED = "20240406T120621"

test_file_paths = _test_files_directory.glob("*.csv")
valid_datatypes = list(util.TOKEN_TO_DATATYPE.values())

@pytest.mark.parametrize("this_path", list(test_file_paths))
def test_filename_to_datatype(this_path):
    """Test that raw filenames output correct datatypes"""
    this_datatype = util.filename_to_datatype(this_path.name)
    assert isinstance(this_datatype, str)
    assert this_datatype in valid_datatypes


# fmt: off
@pytest.mark.parametrize("instrument,time,level,version,result", [
    ("meddea", TIME, "l1", "1.2.3", f"padre_meddea_l1_{TIME_FORMATTED}_v1.2.3.fits"),
    ("meddea", TIME, "l2", "2.4.5", f"padre_meddea_l2_{TIME_FORMATTED}_v2.4.5.fits"),
    ("sharp", TIME, "l2", "1.3.5", f"padre_sharp_l2_{TIME_FORMATTED}_v1.3.5.fits"),
    ("sharp", TIME, "l3", "2.4.5", f"padre_sharp_l3_{TIME_FORMATTED}_v2.4.5.fits"),
]
)
def test_science_filename_output_a(instrument, time, level, version, result):
    """Test simple cases with expected output.
    Since we are using the swxsoc create_science_filename, we are testing whether we did the config correctly in __init__.py"""
    assert (
        util.create_science_filename(instrument, time, level=level, version=version)
        == result
    )
# fmt: on


# fmt: off
@pytest.mark.parametrize("time,level,version,descriptor,result", [
    (TIME, "l1", "1.2.3", "adcs", f"swxsoc_reach_l1_adcs_{TIME_FORMATTED}_v1.2.3.fits"),
    (TIME, "l2", "2.4.5", "adcs", f"swxsoc_reach_l2_adcs_{TIME_FORMATTED}_v2.4.5.fits"),
    (TIME, "l2", "1.3.5", "gnss", f"swxsoc_reach_l2_gnss_{TIME_FORMATTED}_v1.3.5.fits"),
    (TIME, "l3", "2.4.5", "hk", f"swxsoc_reach_l3_hk_{TIME_FORMATTED}_v2.4.5.fits"),
]
)
def test_craft_filename_output_a(time, level, version, descriptor, result):
    """Test simple cases with expected output.
    Since we are using the swxsoc create_science_filename, we are testing whether we did the config correctly in __init__.py"""
    assert (
        util.create_craft_filename(time, level=level, descriptor=descriptor, version=version)
        == result
    )
# fmt: on
