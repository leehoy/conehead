import pytest
import numpy as np
from conehead.source import Source


class TestSource:
    def test_SAD(self):
        SAD = 50
        source = Source("varian_clinac_6MV", SAD=SAD)
        assert(source.SAD == 50)

    def test_source_not_implemented_error(self):
        with pytest.raises(NotImplementedError):
            Source("varian_clinac_10MV")

    def test_gantry_0(self):
        source = Source("varian_clinac_6MV")
        source.gantry(0)
        correct_pos = np.array([0, 0, 100])
        np.testing.assert_array_almost_equal(
            correct_pos, source.position, decimal=5
        )
        correct_rot = np.array([0, 0, 0])
        np.testing.assert_array_almost_equal(
            correct_rot, source.rotation, decimal=5
        )

    def test_gantry_45(self):
        source = Source("varian_clinac_6MV")
        source.gantry(45)
        correct_pos = np.array([np.cos(np.pi/4)*100, 0, np.sin(np.pi/4)*100])
        np.testing.assert_array_almost_equal(
            correct_pos, source.position, decimal=5
        )
        correct_rot = np.array([0, np.pi*7/4, 0])
        np.testing.assert_array_almost_equal(
            correct_rot, source.rotation, decimal=5
        )

    def test_gantry_225(self):
        source = Source("varian_clinac_6MV")
        source.gantry(225)
        correct_pos = np.array(
            [-np.cos(np.pi/4)*100, 0, -np.cos(np.pi/4)*100]
        )
        np.testing.assert_array_almost_equal(
            correct_pos, source.position, decimal=5
        )
        correct_rot = np.array([0, np.pi*3/4, 0])
        np.testing.assert_array_almost_equal(
            correct_rot, source.rotation, decimal=5
        )

    def test_gantry_270(self):
        source = Source("varian_clinac_6MV")
        source.gantry(270)
        correct_pos = np.array([-100, 0, 0])
        np.testing.assert_array_almost_equal(
            correct_pos, source.position, decimal=5
        )
        correct_rot = np.array([0, np.pi/2, 0])
        np.testing.assert_array_almost_equal(
            correct_rot, source.rotation, decimal=5
        )

    def test_collimator_90(self):
        source = Source("varian_clinac_6MV")
        source.collimator(90)
        correct_rot = np.array([0, 0, np.pi/2])
        np.testing.assert_array_almost_equal(
            correct_rot, source.rotation, decimal=5
        )

    def test_collimator_270(self):
        source = Source("varian_clinac_6MV")
        source.collimator(270)
        correct_rot = np.array([0, 0, np.pi*3/2])
        np.testing.assert_array_almost_equal(
            correct_rot, source.rotation, decimal=5
        )
