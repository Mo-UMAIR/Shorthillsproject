def generate_markdown_report(content: str, filename: str = "contest_summary.md") -> str:
    """
    Saves formatted contest summary.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    return f"Report saved as {filename}"