from crewai import Task
from tools import scraper_tool, file_tool
from agents import page_scanner, change_detector, impact_analyzer

page_scanning_task = Task(
    description="Scan and capture the current state of webpage: {url}. Extract key elements including buttons, forms, navigation, IDs, classes, and interactive elements. Save snapshot data for comparison.",
    expected_output="Detailed webpage structure analysis including all automation-relevant elements like buttons, forms, links, and their selectors (IDs, classes, XPaths).",
    tools=[scraper_tool, file_tool],
    agent=page_scanner
)

change_detection_task = Task(
    description="Compare the current webpage snapshot with previous version (if exists). Identify all changes including: moved elements, deleted elements, new elements, changed IDs/classes, modified text content.",
    expected_output="Comprehensive change report listing all detected differences between webpage versions with specific element details and locations.",
    tools=[file_tool],
    agent=change_detector
)

impact_assessment_task = Task(
    description="Analyze detected changes and assess their impact on browser automation. Determine which changes would break existing automation scripts, cause element selection failures, or require script updates.",
    expected_output="Impact assessment report with severity scores, broken automation predictions, and recommendations for maintaining robust web agents.",
    tools=[],
    agent=impact_analyzer,
    output_file='ui_change_impact_report.md'
)