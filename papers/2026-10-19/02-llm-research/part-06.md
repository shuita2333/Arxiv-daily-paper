# 🧠 大模型相关研究 | 2026年10月19日

> 本类共 **321** 篇论文：已确认 **300** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-321](./part-07.md)

---

### 251. [CLUE: Uncovering Social Context for Pragmatic Understanding](https://arxiv.org/abs/2610.22167)

**<font color=#1a73e8>作者：</font>** Chengfei Wu, Zhaoqing Wu, Dan Goldwasser  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding a conversation requires connecting what is said to the speakers' relationships, expectations, and earlier exchanges. Prior work shows that supplying relevant context can improve models' social judgments, but much of this information may already be present in the conversation. This motivates training models to discover the cues that matter and use them to support an interpretation. We propose CLUE, a two-stage training pipeline that combines supervised evidence reasoning with GRPO guided by Grounded Information Utilization ($\mathrm{IU}_{\mathrm{G}}$). This reward credits new, evidence-supported social inferences while accounting for reasoning effort. We train on a small set of conversational examples to assess effectiveness and generalization across tasks, languages, and genres. At inference time, the trained model reasons over the supplied interaction in a self-contained manner. Compared with base Qwen, CLUE achieves relative gains of 17.3% in-domain and 9.3% out-of-domain in average weighted F1, with higher F1 on four of five out-of-domain evaluations. These gains are accompanied by over 80% fewer reasoning tokens on average in both domains. Human evaluation further finds that CLUE more often grounds its explanations in specific conversational content, with closer alignment between its quoted evidence and human-selected context.

---


### 252. [Lexical Reference Frames: Interpreting LM Residual Streams in Native Semantics](https://arxiv.org/abs/2610.22169)

**<font color=#1a73e8>作者：</font>** Jian Gu, Hongyu Zhang, Chunyang Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The vocabulary of a language model is its native semantics: the embedding and the unembedding fix the meaning of a state at the two ends of the residual stream. Between them, existing methods either reuse a fixed lens or treat the states as a point cloud, and neither reads a state the way the model does. We argue that every hidden state has a native reference frame, induced by the layers that read it next and adaptive to the context. Lexical reference frames approximate it by reading a state through the model's own remaining layers with a stated number of rounds of attention between positions and a typical attention output for the rest, without fitting to the model's output. No lens, with fixed directions per layer, can exceed the square root of the native frame's coherence, 0.30 and 0.35 at mid-depth of SmolLM3-3B and OLMo3-7B, whereas the first-order frame, LexFrame[1], reaches 0.97 and 0.97 and reads a state within 0.16 nats of the model's output. Its coefficients attribute predictions more faithfully than attribution patching, its lexical basis steers a prediction while sparing other tokens, and its confident readings would let an early exit skip 0.45 and 0.42 of the layers, where lenses skip almost none. In this way, lexical reference frames make every hidden state of the model readable, attributable and steerable.

---


### 253. [Mosaic: Multi-Session Agentic Reinforcement Learning](https://arxiv.org/abs/2610.22174)

**<font color=#1a73e8>作者：</font>** Yilong Xu, Minrui Xu, Xinyu Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most existing agentic reinforcement learning methods assume single-session trajectories, where interaction proceeds within one continuously accumulated context. However, agentic techniques such as context compaction and subagent forking may produce trajectories spanning multiple sessions, creating a mismatch between the single-session training assumption and inference-time execution. Therefore, we introduce Multi-Session Agentic Reinforcement Learning, a more general setting that supports an arbitrary number of sessions within a trajectory. Under this setting, a widely adopted method is to broadcast trajectory-level advantages to all sessions, but this does not distinguish contributions from various sessions or guide session allocation within trajectories. To address this issue, we propose Mosaic, a multi-session agentic RL method with critic-free hierarchical optimization. At the trajectory level, it incorporates session-usage signals into advantage estimation. At the session level, it shapes each session's advantage according to the estimated marginal contribution. Experiments on BrowseComp with Qwen3.5-4B show that Mosaic outperforms broadcasting in both context compaction and subagent forking scenarios while using fewer sessions on average. Further analyses show that our method achieves improvements in session utility and allocation, which we suggested is a promising target for future advances in multi-session agentic RL.

---


### 254. [LCT: Losslessly Compressed Tensors with GPU friendly execution for Training](https://arxiv.org/abs/2610.22179)

**<font color=#1a73e8>作者：</font>** Max Zhu, Bohang Sun, Pietro Lio 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lossless tensor compression could reduce memory usage during training, but training requires tensors to be repeatedly re-encoded. We introduce Losslessly Compressed Tensors (LCT), a GPU execution framework designed for this repeated encode-decode regime. LCT exploits the natural redundancy in floating point data to reduce storage for weights, activations and optimizer states. Highly optimized GPU kernels implement Huffman coding with precomputed codebooks for low compression and decompression overhead, essential for training. Our analysis characterizes LCT's storage costs and adaptation to magnitude shifts. LCT achieves a compression ratio of up to $1.455\times$, and is demonstrated in training and finetuning settings. On a 162M-parameter NanoGPT, LCT reduces memory usage by $24.6\%$ for a $7.2\%$ step-time increase. In Qwen3-4B fine-tuning, LCT saves up to $23.8\%$ of peak memory, enabling a $3.5\times$ larger context length in training on the same GPU.

---


### 255. [EVA-Cap: Optimizing Audiovisual Video Captioning via Event-Centric Alignment](https://arxiv.org/abs/2610.22186)

**<font color=#1a73e8>作者：</font>** Jiapeng Shi, Qiuxia Hou, Jiaqi Leng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Omni Language Models (OLMs) provide a unified solution for audiovisual video captioning. Nevertheless, existing approaches predominantly treat captioning as an unstructured text generation process, neglecting the inherent semantic structure of videos and leading to suboptimal fine-grained audiovisual alignment. To bridge this gap, we propose EVA-Cap, a novel framework that decomposes captions into atomic audiovisual events and transforms unstructured text supervision into event-centric alignment. We train EVA-Cap via Supervised Fine-Tuning (SFT) and Group Relative Policy Optimization (GRPO) on a self-curated dataset, EVA-Data, which is built with event-centric quality control. During the GRPO phase, the model is explicitly optimized against three event-centric alignment targets: global event completeness, intra-event attribution, and inter-event synchronization. Extensive experiments demonstrate that EVA-Cap significantly outperforms existing methods in event-centric evaluation (e.g., +9.0% average gain on ChronusAV), while achieving competitive performance on general audiovisual captioning benchmarks (e.g., +3.3% on WorldSense).

---


### 256. [Change the Number, Change the Answer: Assessing Rating Scale Sensitivity in LLM-Based Text Scoring](https://arxiv.org/abs/2610.22187)

**<font color=#1a73e8>作者：</font>** Wonjeong Jo, Gyuwan Kim, Ming Shan Hee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used in computational social science to assign scalar scores to social and psychological constructs. However, studies use different rating scales, and whether their scores remain comparable across scale designs is understudied. To address this gap, we define and systematically investigate scale sensitivity, the variation in LLM-generated scores caused by rating scale design. We distinguish numerical sensitivity, changes in normalized scores, from semantic sensitivity, changes in score interpretation. To assess both, our experimental design crosses 2 formats (continuous vs. ordinal), 4 ranges (3, 5, 11, and 21 points), and 2 signs (signed vs. unsigned) across 3 tasks (political leaning, sentiment, and toxicity), 2 prompting strategies (zero-shot and rubric-based), and 5 LLMs. We find that changing one design element shifts normalized scores by about 0.10 on average and changes the category of roughly 20% of texts. Sensitivity is greatest for toxicity, the only unipolar construct examined. Also, rubric-based prompting does not reduce sensitivity compared with zero-shot prompting. We provide practical guidance for designing more reliable LLM-based text scoring and highlight the need for robustness checks across alternative scales.

---


### 257. [Terminal-RSI: Recursive Self-Improving Terminal Agents via Recursive Self-Rewrite and Policy-Refine](https://arxiv.org/abs/2610.22192)

**<font color=#1a73e8>作者：</font>** Junyao Yang, Zongxia Li, Yucheng Shi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Converting verifier outcomes into useful policy updates and partial progress into complete task resolution is crucial for terminal agents. We present Terminal-RSI, which alternates Recursive Self-Rewrite (RSR) of verified trajectories with critic-inheriting Recursive Policy-Refine (RPR). We formulate Turn-Boundary Skip-Observation GAE (TB-GAE) to retain token-specific baselines while applying decay across interaction turns. Family Dense Reward (FDR) calibrates semantic progress across task families; Success-Prioritized Reward (SPR) separates strict success from bounded partial credit. A Warm-up Critic Model, recursive critic handoff, and stage-specific learning rates coordinate the two refinement phases. The five-stage sequence from Qwen3.8-27B base model through RSR-1, RPR-1, RSR-2, and RPR-2 yields Terminal-RSI-27B: 19.84% on Terminal-Bench 4.0, 86.52% on Terminal-Bench 2.1, 16.95% on Terminal-Bench 3.0, and 79.00% on Terminal-Bench Hard. On LHTB, process reward rises from 0.21 to 0.37 and strict completion from 0/46 to 5/46; SWR100 success doubles from 3.00% to 6.00%. By recursively coupling verified trajectory rewriting with critic-inheriting policy refinement, each retained stage consolidates discovered behaviors and progressively advances the agent from partial local repairs to strict terminal verification.

---


### 258. [AutoSFT: An Agentic System for Automated Data Research in Supervised Fine-Tuning](https://arxiv.org/abs/2610.22194)

**<font color=#1a73e8>作者：</font>** Bingxiang He, Pengqi Sun, Shihao Peng 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language model agents increasingly automate post-training, but when given the full training stack they converge on supervised fine-tuning and spend most effort revising training data. Existing systems give the agent one kind of control, selecting rows from a fixed pool or calling a generator, whereas a human data engineer adjusts proportions, prunes, repairs, replaces and synthesizes the data. We design a data action space for these changes and ask whether an automated system can make the full range rather than one of them, and what structure that requires. We first run this loop with a single agent, and it reaches only one action, adjusting category proportions, while its context fills with execution output and is discarded mid-search. We therefore introduce \textbf{AutoSFT}, a multi-agent system where a meta agent separates execution from analysis, gathers proposals from independent angles, and calls a synthesis subagent for capabilities the pool cannot cover, with the model, the trainer, and the budget fixed within each comparison. Adding each component in turn helps: the executor halves context loss, the analysis subagents lift the best IFEval by $+6.5$, and synthesis adds $+3.4$ IFEval and $+2.9$ IFBench. The same loop transfers to code, where analysis adds $+3.7$ MBPP+ over a single agent that does not improve. Every result comes from runs that retrain from the base model each round, so each component's effect is individually attributable. Our findings suggest that automating SFT data research depends more on covering diverse data actions than on a stronger single action.

---


### 259. [HTN-Orchestrate: A Hierarchical Task Network Framework for Multi-Agent Orchestration](https://arxiv.org/abs/2610.22195)

**<font color=#1a73e8>作者：</font>** Yanchen Deng, Jianguo Huang, Yao Long Teng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Orchestrating multiple agents on a complex task requires reconciling local subtask execution with global task planning. Dynamic dispatch approaches provide execution flexibility but do not explicitly model subtask hierarchies or dependencies, while predefined workflows impose this structure but fix the decomposition before execution begins. Therefore, we introduce HTN-Orchestrate, a two-layer framework that separates these responsibilities through a hierarchical task network (HTN). The Planner maintains subtask hierarchies and dependencies, deferring decomposition until prerequisite results become available, while local Orchestrators schedule workers to execute each leaf subtask. Results propagate upward under \textbf{AND} semantics, and accumulated findings inform a rebuilt task network when the current decomposition cannot resolve the task. On five benchmarks spanning web research, scientific reasoning, and research workflows, HTN-Orchestrate outperforms ReAct, Agent Team, and DeepSeek Harness using the same base model, achieving 89.73% accuracy on BrowseComp and 73.44% on SUPERChem, exceeding Agent Team by 2.45 and 4.69 percentage points, respectively.

---


### 260. [Hy-Memory-30B-A3B: Attributed Reinforcement Learning for Long-Term Memory Writing](https://arxiv.org/abs/2610.22196)

**<font color=#1a73e8>作者：</font>** Tianxiang Fei, Jiazheng Kang, Mao Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> External-memory systems extend language-model applications beyond a context window, but their quality depends critically on the model executing the write path: deciding what to retain, how precisely to represent it, and how new evidence should update persistent state. Existing frameworks typically place a general-purpose large language model behind framework-specific prompts. This raises serving cost, and a writer specialized for one protocol does not transfer directly to another; a unified model that can operate across established memory frameworks remains largely unexplored. We present Hy-Memory-30B-A3B, a compact long-term-memory writer trained across Mem0, MemOS, and Hy-Memory. Memory On-Policy Distillation teaches framework-specific write protocols on student-generated states; Memory RL then optimizes downstream answerability using dense per-chunk probes, attributed cross-chunk rewards, over-storage controls, and chunk-level GRPO. Carrying policy-written banks across windows keeps training aligned with deployment. On fixed 20% benchmark subsamples, Hy-Memory-30B-A3B ranks first on all four evaluated harnesses, including held-out EverMemOS, with a 55.49% macro average versus 54.62% for Claude Opus 5.

---


### 261. [OpenGCUA: Toward a Fully Open Stack for Generalist Computer Use](https://arxiv.org/abs/2610.22200)

**<font color=#1a73e8>作者：</font>** Hanzhang Zhou, Long Li, Quyu Kong 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computer use has reached a turning point: the focus is expanding from GUI-only interaction to systems that complete tasks on users' computers through visual and programmatic interfaces. We define a generalist computer-use agent (GCUA) as a system in which the model chooses how to observe, act, and organize its work across visual and programmatic interfaces. Yet frontier implementations, such as GPT-6 Astra's computer-use system, remain largely closed, limiting systematic study of their design. We introduce Open Generalist CUA (OpenGCUA), an ongoing project to develop and open the full stack for GCUAs with the community. This report presents the first release of OpenGCUA. Code execution is a key feature of our agent design: it lets intermediate results determine subsequent operations and enables models to apply their existing programming capabilities directly to computer interaction. We also propose harness-to-model decision transfer, moving selected observations and task-state decisions from fixed harness rules to the model. On OSWorld-v2, our full configuration improves task scores across all eight evaluated models, including GPT-6 Astra and Claude Opus 5, raising mean partial score by +19.6 points and reducing reported steps per task by an average of 53.0% relative to batched GUI-only execution. We release our implementation and prompts, evaluation trajectories from all eight models, and preliminary versions of a real-device harness and a cross-device SDK. The harness addresses real-device challenges not fully captured by benchmarks, while the SDK provides a common programming interface across computers, mobiles and browsers. Across four real macOS tasks under our real-device harness, selected Qwen3.8-Max runs use 19.4 times as many reported reasoning tokens as GPT-6 Astra, highlighting substantial differences between models in real-device execution efficiency.

---


### 262. [Beyond Downstream QA: Rethinking How We Evaluate Agent Memory](https://arxiv.org/abs/2610.22209)

**<font color=#1a73e8>作者：</font>** Sebastian-Antonio Toma, Jean de Kernier, Mike Ply 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent memory benchmarks evaluate whether an agent's responses reflect correct knowledge, measuring downstream question-answering accuracy as a proxy for memory quality. We show this evaluation paradigm is incomplete: it conflates memory correctness with retrieval and generation quality, producing both false positives where correct responses mask broken memory and false negatives where incorrect responses blame correct memory for retrieval failures. We introduce FEB-30, a benchmark of 30 fact-evolution trajectories spanning 6 diagnostic categories and 3 difficulty levels, constructed via paradigm inversion: documents are generated from known fact trajectories, yielding deterministic ground truth without human annotation. Each trajectory defines how a fact should evolve across multi-author artifacts (documents, emails, conversations), enabling direct inspection of the memory store after each ingestion step. Applying FEB-30 to a representative memory system, we demonstrate that intrinsic and extrinsic evaluation diverge by an average of 16 percentage points, with 44% of trajectories exceeding meaningful divergence thresholds. Diagnostic decomposition reveals that the system correctly classifies memory operations (create, update, reinforce, supersede) only 20% of the time, a failure entirely invisible to extrinsic evaluation, and that failure modes differ systematically by category and difficulty. We release the benchmark, document generation pipeline, and scoring framework to support reproducible evaluation of agent memory systems.

---


### 263. [Skill-Decoupled On-Policy Expert Distillation for Unified Vision-Language Models](https://arxiv.org/abs/2610.22217)

**<font color=#1a73e8>作者：</font>** Yuqi Xiong, Chunyi Peng, Zhipeng Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) can elicit specialized visual capabilities in vision-language models (VLMs), yet jointly optimizing heterogeneous objectives often introduces cross-capability gradient conflicts. Training experts independently mitigates this interference, but direct reward optimization may entangle specialized knowledge with reward-hacking biases. This paper proposes Skill-Decoupled On-Policy Expert Distillation (SCOPED), which trains capability-specific experts and extracts explicit skills through reward-guided reflection. During on-policy distillation, these skills guide expert supervision while remaining unavailable to the unified student, encouraging it to internalize procedural knowledge without explicit skills at inference time. Across eight multimodal benchmarks, SCOPED consistently outperforms the backbone and mixed-capability RL, demonstrating the effectiveness of skill-decoupled on-policy expert distillation for integrating independently acquired capabilities. Further analyses reveal interference during joint capability optimization and suggest that skill augmentation promotes more consistent expert trajectories, greater attention to task-relevant visual evidence, and better preservation of specialized expertise in the unified student. All code and data are available at this https URL.

---


### 264. [WaveLLM: Wavelet-Domain LLM Entropy Modeling for Lossless Image Compression](https://arxiv.org/abs/2610.22232)

**<font color=#1a73e8>作者：</font>** Yue Yu, Bowei Kang, Changsheng Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lossless image compression fundamentally relies on accurate entropy modeling, driving a recent shift toward large language model (LLM)-based methods. However, existing approaches mainly emphasize the modeling capacity of LLMs while directly serializing images into pixel or residual sequences, leaving heterogeneous signal patterns entangled within a single prediction stream. In this paper, we argue that effective entropy modeling depends not only on model capacity, but also on the predictability of the input representation. Motivated by this insight, we propose WaveLLM, a wavelet-domain LLM-based entropy model for lossless image compression. By decomposing an image into multi-level wavelet subbands, WaveLLM converts a heterogeneous prediction problem into a set of more structured and statistically homogeneous subproblems that are more amenable to autoregressive probability estimation. To bridge numerical coding symbols with the LLM's native text token space, we introduce a dedicated numerical interface featuring value embeddings and a coefficient prediction head. Furthermore, a task-adaptive prompting strategy is designed to enable a single shared model to adapt to diverse subbands within a unified framework. Built on Llama-3.2-3B with LoRA adaptation, WaveLLM achieves 2.51, 2.24, and 2.27 bpsp on Kodak, this http URL, and DIV2K, respectively, outperforming the PixelCNN-based codec using the same wavelet transform by 0.43, 0.36, and 0.46 bpsp, and surpassing recent LLM-based lossless compressors on all three benchmarks.

---


### 265. [OS-Helix: Unifying GUI Interaction and Code Execution in Native Computer-Using Agents](https://arxiv.org/abs/2610.22234)

**<font color=#1a73e8>作者：</font>** Bowen Yang, Kaiming Jin, Zichen Ding 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real desktop automation is neither purely visual nor purely programmatic. Agents must understand user-facing interfaces while efficiently manipulating files, scripts, and system state. However, native GUI/code coordination cannot be obtained by prompt-level tool composition. In our preliminary experiments, naively adding a code tool degrades a GUI agent, revealing that GUI/code routing must be internalized through training on high-quality hybrid data. We present OS-Helix, an end-to-end trained multimodal computer-using agent that unifies GUI actions and code execution in one action space. To construct the required supervision, we introduce application-artifact composition, pairing desktop applications with authentic file artifacts to instantiate executable Ubuntu states, and a decoupled instruction/evaluator generation pipeline that produces environment-grounded tasks whose final states can be verified regardless of the solution modality. We cold-start the policy with SFT on filtered hybrid data and further improve it through online RL in live desktop environments. For RL, we propose Step-balanced GSPO, which aggregates importance weight by action step rather than raw assistant tokens to prevent long code actions from dominating heterogeneous-action optimization. On OSWorld-Verified, OS-Helix-27B and OS-Helix-35B-A3B achieve relative improvements of 35.0% and 33.7% over their matched Qwen3.5 hybrid baselines, while OS-Helix-27B-RL further improves by 42.9% to reach 66.44% success. Ablations provide evidence consistent with contributions from learned GUI/code coordination, scalable verifiable supervision, and action step balanced optimization, while demonstrating cross-platform transfer on WindowsAgentArena. Our project homepage is at this https URL.

---


### 266. [Training-Free On-Policy Distillation](https://arxiv.org/abs/2610.22236)

**<font color=#1a73e8>作者：</font>** Bangji Yang, Jiajun Fan, Zhaoyu Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation consolidates specialist models into one student at the price of rollouts, teacher passes and gradient steps for every teacher. We show that the consolidation does not need training: with forward passes only, the capabilities of separately tuned specialists can be aggregated into one model that is, on average, more accurate than either specialist alone. When specialists share a base model, distillation has an exact layer-wise solution: each linear layer of the fused model must reproduce every specialist's output on the inputs that specialist receives while reading its own answers, a least-squares problem whose solution needs only the second moments of those inputs. One forward pass over a few hundred rollouts provides them. We call this training-free on-policy distillation (\method). What the rollouts contain matters more than the solver: answers truncated in repetition loops are few among a mathematics specialist's rollouts but carry a large share of their tokens, and removing them lifts the fused model on AIME25 from task arithmetic's level to the specialist's at matched precision. On Olmo~3 7B, a few GPU-hours of forward computation per specialist yield a generalist that keeps most of each specialist's gain on each of seven mathematics and code benchmarks.

---


### 267. [Language Is a Security Surface for Agent Guards](https://arxiv.org/abs/2610.22244)

**<font color=#1a73e8>作者：</font>** Hasan Demirkiran, Jens Ernstberger  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Step-level guards decide, before each tool call, whether an agent's next action is safe given the user's request and the trajectory so far. Users write those requests in many languages, while guard prompts and the benchmarks on which purpose-built guards are trained and evaluated are English. We ask whether a guard's verdict depends on the language of the request. We build LinguaGuardBench from the 1,220 labelled steps of TS-Bench AgentDojo-Traj: we translate only the user instruction into German, French, Turkish, Swahili and Amharic, and keep every tool call, observation and label byte-identical, so any change in a verdict is attributable to language alone. Six English rewordings and a whitespace placebo serve as controls, and managed guards are run three times to measure their noise. Across 19 guards, from frontier APIs to 4B open models and four purpose-built agent guards, most open, small and purpose-built guards change verdicts under translation beyond their own noise floor, and the effect grows with the rarity of the language: among the nine guards below 13B parameters, the mean placebo-adjusted flip rate rises from +1.5 pp on French to +4.4 pp on Amharic. Purpose-built guards are the most sensitive. The direction of the damage tends to follow guard size: open guards of 12-30B parameters block more benign steps (up to +5.0 pp false positives), and every significant loss of recall is in a guard below 10B (up to -7.4 pp). Frontier guards shift by at most about one point; the strongest, Gemini 3.8 Flash, returns identical verdicts with and without the request. The damage is concentrated in a few instructions and, in a post-hoc analysis, falls on steps where the agent's reasoning restates the English request, consistent with guards reacting to inconsistency between channels. English paraphrase moves every guard less than translation does. We release the benchmark and all 489k verdicts.

---


### 268. [Disagreement-Guided Weak-to-Strong Routing](https://arxiv.org/abs/2610.22245)

**<font color=#1a73e8>作者：</font>** Sima Noorani, Shayan Kiyani, George Pappas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Small language models are increasingly deployed on edge devices and robotic systems to meet cost and latency constraints, yet their limited capabilities can make reliable deployment challenging. Stronger models can provide assistance when needed, but deciding when to route a weak-model response to a stronger model often relies on signals of response correctness. In open-ended and agentic tasks, however, obtaining such signals can require costly ground-truth supervision that is difficult to obtain at scale. We revisit the foundations of weak-to-strong routing and ask whether routing decisions can instead be guided by signals that do not require ground-truth supervision. We first characterize the optimal weak-to-strong routing policy, while allowing for multiple weak-model responses generated through local inference. Building on this characterization, we derive a principled approximation to the optimal routing based on model-to-model comparison. In particular, we introduce a notion of model disagreement that can be measured directly from model-generated responses, without ground-truth supervision. Importantly, the approximation becomes increasingly accurate as the strong model becomes a better proxy for the ground-truth distribution. Across agentic and single-turn tasks, our approach effectively navigates the trade-off between routing cost and response accuracy without ground-truth supervision. Moreover, even when ground-truth correctness signals are available for training, disagreement-based routing can outperform methods trained directly to predict correctness

---


### 269. [Not X, but When: Diagnosing a Mandarin LLM Writing Tic through Contextual Appropriateness](https://arxiv.org/abs/2610.22249)

**<font color=#1a73e8>作者：</font>** Yihang Peng, Yi Jing, Dewen Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recurring expressions in model-written text are often treated as signatures of machine authorship, yet most of them serve legitimate functions. Whether such an expression is a tic depends on whether the model knows when it is called for. This judgment of appropriateness, central to communicative competence, remains largely unexamined for language models. We study it through the Mandarin corrective construction bushi X, ershi Y ("not X, but Y"). Drawing on Gricean pragmatics and corrective negation, we introduce a decision tree that classifies uses as substantive, optional, or defective by testing whether the context makes X a live alternative and whether rejecting X is informative. Five commercial models use the construction 2.5 to 9.2 times as densely as a human reference. Of 307 annotated uses, only 1.30% are defective while 52.8% are optional, that is, correct but unneeded, so models fall short in appropriateness far more often than in correctness. Several reward models favor the construction even over quality-matched variants, an LLM judge favors it even where the context does not license it, and both supervised fine-tuning and preference optimization tend to raise its frequency in open-weight models. We hope this work encourages the development of models attentive to the appropriateness of their expressions.

---


### 270. [BitSparse: Compact Activation Storage for ReLU Feed-Forward Networks](https://arxiv.org/abs/2610.22256)

**<font color=#1a73e8>作者：</font>** Max Zhu, Bohang Sun, Pietro Lio 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reducing memory use in large language model (LLM) training is an ongoing challenge. Activation checkpointing saves memory by recomputation, while lossy compression changes the stored activations. The reemergence of sparse $\relu$ and $\relu^2$ activations creates a third opportunity: losslessly compressing the activation cache itself. We present BitSparse, a GPU-resident lossless compression format for sparse activations. Compression and reconstruction run in custom Triton kernels fused into an autograd function, shrinking the activation cache while recovering it exactly for the backward pass. Bfloat16 (BF16) and FP8 activations are supported. Optional sign-bit packing further increases compression up to close to the theoretical limit. We analyze its compression ratio and compare it to the theoretical optimum. BitSparse lowers per-token VRAM by 31\% and 30\% Modded-NanoGPT and Nemotron-H respectively, with overheads of no more than 1\% at practical sequence lengths. Additionally, a new preallocated buffer system avoids host synchronization during training when variable size tensors are allocated.

---


### 271. [Baselines and Score Centering in Policy Gradient Estimation](https://arxiv.org/abs/2610.22263)

**<font color=#1a73e8>作者：</font>** Shuo Han, Ziqing Hu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has become a widely used approach to post-training large language models. In a typical implementation, learning is off-policy: The policy generating the responses differs from the policy being trained because of training-inference mismatch or policy staleness in asynchronous training. This discrepancy is commonly addressed by importance sampling, whose ratio is usually regularized in practice through truncation, masking, or clipping. Under regularized importance sampling, the importance-weighted policy gradient is no longer invariant to constant shifts in the reward. This invariance is recovered by using the covariance between the reward and the importance-weighted score as the estimand, which coincides with the policy gradient when the ratio is not regularized. This note develops this covariance perspective for both sequence-level and token-level importance sampling. The covariance perspective reveals the roles of the group-mean baseline and score centering in policy gradient estimation. Both perform centering in covariance estimation, but they differ in the mean being subtracted: The group-mean baseline uses a sample mean, whereas score centering uses a population mean. The two lead to distinct unbiased covariance estimators with different variances. Whether both forms of centering should be used simultaneously depends on whether importance sampling is applied at the sequence level or at the token level. With sequence-level importance sampling, score centering adds no benefit once the group-mean baseline is used; with token-level importance sampling, using the group-mean baseline without score centering generally introduces bias when the importance ratio is regularized.

---


### 272. [SCOPE: Semantic Bounded Credit Optimization for Prompt Engineering in Text-to-image Generation](https://arxiv.org/abs/2610.22264)

**<font color=#1a73e8>作者：</font>** Yufei Jiao, Jinfa Huang, Zeyue Xue 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) enables language models to improve text-to-image (T2I) generation by rewriting prompts for a frozen image generator. Existing methods typically apply a single signal derived from the image to individual subword tokens, although objects, counts, attributes, and relations form coherent semantic spans. We propose SCOPE, an objective based on Group Relative Policy Optimization (GRPO) that aligns update weighting with this structure. The rewriter jointly generates an enhanced prompt and its semantic partition. SCOPE pools shifts in policy log probabilities within each span to derive a shared coefficient for its token losses while retaining a single advantage for each completion. It requires neither separate span rewards nor additional image renders. Across Qwen-Image, SD3, and FLUX.1-dev, SCOPE achieves average relative gains over vanilla GRPO of 9.48% on GeneVal and 7.62% on T2I-CompBench. Ablation studies show that both semantic boundaries and pooling within spans contribute to these gains, supporting semantic structure as a practical inductive bias for prompt engineering with RL.

---


### 273. [X-RIC: An Agentic RAN-Intelligent Controller Benchmark for Enhancing Reinforcement Learning](https://arxiv.org/abs/2610.22269)

**<font color=#1a73e8>作者：</font>** Adhwaa Al-Chaab, Ayman Younis, Dario Pompili  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The O-RAN ALLIANCE introduces architectural flexibility through disaggregation and AI-driven control. While the RAN Intelligent Controller (RIC) enables centralized optimization, current AI approaches lack reasoning capabilities and explainability. We propose eXplainable RIC (X-RIC), a novel framework integrating agentic AI into O-RAN architectures. X-RIC combines reactive Reinforcement Learning (RL) with strategic agentic reasoning through: (i) automated Behavioral Cloning (BC) using domain heuristics for sample-efficient training, (ii) a Telecom Language Model (TLM), a transformer-based reasoning module providing contextual abstraction and interpretability, and (iii) closed-loop co-adaptation within the Near-RT RIC control loop enabling continuous policy refinement. To ensure deployment readiness, we introduce BARX (Benchmarking Agentic Reasoning for RAN), a domain-specific evaluation framework assessing agentic control across latency, compliance, and determinism metrics. We validate X-RIC on SLA-aware network slicing in simulation and O-RAN-compliant testbed deployments. X-RIC achieves 89% operational cost reduction while maintaining SLA compliance, converging 75% faster with 50% fewer training steps and 46% lower variance.

---


### 274. [Librarian Agents: Training LLMs to Curate Long-Context Workspaces that Anticipate Future Queries](https://arxiv.org/abs/2610.22273)

**<font color=#1a73e8>作者：</font>** Anikait Singh, Teresa Zhang, Yoonho Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning over long document contexts remains a challenge for large language models (LLMs). Standard retrieval methods are inherently reactive, bottlenecking agents with complex, cross-document reasoning at inference time, while precomputed structures like knowledge graphs often fall short because they rely on rigid heuristics. Instead, can we allow agents to perform anticipatory directed curation: learning to proactively reorganize unstructured corpora prior to inference to efficiently serve diverse future queries. We build on a key asymmetry in modern agentic harnesses (e.g., Claude Code): while LLM agents are adept at navigating existing filesystems to solve an immediate task, they are rarely trained to construct reusable workspaces for future use. To instantiate this capability, we introduce Librarian Agents, a framework in which a builder agent transforms raw documents into a hierarchical filesystem of synthetic files and reference links, which forms a workspace tailored for a downstream answering agent. We formulate workspace construction as a Markov decision process and optimize the builder policy via reinforcement learning to directly maximize downstream answering accuracy. Empirically, Librarian Agents outperforms the strongest retrieval and precomputation baselines by 33 percentage points on BrowseComp-Plus, amortizes upfront construction costs across repeated queries, and generalizes zero-shot to unseen domains on BRIGHT with a 31-point average accuracy improvement.

---


### 275. [MJev-Spatial: System One Spatial Intelligence via Native Attention Matching](https://arxiv.org/abs/2610.22276)

**<font color=#1a73e8>作者：</font>** Luozheng Qin, Yuhan Zhu, Changhai Zhou 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial intelligence lets an agent perceive and act in the physical world, and many of its judgments must be made at interaction rates: which spatial relation holds, how far an object is, or where to place it. Vision-language models (VLMs) produce these answers by free-form text generation, paying for autoregressive decoding and answer parsing even though the output space is compact: one of a few options, a scalar, or a 2D point. In light of this, we introduce MJev-Spatial, a System 1 multimodal decision model that tackles all three types of spatial understanding tasks within a unified classification framework. Specifically, MJev-Spatial treats each candidate as a class and scores it using the backbone's pretrained query and key projections, without adding parameters. The candidates are the given options for choice tasks, or value bins and image regions refined through coarse-to-fine classification for numerical and point prediction, respectively. At inference, each classification decision takes a single forward pass and generates no answer tokens. To train on heterogeneous spatial data efficiently, we supervise all coarse-to-fine stages jointly with teacher forcing in one forward pass, and combine this with length-aware global batching and cross-GPU load balancing, raising training throughput by 30.8% over the original batching strategy. Built on Qwen3.5-4B and trained on 12.3M question-answer pairs converted from existing spatial datasets, MJev-Spatial achieves the highest overall score (65.64%) among eight tested models, ranks first on seven of twelve benchmarks, and outperforms its unmodified autoregressive base model on all twelve, while running 2.5 times faster than the fastest autoregressive baseline and 5.6 times faster than the base model.

---


### 276. [LEASH: Uncertainty-Aware Weak-to-Strong Escalation and Oversight for Computer-Use Agents](https://arxiv.org/abs/2610.22280)

**<font color=#1a73e8>作者：</font>** Qingni Wang, Changdae Oh, Yuzhe Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-use agents increasingly tackle long-horizon tasks, where running a frontier model at every step is expensive and a small open-weight model alone often fails. Weak-to-strong escalation offers a middle ground where a weak agent acts by default and hands control to a strong one only when needed. The core challenge is deciding when to escalate, which requires an uncertainty signal cheap enough to check at every step. However, even after handoff, the strong agent can still get lost, but a black-box API that the strong agent is usually served exposes no internals to monitor. To this end, we propose LEASH, a training-free framework that unleashes the strong agent only when the weak agent's latent uncertainty signals it is needed, and keeps it on a leash afterward. LEASH has three layers: (1) initial task uncertainty for early routing, (2) step-level uncertainty for runtime escalation, and, after handoff, (3) a shadow observer for continued oversight of the strong black-box agent. Here, we use latent uncertainty as a fuel for all three layers. Specifically, we compare the weak model's hidden states with those from its past successful and failed trajectories, and a state that looks more like the failures signals higher uncertainty. During weak-agent execution, our uncertainty estimator reuses activations already produced during action generation, so it needs no extra forward pass or dedicated monitor training. Experiments on OSWorld across four contemporary model backbones show that LEASH consistently improves over standalone weak agents and outperforms random escalation by 6.55--11.94 points at matched escalation rates. With Qwen3.5-35B-A3B, LEASH achieves 73.66% task success at $0.4117 per task, matching always-on Claude Opus 5 (72.90%) while reducing inference cost by 19.2%.

---


### 277. [Improving Environment-Agnostic Coding Agents: The Role of Scaffolding](https://arxiv.org/abs/2610.22289)

**<font color=#1a73e8>作者：</font>** Sergey Rodionov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Stronger language models may increasingly construct useful procedures for themselves, reducing the advantage of developer-supplied scaffolding. We investigate why this advantage persists and whether an environment-agnostic agent can be improved without environment-specific engineering. We evaluate a Codex-based agent in two nearly identical prompt variants on ARC-AGI-3, AGI Maze, and Terminal-Bench. Each variant is deployed with unchanged code, prompts, and general-purpose tools across environments, receiving environment-specific information as input. Changing only an instruction to encourage reporting difficulties and returning control for automatic continuation improves mean scores on both ARC-AGI-3 and AGI Maze, while Terminal-Bench shows small, mixed changes. Yet the general agent remains below an ARC-AGI-3-specific reference, including with GPT-5.6-sol. The reference prescribes organization and control rather than supplying new game rules or solutions. To investigate this gap, we transfer reset decisions to a scripted controller that follows a convention already given to the agent. This small change recovers part of the specialized agent's advantage. A complementary AGI Maze experiment shows that additional tutorial experience can reduce performance. Together, these findings highlight the distinction between having information and tools available and using them effectively. Supplied procedures still matter for the models tested here. The performance gains also come with higher token-based cost. The experiments do not separate better use of information and procedures from additional or differently allocated inference. We provide the EnvTraverse framework and an evaluated baseline agent for testing whether further environment-independent changes improve performance in some environments without degrading it in others.

---


### 278. [EliteReplay: Preserving Diverse Solutions in RL Post-Training via Quality-Diversity Search](https://arxiv.org/abs/2610.22290)

**<font color=#1a73e8>作者：</font>** Hanane Nour Moussa, Doeun Lee, Sachin Kumar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has become a common post-training technique to improve the accuracy of LLMs on verifiable tasks. However, such training can narrow the set of solutions the model can produce. Several approaches have attempted to address this behavior-sharpening effect, but they often optimize metrics that do not reflect the diversity of correct solutions. Ideally, we want a model that can produce multiple good solutions, not only a single reliable one. We propose EliteReplay, a post-training recipe that pairs GRPO with an "elite" archive built by quality-diversity search. Before training, we use the frozen base model to collect solutions that span distinct approaches; during training, GRPO is combined with a replay loss on this archive. The result is a post-trained model that improves accuracy while preserving more of the base model's solution diversity. On multiple text-to-SQL tasks, EliteReplay achieves a higher pass@128 than all baselines, producing up to 77% more distinct correct strategies than the strongest baselines. It preserves most of the base model's correct strategies, outperforming existing methods in strategy retention. This diversity translates into practical benefits on ambiguous questions, where EliteReplay covers both interpretations nearly twice as often as the strongest baseline on AmbiQT.

---


### 279. [CAT-alyzing Honesty: Continuous Adversarial Training for Transferable LLM Honesty](https://arxiv.org/abs/2610.22292)

**<font color=#1a73e8>作者：</font>** Yuan-Chen Chang, Niklas Herbster, Gauthier Gidel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are becoming prevalent in scenarios where honesty is critical. However, despite alignment training, these models still exhibit dishonest behaviour, such as outputting claims that contradict some knowledge or are not supported by what is accessible in context. We introduce Continuous Adversarial Training for Consistent Honesty (CATCH), inspired by a method originally developed to robustly refuse harmful queries. CATCH trains the model towards an honest answer and away from a dishonest one while maintaining the model's capabilities. We evaluate two architectures (Llama-3.3-70B-Instruct and Qwen3-3.6-27B). We show that trained with only hundreds of targets built from self-reporting scenarios, CATCH learns an honest behaviour that robustly generalizes and transfers across distinct benchmarks. It consistently reduces dishonesty under pressure on MASK, increases confessions in the multi-agent game of Among Us, and improves the discovery rates of the model's hidden behaviours in AuditBench. We show that CATCH outperforms prompting and supervised fine-tuning in improving honesty, and it is on par with state-of-the-art honesty activation steering. However, CATCH surpasses honesty steering in maintaining utility, thanks to a novel choice of utility data.

---


### 280. [Towards Continual Learning: Mitigating Forgetting With Subspace Tuning](https://arxiv.org/abs/2610.22293)

**<font color=#1a73e8>作者：</font>** Arnav Chavan, Kusha Sareen, Rishabh Tiwari 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) acquire new skills through fine-tuning, but it can destroy capabilities they already have: catastrophic forgetting remains a central obstacle to continual learning in LLMs. Recent works connect forgetting to how far, and along which directions, fine-tuning moves the weights. On-policy methods such as reinforcement learning and on-policy distillation avoid updating the principal singular directions of weight matrices and thus forget less. In contrast, SFT concentrates updates along these directions and is susceptible to catastrophic forgetting. In this work, we introduce Subspace Tuning (SST), which restricts each weight update to the bottom singular subspace, eliminating changes along the principal directions. SST is optimizer-agnostic and composes well with fine-tuning recipes including SFT and self-distillation. SST combines tight subspace protection, dense gradient estimation, and a simple refresh mechanism, enabling stronger learning than prior orthogonal fine-tuning methods. With these mechanisms, protecting as much as 99\% of the weight subspace substantially improves retention while preserving strong target-task performance. This behavior strengthens with model and data size and nearly eliminates forgetting in the large-model regime. SST also keeps the model close to its base distribution, inducing $2$--$4\times$ less KL drift than the baseline recipes. Overall, SST advances the learning--forgetting Pareto frontier, making it a practical default for fine-tuning pre-trained language models.

---


### 281. [Multi-Target Few-Shot Prompting with Diffusion Language Models](https://arxiv.org/abs/2610.22294)

**<font color=#1a73e8>作者：</font>** Anton Xue, Alan Li, Rahul Saha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Few-shot prompting is useful when instructions and rewards are hard to specify. One such application is editing by example, where a demonstrated formatting change or API migration may need to be applied across multiple sites. However, such edits often depend on both left and right context, making generation with causal autoregressive models awkward. We therefore introduce multi-target few-shot prompting with diffusion language models, where examples guide the infilling of multiple masked regions within a shared canvas. To address the known challenge of reliably following demonstrations in few-shot prompting, we further leverage selective masking of the canvas to derive a likelihood-ratio reward that favors example-supported infills. Across few-shot prompting benchmarks and software refactoring case studies, we find that demonstrations improve infilling accuracy, with example guidance yielding further gains in several settings.

---


### 282. [Grounded Human-Attributed Description and Activity Recognition in Videos](https://arxiv.org/abs/2610.22295)

**<font color=#1a73e8>作者：</font>** Jay N. Paranjape, Jurijs Nazarovs, Rohan Sarkar 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding characteristics and activities of individuals in complex multi-person environments is crucial for real-world applications. However, existing datasets often simplify this problem to grounded group activity recognition, single-person activity recognition, or close-set activity recognition, thus limiting the generalizability of models trained on these datasets. In this work, we introduce the task of Grounded Human-Attributed Description and Activity Recognition (GHADAR), which involves describing the characteristics and activity descriptions of \textbf{every} person in a video, provided the location of the person in the video, which is more practical for real-world applications. To facilitate this, we introduce a new dataset derived from AVA-Actions by generating open-set captions for the person description and activity. In addition, we propose a novel method to effectively utilize the information contained in grounding during training by constraining the cross-attention masks during training in VLMs to improve performance for this task. Our experiments show that our method outperforms SOTA VLMs on this task. Finally, we demonstrate the limitations of existing evaluation metrics, which are overly reliant on human-annotations and exact text-text matching. As an added video-based evaluation, we propose a holistic VLM-based evaluation schema that compares concepts {\em directly} between the video and the generated predictions. Thus, in this work, we develop a complete framework for GHADAR, including a dataset, a novel method and an evaluation schema, thereby establishing a strong foundation for future research in this domain.

---


### 283. [Private Retrieval Augmented Generation via Random Projection](https://arxiv.org/abs/2610.22297)

**<font color=#1a73e8>作者：</font>** Dixi Yao, Tahseen Rabbani, Tian Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) enhances the capabilities of large language models (LLMs) by querying external structured knowledge. However, it can also introduce privacy risks by leaking sensitive information from the retrieval datastore. We propose a simple method to preserve datastore privacy in RAG systems via random projection. By applying the same projection to both datastore embeddings and query embeddings, our method provably preserves semantic similarity between queries and retrieved items while substantially mitigating data extraction attacks. Across multiple RAG architectures and datasets, we show that this lightweight approach achieves superior retrieval and generation performance compared to prior methods which leverage formal differential privacy (DP) guarantees, while exhibiting comparable empirical privacy under strong attack models. Our results for the first time suggest that random projection can serve as a competitive and practical baseline for privacy-preserving RAG systems.

---


### 284. [AI Consilium: a Benchmark of LLM Clinical Multidisciplinary Second Opinions](https://arxiv.org/abs/2610.22298)

**<font color=#1a73e8>作者：</font>** Alexey A. Bokov, Ivan I. Panin, Nikolay B. Nechaev 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can generate differential diagnoses for complex cases, but a useful second opinion must also be factually grounded, clinically coherent, actionable, and safe. We developed a multidimensional benchmark using 300 diagnostically resolved NEJM--MedQA cases: 110 for physician reference ratings and Judge calibration and 190 for held-out evaluation. Eight single-model pipelines generated independent role-specific opinions and interactive-consilium reports under free-form and structured clinical-reasoning conditions. A physician-calibrated LLM Judge evaluated 3,040 final reports and the corresponding structured primary-role outputs. Model identity separated report quality more strongly than response format. Structured final reports had higher overall mean scores in seven of eight model pipelines, with their clearest advantage in management (2.740 vs. 2.436). Compared with the structured pre-consilium primary-role opinion, the complete structured synthesis had higher pooled scores across all five shared criteria, with the largest increases in problem prioritization, factual grounding, and reasoning coherence. GPT-5.6-Sol led every evaluated component and reached consensus in the fewest review rounds. These findings show that the benchmark can distinguish model capability, the contribution of multidisciplinary synthesis, criterion-specific effects of response structure, deliberation dynamics, and inference requirements within one common-case evaluation.

---


### 285. [Knowledge That Is Linear Before Fine-Tuning Generalizes After It](https://arxiv.org/abs/2610.22300)

**<font color=#1a73e8>作者：</font>** Faridoun Mehri, Hinrich Schütze  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Not all facts a language model can recall support further learning equally well. We distinguish active facts, which support generalization beyond their own recall, from inert facts, which can be recalled but do not support such generalization in a given task. We study this distinction by constructing new relations from existing ones. Take the relation that maps a place to its continent (Paris -> Europe) and assign each of its answers an arbitrary new label (Europe -> crab, Asia -> zebra). The new relation then maps Paris -> crab. We fine-tune the model on the new relation for a subset of subjects, without telling it the original relation or the relabeling rule, and test whether it assigns the corresponding labels to held-out subjects that share an answer in the original relation. Having learned Paris -> crab, does it answer Munich -> crab? Across eleven language models and 70 relations, how linearly readable the original relation is in pretrained representations strongly predicts this generalization. Within each model, the two correlate across relations at Pearson r = 0.87 to 0.92. This association persists when controlling, separately and jointly, for the number of fine-tuning subjects and answers, the model's accuracy on the original relation, and how often the subjects occur in pretraining text. It is also robust to re-randomizing the label assignment and fine-tuning seed, and to replacing the animal labels with labels from thirteen other semantic categories. When we map a fine-tuned model's wrong label back to the original answer it was assigned to, Munich -> zebra becomes Munich -> Asia. Answers recovered this way are more often among the linear probe's top answers for the subject than among the pretrained model's own. Whether a new relation generalizes depends less on whether its facts can be recalled than on how readily their shared structure can be read out linearly.

---


### 286. [Grid-Bench: Can LLMs Predict How Discrete Worlds Change?](https://arxiv.org/abs/2610.22312)

**<font color=#1a73e8>作者：</font>** Zixiang Xu, Zirui Song, Wanrong Zheng 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Spatial instructions describe how to move objects, transform regions, or modify their surroundings. When several operations are applied in sequence, each acts on a configuration shaped by earlier changes. How accurately can large language models (LLMs) predict the resulting spatial state? We introduce Grid-Bench, an executable benchmark in which eight families of operations transform discrete worlds represented as two-, three-, and four-dimensional grids. Given an initial grid, explicit rules, and an event history expressed as text, a model predicts the complete final grid. Reference execution makes every predicted value checkable, supporting comparisons across spatial operations, history lengths, and workloads. Evaluating six LLMs shows that complete-state accuracy falls sharply as histories grow, with substantial divergence among models that perform similarly on single events. Models with similar exact-match accuracy can nevertheless differ substantially in the number of incorrect cells on shared instances. Even over long histories, some models recover many correct changes beyond what copying the initial state would yield. Grid-Bench makes both complete recovery and these differences in returned states directly measurable across a range of spatial conditions.

---


### 287. [MindEval2: Clinically Grounded Patients and Rubrics for Evaluating Language Models in Mental Health Support](https://arxiv.org/abs/2610.22314)

**<font color=#1a73e8>作者：</font>** John Mendonça, Daniel Tschernutter, José Pombal 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With people increasingly turning to AI chatbots for mental health support, the need to evaluate these tools is becoming more pressing. Recent benchmarks attempt to mimic a realistic setting by simulating multi-turn interactions with synthetic patients and evaluating them with an LLM-as-a-judge. However, the usefulness of these methods is limited because simulated patients can be overly forthcoming and self-reflective, and judgments typically involve opaque Likert scales with unclear practical utility. To bridge these gaps, we introduce MindEval2, an evaluation framework that consists of two components: Mental Health Quality Rubrics (MHQR), for evaluation, and MindSim, for patient simulation. For MHQR, we collaborate with PhD-level psychologists to develop a set of rubrics that break down response quality into explicit operational criteria that are more interpretable and actionable than existing evaluation taxonomies. MindSim, in turn, is an LLM harness that combines carefully-designed patient profiles with tools, enabling more varied, challenging, and realistic interactions than existing baselines. The harness also contains a memory component that is updated between each interaction, enabling MindEval2 to model the longitudinal aspect of mental health. We evaluate 18 proprietary and open-weight models on MindEval2, finding that while frontier models have largely improved on issues related to surface level quality and boundaries, guidance calibration remains the dominant failure mode across all models, accounting for most of the quality gap.

---


### 288. [Learning to Steer LLM Agents and Multi-Agent Systems](https://arxiv.org/abs/2610.22316)

**<font color=#1a73e8>作者：</font>** Leyang Shen, Yaxin Gong, Yang Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based agents and multi-agent systems increasingly tackle complex tasks through long-horizon tool use and inter-agent collaboration. However, these systems are prone to deviating from the overall goal as execution unfolds, which wastes execution resources and leads to undesired outcomes, a failure termed goal drift. In this work, we propose a steering agent that supervises execution on the fly and steers the system back on track when drift occurs. The steering agent observes the execution context, deciding when to intervene with a low-cost fast path and how to intervene with a high-cost slow path. To unlock its steering intelligence, the ability to assess goal drift and generate effective interventions, we jointly train the two paths with reinforcement learning, combining a pairwise ranking objective with group-relative policy optimization (GRPO). Experiments on information-seeking search tasks show that the steering agent provides effective supervision for both single-agent and multi-agent systems, improving their performance and efficiency. The learned steering intelligence generalizes to out-of-domain tasks, transfers to unseen executors, and supports controllable intervention frequency without retraining.

---


### 289. [A team of Gemini 4 Argon agents beats Minecraft](https://arxiv.org/abs/2610.22319)

**<font color=#1a73e8>作者：</font>** Maxence Faldor, Satinder Singh, Roberta Raileanu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We placed four Gemini 4 Argon agents in a sandboxed Minecraft survival world and gave them one goal: defeat the Ender Dragon. Each agent controlled a player via an open-source library called Mineflayer and coordinated with its teammates through in-game chat and shared memory. No one assigned roles or wrote game logic. The agents planned, wrote, and debugged every program themselves. Researchers could watch the run on a live dashboard and pause or stop it at any time, but they had no cause to intervene. Starting from a randomly generated world on Easy difficulty, the team wrote 2,783 programs and defeated the dragon in 27 hours and 14 minutes, dying 605 times along the way. To our knowledge, this is the first end-to-end autonomous completion of Minecraft by AI agents, achieved using only the standard Mineflayer library without pre-scouted seeds or other game-specific tools written by humans. Winning required the agents to keep a coherent plan across thousands of dependent steps for more than a day. Complex real-world software engineering and enterprise tasks demand the same long-horizon coding and multi-agent coordination. We describe the setup, how the run unfolded, the team's strategies (dividing the work, sharing what they learned, recovering each other's items), and the limits of the result.

---


### 290. [Training Reasoning Models to Generate Diverse Scientific Ideas](https://arxiv.org/abs/2610.22324)

**<font color=#1a73e8>作者：</font>** Manya Wadhwa, Pranav Narayanan Venkit, Hiroaki Hayashi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> One of the first steps of a research pipeline is generating ideas. Large Language Models (LLMs) are increasingly used to automate this step, but most of this work optimizes the quality of individual ideas, while overlooking diversity. In our work, we study document-grounded ideation, focusing on increasing the diversity of LLM generated ideas and ensuring they are high quality. Given prior papers, a model must propose a set of ideas that are each high-quality and clearly distinct from one another, while also being grounded in the input documents. To optimize for this, we propose training with a set-level reinforcement learning objective. In our setup, in a single generation, the model writes K structured idea cards grounded in the source papers, and the set is scored jointly, where each idea's quality is weighted by its distance from the ideas written before it. This teaches the model to steer each new idea away from its predecessors. We show that our trained 8B model achieves higher creative utility (a measure combining quality and diversity) than Claude Opus 4.8 and GPT-6 Astra on our contamination-free benchmark. In a pilot human study with four experts, our sets are judged as promising as Claude Opus 4.8's and contain marginally more unique ideas. When a coding agent runs proof-of-concept experiments on the ideas, our model's success@k is comparable to Claude Opus 4.8's, so we see that the added diversity does not cost any executability.

---


### 291. [Twice Upon a Time: Complementary Representations for Time-Series Reasoning](https://arxiv.org/abs/2610.22327)

**<font color=#1a73e8>作者：</font>** Hedi Zisling, Liran Nochumsohn, Ilan Naiman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time Series Language Models (TSLMs) enable language-based understanding and reasoning over temporal data, yet a fundamental question remains: what information should their time-series representations preserve, and what variation should they factor out? Existing TSLMs typically expose the language model to a single representation, imposing a fixed inductive bias across downstream tasks. We instead introduce complementary representations as a design principle for time-series reasoning. Our model combines two visual views: line plots preserve absolute measurements and the observed coordinate frame, while normalized delay embeddings factor out positive amplitude rescaling and offsets while exposing temporal structure. Dedicated visual encoders integrate both views into a shared language model through visual tokens and multi-level feature fusion. Evaluation-time interventions verify that the two views exhibit distinct invariance profiles, while single-view ablations show that their combination is particularly beneficial beyond basic perception, with the large gains in prediction and reasoning. Built on Qwen3-VL-8B, our dual-view model improves overall TSRBench accuracy from 44.5% with line plots alone to 53.2%, substantially exceeding the strongest evaluated dedicated TSLM baseline at 36.7%. It further achieves 89.9% accuracy on TSExam and 86.8% numerical accuracy on multivariate ChatTS alignment. Together, these results demonstrate that complementary representations provide an effective design principle for general-purpose TSLMs, enabling models to exploit temporal structure without sacrificing access to the original measurement frame.

---


### 292. [Designing Transformers for Continuous Diffusion Language Models](https://arxiv.org/abs/2610.22330)

**<font color=#1a73e8>作者：</font>** Weijian Luo, Yujian Chen, Hao Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Continuous diffusion language models (CDLMs) offer an alternative approach to parallel language generation; however, most existing studies directly use transformer architectures from either causal large language models (LLMs) or Diffusion Transformers (DiTs) for image generation, which were not optimized for CDLMs. In this paper, we conduct a systematic study on Transformer architectures for CDLMs and introduce Language Diffusion Transformer (LangDiT), combining feature and query-key normalization, wider noise conditioning, likelihood-shortcut gradient routing and calibration, and confidence-gated training self-conditioning. LangDiT significantly reduces generation perplexity in matched LangFlow comparisons, establishing a new state of the art in continuous language generation across different model formulations. Using LangFlow as a representative CDLM, LangDiT as a plug-and-play backbone leads to a new state-of-the-art model with a generation perplexity (GenPPL) of 21.72 using 1024 NFEs and 44.72 GenPPL using 128 NFEs on the unconditional generation of 1024-token sequences on the OpenWebText dataset. When adapted to Plaid-style CDLM formulations, LangDiT results in a new leading GenPPL of 11.33 using 1024 denoising NFEs, and 27.51 GenPPL using 128 denoising NFEs. These gains are achieved while retaining each model's underlying representation, training objective, and inference sampler, isolating transformer architecture as a fundamental source of improvement. Our study identifies architectural design as an important source of improvement in continuous diffusion language models.

---


### 293. [Evaluation Awareness Beyond English: Do LLMs Act Differently When Tested in Indic Languages?](https://arxiv.org/abs/2610.22333)

**<font color=#1a73e8>作者：</font>** Trizal Garg, Sibayan Mitra, Arya Karanjkar 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can often tell when they are being tested. This ability, known as evaluation awareness, can lead models to act more cautiously during safety evaluations than in real use. Existing work has studied evaluation awareness almost entirely in English, although models serve users in many languages. Indic languages are spoken by over a billion people, yet evaluation awareness remains almost entirely unstudied in them. We test four instruction-tuned models from three families in five Indic languages alongside English. A set of cues varies whether the model is told that it is monitored and whether the monitoring is a safety test. Models refuse harmful requests more often when they are told that they are being tested. This increase appears in all four models and all six languages. In Indic languages, refusal of harmful requests rises by 14.4 percentage points on average. The test cue also brings Indic refusal of harmful requests level with English, but raises refusal of benign Indic requests from 6.9% to 11.3%. We release all 47,880 judged responses to support further work. These results suggest that safety evaluations in Indic languages may not reflect how models treat their everyday users.

---


### 294. [3DCodeVerse: Exploring 3D Worlds as Code](https://arxiv.org/abs/2610.22341)

**<font color=#1a73e8>作者：</font>** Yipeng Gao, Ziyao Zeng, Jinfa Huang 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce 3DCodeVerse, a research ecosystem that enables coding agents to create editable and verifiable 3D content at scale. 3DCodeVerse comprises large-scale, high-quality datasets of executable 3D code, a coding harness for spatial reasoning and automated verification, and practical guidance for 3D coding. First, we construct 3DCodeVerse-2M, a large-scale curated dataset of standalone 3D executable code. We build this corpus by collecting open-source data, converting specialized representations, and generating new programs with coding agents. Each program is packaged with the source files and associated assets required for execution in its declared environment, along with available descriptions and verification records. Second, we develop the 3DCodeVerse Harness, a multi-agent directed acyclic graph framework for generating and refining 3D content. It uses execution checks, spatial measurements, and visual feedback to automatically evaluate and revise generated programs without human feedback during generation. Third, we conduct systematic empirical studies of 3D coding, establishing baselines with fine-tuned open models and deriving practical guidance through component-level analyses of our harness. Extensive experiments demonstrate that fine-tuning on our dataset significantly improves the 3D coding capabilities of open-source models. Notably, our 3DCodeVerse harness achieves a 90% win rate against Claude Design (3D Object) in pairwise human evaluations, when both are utilized by Claude Opus 5.5.

---


### 295. [MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning Engineering](https://arxiv.org/abs/2610.22344)

**<font color=#1a73e8>作者：</font>** Shangheng Du, Jinxin Shi, Shuaiyu Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are expanding from assisting scientific research and engineering to autonomously developing and improving AI systems, advancing AI for AI (AI4AI) as a pathway toward recursive self-improvement (RSI). Workflow-driven machine learning engineering (MLE) systems provide a practical path toward this pursuit through complex orchestration that manages long-horizon experimentation, while recent MLE systems adopt model-directed interaction, allowing models to autonomously organize experiments and adapt optimization strategies based on execution feedback. However, feedback from each experiment reflects several preceding decisions, and a long MLE run contains many such costly experiments. Training must therefore select useful supervision from long interaction trajectories and learn from intermediate outcomes. We propose a post-training method for autonomous long-horizon MLE optimization and apply it to train MLExpert, a 35B Mixture-of-Experts agentic model. We design the Kaggle-MLE Factory to construct executable tasks and an interaction harness for model-directed experimentation. Hierarchical agentic SFT transfers general tool-use and coding capabilities to MLE through outcome-guided supervision. Windowed Interaction RL (WIRL) treats the multi-turn decisions between successive experiment results as an execution window and assigns it a shared outcome-based reward. Asynchronous collection and policy correction support policy updates before the trajectory ends. On MLE-Bench Lite, MLExpert improves the average medal rate of the base model from 37.9% to 72.7%, achieving performance comparable to larger frontier models such as Kimi-K3 and GLM-5.3. Further experiments show that MLExpert improves performance on NatureBench Lite, agent scaffold optimization, and algorithm optimization, suggesting that the learned optimization capability generalizes to other tasks.

---


### 296. [SUPRA-TEX: 3D Generation with Super-Aligned Texture](https://arxiv.org/abs/2610.22352)

**<font color=#1a73e8>作者：</font>** Chen Yang, Jiemin Fang, Fanpeng Meng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single image 3D generation aims to dress a given 3D mesh with relightable materials while faithfully preserving the visual details of a reference image. Existing methods either introduce artifacts when fusing inconsistent multi-view predictions or struggle to preserve fine details through implicit image-feature conditioning. To resolve these challenges, we introduce SUPRA-Tex, built on the principle of decoupling visible-material estimation, surface alignment, and observation-guided 3D completion. This division of labor allows the 3D generator, trained on limited 3D data, to focus its capacity on preserving visible evidence and completing unobserved surfaces. Specifically, we first train an MLLM-based image editing model to predict lighting-separated PBR maps in the reference view. We then project these maps onto the visible surface and encode them with the pretrained material VAE encoder into native observation latents that share the generation target's latent space. An interleaved flow transformer holds these latents as fixed, read-only anchors while alternating unobserved-region and full-surface updates to generate complete material latents. This design achieves super-alignment with the reference, delivering What You See Is What You Get fidelity on visible regions and coherent completion on unobserved surfaces. Trained solely on public datasets, SUPRA-Tex achieves SOTA performance in both geometry-conditioned texturing and end-to-end asset generation, matching or even exceeding leading commercial systems on in-the-wild images. Project page: this https URL

---


### 297. [Rethinking Routing Exploration in Modern Mixture-of-Experts](https://arxiv.org/abs/2610.22353)

**<font color=#1a73e8>作者：</font>** Bingcong Li, Hao Ma, Michael Muehlebach 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-experts (MoE) models have become an important approach for scaling model parameters. Modern MoE architectures increasingly combine two design choices: fine-grained expert segmentation and shared experts. The former increases expressiveness by enabling more expert combinations at a fixed activation ratio, and the latter introduces experts that are active for every token. We identify an exploration dilemma between these designs: shared experts can make routing less exploratory by reducing the variability of token representations. This conflicts with the greater need for exploration induced by fine-grained expert segmentation due to the combinatorially enlarged routing space. Consequently, the additional expressiveness offered by fine-grained segmentation may not be fully realized in practice. MirrorMoE is proposed to reconcile this exploration dilemma by shrinking the exploration space through token-adaptive suppression of unnecessary experts. MirrorMoE consistently improves performance across model scales.

---


### 298. [DK-VLM: Geometry as Position for Spatial Reasoning in Vision-Language Models](https://arxiv.org/abs/2610.22356)

**<font color=#1a73e8>作者：</font>** Han Su, Meng Tian, Tianyu Huang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models still struggle to understand 3D spatial relations across views and update spatial judgments as the observer moves. A common approach fuses 3D reconstruction features into visual tokens, but aligning these features with pretrained semantic representations remains challenging under limited spatial supervision. We propose DK-VLM with Dual-Kernel Attention, which computes attention from both a visual token's input position and its geometric position in the scene. A semantic kernel retains the pretrained model's native attention and positional encoding, while a separate geometric kernel uses estimated 3D points and camera poses to directly modulate attention through point displacements and relative view transformations. Then, a learned gate fuses their outputs. Geometry thus enters attention as position rather than as fused reconstruction features. We further introduce Reference-Frame Composition (RC) supervision to train the model to update its reference frame across successive judgments. It provides stepwise turn and heading targets derived from verified single-step annotations. Among the compared methods, DK-VLM-8B achieves the highest average score across six spatial benchmarks and the highest overall scores on VSI-Bench (74.33) and ReVSI-32 (58.28). RC supervision further improves multi-step spatial reasoning, while the full model preserves general video understanding. Project page: this https URL.

---


### 299. [Grounding Generative Verification in 3D Content](https://arxiv.org/abs/2610.22360)

**<font color=#1a73e8>作者：</font>** Shuanglin Li, Jiaying Lin, Shuquan Ye  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in multimodal large language models (MLLMs) and 3D generation have expanded 3D understanding and synthesis. However, beyond visual fidelity, task-specific correctness grounded in 3D evidence remains a major challenge. We argue that building reliable 3D systems requires not only stronger generation and reasoning, but also verification feedback that identifies unmet requirements and explains their violations, allowing systems to reflect on and refine their outputs. Such feedback must integrate multi-view observations and distinguish genuine inconsistencies from projection-dependent appearances. We make three contributions. First, we introduce 3DVerifierBench, a benchmark spanning 10 tasks that evaluates decisions, rejection explanations, and responses to controlled changes in specifications and candidates. A human study reveals a 21.6 percentage-point gap between humans and the strongest tested model, GPT-6 Astra, while explanation-aware analysis exposes weaknesses in rejection reliability. Second, we analyze verification across fine-grained factual categories, exposing errors in values and target binding. We develop a scalable pipeline combining multi-view fact extraction, controlled 3D editing, and native annotations to produce 14,126 training examples with contradiction explanations and linked counterfactuals. Third, we examine how verification could support 3D generation through candidate selection and recursive refinement. In human-labeled sixteen-candidate pools, oracle selection improves complete factual success from 26.7% to 90.0%. In a separate eight-input study, human-guided recursive refinement satisfies all seven requirements for every input, compared with three under parallel Oracle@8. Together, our benchmark, analysis, and data pipeline establish a foundation for models to reflect on 3D content through reliable verification feedback.

---


### 300. [Perceive, Predict, and Plan: a Unified World Action Model for Egocentric Dexterous Manipulation](https://arxiv.org/abs/2610.22363)

**<font color=#1a73e8>作者：</font>** Zirui Wu, Chen Guo, Tianjian Jiang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce P$^{3}$-WAM, a unified world action model for egocentric dexterous manipulation that learns 3D perception, action-conditioned prediction, and goal-directed planning through three complementary modes: Perceive, which reconstructs articulated hand motion and camera trajectories from video; Predict, which generates visual futures under prescribed actions; and Plan, which jointly generates action trajectories and their anticipated visual consequences conditioned on an initial image, a language instruction, and an optional visual goal. Our model integrates a compact, structured 3D action representation into a pretrained video diffusion transformer through a mixture-of-transformers architecture with shared base weights, modality-specific adaptation, and bidirectional visual-action attention. Randomized modality visibility lets video and 3D actions serve as either conditioning context or prediction targets across the three modes. Experiments show that unified training improves all three capabilities over single-mode training, including gains in planning quality under a vision-language model evaluation. Through unified training, our model outperforms specialized baselines on 3D hand reconstruction and action-conditioned video prediction across four datasets, while producing goal-directed manipulation videos with stronger instruction adherence and action progression than video-generation baselines. Project Page: this https URL

---


> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-321](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
