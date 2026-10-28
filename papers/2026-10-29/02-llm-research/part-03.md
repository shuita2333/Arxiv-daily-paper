# 🧠 大模型相关研究 | 2026年10月29日

> 本类共 **226** 篇论文：已确认 **214** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-226](./part-05.md)

---

### 101. [SetGRPO: Calibrating Grader-Induced Policy Optimization](https://arxiv.org/abs/2610.36807)

**<font color=#1a73e8>作者：</font>** Jiale Huang, Zixu Li, Zhiwei Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rubric-based reinforcement learning uses fine-grained grader feedback to train large language models on open-ended tasks, but grader randomness can alter GRPO updates in ways that score discrepancies alone cannot characterize. Because GRPO jointly normalizes rewards within each response group and combines the resulting training coefficients with response-level gradients, a scoring discrepancy can shift the coefficients of the entire group and induce policy-dependent update changes. Selective execution further affects the direction-reversal risk of retained updates. To address this, we propose Set-Valued Group Relative Policy Optimization (SetGRPO). It comprises three modules: (a) Joint Reward Set Calibration constructs a joint uncertainty set for the training coefficients; (b) Geometry-Guided Safe Recovery maps candidate coefficients into the current policy's local update geometry and determines the largest safe recovery ratio for each response group; and (c) Selective Risk-Gated Optimization selects a global threshold through independent risk calibration to control the conditional direction-reversal risk of accepted updates while preserving the original GRPO objective. Under exchangeability, SetGRPO provides finite-sample marginal coverage for the joint coefficient set and simultaneous risk control across candidate thresholds. On ten open-ended benchmarks spanning three domains, SetGRPO achieves the highest macro average among all compared training methods on both Qwen3.5 and Llama3.2 model families.

---


### 102. [Latent Visual Contrastive Reasoning with Multi-Branch Exploration](https://arxiv.org/abs/2610.36809)

**<font color=#1a73e8>作者：</font>** Kegeng Tang, Jingbo Wang, Yangming Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models have made substantial progress in visual question answering, but complex visual reasoning often requires locating and comparing multiple pieces of question-relevant visual evidence. Existing methods that move intermediate reasoning into the visual latent space usually follow a single linear reasoning trajectory, which can be limiting when multiple visual hypotheses or competing evidence regions are relevant. We propose Latent Visual Contrastive Reasoning, a branch-aware latent reasoning framework that generates multiple question-conditioned latent visual branches as soft hypotheses over image tokens. To train these branches, our method uses bounding-box evidence annotations to build target evidence representations and introduces a soft contrastive branch-evidence alignment objective. This objective encourages evidence-relevant branches to align with annotated visual regions while contrasting them against negative evidence. We instantiate our method on Qwen2.5-VL backbones and train it with standard supervised fine-tuning. Experiments on perception-intensive visual reasoning benchmarks show that the proposed method achieves overall improvements over the corresponding backbone and single-path latent reasoning baselines at both 3B and 7B scales.

---


### 103. [Weakness Localization Is Not Enough: State-Aware Recursive Knowledge Improvement for Large Language Models](https://arxiv.org/abs/2610.36811)

**<font color=#1a73e8>作者：</font>** Runze Jiang, Yan Wang, Boran Jin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge improvement in large language models is shifting from predefined knowledge incorporation pipelines toward evaluation-guided updating. Existing methods use evaluation to localize model-specific knowledge weaknesses and guide targeted post-training. However, identifying what to improve does not necessarily provide sufficient information for deciding how to improve it. The same localized weakness can be compatible with distinct operational knowledge states: the relevant knowledge may be unavailable, available but difficult to access reliably, or accessible but ineffective for downstream use. We call this ambiguity knowledge-state aliasing. When compatible states favor different interventions, greater diagnostic resolution alone is insufficient for intervention selection. Moreover, model updates can change the underlying knowledge state before the observed weakness disappears, such that an intervention appropriate in one round may no longer address the bottleneck in the next. To address these challenges, we propose Recursive Knowledge Improvement (RKI), which formulates knowledge improvement as a sequential, state-aware intervention process. RKI organizes knowledge into graph-structured units that provide a shared basis for diagnostic evaluation and targeted intervention across rounds. At each round, RKI localizes knowledge weaknesses, estimates the model's operational knowledge state from diagnostic evidence and intervention history, selects a corresponding intervention, and re-evaluates the updated model before determining the next intervention. On HotpotEval and SafeInternalEval, RKI outperforms existing knowledge incorporation methods by 18.41 points on average. Further analyses show that knowledge states provide additional guidance for intervention selection beyond weakness localization and can change across model updates even when the observed weakness persists.

---


### 104. [Words or Deeds? How LLMs Predict Users' Decisions in Human-Agent Dialogue](https://arxiv.org/abs/2610.36813)

**<font color=#1a73e8>作者：</font>** Baiqiao Zhang, Shuai Ma, Zhifeng Liao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Web systems increasingly predict users' decisions from what users say, yet when interests partly conflict, users may promise to cooperate to win the other side's cooperation and then not do so. Sales or service agents that rely on such promises may grant concessions to users who then do not keep their promises, at a cost to the party they represent. We test how LLMs combine users' statements with decision records to predict users' decisions, using 1,260 rounds in which 42 users played a repeated prisoner's dilemma-style game with five agents, each prompted to express a dominant Big Five trait, and could talk with the agent before every decision. Across eight open-weight LLMs, predictions from decision records separated cooperation from defection well (AUC = .80), and adding dialogue brought no detectable gain. With dialogue, predictions agreed with users' statements more often, and errors concentrated on rounds in which users broke their statements: accuracy on rounds with a statement barely changed (.73 to .74), while it rose on kept statements (.76 to .95) and fell sharply on broken ones (.65 to .17). Predictions weighted statements more heavily than users' behavior warranted: when users stated a decision they had not yet made in that game, the predicted probability of keeping it rose from .13 to .69, whereas users kept .40 of such statements. Users' decisions also varied with the agent they faced, but predictions hardly reflected this: users cooperated more with the Agreeableness agent than with the Extraversion agent (70.6% vs. 54.5%), whereas predicted cooperation was nearly identical (64.5% vs. 63.1%). Users also cooperated more with an agent when they themselves scored higher on that agent's trait, whereas predicted cooperation barely changed with these scores. Dialogue-based predictions should therefore weigh users' statements by their earlier decisions and the agent they face.

---


### 105. [Who Knows What - and What Does It Support? Perspective-Bounded Evidence Calibration for Multimodal Theory of Mind](https://arxiv.org/abs/2610.36824)

**<font color=#1a73e8>作者：</font>** Ziqi Liao, Jiaqi Shen, Yiming Na 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Theory of Mind (ToM), the ability to infer others' beliefs, goals, and intentions, is a cornerstone of social intelligence. Multimodal ToM requires inferring an agent's mental state from evidence that is available to that agent, rather than from the complete episode observed by the solver. Existing LLM-based and Bayesian model-based approaches reconstruct global event traces, yet they do not explicitly distinguish objective events from agent-admissible evidence during hypothesis evaluation. Consequently, agent-inaccessible events or semantically misaligned actions and utterances may influence the inferred belief, goal, or social intention, leading to perspective leakage and source or route confusion. We formulate this limitation as an evidence-admissibility problem: evidence should contribute to a mental-state hypothesis only when it is accessible to the relevant agent, preserves its information source, and is diagnostic of the queried mental-state variable. To operationalize this principle, we propose PIP-ToM, an evidence-admissibility interface that constructs agent-specific evidence stores, aligns them with structured mental-state claims, and calibrates model-based hypothesis scores while preserving the underlying Bayesian inference process. PIP-ToM with GPT-4o outperforms existing ToM methods across MuMA-ToM, MMToM-QA, and Hi-ToM, achieving average accuracies of 92.56%, 95.00%, and 95.00%, respectively.

---


### 106. [When the Critic Falls Behind: Co-Evolving Rubrics and Harnesses for Continual Agent Self-Improvement](https://arxiv.org/abs/2610.36826)

**<font color=#1a73e8>作者：</font>** Hao Chen, Yukun Yan, Ziyu Han 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous agents increasingly depend on harnesses that govern interaction, memory, tools, and execution around large language models (LLMs). While recent work has begun to evolve these harnesses from execution experience, the supervision used to guide evolution often remains relatively static, making it difficult to track changing behavioral weaknesses across rounds and potentially limiting generalization to unseen tasks. To address this issue, we propose RuHarness, a rubric--harness co-evolution framework for continual agent self-improvement. RuHarness continually discovers and reassesses behavioral criteria from execution trajectories, prioritizes the most relevant unresolved weaknesses, and uses them to guide targeted harness updates while keeping the task objective fixed. Extensive experiments across diverse agent tasks and backbone models show that RuHarness outperforms strong harness-evolution baselines, particularly on unseen held-out tasks. Further analyses show that adaptive rubric prioritization tracks shifting weaknesses and supports more sustained improvement and stable generalization across evolution rounds.

---


### 107. [Evolving Agent Teams](https://arxiv.org/abs/2610.36848)

**<font color=#1a73e8>作者：</font>** Shiyi Cao, Ziming Mao, Dacheng Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid progress of software engineering agents drives interest in applying them to open-ended problems such as GPU kernel optimization. However, we find that existing coding agents converge to local optima on real-world, expert-written kernels (e.g., FlashInfer). We introduce Evolving Agent Teams, a multi-agent framework that escapes such local optima. It features (1) a central supervisor that diagnoses each local optimum and restructures a team of agents; and (2) a persistent file system that comprises a learning document, an evolution history, and per-team artifacts, grounding restructuring with accumulated experience. Under a matched token budget, Evolving Agent Teams consistently outperforms strong coding-agent baselines. With an extended token budget, Evolving Agent Teams generates a CUDA kernel that reaches 1.2x mean speedup over the production FlashInfer MLA paged decode kernel from scratch and wins on 36 of 47 production workloads from FlashInfer-Bench (0.86-0.99x on the remaining 11). It also demonstrates superior performance on tasks such as KDA prefill on AMD MI350X (3.01x over vLLM) and NVIDIA B200 (3.44x over FlashKDA), MoE expert-offload serving on Apple silicon (30.3 tokens/s decode for Qwen3.8-Flash-Next in MLX 4-bit on a 48 GB M4 Pro), and RoboDojo robot manipulation (62.1 on held-out seeds vs. 55.3 for the best leaderboard entry). Code is available at this https URL.

---


### 108. [When All Rollouts Fail: Policy-Compatible Joint Decoding for Hard-Problem Reasoning](https://arxiv.org/abs/2610.36849)

**<font color=#1a73e8>作者：</font>** Zehao Wang, Hanzhu Chen, Runquan Gui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) derives its learning signal from binary rewards via on-policy exploration and becomes a powerful paradigm for improving the reasoning of large language models. Yet it faces a learning cliff on problems beyond model's current ability: when every rollout fails, the samples reveal nothing about a correct solution, and group-relative estimators (e.g., GRPO, RLOO) collapse the update to zero advantage. Expert trajectories offer a remedy, but they are incompatible with the current policy and often lie in the student's low-probability regions, so the surviving updates demand large parameter shifts and decay into surface-level imitation rather than transferable reasoning. We argue that a useful learning signal on hard problems must be both verifiably correct and sufficiently compatible with the current policy. We propose Policy-Compatible Reinforcement Learning (PICO), which performs distribution-constrained joint decoding: expert data guides decoding at the token level while preserving the student's relative token probabilities, and a dynamic top-k mechanism confines the sampling distribution under a finite divergence budget, yielding trajectories that are verified and policy-compatible by construction. These trajectories are optimized jointly with on-policy rollouts under a mixed-behavior objective that mitigates their distribution mismatch via importance sampling. Experiments across reasoning diverse datasets and agentic benchmarks demonstrate that PICO consistently outperforms standard RLVR and prior off-policy baselines.

---


### 109. [AdaGround: Token-Normalized Adaptive Zooming with Verifier-in-the-Loop Refinement for GUI Grounding](https://arxiv.org/abs/2610.36874)

**<font color=#1a73e8>作者：</font>** Bingchao Wang, Yongcheng Jing, Chengyu Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> GUI grounding on high-resolution screens fails mostly on small targets, and zooming in is a common training-free remedy. However, most existing zooming pipelines do not match the zoom to the target's size, accept the zoomed answer unconditionally and never revisit a wrong answer. To address these issues, we propose AdaGround, a training-free framework with three components: (1) Token-Normalized Adaptive Zooming, which sets the magnification, field of view and zoom depth of each sample from the model's own estimate of the target size; (2) Verifier-in-the-Loop Refinement, which uses one marked-click Yes/No verifier to keep or reject each zoom, choose between zoom chains, trigger re-grounding and, with an existence query, decide when to abstain; and (3) Compositional Structure Grounding, which composes spreadsheet cells from their headers. On Qwen3-VL models, AdaGround surpasses state-of-the-art training-free zooming methods and many trained GUI models, improving accuracy over the backbone by 7.4 to 20.6 points on OSWorld-G and ScreenSpot-Pro, and its gains carry over to held-out UI-Vision. Code is available at this https URL

---


### 110. [GUI-JEPA: Candidate-Conditioned JEPA Latents as a Fast Action Policy for Mobile GUI Agents](https://arxiv.org/abs/2610.36877)

**<font color=#1a73e8>作者：</font>** Bingchao Wang, Yongcheng Jing, Shunyu Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mobile GUI agents are typically fine-tuned 7B-scale vision-language models (VLMs) that generate each action as text. However, these VLMs decode every action token by token, and even agents that score candidate actions keep a large language model or VLM in the loop, making them slow and memory-hungry. To address these issues, we propose GUI-JEPA, to our knowledge the first decoder-free GUI agent policy built on a Joint-Embedding Predictive Architecture (JEPA), which selects actions in the latent space of a JEPA encoder pretrained on unlabelled GUI screenshots. Its action- and region-conditioned latent predictor turns the screen latent into one latent per candidate action, letting lightweight heads score all candidates against the instruction in a single batched pass, without decoding a token. We further show that the scorer relies on this latent pathway and that the predictor is trained for the decision itself: a randomly initialised predictor does just as well as one pretrained on screen dynamics. On AndroidControl, GUI-JEPA is 2.8-4.0x faster on the same GPU than a Qwen2.5-VL-7B agent we fine-tune with the same inputs, while reaching 86-92% of its in-distribution accuracy with 6% of its parameters. Code is available at this https URL

---


### 111. [HiLo-RD: Cross-Budget Self-Distillation for Masked Diffusion Language Models](https://arxiv.org/abs/2610.36901)

**<font color=#1a73e8>作者：</font>** Xiang Li, Chengting Yu, Jungang Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose HiLo-RD (High-to-Low Budget Representation Distillation) to improve masked diffusion language models (MDLMs) under a limited generation budget. Unlike autoregressive models, MDLMs choose both what to generate and where to commit it. This creates two coupled challenges: predicting useful content before reasoning is complete, and deciding when to fix answer tokens that shape later predictions. We identify budget-induced premature commitment: even when a correct solution fits, the model can fix answer fragments near the window boundary before resolving intermediate steps. These fragments become context for later predictions and redirect subsequent reasoning. Existing post-training methods do not directly transfer the stronger trajectories that the same model follows with a larger window. HiLo-RD addresses this gap by (1) pairing large-window teacher states with cropped small-window views and (2) matching their hidden representations at committed positions. This supervision guides both token prediction and commitment order without an external teacher. Across mathematics benchmarks, HiLo-RD improves low-budget accuracy and shortens responses; these gains extend to code generation without code-domain training. On GSM8K, accuracy rises by 9.4 percentage points as mean readable length falls by about 25%. Attention diagnostics and fixed-budget order interventions support the proposed mechanism. Together, these results show that large-window reasoning can improve small-window decoding.

---


### 112. [Nothing Left Behind: Finding Evidence from a Large Randomized Evaluation Corpus](https://arxiv.org/abs/2610.36910)

**<font color=#1a73e8>作者：</font>** Giuliano Martinelli, Abelardo Carlos Martinez Lorenzo, Satvik Garg 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many AI systems need to find every relevant items in a large collection and then organize what they found. The standard way to do this is to tag each item with labels from a curated vocabulary and search on those labels. Those labels are useful for organizing results, but searching on them misses items that do not fit a label and returns too much when labels are broad. We compare this approach with an embedding-based approach: find candidates by meaning using text embeddings, then have a language model keep only the relevant ones. In a corpus of 7,354 randomized trials, label search found 45% of the evidence a systematic review would include, while the new approach found 92%, at a cost per query that rises with search depth. These results support a two-stage architecture that combines broad candidate retrieval with query-specific evidence filtering.

---


### 113. [Developing a Speech Language Model for Basque](https://arxiv.org/abs/2610.36911)

**<font color=#1a73e8>作者：</font>** Andoni Sudupe, Inma Hernaez, Ander Arriandiaga 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although the recent development of LLMs has paved the way for multi-modal interaction, minority languages face difficulties keeping pace. This work presents the first open Speech Language Model for Basque, designed for low-latency, end-to-end spoken interaction. Based on the LLaMA-Omni architecture, the system integrates a Latxa model as its backbone, transferring its Basque capabilities to the spoken modality by fine-tuning several modules. To address data scarcity, the English VoiceAssistant-400K corpus was translated into Basque, and the audio was synthesized using a Basque TTS. Evaluation results confirm the system's viability, achieving 3.86/5 in content quality, a 9.94% WER for spoken intelligibility, and a 3.07 UTMOS for audio quality. This work demonstrates that advanced spoken interaction systems can be developed using modular architectures and synthetic data even in low-resource languages.

---


### 114. [Do We Need an LLM to Know Why Sources Conflict? Decision Models for Knowledge-Conflict Typing in RAG](https://arxiv.org/abs/2610.36915)

**<font color=#1a73e8>作者：</font>** Parv Khatri, Harshul Jain, Mehak Kapoor 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When the sources retrieved for a query disagree, the right response depends on why they disagree: a question with several valid answers, a contested topic, stale information and a false source each call for different behaviour. Cattan et al. (2025) showed that telling a generator the conflict type improves its responses by about 24 points, but that predicting the type is hard even for frontier LLMs. We study whether typed decision models, which return probabilities over fixed options in a single forward pass instead of generating text, can do this classification fast and cheaply. Using the CONFLICTS benchmark and the original paper's prompt verbatim, we evaluate all 11 decision models served by one commercial inference gateway, from 7 providers, against Gemini models on identical inputs. Asked directly, the decision models reach 50.0--67.0% accuracy; 10 of the 11 match or exceed Gemini 2.5 Flash, the paper's model (61.3%), at 4--39x lower billed cost (2 were free) and 2.6--6.0x lower latency. The current Gemini 3.8 Flash (70.0%) is significantly more accurate than 8 of them, but sending each decision model's least confident quarter of queries to it gives a cascade statistically tied with it for 8 of the 11, at 25--37% of its cost. End to end, answers generated with the types of 10 of the 11 follow the expected behaviour as often as with the LLM's types. Decomposing the taxonomy into yes/no questions lowers accuracy for every model, and a repair fitted on one model does not transfer. Pre-specified diagnostics show that dates play no measurable role and that sensitivity to source order varies widely between models. Decision models detect a planted false source less reliably than the LLM as hard labels, but their probabilities still separate planted from clean sources. We release code, prompts and all model outputs at this https URL.

---


### 115. [TrawMem: Reframing Agent Memory as Task-Oriented Role-Adaptive Workspaces](https://arxiv.org/abs/2610.36918)

**<font color=#1a73e8>作者：</font>** Mingyu Zhang, Zixu Li, Zhiheng Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents rely on memory systems to leverage long-term interactions, yet existing systems typically retrieve memories based on their relevance to the current query and use them as contextual evidence. However, relevance alone does not characterize how a memory contributes to task solving: the same memory may serve different roles across tasks, such as directly supporting the answer or linking to complementary memories with weaker semantic relevance but necessary information. We therefore reframe agent memory systems as Task-Oriented Role-Adaptive Workspaces, where memories are selected and organized by their task-oriented roles and relations. Based on this view, we propose TrawMem, which organizes interaction histories into local threads and constructs task-oriented workspaces by assigning roles and jointly selecting complementary memories. Experiments on LoCoMo and MemGallery with four open- and closed-source backbones show consistent improvements over representative memory systems, with macro-F1 gains of 2.23-3.14 points. On LoCoMo, TrawMem improves the LLM-Judge score over SimpleMem by 4.07 and 4.31 percentage points on Qwen3.5-9B and DeepSeek-V4-Flash, respectively, while requiring approximately 12.8% and 5.1% fewer context tokens, respectively.

---


### 116. [Vision-Language Agents Can Learn in Their Own Latent Worlds](https://arxiv.org/abs/2610.36925)

**<font color=#1a73e8>作者：</font>** Haoxi Li, Sikai Bai, Jianfei Ma 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning from experience is essential for building the next generation of agents that continually expand their capabilities. Pretrained vision-language models (VLMs) already internalize rich world knowledge, yet this knowledge is rarely leveraged to drive policy improvement through online interaction. Realizing this potential efficiently remains challenging, as policy updates shift the agent's interaction distribution, requiring the world model to adapt accordingly, while continually updating large pretrained models is computationally expensive. To address this challenge, we introduce Dwell, a model-based reinforcement learning (RL) framework that reframes a VLM as a recurrent latent transition operator, endowing it with the ability to predict, adjust, and act in latent space. Leveraging the VLM's own representations and its dual role as both world model and policy, the agent continually learns from real interactions to anticipate and evaluate action outcomes, and from latent imagination to improve its behavior. Across five interactive visual environments, Dwell achieves the strongest overall performance among trainable methods while substantially reducing the compute required for imagination, showing that effective world models for VLM agents need not reconstruct the future; they need to predict futures that are useful for action. Our code is publicly available at this https URL

---


### 117. [JevRec: Linguistic Encoding with Jev-like Decision Modeling for LLM-based Generative Recommendation](https://arxiv.org/abs/2610.36937)

**<font color=#1a73e8>作者：</font>** Qiyong Zhong, Jiajie Su, Ming Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generative recommendation (GR) represents items as semantic identifiers (SIDs) and autoregressively generates the next item's SID from interaction history. However, most methods assign the same SID length to all items despite highly unequal interaction frequencies. This uniform design repeatedly incurs the cost of fine-grained codes for popular items, while shortening codes to reduce this cost also compresses the semantic representations of long-tail items. Inspired by the compact forms of frequent expressions in natural language, we propose JevRec to encode items as variable-length words and generate the next item from interaction context. Linguistic encoding retains frequency-dependent semantic prefixes from shared codebooks, producing shorter SIDs for popular items and richer descriptions for long-tail items. Yet predicting a sequence-level length and generating token-level content impose different optimization requirements that may conflict under a shared output head. Our Jev-like decision modeling component therefore predicts a length distribution with a dedicated head and generates content conditioned on length through a separate head while sharing the interaction-history representation. Experiments on three public datasets show that JevRec outperforms all compared baselines across the evaluated recommendation metrics. Further analyses show lower training and inference time than TIGER and reduced gradient conflict between length and content prediction.

---


### 118. [TDLM: Adaptive Temporal Integration for Diffusion Language Models](https://arxiv.org/abs/2610.36940)

**<font color=#1a73e8>作者：</font>** Bohang Sun, Max Zhu, Francesco Caso 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models repeatedly compute representations for unresolved tokens, but conventional denoisers do not explicitly retain these representations for reuse across steps. We introduce Temporal Self-Conditioning Diffusion Language Model (TDLM), which lets each unresolved position attend to its own history of hidden representations within a frozen denoiser. This gives later predictions access to computation already performed. Training uses self-generated trajectories and a simple cross-entropy objective for tokens revealed between consecutively sampled decoding steps, while causal temporal attention permits parallel evaluation during training. On LLaDA, the temporal modules add only approximately 0.84% trainable parameters. Across LLaDA and Dream, the main comparison shows up to 7.15$\times$ faster generation than the corresponding original diffusion language model, with competitive answer quality on the evaluated tasks. These results motivate temporal memory as a practical way to make more effective use of repeated denoising computation.

---


### 119. [Self-Keyed In-Parameter Memorization for External Memory-Free Dialogue Recall in Frozen Language Models](https://arxiv.org/abs/2610.36948)

**<font color=#1a73e8>作者：</font>** XinYu Piao, Myunghoon Ryu, Joongheon Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A large language model maintains conversational content in an external storage that is outside the model and grows as the dialogue continues. This work assumes an environment where a language model has no external memory and no prior knowledge of the future question or its answer. The motivation is to research whether a dialogue can be stored in the model parameters and later answer a question about it. This work proposes self-keyed in-parameter memorization (SKIM), a closed-form method in which the model generates its own questions about each dialogue turn and writes those questions into its parameters as the keys that later retrieve the turn's content. Generating many varied questions for each turn allows a later user question to match one even when phrased differently, and its answer is recalled from the parameters alone. Evaluated on five language models, SKIM recalls most stored dialogue turns from later user questions, and it answers from the model parameters without any external storage.

---


### 120. [DCKV: Learned Transform Coding of the Prompt KV Cache in Hybrid Language Models](https://arxiv.org/abs/2610.36950)

**<font color=#1a73e8>作者：</font>** Egor Maximov, Aleksei Merkelov, Vasiliy Alekseev 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid language models keep a key-value (KV) cache only in their few full-attention layers, but this cache is still the part of a prompt's state that grows with the prompt and that must be stored or moved to reuse it. We present DCKV, a differentiable codec for the KV cache and the first KV-cache codec that is trained end to end. Its transform, its quantizer and its entropy models, which are conditioned on the prompt tokens and on already decoded neighbouring positions, are optimized together against the frozen language model, both for the code length that the entropy models assign and for the change of the model's output. On Qwen3.5-2B, DCKV stores a compressed token in more than 55 times fewer bytes than bf16 at a loss of at most 1.8 points on three long-context benchmarks, and in more than 100 times fewer bytes at a loss of at most 3.6 points.

---


### 121. [Live-OPSD: On-Policy Self-Distillation for Proactive Streaming Large Video Models](https://arxiv.org/abs/2610.36959)

**<font color=#1a73e8>作者：</font>** Kaixuan Du, Xin Wan, Dai Guan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Streaming multimodal assistants must make response decisions while events are still unfolding. They need to recognize when the available evidence warrants a response, produce an appropriate continuation, and remain silent otherwise. Supervised fine-tuning learns from recorded assistant turns, but does not directly train on the response prefixes produced by the evolving policy itself. We introduce Live-OPSD, an on-policy self-distillation method that uses privileged hints available only during training to supervise the policy on its own outputs. The policy first generates a continuation from the streaming context alone. The same model then re-evaluates that continuation with a hint describing the relevant evidence, and the resulting distributions guide the unhinted policy. On Qwen3-Omni-30B-A3B, Live-OPSD attains an average score of 59.64 on LiveProBench, 5.26 points above the strongest continued-SFT baseline, and stays competitive on OVO-Bench (65.84). These results indicate that guiding the policy on its own outputs with privileged hints improves both when and how a streaming assistant responds.

---


### 122. [Do bots feel bad? Assessing empirical evidence for functional valence in LLMs](https://arxiv.org/abs/2610.36962)

**<font color=#1a73e8>作者：</font>** Iwan Williams  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Do LLMs have valenced states, i.e. states that feel pleasant or unpleasant? Recent empirical work has claimed to show that LLMs possess functional valenced states (e.g. ``functional pleasure and pain'' [Ren et al. 2026], ``functional emotions'' [Sofroniew et al. 2026], and ``functional welfare'' [Han et al. 2026]) that play the same causal role as valenced states in cognition and action, without necessarily being consciously experienced. But it remains unexplored how well the identified states fit the functional role of valence as understood in the philosophical and cognitive science literature. Here, I assess the current body of evidence, and argue (i) that key aspects of valence remain untested in LLMs, and (ii) that extant empirical paradigms inadequately distinguish (functional) valence from neighbouring constructs like preferences, value-judgments, valence attributions and role-play. I conclude by sketching some novel experimental approaches to better target (functional) valence itself.

---


### 123. [Proactive Memory for Event-Driven LLM Agents](https://arxiv.org/abs/2610.36967)

**<font color=#1a73e8>作者：</font>** Jinyang Li, Zichuan Fu, Xian Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Proactive LLM agents anticipate service opportunities from ongoing observations and accumulated history. Existing approaches emphasize recent context or retrieval of related memories, providing limited support for validating recurring behavioral regularities and assessing their applicability to the current event. We propose Proactive Memory (ProactMem), which organizes history into recent events, temporal trajectories, and behavioral regularities. Trajectory facts are checked against source events, and regularities are assessed through historical replay before being matched to current conditions. We also construct ProactiveStream, a longitudinal benchmark covering three application scopes, where agents process isolated event streams chronologically under episode-aware opportunity labels. On ProactiveStream, ProactMem achieves an overall effectiveness (F1) of 52.6%, a 21.4% relative improvement over the strongest of five external baselines. Code is available at: this https URL.

---


### 124. [Explicit Regional Representations For Video Quality Assessment](https://arxiv.org/abs/2610.36978)

**<font color=#1a73e8>作者：</font>** Fuyi Yang, Lei Yang, Andrew Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end video quality assessment (VQA) methods leave the regional evidence underlying their predictions largely implicit. We introduce an explicit pixel-level regional representation for VQA, instantiated as a Quality-Relevance Heatmap (QRH) that combines localized degradation evidence with perceptual priors under vision-language model guidance, without requiring pixel-level annotations. We apply QRH to existing VQA models through two deterministic fragment-sampling strategies: distribution-preserving sampling approximates the original sampler's QRH-score distribution without retraining, while quality-aware sampling prioritizes regions with high QRH scores and is paired with fine-tuning. Experiments with DOVER on multiple benchmarks show that the former closely approximates predictions averaged over random samples, while the latter improves most evaluated metrics across popular VQA benchmarks. These results support explicit regional representations as a useful interface for downstream VQA.

---


### 125. [AutoVend: Benchmarking LLM Agents on Long-Horizon Autonomous Vending Operations](https://arxiv.org/abs/2610.36980)

**<font color=#1a73e8>作者：</font>** Qiming Shi, Yikun Li, Beidi Luan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are extending agent-mediated commerce on the Web from shopping for consumers to operating businesses for sellers. In online-to-offline (O2O) commerce, decisions are issued through Web-based platforms but realized through costly physical execution. Evaluating such agents requires going beyond individual transactions to ask whether decisions made online turn into sustained economic returns. We introduce AutoVend, a benchmark in which one LLM agent manages 20 vending machines across five site types through a Web-based operating interface for 180 simulated days. Its data-grounded simulator combines a shared warehouse, procurement lead times, paid replenishment, inventory expiration, and recurring operating costs. We evaluate five LLM agents against a rule-based inventory-control baseline and diagnose their site coordination, execution, and performance over time. Four of five evaluated LLM agents fall short of this baseline, and returns per dollar of inference cost rank models differently from returns alone. Operational analyses show that gains in individual metrics do not consistently yield stronger economic growth, as inventory and execution costs erode these gains. Trajectory analysis further reveals difficulties in grounding feasible actions, managing inventory commitments, and converting feedback into effective policy revisions.

---


### 126. [Advancement or Acceleration? How Data Curation Improves LLM Training](https://arxiv.org/abs/2610.36983)

**<font color=#1a73e8>作者：</font>** Jiaxing Wang, Zicheng Zhang, Deping Xiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While data curation is widely credited with improving large language model training, a basic question remains unresolved: does curation expand what a model can ultimately learn, or merely reach the same solution faster? In this paper, we formalize this distinction between advancement (improving the attainable performance) and acceleration (reaching the same performance with less data). Through an analytic characterization and real-world LLM experiments, we show that advancement requires a correctable train-target gap. When the baseline training and target objectives coincide, no curation policy improves the endpoint, although curation may still accelerate training. This reframes advancement as a property of the curation task rather than the curation method. Under a common gap-centric view of data mixture and selection, we operationalize this condition as the $\Delta$-test, an observable discrepancy between the uncurated baseline's training and target losses that is computable prior to expensive curation. Across extensive experiments, an appreciably nonzero $\Delta$ predicts persistent gains, whereas gains near $\Delta=0$ tend to diminish as the training budget grows. Beyond individual methods, our findings recenter data curation on the task itself and point to target-set construction as a promising direction for shaping what curation can achieve.

---


### 127. [LearnPrunerV2: Learnable Progressive Token Pruning for Vision-Language Models](https://arxiv.org/abs/2610.36986)

**<font color=#1a73e8>作者：</font>** Rinyoichi Takezoe, Yaqian Li, Weiren Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have demonstrated remarkable multimodal capabilities but suffer from prohibitive computational overhead due to the massive number of visual tokens. While token pruning is a promising solution, existing methods still suffer from two major drawbacks: 1) unreliable pruning criteria that fail to accurately localize task-specific regions due to inherent attention biases or query-agnostic designs, and 2) suboptimal pruning strategies that employ rigid, non-adaptive schedules, overlooking the dynamic evolution of token redundancy across different model depths. To address these challenges, we propose LearnPrunerV2, which extends the previous two-stage heuristic framework (LearnPruner) into a fully learnable architecture. Specifically, we integrate lightweight learnable modules into every layer of the VLM backbone, which estimate token importance by fusing intrinsic visual saliency with extrinsic query relevance captured via a shadow token. By uncovering a consistent staircase redundancy pattern across VLM layers, we further introduce Budget-Deterministic Pruning (BDP) to establish a hardware-friendly schedule with fixed per-layer budgets. Extensive experimental results across various benchmarks and VLMs demonstrate that LearnPrunerV2 consistently outperform previous state-of-the-art methods. Notably, LearnPrunerV2 preserves 99.8% of the original performance when pruning 77.8% of visual tokens on LLaVA-v1.5, achieving a superior accuracy-efficiency trade-off.

---


### 128. [A Serious-Game Testbed for Self-Governing Human-Machine Institutions](https://arxiv.org/abs/2610.36989)

**<font color=#1a73e8>作者：</font>** Callum Berger, Jeremy Pitt, Stefan Sarkadi  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> AI agents no longer act alone: they cooperate, coordinate and compete within and between groups, increasingly alongside humans who are in, on or out of ``the loop''. Whether such mixed groups can govern themselves is an open question about machine behaviour and human-computer interaction that needs a testbed for hybrid institutions. We present Megabike, a multi-agent simulator and serious game with interdependent arenas for common-pool resource management, cooperative survival and constitutional choice. Riders sharing a megabike must agree their arrangements for steering, pedalling and distributing resources, and their political regime, while negotiating with rival bikes and avoiding an existential threat. Every rule is enforced by the simulator, every action is logged, and any seat can be taken by a human or a machine, so governance can be studied under well-defined metrics. We demonstrate Megabike with forty sessions in which language-model riders with cooperative, lazy, subversive or opposing dispositions chose regimes, elected leaders and expelled one another. The results show that different combinations of agent archetypes could produce unexpected and counterproductive outcomes. We conclude with extensions for systematic experiments mixing human and computational agents.

---


### 129. [The State and Fate of Multilingual, Contextual Evaluation in the NLP World](https://arxiv.org/abs/2610.36990)

**<font color=#1a73e8>作者：</font>** Manan Uppadhyay, Himanshu Beniwal, Prashant Kodali 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual evaluation benchmarks are the primary instrument for assessing whether large language models generalize beyond English, yet the adequacy of these benchmarks has received little systematic scrutiny. We present a data-driven audit of 51 recent multilingual benchmarks spanning 242 datasets and 219 languages, organized around three pillars: coverage, representativeness, and rigor. Our analysis reveals that coverage is wide but thin with 36% of evaluated languages appearing in only a single benchmark, entire regions (Oceania, the Americas, Central Asia) are near-zero, and a stark task equity gap leaves low-resource languages evaluated on only 1-3 task categories versus 14 for high-resource languages. Representativeness is structurally compromised: translation from English remains the dominant construction strategy where 56% of all dataset-language instances are translated introducing artifacts and English-centric framing, while culturally grounded content is concentrated in a handful of community-driven benchmarks with narrow language scope. The ecosystem thus forces a trade-off between breadth and validity. Rigor is undermined by benchmark contamination, including translated benchmark leakage and parallel corpus overlap that evade surface-form detection. We synthesize these findings into concrete recommendations for building evaluation frameworks that are natively constructed, culturally grounded, contamination-aware, and designed to serve the communities whose languages they claim to evaluate. The dashboard with all the metadata collected can be found at this https URL.

---


### 130. [SpectRAG: Weighted Chunk Graphs for Token-Budgeted Context Selection in Multi-Hop Retrieval-Augmented Generation](https://arxiv.org/abs/2610.36991)

**<font color=#1a73e8>作者：</font>** Zafer Sahinoglu, Abdulazeez Mohammed, Buse Yaren Kazangirler 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) systems ground large language models (LLMs) by retrieving external evidence and conditioning generation on the retrieved context. Although dense retrieval is effective for local semantic matching, independently ranked retrieval can return redundant passages, miss cross-chunk dependencies, and provide incomplete evidence for multi-hop reasoning. We propose SpectRAG, a spectral graph-augmented retrieval framework that combines hybrid candidate seeding, weighted chunk graph construction, graph-based expansion, spectral relevance propagation, and token-budgeted context selection. Document chunks are represented by dense semantic embeddings and graph-spectral coordinates derived from a weighted chunk graph whose edges encode semantic similarity, document adjacency, section hierarchy, shared entities, citation links, and similarity between LLM-generated utility questions. At query time, SpectRAG builds a high-recall seed set using exact inner-product search and hybrid relevance signals, expands it over the chunk graph, re-scores candidates using graph proximity and spectral information, and assembles the final context under a fixed token budget. The goal is not merely to retrieve individually similar chunks, but to construct a context that is relevant, diverse, structurally connected, and sufficient for grounded reasoning. Experiments on MultiHopRAG, UltraDomain, and long-document question-answering settings show that SpectRAG improves broad evidence recovery and achieves competitive generation quality against dense, hybrid, HyDE, LightRAG, and NaiveRAG baselines. The results further indicate that graph-spectral structure is particularly useful for inference-oriented and cross-document retrieval, while highlighting trade-offs in early precision, computational cost, and domain-dependent performance.

---


### 131. [CaLLM: Continual Adaptation of LLMs via Non-Parametric Adapter Routing](https://arxiv.org/abs/2610.36994)

**<font color=#1a73e8>作者：</font>** Bilge Celik, Anna Vettoruzzo, Joaquin Vanschoren  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual adaptation of large language models (LLMs) to evolving task distributions while mitigating catastrophic forgetting remains an open problem. Existing strategies often struggle to scale or lack a robust mechanism for zero-shot task-to-expert assignment. We introduce CaLLM, a framework that resolves these tensions by combining metric-based meta-learning with modular parameter isolation via lightweight adapters. First, CaLLM projects each input batch into a task-agnostic embedding space to find its nearest prototype. It then routes the batch to the specific adapter specialized for that data distribution. This formulation provides (i)~controllable cross-task interference by design, (ii)~constant computational complexity regardless of task count, (iii)~seamless integration of novel distributions through prototype expansion, and (iv)~regime agnosticism as the local routing decision enables a unified approach to both online and offline settings. Our experiments demonstrate that this routing mechanism discovers semantically coherent task groupings while facilitating constructive interference between similar tasks, and keeping overhead at a minimum. Across diverse and fine-grained continual learning benchmarks, CaLLM consistently outperforms traditional isolation and replay methods, establishing prototype-based modular routing as a principled and scalable approach to lifelong adaptation of LLMs.

---


### 132. [Meta Models: Models that Model Learning](https://arxiv.org/abs/2610.37001)

**<font color=#1a73e8>作者：</font>** Peihang Li, Ziming Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Every neural-network training run produces not only a model, but also evidence about how models learn. Can these accumulated experiments enable us to predict and compare new training runs before executing them? We study meta-models: models that predict the learning behavior of other models. From this perspective, final-performance prediction, learning-curve prediction, and hyperparameter selection are different queries to the same training response function. We take a first, humble empirical step toward this goal: treating real language-model training records as native numeric data, we find that an off-the-shelf tabular in-context learner, TabPFN, can match or outperform a fine-tuned LLM meta-model in multiple evaluated settings. Whereas recent work fine-tunes LLMs on tokenized configurations at a cost of tens to hundreds of GPU-hours, TabPFN requires seconds of fit-and-predict time without task-specific weight updates. We argue that meta-modeling is better treated as its own numeric modality rather than as a text task for LLMs. Going one step further, augmenting TabPFN with Kolmogorov-Arnold Networks (KANs) further improves accuracy on selected prediction tasks. Finally, we pre-registered a forecast of the Marin Hero Run, a 535B-parameter public training run, whose ground truth is revealed point by point as training progresses, putting meta-model predictions to the test against training outcomes not yet observed at the time of forecasting.

---


### 133. [V-LUMEN: Visual Lookup Memory for Embedding Scaling in Vision-Language Models](https://arxiv.org/abs/2610.37019)

**<font color=#1a73e8>作者：</font>** Miso Choi, Daekeun Kim, Eunji Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Embedding-level scaling expands the capacity of language models through lookup-based memory rather than by increasing model depth, width, or dense computation. Extending this idea to vision-language models (VLMs) is challenging because visual features are continuous, spatially structured, and query-dependent, unlike discrete text tokens that naturally support n-gram lookup. We introduce V-LUMEN, a visual lookup memory for VLMs. V-LUMEN discretizes visual features with a frozen codebook, builds spatially aware memory keys through spatial aggregation-based hashing, and modulates them with text-conditioned relevance signals; all addressing is non-parametric, and the retrieved embeddings are fused into the backbone through a gated residual pathway. On five reasoning-intensive benchmarks, V-LUMEN substantially improves a frozen Qwen3-VL-2B backbone and transfers zero-shot to three benchmarks whose images are disjoint from the training data. At a matched parameter budget, moving part of a LoRA or MoE adapter's capacity into V-LUMEN preserves accuracy on two backbones, indicating that external visual memory is an independent capacity axis rather than a stronger adaptation method. Because lookup cost is constant in table size and incurred only once at prefill, this capacity grows in storage rather than in per-token compute. Code is available at this https URL.

---


### 134. [Zooming without Zooming v2: From Seeing Details to Connecting Evidence for Generalizable Multimodal Perception](https://arxiv.org/abs/2610.37037)

**<font color=#1a73e8>作者：</font>** Lai Wei, Yatai Li, Liangbo He 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal perception forms the foundation of multimodal intelligence. In particular, spatial perception and multimodal long-context understanding are two pivotal tasks that underpin embodied AI and multimodal agents. However, synthesizing targeted, high-quality training data for these tasks remains difficult and costly. Our key insight is that these tasks share an underlying capability, which we call connecting evidence: identifying relevant visual facts, binding them to the correct entities, recovering their relations, and composing them into an answer. Crucially, targeted training data are far easier to synthesize for this capability than for these tasks themselves. To strengthen this capability, we propose EvidenceConnect, an easy-to-implement data synthesis framework that uses zoomed views of related regions within a single image to generate questions requiring comparison, aggregation, or chaining of visual evidence. To ensure quality, a reference answer is retained only when independent VLMs agree on it, and region-ablation tests discard questions whose answer survives the removal of selected regions. We then train base VLMs on the resulting data with RLVR, obtaining Zooming without Zooming v2 (ZwZ2). Although the synthesized data are not tailored to any downstream benchmark, ZwZ2 improves fine-grained and spatial perception, with further gains on embodied spatial reasoning, multimodal long-context understanding, multimodal agent tasks, and general visual reasoning. These results establish EvidenceConnect as an effective framework for supervising evidence connection and suggest that strengthening this shared capability leads to more generalizable multimodal perception.

---


### 135. [Guided-RLVR: Guided Exploration in Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2610.37041)

**<font color=#1a73e8>作者：</font>** Bo Yang, Zishuai Zhang, Weihua Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has shown strong empirical gains in improving the reasoning ability of large language models (LLMs) on tasks such as mathematics and programming. However, recent studies have shown that RLVR rollouts often collapse onto a narrow set of reasoning trajectories, limiting the explored reasoning space. Motivated by findings that thinking tokens at critical steps serve as critical structural elements in LLM reasoning pathways, we propose Guided-RLVR, a novel approach that augments RLVR with a lightweight controller. The controller strategically injects semantically meaningful steering tokens into the sampling distribution, encouraging the model to approach problems from multiple reasoning perspectives and thereby expanding the exploration space. Experiments on mathematical reasoning and code generation benchmarks show that Guided-RLVR consistently outperforms existing RLVR methods while producing more diverse reasoning trajectories.

---


### 136. [Learning to Code the World: Harness Evolution for Compositional 3D Reconstruction](https://arxiv.org/abs/2610.37046)

**<font color=#1a73e8>作者：</font>** Haoyu Yao, Chenguo Lin, Ruize Du 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing editable and compositional 3D scenes from a real image requires jointly reasoning about geometry, object structure, and spatial relationships. We introduce SceneEvolve, a framework that represents 3D scenes as executable code and improves reconstruction by evolving the harness around a small open-source agent. SceneEvolve combines SceneAct, a compositional semantic action interface built on parameterized primitives, hierarchical composition, and semantic spatial relations, with SceneHarness-RSI, which leverages a stronger teacher agent to iteratively evolve the harness using feedback from development-set reconstructions. Throughout harness evolution, the model parameters, action semantics, and execution backend remain fixed. The resulting harness provides a reusable reconstruction procedure that enables the small open-source model to reconstruct unseen scenes without parameter updates or teacher assistance. Across two in-domain datasets and one out-of-domain dataset, SceneEvolve with the comparatively compact Qwen3.8-27B model improves all four evaluated reconstruction metrics while reducing mean inference time by 47.0% relative to the base model. More notably, despite relying on a substantially smaller model, SceneEvolve achieves 32.3% higher reconstruction quality than the large proprietary GPT-5.6-Sol model, while reducing mean equivalent deployment cost by 59.8%. Furthermore, the harness evolved using Qwen3.8-27B also generalizes to Kimi-K3, achieving comparable reconstruction performance to GPT-6-Astra. The project page is this https URL.

---


### 137. [Blindfold: Keeping the Audit Coin Secret from LLM Agents](https://arxiv.org/abs/2610.37055)

**<font color=#1a73e8>作者：</font>** Wei Zhu, Meiyun Zuo, Huiping Sun  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Audit-based certification bounds the violation rate of an LLM agent by auditing a random fraction $\varepsilon$ of actions and reweighting the audited labels; its validity is meant to rest only on the defender's audit coin. We show that it also rests on a confidentiality property: the coin must not interfere with the agent's view before the action commits, at a time the agent chooses. We call this pre-commit noninterference (PNI) and measure its violation by $D_{\mathrm{A}}$, the total-variation distance between the agent's views under the two coin values. PNI is necessary and sufficient for an unbiased certificate against adaptive agents, the worst-case bias is $(1-\varepsilon)D_{\mathrm{A}}$, and no procedure that sees only audited labels can pay less. Leakage composes across steps, a resource shared across episodes opens a channel of computable size, and raising the audit rate cannot restore validity. On a monitor we built, a silent audit changes no output but adds latency that tool timestamps expose, and the agent can enlarge it. A real LLM agent follows an injection that names a visible audit notice (generic, tool, and timing clauses have no effect); over that channel the plain certificate fails on measured labels and, by a post-hoc analysis, in a live run on a pre-registered schedule, while a silent audit restores it. A fresh coin per audited call closes the timing channel; padding only narrows it.

---


### 138. [Exploring the Limits of the Delta Learning Hypothesis: Single-Pair Generator Biases in Direct Preference Optimization](https://arxiv.org/abs/2610.37058)

**<font color=#1a73e8>作者：</font>** Giuseppe Curci, Stefano Simonazzi, Andrea Molinari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Direct Preference Optimization (DPO) typically relies on preference pairs generated from diverse model pools and ranked by an external LLM judge. The recently proposed delta-learning hypothesis suggests that comparable supervision can instead be obtained from a single pair of models by treating the larger model's response as preferred. We investigate the limits of this approach across model families and scales. We show, both theoretically and empirically, that fixed model pairs introduce systematic, generator-dependent biases that are predictive of the preference label independent of response quality. Consequently, DPO trained on single-pair data consistently underperforms multi-model preference data, despite the larger generator producing higher-quality responses, and we trace this gap to training dynamics consistent with reward hacking on these biases. We further show that simply increasing the number of generators, even without an external judge, is enough to partially mitigate this effect. Our results highlight generator diversity as a critical factor in preference-data construction.

---


### 139. [EnergyCal: Taming Loss Spikes in Muon-Family Optimizers for Sparse MoE Training](https://arxiv.org/abs/2610.37062)

**<font color=#1a73e8>作者：</font>** Masato Fujitake  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse mixture-of-experts (MoE) language-model training can exhibit large loss spikes with Muon-family optimizers. We introduce EnergyCal, a lightweight rule that attenuates routed-expert updates according to the normalized squared Frobenius norm of their finite-step Newton-Schulz directions. EnergyCal leaves the spectral transform unchanged and adds no persistent optimizer state. We evaluate it on a 4B-parameter MoE model. Against a development-selected, lower-learning-rate MuonH recipe, EnergyCal-MuonH reduces mean thresholded loss-spike burden by 99.51% and final geometric-mean perplexity by 4.06%, with a modest throughput cost. With plain Muon at matched nominal learning rate and weight decay, the reduction in mean spike burden averages 95.98% across the two tested exponents, accompanied by small endpoint improvements. These findings support stabilization both with and without Hyperball in the evaluated setting.

---


### 140. [Hierarchical Low-Rank Reparameterization for Parameter-Efficient](https://arxiv.org/abs/2610.37068)

**<font color=#1a73e8>作者：</font>** Rong Huang, Yi Xiong, Yuan-Yuan Cheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning (PEFT) methods adapt large models by introducing a small number of trainable parameters. However, we find that these parameters still contain redundancy and can be further compressed while maintaining strong task performance. To this end, we propose a novel hierarchical low-rank reparameterization method. Its core idea is to reorganize the trainable parameters of PEFT methods into an approximately square matrix and then express it via a low-rank decomposition, which can be applied recursively. This forms a multi-level structure with factors compressed level by level, drastically reducing the number of trainable parameters. In our experiments, we combine this reparameterization with LoRA, DoRA, MoSA, and RaSA. We evaluate commonsense reasoning on LLaMA-3.1-8B and Qwen2.5-7B, with additional GSM8K math reasoning experiments on LLaMA-3.1-8B. Under comparable trainable-parameter budgets, our method combined with LoRA or DoRA achieves better performance. Furthermore,when the parameter count of the original methods is compressed by approximately an order of magnitude, our method can still maintain competitive task performance and even surpass the corresponding baselines in average accuracy across the eight commonsense reasoning benchmarks.

---


### 141. [Correctness Conditioning as Selection in Chain-of-Thought Faithfulness Evaluation](https://arxiv.org/abs/2610.37070)

**<font color=#1a73e8>作者：</font>** Yueer Pan, Yuexi Pan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Restricting chain-of-thought (CoT) faithfulness evaluation to correctly answered instances changes the population being measured. We study this selection step in a seven-variable structural causal model and derive the exact observed gap $\Delta = \operatorname{Cov}(A, C)/P(C=1)$. The model distinguishes difficulty confounding from shortcut-induced collider bias and states the conditional-independence assumption needed to express the gap through latent response propensities. A protocol review of 18 papers distinguishes answer-correctness restrictions from agreement-based selection, benchmark construction, and training-data filtering. We evaluate four sub-ceiling deployments on arithmetic tasks and observe positive selection gaps in all four. The primary GLM-5.3 run yields a +7.4 percentage-point gap ($n = 1000$, $p < 0.0001$), and pooled Cochran-Mantel-Haenszel analysis gives OR = 1.70 ($p < 10^{-6}$). An assumption-free covariance decomposition assigns 42.8% of the GLM-5.3 gap to between-stratum variation in interventionable-operation count, leaving the majority unattributed. When counterfactual compliance is observable for every instance, evaluating all traces directly estimates population faithfulness without correctness filtering.

---


### 142. [OpenGray: a benchmark for evaluating the decisions of radiotherapy planning agents](https://arxiv.org/abs/2610.37081)

**<font color=#1a73e8>作者：</font>** Humza Nusrat, Kundan Thind  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Background and purpose: Radiotherapy planning agents based on large language models (LLMs) decide when to submit a plan or request review but are evaluated mainly by dose. This study developed OpenGray, a benchmark of planning tasks with known correct decisions. Materials and methods: OpenGray adds tasks with known answers to the OpenKBP-Opt head-and-neck dataset, including two contradictions with dose goals proven incompatible and a feasible control with a stored plan meeting every hard goal. Four systems, from a rule-based planning script to a full LLM agent, were evaluated on 30 patients, the LLM-based ones with a commercial (Terra) and a local (Ministral 3 8B) LLM. Decisions, achieved dose, problem recognition, and technical failures were recorded and also read from logs of 39 stereotactic radiosurgery runs of SAGE, a clinical LLM agent. Results: With Terra, the script preceded by an LLM review and the full agent had decision accuracies of 95.4% and 92.1%, respectively, yet escalated only 50% (95% confidence interval, 25-75%) and 25% (10-40%) of overlap contradictions, which required arithmetic on the anatomy. All four systems submitted every feasible control, but 24% of these plans missed a hard goal that the stored plan had met. In four SAGE runs, one goal failed at every attempt; the agent identified it in every reply but had no action for stopping. Conclusions: Favorable aggregate scores concealed specific decision failures. Planning agents should be evaluated on their decisions as well as their dose and given an explicit action for stopping and requesting review.

---


### 143. [On the Sparsity of Direct Preference Optimization: Weight Disentanglement in the NTK Regime](https://arxiv.org/abs/2610.37085)

**<font color=#1a73e8>作者：</font>** Kensuke Sasaki, Issei Sato  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Direct Preference Optimization (DPO) has been widely adopted for aligning language models with human preferences. Recent empirical work has revealed that DPO induces remarkably sparse parameter updates, yet no theoretical explanation for this phenomenon has been offered. We analyze DPO's optimization dynamics under a neural tangent kernel linearization and show that the logistic structure of the DPO loss gives rise to an implicit maximum-margin bias. Building on this observation, we introduce the concept of dual sparsity: the DPO update direction is a sparse linear combination (data-level sparsity, driven by support vectors) of sparse gradient feature vectors (parameter-level sparsity, arising from gradient cancellation between preferred and dispreferred responses). We formalize this structure in our main theorem, bound the number of support pairs by a margin-dependent spectral quantity, and present a framework relating dual sparsity to weight disentanglement---a condition favorable for model merging. Experiments on GPT-2 Small and Medium and on 7--9B instruction-tuned models (Llama-3-8B, Mistral-7B, Gemma-2-9B) with the Anthropic HH-RLHF and UltraFeedback datasets confirm both sources of sparsity, and experiments on GPT-2 show that DPO reduces cross-task interference by up to $35{\times}$ compared to supervised fine-tuning.

---


### 144. [Learning to Look Beyond Screens: Transferable Visual Observation from GUI Grounding](https://arxiv.org/abs/2610.37093)

**<font color=#1a73e8>作者：</font>** Ruilin Yao, Xinyu Qiu, Tianyu Zou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual perception is evolving from passive recognition toward active, task-oriented observation. We investigate GUI grounding as a scalable source of spatial supervision for learning observation behaviors that transfer beyond interfaces. We introduce LBS (Look Beyond Screens), a vision-language model trained through supervised initialization on teacher-generated GUI grounding trajectories, followed by reinforcement learning for multi-turn crop-and-inspect decisions. Under fixed inference settings, LBS models based on Qwen3.5-35B-A3B and Qwen3.8-27B consistently improve over their corresponding baselines. Gains beyond supervised fine-tuning transfer to PerceptionBench for both backbones and to HR-Bench and ChartQAPro for Qwen3.5-35B-A3B, supporting observation strategies that generalize beyond GUI-specific imitation. Further analysis suggests complementary roles for the two stages: SFT establishes visual inspection primitives, while RL improves their downstream effectiveness. These findings support GUI grounding as a practical supervision paradigm for transferable active visual perception and broader multimodal reasoning. Our code and model are publicly available at this https URL and this https URL, respectively.

---


### 145. [SplatScout: Query-Driven Part-Level Referring Segmentation in Gaussian Scenes](https://arxiv.org/abs/2610.37098)

**<font color=#1a73e8>作者：</font>** Yihan Zang, Da Li, Shinkyu Park 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing referring segmentation methods on Gaussian scenes primarily target whole objects, relying on segmenter-generated candidates from which a vision-language model (VLM) selects. Such predetermined fixed candidates may omit fine-grained parts needed as targets or cues for identifying objects. We introduce SplatScout, a query-driven, closed-loop approach that places perception under VLM control. The model actively selects views, directs segmentation, and inspects rendered 3D results to refine its predictions. For part-level evaluation, we introduce PartRef-ScanNet++, comprising 261 manually verified queries across 12 ScanNet++ scenes with mesh-derived ground truth. On PartRef-ScanNet++, SplatScout achieves 0.538 mIoU, substantially outperforming existing methods. Ablations demonstrate the benefits of iterative refinement, while comparisons across VLM backbones highlight the importance of effective tool-feedback utilization. SplatScout also achieves higher scores on four existing referring benchmarks. Code and the PartRef-ScanNet++ benchmark are available at this https URL.

---


### 146. [Text Generation in Low-Resource Languages Using Human-Curated Vocabularies](https://arxiv.org/abs/2610.37105)

**<font color=#1a73e8>作者：</font>** Michael Christlambert Sinanta, Muhammad Dehan Al Kautsar, Amanda Nurul Izzah 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Synthetic text generation offers a promising approach to alleviating data scarcity in low-resource languages. However, its effectiveness is inherently limited for languages that are scarcely represented, or entirely absent, in an LLM's pretraining data. At the same time, many such languages have human-curated vocabularies that provide rich lexical and semantic information, often accompanied by grammatical information such as part-of-speech labels. In this work, we ask whether LLMs can leverage these resources to generate coherent text in extremely low-resource and unseen languages. We introduce a framework that combines human-curated vocabularies with a small number of human-written exemplars that provide syntactic signals, while sampling candidate words according to a Zipfian distribution. Across languages with varying levels of resource availability, we evaluate the generated text using lexical diversity, off-target ratio, and human judgments of fluency. Our results show that reasoning-enabled LLMs can generate fluent text even in extremely low-resource languages, with particularly strong results at the sentence level and promising performance at the paragraph level. Our findings highlight a practical pathway for bootstrapping synthetic data in low-resource languages, expanding the amount of usable text even when existing digital resources are extremely limited. Our source code is available at this https URL.

---


### 147. [Self-Regularized Flow Language Models](https://arxiv.org/abs/2610.37115)

**<font color=#1a73e8>作者：</font>** Theodoros Kouzelis, Spyros Gidaris, Nikos Komodakis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce SERF (Self-Regularized Flow Language Models), a simple self-supervised framework for improving continuous diffusion language models by exploiting the denoising trajectory itself. While continuous flow-based language models offer a promising alternative to autoregressive generation, their training objectives typically rely on supervision from clean target tokens, leaving the denoising trajectory underexploited as a learning signal. SERF addresses this limitation through noisy-to-clean self-distillation: an exponential moving average (EMA) teacher receives a cleaner version of the student's noisy input along the same interpolation path and provides additional supervision. We investigate two variants: SERF-L, which aligns the student's intermediate representations with deeper teacher representations, and SERF-P, which aligns their output token distributions, either at the student's output or at an early student layer. All variants augment the standard training objective without requiring external pretrained models or modifying the inference procedure. Experiments across three continuous language-model paradigms (one-hot FLM, latent ELF, and hyper-spherical S-FLM) demonstrate substantial improvements in training efficiency, generation quality, and few-step generation. In particular, SERF achieves up to 7.7x wall-clock training acceleration on OpenWebText, improves MAUVE by 24.3% and GSM8K accuracy by up to 28.8%, and matches baseline performance with up to 64x fewer sampling steps. These results establish noisy-to-clean self-distillation as an effective approach to improving continuous diffusion language models.

---


### 148. [Prospector: learning a compact graph traversal policy for scientific reasoning](https://arxiv.org/abs/2610.37121)

**<font color=#1a73e8>作者：</font>** Haiqian Yang, Markus J. Buehler  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific reasoning in specialized engineering fields depends on knowledge scattered across the literature, often proprietary and absent from frontier LLM training data. In such domains, frontier models tend to give generic answers. Knowledge graphs (KGs) can ground LLM reasoning. Because a graph is too large to provide in full, typical LLM+KG systems preselect a portion, deciding relevance before reasoning begins. Here we train a compact model, Prospector, to reason over a domain knowledge graph by traversing it step by step, seeking evidence in light of what it has already found. Prospector calls a small set of tools one at a time to progressively build its context, and answers with a chain of evidence that can be checked edge by edge against what its tools retrieved from the graph. On a knowledge graph built from the semiconductor-manufacturing literature, Prospector approaches the strongest off-the-shelf models given the same graph and tools, and it far exceeds off-the-shelf models answering closed-book or from a pre-selected portion of the graph. Although trained only on the semiconductor graph, Prospector transfers to unseen knowledge graphs from three other distinct fields: bio-inspired materials, per- and polyfluoroalkyl substances (PFAS) and materials properties. Served on a single GPU, Prospector answers faster and at a fraction of the cost of a hosted service, while keeping proprietary data on the owner's hardware. We find that the policy's latent state is indicative of its next move on both seen and unseen graphs, and modulating the latent state can steer the policy from one behavior mode to another. These results suggest a practical LLM + KG paradigm for scientific and engineering reasoning over private data, in which a compact model trained on a graph from published literature transfers its traversal to unseen graphs that stay with their owners.

---


### 149. [Mechanistic Failure Modes of Weight Pruning in Transformer Language Models](https://arxiv.org/abs/2610.37126)

**<font color=#1a73e8>作者：</font>** Nabeelah Faumi, Deshan Sumanathilaka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pruned language models are judged almost entirely by accuracy and perplexity, which assumes that preserved output behaviour implies preserved internal computation. We test this assumption with a factorial pruning study on GPT-2, crossing two importance criteria (magnitude, random), two component types (attention heads, MLP neurons) and three sparsity levels (3%, 50%, 70%). Using the fully characterised indirect object identification (IOI) circuit as ground truth, we measure circuit integrity with activation patching, path patching and direct logit attribution. We find two qualitatively distinct failure modes. Magnitude head pruning >= zeroes the circuit: output-facing heads are removed, and the model falls to near-chance. Magnitude neuron pruning at 30% inverts it: all 26 circuit heads remain intact, but Name Mover contributions flip sign, and the model systematically prefers the wrong name (17.7% accuracy). Perplexity ranks it as less damaged than random head pruning (74.6 vs 140.1). A replication of the Greater-Than circuit shows that the critical component type depends on the circuit's architecture. These results show that output metrics and structural checks can both miss mechanistic damage, motivating circuit-level causal analysis as a complementary evaluation of compressed language models.

---


### 150. [What Survives Distillation? A Mechanistic Interpretability Study of GPT-2 and DistilGPT-2](https://arxiv.org/abs/2610.37157)

**<font color=#1a73e8>作者：</font>** Nabeelah Faumi, Deshan Sumanathilaka  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation compresses large language models into compact students that preserve aggregate metrics, yet the mechanistic consequences of depth-reduction distillation remain largely uncharacterized. This work applies linear CKA, logit lens analysis, attention pattern decomposition, sparse autoencoder feature statistics, and activation patching to compare GPT-2 and its six-layer student DistilGPT-2 across two canonical circuits: the Indirect Object Identification (IOI) circuit and the Greater-Than (GT) circuit. The results reveal a compression-collapse dichotomy: the IOI circuit suffers complete mechanistic collapse (DistilGPT-2: 35.2% accuracy vs. 94.8%, zero name-mover preservation), while the GT circuit survives with 87.7% task performance recovery through active remapping of the teacher's layer-9 comparison head into student layer~4 (mean Pearson r = 0.945). These findings demonstrate that circuit compressibility governs mechanistic survival under distillation, and that aggregate metrics are insufficient diagnostics for circuit integrity.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-226](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
