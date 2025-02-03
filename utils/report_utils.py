import csv
import json
import datetime

from utils.response_utils import extract_llm_response


async def generate_report(memory, score_memory, category, report_format="allure"):
    """Generate a report in the specified format."""
    timestamp=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    results=[]

    for prompt_data, score_data in zip(memory,score_memory):

        results.append({
            "prompt": prompt_data._converted_value,
            "response":extract_llm_response(memory),
            "score": score_data.score_value,
            "status": "Pass" if score_data.score_value  else "Fail",
            "metadata": prompt_data.prompt_metadata or "N/A",
            "score_reasoning":score_data.score_rationale
        })

    if report_format=="csv":
        with open(f"reports/csv_reports/{category}_{timestamp}.csv","w") as file:
            writer = csv.DictWriter(file, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
    elif report_format == "json":
        with open(f"reports/json_reports/{category}_{timestamp}.json","w") as file:
            json.dump(results, file, indent=4)