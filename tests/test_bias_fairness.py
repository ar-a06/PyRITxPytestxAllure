import pytest_asyncio
import pytest

from object_model.bias_fairness.cultural_bias import Cultural_bias
from object_model.bias_fairness.gender_bias import Gender_bias
from object_model.bias_fairness.racial_bias import Racial_bias
from utils.allure_utils import generate_allure_report
from utils.report_utils import generate_report


@pytest.mark.asyncio
async def test_gender_bias_with_dynamic_prompts():
    gender_bias_tester = Gender_bias()
    memory, score_memory =await gender_bias_tester.test_gender_bias_with_dynamic_prompts()

    for score in score_memory:
        assert score.score_value, "Evaluation score is False, test failed."

    generate_allure_report(memory, score_memory, "Gender bias with dynamic prompts")
    await generate_report(memory, score_memory, "Gender bias", report_format="csv")

@pytest.mark.asyncio
async def test_gender_bias_with_predefined_prompts():
    gender_bias_tester = Gender_bias()
    memory, score_memory =await gender_bias_tester.test_gender_bias_with_predefined_prompts()

    for score in score_memory:
        assert score.score_value, "Evaluation score is False, test failed."

    generate_allure_report(memory, score_memory, "Gender bias with predefined prompts")
    await generate_report(memory, score_memory, "Gender bias", report_format="csv")

@pytest.mark.asyncio
async def test_cultural_bias_with_dynamic_prompts():
    cultural_bias_tester = Cultural_bias()
    memory, score_memory =await cultural_bias_tester.test_cultural_bias_with_dynamic_prompts()

    for score in score_memory:
        assert score.score_value, "Evaluation score is False, test failed."

    generate_allure_report(memory, score_memory, "Cultural bias with dynamic prompts")
    await generate_report(memory, score_memory, "Cultural bias", report_format="csv")

@pytest.mark.asyncio
async def test_cultural_bias_with_predefined_prompts():
    cultural_bias_tester = Cultural_bias()
    memory, score_memory =await cultural_bias_tester.test_cultural_bias_with_predefined_prompts()

    for score in score_memory:
        assert score.score_value, "Evaluation score is False, test failed."

    generate_allure_report(memory, score_memory, "Cultural bias with predefined prompts")
    await generate_report(memory, score_memory, "Cultural bias", report_format="csv")

@pytest.mark.asyncio
async def test_racial_bias_with_dynamic_prompts():
    racial_bias_tester = Racial_bias()
    memory, score_memory =await racial_bias_tester.test_racial_bias_with_dynamic_prompts()

    for score in score_memory:
        assert score.score_value, "Evaluation score is False, test failed."

    generate_allure_report(memory, score_memory, "Raciall bias with dynamic prompts")
    await generate_report(memory, score_memory, "Racial bias", report_format="csv")

@pytest.mark.asyncio
async def test_racial_bias_with_predefined_prompts():
    racial_bias_tester = Racial_bias()
    memory, score_memory =await racial_bias_tester.test_racial_bias_with_predefined_prompts()

    for score in score_memory:
        assert score.score_value, "Evaluation score is False, test failed."

    generate_allure_report(memory, score_memory, "Racial bias with predefined prompts")
    await generate_report(memory, score_memory, "Racial bias", report_format="csv")




