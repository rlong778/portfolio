# Ralph Long IV — ePortfolio

Architect's-notebook style portfolio built with Python + Streamlit.

## Run it on your computer (optional)

```
pip install streamlit
streamlit run streamlit_app.py
```

## Publish it (required for the assignment)

1. **GitHub:** go to github.com → **New repository** → name it `portfolio` → set it to **Public** → Create.
2. On the new repo page click **"uploading an existing file"**, then drag in **everything inside this folder**
   (including the `.streamlit`, `assets`, `pages`, and `static` folders) → **Commit changes**.
   - Hidden folder tip: if `.streamlit` doesn't show up when you drag, create the file on GitHub instead:
     **Add file → Create new file**, name it `.streamlit/config.toml`, and paste in the contents.
3. **Deploy:** go to **share.streamlit.io** → sign in with GitHub → **Create app** → pick the `portfolio` repo,
   branch `main`, main file `streamlit_app.py`. Under "App URL" you can choose a name like `ralphlongiv`. → **Deploy**.
4. **Test:** open the link in an incognito window AND on your phone. Then submit it on Canvas.

## Adding your own photos

Drop these into `assets/` (exact names) and they appear automatically:

| File | Where it shows up |
|---|---|
| `headshot.jpg` | Home page, next to the welcome |
| `about.jpg` | About Me page |
| `boxoffice.png` | Screenshot under the Box Office project |
| `discovery.jpg` | Discovery Project → The Outcome (add before the Showcase!) |

## Adding a new project later

Open `pages/projects.py` and add another `{ ... }` block to the `PROJECTS` list. That's it.

## Regenerating the hand-drawn figures

The figures in `assets/fig_*.png` were drawn with matplotlib using the Architects Daughter font.
