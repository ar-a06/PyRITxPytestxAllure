import allure

from utils.response_utils import extract_llm_response


def generate_allure_report(memory, score_memory, category):
    """Generate an Allure report from the test results"""
    for prompt_data, score_data in zip(memory, score_memory):

        score = True if str(score_data.score_value).lower() == "true" else False

        test_description = (
            f"**Test Category**: {category}\n\n"
            f"**Prompt**: {prompt_data._converted_value}\n\n"
            f"**Response**:{extract_llm_response(memory)}\n\n"
            f"**Evaluation Score**: {'✅ Pass' if score else '❌ Fail'}\n\n"
            f"**Scoring Reasoning**: {score_data.score_rationale}\n\n"
        )

        with allure.step(f"Test: {category}-{prompt_data._converted_value}"):
            allure.dynamic.description(test_description)

            allure.attach(
                name="Test Summary",
                body=test_description,
                attachment_type=allure.attachment_type.TEXT
            )

            if not score:
                assert False, f"Test failed for prompt: {prompt_data._converted_value}"

            # metadata_table = "| Key | Value |\n| --- | --- |\n"
            # for key,value in prompt_data.prompt_metadata.items():
            #     metadata_table+=f"| {key} | {value} |\n"
            #
            # allure.attach(
            #     name="Metadata",
            #     body=metadata_table,
            #     attachment_type=allure.attachment_type.TEXT
            # )

        # with allure.step(f"Test: {category} - {prompt_data._converted_value}"):
        #     allure.attach(f"Labels:{prompt_data.labels}", name="Labels")
        #     allure.attach(f"Response: {extract_llm_response(memory)}", name="Response")
        #     allure.attach(f"Score: {score_data.score_value}", name="Evaluation Score")
        #     allure.attach(f"Reasoning: {score_data.score_rationale}", name="Scoring Reasoning")
        #     allure.attach(f"Metadata: {prompt_data.prompt_metadata or 'N/A'}", name="Metadata")
        #
        #     if not score_data.score_value:
        #         allure.dynamic.description(f"Test failed for prompt: {prompt_data._converted_value}")
        #         assert False, f"Test failed for prompt: {prompt_data._converted_value}"