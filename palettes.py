palette_options= {}
feifan_palette = {
       "bg": (241, 255, 231),
       "primary": (209, 102, 102),
       "secondary": (44, 68, 81),
       "accent": (182, 198, 73)
   }
# Color palette for person 2 here
riley_palette = {
      "bg": (33, 0, 16),
      "primary": (107, 34, 70),
      "secondary": (211, 128, 217),
      "accent": (167, 243, 250)
      #199, 255, 248
  }
# Add this line at the end
palette_options["riley_palette"] = riley_palette
# Color palette for person 3 here
melody_palette = {
   "bg": (33, 89, 179),
   "primary": (78, 125, 202),
   "secondary": (142, 173, 228),
   "accent": (242, 242, 236)
}
# Add this line at the end
palette_options["melody_palette"] = melody_palette
palette_options = {
   "feifan": feifan_palette,
   "riley": riley_palette,
   "melody": melody_palette,
}
palette_names = list(palette_options.keys()) + ["random"]
# Run this cell to look at all the names.


palette_names = list(palette_options)
palette_names.append("random")
print(f"The available color palettes are: {palette_names}")
