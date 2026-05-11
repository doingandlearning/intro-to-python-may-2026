# Python Next Steps: A Resource Map for BBC Learners

Most learners hit a plateau after an introductory course—not because Python gets harder, but because the **next steps feel fuzzy**. Below is a curated map of resources, challenges and project ideas that work for _both_ non-developers and seasoned coders, and that play nicely with the BBC's in-house O'Reilly subscription. Follow the sections in roughly the order given, mixing structured study with bite-size practice and small "automation wins" to keep momentum high.

---

## Structured Learning & Reference

### Real Python – "deep-dive articles + videos"

Free tutorials and paid learning paths cover everything from f-strings to async I/O, with quizzes to check retention ([realpython.com](https://realpython.com))

### Python Morsels – "one exercise per week"

Weekly graded challenges (novice → advanced) plus screencasts; ideal for habit building without overwhelm ([pythonmorsels.com](https://www.pythonmorsels.com/exercises/))

Code: 9B92Y7R3XYAD - 60 free days!

### O'Reilly Learning Platform

Use the corporate subscription to stream **interactive** Python labs and classic books such as _Learning Python_ and _Fluent Python_; the platform's "Interactive Learning" area lets you run code in-browser.

Python for Data Analysis, 2nd Edition by Wes McKinney.

### Recommended Books

| Goal               | Title (O'Reilly or CC-licence)                        | Why it helps                                                     |
| ------------------ | ----------------------------------------------------- | ---------------------------------------------------------------- |
| Solid fundamentals | _Learning Python_ (Mark Lutz)                         | Deep coverage of core language                                   |
| Practical wins     | _Automate the Boring Stuff with Python_ (Al Sweigart) | Project-based automation ideas — also free online at [automatetheboringstuff.com](https://automatetheboringstuff.com) |

_(Both are included in O'Reilly.)_

---

## Practice & Daily Challenges

| Format                      | Platform                                                                                                       | Why try it?                                                                   |
| --------------------------- | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| "25-day December puzzle"    | **Advent of Code**                                                                                             | Fresh problem each day; great pair-programming fodder                         |
| Guided TDD drills           | **Exercism Python track** – 140+ exercises with mentor feedback ([exercism.org](https://exercism.org/tracks/python)) |                                                                               |
| Real-world bite-sized katas | **PyBites / CodeChallenge.es** – emphasises idiomatic code ([codechalleng.es](https://codechalleng.es))        |                                                                               |
| Beginner-friendly puzzles   | **Codewars** – gentler on-ramp than LeetCode; good for building confidence with kata-style problems             |                                                                               |
| Gamified challenges         | **CheckIO** – browser-based challenges presented as a game; lower-stakes and more approachable than most puzzle sites ([checkio.org](https://checkio.org)) |                              |
| Data-centric notebooks      | **Kaggle Learn "Python" micro-courses** – interactive, no setup needed ([kaggle.com](https://www.kaggle.com/learn/python)) |                                                                |
| Long-form habit builder     | **100 Days of Python** (Replit/Udemy/TalkPython variants) – build something daily for ~3 months                |                                                                               |
| Rebuild real tools from scratch | **Codecrafters** – implement Redis, Git, an HTTP server, and more in Python; excellent for experienced devs who want genuine depth ([codecrafters.io](https://codecrafters.io)) | |
| Interview-style puzzles     | **LeetCode** – best suited to developers actively preparing for technical interviews; the difficulty curve is steep and problems skew heavily towards algorithms, so not recommended as general Python practice |  |

Mix one "evergreen" track (e.g. Exercism) with a seasonal burst (Advent of Code) to keep practice varied. If you are newer to coding, start with CheckIO or Codewars before attempting LeetCode.

---

## Projects & Applied Learning

1. **Personal Automation** – re-implement _Automate the Boring Stuff_ scripts with your own BBC-adjacent tasks: bulk-rename files, scrape schedules, auto-format subtitles
2. **Data Snack-Size Projects**

   - Small dashboard or report built from lists and CSV data like the class labs.
   - Simple ETL: pull open data CSV → clean with pandas → push to SQLite.

3. **API Mash-ups** – build a CLI or Streamlit mini-app that hits the News API or the BBC Developer Portal for programme metadata.
4. **Kaggle Mini-Comp** – choose a beginner competition (Titanic, House Prices) to practise pandas, plotting and model baselines.
5. **"One-Module" Libraries** – publish a tiny package (e.g. `bbc-titlecase`) to PyPI; great real-world exposure to packaging and testing.

---

## Community & Support

| Community                   | Value                                                                            |
| --------------------------- | -------------------------------------------------------------------------------- |
| **Python Discord**          | Live help channels, monthly code jams                                            |
| **r/learnpython** on Reddit | Peer Q&A, book/course reviews                                                    |
| Real Python & PyBites Slack | Topic-specific chat and office-hours                                             |
| O'Reilly live events        | Author Q&A, "Superstream" one-day conferences                                    |

Joining one or two communities ensures you have humans in the loop when docs aren't enough.

---

## Suggested Path (Developers vs Non-Developers)

| Profile                  | Next 4 Weeks                                               | After 4 Weeks                                                  |
| ------------------------ | ---------------------------------------------------------- | -------------------------------------------------------------- |
| **Data-curious non-dev** | Real Python "Beginner Data" path + Automate chapters 1–6   | Kaggle Learn ➜ first mini project                              |
| **Junior dev**           | Python Morsels weekly + Exercism or CheckIO                | Advent of Code or PyBites kata streak                          |
| **Experienced dev**      | O'Reilly _Fluent Python_ chapters + Codecrafters           | Contribute mentor notes on Exercism; release a small PyPI tool; LeetCode if interview prep is relevant |

---

### Final Tip

Treat learning as **cycling gears**: alternate focused reading (low gear) with real-world friction (high gear). These resources give you the gears—schedule the ride.