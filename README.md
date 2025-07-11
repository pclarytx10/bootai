# BootAI: A Custom Agent for Coding Tasks
This is a small project from the boot.dev Back End Developer coursework focusing on functional programming techniques.  

We're building a toy version of Claude Code using Google's free Gemini API! As long as you have an LLM at your disposal, its actually surprisingly simple to build a (somewhat) effective custom agent.

**What Does the Agent Do?**

The program we're building is a CLI tool that:

1. Accepts a coding task (e.g., "strings aren't splitting in my app, pweeze fix")
1. Chooses from a set of predefined functions to work on the task, for example:
	1. Scan the files in a directory
	1. Read a file's contents
	1. Overwrite a file's contents
	1. Execute the python interpreter on a file
	1. Repeats step 2 until the task is complete (or it fails miserably, which is possible)