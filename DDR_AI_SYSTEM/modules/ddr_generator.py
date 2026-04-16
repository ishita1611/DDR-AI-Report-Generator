import ollama

def generate_ddr(text, _):

    prompt = f"""
From the following inspection and thermal scan data,
extract AREA-WISE OBSERVATIONS.

IMPORTANT:
- Each page should be treated as one inspection area.
- Do NOT say "no observations".
- If no visual inspection note exists write: Not Available
- Use temperature readings as the thermal finding.
- If image paths appear include them.

Format EXACTLY like this:

Area: Inspection Area (Page X)
Observation: <inspection observation or Not Available>
Thermal Finding: <temperature or thermal data>
Image: <image path or Image: Not Available>

DATA:
{text}
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0.2}
    )

    return response["message"]["content"]