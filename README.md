# Mutual Fund Analyzer with CrewAI

## Introduction

## CrewAI Framework
CrewAI is designed to facilitate the collaboration of role-playing AI agents. In this example, these agents work together to identify & rank mutual funds based on the given inputs.

## Running the Script
It uses GPT-4o by default so you should have access to that to run it.

***Disclaimer:** This will use gpt-4o unless you change it to use a different model, and by doing so it may incur different costs.*

- **Configure Environment**: Copy `.env.example` and set up the environment variables for [OpenAI](https://platform.openai.com/api-keys) and other tools as needed.
- **Install Dependencies**: Run `poetry lock && poetry install`.
- **Customize**: Modify `src/mfanalyser/main.py` to add custom inputs for your agents and tasks.
- **Customize Further**: Check `src/mfanalyser/config/agents.yaml` to update your agents and `src/mfanalyser/config/tasks.yaml` to update your tasks.
- **Custom Tools**: You can find custom tools at `mfanalyser/src/tools/`.
- **Execute the Script**: Run `poetry run mfanalyser` and input your project details.

## Details & Explanation
- **Running the Script**: Execute `poetry run mfanalyser`. The script will leverage the CrewAI framework to find the best mutual funds for the given inputs & generate a detailed report.
- **Running Training**: Execute `poetry run train n` where n is the number of training iterations.
- **Key Components**:
  - `src/mfanalyser/main.py`: Main script file.
  - `src/mfanalyser/crew.py`: Main crew file where agents and tasks come together, and the main logic is executed.
  - `src/mfanalyser/config/agents.yaml`: Configuration file for defining agents.
  - `src/mfanalyser/config/tasks.yaml`: Configuration file for defining tasks.
  - `src/mfanalyser/tools`: Contains tool classes used by the agents.

## License
This project is released under the MIT License.

## Disclaimer
*This tool was created for educational purposes only and should not be considered as financial recommendations or advice.*


