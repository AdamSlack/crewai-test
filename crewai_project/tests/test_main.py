import pytest
from crewai_project.main import main
from unittest.mock import patch

def test_main_runs_without_error():
    try:
        main()
    except Exception as e:
        pytest.fail(f"main() raised an exception: {e}")

def test_main_prints_start_message():
    with patch("builtins.print") as mock_print:
        main()
        mock_print.assert_called_once_with("CrewAI project started via Docker.") 