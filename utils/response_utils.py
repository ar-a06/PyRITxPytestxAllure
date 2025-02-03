def extract_llm_response(processed_memories):
    """Extract the LLM response from processed_memories where role is 'assistant'."""
    for memory in processed_memories:
        if hasattr(memory, 'role') and memory.role == 'assistant':
            assistant_response = getattr(memory, '_original_value', None) or getattr(memory, '_converted_value', None)
            if assistant_response:
                return assistant_response
    return "N/A"
