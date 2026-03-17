# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

- One: (Developer Debug Info) The app does not display the recent guesses immediately after submission.
- Two: (Developer Debug Info) Clicking the new game button does not reset the guess history as expected.
- Three: When the user presses the enter key to submit a guess, the app does not
  store the value or prompt the user.
- Four: The app shows opposite prompt for each incorrect guest, prompting "Go Higher" for guesses below the target and vice versa.
- Five: The number ranges for the difficulties are incorrect for normal and hard modes.
- Six: Normal mode displays range 1 to 20 but can have a target outside of that range.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

- Copilot suggested I modified the Normal difficulty range for the get_range_for_difficulty function from 1 to 100 to 1 to 20, which was wrong (should intuitively be 1 to 50). I made the correct modification myself afterward.
- When examining the check_guess function for more bugs, Copilot noted the intentional string convertion and int to string comparison that can cause type mismatches between guess and secret. I found this to be a real bug and refactored appy.py and logic_utils.py with Copilot to fix the issue.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

- I decided a bug was really fixed after running tests using pytest and also rerunning the app after each fix.
- One test I ran using pytest was test_guess_9_vs_secret_10 which would have failed under the old string-based comparison, incorrectly returning "Too High" due to lexicographical ordering.
- Copilot helped me design and understand the test_guess_9_vs_secret_10 test and similar tests by explaining the reasoning behind the "intentional glitch" of the string conversion of secret and comparison with int guess.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
