import json
import re


def get_trading_recommendations(
    system_prompt: str,
    user_message: str,
    provider: str,
    api_key: str,
) -> list:
    if not api_key:
        raise ValueError("No API key provided.")

    response_text = ""

    if provider == "anthropic":
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)
        from trading_bot.config import ANTHROPIC_MODEL
        msg = client.messages.create(
            model=ANTHROPIC_MODEL,
            max_tokens=1024,
            system=system_prompt,
            messages=[{"role": "user", "content": user_message}],
        )
        response_text = msg.content[0].text

    elif provider == "openai":
        import openai
        client = openai.OpenAI(api_key=api_key)
        from trading_bot.config import OPENAI_MODEL
        resp = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
            max_tokens=1024,
        )
        response_text = resp.choices[0].message.content
    else:
        raise ValueError(f"Unknown provider: {provider}")

    # Parse JSON
    try:
        return json.loads(response_text)
    except json.JSONDecodeError:
        pass

    # Try to extract JSON array from response
    m = re.search(r"\[.*\]", response_text, re.DOTALL)
    if m:
        try:
            return json.loads(m.group())
        except json.JSONDecodeError:
            pass

    raise ValueError(f"Could not parse JSON from LLM response:\n{response_text[:500]}")
