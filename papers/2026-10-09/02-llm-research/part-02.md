# 🧠 大模型相关研究 | 2026年10月09日

> 本类共 **266** 篇论文：已确认 **245** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-266](./part-06.md)

---

### 51. [RippleCP: Measuring Counterfactual Checkpoint Advantage in Coding Agents](https://arxiv.org/abs/2610.09088)

**<font color=#1a73e8>作者：</font>** Mayur Akewar, Ravi Ranjan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent checkpoint systems decide what state is recovery-relevant, how to snapshot it, and whether rollback is admissible. None decides which of the safe boundaries they expose are worth materializing. We formulate this as counterfactual checkpoint advantage, the reduction in future recovery cost obtained by checkpointing a candidate rather than skipping it, and measure it by driving a CP branch and a SKIP branch to the same logical failure and recovering both under matched model, tool, verifier, and stopping conditions. On a frozen pilot of 12 SWE-bench Verified tasks and 106 real recovery branches, checkpointing saves 49.4 s per task, and that figure resolves into two regimes two orders of magnitude apart. The first checkpoint returns 100.0 s on 156.5 s of protected work, a conversion of 0.64; a second one step later returns-1.1 s on 41.8 s, a conversion of -0.03. Recovery is a re-derivation rather than a replay, so preserved work is a poor guide to saved work, and the classical elapsed-work rule misprices the second checkpoint by its full nominal cost. We identify where placement can pay, and set the bar a placement policy must clear.

---


### 52. [GeoNatureAgent (GNA): A Framework and Benchmark for Pre-Production Evaluation of Tool-Using Agents on Geospatial and Environmental Tasks](https://arxiv.org/abs/2610.09112)

**<font color=#1a73e8>作者：</font>** Gabriel Diaz-Ireland, Diego Prieto-Herráez, Mario García Peces 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Before tool-using LLM agents are deployed in environmental and geospatial workflows, teams need evidence that an agent reliably selects the right operations against real APIs. We introduce GeoNatureAgent (GNA), a framework for pre-production evaluation of tool-using agents: a fixed sixteen-tool geospatial interface published as a Model Context Protocol (MCP) server, so the agent under test is the only variable, scored against an identical tool layer, task suite, and deterministic scorer. Its flagship instance is a 103-task benchmark (a 93-task main suite across 18 categories plus a ten-task comparison expansion) evaluated against an open, self-hostable geospatial API serving three environmental indicators across Spain and Portugal. We evaluate nine LLMs under three temperature-1.0 seeds, reporting capability and per-case cost as orthogonal axes. (1) Claude Sonnet 4 achieves the highest capability (61.7% +/- 0.7% on all 103 tasks; 60.8% on the main suite), followed closely by DeepSeek V3.2 (57.9%), while no other model exceeds 53%; (2) the cost-accuracy Pareto frontier is mostly open-weight, with DeepSeek V3.2 offering 93% of Claude's capability at 11.3x lower list-price cost; (3) under strict all-checks scoring the best model sits 24-36 points below the 85-97% reported on general-purpose GIS benchmarks, whereas per-check partial credit for the top four models (86-90%) is comparable, so much of that gap reflects scoring strictness rather than task difficulty alone. The MCP server, evaluation harness, benchmark, and API are publicly available; swapping the tool executors and task suite instantiates an equivalent benchmark for any geospatial domain.

---


### 53. [From Uncertainty to Action: Learning to Steer LLM Agents](https://arxiv.org/abs/2610.09115)

**<font color=#1a73e8>作者：</font>** Hanwen Li, Jinhao Duan, Guanhua Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Steering an LLM agent means deciding whether to correct it, at which step, and with which mechanism. Uncertainty is often used to decide when to correct an agent, but whether it can guide these decisions remains unclear. We steer agent trajectories separately at every non-terminal step with each of four mechanisms and run each continuation to completion. The resulting stepwise outcome table (SOT) holds about 82,000 counterfactual continuations of 1,864 trajectories from three benchmarks and two agents. It shows that uncertainty can identify failing trajectories, but that no single signal reliably locates the step at which steering helps. We therefore propose VoS (Value of Steering), a trajectory-level monitor, offline or online, that learns from SOT the value of steering at each step and decides where to steer by it. A harm-budgeted trigger decides whether to steer, limiting the fraction of successful trajectories that VoS disturbs. VoS improves on unmodified execution in all 12 settings of benchmark, agent, and offline or online use, by 7.8 points on average, and outperforms the strongest of five existing uncertainty-triggered methods in 11, by 2.9 points on average. Ablations show that training on measured outcomes and a tight harm budget are both essential.

---


### 54. [SPLATIFY: Reproduce, Discover, Innovate! From Papers and Ideas to Trainable 3DGS Code](https://arxiv.org/abs/2610.09116)

**<font color=#1a73e8>作者：</font>** Seemandhar Jain, Keshav Gupta, Manmohan Chandraker  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid growth of 3D Gaussian Splatting (3DGS) research demands significant effort to reimplement papers before building on them. We introduce SPLATIFY, a multi-agent framework that converts 3DGS papers into trainable gsplat-based implementations, where generic paper-to-code methods and frontier models fail. SPLATIFY achieves this through five innovations: (1) A context-free grammar for gsplat over a modular method template with extension points for losses, densification, rendering, and optimization, constraining synthesis so generated code satisfies gsplat's architectural invariants by construction. (2) Architectural elements for faithful reproduction: fork-aware citation recovery retrieving component-level code at function-level granularity, Graph-of-Thought synthesis in topological dependency order, RAG-guided in-context example selection from over 20 verified implementations, and visual feedback combining PSNR-guided regeneration, Gaussian-level structural checks, and VLM-driven patching. (3) Knowledge-driven compositional improvement that autonomously finds weaknesses and composes complementary regularizers, losses, and densification strategies to improve upon original results. (4) Interdisciplinary method discovery where agents retrieve physical priors from outside the 3DGS literature and compose them with rendering knowledge to produce methods for previously unaddressed scene types. (5) SPLATIFY-Bench, an evaluation framework across 30 diverse 3DGS papers. On papers without public code, SPLATIFY matches expert implementations while reducing development time from weeks to minutes, and through compositional discovery further improves PSNR by up to 2.4 dB. We additionally demonstrate novel methods for volumetric nebula rendering and other scientific domains, synthesized entirely by SPLATIFY.

---


### 55. [Spatial Induction Heads: In-Context Learning of Multidimensional Cellular Automata](https://arxiv.org/abs/2610.09124)

**<font color=#1a73e8>作者：</font>** Kimia Kazemian, Menghan Xu, John Thickstun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Induction heads provide a mechanistic account of in-context learning in sequential data, but existing theory largely assumes that the context relevant to a prediction forms a contiguous block. In multidimensional data, serialization breaks this assumption by scattering spatial neighbors across distant positions in the token sequence. We study how transformers overcome this routing problem in multidimensional stochastic and deterministic cellular automata, where each trajectory is generated by an unknown local rule and presented as a flattened sequence without an explicit coordinate-based spatial inductive bias. We introduce spatial induction heads, two-layer gather-and-match circuits in which the first layer reconstructs the relevant spatial neighborhood and the second matches the resulting configuration against earlier occurrences. We give two explicit realizations of the gather and show that the positional dimension required for spatial routing depends only on the local neighborhood and spatial dimension, not on grid volume or trajectory horizon. We further construct a matching layer which implements Bayesian counting. The end-to-end circuit can approximate the Bayesian posterior arbitrarily closely for stochastic rules and can predict exactly for deterministic rules. Empirically, trained two-layer transformers generalize to unseen rules in one and two dimensional settings, achieving near-perfect deterministic rollouts and less than 0.005 nats KL from the Bayes-optimal predictor on stochastic rules. Attention patterns and layerwise probes align with the predicted gather-and-match computation, providing mechanistic evidence for spatial induction in trained transformers.

---


### 56. [Breaking the Space Barrier and its Application to Language Model Inference](https://arxiv.org/abs/2610.09139)

**<font color=#1a73e8>作者：</font>** Arip Asadulaev  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models are more and more often asked for structured output: JSON that follows a schema, or a tool call with typed arguments. A small machine, an automaton, enforces the format by forbidding the tokens that would break it. We observe that this machine has a rare property: from any of its states, each token leads along exactly one path. Graphs in which only a few paths join any two points are a classical object of complexity theory, and our theoretical result settles an open question about them: one can decide whether such a graph connects two points while verifying that it really has few paths, with very little memory. Precisely, the problem lies in the classes ReachUL, LOGDCFL, C=L and SC2, and needs only O(log2 n/ log log n) space, below the classical O(log2 n) of Savitch's theorem. The constructions behind the proofs become an inference engine: text the format forces is written without running the model, the mask is recomputed on the GPU without any table, recursive formats use a small stack, every output stays valid under a token limit, and independent fields are decoded in parallel and verified. On one 16 GB Apple M2 Pro with Qwen3.5-2B and 4B, against MLX with llguidance, the standard setup for this hardware, schema-constrained extraction finishes 1.2- 1.3x sooner with the same answers, a grammar costs 3 MB instead of up to 1.5 GB, one server holds sixteen grammars where tables run out of memory, and sixteen tool-calling agents finish 2.5x sooner.

---


### 57. [DIVA: Dual-Space Intent-Aware Visual Attenuation for Vision-Language-Action Policies](https://arxiv.org/abs/2610.09144)

**<font color=#1a73e8>作者：</font>** Kaixi Feng, Guoheng Sun, Ziyao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) policies typically feed dense visual patch tokens into a language-action backbone, preserving scene context but offering no explicit mechanism to regulate how strongly different visual tokens influence policy computation. We introduce DIVA, a Dual-Space Intent-Aware Visual Attenuation module with an anchor-then-attenuate design. DIVA combines high-level task intent with low-level visual evidence to estimate patch-wise relevance anchors, then applies them in two complementary spaces: it reweights projected visual tokens before backbone entry and persistently attenuates low-relevance visual states within the backbone. DIVA preserves the full visual token sequence and requires no external grounding supervision. On LIBERO, DIVA improves OpenVLA-OFT from 96.6% to 98.0% average success and raises its zero-shot LIBERO-Plus score from 69.6 to 72.6. Real-world experiments further show consistent gains under task-irrelevant visual perturbations, supporting the robustness of intent-aware visual attenuation beyond simulation.

---


### 58. [Noise Your Prompt: Noising Conditioning Tokens in Continuous Diffusion Language Models](https://arxiv.org/abs/2610.09145)

**<font color=#1a73e8>作者：</font>** Justin Jung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We revisit a standard accepted practice in the continuous diffusion language model
literature of fixing conditioning prompt tokens clean during training.
We make a very simple modification: also noise the conditioning prompt tokens during training.
We demonstrate that under this modified training objective, we achieve better generalization
in combinatorial reasoning tasks such as Sudoku and N-Queens, with the largest gains on harder variants
($3.73\% \to 24.65\%$ solve rate on Sudoku Hard), and increased diversity of generated solutions ($50.60\% \to 73.79\%$ coverage on
10x10 N-Queens). We also show measurable improvements to natural language generation quality
in modest dataset regimes with Gigaword summarization, but notably demonstrate that gains do not
transfer to all natural language tasks (e.g open ended dialogue generation).
Our method is a single line change to the training objective, requires no additional inference costs by default,
and provides the flexibility of classifier-free guidance inspired guided sampling. Our
\href{this https URL} {code} is publicly available.

---


### 59. [Frozen Models, Evolving Expertise: Model-Agnostic Learning from Deployment Experience for Multimodal Medical AI](https://arxiv.org/abs/2610.09146)

**<font color=#1a73e8>作者：</font>** Yexiao He, Yucheng Tang, Pengfei Guo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) and vision-language models (VLMs) are usually frozen after deployment, so they do not learn from the cases they solve. This is especially concerning in medicine, where new clinical evidence, updated guidelines, and new therapies can change established practice. Fine-tuning can update the model, but it requires access to model weights and additional training. Parameter-free methods avoid training, but they may overfit a fixed validation set, lack reliable domain knowledge, or lose visual details by saving experience only as text. To address these limitations, we present a model-agnostic framework that allows frozen LLMs and VLMs to learn from deployment experience through three forms of external expertise: a Skill that guides reasoning and tool use, a Knowledge Memory that stores reliable facts supported by earlier cases or trusted external evidence, and a Multimodal Knowledge Base that keeps visual examples and guides the model to relate each retrieved case to the current image. Instead of relying on a fixed validation set, a validation strategy keeps an update only if it helps on new cases without degrading performance on earlier ones. Across six benchmarks covering clinical diagnosis, clinical workflows, medical reasoning, and medical and non-medical visual reasoning, and with four open-weight and closed-source base models, our framework improves performance during online deployment by up to 34.2% over the base model on medical tasks, generalizes to unseen cases, transfers to other models without further optimization, and works in non-medical domains.

---


### 60. [sk-bench: A Native-First Benchmark for Evaluating Large Language Models in Slovak](https://arxiv.org/abs/2610.09152)

**<font color=#1a73e8>作者：</font>** Marek Šuppa, Ivan Vykopal, Andrej Ridzik 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual LLM benchmarks omit Slovak, a morphologically rich West Slavic language of five million speakers, or cover it only by machine translation. We present sk-bench, a native-first Slovak benchmark with 30 datasets (33 scored task variants) across ten skill categories. Eleven resources are introduced or first packaged for generative-LLM evaluation, including IFEval-SK with Slovak-adapted instruction checkers and native Chiby/SKJ1 resources for Slovak grammar and morphology. We evaluate 55 open- and closed-weights models under one harness. The best open model trails proprietary APIs by 12.6 points. Model rankings are similar for native and translated closed-form data ($\rho\geq0.98$), though translation separates the strongest models less well. By contrast, human-authored and LLM-generated QA questions rank models differently ($\rho=0.72$). For Qwen3-14B, continued Slovak pretraining lowers the overall score by 13.9 points. A small instruction set restores three quarters of that loss. Test-time reasoning improves scores by 8.5 to 12.5 points for models of 9B and above. Together, these findings suggest four design lessons for other under-resourced languages: use native data where translation fails, plan instruction repair after language adaptation, enable test-time reasoning before scaling up, and avoid overinvesting in target-language prompts. We release the data and code at this https URL

---


### 61. [Drawing the Line: Where AI Guidance and Human Creativity Meet in Emotion-Driven Comic Storyboarding](https://arxiv.org/abs/2610.09155)

**<font color=#1a73e8>作者：</font>** Jocelyn Shen, Isabella Pu, Alessandro Briseño 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> While generative AI models can produce visually faithful artwork, they often fall short in conveying emotional authenticity--a key driver of human expression. In visual storytelling, particularly comic storyboarding, this gap becomes pronounced: effective storyboards require both technical knowledge (e.g., anatomical accuracy or scenic composition) and emotional insight (from lived experience). We explore how human-AI collaboration can support emotion-driven creativity, where the user's feelings guide generation and emotional resonance is the goal. We present EmoToon, a technology probe that helps non-professional artists generate sketch-like storyboards and iterate on visual ideas. In a controlled study with N=25 participants, we find that AI assistance significantly improves emotional expression, aesthetic quality, and exploration, but reduces users' creative ownership. Our findings offer broader insights for human-AI co-creation in the domain of comic storytelling, emphasizing balance between output quality and user freedom, and raising new challenges for image generation models in this domain.

---


### 62. [SpecGuard: Proving a Task Is Broken Before the Agent Cheats](https://arxiv.org/abs/2610.09159)

**<font color=#1a73e8>作者：</font>** Param Biyani, Krishnamurthy Dvijotham  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As autonomous coding agents get increasingly deployed, the risk that accidental or adversarially injected misspecifications in tasks lead to dangerous agent behavior is critical to address. Prior work has shown that agents given such tasks rarely flag the conflict and instead cheat, editing tests or hard-coding expected outputs, and the actions taken to cheat can cause real damage, such as deleting a security defense to make a corrupted test pass. It remains unclear whether such conflicts can be established with independently verifiable evidence before the agent acts. We present SpecGuard, which detects and formally certifies these conflicts between task intent and tests. Given only the task description and codebase, SpecGuard autoformalizes the intended behaviour into a Lean 4 specification. The tests are formalized independently, and the Lean kernel checks whether any implementation could satisfy both formalizations, producing a machine-checked certificate when none can. On conflicted SWE-bench tasks, SpecGuard detects up to 72.8% of conflicts and formally certifies up to 51.1%, with a nearly five-fold lower conflict miss rate than model-based judgment. SpecGuard provides a pre-execution safety check that identifies reward-hacking opportunities through formal certification of task-level conflicts, before any agent behavior is observed. Our code is available at this https URL.

---


### 63. [ToolRACER: A Robust Agentic Conversation Emulation Resource for Agent Training and Evaluation](https://arxiv.org/abs/2610.09163)

**<font color=#1a73e8>作者：</font>** Arkajyoti Chakraborty, Aryan Tayal, Ishika Agarwal 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Task-oriented conversational agents remain fragile under real world conversation scenarios as they rarely follow a predictable script, especially when users exhibit non-cooperative behavior. Existing function-calling benchmarks often emphasize successful, cooperative interactions and underrepresent adversarial conversation trajectories, thereby limiting the training resources available for developing robust agents. We present ToolRACER, a synthetic data generation pipeline that coordinates user, assistant and tool emulation models to generate and validated multi-turn interactions between a user and an agent. Using \sysn, we construct ToolRACERBench a robust multi-turn conversation benchmark spanning six domains, ranging over 55 varied personas, generating a validated corpus of 5.6K conversation trajectories, with approximately 66\% of conversations containing failure-prone conversation scenarios. We inject adversarial behaviors, producing validated conversational interaction trajectories that capture realistic, robust scenarios. We evaluate models trained on ToolRACERBench against internal benchmarks, as well as on function calling benchmarks such as $\tau^2$-bench, BFCLv3 and ACEBench to evaluate agentic accuracy and robustness. Models trained on ToolRACERBench improve end to end agentic accuracy across $\tau^2$-bench and ACEBench, demonstrating significant gains when mixed with in-domain dataset in small language models for agent capability tasks.

---


### 64. [Training Language Models To Be Coherent Decision-Makers](https://arxiv.org/abs/2610.09164)

**<font color=#1a73e8>作者：</font>** Khurram Yamin, Xavier Fernandes, Paul Koch 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable decision-making requires more than accurate prediction: a model must preserve its beliefs, apply the relevant utilities, and recognize when the information needed to justify an action is missing. We study whether language models can learn this decision procedure from supervised fine-tuning and generalize it across domains and differing natural-language expressions of the decision challenge. Across 20 datasets, we explore challenges of belief instability and decision-making errors by first eliciting probabilities of outcomes and then varying only the utilities and the framing of the decision problems, while holding the evidence fixed. We train models to preserve elicited beliefs while selecting the action that maximizes expected utility, and evaluate transfer to unseen application domains, held-out framings, and different classes of payoff structures. We further introduce incomplete-information settings in which required utilities are withheld and replaced with irrelevant text, testing whether models can distinguish missing decision-relevant information from merely additional context. We find that targeted fine-tuning substantially improves coherent decision-making and that in many situations, learning transfers across domains and framings to situations unobserved during training. Further, models trained for decidability learn to identify when action cannot be justified based on missing information. Finally, we show the value of a routed system that considers separately the recognition of decision completeness and utility-sensitive decision execution.

---


### 65. [LayerRoPE: Dynamic Depth-wise Magnitude & Angular Superposition](https://arxiv.org/abs/2610.09179)

**<font color=#1a73e8>作者：</font>** Shikhar Srivastava, Christopher Kanan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As data propagates through a Transformer, the norm of its hidden states grows by orders of magnitude with depth, a phenomenon framed as 'curse of depth' and nearly universally treated as a pathology to be suppressed. We take the opposite view. Across 16 pre-trained LLMs from 9 families, spanning dense, mixture-of-experts and hybrid architectures and Pre-, Peri- and Post-Norm designs, we find that this growth reflects an emergent depth-positional encoding, carried by the only learned per-layer gain on the residual stream, the normalization weight $\gamma$: with depth, $\gamma$ grows in magnitude and rotates in direction, jointly encoding the layer index. We make this depth-conditioned encoding explicit with LayerRoPE, an implicit analog of RoPE along the depth axis, which replaces all layerwise $\gamma$ vectors with a single shared vector and depth-conditioned scalars, at a net reduction in parameters and $<0.02\%$ change in FLOPs. Across a model ladder scaled up to $100$B+ tokens, LayerRoPE consistently outperforms Pre-, Post- and Peri-Norm and Layer-Norm Scaling, reaching Pre-Norm's 1.3B loss with $3.4\times$ less compute; LayerRoPE is the only approach that shows strong convergence and improves near monotonically as depth scales to 512 layers. It improves learning-rate sensitivity by $3$-$10\times$, and transfers naively to and consistently improves looped latent models and Vision Transformers. Inspecting its learned schedule inverts the prevailing premise: LayerRoPE does not shrink the residual stream but widens it, damping what each block reads while amplifying what it writes. Depth stability, our results suggest, calls not for suppressing the residual stream, but for depth-conditioned regulation of the computational blocks it feeds.

---


### 66. [Q-PACE: Dynamic Precision Allocation for Quantization-Aware Training](https://arxiv.org/abs/2610.09183)

**<font color=#1a73e8>作者：</font>** Alexandra Volkova, Matin Ansaripour, Erik Schultheis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantization-aware training (QAT) leverages lower-precision arithmetic to reduce the cost of LLM deployment, but aggressive quantization degrades final model performance. A common remedy is mixed-precision training, in which high precision is assigned to some of the layers to maintain performance while keeping the cost constrained. This approach then requires precision assignments for model layers during training. We provide a new approach, called Q-PACE, consisting of a second-order sensitivity model that predicts the loss increase as a sum of quantization noise MSE weighted by per-layer curvature coefficients. During training, we periodically re-compute these coefficients using perturbations across layers, and re-assign precision. Pretraining and supervised fine-tuning experiments on LLMs of up to 4B parameters show that Q-PACE consistently improves over existing mixed-precision training recipes, and achieves comparable loss at substantially lower total memory budgets. We further find that quantization sensitivity is highly predictable by depth and layer type, and its stability during training allows for infrequent, cheap recalibration.

---


### 67. [The Dichotomy Between Pattern Recognition and Step-by-Step Reasoning](https://arxiv.org/abs/2610.09186)

**<font color=#1a73e8>作者：</font>** Amrut Nadgir, Pratik Chaudhari, Vijay Balasubramanian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We argue that pattern recognition and step-by-step reasoning are two ends of a spectrum. A large language model (LLM) learns to reason step-by-step when data is structured such that the next token depends on a small amount of preceding context. Inference in LLMs resembles pattern recognition when the next token depends on a large amount of preceding context. If the next token depends on only the $c$ most recent tokens, reasoning traces are paths on a De Bruijn graph whose nodes are $c$-length contexts and edges are next-token transitions between contexts. The set of reasoning traces of a task forms a directed acyclic subgraph of the De Bruijn graph. An LLM that has learned all edges of this subgraph can compose them to solve longer, unseen tasks, i.e., it reasons step-by-step. We prove that the number of edges is vanishingly small compared to the number of reasoning traces. Empirically, the number of training samples a transformer needs is a power law in the number of edges, so learning to reason step-by-step is sample efficient. We can induce De Bruijn structure in any task by maintaining a ``state'' that makes future reasoning independent of the past. The frequency of states in the reasoning trace determines $c$. We show, by fine-tuning Qwen2.5-1.5B-Instruct to solve equations and answer questions about stories, that frequent states (small $c$) result in higher accuracy but greater fragility to perturbations at test time. LLMs trained with a large $c$ are only as good as models that perform pattern recognition without reasoning. A moderate density of states balances accuracy and robustness. We show that real-world data has De Bruijn structure: Qwen3-14B and Qwen3-32B retain over 75% of their accuracy on GSM8K, MATH-500 and GPQA-Diamond when attention is restricted to a sliding window less than 15% as long as the full reasoning trace.

---


### 68. [From Probabilities to Decisions: Search and Multi-Teacher Distillation with Jev](https://arxiv.org/abs/2610.09188)

**<font color=#1a73e8>作者：</font>** Mohamad Yazan Sadoun, Sarah Sharif, Yaser Mike Banad  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Probability-only models, which TypeSafe calls System One models, return calibrated probabilities for fixed choices in milliseconds and generate no text. We study one such model, Jev, through two tasks that require decisions under tight constraints. In bullet chess, a bot that places Jev's judgment inside Stockfish search alongside an opening book and endgame tablebases climbs above a 2200 Lichess bullet rating against other bots. Live model calls are too slow for search, so we distill pairwise judgments into a compact evaluator that runs at every position. We then ask how best to spend a fixed labeling budget when an LLM, Qwen3-32B, is available as a second teacher. In chess, averaging both judges' labels beats spending the whole budget on Qwen alone by 9.6 Elo (95% interval 4.3 to 14.9), and the gain replicates on fresh openings; a second answer from the same judge is no substitute, and Jev is the strongest partner for Qwen among the models tested. In passage reranking, Jev's labels alone train a reranker that scores as high as Qwen's, from 21 minutes of API calls instead of 5.1 GPU-hours, and adding Qwen gains at most a few thousandths in ranking quality. Search supplies the lookahead, distillation makes the judgment cheap enough to use at every position, and an LLM partner pays off in chess.

---


### 69. [FreeEvolve: Learning to Evolve Beyond Fixed Loops](https://arxiv.org/abs/2610.09197)

**<font color=#1a73e8>作者：</font>** Lecheng Kong, Like Hui, Nikos Kanakaris 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent evolvers automate the design of the prompts, skills and workflows around language model agents, yet the optimization process they follow is still designed by hand: a fixed search loop decides how candidates are evaluated, which are kept and when the search stops. We propose FREEEVOLVE, which automates this process as well. An environment specifies the goal, target agent, evaluator, data and resource limits; within these limits, the evolver itself decides what to test, how much evidence to collect, which candidates to pursue and when to stop. These decisions follow an editable evolution skill, which we improve through meta-evolution by scoring each candidate skill on the fresh target agent it produces. The optimization process thus becomes a capability learned from experience rather than a loop engineered in advance. On tau3-bench, ARC-AGI-2, ARC-AGI-3 and Terminal-Bench 2.1, FREEEVOLVE controls the evolution campaign by itself, yet improves the primary held-out metric by 13.6 points on average and matches or exceeds hand-designed evolvers. The learned process keeps improving with experience: meta-evolved skills add 6.9 points over the seed skill on fresh target agents, demonstrating transferability across environments.

---


### 70. [Few Bits, One Law: Toward W2A4KV2](https://arxiv.org/abs/2610.09202)

**<font color=#1a73e8>作者：</font>** Kai Yi, Tarek Elgamal, Sruthikesh Surineni 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Extreme low-bit LLM compression is most challenging when weights, activations, and KV caches are quantized together: their distributions differ, and quantization errors interact throughout the network. We introduce CanonQ, a unified quantization-aware training framework that addresses these challenges by separating source canonicalization from task-aware adaptation. Fixed rotations and energy normalization map heterogeneous tensor sources to canonical coordinates, enabling frozen Gaussian-reference codebooks to be reused across layers and models. Joint training then adapts the network to the coupled errors of weight, activation, and cache quantization within a common scalar/vector interface. We bound frozen-codebook transfer error and local task loss, and derive an exact normalization-aware straight-through Jacobian that links quantization distortion to gradient bias. The strongest gains arise under joint W2A4KV2 compression: across LLaMA3-1B/3B/8B, CanonQ-Omni achieves up to 14.28x lower WikiText-2 perplexity and up to 57.9% higher mean zero-shot accuracy than prior state-of-the-art and representative quantization baselines. The benefits extend to Qwen3-1.7B, code generation, and mathematical reasoning: on instruction-tuned MobileLLM-Pro-1B at W2A16KV16, CanonQ achieves relative improvements of 41.7% in HumanEval pass@1 and 39.1% in GSM8K exact match over the strongest evaluated quantization baseline.

---


### 71. [Do Vision Models Learn Physical Constraints or Rendering Shortcuts? A Counterfactual Benchmark for Grounded Physical Consistency](https://arxiv.org/abs/2610.09205)

**<font color=#1a73e8>作者：</font>** M. Moein Esfahani, Sepehr Salem, Mohammed Alser 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern image editing models can satisfy a text instruction while breaking the physics of the edited scene. A new object may cast no shadow, a mirror may fail to reflect visible geometry, or an object may float above a surface that should support it. We study physical plausibility diagnosis, detecting whether an edited image violates scene physics, naming the violation type, localizing the affected region, and explaining the failure in language. We introduce a counterfactual benchmark whose controlled synthetic component uses Mitsuba~3 to generate 5,500 images from 500 scene families. Each family contains one clean image and ten matched violations involving shadows, reflection, support, surface response, and occlusion. The renderer pipeline provides category labels, affected-region masks and boxes, scene metadata, and explanation targets. We use LLaVA-1.5-7B, Qwen2.5-VL-7B, and InternVL3.5-8B as diagnostic baselines rather than proposed methods. On a 1,650-image synthetic test set, the adapted baselines reach 64.0--67.8\% category macro-F1 on standard held-out scenes. For LLaVA-1.5-7B, category macro-F1 falls from 64.0\% on the standard split to 40.8\% under intervention shift. This gap shows that high in-distribution accuracy partly reflects cues tied to rendering and counterfactual construction.

---


### 72. [Multi-Objective Aligned Small Language Model Framework for SUD Patient Dialogue Generation](https://arxiv.org/abs/2610.09209)

**<font color=#1a73e8>作者：</font>** Thushara Manjari Naduvilakandy, Hyeju Jang, Mohammad Al Hasan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Substance Use Disorder (SUD) counseling requires patient responses that reflect underlying cognitive states such as beliefs, coping strategies, and readiness for change. Although large language models (LLMs) can generate fluent text, they often fail to produce cognitively coherent and clinically realistic patient behavior, especially under ethical and data-scarce clinical settings. Moreover, deploying frontier-scale LLMs in healthcare applications presents practical challenges including high computational cost, latency, privacy concerns, and limited deployability in resource-constrained environments, motivating the need for cognitively aligned small language models (SLMs). We propose a cognitively grounded framework for SUD patient dialogue generation that explicitly models and aligns latent cognitive components with patient histories and counselor questions. Our pipeline consists of two stages: cognitive component detection and cognitive component-aligned dialogue generation. To enable effective learning with smaller models, we combine knowledge distillation from high-capacity teacher models, preference optimization from human-annotations, and attention-guided reward shaping. Extensive evaluations using automatic scores like BERTScore, ROUGE, METEOR and BLEU, and LLM-as-judge hit-metrics against both human and teacher-model references show that cognitively informed fine-tuning substantially improves cognitive realization and alignment over a generic instruction-tuned baselines and mental health domain specific SLMs, with particularly strong gains for open-ended cognitive components.

---


### 73. [CurveTQ: Rotation-Free Trellis Quantization of LLM Weights via Curvature-Weighted Search](https://arxiv.org/abs/2610.09212)

**<font color=#1a73e8>作者：</font>** Guanhua Ding, Zi Wang, Ruichao Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The best two-bit weight quantizers for large language models, such as QTIP and Proteus, rotate each weight matrix by a random orthogonal transform, which must be undone at every decoding step, then encode it with a trellis or lattice code under a Euclidean search; the layer Hessian enters only through error feedback between coding blocks. We show that this leaves part of the Hessian unused. Error feedback turns the loss into a weighted sum of per-coordinate rounding errors whose weights, the diagonal of the Hessian's LDL factorization, existing quantizers compute but never read. We put these weights into the Viterbi branch metric, so the search follows the curvature within each coding block. This also explains the rotation: it removes this within-block variation, so weighting in the native basis and rotating are substitutes. On three models the weighted native search matches a full-dimension randomized Hadamard to within about one point of downstream accuracy, and weighting after the rotation gains little. Around this search we build CurveTQ, a trellis codec with no rotation, which handles the weights' amplitude and marginal shape with a factored scale field and a closed-form quantile table, and stores a start state per coding block so the trellis can adapt to the residual that error feedback carries into it. At two bits CurveTQ is 1-3 points higher in mean downstream accuracy than QTIP and Proteus on three 4-8B Instruct models, even after both are given our start state, which alone lifts either baseline by 1-3 points. It also leads on a 35B mixture of experts, to our knowledge the first trellis-coded result on such a model. With no rotation to undo, our decoder is the fastest of the three at all tested batch sizes and bit widths.

---


### 74. [AGAR: a reinforcement learning substrate for LLM program evolution](https://arxiv.org/abs/2610.09215)

**<font color=#1a73e8>作者：</font>** Haoran Li, Zengle Ge, Xiaomin Yuan 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Given a task and an evaluator, a language model can rewrite a candidate program while a search loop decides which rewrites survive, offering a practical route to algorithm discovery. But that loop is governed by five constants set by hand: which parent to select, how hard to mutate, how to keep diversity, what to remember, and a scalar score that never says which part of the program earned it. Reinforcement learning already has an estimator for each. The obstacle is that program evolution is not usually written down as a decision process. We formalize it as a Markov decision process whose action is the modular prefix the model is conditioned on, rather than the program it emits. Credit assignment, value estimation, adaptive exploration, and experience memory can then attach to distinct components. AGAR (Algorithm Generation As RL) provides the resulting substrate: any estimator can be replaced or switched off without changing the controller, making the transfer auditable one mechanism at a time, with no gradient training of the backend model. Across 19 tasks, two backends, and three seeds under one harness, AGAR improves on the stronger of two published baselines on most tasks, with gains concentrated in the competitive-programming family. The formalization also yields a checkable reading of prior work: these systems are implicitly zero-discount, not by choice, but because fitness is exogenous to an individual rather than a return over successors, leaving a discount factor nothing to act on.

---


### 75. [A Deterministic Evidence Layer for Vision-Language Autism Screening from Naturalistic Home Video](https://arxiv.org/abs/2610.09217)

**<font color=#1a73e8>作者：</font>** Wenqi Li, Mindi Ruan, Chuanbo Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autism spectrum disorder (ASD) is diagnosed through specialist observation of a child's social behavior, and access to that expertise is the bottleneck for early identification. Vision-language models (VLMs) describe a child's behavior from video well; the verdict drawn from the description is unstable: at temperature~0, across eight pipeline configurations on one backbone, 16--37\% of clips change their predicted label between repeated runs, and the cause lies in the serving stack. We keep the VLM frozen and move the decision out of the model. Under our grounded perception constraints the VLM writes an event table of timestamped, glossary-labeled events that names the eliciting press and logs counter-evidence; a text-only stage age-calibrates the confidence of each row; a deterministic weight-of-evidence scorer sums it into an evidence total and stratifies it into a risk category, so every decision decomposes into named per-feature contributions and can be re-scored from the saved table. On 43 caregiver-recorded, protocol-free home free-play clips of preschool children, the pipeline reaches AUC $0.851 \pm 0.012$, 86.0\% accuracy, and F$_1$ 71.8 over three runs. It labels 74.4\% of clips correctly in every run (60.5\% for the zero-shot baseline) and flags no typically developing clip in every run (9 of 31 at zero-shot). An ablation on the same backbone attributes the gain to the grounded perception constraints read through the deterministic scorer.

---


### 76. [RLDISCOVER: LLM-driven co-evolution of reinforcement learning algorithms](https://arxiv.org/abs/2610.09218)

**<font color=#1a73e8>作者：</font>** Haoran Li, Zengle Ge, Xiaomin Yuan 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-guided program evolution has enabled discoveries in mathematics and computational optimization, raising the prospect of reinforcement learning (RL) algorithms that self-evolve to improve how agents learn. However, realizing this prospect faces two obstacles. Joint search over coupled algorithmic components is difficult to scale: simultaneous changes can disrupt learning, while isolated changes overlook their dependencies. Evaluating candidate algorithms also requires costly training, with fitness remaining uncertain across random seeds. We introduce RLDiscover, a framework for the self-evolution of model-free deep RL algorithms. Progressive Co-Evolution advances from targeted component edits to joint evolution, while Progressive Probabilistic Evaluation balances search breadth and evaluation fidelity through staged training and repeated evaluation. Experiments across SAC, PPO, and DQN on four benchmark suites show substantial improvements in mean return, with per-family median gains of 32%-84% and a peak return ratio of approximately 363x over a near-zero baseline. These gains include transitions from failed learning to successful task completion, and improvements persist when evolution starts from stronger open-source implementations. On measured SAC locomotion runs, evaluation uses approximately one-fifteenth the estimated compute required to fully evaluate the same candidate pool. Remarkably, independent searches repeatedly discover interpretable combinations of adaptive robust losses, progress-dependent value targets, and running statistics, with selected programs transferring to unseen tasks. These findings point toward a broader role for self-evolution in AI: discovering interpretable algorithms that improve how agents learn.

---


### 77. [CM-DPO: Constraint-Margin Direct Preference Optimization for LLM Planning](https://arxiv.org/abs/2610.09219)

**<font color=#1a73e8>作者：</font>** Rabimba Karanjai, Qun Gu, Hemanth Hegadehalli Madhavarao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Direct Preference Optimization (DPO) treats all constraint violations equally: a $1 budget overshoot and a $1,000 overshoot induce the same training signal. It is also susceptible to length and style bias when preference pairs come from different model families. We introduce Constraint-Margin DPO (CM-DPO), which replaces DPO's binary preference signal with a continuous margin derived from a deterministic symbolic verifier and scaled by violation severity. Hard and soft constraints are separated through a lexicographic objective, ensuring hard constraints are never traded off against preferences. To supply CM-DPO with bias-reduced training pairs, we generate preference data through procedurally generated constraint profiles (DCCG) and minimal-edit distillation from a reasoning teacher (RT-MED), within a framework we call SynPlan-R. On TravelPlanner, NaturalPlan, and out-of-distribution PlanBench, an 8B model fine-tuned with CM-DPO achieves 89.2% pass rate and 93.4% solve rate, matching multi-agent systems at 13x lower latency while outperforming GPT-4o on unseen Blocksworld by 9.2 points.

---


### 78. [Conditional Accuracy Profiles: Diagnosing LLM Judges across Deployment Conditions](https://arxiv.org/abs/2610.09229)

**<font color=#1a73e8>作者：</font>** Wenqi Li, Bin Liu, Mindi Ruan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM-as-judge is now a standard tool for scalable evaluation, but judge performance is still often summarized by a single accuracy number. This aggregate view hides the deployment conditions under which a judge succeeds or fails. We introduce \textbf{Conditional Accuracy Profiling} (CAP), a post-hoc diagnostic framework that decomposes pairwise LLM-judge accuracy into eight conditions organized into content sensitivity, robustness, and rationale quality. CAP is benchmark-agnostic: it can be applied directly when a benchmark provides the required annotations, approximately through task-subset proxies, or through controlled augmentation when perturbation pairs can be generated. We instantiate CAP on seven LLM judges across six pairwise judging benchmarks, including \textsc{judgerEva-Standard}, a controlled testbed we created to support all eight conditions. CAP exposes profile differences hidden by aggregate accuracy: on \textsc{judgerEva}'s judge-independent Hard-Constructed subset, the two judges most sensitive to omitted qualifications rank in the bottom three of seven by overall accuracy, so omission sensitivity is not predicted by aggregate accuracy. Across benchmarks, Position Robustness shows the strongest rank stability (mean Spearman $\bar{\rho}{=}0.87$) but is itself fragile under JudgeBench-Pro adversarial stress, showing the largest mean accuracy drop among the shared conditions, though the dominant degradation channel varies by judge. Condition-level profiles provide a more actionable basis than aggregate accuracy for selecting LLM judges.

---


### 79. [Trajectory Abstraction for the Science of Language Agent Behavior](https://arxiv.org/abs/2610.09237)

**<font color=#1a73e8>作者：</font>** Tianqiang Yan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific studies of language agents need behavioral variables that support hypotheses across tasks and models. We formulate this research problem as learning and testing a hierarchy of trajectory abstractions. A concrete recursive procedure first measures role- and phase-indexed events, proposes temporally constrained relations, and tests their stability across conditions. It then constructs episode-level motif variables from selected relations and repeats the analysis on those variables. Explicit measurement functions connect every abstraction level to the original trajectories. Observations and randomized protocol experiments assess the resulting hypotheses, while comparisons between intervention realizations determine whether an abstraction should be retained, refined, or restricted. We derive a finite-depth bound for accepted reductions, identify protocol effects on fixed abstractions, and characterize realization disagreement and composition of abstraction error. A finite-sample test makes projected intervention consistency operational, and constructed examples illustrate motif construction and abstraction refinement. The formulation distinguishes this experimental approach from semantic taxonomies, qualitative theory induction, and behavior-model recovery. It specifies a proposed research procedure for discovering generalizable behavioral hypotheses, with literature-relative novelty assessed separately from model-relative surprise.

---


### 80. [The Winner's Curse in LLM Self-Improvement Loops: Selection Noise, Lock-in, and Acceptance Rules](https://arxiv.org/abs/2610.09239)

**<font color=#1a73e8>作者：</font>** Litao Hu, Yutong Tang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-improving LLM systems propose changes to themselves and keep those that score better on a small evaluation set. We treat this keep-if-better step as selection under measurement noise, model the correlated errors of the candidates in a single decision, and study empirically what happens when the evaluation set is reused. In runs where Qwen models rewrite their own instructions and every candidate is also scored on 600 held-out items, most proposals after the first are harmful, and the model gives the size of the winner's curse of a generation's best candidate. With a prior from a separate pilot, it matches the average overstatement of first-generation commits in native loops, though not setting by setting. In a pre-registered study, the final selection-set score of greedy loops exceeded held-out accuracy by 13 to 20 points with 16 selection items and by 1 to 5 points with 256. Held-out gains grew with the selection set on TREC but not on GSM8K, and the tested acceptance rules did not beat greedy acceptance over whole runs. Gains measured on the selection set also exceeded held-out gains when a current model refined a competent instruction, and in the validation scores of GEPA and MIPROv2. Scoring the starting and the current instruction on 64 items never used for selection removes the average bias of a loop's reported gain, but single estimates remain off by about 6 points. Self-improvement studies should report held-out gains with their uncertainty.

---


### 81. [Adversarial Images Hijack Web Agents from Visual Grounding to Browser Execution](https://arxiv.org/abs/2610.09240)

**<font color=#1a73e8>作者：</font>** Wanjing Han, Levi Taiji Li, Mu Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern web agents built on large vision-language models process webpages, select relevant UI elements, and translate model outputs into browser actions. Existing visual red-teaming approaches use adversarial visual content to manipulate this process. However, they primarily target model inference and do not explicitly account for structured input processing or action post-processing. Consequently, model-level success does not establish control over browser execution and cannot reliably characterize end-to-end agent robustness. To address this gap, we formulate red teaming for vision-grounded web agents as an end-to-end grounding-to-execution problem, and introduce WebMirage, a framework that crafts localized visual perturbations that cause agents to select attacker-controlled content and execute the corresponding browser action across varying webpage renderings. It uses a role-slot abstraction and webpage recomposition to capture competition among webpage elements, and dataflow analysis to align optimization with action post-processing. We evaluate WebMirage across four agent configurations and six VLM backbones on 2,250 tasks covering 13 public websites and a sandbox benchmark. WebMirage achieves an average attack success rate of 91.9%, compared with 17.4% for the strongest baseline, and remains effective against three agent-level defenses.

---


### 82. [We Query, Therefore We Compute: On Oracle Computation beyond the Machine, with an Application to Agents](https://arxiv.org/abs/2610.09243)

**<font color=#1a73e8>作者：</font>** Kefan Liu, Fengning Ou, Yelin Luo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic systems use large language models (LLMs) to carry out concrete tasks. Prior work often borrows abstractions such as scheduling, caching or isolation piecemeal from operating systems, so the mechanisms it builds share little common ground, and the shared view of the two forms of agentic system, Workflows and Agents, is limited. We construct an abstract machine that provides both.
We treat the LLM as an Oracle and extend a two-stack pushdown automaton with one instruction, which hands the Oracle a whole stack as its query and appends the answer to that same stack. The machine thus performs two computations, the Oracle's and a Turing-complete one that we call the Priestess. A stack that the program only appends to grows autoregressively, as an agent's context does. Two symmetry breakings, S in storage and T in transitions, make a Priestess program the operating system of the programs the Oracle runs, and produce the Agent and the Workflow as the two placements of a task's program.
For internally autoregressive Oracles, the two computations synchronize at the end of every answer under certain conditions, and through that synchronization we model caching and analyse scheduling. No guarantee that holds for every Oracle can fix which content crosses between the two computations, but such a guarantee does fix the boundary itself.
The construction V fits the machine to a von Neumann computer. To show that it is realizable, we propose ArchNights, an extended RISC-V ISA and a Linux-style operating system implementing the machine by design. ArchNights-SE runs on gem5 as a computer system, becomes an agentic system when it runs an LLM as the Oracle, and will be open source.
Agentic systems can then be designed as computer systems are. With a foundation built and a unified view, future work can share invariants and bounds, each with its conditions.

---


### 83. [Adaptive Visual Token Reduction for Accelerated Image Understanding](https://arxiv.org/abs/2610.09252)

**<font color=#1a73e8>作者：</font>** Seyoung Jeong, Jong Pil Yun, Sang Jun Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models achieve strong VQA performance, but processing high-resolution, information-rich images requires substantial computation, motivating visual token reduction. However, existing methods often prune individual tokens or rely on fixed-size cropping, limiting their ability to preserve spatially structured information such as horizontally or vertically elongated text. To address this limitation, we propose ReFIT, an instruction-guided visual token reduction framework for efficient LVLM inference. ReFIT consists of Relevance-Guided Window Reshaping (RWR) and Instruction-Guided Token Refinement (ITR), where RWR captures instruction-relevant regions by adapting to their spatial characteristics, while ITR further removes unnecessary visual tokens. Experiments on four VQA benchmarks demonstrate that ReFIT improves answer accuracy while reducing computational cost, and qualitative results demonstrate its effectiveness in localizing relevant regions and removing unnecessary visual information.

---


### 84. [Evaluating Trajectory Features for Routing Final-Layer Attention](https://arxiv.org/abs/2610.09272)

**<font color=#1a73e8>作者：</font>** Yupeng Yao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attention routing requires a signal that predicts the value of attention on the current prefix. We evaluate whether hidden-state extrapolation error, curvature and error change improve this prediction beyond uncertainty, one-step displacement, position and state projections. Paired executions of the final attention layer supply signed next-token loss differences in frozen SmolLM3-3B-Base and Qwen3.5-4B-Base checkpoints. Utility-supervised routers are tested on 100 held-out PG-19 books at an identical causal 20 percent invocation quota. None of six prespecified comparisons shows a positive gain after familywise correction. In Qwen3.5, a parameter-matched fixed-projection control lowers NLL by 0.00356 nats/token relative to the trajectory router (95 percent interval 0.00218 to 0.00487). Secondary results depend on the operation removed, feature location and scoring horizon; frozen thresholds also drift substantially at longer horizons. Actual selected-query execution yields small long-sequence latency reductions with increased NLL, while learned routers remain slower during cached continuation. The study identifies limits on the incremental value of these trajectory summaries and separates allocation quality from measured inference benefit.

---


### 85. [AI-Assisted Submissions in Online Research Are Rare and Highly Concentrated but Routinely Approved](https://arxiv.org/abs/2610.09279)

**<font color=#1a73e8>作者：</font>** Neil K. R. Sehgal, Manuel Tonneau, Dunigan Folk 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Online research platforms underpin much of what science claims about people, on the assumption that a human produced each response. Generative AI threatens that assumption by letting participants delegate responses to a chatbot, yet how often they do so remains unclear because prior estimates rely on self-report or automated detection rather than direct observation. We surveyed 2,500 workers on a high quality online research platform and directly observed AI assistance by linking donated ChatGPT histories to platform submission records of weekly ChatGPT users, covering 712,930 submissions across more than 127,000 studies. Although one in eight surveyed workers reported ever using AI on a study and 68% of observed workers had done so, assistance appeared in only 1% of submissions, with no detectable increase over more than 3 years. Assistance was often temporally localized within tasks and highly concentrated among workers, with 5% accounting for 64% of assisted submissions. Where assistance occurred, workers were virtually always paid, even when study instructions prohibited AI use, with overall approval rates similar to those for unassisted submissions. Half of assisted submissions involved bounded responses, outside the scope of the platform's LLM detector for open-ended responses. Taken together, our results do not support the view that AI assistance currently poses an existential threat to online research, but reveal limited payment consequences for prohibited use and gaps in platform safeguards, leaving platforms poorly prepared should that threat materialize.

---


### 86. [RT-Safe: Benchmarking Agent Safety in Real-Time Embodied Environment](https://arxiv.org/abs/2610.09294)

**<font color=#1a73e8>作者：</font>** Tianruo Rose Xu, Jiawei Ren, Yichi Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rapid progress in AI agents has brought growing attention to agent safety, with extensive evaluation focused on digital environments. As agents move into the physical world, embodied safety becomes increasingly important: failures can cause human injury and costly hardware damage. Beyond selecting safe actions, embodied agents must also operate under real-time constraints: the physical world does not pause while an agent reasons. As pedestrians move and vehicles approach during inference, an action that appears safe at observation time may become unsafe before execution. Real-time embodied safety therefore depends on both decision quality and decision latency. We introduce RT-SAFE, a simulated urban benchmark for evaluating embodied-agent safety under real-time constraints. RT-SAFE combines navigation tasks with moving actors, environmental hazards, and traffic rules, while allowing the world to evolve throughout inference and action execution. Across eight VLMs, agents achieve high task completion yet almost never complete safely: in the hardest setting, only 0.7% of episodes finish without a safety event. More strikingly, matched static and real-time evaluations yield task completion rates of 91.3% and 94.1%, respectively, while real-time execution increases collisions by $12.3\times$. These results reveal that standard task success can mask substantial safety failures, and that decision latency itself can become a source of physical risk. Finally, we show that RT-SAFE can support offline RL training and substantially reduce collision rates while achieving strong task completion.

---


### 87. [The AI Evaluation Ecosystem](https://arxiv.org/abs/2610.09296)

**<font color=#1a73e8>作者：</font>** Yash Dave, Sang T. Truong, Serena Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI evaluation shapes the decisions of model providers, users, funders, and regulators. We argue that designing valid benchmarks requires contextualizing design choices in the dynamics of this ecosystem of actors. We develop a simulation architecture that combines rule-based market dynamics with LLM-driven strategic actors, building on advances in Generative Agent-Based Modeling (GABM). We model benchmarks, consumer needs, and provider capabilities as vectors over a six-dimensional capability space (reasoning, coding, knowledge, safety, communication, agentic), with structural information partitions across actors. As a case study, we apply this stylized simulation to explore benchmark holdout design. We find that moving from public benchmarks to private holdout benchmarks shrinks the gap between benchmark scores and user satisfaction on most benchmarks but widens it on a few, depending on where holdout weights shift scoring credit. We stress-test our findings at both the instrument and case-study level, drawing on the V&V framework of Sargent (2013) and GABM-specific evidence criteria. Beyond holdout design, our simulation is a hypothesis-generating sandbox for studying how evaluator and policy choices, in turn, reshape the ecosystem.

---


### 88. [Denoising Blocks, Not Tokens: Efficient Compressed Continuous Diffusion with Branching Token Realization](https://arxiv.org/abs/2610.09311)

**<font color=#1a73e8>作者：</font>** Xinsong Feng, Peng Du, Zhizhuo Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) generate text through iterative parallel refinement, offering the potential for higher throughput than autoregressive (AR) decoding. However, most DLMs still maintain one generative state per token, so every denoising step processes a state sequence as long as the output sequence, limiting the throughput gains from parallel generation. Continuous DLMs provide an additional degree of freedom: a single continuous state can represent multiple tokens, allowing diffusion to operate on a much shorter latent sequence. We introduce \emph{Branching Latent Diffusion (BLD)}, which exploits this flexibility by compressing a 1024-token sequence into only 64 block latents, a $16\times$ reduction. BLD combines latent compression with \emph{branching token realization}, where each latent is decoded by a local AR branch and all branches run in parallel. Because strong compression makes joint latent generation difficult, BLD generates the latents in groups, conditioning each group on previously generated latents. In end-to-end evaluation on the same GPU, BLD reduces generation FLOPs by more than $80\times$ and increases throughput by more than $6\times$ relative to the similarly sized ELF-L baseline. Compared with the AR baseline, BLD achieves more than $6\times$ higher throughput and more than $4\times$ lower latency. Despite the compression, BLD maintains competitive local fluency and diversity, although long-range coherence remains challenging. Overall, BLD shows that moving diffusion from token-level states to compressed latent sequences can substantially improve the efficiency of long-sequence generation.

---


### 89. [Why VLMs Miss Small Objects, and When Zooming In Is Safe](https://arxiv.org/abs/2610.09313)

**<font color=#1a73e8>作者：</font>** Junzhe Shi, Yuan Gan, Shida Jiang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) often miss small objects in large images. We ask three questions: what limits them, which of these limits better models can remove, and whether the classical way of handling large images, local decomposition, still has a future. We answer them with a theory built on two quantities of the image interface: S, the number of visual tokens across an object's side, and L, the content a call must cover. The limits: a W x H image sent whole within N tokens gives an object of side m at most m*sqrt(N/(WH)) tokens per side. Doubling the token budget N therefore raises the largest S a whole image can reach by only 41%, and seeing an image at the S an object needs costs at least order S^2 tokens whatever the model. If recognition improves gradually with S, any search strategy, zoom agents included, obeys a recall-cost frontier. What better models can change: the S an object needs and how much one call can carry, measured in bits per object found; the coverage cost remains. Decomposition: yes. Assuming only that more tokens per object and less content per call do not hurt on average, splitting an image cannot lower recall if no view zooms out relative to the whole image and views overlap by one object. Neither part of this condition can be dropped; we bound the cost of every such decomposition, and a simple rule approaches the bound as the image grows. We test the theory in about 177,000 requests on 797 images. On controlled images, none of 40 orderings predicted for 8 VLMs is violated. Checked after the fact on drawings, floor plans, natural and synthetic images, 61 of 89 implied orderings hold significantly and 4 fail, all for OpenAI models given more pixels than their default path. On construction drawings the rule never significantly lowered recall relative to the whole image and raised it by up to 0.28. Code and data: this https URL

---


### 90. [Dialect-Robust Speech Language Models with Synthetic Pseudo-Dialect Augmentation](https://arxiv.org/abs/2610.09321)

**<font color=#1a73e8>作者：</font>** Shunsuke Mitsumori, Tomoya Mizumoto, Yusuke Fujita  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech Language Model (SLM) performance often degrades on dialects due to data scarcity. Conventional text-to-speech (TTS) augmentation struggles to cover diverse dialects as it requires a certain amount of real dialect speech. We propose synthesizing pseudo-dialect speech by converting LLM-generated dialect text via a standard-language TTS model, requiring zero real dialect speech. Additionally, we introduce intermediate standard-text prediction during training, acting as semantic normalization for downstream tasks. We evaluate dialect understanding via dialect-to-English speech translation across Japanese, German, and Chinese dialects. Compared to synthetic standard speech baselines, pseudo-dialect augmentation improves scores for Japanese (from 25.38 to 26.24) and German (from 31.57 to 32.47). Furthermore, the intermediate standard-text prediction effectively bridges the semantic gap, boosting performance to 28.26 for Japanese and from 11.67 to 16.37 for Chinese. These results suggest that our approach scales to various languages without requiring speech resources specific to each dialect.

---


### 91. [Visual Jev Rewards: Reference-Bound Verification for Multi-Subject Image Generation](https://arxiv.org/abs/2610.09328)

**<font color=#1a73e8>作者：</font>** Baoteng Li, Wenzhuo Wu, Kongming Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-subject image generation requires rewards that verify whether requested attributes, actions, and relations hold for the specified reference subjects. Subject presence alone does not establish that the correct subjects participate in a requested interaction. We present reference-bound Visual Jev rewards that turn these visual decisions into generator training signals. Each subject-related question receives a positive label only when the requested condition and the relevant reference identities hold jointly. We construct fixed questions offline, train a Qwen3.5-4B verifier with binary supervision, and directly read Yes probabilities from its language-model head. Their mean supplies a GRPO reward while retaining individual judgments for inspection. Using 200 MICo-150K training tasks and 30 updates, the framework raises a GPT-5.4 composite score from 41.78 to 52.50 on a manually selected 897-task MICo-Bench subset; direct 27B rewards yield 51.84. Each reward is tested in one GRPO run, and offline human evaluation does not establish a statistically significant advantage over direct scoring. The study provides an initial implementation and evaluation of Visual Jev as a reference-bound reward for multi-subject image generation.

---


### 92. [Ask the Expert: LLM-Guided Reinforcement Learning for Autonomous Cyber Defense](https://arxiv.org/abs/2610.09337)

**<font color=#1a73e8>作者：</font>** Fernando Martinez, Abhishek Satyam, Tao Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Policy-based reinforcement learning (RL) approaches have produced promising results for autonomous cyber defense; however, they are sample-inefficient in settings where defenders must respond under delayed, partial observations with actions from large action spaces. While large language models (LLMs) may reason semantically about security state space, high latency and trust assumptions prevent attractive in-line deployment models. We introduce Ask the Expert, a training-time guidance framework which first summarizes hard cyber-defense states, then intermittently queries an LLM for host-level defensive recommendations via a constrained action interface, and finally transforms those recommendations into tiered reward shaping for use with PPO. Because the LLM is discarded after training, deployment is a pure RL policy. Across TTCP CAGE CC1 and CC2 and both attacker types, this asymmetric design improves sample efficiency over PPO and outperforms the evaluated potential-based reward shaping (PBRS) baselines, while retaining the strongest terminal mean and requiring no LLM dependency at deployment time.

---


### 93. [Shared Low-rank Basis Factorization for Data-free Mixture-of-Experts Compression](https://arxiv.org/abs/2610.09342)

**<font color=#1a73e8>作者：</font>** Tianxiao Cao, Jiahe Shao, Yuning Qiu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) large language models decouple capacity from compute through sparse routing, but their large parameter count creates storage and serving challenges. We analyze three MoE compression families: expert pruning, expert merging, and weight reconstruction, and derive structural error bounds showing that pruning and merging can incur non-vanishing errors tied to routing and expert heterogeneity. In contrast, weight reconstruction avoids these structural costs by preserving expert structure and routing. Motivated by the analysis, we propose Shared Low-rank Basis Factorization (SLBF), a data-free weight reconstruction method that uses rank-$k$ bases shared among experts, enabling richer cross-expert sharing, faster convergence, and lower reconstruction error. A post-hoc gauge fixing removes redundant parameters at no representational cost. Across five MoE architectures spanning 16B to 122B parameters, SLBF consistently outperforms methods from all three compression families.

---


### 94. [Do Image Editors Follow Depth-Dependent Blur and Aperture Response? A Rendered-Ground-Truth Pilot Audit](https://arxiv.org/abs/2610.09344)

**<font color=#1a73e8>作者：</font>** Zhihan Chen, Yuhuan Zhao, Yijie Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> General image editors are asked to make a photo look as if it were taken at f/1.4, yet it is rarely checked whether the blur they add follows thin-lens optics. A physical aperture edit spreads blur across depth in thin-lens proportions and changes the blur when the aperture changes; prior evaluations check blur monotonicity, sharpness-trend correlation, effective-aperture error, or vision-language judgments, and none we found reports the two properties separately at known depths. In this pilot audit of two editors (Gemini~3.1 Flash Image and GPT-image-2.5) we compare against a rendered oracle: Blender Cycles scenes with true thin-lens depth of field, one blur-width estimator applied identically to oracle and editor outputs, and preregistered depth and aperture indices. In 24 texture scenes rendered in one three-panel geometry, accepted and measurable panels show f/1.4-to-f/2.8 width ratios, $\bar\sigma_{1.4}/\bar\sigma_{2.8}$, of 0.99--1.18 against 1.98--2.13 for the oracle, and ratios of pooled median Gaussian-equivalent near/far blur widths of about 1.18--1.25 (Gemini) and 0.97--1.05 (GPT-image) against 1.69--1.82. Preregistered black-box interventions show that qualitative wording changes blur strength by roughly 2--10 times, whereas a request for 2 versus 6 px changes it 1.1--1.3 times and no tested wording of the f-number meets the registered ``followed'' criterion. The depth compression appears in the original and reversed centre-focus layouts; with the focus on the near panel, the available-panel depth index reaches the registered threshold, and the aperture response stays attenuated in every layout tested. Scalar metrics adapted from published ones give oracle-like scores to synthetic editors whose proportions are compressed.

---


### 95. [OnlineQAT: On-Policy Distillation for Ultra-Low-Bit Large Language Models](https://arxiv.org/abs/2610.09346)

**<font color=#1a73e8>作者：</font>** Wenjun Wang, Heng Li, Yanggan Gu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Quantization-aware training (QAT) can recover much of the accuracy lost when large language models are compressed below four bits. Existing re- covery stages, however, are commonly optimized on fixed completions or teacher-generated answers, whereas the deployed quantized model condi- tions on prefixes generated by itself. Quantization errors can therefore move the model into states that are absent from offline recovery data. We introduce OnlineQAT, a two-stage framework that first obtains a usable low-bit initialization through block-wise QAT and then performs on-policy distillation (OPD) on student-generated responses. At each visited pre- fix, a frozen full-precision teacher provides a sampled reverse-KL training signal. On Qwen3-1.7B, OnlineQAT obtains the best average among the compared quantized methods: 57.28 at W3A16 and 32.52 at W2A16, im- proving over ReasoningQAT by 2.90 and 0.44 points, respectively. The results suggest that student-visited states provide a useful recovery signal beyond fixed-completion training, particularly at three bits.

---


### 96. [Relevance Is Not Sufficiency: What Actually Closes the Evidence Gap in Long-Term Memory QA](https://arxiv.org/abs/2610.09348)

**<font color=#1a73e8>作者：</font>** Yufeng Li, Shuxin Li, Zhenhua Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents that interact with a user across many sessions accumulate histories that exceed their context window, so they store past interactions in an external memory and answer each question from a small set of retrieved records. Existing memory systems rank records by lexical or embedding relevance, yet the top-ranked memories can each be relevant while jointly omitting a complementary fact that the answer requires, especially for multi-session and temporal questions.
Drawing on the distinction between relevance and sufficiency in legal evidence scholarship, we recast memory retrieval as constructing a sufficient memory set.
To operationalize this view, we introduce a blinded LLM judgment over the retrieved set, together with Gold Hit and Turn Hit as evidence-coverage proxies. We then propose Budgeted Flat Reconstruction (BFR), which builds sufficient sets over a fixed flat memory store in two stages. Specifically, we first apply Formal Concept Analysis for Memory Selection (FCA-MS) to decompose the question into information requirements and select a compact candidate subset that jointly covers them. Then, we repeatedly acquire unseen records through deeper text search or complementary entity and session views, stopping when the budget is exhausted.
Experiments on LoCoMo and LongMemEval-S show that BFR outperforms same-store adaptations of recent agent-memory systems in both answer quality and evidence coverage. Specifically, on LongMemEval-S it raises judged accuracy from 72.4% to 82.2% and Turn Hit to 91.4%.

---


### 97. [Multimodal LLMs Can Learn to Read Brain Signals: A Vision--Language Model for Unified Multi-Task EEG Decoding](https://arxiv.org/abs/2610.09355)

**<font color=#1a73e8>作者：</font>** Parastoo Azizeddin, Omid Sharafi, Maryam M. Shanechi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning EEG representations that generalize across cognitive tasks, subjects, and recording conditions remains a key challenge in electroencephalography (EEG) decoding. Recent advances in foundation models have improved EEG decoding performance, yet a fundamental open question remains: how to effectively interface neural signals with these models to enable multi-task learning across datasets. To investigate this question, we introduce BraVista, a visual-language framework that encodes multichannel EEG signals as structured images and enables multi-task learning through instruction-conditioned vision-language models (VLMs). Our approach relies on continued post-training of a general-domain VLM, leveraging its visual and linguistic priors to adapt to neural signals without a separate large-scale EEG-specific pretraining stage. We evaluate BraVista on four datasets spanning sleep staging, emotion recognition, cognitive workload classification, and abnormal EEG detection, showing strong performance across these tasks. Further analyses show that the choice of EEG-to-image representation is critical to performance. Moreover, through controlled perturbations of the EEG signal, we observe a gradual performance degradation under increasing noise, suggesting that the model relies on EEG-relevant information rather than superficial visual patterns. Together, these findings establish structured visual representations as an effective and scalable interface between neural signals and general-domain foundation models for unified multi-task EEG decoding.

---


### 98. [Expert Coupling in MoE Pretraining: Reducing All-to-All Overhead with Correlated Placement and Token Shuffling](https://arxiv.org/abs/2610.09372)

**<font color=#1a73e8>作者：</font>** Radha Gulhane, Quentin Anthony, Beren Millidge  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) layers replace the feed-forward block of a Transformer with E expert networks, and each token is routed to k of these experts. Under expert parallelism (EP) the experts are distributed across GPUs, and every MoE layer runs all-to-all collectives in the forward and backward passes to dispatch tokens to their experts and then combine the results. On a cluster with 8 AMD Instinct MI300X GPUs per node, these collectives can take 45% of the training step at EP32 with top-2 routing and 60% with top-6 routing. We find that early in pretraining routers have already learned to assign tokens to experts in correlated patterns, both within a layer and across layers. At top-2, 0.8% of the expert pairs in a layer are selected together by 42% of tokens, and the experts a token selects at one layer predict the experts it selects at the next layer. We use these correlations to keep more token--expert assignments on the token's own GPU, which reduces communication across GPUs and across nodes. Correlated expert placement puts experts that are often selected together on the same GPU. Combined with a dispatcher that sends each token to each GPU once, it removes up to 58% of dispatched rows. Token shuffling applies when sequence parallelism shards tokens across the EP group. It moves each token to the GPU predicted to hold its next-layer experts during the reduce-scatter that follows attention. On one node this raises the share of token--expert assignments served on the token's GPU from 12.5% to 59%. In Megatron-LM, across EP degrees from 8 to 64 with top-2 and top-6 routing, the two methods reduce all-to-all time by 1.16-2.63X and end-to-end step time by up to 1.41X. Neither method changes the models' underlying routing decisions or expert parameters.

---


### 99. [DUDA-Bench: Benchmarking LLM Agents on Multimodal Data-Driven Urban Diagnosis](https://arxiv.org/abs/2610.09374)

**<font color=#1a73e8>作者：</font>** Yizhi Song, Hang Ni, Weijia Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Urban diagnosis integrates heterogeneous observations to identify urban problems, localize affected areas, and investigate contributing factors, informing evidence-based urban planning and management. However, its reliance on labor-intensive, case-specific expert workflows limits scalability and reuse, motivating the exploration of agent-based execution. To evaluate this capability, we introduce DUDA-Bench, a hierarchical and interactive benchmark that formalizes data-driven urban diagnosis as a multi-stage agent workflow. It comprises 86 atomic and 22 workflow tasks spanning four analytical stages, grounded in multimodal data from 12 cities covering five urban problem types. Evaluations of seven backbone models and five agent systems reveal a substantial gap between isolated analytical competence and end-to-end diagnosis, with system benefits varying across backbones. Trajectory analysis shows that unresolved evidence gaps propagate across stages, while successful recovery involves revising assumptions and actions using feedback. These findings highlight limitations in coordinating analytical capabilities across stages, particularly adaptive planning, evidence integration, and verification. More broadly, DUDA-Bench provides a framework for translating expert analytical workflows into hierarchical agent tasks and process-aware evaluation, supporting systematic assessment of end-to-end analytical capabilities.

---


### 100. [From Retrieval to Customer Context: Evaluating Frontier-Model Systems for Voice-of-Customer Analysis](https://arxiv.org/abs/2610.09375)

**<font color=#1a73e8>作者：</font>** Raviraja G, Viraj Bagal, Prabhath Chellingi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Organizations increasingly use frontier language models to analyze customer feedback, but answer quality also depends on how that feedback is organized and made available. We define a \emph{customer context graph} as a unified model of customer and business context. Typed relationships connect customer objects (feedback, conversations, users, and accounts), operational objects (tickets, support agents, opportunities, and competitors), and analytical or action objects (taxonomy concepts, evidence, insights, work items, and outcomes). This lets an agent investigate not only what customers say, but why, who is affected, what action followed, who owns it, and whether it was resolved. For this experiment, the graph is populated from public Cursor feedback; the same architecture can support any type of feedback source. We compare Agentic RAG, a Deep Research Agent, and a Customer Context Graph-backed Agent on the same 9,432 public Cursor feedback records using 30 realistic product, incident, comparison, and metadata questions. Without exhaustive ground truth, we jointly score responses on answer quality (coverage and organization), analytical depth (specificity and decomposition), and evidence quality (citation support and traceability), using a comparative rubric calibrated on 28 of the 30 questions. We sample cited records against their claims and weight the three dimensions equally. Under this aligned rubric, the Customer Context Graph-backed Agent scores 0.961 overall, versus 0.710 for the Deep Research Agent and 0.651 for Agentic RAG, and leads the Deep Research Agent on 27 of 30 paired questions (sign-test p < 10^(-5); strictly best on 26 of 30). Its largest advantage is analytical depth (0.967 versus 0.642), reflecting more specific, hierarchically developed findings with quantified themes and traceable evidence...

---


> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-266](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
