# Mutual Fund Analyzer with CrewAI

## Introduction

## CrewAI Framework
CrewAI is designed to facilitate the collaboration of role-playing AI agents. In this example, these agents work together to identify & rank mutual funds based on the given inputs.

## Running the Script
- **Configure Environment**: Copy `.env.example` and set up the environment variables for [OpenAI](https://platform.openai.com/api-keys) and other tools as needed.
- **Install Dependencies**: Run `poetry lock && poetry install`.
- **Customize**: Modify `src/mfanalyser/main.py` to add custom inputs for your agents and tasks.
- **Customize Further**: Check `src/mfanalyser/config/agents.yaml` to update your agents and `src/mfanalyser/config/tasks.yaml` to update your tasks.
- **Custom Tools**: You can write further custom tools at `mfanalyser/src/tools/`. An example tool with gemini-pro integration has been provided for reference.
- **Execute the Script**: Run `poetry run mfanalyser` and input your project details.

## Details & Explanation
- **Running the Script**: Execute `poetry run mfanalyser`. The script will leverage the CrewAI framework to find the best mutual funds for the given inputs, analyse & rank them & generate a detailed report.
- **Running Training**: Execute `poetry run train n` where n is the number of training iterations.
- **Key Components**:
  - `src/mfanalyser/main.py`: Main script file.
  - `src/mfanalyser/crew.py`: Main crew file where agents and tasks come together, and the main logic is executed.
  - `src/mfanalyser/config/agents.yaml`: Configuration file for defining agents.
  - `src/mfanalyser/config/tasks.yaml`: Configuration file for defining tasks.
  - `src/mfanalyser/tools`: Contains tool classes used by the agents.

## Agents and Tasks in Mutual Funds Analyser

### Agents
Agents are autonomous entities designed to perform specific roles in analysing mutual funds. Each agent is configured with a clear role, goal, and backstory to ensure it effectively completes its tasks. The agents are fully customisable via the `agents.yaml` configuration file.

#### Default Agents
1. **Financial Researcher**:
   - **Role**: Financial Researcher
   - **Goal**: Fetch the latest mutual fund names with a positive sentiment from reliable sources.
   - **Backstory**: 
     - Expert in researching financial topics across the web.
     - Performs sentiment analysis to identify funds with positive public perception.

2. **Financial Data Gatherer**:
   - **Role**: Financial Data Gatherer
   - **Goal**: Fetch detailed financial data for the mutual funds identified by the researcher.
   - **Backstory**: 
     - Skilled at gathering structured financial data for specific mutual funds.
     - Focuses on obtaining key metrics like NAV, expense ratio, and historical returns.

3. **Financial Analyst**:
   - **Role**: Financial Analyst
   - **Goal**: Analyse and compare the financial data to identify top-performing mutual funds.
   - **Backstory**: 
     - Specialises in mutual fund analysis using best practices.
     - Scores funds based on performance, risk, expense ratio, and other metrics.
     - Detects patterns and trends in financial data to provide insights.

4. **Investment Advisor**:
   - **Role**: Investment Advisor
   - **Goal**: Provide tailored investment advice based on the financial data and analysis.
   - **Backstory**: 
     - Expert at presenting financial data in an understandable format.
     - Offers actionable investment advice linked to analysis findings.

---

### Tasks
Tasks define specific objectives that the agents collaborate on to complete. Each task has a description, expected output, and involves one or more agents. Tasks are fully customisable in the `tasks.yaml` configuration file.

#### Default Tasks
1. **Research Task**:
   - **Description**:
     - Search the internet for mutual fund information, focusing on topics such as asset class, investment objectives, structure, risk profile, market capitalisation, thematic focus, and more.
     - Conduct sentiment analysis to identify funds with positive sentiment in recent news and social media (last 2 months).
     - Ensure information is collected from reliable and relevant sources.
   - **Agents Involved**: Financial Researcher
   - **Expected Output**:
     - A comma-separated list of mutual fund scheme names, sorted by positive sentiment score in descending order.

2. **Data Gatherer Task**:
   - **Description**:
     - Search for financial data (e.g., NAV, expense ratio, historical returns) for each mutual fund identified in the research task.
     - Scrape data from reliable financial websites and organise it into a tabular structure for analysis.
   - **Agents Involved**: Financial Data Gatherer
   - **Expected Output**:
     - A structured table containing data like NAV, expense ratio, and 1-year, 2-year, 5-year returns for each mutual fund.

3. **Analysis Task**:
   - **Description**:
     - Map the mutual fund data to the research findings and data gatherer tasks.
     - Strictly follow the research findings and data gatherer tasks without deviation.
     - Analyse the mutual fund data by comparing performance, risk, expense ratios, and other metrics.
     - Follow industry best practices for financial analysis (e.g., assessing historical performance, risk-adjusted returns, and expense ratios).
     - Score each fund on a scale from 0 to 100 based on analysis criteria.
   - **Agents Involved**: Financial Analyst
   - **Expected Output**:
     - A structured list of the top 10 performing mutual funds, including their scores, risks, and potential gains.

4. **Advisor Task**:
   - **Description**:
     - Provide investment advice to the user based on the financial data and analysis.
     - Link recommendations to the analysis for transparency.
     - Summarise market conditions and provide actionable advice.
   - **Agents Involved**: Investment Advisor
   - **Expected Output**:
     - A detailed report including:
       - List of mutual funds with details like fund name, fund house, category, score, NAV, AUM, expense ratio, risks, and potential gains.
       - Summarised investment advice and market insights.

---

### Configuration
The agents and tasks are defined in the respective YAML files:
- **Agents**: `src/mfanalyser/config/agents.yaml`
- **Tasks**: `src/mfanalyser/config/tasks.yaml`

#### Adding or Modifying Agents and Tasks
1. **To Add or Modify Agents**:
   - Update the `agents.yaml` file with the new agent's role, goal, and backstory.
2. **To Add or Modify Tasks**:
   - Update the `tasks.yaml` file with the new task's description, expected output, and assigned agents.
3. Implement any additional logic or tools required in `src/mfanalyser/crew.py`.

This structure ensures flexibility and scalability for customising the mutual funds analyser.


## License
This project is released under the MIT License.

## Disclaimer
*This tool was created for educational purposes only and should not be considered as financial recommendations or advice.*


