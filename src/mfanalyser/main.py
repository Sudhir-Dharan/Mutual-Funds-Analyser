#!/usr/bin/env python
import sys
from mfanalyser.crew import MFAnalyserCrew
import os
os.environ['LITELLM_LOG'] = 'DEBUG'


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'Asset Class': """
            Equity
        """,
        'Investment Objective': """
            Growth
        """,
        'Structure': """
            Open-Ended
        """,
        'Risk Profile': """
            High
        """,
        'Market Capitalization': """
            Large-Cap
        """,
        'Investment Style': """
            Active
        """,
        'Thematic or Sectoral Focus': """
            None
        """,
        'Tenure of Investment': """
            5 years
        """,
        'Tax Implications': """
            Equity-Oriented
        """,
        'Geographical Exposure': """
            Domestic
        """,
        'Fund Size': """
            Large
        """,
        'Payout Options': """
            Direct
        """,
        'Topic': """
            Top performing largecap funds in India good for SIP in 2025.
        """
    }
    try:
        MFAnalyserCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

def train():
    inputs = {
        'Topic': """
        Top performing Index funds in India good for SIP in 2025 based on latest NAV,expense ratio, 1 year return, 3 years return, 5 years return.
        """
    }
    try:
        MFAnalyserCrew().crew().train(n_iterations=int(sys.argv[1]), filename=str(sys.argv[2]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
