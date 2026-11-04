# Feifan-Melody-Riley_CreativeCodingGP

**Created by:** Feifan Ling, Melody Sun, Riley Arico

**Course:** Creative Coding, Pratt Institute

**Semester:** Fall 2026

## About the Project

For this poster generator, we made our own seperate palettes and tiles, and then collaborated by bringing them together in this interactive project. Users can pick between each of our palettes, while the tiles are randomly picked from either of our tile libraries. Tiles change orientation and apperance based on their coordinates in the grid, in which it's size is given by the user as well.

## The Interface

**What can the users modify?**
- width and height of the canvas
- colors (pick from existing palettes or randomly generate one)

## Meet the Designers

- **Feifan Ling:** My tiles include semicircles that have a rainbow effect, border lines, and a flower mandala design. For this project, I contributed to debugging the code and making sure that it ran smoothly.
- **Melody Sun:** My tiles design incorporates flowers, lines, and diamonds. For this project, I contributed to creating the user input code, formatting the final printed canvas (the color palettes, text, alignment, size, etc), and uploading files to the GitHub
- **Riley Arico:** My tiles were inspired by halloween with the moody color palette and spiderwebs. I contributed to this project by making sure the rotation and placement of tiles were accurate given the size of the grid.

## Try it yourself

Copy this code into a Colab Notebook.

```python
!git clone https://github.com/bsun07/Feifan-Melody-Riley_CreativeCodingGP.git
%cd Feifan-Melody-Riley_CreativeCodingGP
!pip install -r requirements.txt
from project import generate_poster
generate_poster()
```

Or click below to open an example notebook in Google Colab and generate your own poster!

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1EggqLCk5d4GBNBFRn2R-0YavMqt_SYtL?usp=sharing)

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
