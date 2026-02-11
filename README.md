# JB1 Zoomies

A simple Sphinx extension to integrate [Viewer.js](https://github.com/fengyuanchen/viewerjs) for image zooming in Jupyter Books and Sphinx documentation.

## Features

- **Pinch & Zoom:** Smooth, mobile-friendly zooming for all your images.
- **Theme Integrated:** Automatically adapts to light and dark modes, using your theme's native colors.
- **Smart Captions:** Automatically pulls captions from `<figure>` elements to display them in the viewer.
- **Best-Fit Logic:** Intelligently scales images to fit your viewport (configurable).
- **Dark Mode Optimization:** Option to automatically invert image colors in dark mode—perfect for scientific plots with white backgrounds.
- **Customizable Toolbar:** Choose exactly which tools (zoom, rotate, reset) are available to your readers.

## Installation

```bash
pip install jb1-zoomies
```

Or from source:

```bash
pip install .
```

## Usage

### Jupyter Book

Add the extension to your `_config.yml`:

```yaml
sphinx:
  extra_extensions:
    - jb1_zoomies
```

### Sphinx

Add the extension to your `conf.py`:

```python
extensions = [
    # ...
    'jb1_zoomies',
]
```

## Configuration

JB1 Zoomies works out-of-the-box with PyData-based themes (like the Jupyter Book default), but you can fully customize it in your `_config.yml` (Jupyter Book) or `conf.py` (Sphinx).

### Options

| Option | Default | Description |
| --- | --- | --- |
| `zoomies_selector` | `".bd-article img"` | CSS selector for images that should be zoomable. |
| `zoomies_best_fit` | `70` | Initial zoom level as a % of the viewport (1-100). |
| `zoomies_toolbar` | `["zoomIn", ...]` | Tools to show. Options: `zoomIn`, `zoomOut`, `oneToOne`, `reset`, `prev`, `play`, `next`, `rotateLeft`, `rotateRight`, `flipHorizontal`, `flipVertical`. |
| `zoomies_invert_colors` | `true` | Inverts image colors in dark mode. Useful for charts with white backgrounds. |
| `zoomies_bg_apply_to_img` | `true` | If true, adds a background/padding directly to the image. If false, colors the entire backdrop. |
| `zoomies_bg_color_light` | `"rgba(255, 255, 255, 0.95)"` | Viewer background color in light mode. |
| `zoomies_bg_color_dark` | `"#333"` | Viewer background color in dark mode. |
| `zoomies_caption_color_light`| `"var(--pst-color-text-base)"` | Caption text color in light mode. |
| `zoomies_caption_color_dark` | `"var(--pst-color-text-base)"` | Caption text color in dark mode. |
| `zoomies_cdn_css` | `"...viewer.min.css"` | URL for the Viewer.js CSS file. |
| `zoomies_cdn_js` | `"...viewer.min.js"` | URL for the Viewer.js JS file. |

### Example `_config.yml` (Jupyter Book)

```yaml
sphinx:
  config:
    zoomies_selector: ".bd-article img, .my-custom-image-class"
    zoomies_best_fit: 85
    zoomies_toolbar: ["zoomIn", "zoomOut", "reset", "rotateRight"]
    zoomies_invert_colors: false  # Disable if your images are already dark-mode friendly
```

### Example `conf.py` (Sphinx)

```python
zoomies_selector = ".bd-article img"
zoomies_best_fit = 80
zoomies_invert_colors = True
```
