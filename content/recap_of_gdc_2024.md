Title: Topical Recap of GDC Week
Date: 2024-03-24 21:25
Tags: startup, ai, games
Author: Ramon Dario Iglesias
Summary: Busy week for Clementine!

Last week I presented at Speedrun's Demo Day! And that was just the beginning of a *very* busy week of GDC. 

I will leave the details of the program for a future post (technically this week is still part of the program). Instead, I want to highlight the main topics I heard as they relate to AIxGames. Here comes a laundry list!

**Agents.**
Lots of interest in game agents! From what I saw, the most advanced systems combine LLMs with a suite of more traditional techniques. Some (like us!), use a combination of LLMs and traditional action planners found in games and in robotics, e.g. [GOAP](https://medium.com/@vedantchaudhari/goal-oriented-action-planning-34035ed40d0b). Others are combining RL and LLM-based, skill learning approaches in the style of [Voyager](https://arxiv.org/pdf/2305.16291.pdf) but with added tricks. The more advanced systems are relying on GPT-3.5 rather than 4, and some are using finetunes. It may be the case that for real-time action planning, the quality of the model is enough and what matters more is speed in cost.

On cost, it is clear that the marginal cost remains an issue. All of the people I talked to seem to be in the very early stages and have rough ideas on how to monetize and how to reduce their costs, but making the systems work like they want to is still the number one priority.

On what to do with them, there is a wide variety: [Minecraft bots](https://www.youtube.com/watch?v=gvkEHrLLI4k), [quest-centric NPCs](https://twitter.com/FirstDayGG/status/1764483275027095840), [Sims-like games](https://twitter.com/peggy_wang/status/1767656498212356597), [text games](https://www.thepromenade.ai/), and even [for Q&A](https://www.agentic.ai/).


**Asset Generation.**
It's clear this is the most frequent use case for Generative AI. Plenty of companies trying to produce ready-made assets, and a handful that are doing the clever part of bridging between the output of a model and the ready-made asset. 

It is interesting to see two approaches for motion though. [HEAT](https://heat.tech/) on the one hand is a motion marketplace. The idea is that you can find any any motion in the marketplace, download it, and apply it to your characters. [Latent Technologies](https://www.latent-technology.com/) on the other hand is building motion from first principles: given a task and a physics rule set, they can provide the motion that achieves the task. I am unsure how big of a market the latter is, but it does open the door for more physics-based mechanics. For example, Skypunk's [Brain Cell](https://store.steampowered.com/app/851720/Brain_Cell/) makes custom physics the main mechanic, and it looks awesome!

I think there is a unique opportunity for high quality anime-style, game-ready 2d sprites or even _glTF_ scenes. First because how popular the genre is, second because of waifus, and third because high-quality 2d is within grasp. [Avatech](https://www.avatech.ai/) has a strong prototype: a workflow that delivers a programmable animation! But [Parhelion](https://parhelion.gg/), who is building Sushi-grade anime games, is the right benchmark for what is useful. They have an army of artists, so anything that deviates their workflows from artists to GPUs is a strong endorsement of the technology. That would be my target client if I was in the space.

Then, there is [videogame.ai](https://videogame.ai/) that is re-structuring how game development is done to take the most advantage of generative AI at the development stage.

I missed Tencent's presentation, but it sounds like it was the mother of all Gen AI asset generation toolkits. 

**Structural Storytelling.**
A very common early learning in anyone's LLM adventure is that LLMs really need an external structure to shine. This appeared multiple times during GDC. Folks from [Bonfire](https://www.trybonfire.ai/), [the Promenade](https://www.thepromenade.ai/), and [Hidden Door](https://www.hiddendoor.co/) all echoed this sentiment.

Hidden Door and the Promenade have opposite but equally interesting approaches. Hidden Door uses existing IP to seed the storytelling aspect, thus making it easy for players to buy in. Promenade instead is generating all its own IP, in fact that's the stated goal!, and using a gamified system to hook people in. 

On the one hand, it makes me think that there is an opportunity for finding the right structural framework for LLMs. Perhaps we could combine something like automated planning and storytelling! 

On the other hand, it seems like games already do this. Tynan Sylvester [sees certain games as story engines](https://www.gdcvault.com/play/1024232/-RimWorld-Contrarian-Ridiculous-and) because they let your imagination color in between the lines. But perhaps, just like some people lack the creativity to play a text game, others may not be able to enjoy story engine games because they lack the ability to tell themselves stories, even when aided by a game. LLMs could broaden the audience of story engine games. 

**Control vs Emergence.**
A salient point in Generative AI, specially as it relates to agents, is how much control is ceded to the model. This is important because game designers have an experience in mind, and tuning a system without knobs is *hard*. At the same time, that is part of the magic, to see mechanics and outcomes that are unexpected even by the designer. 

An example of well controlled emergence, is how Rimworld is built: lots of small, well understood, elegant mechanics that when they interact they produce a rich and varied experience. But this requires _a lot_ of work! 

One argument is that perhaps we want at least to have a way to balance how much direct control and how much emergence we want in the game. But that requires us to fully build and understand these systems, and then we will be able to make them more predictable or less. For us to navigate the Pareto frontier, we first have to get to it!

I keep thinking of how the Stable Diffusion has this rich ecosystem with closer to proper control systems for art creation: [ControlNet](https://github.com/lllyasviel/ControlNet) and [ComfyUI](https://github.com/comfyanonymous/ComfyUI) are clear examples. This was only possible because of the open source nature of the model. LLMs have seen some success with LoRAs, LangChain, and DSPy, but not nearly enough. In part because the best models are closed and in part because the use cases are much more varied. 

If we are going to see control knobs for LLM workflows, it will be for specific use cases and it will require open source models.

**Some companies to follow in the space**:

- Agents: [Agentic](https://www.agentic.ai/), [Altera](https://twitter.com/Altera_AL), [Clementine](https://twitter.com/ClementineInc) (obviously), [Ego](https://twitter.com/ego_ai_), [First Day Entertainment](https://twitter.com/FirstDayGG), [Incite](https://incite.dev/), [Jam and Tea](https://twitter.com/JamandTeaTime), [Open Souls](https://www.socialagi.dev/), [Pocket Frens](https://www.pocketfrens.xyz/), [Proxima](https://twitter.com/studioproxima?lang=en), [the Simulation](https://www.thesimulation.ai/)
- Content generation: [Avatech](https://www.avatech.ai/), [glyf](https://glyf.space/), [HEAT](https://heat.tech/), [Hedra](https://www.hedra.com/), [Latent Technologies](https://www.latent-technology.com/), [OptimizerAI](https://www.optimizerai.xyz/), Tractive, [videogame.ai](https://videogame.ai/)
- Text-based games: [AI Dungeon](https://aidungeon.com/), [Bonfire](https://www.trybonfire.ai/), [Hidden Door](https://www.hiddendoor.co/), [the Promenade](https://www.thepromenade.ai/)