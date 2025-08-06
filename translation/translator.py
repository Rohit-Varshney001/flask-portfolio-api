def mock_translate(content, target_lang):
    # Replace this with real API if needed
    translated = {}
    for key, val in content.items():
        if isinstance(val, str):
            translated[key] = f"[{target_lang.upper()}] {val}"
        elif isinstance(val, list):
            translated[key] = [f"[{target_lang.upper()}] {v}" for v in val]
        elif isinstance(val, dict):
            translated[key] = mock_translate(val, target_lang)
        else:
            translated[key] = val
    return translated
