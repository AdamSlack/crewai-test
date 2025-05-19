import pytest
from unittest.mock import patch, MagicMock, ANY
import sys

import presales_crew.main as main

@pytest.fixture(autouse=True)
def restore_sys_argv():
    original_argv = sys.argv.copy()
    yield
    sys.argv = original_argv

def test_run_calls_kickoff():
    with patch('presales_crew.main.PresalesCrew') as MockCrew:
        mock_crew = MockCrew.return_value
        mock_crew.crew.return_value.kickoff = MagicMock()
        main.run()
        mock_crew.crew.return_value.kickoff.assert_called_once()

def test_run_handles_exception():
    with patch('presales_crew.main.PresalesCrew') as MockCrew:
        mock_crew = MockCrew.return_value
        mock_crew.crew.return_value.kickoff.side_effect = Exception("fail")
        with pytest.raises(Exception, match="An error occurred while running the crew: fail"):
            main.run()

def test_train_calls_train():
    sys.argv = ["main.py", "5", "output.txt"]
    with patch('presales_crew.main.PresalesCrew') as MockCrew:
        mock_crew = MockCrew.return_value
        mock_crew.crew.return_value.train = MagicMock()
        main.train()
        mock_crew.crew.return_value.train.assert_called_once_with(n_iterations=5, filename="output.txt", inputs=ANY)

def test_train_handles_exception():
    sys.argv = ["main.py", "5", "output.txt"]
    with patch('presales_crew.main.PresalesCrew') as MockCrew:
        mock_crew = MockCrew.return_value
        mock_crew.crew.return_value.train.side_effect = Exception("fail")
        with pytest.raises(Exception, match="An error occurred while training the crew: fail"):
            main.train()

def test_replay_calls_replay():
    sys.argv = ["main.py", "task123"]
    with patch('presales_crew.main.PresalesCrew') as MockCrew:
        mock_crew = MockCrew.return_value
        mock_crew.crew.return_value.replay = MagicMock()
        main.replay()
        mock_crew.crew.return_value.replay.assert_called_once_with(task_id="task123")

def test_replay_handles_exception():
    sys.argv = ["main.py", "task123"]
    with patch('presales_crew.main.PresalesCrew') as MockCrew:
        mock_crew = MockCrew.return_value
        mock_crew.crew.return_value.replay.side_effect = Exception("fail")
        with pytest.raises(Exception, match="An error occurred while replaying the crew: fail"):
            main.replay()

def test_test_calls_test():
    sys.argv = ["main.py", "3", "gpt-4"]
    with patch('presales_crew.main.PresalesCrew') as MockCrew:
        mock_crew = MockCrew.return_value
        mock_crew.crew.return_value.test = MagicMock()
        main.test()
        mock_crew.crew.return_value.test.assert_called_once_with(n_iterations=3, eval_llm="gpt-4", inputs=ANY)

def test_test_handles_exception():
    sys.argv = ["main.py", "3", "gpt-4"]
    with patch('presales_crew.main.PresalesCrew') as MockCrew:
        mock_crew = MockCrew.return_value
        mock_crew.crew.return_value.test.side_effect = Exception("fail")
        with pytest.raises(Exception, match="An error occurred while testing the crew: fail"):
            main.test() 