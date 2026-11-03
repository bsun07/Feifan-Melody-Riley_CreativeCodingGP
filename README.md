# Feifan-Melody-Riley_CreativeCodingGP

**Created by:** Feifan, Melody Sun, Riley
**Course:** Creative Coding, Pratt Institute  
**Semester:** Fall 2026

## About the Project

[Write a short description of your project. What was the idea behind your poster generator? What visual qualities or design ideas inspired it? How does the program combine everyone's individual tile designs into a unified composition?]

## The Interface

**What can the users modify?**
- width and height of the canvas
- colors (pick from existing palettes or randomly generate one)

## Meet the Designers

- **Feifan:** [Brief description of their tile designs or contribution.]
- **Melody Sun:** My tiles design incorporates flowers, lines, and diamonds. For this project, I contributed to creating the user input code, formatting the final printed canvas (the color palettes, text, alignment, size, etc), and uploading files to the GitHub
- **Riley:** [Brief description of their tile designs or contribution.]

## Try it yourself

Copy this code into a Colab Notebook.

```python
!git clone https://github.com/bsun07/Feifan-Melody-Riley_CreativeCodingGP
!pip install -r requirements.txt
from project import generate_poster
generate_poster()
```

Or click below to open an example notebook in Google Colab and generate your own poster!

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1iho7fD12AxIXqKzoNI5bAI-NxnKauBgz?usp=sharing)

### How to Use

1. Open the notebook in Google Colab.
2. Run the setup cells to download the project code and install the required libraries.
3. Run the cell that calls the function and prompts the user to choose a title, grid dimensions, and color palette.
4. Your own poster will be saved as poster.svg!

## Files

- `project.py` – Main poster-generation program.
- `tilecollection.py` – Collection of custom tile-drawing functions.
- `palette.py` – Available color palettes.
- `requirements.txt` – Required Python libraries.
- `example_poster.svg` – Scalable vector version of an example final poster image.
