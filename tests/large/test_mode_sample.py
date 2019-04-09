import subprocess
from datetime import datetime
import re


def test_mode_sample():
    """Test normal sample mode with end = 1 which will generate the from the sample once"""
    current_datetime = datetime.now()
    output = subprocess.check_output(["splunk_eventgen", "generate", "conf/eventgen_sample.conf"])

    events = output.split("\n")[:-1]
    # assert the event length is the same as sample file size when end = 1
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
        assert delter_seconds > -15


