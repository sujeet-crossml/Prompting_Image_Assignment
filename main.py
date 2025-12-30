from utils import text_generation, self_consistency
from prompt import *

# Driver code
if __name__ == "__main__":
    # selecting prompts
    prompt_selection = consistency_prompt

    # if prompt is consistency prompt
    if prompt_selection == consistency_prompt:
        consistency_output = self_consistency(consistency_prompt, image)
        for lst in consistency_output:
            print(f'Output:\n{lst}\n\n')
    else:
        # for other prompts
        print(text_generation(prompt_selection, image))
