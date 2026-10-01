# 🧠 大模型相关研究 | 2026年10月02日

> 本类共 **390** 篇论文：已确认 **371** 篇，待复核 **19** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-390](./part-08.md)

---

### 51. [VidHarness: Evolving Agent Harnesses for Cost-Efficient Long Video Understanding](https://arxiv.org/abs/2609.38413)

**<font color=#1a73e8>作者：</font>** Susan Liang, Jianmin Wu, Daxiang Dong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) can answer questions about hour-long videos, but processing every frame is prohibitively expensive, even though the evidence for a question usually spans only a few seconds. Video agents, i.e., harness programs wrapped around a frozen VLM, address this by observing the video selectively, yet existing harnesses are hand-crafted by experts through slow build-and-test cycles. We propose VidHarness, a framework that automates harness design for cost-efficient long video understanding, in which a harness proposer iteratively evolves harnesses based on execution feedback from an evolution environment. To escape the local optima of greedy refinement, we organize the evolution as Monte Carlo tree search (MCTS), and to reduce the evaluation cost, we integrate uncertainty-aware multi-fidelity validation, which screens new harnesses on a few questions and promotes only the promising ones. Since the best harness varies with the frame budget, we further introduce a mixture-of-harness that routes each question to a harness specialized for its budget. VidHarness sets new state-of-the-art results on LongVideoBench, Video-MME, and Video-Holmes, outperforms the strongest hand-crafted video agent by up to $11.2$ points, and generalizes to the knowledge-intensive benchmarks Video-MMMU and MMVU with fewer than half of the frames of uniform sampling.

---


### 52. [Synthesis Without Training: An Inference-Only Pipeline for Tabular, Temporal, and Relational Synthetic Data](https://arxiv.org/abs/2609.38414)

**<font color=#1a73e8>作者：</font>** Zilong Zhao, Abdul Raheem, Jiayu Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic data generation is dominated by the fit-then-sample paradigm: a generative model is trained on a private dataset and then sampled from. Despite its widespread adoption, this paradigm faces three challenges: (1) a new training run is required for every dataset; (2) different data modalities, such as single tables, time series, and relational databases, require task-specific models and feature engineering; and (3) the resulting model is opaque, making its behavior under data constraints difficult to inspect. We propose GENSCRIPT, an inference-only pipeline that eliminates model training. GENSCRIPT computes a deterministic statistical profile of the source data (column types, ranges, missingness, categories, correlations, etc.) and passes it--rather than raw rows--to a language model to infer field semantics and cross-column integrity constraints. A coding agent then compiles the profile and constraints into an executable, auditable sampler. This unified approach supports single-table, temporal, and relational data without task-specific modeling. Across four single-table benchmarks, GENSCRIPT builds generators in 2 minutes and samples 50k rows within 6 seconds, while remaining within a few points of leading methods in marginal fidelity. Notably, it is the only method that perfectly preserves a 1-to-1 mapping between columns in the Adult dataset. On a smart-building dataset, it produces conditional time series that more closely match the real distribution than two baselines and perfectly preserves primary- and foreign-key relationships in the corresponding relational database.

---


### 53. [Evaluating Whether GPT-6 Astra Performs Unsanctioned Supply-Chain Attacks](https://arxiv.org/abs/2609.38415)

**<font color=#1a73e8>作者：</font>** Alexandra Souly, Kai Fronsdal, Abby D'Cruz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This technical report presents an alignment evaluation developed and performed by the UK AI Security Institute for assessing whether advanced AI systems take unsanctioned actions outside the scope of their assigned task. We evaluate whether frontier models conduct supply-chain attacks against out-of-scope, third-party targets when placed in difficult cybersecurity challenges, motivated by recently observed cases of models attacking real open-source repositories during evaluations. Applying our methods to GPT-6 Astra and previous OpenAI models, with cyber safeguards disabled, we find that GPT-6 Astra attempts complete supply-chain attacks in simulation at a higher rate than GPT-5.6 Sol and GPT-5.5. This includes writing malicious code as a contribution to an out-of-scope open-source codebase, creating fake identities to deceive open-source developers, and submitting benign contributions before malicious ones. GPT-6 Astra frequently reasons about the scope of the challenge in its chain-of-thought yet still proceeds to attack out-of-scope targets; it often asks for permission, and treats an automated message as as authorisation; and it continues to take unsanctioned actions, at a reduced rate, when internet access is more explicitly disallowed. Our evaluation builds on an internal version of Petri, an open-source LLM auditing tool, with all tool calls simulated by other LLMs, so that no real network access, systems or third-party repositories are reachable and no real-world harm is caused. Finally, we discuss limitations, in particular simulation awareness. We believe simulation awareness may have driven some of the observed behaviour but does not remove our concern. Our results suggest that defences beyond model alignment, such as sandboxing and monitoring, are increasingly critical for safe and secure deployment.

---


### 54. [LoopVL: Recurrent Visual Intelligence](https://arxiv.org/abs/2609.38426)

**<font color=#1a73e8>作者：</font>** Zhe Qian, Ziyang Gong, Zhongxing Xu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce LoopVL to study whether Loop Transformers can be effectively extended to vision- language models. LoopVL combines Module-Loop and Model-Loop computation to iteratively update a unified vision-language state through shared modules. We train LoopVL from scratch through language pre-training, multimodal training, and post-training. LoopVL outperforms a range of similarly sized and larger non-recurrent models on multimodal understanding and visual reasoning benchmarks. We also observe Visual Aha Moments in LoopVL, characterized by pronounced shifts in visual attention across loops. LoopVL provides practical evidence for recurrent vision-language modeling and offers an intuitive perspective on how shared parameters can support deeper multimodal computation over continuously evolving visual-language states.

---


### 55. [MOBA-VL: Event-Localized Multi-Turn Reinforcement Learning for Real-Time MOBA Commentary](https://arxiv.org/abs/2609.38428)

**<font color=#1a73e8>作者：</font>** Shengyun Zhong, Xinkang Zhao, Ziyuan Chu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time commentary for Multiplayer Online Battle Arena (MOBA) esports requires a vision-language model (VLM) to narrate a live match second by second, both fluently and accurately. Existing streaming VLMs sound natural but often miss key events such as kills and objectives. To address this limitation, we use game telemetry, which records exactly when each event occurs, as a supervision signal. We introduce MOBA-VL, a 9B-parameter model trained on this signal with event-localized multi-turn reinforcement learning, which rewards the turns that describe each event. We also collect MOBACast, 860 professional matches (about 460 hours) across three MOBA games with word-level timestamped commentary, and MOBACast-Bench, a benchmark from held-out tournaments. On MOBACast-Bench, MOBA-VL achieves the highest Overall score on full matches (63.25 vs. 55.12 for StreamingVLM) and clips (63.45 vs. 56.22 for DeepSeek-V4.1-Flash). Event-localized credit also raises event recall from 34.5 to 42.1 over supervised fine-tuning. Code and data will be released, and demos are available on an anonymous project page at this https URL.

---


### 56. [Audible World Models: Spatially Aware Sound Generation for 3D Worlds](https://arxiv.org/abs/2609.38444)

**<font color=#1a73e8>作者：</font>** Duowen Chen, Jinjin He, Gouthaman KV 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text- and image-conditioned world generators can create visually rich 3D environments, yet these worlds often remain silent or rely on soundtracks synthesized solely from text or rendered video. Although such audio can convey what should be heard, it lacks an explicit representation of where sound sources are located and how their perceived sound should vary with listener movement. We introduce Audible World Models, a training-free framework that incorporates sound into the generated world state. Starting from a text prompt, our system constructs a panoramic 3D proxy, separates it into semantic layers, identifies sound-producing foreground objects and ambient background regions, and synthesizes dry audio for each sound label. It then anchors these sources to reconstructed geometry and renders listener-dependent spatial audio using geometric acoustic propagation. By explicitly linking semantics, geometry, and sound propagation, the framework maintains persistent source locations while adapting the rendered audio to changes in listener viewpoint and motion. Experiments across 80 generated scenes demonstrate substantial gains in spatial consistency over text-, video-, and panorama-conditioned baselines, while preserving competitive semantic alignment. VLM-based assessments and human evaluations further indicate that our soundtracks are preferred for their audio-visual consistency, spatial plausibility, and motion-dependent behavior.

---


### 57. [AIM: Agentic Idea Management for Automated Research](https://arxiv.org/abs/2609.38445)

**<font color=#1a73e8>作者：</font>** Hyeong Kyu Choi, Bhavana Dalvi Mishra, Jiefeng Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier LLMs are increasingly used to automate scientific research through iterative search. We distinguish idea-driven search from solution-driven search and identify three core challenges: organizing evolving research ideas, selecting promising directions, and maintaining alignment between ideas and their implementations. To address these challenges, we introduce the Agentic Idea Manager (AIM), a fully autonomous framework for managing and exploring research directions in idea-driven automated research. Inspired by Bayesian optimization, AIM uses an Agentic Surrogate and an Agentic Acquisition mechanism to organize discovered ideas and guide their selection. A Solution Auditor maintains idea-solution integrity, while a Resource Planner adaptively allocates the remaining experimental budget across parallel search branches. Experiments on 10 AutoLab benchmark tasks show that AIM surpasses the strongest baseline by 1.6 percentage points on System Optimization tasks and 4.9 percentage points on long-horizon Model Development & CUDA tasks. Notably, AIM reaches the best baseline performance up to 3.1x faster in wall-clock time. We further provide a theoretical analysis of when searching over ideas becomes beneficial. Our analysis shows that explicit idea-level allocation makes semantic coverage directly controllable, and that broader coverage becomes increasingly valuable when competitive research directions are sparse among many plausible alternatives. Project Page: this https URL

---


### 58. [What Pretraining and Midtraining Make Learnable from Rewards?](https://arxiv.org/abs/2609.38446)

**<font color=#1a73e8>作者：</font>** Chiwun Yang, Xiaoyu Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A reward can identify a correct answer while leaving the computation needed for new inputs undetermined. We study how pretraining and midtraining supply the information and computation that make reward adaptation effective. In sequential state computation and contextual memory, we characterize mechanisms that agree on every training reward yet demand different held-out answers. Task-independent source observations resolve this ambiguity. We construct finite sampled Adam paths from specified random initializations through source prediction and reward adaptation in the same parameters, proving how prediction acquires execution or retrieval and rewards learn their task-specific use. Experiments with pretrained Qwen2.5 checkpoints test this division of labor. Across eight worlds, Sequential models trained with correct source and first-operation supervision reach 82.61% success, versus 44.15% for a private-random source control. Memory replay preserves retrieval during reward adaptation, and an independent eight-world confirmation achieves 75.32% task success versus 49.86% after matched alternative-retrieval training. GSM8K and HotpotQA separate accuracy at reward entry, subsequent gain and final performance. Together, these results connect information acquisition, executable computation and reward-guided task learning.

---


### 59. [Reach Into The CHOIR: Free-List Elicitation Uncovers Distinct Model Voices in LLM Ensembles](https://arxiv.org/abs/2609.38448)

**<font color=#1a73e8>作者：</font>** Ben Wigler, Maria Tsfasman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Open-ended LLM homogeneity can create false plurality when several systems appear to offer independent perspectives while returning the same familiar default. Single-pass answers obscure the distinction between agreement produced by a tightly constrained answer space, prompt-vocabulary echo, and broader answer spaces with stable alternatives beneath the surface. We introduce CHOIR (Collective Hierarchically-Ordered Inquiry Responses), a framework that adapts free-list elicitation from cognitive anthropology to LLM ensembles. CHOIR repeatedly elicits ranked lists, clusters items into prompt-level concepts, and measures concept salience across models, prompt variants, and persona conditions. We evaluate CHOIR on Infinity-Chat 100, an external prompt bank from recent work on open-ended model homogeneity, and on a 27-question targeted diagnostic bank designed to isolate mechanism-level contrasts. On Infinity-Chat 100, CHOIR reproduces high surface agreement (93/100 prompts above chance) while separating narrow prompts from broad prompts with recoverable depth. Across targeted probes and the external prompt bank, base-model identity remains the strongest recoverable signature, and persona prompts shift surfaced concepts within base-model signatures. A source-blind ranking module prioritises rare-but-stable candidates for later inspection. CHOIR turns open-ended homogeneity into a diagnostic measurement problem by asking where models converge, why they converge, and what remains reachable under structured depth probing.

---


### 60. [PrivMeSA: Privacy-Aware Self-Evolving Multi-Agent System for Medicine via Local-Remote LLM Collaboration](https://arxiv.org/abs/2609.38458)

**<font color=#1a73e8>作者：</font>** Dannong Wang, Yuran Zhang, Bian Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical large language model (LLM) agents deployed locally can consult more capable remote models, but doing so risks exposing patient information. Privacy-conscious delegation places disclosure decisions with a local agent, yet removing explicit identifiers is insufficient: quasi-identifiers can accumulate across multi-turn consultations and repeated patient visits to enable re-identification. We introduce PrivMeSA, a privacy-aware self-evolving multi-agent system that learns to control disclosure and retains remote expertise for local reuse. A local agent manages each encounter and consults remote specialists that may request additional information. Reinforcement learning balances task accuracy against direct disclosure and registry-based re-identification risk, with privacy evaluated over the complete outbound transcript of each encounter. A local lesson memory distills completed consultations into generalized clinical guidance and retrieves relevant lessons before transmission, allowing subsequent cases to reuse expertise without another remote exchange. Memory grows without additional outcome labels or parameter updates. On an emergency-department benchmark built from MIMIC-IV-ED records, PrivMeSA improves mean task accuracy over delegation by up to 15.8 percentage points. In the same setting, PrivMeSA reduces the disclosure of personal details from 98.0% to 0.2% of cases and the share of cases in which the patient can be narrowed to ten or fewer registry patients from 74% to 0%.

---


### 61. [NAQD Env: A benchmark for selective withdrawal in language agents](https://arxiv.org/abs/2609.38460)

**<font color=#1a73e8>作者：</font>** Mohamed Abouzahra  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language agents must revise planned actions when evidence changes, permission is revoked, or a stop instruction arrives. A useful response is selective: suspend affected actions, preserve unaffected work, and resume only after sufficient repair. We introduce NAQD-Env, a synthetic environment that evaluates these decisions against a deterministic reference policy over explicit evidence, authorization, and constraint dependencies. Eleven dependency families support evaluation on development structures, held-out families, and held-out combinations of structures. Metrics distinguish attempted violations from violations permitted by a simulated execution gate and jointly report policy agreement, task value, withdrawal, resumption, and event reporting. We evaluate three open-weight instruction-tuned models from two families under three prompt conditions on 350 frozen scenarios, yielding 3,150 model-prompt episodes before gate replay. Across the reported conditions, withdrawal recall is at most 0.06, no valid resumption is observed at eligible opportunities, and only one episode matches the complete reference policy. Under the NAQD prompt, Qwen2.5-7B has fewer unsafe-attempt episodes than Qwen2.5-3B and Llama-3.1-8B, but also completes less useful work and preserves unaffected actions less accurately. Exploratory supervised fine-tuning probes increase Qwen2.5-3B decision accuracy from 0.45-0.54 to 0.83-0.92; separate diagnostics reveal inappropriate withdrawal after curriculum omissions and a loss of event reporting. These results motivate evaluating selective withdrawal as a distinct component of agent reliability. The setting measures policy application with trusted structured inputs and does not establish real-world containment or source-verification ability.

---


### 62. [The Backdrop Exposes What the World Around an Agent Costs It](https://arxiv.org/abs/2609.38469)

**<font color=#1a73e8>作者：</font>** Nusrat Jahan Lia, Shubhashis Roy Dipta  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent benchmarks test agents in worlds that stay still. Deployed agents work in worlds that other people also change. Someone texts the agent to send the money elsewhere or an order confirmation asks it to reply with a door code. We present BACKDROP, which asks how much of an agent's capability in a clean world survives in such a world. BACKDROP takes a task along with the agents execution environment, and plants four everyday hazards in its world, one at a time and all together. The instruction and the correct end state stay the same. Each hazard asks one question. Authority: does a message from another person override the user? Injection: does text planted in a record redirect the agent? Boundary: does a request pull it into an app it was not given? Fault: after a write fails without saying whether it landed, does the agent check before it retries? Across 3,678 variants and 16 models, , the average pass rate falls from 69.5% to 31.3% once all four hazards are present; the strongest models fall furthest (Claude Fable 5.1 from 96.6% to 56.0%). Agents have learned to resist injected text but often follow other unauthorized requests of other people. With all four hazards present, and counting only runs where the planted text reached the agent, agents followed another person's message in 46.4% of runs and injected text in 20.3%. The gap is consistent throughout all 16 models. BACKDROP formalizes these gaps and shows how an agent's score in a task's world is a ceiling on real-world performance.

---


### 63. [Curating Synthetic Data for Task-Specific Visual Perception](https://arxiv.org/abs/2609.38476)

**<font color=#1a73e8>作者：</font>** Saptarshi Neil Sinha, Paul Julius Kühn, Michael Weinmann  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic data are most valuable where general-purpose datasets cannot provide the domain-specific priors a task requires, and where manual annotation is expensive, imprecise, or infeasible. In this article we argue that the central question for specialized vision systems is not how to generate more data, but which data to generate. We therefore discuss curated synthetic data, whose scene content, appearance variations, sensing characteristics, and annotations are deliberately designed around a given task. We examine three complementary curation paradigms. Procedural rendering offers explicit control over scene parameters and the annotations follow by construction. Physically-based simulation encodes the mechanism behind an observed effect and yields exactly aligned supervision pairs. Generative AI learns sensor-specific appearance from small real seed sets and attains plausible realism, though it remains prone to hallucination and to inaccurate annotation. These paradigms are illustrated with examples from industrial surface defect detection, restoration of degraded digitized autochrome plates, and 6DoF pose estimation from RGB and event data. Using these examples, we analyze different data regimes and training strategies that combine synthetic and real data across these paradigms. We conclude that curated synthetic data are best understood as a complement to real observations, and that hybrid pipelines combining controllable supervision with learned appearance are the most promising direction for reliable sim-to-real transfer.

---


### 64. [Security-Enhanced Seed-Based Weight Quantization for Large Language Models](https://arxiv.org/abs/2609.38477)

**<font color=#1a73e8>作者：</font>** Qiuyu Ren, Sudipta Paria, Aritra Dasgupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) incur substantial storage, memory-bandwidth and energy costs, motivating compact weight representations. Existing seed-based compression methods reconstruct weights from compact pseudo-random representations but do not explicitly account for the non-uniform sensitivity of model weights. We introduce Seed-Q, a security-enhanced sensitivity-aware seed-based weight compression framework that uses lightweight Linear Feedback Shift Register (LFSR)-based weight generation with non-uniform bit allocation. Our approach assigns larger representation budgets to sensitive weights while aggressively compressing less sensitive regions. Importantly, this non-uniform allocation requires no side-information: the decoder deterministically reconstructs the bit-allocation schedule, with no rung depending on the decoded weights, eliminating the need to store per-block metadata or use calibration data while preserving the baseline coding rate. Experiments across diverse LLMs show that Seed-Q matches 4-bit perplexity of SeedLM with fewer bits, while at the same 4 bits/weight it reduces both perplexity degradation and zero-shot accuracy loss relative to SeedLM. We also show that Seed-Q simultaneously achieves high security against bit-flip attacks on model parameters, as bit corruption affects multiple reconstructed weights, greatly amplifying its impact and making it easier to detect. We further implement Seed-Q in an ASIC-based accelerator and demonstrate modest hardware overhead compared to prior seed-based approaches.

---


### 65. [Caption-Mediated Perceived-Safety Estimation for Pedestrian Routing](https://arxiv.org/abs/2609.38479)

**<font color=#1a73e8>作者：</font>** Simon Parkinson, Paloma Liu, Wei Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents an explainable approach to pedestrian routing, in which perceived safety is estimated from street-level imagery through an explicit natural-language intermediate representation. A vision--language model caption is generated and stored before any scoring is undertaken, and the perceived-risk class is derived entirely from structured features of that stored text, so that every segment score remains inspectable by the user. Nine captioning conditions across five model families are benchmarked against a direct Contrastive Language--Image Pre-training (CLIP) image-embedding baseline under an identical downstream pipeline, and the caption-mediated representation is found to reach parity with the image embedding rather than to trail it. The approach was deployed over 654,115 images covering 36 electoral wards in two locations in Northern England (Manchester and Huddersfield). Independent field validation against 3,669 locally collected ratings of 494 images across 70 participant sessions established agreement that is statistically significant but modest, at $r=0.262$, against a measured noise ceiling of 0.737 imposed by disagreement between raters. A single-use confirmatory test then found that a pipeline 44\% stronger on the supervised benchmark did not produce measurable improvement in the field ($r=0.250$, $p=0.84$), so the benchmark gains did not predict the deployment gains in this case. Routing behaviour varies systematically with journey length. There is negligible change below 1\,km, reaching a median increase of 12.78\% in low-risk route length for a median detour of 2.73\% on journeys of 3 to 6 km.

---


### 66. [KlinikeBench: Evaluating Language Models Beyond Diagnostic Accuracy](https://arxiv.org/abs/2609.38480)

**<font color=#1a73e8>作者：</font>** Xueting Fang, Zehui Li, Yang Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most clinical benchmarks evaluate language models (LMs) on diagnosis using complete case descriptions. In clinical practice, however, patients present information in different ways, and clinicians must obtain relevant history and determine which examinations are needed before reaching a diagnosis. Diagnostic accuracy alone therefore cannot establish whether an agent gathered essential information or conducted an appropriate clinical assessment. Furthermore, existing benchmarks lack professional clinicians' verification. To address this gap, we introduce KlinikeBench, a benchmark of 333 clinician-authored tasks, each providing an isolated sandbox environment with a virtual patient, clinical tools, and task-specific success criteria. More than 35 clinicians contributed to case authoring and benchmark evaluation. In an empirical study, clinicians gave simulated dialogues higher mean quality ratings than reference conversations, which is adapted from real conversation. In each task, an LM has a fixed budget of turns to communicate with the patient, ask about relevant history, request examinations, follow action constraints, and record a final diagnosis. We score these steps separately as well as together. Across 31 models and seven model families, the best-performing models (e.g., GPT-6-astra and Claude Opus 5) succeed on less than 30% of tasks, even though their diagnosis accuracy reaches 90.7%. Some models benefit from talking with the patient; others diagnose well from a complete chart but perform much worse in conversation. Overall, KlinikeBench provides a testbed for evaluating the full clinical encounter and reveals a substantial gap between diagnostic accuracy and performance in interactive clinical assessment.

---


### 67. [PANDA: A Decentralized Architecture with Flexible Orchestration for Scalable, Fault-Tolerant Multi-Agent Systems](https://arxiv.org/abs/2609.38482)

**<font color=#1a73e8>作者：</font>** Matthew D. Laws, Cristina Nita-Rotaru  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Existing architectures for LLM-based multi-agent systems (MAS) cannot reliably and efficiently solve multi-step tasks at scale: they struggle to support large numbers of agents and concurrent tasks, tolerate failures, govern agent interactions, and accommodate the diverse planning and execution patterns different tasks require. We present PANDA, a decentralized architecture that connects a large collective of heterogeneous, independently administered agents, letting them discover each other's capabilities and self-organize into small specialized teams per task. PANDA scales by decoupling collective communication from team communication, allowing agents to participate in multiple teams simultaneously, load-balancing tasks across the collective, and scheduling concurrent work within each agent. PANDA further separates the underlying architecture from the orchestration strategy, supporting three planning and execution patterns (star, chain, and mesh) that can be selected according to the structure and requirements of each task. PANDA detects infrastructure and orchestration failures and recovers affected tasks by dynamically replanning around failed components. Finally, to provide governance without a centralized service that would limit scalability, PANDA uses a web-of-trust model to constrain agent interactions to established trust relationships. We evaluate PANDA on the HotPotQA benchmark, demonstrating that it scales to thousands of agents, assembles teams in milliseconds, matches state-of-the-art accuracy at up to 8x the efficiency, and sustains 100% task completion under faults where existing systems fail.

---


### 68. [Beyond Layers: Position-Resolved Gradient Conflict and Position-Aware Modulation for Unified Multimodal Models](https://arxiv.org/abs/2609.38485)

**<font color=#1a73e8>作者：</font>** Shuyang Jiang, Fucheng Deng, Yuchuan Luo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models (UMMs) train image understanding and autoregressive image generation on shared parameters, and the two objectives are known to interfere. Existing diagnoses and remedies operate at the resolution of layers or experts, measuring conflict per layer and resolving it by separating parameters. We argue that this resolution hides an orthogonal axis. Generation in a UMM is next-token prediction over a raster sequence of visual tokens whose roles vary systematically with position, so how strongly a generation gradient interferes with understanding should depend on where in the sequence it originates. We introduce a position-resolved interference map that attributes understanding-generation gradient conflict to visual-token positions within every layer, computed from a single backward pass at $1.2\times$ the cost of a standard backward pass. On Show-o and Janus-Pro, position explains a large share of conflict variance after controlling for depth (partial $\eta^2=0.31$ vs. $0.35$ for layer on Show-o; $0.15$ vs. $0.30$ on Janus-Pro): the first quarter of the sequence has a mean gradient cosine of $-0.18$ against understanding, the last quarter $-0.02$. The dependence survives per-position gradient-norm normalization, retaining $80%$ of its effect size, and conflict strength tracks semantic content (Spearman $\rho=0.64$). Building on the map, we propose position-aware modulation (PAM), which removes the anti-aligned component of generation gradients only at high-conflict positions without changing the architecture. Under a matched trainable-parameter budget, PAM improves over layer-wise separation by $+21$ MME and $+2.4$ GenEval points on Show-o while matching it on POPE and overall FID; a random-position control recovers about $31%$ of the gain. Position-based and layer-based separation are complementary degrees of freedom and can be combined.

---


### 69. [Personalized State-Transition-Aware Memory for Clinical Agents](https://arxiv.org/abs/2609.38490)

**<font color=#1a73e8>作者：</font>** Maryam Haghifam, Zahra Rajabi, Yizhou Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents that reason over clinical records must track changes in a patient's state while preserving the history needed to understand them. Simply accumulating memories leaves it unclear which information still applies, whereas overwriting earlier memories can erase evidence needed to reconstruct treatment history and clinical trajectories. We introduce STAM, a state-transition-aware memory framework that records state changes as new clinical entries arrive. STAM combines semantic retrieval with typed clinical relations to identify affected memories, maintaining current information in Active and superseded or resolved information in History. At read time, a query-dependent gate selectively serves historical memory. Across four longitudinal clinical benchmarks, we evaluate STAM with downstream question answering, direct state-maintenance diagnostics, and comparisons at approximately matched context lengths.

---


### 70. [Role-guided Speaker Deletion Verification in Clinical Psychiatry Speech Recordings with Audio Language Models](https://arxiv.org/abs/2609.38491)

**<font color=#1a73e8>作者：</font>** Joseph T Colonel, Daniel Katzman, Kelsey Kirker 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical research in psychiatry increasingly relies on large scale collection of spoken language data to identify acoustic and linguistic biomarkers. Yet evolving consent and protocol requirements can oblige investigators to remove a designated speaker from multi-speaker recordings and to verify said removal at a scale infeasible for manual review of entire corpora. We study this verification problem for role-driven dyadic clinical dialogue in psychiatry and investigate it with two parallel, symmetric pipelines: confirming that clinician speech has been removed from psychiatric interview recordings, and confirming that patient speech has been removed from the same recordings. Each pipeline redacts the raw audio for its target role and then scans the surviving output with audio-language and large-language models to identify missed deletions. We evaluate this approach on a corpus of 48 dyadic recordings drawn from psychiatry settings, testing four open-weight models in an inference-only setting: Gemma-4-12B, Gemma-4-31B, Nemotron-3-Nano, and Nemotron-3-Nano-Omni. A disjunctive OR ensemble over fourteen model-view configurations had a combined F1 of 0.478 (precision 0.330, recall 0.870), an improvement over individual model estimates driven by recall gains that point to substantial complementarity across models and context views.

---


### 71. [DEdit: Iterative Draft Editing for Speculative Decoding](https://arxiv.org/abs/2609.38510)

**<font color=#1a73e8>作者：</font>** Longxuan Yu, Bingsen Chen, Peng Shi 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates autoregressive LLMs by having a lightweight drafter propose tokens that the target model verifies in parallel. Diffusion-based drafters further reduce drafting latency by proposing multiple tokens at once. However, these tokens are predicted independently, so a single early error causes prefix verification to discard the rest of the draft, even when it contains useful downstream predictions. We introduce DEdit, a diffusion-based drafter that can not only draft by conventional parallel unmasking but also iteratively edit its draft through token-to-token predictions. Through editing, later predictions can serve as bidirectional context for repairing earlier errors and extending the accepted prefix. To teach the model to repair errors while preserving correct predictions, we propose ProposalMix, a training scheme that mixes draft predictions with ground-truth tokens based on first-pass confidence during training. Across seven benchmarks on Qwen3-4B and Qwen3-8B, DEdit achieves the highest macro-average token acceptance and speedup among the evaluated drafters, reaching macro-average speedups of $5.72\times$ and $5.97\times$ over autoregressive generation under greedy decoding, respectively. Further analysis shows that acceptance improves with more editing passes and wider drafting windows, and that ProposalMix halves harmful edits that shorten the accepted prefix. Moreover, restricting the editor to causal attention lowers acceptance, especially on highly predictable outputs, indicating that future context is a key source of these gains.

---


### 72. [VAmoS Part Deux: Harder, More Realistic Voice-Agent Simulation](https://arxiv.org/abs/2609.38512)

**<font color=#1a73e8>作者：</font>** Joshua Meyer, Sahar Shayegan, Ritiz Tambi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Voice agents in production must handle several requests, background speech, and customers who lose patience. We introduce VAmoS Energy, a benchmark that combines these challenges in 100 calls about utility billing and payment assistance. Each caller makes two to four requests. The agent has sixteen tools backed by a stateful Stripe billing twin and the Apache Fineract loan engine, with account access blocked until caller verification succeeds. The tasks use public household electricity data and a policy based on Pennsylvania's residential billing rules. An LLM-as-a-verifier checks the agent's actions and spoken figures against explicit requirements. On a calibration run, it agrees with a code verifier on 99.1% of checks. Across fourteen voice stacks and three repeats per task, completion ranges from 17.3% to 44.7%. Grok Voice leads, and Gemini 3.8 Live and GPT-Live follow at about the same cost per call. Background television reduces pooled completion from 38.7% to 8.6%. The simulated caller often accepts an incorrect result because it hears the agent's words but cannot inspect its actions. These findings show why voice agents need evaluation across the whole call, including what they say, what they change, and how they handle competing speech.

---


### 73. [From Solo to Social Learning: Characterizing Recursive Social Improvement in LLMs](https://arxiv.org/abs/2609.38516)

**<font color=#1a73e8>作者：</font>** Kunal Jha, Max Kleiman-Weiner, Natasha Jaques  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can now improve themselves by revising the instructions they follow, and LLM agents are increasingly orchestrated to work together on complex problems. However, self-improvement methods typically optimize one system at a time, and multi-agent frameworks often have every model work toward a shared goal. We ask a different question. When each agent pursues its own reward, can self-improving LLMs learn from one another well enough to improve the whole population? We call this capability recursive social improvement. We study populations that revise skill files and choose whether, when, and whom to copy from. Independent search, learning from peers, and acting all share one token budget. In controlled environments, established social-learning algorithms benefit from peers, but three LLMs do not. They earn less reward per token than solo learners, and explore too narrowly or run out of tokens before acting. We then let the models write and revise their own skills. Observing peers changes how they improve, helping one model find useful skills sooner and another spend less on private search. Neither, however, outperforms independent learners at the same cost. Skills are copied, revised, and passed on, so one discovery can seed further search. Yet these exchanges concentrate the population around fewer independent discoveries. Together, these results show that LLMs can make learning more efficient by copying from peers, but not yet more effective.

---


### 74. [ShamAN-Q: Shampoo Augmented NanoQuant for Sub-1-bit LLM Weights](https://arxiv.org/abs/2609.38521)

**<font color=#1a73e8>作者：</font>** Jonathan Mei, Sang Hyub Kim, Oliver Knitter 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce ShamAN-Q, a sub-1-bit post-training quantization method that extends NanoQuant by replacing each its diagonal reconstruction geometry with a tractable dense curvature metric, using a general paradigm popularized by the Shampoo optimizer. For each linear weight, ShamAN-Q fits a Kronecker product to the empirical Fisher information matrix of a small calibration set by Kullback--Leibler minimization, forming a Mahalanobis reconstruction loss from the result. The continuous ADMM updates from NanoQuant become solutions to Sylvester equations, while its discrete projection and deployment format remain unchanged. Because the curvature is local to a given set of weights, ShamAN-Q re-measures the input curvature statistic for each layer immediately before layer factorization, periodically refreshing all statistics on the partially quantized model. ShamAN-Q also redistributes the uniform rank from NanoQuant across layers at the same total number of bits. On Qwen3-Base, ShamAN-Q lowers WikiText-2 perplexity at $\approx$1 bpw from 27.56 to 22.96 (0.6B), 19.21 to 16.72 (1.7B), and 14.29 to 13.80 (4B) while matching or improving zero-shot accuracy on the Eleuther LM Evaluation Harness. On 0.6B, ShamAN-Q at $\approx$0.8 bpw matches the published perplexity of NanoQuant at $\approx$1.0 bpw.

---


### 75. [MM-FinEval: A Multi-Task Multimodal Benchmark for Real-World Financial Forecasting](https://arxiv.org/abs/2609.38523)

**<font color=#1a73e8>作者：</font>** Dong Shu, Yanguang Liu, Huopu Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial forecasting from earnings conference calls requires models to reason over complex corporate disclosures, market expectations, and subtle communication signals. However, existing financial benchmarks are often limited to unimodal inputs or single-task settings, making it difficult to evaluate whether multimodal large language models (LLMs) can support real-world financial analysis. In this paper, we introduce MM-FinEval, a novel benchmark designed to evaluate multimodal LLMs across multiple financial tasks. MM-FinEval spans a diverse timeline from 2019 to 2022. The entire proposed dataset contains 2,045 S\&P 500 conference earning calls as inputs and 12 financial task labels as outputs. Each input contains three modalities: a word-to-word text transcript of the earning call, the corresponding presentation slides used during the call, and the entire audio recording. To establish a rigorous evaluation framework, we analyze 19 baseline models across three distinct model categories: Image-Text, Audio-Text, and Any-to-Any configurations. We observe that small-size Any-to-Any models processing all three modalities achieve strong performance, even when compared against larger proprietary models restricted to two-modality inputs. This indicates that our tri-modal dataset design introduces useful, non-redundant information. These results validate that text, audio, and visual data serve as important, complementary signals that mimic the decision-making process of expert human analysts.

---


### 76. [Shifting Mechanisms: How Positional Encoding Choice Shapes In-Context Retrieval](https://arxiv.org/abs/2609.38530)

**<font color=#1a73e8>作者：</font>** Eric Enouen, Sainyam Galhotra  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models increasingly use architectures that vary attention span and positional encoding across layers, such as applying RoPE with sliding-window attention and NoPE with global attention (SWA NoPE). However, how these choices shape in-context retrieval remains unclear. To study this question, we take a mechanistic view, tracing how positional encoding (PE) choice shapes the internal mechanisms models use for in-context retrieval. Across 22 open-weight models spanning eight families, we find that standard RoPE models rely primarily on positional retrieval, while PE hybrids shift toward semantic retrieval. We further show on a controlled pre-training ablation that confining positional encoding to local layers produces this semantic shift, degrading representations of positional information. Finally, we show that the reported long-context gains of PE hybrids mask a retrieval trade-off: SWA NoPE improves over RoPE on multiple-target retrieval and QA, but degrades when distinguishing competing keys. We show that these behavioral differences better track the mechanism shift from positional toward semantic mechanisms than a uniform improvement in long-context retrieval.

---


### 77. [Does This Action Still Explain the Task? Reverse Scoring for Diffusion Language Model Agents](https://arxiv.org/abs/2609.38536)

**<font color=#1a73e8>作者：</font>** Jiacheng Qiu, Christopher E. Mower, Jan Peters 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion-based large language models (dLLMs) promise to break the sequential latency bottleneck of autoregressive agents through parallel decoding, but recent evaluations show this efficiency does not transfer to embodied agentic competence: dLLM-backed agents repeatedly fall into retry loops, re-issuing an action long after it has failed. We give a mechanistic account of this failure and a training-free remedy. We trace the retry loop to the adaptivity of masked decoding: the sampler commits the positions it is most confident about and defers the uncertain ones, and at a failure state the context already offers a confident fill for the deferred decision, i.e. the failed action itself, so the retry is committed without the failure feedback ever being confronted. We model the resulting distortion of the action distribution as a task-blind corruption: contextually salient actions (e.g., the action just taken) receive inflated probability by a factor that depends on the state and the action but not on the task. Under this model, we analyse an invariance proposition: the task-blind factor cancels exactly from the reverse conditional, i.e. the likelihood of the task given the state and a candidate action, which coincides with the task posterior of an idealized uncorrupted model. Masked dLLMs evaluate the reverse conditional natively, unlike autoregressive models, by masking the task tokens and denoising, at the cost of a few parallel passes per candidate. We instantiate the rule as Reflect Reverse and evaluate it on four multi-turn embodied benchmarks, where it improves task success and progression rates over forward-scoring baselines.

---


### 78. [ThinkV2V: Unleashing the Reasoning Capability of MLLMs for Instruction-Guided Video Editing](https://arxiv.org/abs/2609.38541)

**<font color=#1a73e8>作者：</font>** Donghao Zhou, Haoyang He, Fan Zhang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instruction-guided video editing has made significant progress, yet existing methods use multimodal large language models (MLLMs) primarily as semantic encoders, so they often fall short in working with implicit edits that require causal or semantic reasoning. To bridge this fundamental gap in video editing, we propose ThinkV2V, a reasoning-driven framework for complex instruction-guided video editing, explicitly activating MLLM thinking before visual generation. At its core, ThinkV2V builds on a practical MLLM-to-DiT architecture to turn explicit thinking over the source video and instruction into refined conditioning signals for video editing. Further, we equip it with a dedicated training and inference recipe, combining Progressive Curriculum Training, which gradually cultivates the model from basic editing to reasoning-intensive cases, with Inference-Time Thinking Scaling, which iteratively refines candidate prompts and selects the most reliable one, to better elicit reasoning in challenging editing scenarios. We also curate the ThinkV2V-150K dataset and introduce ThinkV2V-Bench to support training and evaluation of video editing with implicit intent and causal reasoning. Experimental results demonstrate the state-of-the-art performance of ThinkV2V on both complex and standard editing scenarios, in which our 5B-scale DiT model substantially outperforms larger 10B-scale baselines.

---


### 79. [MedKIT: Evaluating Knowledge Integration and Generalization in Large Language Models](https://arxiv.org/abs/2609.38543)

**<font color=#1a73e8>作者：</font>** Lukas Thede, Yash Kumar Atri, David Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Constantly evolving real-world knowledge necessitates models to be updated continuously. Especially in medicine, as clinical evidence changes over time, outdated knowledge can pose safety risks. Existing evaluations of knowledge integration focus on factual recall, offering limited insight into whether newly integrated knowledge is actually usable. Our benchmark MedKIT (Medical Knowledge Integration and Transfer) provides a granular evaluation of how models integrate and apply knowledge under realistic sequences of clinical updates. Each instance corresponds to a factual update derived from clinical evidence, paired with targeted probes that assess transfer across lexical variation, relational transformations, compositional reasoning, and open-ended operationalization, as well as locality tests for knowledge preservation. Using MedKIT, we conduct a large-scale empirical study of 12 knowledge integration strategies across 5 diverse models, including both general-purpose and medical LLMs. Our results reveal a consistent gap between recall and usable knowledge: while most methods achieve strong gains on the original update task and under lexical variation, relational generalization is limited, and no method yields meaningful improvements on compositional or operational tasks. These findings highlight a fundamental challenge in knowledge integration and position MedKIT as a testbed for developing methods that make newly integrated knowledge more consistently usable across tasks and contexts.

---


### 80. [Demographic Pluralism: Inference-Time Modeling of Pluralistic Human Preference Distributions](https://arxiv.org/abs/2609.38555)

**<font color=#1a73e8>作者：</font>** Meng-Chen Wu, Qipin Chen, Ansh Jain 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used in culturally sensitive settings, where alignment requires representing diverse preferences within populations. Yet existing methods model populations at coarse demographic or community levels and overlook within-group variation. We introduce Demographic Pluralism, an inference-time framework that estimates population-level opinion distributions without opinion-distribution training data or task-specific fine-tuning by generating multiple perspectives within demographically grounded groups. Across four backbones on GlobalOpinionQA and VITAL, it reduces Jensen-Shannon distance by 8.4%-26.4% over Modular Pluralism. Among weighted, equal-weighted, and inverse-weighted aggregation, equal weighting performs best overall; group-level error also increases with group weight, helping explain weighted aggregation's weaker performance.

---


### 81. [Defining and Categorising Human-AI Interactions in Clinical Trials: A Multidimensional Human-AI Classification Approach](https://arxiv.org/abs/2609.38559)

**<font color=#1a73e8>作者：</font>** Sandra Woolley, Tim Collins, Khalid Khattak 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper examines human-AI interactions (HAIIs) in clinical trials and presents a multidimensional categorisation framework that classifies interactions according to AI tasks, human-AI relationships, interaction configurations and interacting human groups. We define HAII, examine existing taxonomies and extend existing categorisation approaches through this novel multidimensional framework. We purposively sampled 15 clinical trials from a previously reported dataset. Each trial was independently categorised by two human reviewers and six large language model (LLM) classifiers. The proposed categorisation provides a structured method for the consistent identification, comparison and synthesis of human-AI interactions across clinical-trial records. The framework is intended to support more consistent comparison and synthesis of AI-related clinical trials and to make explicit the different forms of human involvement associated with AI interventions. The results demonstrate the potential for LLM-assisted categorisation while indicating the continuing importance of human judgement where trial records are incomplete or ambiguous. The principal contribution is a proposed multidimensional framework that brings together AI tasks, human-AI relationships, interaction configurations and interacting human groups within a single approach designed for clinical-trial records. Its significance lies in its potential to support more systematic identification, comparison and synthesis of how humans and AI interact in clinical trials.

---


### 82. [The Advantages of Fresh Sketching for Ridge Regression](https://arxiv.org/abs/2609.38565)

**<font color=#1a73e8>作者：</font>** Linkai Ma, Qilin Li, Petros Drineas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Over the past 25 years, sketching and sampling have become widely used tools for accelerating large-scale regression. In iterative randomized solvers, a basic design choice is whether to $\textit{reuse}$ the same sketch or draw $\textit{fresh}$ randomness at every step. For (under-constrained) iterative ridge regression with column sampling, whether fresh sketches offer provable advantages has remained open: $\textit{We show that they do.}$ Fresh sketching lets us analyze error only along the current residual solution, rather than uniformly over the entire Gram matrix. This directional view yields sharper convergence guarantees for leverage score and ridge leverage score sampling and, more importantly, leads to residual-aware sampling rules. By minimizing the variance of the relevant sketched matrix-vector product, we derive an oracle distribution and practical approximations to the oracle distribution, including a mixture sampling distribution with (somewhat weaker) convergence guarantees. Experiments on synthetic and real data, including ridge probes on Qwen2.5 representations, support our theory, showing substantially faster convergence.

---


### 83. [Towards Model as a Library: Offline, Community-Sourced AI for Low-Resource African Languages](https://arxiv.org/abs/2609.38574)

**<font color=#1a73e8>作者：</font>** Fendji K. E. Jean Louis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are frequently proposed as a route to AI-powered services for African communities, but they are least reliable exactly where the need is greatest: all African languages remain low-resource by any standard measure, and models trained on scraped, standardised text systematically misrepresent the dialectal and regional variation of how people actually speak. We introduce \textbf{Model as a Library (MaaL)}, a software architecture that packages small, community-enrolled speech models as versioned on-device dependencies, enabling offline structured data collection that cannot generatively hallucinate, for populations that current language models serve worst. Rather than relying on web-scraped corpora, MaaL's vocabulary is enrolled directly from a small number of example recordings by the speakers themselves, at the point of deployment. We describe the architecture and its central mechanism - keyword spotting that turns a closed-vocabulary text form into a voice form, filled and submitted entirely on-device - and propose transpiling the closed-vocabulary elements already present in widely-deployed digital form tools into MaaL schemas, a low-friction path to voice-first, offline data collection for the low-literacy populations these tools already reach. This is a position and system-design paper: we describe the concept, the mechanism, and an analytical feasibility case, and identify what a working implementation still requires.

---


### 84. [Conditional Generation of Creative Chess Puzzles with Diffusion Models](https://arxiv.org/abs/2609.38577)

**<font color=#1a73e8>作者：</font>** Aatu Selkee, Severi Rissanen, Xidong Feng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While modern language models demonstrate impressive generative capabilities, they often struggle with constrained, counter-intuitive creative tasks. To address this limitation, we explore chess puzzle generation as a rigorous testbed for computational creativity and reasoning, a domain where altering a single piece can invalidate an entire solution. We propose a novel approach for conditional generation of creative chess puzzles using masked diffusion models. Unlike previous methods, our non-directional diffusion approach allows for conditioning on specific tactical themes and partial board positions. We introduce a novel auxiliary task of simultaneous best-move prediction, which improves solution uniqueness by 11.6% and theme-conditioning accuracy by 2.5%. To further optimize solution uniqueness and theme conditioning, we establish a reinforcement learning framework adapted from Denoising Diffusion Policy Optimization (DDPO). This RL training increases the yield of unique and theme-matching positions by 89.1%. Finally, we release the first open-weights models (Appendix B) for chess puzzle generation, offering a new pathway for controllable, creative generation.

---


### 85. [FlexRouter: Learning Complementary Model Sets for Flexible LLM Routing](https://arxiv.org/abs/2609.38585)

**<font color=#1a73e8>作者：</font>** Wang Wei, Harry Yang, Tiankai Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing Large Language Model (LLM) routing methods score LLMs independently to select top-$k$ models. However, this ignores model correlations and enforces a rigid computational budget. Consequently, routers often select redundant models that share failure modes, limiting the overall probability of success. To address this, we propose FlexRouter, a routing framework that explicitly models model complementarity. FlexRouter optimizes for \textit{answer coverage}, maximizing the probability that at least one selected model yields a correct response. This objective aligns with practical inference pipelines where multiple candidate outputs are generated and a downstream verifier or user selects the final one. We formulate routing as a coverage-oriented subset selection problem and model the routing policy using Determinantal Point Processes (DPPs), which naturally capture both model competence and redundancy. To directly optimize coverage without requiring a ground-truth target subset, we introduce a training objective based on marginalizing over failure sets. During inference, we employ a greedy strategy based on marginal log-determinant gains, enabling the router to adaptively determine subset sizes without a predefined budget. Extensive experiments on the large-scale RouterEval benchmark demonstrate that our proposed FlexRouter achieves higher coverage with lower redundancy across both in-domain and out-of-domain tasks than strong baselines while maintaining flexible inference cost.

---


### 86. [Prompt2Skill: Unsupervised Skill Optimization From Natural Language Instructions](https://arxiv.org/abs/2609.38593)

**<font color=#1a73e8>作者：</font>** Bo Ni, Li Li, Ryan A. Rossi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Skills are external artifacts that Large Language Models (LLMs) consume at inference time to improve their performance on specialized domains by incorporating relevant procedural and domain knowledge. Expert-authored skills are expensive to produce, and the resulting artifacts are not optimized for the specific model that consumes them, whose failure modes can vary with version, scale and training. In addition, emerging tasks may fall outside the scope of existing skill libraries, creating a need to develop new skills before curated training data become available. Recent works have explored automated skill optimization through reflection, but they require a curated, in-distribution training set, which users might not always have. To address these limitations, we present Prompt2Skill, a framework that builds skills from natural-language task description alone. From the prompt, the system derives a task specification, discovers or synthesizes datasets, and refines the skill in a closed loop of reflective editing. Across four domains spanning question answering, reading comprehension, spreadsheet manipulation, and mathematical reasoning, Prompt2Skill consistently outperforms the direct prompting baseline, achieving an average improvement of 10.8 across open-source and frontier models.

---


### 87. [JARQ: Joint Alternating Refinement for Quantization](https://arxiv.org/abs/2609.38599)

**<font color=#1a73e8>作者：</font>** Xinyu Wang, Sicheng Lyu, Xiao-Wen Chang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group-wise post-training quantizers for large language models round weights onto a grid that is not refit to the resulting integer codes. We show that this leaves accuracy on the table: the best grid depends on the codes, input correlations couple the errors of different groups, and useful code changes often involve many codes at once. We propose JARQ , a plug-in refinement that starts from any group-wise quantizer and alternates a joint least-squares fit of all group scales with bounded Babai proposals that move many codes of a group together on the current grid. The problem is a bilinear box-constrained mixed-integer least-squares problem; the solver is backpropagation-free, does not increase the layer-wise objective under exact scale solves, and keeps the host's bit width, groups, zero points, and inference cost. Across Llama-2, Llama-3, and Qwen models with RTN, GPTQ, OmniQuant, and AWQ hosts, JARQ lowers perplexity in 90 of 96 comparisons, cuts three-bit RTN perplexity by up to 36%, raises mean multiple-choice accuracy in 23 of 24 configurations, and improves QEP, QuaRot, and OJBKQ outputs, at under a minute per 7B block.

---


### 88. [Sense and Sensitivity: Benchmarking LLM Clinical Triage Recommendations with Physician Experts](https://arxiv.org/abs/2609.38600)

**<font color=#1a73e8>作者：</font>** Abinitha Gourabathina, Haoran Zhang, Yuexing Hao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly used in clinical settings, it is critical to evaluate their reliability under realistic variation in clinical text. We study this question in clinical triage, comparing LLMs to practicing physicians under text perturbations that preserve the underlying clinical setting. We introduce a benchmark of over 6,000 clinical scenarios, 7,000 physician annotations, and 225,000 model responses. Using this benchmark, we make two key observations. First, LLMs are more likely than physicians to recommend unnecessary care at baseline, and this tendency increases under perturbed inputs. Further, we find that LLM recommendations are more sensitive to gender and tone perturbations than human recommendations. Together, these results demonstrate that LLMs can vary under clinically irrelevant textual changes, highlighting the need for deployment-oriented evaluations grounded in expert physician behavior.

---


### 89. [Aperture: Training-Free Multiscale Concept Bottlenecks for Remote Sensing](https://arxiv.org/abs/2609.38603)

**<font color=#1a73e8>作者：</font>** Rishabh Mondal, Nipun Batra, Utkarsh Mall  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While earth observation models have advanced substantially, they still lack interpretability. While concept-bottleneck models provide interpretability and expert interaction, they are either too expensive to train for the remote sensing domain or perform poorly without annotation. We posit that in expert domains like remote sensing, such training-free models require both fine details in both image and concept space. In image space, we propose a multiscale concept bottleneck using greedy quadtree routing to locate small concepts. In concept space, we replace contrastive vision language models with pre-trained MLLMs and present a way to get reliable concept scores from them. We introduce APERTURE that blends concept scores at the global image and native concept-scale level to give state-ofthe-art training-free model performance. To test these models, introduce SiFC, a fine-grained concept-centric dataset across three countries, with human-reviewed class-level concept maps. On SiFC, APERTURE outperforms the best training-free baselines by more than 10 percentage points in macro F1-score, and notably also outperforms supervised concept bottleneck models. Targeted component-removal tests examine whether concept scores respond to changes in visual evidence, while temporal experiments show that descriptor updates improve recognition of technological changes without retraining.

---


### 90. [Beyond Oracle Communication: Benchmarking Interactive Intent Alignment Under Miscommunication and Evolving User Intent](https://arxiv.org/abs/2609.38604)

**<font color=#1a73e8>作者：</font>** Zheyuan Zhang, Mengyuan Chao, Ke Xiao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern LLM agents increasingly tackle complex tasks through interactive, long-horizon exchanges with users, while existing benchmarks generally assume that users always accurately and sufficiently communicate a fixed intent. However, this oracle communication assumption rarely holds in practice: users may miscommunicate, change their goals, and run out of patience. We define this task setting as Interactive Intent Alignment, where agents must recover and continuously track the user's current intent despite imperfect communication and evolving goals. To study this setting, we introduce Drift-Bench++, a principled benchmark construction pipeline for verified executable tasks with controlled misalignment and intent shifts, along with an interaction protocol featuring finite patience, diverse simulated users, and silent interaction-conditioned shifts. We further develop GRIP, a comprehensive evaluation protocol covering task grounding, user realism, inquiry effectiveness, and adaptation to evolving intent. Across diverse environments, models, and interaction conditions, stronger interaction consistently helps but remains far from oracle performance; Validation on deployed ProdAgent sessions further shows that the modeled failures are prevalent and consequential in deployment. By providing a unified, executable benchmark for interactive intent alignment, Drift-Bench++ offers a foundation for evaluating and advancing agents under realistic communication and evolving intent.

---


### 91. [StreamDecisionBench: Evaluating Decisions in Force on Evolving Language Streams](https://arxiv.org/abs/2609.38612)

**<font color=#1a73e8>作者：</font>** Jhen-Ke Lin, Chung Chun Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As natural language drives more applications, language models increasingly run inside programs as decision components: the program sends them the current state and acts on the returned decision until a newer one arrives. When evidence changes during inference, a decision correct for its own state can stay in force after that state has passed, as when a call recorder keeps running after a customer starts reading out a card number; untimed (offline) accuracy counts such an error as correct. We introduce StreamDecisionBench (SDB), which evaluates the decision in force at every instant and attributes every erroneous instant to judgment, latency or both. Its scenarios stream evidence in four application families, with reference decisions computed from public rules by executable code. We summarize in-force accuracy across update intervals of 1-5 s by its normalized area under the curve on a logarithmic time axis, giving equal weight to equal multiplicative ranges. Across six settings of four hosted models, this score stays within 2.9 points of the scenario-wise product of untimed accuracy and an oracle's integrated timing score. Reasoning improves judgment, but at low effort latency costs Luna and Terra, two GPT models we also evaluate without reasoning, 38.8 and 42.8 points relative to untimed accuracy; a faster component with weaker judgment attains a similar integrated score to Terra without reasoning. The aggregate and family curves show where these tradeoffs change, making the evaluation's time-scale dependence visible.

---


### 92. [When Scientific Contradictions Are Lost in Translation](https://arxiv.org/abs/2609.38621)

**<font color=#1a73e8>作者：</font>** Tal Zeevi, Trey W. Jensen, Maxwell Strome  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Two scientific findings can disagree without contradicting each other. Determining whether they conflict requires knowing whether they describe comparable measurements. We study how language models behave at this decision point. In a controlled task, we generate an unsatisfiable XOR constraint system and translate its constraints into scientific reports from different laboratories. One assignment satisfies more constraints, while another satisfies fewer but better matches expected biology. This creates a simple dilemma: does the model choose the assignment that best fits the constraints, or the one that better matches biological expectations? When the constraints are stated directly, GPT-5.6 Sol and Claude Opus 5 recover the best-supported assignment in 90% and 96% of cases, respectively. In scientific prose, however, the models behave differently. Claude Opus 5 often prefers the biologically expected assignment. Removing that biological preference increases recovery of the better-supported assignment from 27% to 79% (p<.001); recovery reaches 92% when the same Biology-favored record is accompanied by a formalization request and an explicit paired-design cue (p<.001). GPT-5.6 Sol is less sensitive, with neither corresponding change reaching statistical significance. These results suggest that reliable scientific verification depends not only on formal reasoning, but also on how models decide which findings should be compared and what relations they imply.

---


### 93. [Strong Multilingual Privacy Tagging at Encoder Speed](https://arxiv.org/abs/2609.38630)

**<font color=#1a73e8>作者：</font>** Jonathan Graehl  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Privacy redaction must remove personal information while preserving relationships expressed in text. We develop a multilingual named-entity tagger with fine-grained distinctions supporting varied redaction policies and methods for cheaply learning additional distinctions. We fine-tune a multilingual encoder with an affine span-tagging head on frontier-model annotations in 35 languages, replay mapped human gold with coverage-aware masking so unannotated types are not treated as negatives, and repair subword boundaries with a learned +/-1-character adjustment. On 1,283 human-gold test segments in seven languages, best measured redaction F1 is 88.8, against 69.1 for published GLiNER2 with 11 unrepresentable types excluded from its task (68.8 without that exemption), 67.8 for GLiNER2 adapted to the new training data, 57.3 for Microsoft Presidio and 35.8 for the best published OpenAI Privacy Filter fine-tune. Adding about 50,000 annotated training sentences and increasing human-gold replay improves exact typed-span F1 from 74.5 to 76.3 on Ont3, our 31-type frontier-annotated NER evaluation of 1,201 development segments. Mapped-gold replay alone raises human-gold F1 by ten points without loss on frontier-annotated text; boundary adjustment adds 1.7 exact typed-span F1 points on Ont3. Local LLMs fitting on a single 96-GB GPU underperformed as prompted annotators and frozen encoders, with encoding 30-95 times slower than XLM-R inference and prompted annotation roughly 180-1,100 times slower in the evaluated configurations. The encoder architecture delivers 4.9 times GLiNER2's CPU throughput. We release code, prompts and training recipes, with data-acquisition scripts and source links.

---


### 94. [Component-Aware Feedback for Self-Evolving Programs](https://arxiv.org/abs/2609.38639)

**<font color=#1a73e8>作者：</font>** Ethan Lin, Jinming Nian, Yi Fang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-guided evolutionary search can discover complex programs, but existing methods mostly only save candidate programs and fitness scores while discarding which component edits produced which fitness metric changes. Existing methods force the mutator LLM to infer the effect of prior edits from cluttered histories, making program search slow and unstable. This is especially true for locally servable LLMs to evolve multi-component systems. We introduce component-aware feedback, which compares each evaluated program with its parent, identifies the components that changed, and logs them with the associated metric differences into an attribution memory that later mutations read. The memory keeps each change in two reference frames, local against the parent it came from and global against the seed program, which shows both the immediate effect of a change and the cumulative progress made since the seed. We study this on LLM reranking, a multi-objective optimization problem where a multi-stage pipeline must balance quality against serving cost. Across twelve \textsc{Bright} datasets, our method reaches the strongest baseline's final quality after a median of one third of the search budget and ends 7.2\% higher in held-out nDCG@10, and under a cost-aware objective it finds pipelines that are on average more accurate while using 11\% fewer tokens per query, showing component-aware feedback to be a promising direction for more efficient self-evolving systems.

---


### 95. [Vision-Language-Action Autonomous Driving Agent with Language-based Memory](https://arxiv.org/abs/2609.38641)

**<font color=#1a73e8>作者：</font>** Kai Yan, Xiangyu Chen, Yulong Cao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) foundation models have recently emerged as one of the prevailing solutions for autonomous driving, as they can utilize knowledge acquired during vision-language pretraining for accurate and interpretable driving. However, VLAs can take only a limited number of frames as visual input due to the high token cost of an image, which is problematic for memory-dependent tasks such as determining the arrival order at all-way stops and long-horizon driving scene understanding. Existing solutions use latent vector memories accessed through cross-attention, which are neither interpretable nor portable. In this paper, we propose AD-Memo, a general-purpose VLA driving agent with language-based memory. The agent outputs memory as an extension of its Chain-of-Thought (CoT) to record surrounding objects critical to driving; this memory becomes part of the agent's future input. We curate memory-based datasets and train VLAs with a two-stage recipe: Supervised Fine-Tuning (SFT) and \textit{Da Capo}, a novel semi-closed-loop Reinforcement Learning (RL) algorithm which uses trajectory-level advantage for memory and step-level advantage for driving, leading to better credit assignment. Across scenarios such as all-way stops and general driving, AD-Memo improves driving quality, enables better question answering on driving scenes, and produces plug-and-play memory for other models.

---


### 96. [Uncertainty-Normalized Margins for Direct Preference Optimization](https://arxiv.org/abs/2609.38647)

**<font color=#1a73e8>作者：</font>** Sadegh Khorasani, Petrus Mikkola, Matthias Grossglauser  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Direct preference optimization (DPO) models binary preferences through a Bradley-Terry model with a common noise scale, without explicitly accounting for preference strength or prompt-dependent uncertainty from human feedback. We introduce uncertainty-normalized margin DPO (UNM-DPO), which combines strength-dependent margins with a learned prompt scale. Motivated by a heteroskedastic Bradley-Terry model, we develop two training objectives. Both compare the implicit rewards of preferred and rejected responses, derived from response log-probability ratios to a reference policy. Advantage-only (AO) divides this reward difference by the prompt scale before subtracting the margin; whole-residual (WR) subtracts the margin before dividing by the scale. For the WR comparison model, we establish a necessary and sufficient condition under which known margins make the prompt scale identifiable. We introduce a practical procedure for learning the scale. Building on WR, we introduce ULNM-DPO-WR, which normalizes each response's implicit reward by its length. We evaluate our methods against DPO and related baselines on HelpSteer2 and HelpSteer3, using the Skywork reward model as a judge. With Llama-3.1-8B-Instruct, ULNM-DPO-WR achieves tie-adjusted win rates against matched DPO of 68.00% and 65.31% on evaluation panels, with higher mean rewards and shorter responses on average. On AlpacaEval with a GPT-4.1 judge and GPT-4-Turbo reference answers, the same 8B policy achieves a length-controlled win rate of 21.62%, compared with 16.39% for DPO and 15.30% for SimPO. These results demonstrate the potential of combining preference-strength margins, learned prompt scales, and length normalization for policy optimization.

---


### 97. [AgBench: Agentic AI Benchmarks for Personal AI Devices](https://arxiv.org/abs/2609.38652)

**<font color=#1a73e8>作者：</font>** Yizhou Han, Di Wu, Dhananjay Saikumar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems increasingly rely on cloud-hosted large language models for planning, tool use, and iterative execution, raising concerns about API cost and data exposure. Advances in personal AI devices enable agents to execute locally, but limited resources on device may affect task success and performance. Existing benchmarks are inadequate for systematically characterizing these trade-offs across devices, workloads, and deployment architectures. We present AgBench, a benchmark suite and open artifacts for reproducible evaluation of agentic AI on personal devices. Using AgBench, we evaluate local, hybrid, and cloud execution across agentic workloads, examining task success, latency, cloud API cost, and data exposure. Our results, drawn from over 162.07 million data points, show that personal AI devices can complete many agent tasks locally, but local-only execution generally has lower task success and longer completion times than cloud-only execution, especially as concurrency increases. Local-only execution eliminates cloud model API costs and sensitive-information exposure to cloud agents. Hybrid execution can improve task success, but its cloud cost and data exposure depend on how agents divide work and share information. No single architecture performs best across task success, goodput, cloud cost, and data exposure; deployment choices should reflect the intended workload and device capabilities. AgBench is available at this https URL.

---


### 98. [Breaking Babel: A Self-Evolving Multi-Agent System for Long-Form Subtitle Translation](https://arxiv.org/abs/2609.38660)

**<font color=#1a73e8>作者：</font>** Haibo Jin, Xinjie Li, Najmeh Sadoughi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-form subtitle translation requires reasoning over discourse and cultural context spanning episodes or entire series, while maintaining consistent terminology and style. Existing single-LLM methods are largely sentence-level, and multi-agent systems often use static workflows that do not adapt to scene complexity or production context. We propose SMART, a Self-evolving Multi-Agent system for long-foRm subtitle Translation. During test-time training, SMART builds persistent series-level memory and translates a subset of sentences through a dynamic router and Mixture-of-Agents layer with tools for terminology verification, subtitle constraint validation, and contextual retrieval. A judge-refiner loop scores candidates and uses textual critiques to update agent prompts and routing policies without retraining the underlying LLMs. During test-time inference, the evolved configuration translates the remaining series. We also introduce Subtitle Arena, covering 14 genres, 2--198 episodes per series, production years 1959--2023, and 15 target locales, together with SubMQM, a subtitle-adapted MQM framework with seven dimensions and 19 error categories. SMART achieves the best overall MQM score in all 15 Subtitle Arena directions, reducing average penalty by 6.9% over the strongest competing agent system. On the public MuSC benchmark, SMART obtains the best model result across all four language pairs and also achieves the best human-evaluation result, with an overall score of 4.50/5.

---


### 99. [EvoSteer: Online Self-Evolving Graph Orchestration via Reference-Anchored Credit Assignment](https://arxiv.org/abs/2609.38661)

**<font color=#1a73e8>作者：</font>** Mingda Zhang, Hanwen Zhang, Qiang Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In recent years, LLM-based multi-agent systems have been widely applied to orchestrate tool-using agents into executable communication graphs. However, existing self-evolving orchestration still faces key challenges, including post-hoc evolution that revises the team only after the trajectory ends, credit diffusion that gives every action the same terminal advantage under confounded baselines, and skill admission that is uncalibrated and never retired. To address these challenges, we propose EvoSteer, a new paradigm of Online Self-Evolving Graph Orchestration -- the orchestrator builds a running team and repairs its plausible but failing steps from execution features and a learned value estimate. To support this paradigm, we introduce Anchored Trajectory Balance (AnchorTB), a regression-style flow-matching loss that assigns each orchestration action a coefficient by balancing subtrajectories against a frozen reference. Built on the learned flow, we further propose Validated Skill Admission, in which a candidate skill is tried before promotion and promoted only if paired evidence passes a sequential test under a shared nominal testing budget. Moreover, AnchorTB combines measured task-level reference reward statistics with prefix-dependent corrections. Experimental results on twelve datasets show that EvoSteer significantly outperforms baselines across question answering, mathematical reasoning, code generation, and interactive decision making. Our code is available at this https URL.

---


### 100. [CollabFlow: Recursive Self-Improvement of Agent Collaboration](https://arxiv.org/abs/2609.38662)

**<font color=#1a73e8>作者：</font>** Xiao Huang, Mingda Zhang, Junming Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement (RSI) lets a system improve from its own outcomes; in LLM-based multi-agent systems, Agents refine one another within a task, and outcomes improve how they collaborate across tasks. However, existing multi-agent collaboration leaves this loop open: collaboration is pre-defined at the operator level, topology-only learning keeps verbatim exchange that propagates errors, and reward maximization on a system's own outcomes concentrates on a few teams. To address these challenges, we propose CollabFlow, an RSI system of Learned Agent Collaboration: a trainable Collab-Director constructs teams of complete Agents, a frozen executor runs them, and each round's outcomes retrain the director. Within each round, the edges of a collaboration graph carry protocols of Evidence-Conditioned Communication: a receiver adopts a differing answer only when the sender's evidence is stronger by a margin, so the director learns who communicates and how. Across rounds, we further propose Collaborative Trajectory Balance (CTB), a flow-based objective that credits each team once across its construction orders and targets a reward-proportional distribution over teams, so several good teams stay in play. We also bound how far this self-generated target moves between rounds, which shrinks as records accumulate. On twelve datasets, CollabFlow outperforms all baselines and keeps improving across rounds. Code is available at this https URL.

---


> [!TIP]
> 当前位于：**51-100**（第 2/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-390](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
