# tests/test_analysis.py
import pytest
from assignmentpkg import Analysis


@pytest.fixture
def analysis_instance():
    return Analysis('config/user_config')  


def test_load_data(analysis_instance, capsys):
    analysis_instance.load_data()
    captured = capsys.readouterr()
    assert captured.out.strip() == "figure title"


def test_compute_analysis(analysis_instance):
    # Add tests for compute_analysis function
    pass


def test_plot_data(analysis_instance, caplog):
    with caplog.at_level(logging.INFO):
        analysis_instance.plot_data()
        assert "Saving plot to:" in caplog.text


def test_plot_data_with_save_path(analysis_instance, caplog):
    with caplog.at_level(logging.INFO):
        analysis_instance.plot_data(save_path='/path/to/save')
        assert "Saving plot to:" in caplog.text
        assert "/path/to/save" in caplog.text
