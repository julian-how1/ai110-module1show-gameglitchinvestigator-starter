# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  #1 Hints give the opposite response that it should
  #2 Guess history doesn't update until you submit another guess, causing attempts to say you have 1 more chance when you lose
  #3 History doesn't resest when you hit new game, preventing you from making new guesses

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|70| | | | "Go lower"           "Go higher"          none
|"New Game" (after losing) | | | | "New game started"   "Game over Start a new game to try again"  History didn't reset
|20 | | | |  "Go higher"        "Go lower"         Expected history to update but it was first guess and nothing was added

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
# The only AI tool that I used on this project was Claude.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
# An example of a suggestion that Claude was that was correct was that for the hint returning the wrong prompt (ex: saying higher when you should go lower) was due to the logic being backwards. It gave me the exact lines that was causing the error so that I could look at it myself before it made any changes, and I was able to verify the result by getting Claude to add a pytest, and then running the game myself to make sure everything was moving smoothly. I also asked it to point me to the exact lines that changes were made on so that I could look at the code myself.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
# I feel like the biggest thing that Claude was doing wrong was my instructions when I asked it to make a pytest. The first time I can admit I worded my prompt wrong, asking it to make test to cover edge cases and anything else it sees fit (can't remember my exact wording) but on my next go I specifically asked for one test and it kept trying to add hundreds of lines for some reason. I used the "tell Claude what to do instead" option, and corrected it to only give one test when this happened, and if it did it again I straight up just hit no to end the task.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
# The first thing I did to decide whether or not a bug was really fixed was make sure that a pytest was created for the bug and that the code passed all the previous test as well once it was added. Next I reran the streamlit and did everything that I could to try to get the error to show up just incase there was some edge case missing.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
# One test ran with pytest that surprised me was the "compare as number" test that Claude made for me. When I orginally explained that the hint that was being provided was backwards it gave 2 spots that was causing the error and one of the spots was something that I never realized. Part of the reason the hint was coming in backwards was because the guess wasn't being registerd as an int properly but instead as a string, this test showed me that there was incorrect logic going on that I wasn't aware of at first.
- Did AI help you design or understand any tests? How?
# Yes, Claude did help me design the test. After I prompted it to make a certain change for one of the bugs I identified I would ask it to create a pytest as I explained in one of the earlier questions. And like I said earlier the problem was that it kept trying to make too many test for the one bug, so I would have to go in and reprompt it to make way less test that were also easier to read and understand.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
# Streamlit reruns makes it so that the python script is completely reran from top to bottom each time there is an interaction with the app. Session state is something used to store things between these reruns incase there is something that you need it to remember.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
# One habit that I want to reuse from this project for the future is going to be labeling where bugs are before I decide to go in and fix it just to keep everything organized. I feel like this allows me to go around and map out how I want to fix everything, instead of just finding one thing fixing it and then looking for the next, instead I can kind of do everything in 2 passes. Next time I work with AI on a coding task I want to be a lot more specific with how I prompt it to do things, I realized when working on this project that my prompts weren't strict enough, for example my biggest problem was it trying to make too many test because of how I prompted it to do so. This project made me less worried about AI generated code making it almost impossible for me to find a job in the future, the reason being is I now understand that this isn't something that everyone can do, and my knowledge of fundementals allows me to identify when something is going wrong based on a prompt, and I'm not just blindly following the AI.

# (Disclaimer for my commits) I was just working through the assignment one tab at a time, so I didn't know I needed to make 3 commits for the grade since it wasn't stated until the very end of the last tab. I'm writting commits for my 3 changes seperately, but have to type this since there weren't any changes.

# History commit