from PIL import Image

# Prompt for test code
prompt = '''
I have given you an image of form that has stored some INFORMATION.
Read that information from the image and show all the necessary details from the image.
'''
# Opening Image
image = Image.open("form.png")
# image2  = Image.Image.load("form.png")

# system_instruction and Role Prompting
system_instruction = '''
    You are a Senior Enterprise Document Intelligence AI operating in regulated
    environments such as government services, banking KYC, and compliance systems.
    '''

# Few shot prompting
fewshot_Prompting = '''
    Objective:
    Given a scanned document image, extract structured data, normalize fields, validate confidence, and generate a professional summary.

    Example 1:
    Input:
    [Image: Clear Government Identity Form Stored Informations]

    Output:
    Document Type:
    Government Identity Form
    Issuing Authority:
    Department of Civil Supplies
    Person Details:
    - Full Name: Ramesh Kumar
    - Date of Birth: 1991-07-14
    - Gender: Male
    Document Metadata:
    - Document Number: ID-458921
    - Issue Date: 2018-03-22
    Confidence Score:
    0.93

    Summary:
    This document is a government-issued identity form belonging to Ramesh Kumar, issued by the Department of Civil Supplies.

    Example 2:

    Input:
    [Image: Partially Blurred Registration Form]

    Output:
    Document Type:
    Registration Form
    Issuing Authority:
    State Registration Office
    Person Details:
    - Full Name: Not Available
    - Date of Birth: 1988-11-02
    - Gender: Not Available
    Document Metadata:
    - Document Number: Not Available
    - Issue Date: 2016-09-10
    Confidence Score:
    0.61

    Summary:
    This is a partially readable government registration form issued by the State Registration Office.

    Now do same like example with the given image:
    Task:
    Generate the final output strictly following the same structure, language tone, and formatting shown above. Return ONLY the formatted text.
    '''

# Role base prompting
role_prompt='''

'''


# Chain of thoughts Prompting
cot_prompt = '''
Objective:
Given a scanned document image, generate a professional compliance-grade textual report based only on visible information.

Rules that are MANDATORY:
- Perform step-by-step reasoning internally.
- Do NOT reveal reasoning, intermediate steps, or analysis.
- Only provide the final structured output.

Process steps (INTERNAL - do not output):
1. Visually inspect the document layout and symbols.
2. Identify document type and issuing authority.
3. Extract personal and document-specific fields.
4. Normalize dates and terminology.
5. Assess readability and completeness.
6. Generate a concise compliance-ready summary.
7. Assign a confidence score based on clarity and completeness.

STRICT rules:
1. Never hallucinate or infer missing data.
2. If any field is unclear, explicitly write "Not Available".
3. Preserve original spelling and casing for names.
4. Normalize dates to ISO format (YYYY-MM-DD).
5. Maintain neutral, professional, audit-safe language.
6. Output must strictly follow the format below.
7. Do not include explanations, reasoning, or metadata.

FINAL OUTPUT FORMAT:

Document Classification:
Issuing Authority:

Extracted Details:
- Full Name:
- Date of Birth:
- Gender:

Document Identifiers:
- Document Number:
- Issue Date:

Confidence Score:
Summary:

Now do same like example with the given image:
Intructions:
Apply internal rules reasoning. Return ONLY the final formatted output.
'''



# Tree of thought Prompt
tot_prompt = '''
Task Objective:
Analyze the provided document image and generate a compliance-ready textual report using you expertise in image and cv reasoning.

Policy that has to be follow (MANDATORY):
- Internally explore multiple reasoning branches.
- Evaluate alternative interpretations of the document.
- Select the most consistent and evidence-supported reasoning path.
- Do NOT reveal branches, scores, or reasoning steps.
- Output ONLY the final selected result.

Tree generation rules (INTERNAL - do not output):
1. Branch A: Interpret document as identity verification form.
2. Branch B: Interpret document as registration or application form.
3. Branch C: Interpret document as administrative record.
4. Score each branch based on visual evidence, completeness, and clarity.
5. Choose the highest-confidence branch.
6. Generate the final output based strictly on the selected branch.

Strict RULES:
1. Never hallucinate or assume missing information.
2. If data is unclear or absent, write "Not Available".
3. Preserve original spelling and casing.
4. Normalize dates to ISO format (YYYY-MM-DD).
5. Maintain formal, audit-safe language.
6. Do not include reasoning, alternatives, or system notes.
7. Output must strictly follow the format below.

FINAL OUTPUT FORMAT (TEXT ONLY):

Selected Interpretation:
Document Type:
Issuing Authority:

Extracted Information:
- Full Name:
- Date of Birth:
- Gender:

Document Identifiers:
- Document Number:
- Issue Date:

Confidence Score:
Summary:

Now do same like example with the given image:
Intructions:
Apply reasoning and strict rules internally. Return ONLY the final formatted output. You can also show the other
necessary details which you will find IMPORTANT and  relevant for the template.

'''


# contextual prompting
contextual_prompt = '''
CONTEXT:
This document is provided as part of a government compliance workflow.
The generated output will be reviewed by auditors and operations teams.
Accuracy, neutrality, and traceability are critical.

Task Objective:
Analyze the provided document image and generate a professional,
context-aware textual report based strictly on the visual content
and the provided operational context.

Internal RULES:
1. Treat the image as an official government or administrative document.
2. Assume the document is used for identity or registration verification.
3. Do not infer beyond what is visually present.
4. Missing or unclear information must be marked as "Not Available".
5. Preserve original casing and spelling.
6. Normalize dates to ISO format (YYYY-MM-DD).
7. Maintain formal, audit-safe language.
8. Do not include reasoning, analysis, or system notes.

Processing Steps (CONTEXT-DRIVEN):
- Interpret document purpose using layout, headers, and symbols.
- Extract visible personal and document-related information.
- Align extracted information with compliance reporting needs.
- Generate a concise, professional summary suitable for enterprise review.

FINAL OUTPUT FORMAT:

Document Context:
Intended Usage:

Document Type:
Issuing Authority:

Observed Details:
- Full Name:
- Date of Birth:
- Gender:

Document References:
- Document Number:
- Issue Date:

Contextual Confidence:
Summary:

Now do same like example with the given image:
Intructions:
Generate the final output using ONLY the provided context and image. Return ONLY the formatted text above. You can also show the other
necessary details which you will find IMPORTANT and  relevant for the template.

'''


# self consistency Prompt
consistency_prompt = '''

'''