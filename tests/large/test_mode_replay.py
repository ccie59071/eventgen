import subprocess
from datetime import datetime
import re
import time


def test_mode_replay():
    """Test normal replay mode settings"""
    current_datetime = datetime.now()
    output = subprocess.check_output(["splunk_eventgen", "generate", "conf/eventgen_replay.conf"])
    events = output.split("\n")[:-1]
    # assert the event length is the same as sample file size
    assert len(events) == 12
    pattern = re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")
    for event in events:
        # assert that integer token is replaced
        assert "@@integer" not in event
        result = pattern.match(event)
        assert result is not None
        event_datetime = datetime.strptime(result.group(), "%Y-%m-%d %H:%M:%S")
        delter_seconds = (event_datetime - current_datetime).total_seconds()
        # assert the event time is after (now - earliest) time
        assert 60 > delter_seconds > -5


def test_mode_replay_end_1():
    """Test normal replay mode with end = 2 which will replay the sample twice and exit"""
    output = subprocess.check_output(["splunk_eventgen", "generate", "conf/eventgen_replay_end_1.conf"])
    events = output.split("\n")[:-1]
    # assert the event length is twice of the events in the sample file
    assert len(events) == 24


def test_mode_replay_end_2():
    """Test normal replay mode with end = -1 which will replay the sample forever"""
    process = subprocess.Popen(["splunk_eventgen", "generate", "conf/eventgen_replay_end_2.conf"])
    time.sleep(60)
    assert process.poll() is None
    process.terminate()


def test_mode_replay_timemultiple():
    """Test normal replay mode with timeMultiple = 0.5 which will replay the sample with half time interval"""
    current_datetime = datetime.now()
    output = subprocess.check_output(["splunk_eventgen", "generate", "conf/eventgen_replay_timeMultiple.conf"])
    events = output.split("\n")[:-1]

    pattern = re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")
    for event in events:
        result = pattern.match(event)
        assert result is not None
        event_datetime = datetime.strptime(result.group(), "%Y-%m-%d %H:%M:%S")
        delter_seconds = (event_datetime - current_datetime).total_seconds()
        # assert the event time is after (now - earliest) time
        assert delter_seconds < 11

def test_mode_replay_csv():
    """Test normal replay mode with sampletype = csv which will get _raw row from the sample"""
    output = subprocess.check_output(["splunk_eventgen", "generate", "conf/eventgen_replay_csv.conf"])
    events = output.split("\n")[:-1]
    # assert the events equals to the sample csv file
    assert len(events) == 10
