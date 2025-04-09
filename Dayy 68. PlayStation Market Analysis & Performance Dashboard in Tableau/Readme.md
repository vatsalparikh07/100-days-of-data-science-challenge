# Day 68. 100 Days of Data Science Challenge - 04/09/2025

## 🎮 PlayStation Generational Market Analysis & Performance Dashboard [(Tableau Link)](https://public.tableau.com/app/profile/vatsalparikh/viz/playstation-dashboard/PlaystationDeepdive)

![image](https://github.com/user-attachments/assets/e7d8dc4c-49dd-4536-8952-1c8058c2888d)

Ever argue about which PlayStation was *really* the best? Or wonder why certain games blew up in Japan but not the US? 🤔 Me too! That's why I created this interactive Tableau dashboard. We're digging into the **massive Video Game Sales dataset** (think **13,000+ PlayStation titles!**) to visually explore the rise and evolution of Sony's iconic consoles from the OG PlayStation all the way through the PS4 era (plus a nod to the PSP).

This isn't just charts and numbers; it's a time machine for gaming history, showing how sales ebbed and flowed, which genres ruled the roost, and who the biggest players were on the publishing scene.

**✨ Ready to explore? Dive into the LIVE Interactive Dashboard! ✨**
**[➡️ Click Here to Launch on Tableau Public](https://public.tableau.com/app/profile/vatsalparikh/viz/playstation-dashboard/PlaystationDeepdive)**

---

## 🗺️ What Cool Stuff Can You Uncover?

Forget static reports. This dashboard lets *you* be the analyst. Here's what you can investigate:

*   **👑 Console Wars (Sibling Rivalry Edition):** See the PS1, PS2, PS3, and PS4 duke it out in sales figures. Just how dominant *was* the PS2? The data doesn't lie!
*   **🌍 Global Domination Tour:** Follow the money! See how sales stacked up across North America, Europe, Japan, and the 'Rest of the World'. Spot the regional favorites!
*   **📈 Ride the Release Wave:** Watch the timeline unfold. See when each console peaked and how their lifecycles overlapped.
*   **👾 Genre Showdown:** Action? RPG? Sports? Racing? Use the treemap (and filters!) to see which genres defined each generation and where the big money was.
*   **🏆 Hall of Fame:** Instantly identify the absolute best-selling games that made PlayStation history. Any surprises?
*   **🏢 Publisher Power Plays:** Track the market share giants like Sony, EA, Activision, Take-Two, Ubisoft, and more. Who ruled the playground in each era?

---

## 💡 Killer Insights Hiding in the Data

After spending time with this data, some seriously cool patterns jump out:

1.  **The PS2 Was a MONSTER:** Seriously, look at the "Sales By Platform" chart. The PS2's global sales performance dwarfs the others in this dataset. It wasn't just a console; it was a phenomenon, driven by a massive library and perfect market timing. 🤯
2.  **Action & Sports = Universal Languages:** These genres are the bread and butter, consistently topping the sales charts across most regions and generations. Reliable crowd-pleasers!
3.  **Japan's Love Affair with RPGs:** The regional data *screams* this. Especially during the PS1/PS2 golden age, RPGs were disproportionately huge in Japan compared to the West. 🇯🇵❤️
4.  **Shooters Rise with Hardware:** Notice the **Shooter** genre gaining serious ground on the PS3 and PS4? Better hardware, online play... the evolution is clear in the sales data.
5.  **It's a Blockbuster World:** Just like Hollywood, a tiny fraction of mega-hit games (your GTAs, Call of Dutys, Final Fantasys) drive a *massive* percentage of the total sales. High risk, high reward! 💰
6.  **Publisher Musical Chairs:** Watching the publisher treemap change when you filter by year or console is like seeing history unfold – Sony battling EA, Activision's rise, the fall of others like THQ... it's all there.

---

## 🛠️ Behind the Magic Curtain: How It Was Made

No wizards here, just data and smart tools:

*   **The Brain:** **Tableau Public** is where all the visualization magic happens. It lets you slice, dice, and interact with the data visually.
*   **The Raw Material:** The project uses the public "Video Game Sales" dataset (`vgsales.csv` attached) [1]. It's a treasure trove of gaming history (though mostly physical sales, keep that in mind!).
*   **The Prep Work (Python, Pandas):** Before Tableau could shine, the raw CSV needed some TLC. This meant:
    *   **Filtering:** Isolating just the PlayStation platforms (PS, PS2, PS3, PS4, PSP).
    *   **Cleaning:** Tidying up messy Publisher names and making sure Genres were consistent.
    *   **Calculating:** Adding things like Global Sales totals if they weren't perfect.

---

## 🚀 Your Turn! Go Explore!

Don't just take my word for it, jump into the dashboard and try these:

*   **Filter by Genre:** Select "Role-Playing" and watch how the regional sales map changes.
*   **Focus on a Publisher:** Pick "Square Enix" (or SquareSoft for older games) and see their journey.
*   **Isolate a Generation:** Use the platform filter (or click on the platform charts) to focus just on the PS3, for example. See its top games and genres.
*   **Hover Everywhere:** Tooltips pop up with specific numbers and details – use them!

---

This dashboard is more than just homework for Day 68 of my #100DaysOfDataScience challenge; it's a dynamic look at the history of a gaming giant. Hope you enjoy exploring it as much as I enjoyed building it!

*Created by Vatsal Parikh*
