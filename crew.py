from crewai import Crew, Process
from agents import page_scanner, change_detector, impact_analyzer, gemini_llm
from tasks import page_scanning_task, change_detection_task, impact_assessment_task

crew = Crew(
    agents=[page_scanner, change_detector, impact_analyzer],
    tasks=[page_scanning_task, change_detection_task, impact_assessment_task],
    process=Process.sequential,
    cache=True,
    max_rpm=100,
    share_crew=True,
    manager_llm=gemini_llm
)

test_urls = {
    "1": "https://www.google.com",
    "2": "https://httpbin.org/forms/post", 
    "3": "https://www.w3schools.com/html/html_forms.asp",
    "4": "https://github.com/login",
    "5": "https://demoqa.com/automation-practice-form",
}

def main():
    print("Web UI Change Detector and Impact Assessor")
    print("-" * 50)
    print("Choose a test URL or enter your own:")

    for key, url in test_urls.items():
        print(f"{key}. {url}")
    print("6. Enter custom URL")
    
    choice = input("\nEnter choice (1-6): ")
    
    if choice in test_urls:
        target_url = test_urls[choice]
    elif choice == "6":
        target_url = input("Enter URL: ")
    else:
        target_url = test_urls["1"]
    
    print(f"\n Analyzing: {target_url}")
    print("This will capture the current state and analyze potential automation impact...")

    result = crew.kickoff(inputs={'url': target_url})
    
    print("\n Analysis Complete!")
    print(f" Report saved to: ui_change_impact_report.md")
    print(f" Result: {result}")

if __name__ == "__main__":
    main()