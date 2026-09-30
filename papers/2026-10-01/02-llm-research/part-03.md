# 🧠 大模型相关研究 | 2026年10月01日

> 本类共 **515** 篇论文：已确认 **473** 篇，待复核 **42** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

---

### 101. [Training LLMs to Verbalize Evaluation Awareness](https://arxiv.org/abs/2609.36316)

**<font color=#1a73e8>作者：</font>** Usman Anwar, Sahar Abdelnabi, David Krueger  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluation awareness (EA) can cause large language models (LLMs) to behave differently during audits than in deployment, yet measuring and accounting for EA remains challenging. We introduce verbalization training (VT), a method for making LLMs less reticent about verbalizing evaluation awareness while avoiding to supervise the latent belief itself. VT uses a model's spontaneous verbalizations as evidence that awareness is present and truncates each rollout immediately before the verbalization, producing training prefixes at which the model is presumed to be aware. The model is then trained with an RL objective designed to increase verbalization in a calibrated way. Across Qwen3.6-35B-A3B, Kimi K2.6, and Inkling, VT increases verbalized EA by 2.4-2.9 times and transfers to held-out agentic settings, while measured latent EA and behavior remain largely stable. In a causal experiment, we independently implant meta-knowledge about evaluations through synthetic-document fine-tuning and show that VT-induced verbalizations reflect the richer knowledge acquired by the model.

---


### 102. [StateTape: Action-Conditioned Evidence Lifecycle Modeling for Long-Horizon Coding Agents](https://arxiv.org/abs/2609.36319)

**<font color=#1a73e8>作者：</font>** Ziyang Yu, Liang Zhao, Bowen Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite the recent success of coding agents built on large language models, it remains challenging to run them over long horizons, since every observation is appended to the context and the context grows with each one. History-based maintenance is a common remedy, which masks or summarizes old observations, or prunes what a model reads as useless, and bounds the context at little cost. However, it decides from the text of the history alone and sees nothing of how the code is connected. Since a coding agent edits code many times over a single task, and each write can change what code elsewhere means, such maintenance may keep records a write has falsified, drop ones that still hold, and miss code the agent needs next. To overcome these challenges, this paper proposes StateTape, a novel and scalable framework that rewrites a coding agent's context as the repository changes rather than as the context grows. The key idea of StateTape is to model the repository as a symbol-level code graph, whose dependencies and language rules expose which symbols a write can affect. Upon this graph, a tape marks the symbols each write changed, which turns staleness from an inference about text into an observation of the agent's writes. We propose a per-write procedure in which the tape nominates the records a write could have falsified while a small manager model settles what the write log cannot, and further provide a theoretical analysis and TraceBench, a benchmark that labels what an agent is holding against what is actually needed. Empirically, we demonstrate that StateTape can effectively clear falsified records and retrieve what is needed, and thus achieve a higher resolve rate in all experiments spanned by six coding agents and three edit-heavy benchmarks with little computational overhead.

---


### 103. [Periodic Weak Spots: Phase Sensitivity from Chunked KV-Cache Compression](https://arxiv.org/abs/2609.36322)

**<font color=#1a73e8>作者：</font>** Xingyu Zhu, Ziheng Cheng, Ang Lv 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chunked KV-cache compression reduces the memory and attention costs of long-context inference by compressing windows of consecutive tokens into fewer cache entries at a fixed stride. Such compression also introduces a new positional coordinate: a token's phase, or its position relative to compression-window boundaries. We uncover a systematic asymmetry in models using such compression: the same information can be easy to retrieve at one phase and difficult at another. We call this periodic variation in retrieval performance phase sensitivity. In large open-weight models with such compression, long-context retrieval accuracy can differ by up to 40 percentage points across phases, revealing periodic weak spots that average benchmark scores can conceal.
To investigate this behavior, we pretrain a family of transformers from scratch across multiple KV-compression designs, reproducing phase sensitivity across the variants. Mechanistic analysis using causal interventions in these models reveals phase specialization: different attention components contribute asymmetrically to retrieving information at different source phases. We further analyze idealized retrieval models, showing how gradient flow dynamics may favor sharp phase specialization. Evaluating models with chunked KV-cache compression thus requires measuring across compression phases: high average accuracy can coexist with systematic positional failures.

---


### 104. [PILLAR: Private Inverted-Index Lexical Lookup for Augmented Retrieval](https://arxiv.org/abs/2609.36326)

**<font color=#1a73e8>作者：</font>** Truong Son Nguyen, Daniel Blackley, Ni Trieu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) hands the user's query to whoever hosts the corpus. We propose PILLAR, a Privacy-Preserving RAG (PPRAG) system based on Private Information Retrieval (PIR) in which a client utilizes the k documents most similar to their query from a server-held and publicly known corpus to respond to their query, while the server learns nothing about the query, either its terms or its access pattern. Prior PPRAG constructions rely on dense retrieval alone, translating approximate nearest-neighbor search into many query-dependent rounds of PIR, and pay for it in both latency and retrieval quality. PILLAR instead performs private hybrid retrieval in two stages. A sparse stage issues a small, fixed number of PIR queries against a carefully designed index of precomputed BM25 scores, filtering the corpus down to candidates that share terms with the query without the server ever seeing which terms these are. A dense stage then fetches only those candidates' document embeddings and re-ranks them locally, avoiding the many costly PIR queries that private dense retrieval typically requires. We instantiate PILLAR with two protocols that trade latency against retrieval quality, each built on a different private rendering of lexical search. PILLAR-Bin bins posting lists into a hash table and is a single-round design that achieves lower latency than state-of-the-art private retrieval schemes. PILLAR-Tree turns block-max pruning into an oblivious tree traversal combined with cuckoo hash tables and achieves the highest retrieval quality at lower latency than state-of-the-art schemes.

---


### 105. [Adapting Linear-Time Architectures for Tabular In-Context Learning](https://arxiv.org/abs/2609.36337)

**<font color=#1a73e8>作者：</font>** David Schnurr, Felix Sarnthein, Thomas Hofmann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models achieve strong performance by conditioning on labelled examples in context, but softmax attention limits their use on large datasets. Existing linear-time alternatives, however, are mostly causal, and their potential for tabular in-context learning (ICL) remains underexplored. To address this, we (1) revisit causal training setups, (2) compare linear sequence mixers, and (3) investigate their ICL generalisation beyond the pretraining context length. First, we show that the best training setup for causal models resembles next-token prediction. Then, perhaps surprisingly, the most promising linear sequence mixer is causal: DeltaNet outperforms even non-causal linear attention. However, it degrades beyond $2$-$4\times$ the pretraining context length, and existing mitigation strategies such as bidirectionality defer the problem at best. A hidden-state oracle shows that this is not a capacity problem. Instead, our analysis points to an instability in the recurrent state, which drifts in deeper layers of causal models. Since DeltaNet's learned write rates overfit to the pretraining regime, we modulate them with a time-dependent decay schedule intervention to stabilise length generalisation. Finally, re-introducing non-causality by reading out from the final state allows us to closely match a controlled softmax attention baseline on OpenML-CC18 and TabArena.

---


### 106. [StructRL: Online Structured Reinforcement Learning for Long-Horizon Vision-Language-Action Tasks](https://arxiv.org/abs/2609.36352)

**<font color=#1a73e8>作者：</font>** Ziyi Yin, Sangmin Woo, Kang Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models perform well on shorter-horizon manipulation tasks but still struggle with long-horizon tasks that require multiple dependent manipulations from a single command. Online reinforcement learning (RL) can improve these policies through environment interaction, yet many existing methods provide reward only after the complete task succeeds. However, such terminal supervision is sparse and does not distinguish early failures from rollouts that make substantial partial progress. We propose StructRL, an online RL framework that constructs structured intermediate supervision from verifiable subtask completions. StructRL decomposes each task into verifiable subtasks, grants intermediate rewards only after the prerequisite subtasks have been completed, and scales each reward according to completion pace. Across RoboCasa365 and LIBERO-Long with GR00T-N1.5 and pi 0.5, StructRL consistently outperforms evaluated online RL baselines. These results show that verifiable, structured intermediate rewards improve long-horizon VLA post-training. Code is available at this https URL.

---


### 107. [HyperZip: Efficient Data Compression through Personalized Diffusion LLMs with Hypernetworks](https://arxiv.org/abs/2609.36357)

**<font color=#1a73e8>作者：</font>** Thai Nguyen, Khang Tran, NhatHai Phan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown strong potential for lossless data compression, but existing approaches are constrained by the high computational cost and low throughput of autoregressive decoding. We propose HyperZip, an efficient and scalable LLM-based compression framework that leverages diffusion-based LLMs (dLLMs) with Multi-Token Prediction (MTP) to accelerate LLM-based data compression processes. We identify a trade-off in diffusion-based compression, where increasing decoding throughput degrades the compression rate. To mitigate this trade-off, HyperZip employs a hypernetwork to generate data-specific updates from a context representation, adapting the dLLM to the target data without costly fine-tuning, resulting in a low compression rate and high throughput. Extensive experiments show that HyperZip achieves a superior trade-off between compression rate and speed compared with state-of-the-art baselines.

---


### 108. [Better Nearest Neighbor Graph Indices via (Efficient) LLM-Guided Pruning](https://arxiv.org/abs/2609.36359)

**<font color=#1a73e8>作者：</font>** Fangzhou Wu, Haike Xu, Sandeep Silwal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graph-based approximate nearest neighbor search (ANNS) is widely used for large-scale semantic search. Its indices are constructed primarily based on geometric relationships among embeddings of an input dataset (e.g., documents or images), rather than explicitly optimizing for semantic relevance. However, when using these indices for downstream query retrieval, performance is evaluated based on the semantic relevance of the retrieved results to the query. This creates a fundamental "geometry-semantic" mismatch between how the indices are constructed and how their retrieval results are evaluated. While existing LLM-based reranking methods can partially mitigate this mismatch at query time, they leave this underlying structural problem in the graph unresolved. We therefore propose LLM-Guided Graph Pruning (LGP), a general framework that addresses this mismatch directly by leveraging LLM reasoning to refine an existing ANN graph index itself. LGP identifies structurally "low-value" neighbors of nodes and replaces them with LLM-selected alternatives that provide useful semantic information while retaining desired geometric structures of the original graph, including sparsity and efficient navigability. Experiments on representative semantic retrieval benchmarks show that LGP consistently improves end-to-end retrieval performance over both vanilla greedy graph search and LLM-based reranking across widely used graph-based ANN indices such as DiskANN and HNSW.

---


### 109. [Compress to Remember: Learning Compact Memory via On-Policy Distillation for Long Video Generation](https://arxiv.org/abs/2609.36364)

**<font color=#1a73e8>作者：</font>** Xiaoyu Wu, Weihang Guo, Yifei Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Standard video generators do not natively compact historical context into reusable memory tokens. As generation continues, the growing history makes it increasingly difficult to retain information from earlier frames due to long-context degradation. Key-frame-based approaches address this challenge by retaining selected past frames, but can discard information needed for future generation. Rather than relying on frame selection alone, we study whether a frozen video generator can supply the supervision needed to learn a compact representation of the history. We propose Prediction-Aligned Context Compaction (PACC), which uses a learned compressor to aggregate information across past frames into compact memory tokens. We train the compressor through on-policy distillation, using the same frozen generator both as a student when conditioned on compressed memory and as a teacher when conditioned on the full history. The student generates continuations, while the teacher provides targets for the same noisy inputs at each denoising step. Only the compressor is updated to align the student's predictions with these targets. We evaluate PACC on MBench, which jointly measures memory-event coverage and consistency. PACC outperforms the strongest baseline by 6.63 points on Causal-rCM and 3.19 points on Causal Forcing. Evaluation on VBench-Long using MovieGen prompts further shows that PACC produces minute-long videos with generation quality competitive with baselines. Together, these results show that learning to compact historical context can improve long-video memory without modifying the underlying generator.

---


### 110. [Engineering Simplicity: Simple Mechanism Interfaces Steer LLM Agents](https://arxiv.org/abs/2609.36365)

**<font color=#1a73e8>作者：</font>** Kehang Zhu, Anand Shah, David Parkes  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can interaction formats and textual scaffolds help large language model (LLM) agents make better decisions, and do better decisions come with better explanations? We study these questions in auctions and matching, multi-agent environments with explicit rules and known optimal strategies. These settings let us vary how a decision problem is presented while retaining a benchmark for evaluating behavior. Drawing on human-motivated theories of simplicity, we compare interfaces that elicit a complete bid or ranking with sequential interfaces that make safe choices easier to identify. We then hold the interaction format fixed and vary reasoning scaffolds and rule descriptions. Across four model families, the ascending auction interface substantially reduces bid deviations. The matching comparison also shows why sequential responses require different error accounting from complete rankings. Laying out payoff contingencies and explaining why truth-telling is safe also improve choices, whereas prompts to plan through matching rounds or form beliefs about opponents worsen play overall. In auctions, these behavioral gains are not accompanied by corresponding improvements in measured verbal indicators of strategic understanding in the agents' short stated plans. Other prompts change those indicators without improving bids. Our findings suggest that human-motivated theories of simplicity can inform the design of decision environments for artificial agents. They also show why scaffolds should be evaluated through realized choices as well as explanations: improvements in one need not appear in the other.

---


### 111. [AdaKerNet: Neural Kernel Decoding for Task-Adaptive Prediction with Multimodal Large Models](https://arxiv.org/abs/2609.36368)

**<font color=#1a73e8>作者：</font>** Konstantinos D. Polyzos, Eleni Oikonomou, Tara Javidi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large foundation models have been introduced with the promise of efficient adaptation to downstream tasks. Yet, under limited supervision, MLLMs, an important class of large foundation models, remain challenging to adapt to various downstream tasks. Adaptation typically relies either on MLLM parameter fine-tuning or on training neural-based decoders. Both approaches struggle under limited supervision, while fine-tuning additionally requires access to model parameters, which is often unavailable for closed-source models. We introduce AdaKerNet, a novel learnable task-adaptive neural kernel decoder. AdaKerNet is fully agnostic to the parameters of the underlying MLLM and operates solely on its (frozen) rich representations obtained from the diverse available modalities. AdaKerNet relies on (i) a set of learnable, Lipschitz-controlled multimodal features derived from these MLLM representations; (ii) a reference kernel that provides a soft structural prior on those features; and (iii) a lightweight nonlinear neural predictor that adaptively deforms that structure. Learning the kernel representation and the neural predictor jointly within a unified optimization framework allows AdaKerNet to capture features and geometric relationships relevant to the downstream task. Numerical tests across four MLLMs: BLIP-2, LLaVA-1.5, Qwen2.5-VL, and Gemini Embedding 2, and multimodal inputs spanning text, audio, images, and tabular measurements demonstrate significant and consistent improvements over direct MLP, attention-, autoencoder- and kernel-based decoders, across a range of scarce-label budgets, with average error reduction of up to 41% across baselines. These results establish AdaKerNet as an effective approach for prediction from frozen multimodal representations in the scarce label regime. Additional structural ablations highlight the complementary contributions of AdaKerNet's components.

---


### 112. [Audience-Bound Persistent Memory: Authorization Across the Memory Lifecycle](https://arxiv.org/abs/2609.36373)

**<font color=#1a73e8>作者：</font>** Sibo Liu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A personal language agent that acts for its owner across private and shared conversations can learn a fact from one audience and later place it in the context it assembles for another. We study authorization before context across the whole memory lifecycle. Each memory item carries the audience present when it was recorded; derived items are partitioned by audience, receive the intersection of their sources' audiences, or are suppressed; an audience widens only by an explicit, object-specific grant; and an item enters a model attempt only when every current viewer belongs to one of its authorized audiences, with unresolved viewers failing closed to public-only. Under explicit identity, provenance and complete-mediation assumptions, this admission is sound and policy-complete on the exact assembled context, enforced by exclusion rather than by model behavior. We realize it in two independently persisted reference architectures, a flat store and a relationship graph, and, descriptively, in a native agent-memory runtime. In a prospectively frozen confirmation over 10,000 multi-party histories, no forbidden item entered any architecture's context, whereas unscoped retrieval exposed forbidden items in 82% of its contexts. Entitled recall matched policy-equivalent baselines exactly and exceeded unscoped retrieval by 0.30 Recall@5, with a Holm-confirmed advantage that grows with distractors. No architecture produced a wrong-principal substitution, but unscoped substitutions were too rare to establish the prespecified joint decision.

---


### 113. [Quantization Enables Private Dense Retrieval against Malicious Service Providers](https://arxiv.org/abs/2609.36376)

**<font color=#1a73e8>作者：</font>** Louis Tremblay Thibault, Sofiane Azogagh, Marc-Olivier Killijian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Dense retrieval, the key component of Retrieval Augmented Generation (RAG), retrieves the most relevant documents by comparing dense vector representations of queries and passages from a large corpus. In privacy-sensitive applications, the server observes the query and controls which evidence is returned, creating both confidentiality and integrity risks. We formulate private dense retrieval as providing query privacy and retrieval integrity against a malicious server, and develop a two-round cryptographic protocol that provides both guarantees. Our protocol reduces private and verifiable retrieval to multiplication of a committed matrix by an encrypted vector and uses low-bit quantization to make this computation practical. We evaluate the resulting trade-off between cryptographic cost, retrieval quality, and downstream RAG accuracy across six embedding models, four language models, and corpora of up to 2.68 million passages. Our results show that, with a clipped quantizer, three-bit quantization largely preserves retrieval quality and downstream accuracy, while a private query over a corpus the size of a clinical reference requires one to three minutes of server time. These results suggest that private dense retrieval is already practical for moderately sized, privacy-sensitive corpora when minute-scale latency is acceptable.

---


### 114. [LEGO-Anything: Coding Agents for 3D Scene Reconstruction](https://arxiv.org/abs/2609.36380)

**<font color=#1a73e8>作者：</font>** Xirui Li, Peng Shi, Mingwen Dong 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A 3D scene reconstructed from a single image is most useful when represented not as a rendering or a fixed 3D output, but as an explicit scene program whose execution yields a scene that can be inspected, edited, and queried. We present LEGO-Anything, an Image-to-Code framework in which a coding agent iteratively writes and executes Blender code, inspects scenes and renderings, and revises the program. To evaluate end-to-end scene recovery, we introduce LEGO-Bench, a simulator-grounded benchmark with 208 images from 104 diverse indoor and outdoor scenes. LEGO-Bench separately scores artifact validity, visible-surface geometry, and rendered appearance. Its simulator-grounded design enables extensibility and precise automatic evaluation. Among evaluated agents, GPT-6-astra achieves the strongest overall results, with 53.4% indoor and 39.6% outdoor scores, yet substantial gaps remain between delivering valid scene artifacts and faithfully recovering scene geometry and appearance. Analysis of agent construction trajectories reveals three recurring issues: weak scene initialization, regressive edits during iteration, and unreliable self-evaluation. These findings motivate LEGO-Plugin, a training-free harness plugin for more controlled iterative scene construction, which improves all six evaluated models, with relative gains of up to 62.7% in overall score. Finally, we test whether reconstructed scenes can represent natural images and support vision tasks. In LEGO-World, we derive object detections, instance masks, and relative depth as deterministic queries on scenes reconstructed by GPT-6-astra. These readouts show non-trivial performance across all three tasks but fall well short of specialized vision models, suggesting that program-constructed scenes from current coding agents are a promising but not yet sufficiently precise representation of natural images.

---


### 115. [Support-Set Target Leakage in Relational Foundation Models during In-Context Learning: Impact, Detection, and Mitigation](https://arxiv.org/abs/2609.36384)

**<font color=#1a73e8>作者：</font>** Roshan Reddy Upendra, Alexandre Dorais, Joe Meyer 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Relational in-context learning (ICL) conditions predictions on the labeled support examples and their linked tables, creating a failure mode when the support set contains target-derived features that are unavailable for the query. We formulate this problem as support-set target leakage, distinct from leakage during dataset construction, temporal splitting, or representation learning. Here, the target-derived (leaker) columns are present only in the labeled support set during relational in-context inference, while queries remain clean. We construct 14 synthetic leaker types, corresponding to 20 columns, spanning proxies with different noise levels, coverage, modalities, semantic transparency, and relational distances. We evaluate a frozen relational encoder with an ICL head on held-out RelBench databases and use Integrated Gradients (IG) to rank and remove suspicious columns. Our results show that the effect of support-set leakage varies across tasks and relational distances. Target-table leakers cause the clearest degradation, while one- and two-hop leakers are not consistently used by the model. IG ranks target-table leakers highly across datasets and partially recovers performance in settings where leakage has the largest effect.

---


### 116. [Persona Dosing: Calibrated Activation Steering for Graded Trait Control](https://arxiv.org/abs/2609.36388)

**<font color=#1a73e8>作者：</font>** Zehao Jin, Junran Wang, Ruixuan Deng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An activation-steering coefficient sets intervention strength, but requesting a particular degree of persona expression requires a behavioral scale. We study persona dosing: controlling a language model through a trait description and a requested mean intensity. PersonaDose specializes a shared, description-conditioned FLAS controller on persona responses, then calibrates its flow time against measured trait expression. Training responses are not paired with requested target intensities. Across Llama-3.1-8B, Qwen3-8B, and Gemma-3-4B, PersonaDose raises core-trait expression at the Persona Vectors coherence floor of 75 by 33.2, 18.3, and 17.8 points over contrastive activation addition. Calibration-selected settings retain an expression advantage on held-out questions, although the coherence floor does not hold for every trait there. Across seven trained traits, calibrated requests yield mean targeting errors of 4.7-6.2 points over 14-22 calibration-reachable targets out of 28 per model. These results separate the behavioral range learned by a controller from the accuracy of requests within that range.

---


### 117. [ARCagent: An Adaptive Retrieval Calibration Agent for Clinical Question Answering](https://arxiv.org/abs/2609.36392)

**<font color=#1a73e8>作者：</font>** Yuyan Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In diseases where clinical guidelines are incomplete, contested, or mutually contradictory, knowledge completeness and dynamic conflict-aware synthesis are two safety-critical properties that standard Retrieval-Augmented Generation systems do not provide. Therefore, we present \sysname, an adaptive retrieval calibration clinical question-answering agent for ME/CFS, a disease where diagnostic frameworks coexist and major guidelines actively contradict each other on treatment. ARCagent contributes three components. First, a 1,706-chunk, 10-source knowledge base with a structured inter-guideline conflict registry spanning all active ME/CFS diagnostic frameworks. Second, a conflict-aware retrieval calibration pipeline that re-ranks retrieved evidence using query-specific focus and conflict signals. Third, a benchmark scored by LLM-as-Judge, avoiding systematic underestimation averaging 10.1 percentage points caused by keyword matching. ARCagent achieves 95.3%, outperforming all base LLMs. Code is available at this https URL.

---


### 118. [Reward-rate Policy Gradient for Efficient Machine Learning Engineering Agents](https://arxiv.org/abs/2609.36393)

**<font color=#1a73e8>作者：</font>** Muhang Tian, Sherry Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traditional reinforcement learning (RL) techniques focus on maximizing expected cumulative reward, where each action assumes to take a constant unit of time. However, this assumption does not hold for agentic RL tasks such as machine learning engineering (MLE) agents, where actions involve data loading, feature engineering, and model training that take variable durations. Efficiency matters in modern agentic RL where actions are costly. To address this limitation, we adapt from continuous-time RL and Semi-Markov Decision Process (SMDP) formulation and propose Reward-rate Policy Gradient (RPG), where we focus on optimizing the reward rate -- the long-term reward per unit of time. RPG estimates the reward rate from off-policy samples, then charges each action for the time it consumes at that rate. We first conduct theoretical analysis in the bandit setting to establish that RPG approximates the optimal reward rate and empirically demonstrate it outperforms baselines while avoiding enumeration over the policy space, a known issue for an existing method. We then further apply RPG on a small language model (Qwen3.5-4B) with self-improvement loops and empirically show it obtains higher rewards within a fixed time budget than vanilla RL on MLE-Bench and NanoGPT, with a 19.2% and 85.7% margin, respectively. Our method provides a practical solution for optimizing performance under wait time considerations in modern agentic RL tasks, where actions interact with external environments and cost time.

---


### 119. [Calibrated to Whom? Persona and Language Effects on Cultural Values in JEV](https://arxiv.org/abs/2609.36399)

**<font color=#1a73e8>作者：</font>** Bushra Asseri, Abdulaziz Asseri  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Decision-only language models return a probability for every answer option instead of generating text, which makes them attractive as survey respondents and as judges. We audit the cultural values of one such model, TypeSafe's JEV, with the Values Survey Module 2013. We asked it the 24 items as 12 matched Saudi and 12 matched American personas and without a persona, in English and Arabic, under eight ways of formulating the request (288,000 answers). JEV's answers were highly repeatable (ICC 0.997), and without a persona they resembled those of its own American personas. When the persona was Saudi rather than American, the answers moved in the direction of the human Saudi-US difference, reproducing 87% of its size in English but 62% in Arabic, with long-term orientation reversed. A language cross shows that the smaller difference in Arabic comes from the language of the items, not from the language of the persona description. Age shifted the profiles about as much as nationality, gender shifted them more for Saudi than for American personas, and JEV was less confident in Arabic and for Saudi personas. These patterns held in every request design, although the model never generates text.

---


### 120. [From Retrieval to Reasoning: Agentic Mechanism Prediction from Cell Painting Profiles](https://arxiv.org/abs/2609.36406)

**<font color=#1a73e8>作者：</font>** Jiayuan Chen, Botao Yu, Tianyu Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cell Painting is a high-content morphological profiling assay widely used for phenotype-based biological inference, with mechanism of action (MOA) prediction as a central application. Existing approaches largely formulate Cell Painting-based inference as representation matching, assigning predictions from nearby reference perturbations in morphological feature space. However, retrieved neighbors are often noisy and partially misleading evidence due to batch effects, non-specific cytotoxicity, phenotypic convergence, and source-dependent variability. We reformulate Cell Painting-based MOA prediction as a calibrated evidence reasoning problem, where retrieved neighbors are treated as uncertain observations that must be evaluated, compared, and sometimes rejected before supporting a mechanistic conclusion. We propose PhenoAIR, a reliability-aware multi-agent framework that maintains a candidate-centric evidence memory and performs controller-guided refinement over phenotype- and mechanism-side evidence. PhenoAIR uses offline reference-set calibration to weight evidence by source reliability, phenotype stability, and mechanism-level confusion. We evaluate PhenoAIR on a benchmark constructed from JUMP Cell Painting profiles and annotations, covering controlled, realistic, and discovery-oriented open-world MOA prediction settings. PhenoAIR outperforms representation-matching and LLM-based baselines across all settings.

---


### 121. [Eternal Sunshine of the Spotless Mind: Systematically Erasing LLM's Memories](https://arxiv.org/abs/2609.36414)

**<font color=#1a73e8>作者：</font>** Olga Ohrimenko  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We consider persistent LLMs that accumulate memories of their interactions with a user over time. Such LLMs maintain memories using external storage, which they can query to overcome the limitations of a fixed context window. Such systems have numerous practical applications, as they can draw on all past interactions when responding to user queries.
In this paper, we ask whether LLMs can forget information shared with them upon a user's request. We find that current LLMs fail to delete such information---even when they claim to have forgotten it and even when operating with a limited context. To this end, we consider a new direction of study: Deletion of LLM Memories.
We show that naively removing messages that match a user's deletion request is insufficient, since conversations naturally introduce message dependencies that cause information to persist. To correctly handle deletion requests, we propose the DeLLM framework. It dynamically constructs relevant context for each LLM query and maintains a provenance graph of messages to determine which ones must be removed during deletion. Our experiments show that DeLLM achieves a high deletion rate while maintaining utility.

---


### 122. [Support-Set Target Leakage in Relational Foundation Models during In-Context Learning: Model Dependence and Evaluation Reliability](https://arxiv.org/abs/2609.36417)

**<font color=#1a73e8>作者：</font>** Roshan Reddy Upendra, Alexandre Dorais, Joe Meyer 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Relational in-context learning (ICL) uses labeled support examples and their linked relational context to predict labels for new queries. This creates a failure mode when target-derived features are present in the support context but unavailable for the query. We study this setting as support-set target leakage. We construct 20 controlled target-derived features that vary in signal fidelity, representation, semantic transparency, coverage, and zero-, one-, and two-hop relational placement, and evaluate them across 13 RelBench tasks and five relational ICL configurations that vary the ICL head, message-passing depth, pretraining cohort, or relational encoder architecture. We evaluate matched 0-hop, 1-hop, and 2-hop leakage settings, together with a Full leakage condition containing all 20 leaker columns. Within the tested configurations, target-table (0-hop) and Full leakage produce the largest aggregate deviations from clean evaluation, while higher-hop effects are often weaker, consistent with differences in effective exposure associated with temporal reachability, sampling, and aggregation fidelity. Leakage effects are strongly task- and model-dependent and can reverse relative conclusions between model variants even when aggregate changes are small. For leaker detection, we compare an Integrated Gradients (IG)-based screening method with mutual information (MI) and leave-one-column-out (LOCO) on a common Baseline subset. Ranking quality is strongest in the high-impact 0-hop and Full leakage conditions, but detector-based removal does not consistently restore the clean evaluation. A four-task rel-salt case study further shows the same evaluation concern with native-schema leakage candidates from the original relational schema. These results identify the support/query information boundary as an important component of reliable relational ICL evaluation.

---


### 123. [The Safety Operator: Modulating the Expression of Safety Instructions via Spectral Optimization](https://arxiv.org/abs/2609.36434)

**<font color=#1a73e8>作者：</font>** Benoit Dherin, Michael Munn, Xavier Gonzalvo 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Context tokens in a transformer-based language model can be absorbed into the model's weights as a multiplicative operator. We study this operator in the setting of safety instructions and show that influencing its dominant eigenvalue modulates how strongly the instruction shapes generation. We derive a Contrastive Safety Loss with a suppression weight that controls the tradeoff between emphasizing the safety instruction on harmful queries while suppressing it on harmless queries. Varying the suppression weight maps a relationship between the attack success and the over-refusal rates, supporting the hypothesis that the operator's eigenvalue acts as a continuous dial for the instruction's influence. Moreover, this relationship holds relatively independently of how the Safety Loss is parameterized, yielding Pareto-improved safety instructions for appropriate values of suppression weight.

---


### 124. [MemFold: Learning Compact Soft Memory for Long-Context Personalization via On-Policy Optimization](https://arxiv.org/abs/2609.36435)

**<font color=#1a73e8>作者：</font>** Jingxuan Wu, Yuzhe Yang, Yiqiao Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An assistant that serves the same user over a long horizon has to answer from what that user has revealed: which preferences still hold, which were revised, and which constraints apply now. Retaining that information is not the same as acting on it, and the two are usually optimized as if they were. Keeping the information as text makes the reader's input grow with the retained history, while compressing it into a fixed number of latent vectors bounds the interface but is typically trained to reconstruct text or imitate reference answers, both of which are scored on sequences the reader never produced. We present MemFold, which optimizes a fixed-budget soft memory by the behavior it supports. A query-conditioned textual memory is compressed into K continuous vectors that form the reader's memory interface, and the reader is then trained on its own rollouts under two complementary signals: group-relative rewards for task outcomes, and confidence-gated on-policy distillation in which a frozen textual-memory teacher re-scores the student's sampled tokens under the textual memory. The teacher is never sampled from, so supervision stays on the student's current distribution and adds no autoregressive decoding; at inference it is removed entirely. Across three Qwen backbones, MemFold attains the highest accuracy we measure on PersonaMem-32K and PersonaMem-128K, with margins that widen at the longer history length, and transfers to PrefEval and LongMemEval without target-domain training. Ablations attribute most of the task gain to the reward term and a smaller additional gain to the teacher signal, and memory interventions show that the reader depends on the instance-specific content of its soft memory.

---


### 125. [Bits Under ZK-LLM: Evaluating Zero-Knowledge-Friendly Quantization for Verifiable Private LLM Inference](https://arxiv.org/abs/2609.36437)

**<font color=#1a73e8>作者：</font>** Taeung Yoon, Yupeng Zhang, Xiaojing Liao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Zero-knowledge proofs are emerging as a promising approach for enabling private, verifiable LLM governance and auditing, where regulators, users, and auditors need to verify claims about training-data usage or LLM inference-time behavior, while model providers must protect proprietary model parameters. However, despite the growing interest in ZK-LLMs, the understanding of ZK-friendly quantization remains limited. This gap matters because in the ZK setting, quantization directly shapes the arithmetic structure, constraint complexity, and proving cost of ZK inference. ZK protocols operate over finite fields and incur costs that depend heavily on the number and type of arithmetic operations, nonlinearities, and lookup constraints. Understanding ZK-friendly quantization is therefore essential for making ZK-LLMs practical. In this work, we present the first systematic study of ZK-friendly quantization for LLMs. We first formalize the definition of ZK-friendly quantization, capturing the properties required for ZK proof generation. We then evaluate nine language models, including Qwen2.5-14B and the mixture-of-experts model Qwen3-30B-A3B, across a broad design space of weight, activation, and nonlinear lookup table precision. Our results show that activation precision is substantially more sensitive than weight precision, while nonlinear lookup approximations can become the dominant source of utility degradation. Also, we identify RMSNorm inverse-square-root lookups as a recurring bottleneck in several large models and recover near-baseline utility by selectively increasing precision only at the bottleneck. Finally, we show that reducing bit-width or lookup-table size does not necessarily yield proportional end-to-end proving savings, showing that conventional low-bit quantization heuristics do not directly translate to ZK proving efficiency and motivating operator-aware precision selection.

---


### 126. [DARE to Mitigate Hallucination: Dual-path Auto-Regressive-aware Editing](https://arxiv.org/abs/2609.36440)

**<font color=#1a73e8>作者：</font>** Jae-Ho Lee, Jeong-Eun Lee, Gyeong-Moon Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) have recently achieved remarkable progress across multimodal tasks, yet object hallucination remains a persistent challenge where models generate descriptions inconsistent with the visual input. Recent work mitigates hallucinations through training-free representation editing, typically by constructing hallucination-related directions from teacher-forcing (TF) contrasts between hallucinated and truthful responses. However, LVLMs operate through autoregressive (AR) decoding during generation, raising the question of whether TF-based analysis fully reflects the generation dynamics that lead to hallucinated outputs. In this paper, we analyze the relationship between TF-based editing and AR generation behavior and find that TF-based editing alone may be insufficient to capture both decoding dynamics and multimodal interactions associated with hallucinations. To address this limitation, we propose DARE (Dual-path Auto-Regressive-aware Editing), a hybrid hallucination editing framework that integrates two complementary contrast pathways: textual contrasts and image contrasts, together with autoregressive-aware representation signals. Specifically, DARE constructs hallucination editing directions from (1) TF-based textual contrasts, (2) AR-aware representation transitions during decoding, and (3) controlled visual differences between paired images. Extensive experiments on multiple LVLM hallucination benchmarks demonstrate that DARE consistently reduces object hallucinations while preserving multimodal perception capability and inference efficiency. Our implementation code is available at this https URL.

---


### 127. [Theory on Attention Dynamics for Out-of-Distribution In-Context Learning](https://arxiv.org/abs/2609.36448)

**<font color=#1a73e8>作者：</font>** Junze Deng, Daouda Sow, Sen Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers have demonstrated remarkable in-context learning (ICL) capabilities, enabling them to perform new tasks without additional fine-tuning. However, their performance often deteriorates when encountering out-of-distribution (OOD) inputs that deviate from the training distribution, and the underlying theory remains poorly understood. To fill this gap, we characterize the OOD error under the input distribution shift through the interplay between the dynamics of the so-called $\alpha$-type and $\beta$-type attention weights, which represent the transformer's confidence in identifying the correct and incorrect features, respectively. Our results indicate that the OOD error for each feature depends on all pairwise interactions between the training features and OOD features, and under certain cases the transformer performs no better than random guessing. To improve the OOD generalization performance, we next investigate the impact of model finetuning with the OOD data, and particularly, characterize the model forgetting performance on the source domain. Interestingly, the performance on the source domain may not always degrade after finetuning, which highly depends on the nature of the feature shift: finetuning on OOD domain keeps enhancing the confidence of identifying correct features from the original distribution, while the interference from other incorrect features may either increase or decrease. Extensive experiments on both synthetic and real data are conducted to corroborate the theoretical insights.

---


### 128. [Invariant Atoms: Sparse Coordinates of Local Semantic Geometry in Language Model Representations](https://arxiv.org/abs/2609.36451)

**<font color=#1a73e8>作者：</font>** Muhammad Ahtesham, Xin Zhong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models often preserve meaning despite substantial changes in wording, style, and syntax, while small semantic edits can systematically alter their hidden representations. This suggests that semantic variation may be organized along recurring local directions. We propose the Invariant Atom Hypothesis: local semantic motion admits preferred sparse coordinates along directions that remain stable under meaning-preserving transformations. We learn a shared semantic frame and sparse coordinates that reconstruct semantic displacements while suppressing nuisance variation, with anchor-dependent diagonal modulation adjusting atom strengths without sample-specific rotations. Empirically, the atoms exhibit strong semantic--nuisance separation, sparse reconstruction, reproducible directions, and causal effects on model predictions. The learned geometry generalizes to unseen semantic neighborhoods and nuisance families, while local reweighting improves semantic selectivity and preserves a consistent global-to-local structure. Atom signatures also remain stable under model modification. These findings support reusable invariant directions as a sparse coordinate system for local semantic geometry in language models.

---


### 129. [Reliable Parallel Decoding in Masked Diffusion Language Models](https://arxiv.org/abs/2609.36452)

**<font color=#1a73e8>作者：</font>** Zhenghao He, Bohan Liu, Guangzhi Xiong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models (MDLMs) can generate text efficiently by predicting multiple masked tokens in parallel, but predictions from the same forward pass are not necessarily reliable when committed together. We study when parallel commitment is reliable. Our diagnostics show that confidence alone does not determine a reliable commitment order: confident predictions near the end of the sequence can fix an answer before its supporting computations are established, and downstream predictions become less reliable as the uncertainty of their upstream context grows. At the same time, a single forward pass can already resolve several masked tokens, and predictions that remain stable across the final layers are more likely to be correct. Based on these findings, we propose Reliable Parallel Decoding (RPD), a training-free method that selects candidates by layerwise prediction stability and final confidence, and commits them under a cumulative entropy budget over their preceding masked positions. RPD defers predictions with uncertain upstream context while committing the remaining candidates in parallel, without relying on a fixed block schedule. Across mathematical reasoning and code generation benchmarks on LLaDA and Dream, RPD achieves the highest decoding throughput among the evaluated methods while maintaining or improving accuracy.

---


### 130. [Emergent phases of superposition: from partial to full representation](https://arxiv.org/abs/2609.36455)

**<font color=#1a73e8>作者：</font>** Lihao Guo, Yizhou Liu, Jeff Gore  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models are thought to represent features by vectors in a hidden space of dimension given by the model's width. Superposition, in which more features are represented than the width by letting representation vectors overlap, is a leading account of how representation vectors are organized. However, how model width and data statistics determine the configuration of representation vectors and the resulting loss when the number of features and the width are large remains less understood. Here we show, in Anthropic's toy model of superposition, that increasing the width drives a continuous phase transition from a partial-representation phase, where only a subset of features receives appreciable representation vectors while the rest vanish, to a full-representation phase, where every feature is represented. Our theory via a partial random projection approximation predicts, and experiments confirm, that the critical width grows linearly with the number of active features up to a logarithmic factor. The loss scaling changes across the transition: below the critical width, the loss grows linearly with the number of active features and depends weakly on the width in a form set by data statistics; above it, the loss grows approximately quadratically with the number of active features and decays inversely with the width. Non-uniform firing probabilities delay the transition and lower the loss, as more frequent features occupy more space. Our results provide an account of how model width and data statistics jointly shape representations and loss, a step toward understanding representation scaling in large models.

---


### 131. [Rethinking Reasoning Paths as Phase-Structured Trajectories](https://arxiv.org/abs/2609.36461)

**<font color=#1a73e8>作者：</font>** Zhenghao He, Guangzhi Xiong, Sanchit Sinha 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models often improve problem-solving performance by generating multi-step reasoning paths, yet how to analyze the hidden states along these paths remains unclear. Existing approaches typically assign each intermediate state the final-answer correctness label and train probes across heterogeneous questions. We argue that this protocol obscures reasoning dynamics in two ways: (1) correctness prediction can exploit question-level variation rather than path quality, and (2) states aligned by absolute step indices may correspond to different functional phases of reasoning. In this work, we propose to view reasoning paths as phase-structured trajectories within fixed questions. We instantiate this view as PAIR, short for Phase-Aligned Intra-question Reasoning. PAIR samples multiple trajectories for each question, maps variable-length paths into shared relative phases based on normalized trajectory progress, and compares successful and unsuccessful trajectories only within the same question and phase. This yields phase-specific path-quality directions that better isolate path-quality signals from question-level variation. Empirically, we find that standard across-question correctness probes lose much of their predictive power under within-question evaluation, suggesting that these probes partly rely on question-level information. PAIR improves within-question trajectory ranking and Best-of-N trajectory selection across models and benchmarks. Phase-wise steering further shows that the learned directions can change generation outcomes, providing causal evidence that they capture trajectory-relevant information.

---


### 132. [Similar Choices, Different Attention: Cross-Modal Associations in Humans and Vision-Language Models](https://arxiv.org/abs/2609.36475)

**<font color=#1a73e8>作者：</font>** Sumin Hong, Katsumi Ibaraki, Renee Shi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-modal associations are systematic pairings of features across modalities, such as the association of 'bouba' with round shapes and 'kiki' with sharp shapes. Prior work has compared humans and vision-language models (VLMs) on such associations, but often using different stimuli or tasks between humans and models. Here, we ask whether VLMs align with humans not only in choices, but also in where they look when making those choices. We study both VLMs and humans (N = 53), presenting them with the same stimuli, a pseudo-word and two images, and record participants' choices and eye movements, which we release. We find choice alignment in a few larger VLMs, but their saliency matches human gaze less closely than a center-bias baseline, a fixed Gaussian at the center of each image. Fine-tuning small VLMs on human choices brings their choice alignment to the level of a human majority-vote reference on unseen words and images, yet their attention still matches human gaze less closely than this baseline. Training model attention on human gaze raises attention-gaze correlation without improving choice alignment, and a single average gaze map per image position raises it by a similar amount. Matching human choices, or even human gaze patterns, is therefore not sufficient evidence of human-aligned cross-modal processing.

---


### 133. [The Teacher Is a Direction, Not a Destination: Extrapolating RL-Induced Representation Residuals in On-Policy Distillation](https://arxiv.org/abs/2609.36484)

**<font color=#1a73e8>作者：</font>** Hao Li, MeiJia Chen, Weijie Ren 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student to match the teacher's next-token distributions on the student's own trajectories and has yielded substantial empirical gains. Generalized variants allow the student to surpass the teacher by extrapolating an implicit reward in output space. The language-model head, however, attenuates this change anisotropically: much of the change encoded in the teacher's hidden states reaches the logits at a small fraction of its weight, and the sampled-token log-probability ratios on which output-space extrapolation relies inject noise that the extrapolation amplifies, making training unstable. We observe that reinforcement learning (RL) shifts a model's internal representations relative to its base checkpoint, and that the direction of this shift can be measured at every layer. Motivated by this observation, we propose RIDE (RL-Induced Direction Extrapolation), which extrapolates the RL-induced change directly in representation space: at every layer and token position, RIDE computes the residual between the teacher and its pre-RL checkpoint and regresses the student's hidden states toward targets displaced beyond the teacher along this residual. Conditioned on a sampled trajectory, this regression is equivalent to maximizing a linear directional reward defined by the residual under a quadratic penalty centered at the teacher, which makes explicit how the objective moves the student along the RL-induced direction while limiting its deviation from the teacher. Across four base/RL-teacher pairs spanning different scales, architectures, and pre-training lineages, RIDE approaches or exceeds the RL-trained teacher on every pair and is the only method whose mean does so, and it consistently outperforms output-space extrapolation, which degrades the student whenever the teacher is close to its base. Project page: this https URL.

---


### 134. [AdaptArena: Evaluating Test-Time Personalization of Web Agents](https://arxiv.org/abs/2609.36488)

**<font color=#1a73e8>作者：</font>** Dongchan Shin, Xing Han Lù, Jiaqi Deng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents have demonstrated strong performance on complex web navigation tasks, yet they remain brittle in real-world settings where user intentions are underspecified and preferences are heterogeneous. In practice, users rarely provide explicit profiles, requiring agents to infer latent preferences from implicit signals. Despite its importance for deployment, this problem setting is largely underexplored in existing benchmarks. To address this gap, we introduce AdaptArena, a benchmark for evaluating test-time personalization of web agents via implicit preference inference. AdaptArena consists of 480 tasks, featuring both single-preference and double-preference scenarios. Each evaluation task must be solved by retrieving and leveraging the most relevant historical user trajectory that implicitly encodes the target preference. In addition, we introduce AdaptiveAgent, a retrieval-based framework for standardized evaluation of implicit preference inference. Experiments reveal a substantial performance gap: while oracle agents with access to ground-truth preferences achieve an 82.92% success rate, the evaluated LLM agents using our framework reach at most 15.62%. Furthermore, we find that correctly inferring user preferences is necessary but not sufficient for task success, as execution failures in downstream web interactions remain a significant bottleneck even when agents align with the target preference. These findings highlight implicit preference inference and robust action grounding as key challenges for deploying reliable, user-facing web agents. We release our code: this https URL

---


### 135. [LLMs Learn to Evade Latent Monitors from Prior Feedback Alone](https://arxiv.org/abs/2609.36490)

**<font color=#1a73e8>作者：</font>** Hugo Lyons Keenan, Christopher Leckie, Sarah Erfani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent space monitors aim to detect undesired behaviors in LLM agents by inspecting an agent's internal activations rather than its outputs. However, interactive monitoring creates a feedback channel where each verdict the monitor delivers leaks information to the model about how its internal states are being evaluated. We ask whether an agent can infer the monitor's decision rule from this feedback and then selectively edit its activations to evade detection. Unlike prior evasion attacks, the model is never explicitly told what the monitor detects. Surprisingly, off-the-shelf models already produce activation edits aligned with the monitored direction, but at insufficient magnitude for evasion. Simply scaling up these edits by a factor of 8 reduces the monitor's TPR from 100% to 27%. A rank-1 LoRA amplifies this behavior into effective evasion within the forward pass, reducing TPR further to 4% on held-out concept monitors while leaving other concepts at their normal detection rates. Capabilities on standard benchmarks are retained under this finetuning, and the evasion skill survives retraining the monitors on the new activations. Mechanistically, we find evidence that the model computes its activation edit from the prior in-context turns, and show that the edit becomes more aligned with the monitored direction as more examples are provided. These results demonstrate feedback-conditioned control over activations and suggest that latent monitoring should be treated as an interactive process in which agents can observe and respond to oversight measures.

---


### 136. [Benchmarking Vision-Language Models on Synapse Detection and Proofreading in Connectomics](https://arxiv.org/abs/2609.36492)

**<font color=#1a73e8>作者：</font>** Yicong Li, Junjie Wang, Leander Lauenburg 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We benchmarked vision-language models (VLMs) on the decisions annotators take when inspecting electron microscopy images in connectomics: synapse detection (presence and polarity) and proofreading (split errors and merge errors). For synapse detection, we evaluated 19 open and 2 closed models across various architectures and sizes under zero-shot, four-shot in-context learning and LoRA settings, against specialist models, on datasets constructed by us using public resources. For proofreading, we evaluated 3 open and 2 closed models on the ConnectomeBench2 dataset, with cross-species transfer from fly and mouse to human and zebrafish. Most models were at chance zero-shot; a few examples helped mainly the closed and largest open ones. LoRA on a few thousand labels brought open models level with specialist models. When evaluated on unseen species, the best adapted VLMs outperformed specialist models trained on the same data in identifying merge errors. The project will be publicly available upon acceptance.

---


### 137. [Know the Normal, Track the Attack: Context-Grounded and Stateful LLM Investigation over System Provenance](https://arxiv.org/abs/2609.36494)

**<font color=#1a73e8>作者：</font>** Lijie Zheng, Ji He, Ying Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Provenance-based intrusion detection systems (PIDSs) identify suspicious activity in audit streams, but their outputs remain difficult to turn into coherent attack narratives. Direct LLM analyses of local anomalous subgraphs lack deployment-specific normal-behavior knowledge and validated attack state across evidence fragments. This can cause unsupported attack interpretations of routine activities and incorrect attribution of temporally dispersed evidence to attack stages. We present ANCHOR, an investigation-oriented provenance system that combines evidence curation with context-grounded LLM reasoning. It calibrates anomaly judgments by relation type and links anomalous windows through rare relation-role patterns. The resulting evidence queues preserve causal structure, temporal boundaries, and cross-window continuity. The investigator interprets process-centered evidence using two complementary forms of context. Deployment Context combines environment-specific interaction and object baselines with high-risk security knowledge. Case Context uses a confidence-gated Attack-Tracking Cache to maintain investigation state across windows. Correlating current evidence with high-confidence prior findings, ANCHOR incrementally reconstructs attack narratives organized by kill-chain stages. We evaluate ANCHOR on six DARPA Transparent Computing E3/E5 datasets across three operating systems. Controlled evidence-level and end-to-end comparisons show improved overall IoC recovery and attack-stage attribution over state-of-the-art provenance-based baselines. These gains persist under a fixed LLM backbone in our evaluation. ANCHOR processes a full audit day at dollar-level API cost, supporting practical, context-grounded investigation across windows.

---


### 138. [BRIDGE: Bilevel Retrieval-Credit-Aware Agentic Reinforcement Learning](https://arxiv.org/abs/2609.36505)

**<font color=#1a73e8>作者：</font>** Quan Xiao, Mingda Liu, Gaowen Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic reinforcement learning (ARL) with verifiable rewards improves the ability of large language models (LLMs) to tackle knowledge-intensive tasks by learning to interleave search and reasoning. However, most existing ARL methods optimize only LLM-generated tokens and treat retrieved evidence as environment observations. This creates an information-credit gap: failures caused by missing or misleading evidence are attributed to the LLM policy rather than to the retriever, which motivates training the LLM and the retriever jointly. In this paper, we show that retrieval and LLM policy learning are order-sensitive: adapting the retriever before optimizing the policy yields a larger reward gain than the reverse order. To preserve this hierarchy while allowing both components to co-adapt, we formulate retrieval-augmented agentic RL as a bilevel optimization problem. To solve it efficiently, we introduce BRIDGE, a memory-efficient first-order bilevel method motivated by a loss-landscape analysis of the RL and retrieval objectives. Across seven open-domain QA benchmarks, BRIDGE achieves the highest average accuracy with both 3B and 7B backbones, improving the multi-hop average over the strongest baseline by 9.6 and 3.4 EM points, respectively. It also achieves the best averaged answer accuracy and reasoning quality across medical QA benchmarks.

---


### 139. [Large-scale factor analysis shows machine intelligence is only partially interpretable](https://arxiv.org/abs/2609.36515)

**<font color=#1a73e8>作者：</font>** Faiz Ghifari Haznitrama, Afrizal Hasbi Azizy, Faeyza Rishad Ardi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A common assumption in language model development is that cognitive abilities are organized around a general, domain-free intelligence factor, like fluid intelligence in humans. This assumption is rarely tested directly, and prior attempts have done so only at a much smaller scale. We take a latent variable approach to intelligence in language models, similar to how psychometricians study psychological constructs. Performance in every specific problem set is influenced by a domain-specific and a domain-agnostic latent factor. Using factor analysis as a dimension-reduction technique, we analyzed 13,251 published evaluation scores covering 1,618 language models across 456 different text-only benchmarks. Due to the super-sparse nature of the dataset, we triangulate our analysis across different data densifiers and imputation methods. A robust pattern across different modes of bias is that 1. A general intelligence factor accounts for 70.8% of variance in model performance at our most generous estimate, and far less than that in most of our solutions, 2. Content-similar benchmarks do not necessarily cluster together, and 3. The $g$ factor is not dominated by any common theme, and there is a lack of evidence that it is well-proxied by standard "intelligence" benchmarks. Our findings go against current endeavors of defining, identifying, and targeting general intelligence as a tangible construct in language model development. This leaves the strategy of targeting a single conceptual ability without support, since the first-order abilities it would have to reach are often partially idiosyncratic and not identifiable in practice.

---


### 140. [Adapting Context Compression for Long-Horizon Agents with Counterfactual Continuations](https://arxiv.org/abs/2609.36526)

**<font color=#1a73e8>作者：</font>** Guanghui Min, Liang Wu, Mingjia Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents require context compression to manage growing interaction histories. Compression quality, however, is ultimately determined by downstream execution. Existing prompt-adaptation methods infer compression errors by comparing full-context and compressed trajectories. Such comparisons cannot isolate individual compressions and are confounded by agent stochasticity. We first find that compression degrades reliability before solvability. Using matched counterfactual continuations that compare execution from the same agent state with versus without compression, we further show that severe degradation concentrates at isolated compression events. Motivated by this finding, we propose PAIR (Prompt Adaptation using Interventional Rollouts) for adapting structured compression prompts. PAIR identifies individual compressions that degrade subsequent execution, diagnoses their effects, and revises the relevant sections of a fixed compression template. PAIR achieves the strongest cross-run reliability among compressed methods in every main benchmark-scope combination, consistently exceeding the competing prompt-adaptation baseline. Without modifying the downstream agent, PAIR brings compressed execution close to the no-compression baseline and sometimes numerically exceeds it.

---


### 141. [Triadic Linear Attention: Three-Dimensional Recurrent States for Long-Context Sequence Modeling](https://arxiv.org/abs/2609.36529)

**<font color=#1a73e8>作者：</font>** Oliver Sieberling, Bharat Runwal, David Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recurrent neural networks (RNNs) compress the historical context into a memory state of fixed size, thus allowing for constant-time inference. The memory state size is a crucial factor in their performance, as exemplified by the strong performance and resurgence of linear attention, which extends the vector-valued hidden states of ordinary RNNs to matrix-valued hidden states. Crucially, linear attention does so in a parameter-efficient way, in particular by using an outer product of the key and value vectors to write to the matrix-valued hidden state. We generalize this construction and propose triadic linear attention, which writes the triadic outer product of a key, a second key, and a value, into a third-order (i.e., 3D) tensor state, and reads from it by contracting both key axes with two queries. An $E$-dimensional second key thus yields an $E$-fold increase in state size while adding only two projections. Triadic linear attention is compatible with data-dependent forgetting, the delta rule, and chunkwise-parallel training. Applied to Gated DeltaNet and scalar-gated linear attention, triadic linear attention substantially improves long-context language modeling and recall, outperforming alternatives that enlarge the state.

---


### 142. [Retrieval Sensitivity to Identity Signals in Queries](https://arxiv.org/abs/2609.36534)

**<font color=#1a73e8>作者：</font>** Andrew Tang, Nicholas Deas, Kathleen McKeown 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dense retrievers decide which documents reach users and the language models that use them, yet they are typically evaluated with neutral queries. We ask whether the identity signals that real users express in their queries---political ideology and dialect---bias what a retriever returns. We design evaluations in two domains, political news and consumer-health questions, each pairing a controlled synthetic set that varies only the identity signal with naturalistic queries. Across five dense retrievers and a sparse baseline, every retriever (i) retrieves articles that align with the query's own political lean and (ii) performs worse for questions written in African American Language (AAL) than in White Mainstream English (WME). Two analyses tie these gaps to queries' identity signals beyond surface vocabulary: partialling out an aggregate lexical-asymmetry score leaves the synthetic gaps largely intact, and linear probes recover lean and dialect from the retrievers' query embeddings beyond token-level features. Left unaddressed, such retrieval biases risk contributing to polarization and reinforcing the health disparities already faced by AAL speakers. Code is available at this https URL.

---


### 143. [When Updating Stops Being Learning: Rethinking LLM Self-Evolution via learnable information gain](https://arxiv.org/abs/2609.36535)

**<font color=#1a73e8>作者：</font>** Chenxu Wang, Chaozhuo Li, Xinze Shi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-evolution lets large language models (LLMs) improve iteratively using their own generated data, but often suffers from self-evolution degeneration: performance improves, plateaus, then declines. Existing methods address this issue at the component level, targeting either the Questioner or the Solver, and overlook that self-evolution is a tightly coupled system. We propose a holistic framework based on learnable information gain, which measures how much novel, parameterizable information a round provides relative to the previous round. Theoretically, this gain equals the Kullback-Leibler divergence between the two rounds' data distributions plus their entropy change. Practically, it is estimated by fitting a small language model to the previous round and scoring new data via negative log-likelihood. Based on this diagnostic, we propose ATRI (Adaptive Training Regulation via Information-gain), which reweights samples within a round and halts training across rounds when information gain remains low. Experiments on popular datasets demonstrate the superiority of our proposal.

---


### 144. [DraftTrace: A Multi-View Analytics Environment for AI-Integrated Writing](https://arxiv.org/abs/2609.36544)

**<font color=#1a73e8>作者：</font>** Divyansh Chandarana, Sandipan De, Vivek Gupta  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generative AI has changed how students produce writing assignments. The final artifact is no longer sufficient to understand the process through which it was produced. We introduce DraftTrace, a writing environment that jointly captures three complementary views of writing: the final product, the writing process and interactions with an integrated AI-assistant. DraftTrace reconstructs how a document develops over time and organizes these signals into submission, longitudinal, and class-level analytics for instructors. We deployed DraftTrace in a graduate NLP course with 81 students and compared their sessions with LLM-generated responses entered by automated tools and with copy-typed responses. While product measures distinguish differences in text formulation, process measures distinguish differences in how text is entered. Considering both views together helps characterize cases such as copy-typing. Interaction traces show that students use the assistant differently across stages of writing: to clarify the question at an early stage and to verify answers at a later stage. A preliminary instructor survey highlights the importance of multi-view writing analytics and their interpretability.

---


### 145. [Interactive-Policy Distillation with Bidirectional Propose-and-Verify](https://arxiv.org/abs/2609.36546)

**<font color=#1a73e8>作者：</font>** Shutong Wu, Xiwen Chen, Brendan Rappazzo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student model on its self-generated trajectories with dense token-level teacher feedback. However, naive OPD may suffer from teacher unanchoring, where the student's reasoning trajectory drifts far from the teacher, causing the teacher to be queried on states it would hardly visit and thus provide unreliable supervision. We propose Interactive-Policy Distillation (IPD), which applies adaptive teacher intervention to the student rollout. Under a bidirectional propose-and-verify state machine, the student and teacher alternately exchange their roles as proposer and verifier, and collaboratively generate mixed-source trajectories. Then different supervisions are applied according to the source of each token. This bidirectional propose-and-verify mechanism and the source-split loss make IPD not only a more performant distillation method, but also a unified bridge between on-policy and off-policy paradigms. To make the interleaved dual-model rollouts more efficient, we also design a dedicated fused inference engine that co-hosts both models in one serving instance with separate KV caches and instantiates the state machine model to distribute, collect, and process requests. On math reasoning tasks and across multiple teacher-student model pairs, student models trained with IPD not only outperform those trained with OPD, but also demonstrate higher data efficiency. Specifically, when distilling Qwen3-30B-A3B into Qwen3-1.7B-Base, IPD brings a +3.28 mean@8 and a +3.28 best@8 benchmark-averaged accuracy improvement compared with OPD. Besides, IPD only consumes about 1/4 of the training examples and steps to outperform OPD trained on the whole training dataset for one epoch. We also investigate the impact of different loss variants and takeover / handback configurations, and demonstrate the robustness of IPD on different training data.

---


### 146. [Grounded Revision vs. Prior Injection: Probing Retrieval-Augmented Patent Claim Amendment](https://arxiv.org/abs/2609.36550)

**<font color=#1a73e8>作者：</font>** Josepha Michiko Leo, Hyun-seok Min, Yehoon Jang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation is widely used in professional writing, yet whether retrieval grounds revision or merely injects templates is rarely tested where "correct" has a definable meaning. Patent claim amendment supplies that signal: the examiner names the attacked limitation and cites prior art, providing per-case ground truth. We release three artifacts: (i) a corpus of 7,385 USPTO prosecution cases with XML-aligned pre/post claims, rejection, and cited prior art; (ii) a seven-probe battery comparing random and structural-match retrieval as two policies under a fixed prompt scaffold; (iii) a deterministic five-channel metric (C1-C3 and C5 in main, C4 supplementary) requiring no LLM evaluation. Across 9,600 pre-registered calls on four frontier LLMs (Claude Sonnet 4, Claude Haiku 4.5, GPT-5.4, GPT-4o-mini), no tested model exhibits detectable classical prior-injection behavior; retrieval effects are small and direction-inconsistent between random and structural retrieval, and the null is unchanged under a dense (semantic) retriever, across retrieval depths k in {1,3,5,10}, and under a paraphrase-sensitive grounding metric. Revision locality reveals a model-specific difference that the template channel misses. The four-cell taxonomy, which we treat as exploratory, leaves the prior-injector cell unoccupied.

---


### 147. [MAADBench: The Refreshable Paradigm for Anomaly Detection in Multi-Agent Systems](https://arxiv.org/abs/2609.36556)

**<font color=#1a73e8>作者：</font>** Lei Ma, Dennis Hofmann, Haowen Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent studies report that LLM-based multi-agent systems (MAS) fail at rates of 41%-87%, yet to our knowledge, no benchmark to date supports systematic anomaly detection (AD) for them. Building MAS AD benchmarks is hard because they must remain fresh as LLM systems evolve: tasks may leak into training data and thus be memorized by LLMs, traces and anomaly patterns expire as backbones evolve, and labels must be provided reliably for each refresh. To address these challenges, we present MAADBench (MA: multi-agent; AD: anomaly detection), the first refreshable MAS AD benchmark designed for diverse, evolving LLM backbones underlying the agents. MAADBench combines (1) sampled-and-coupled generative tasks over an approximately 10^37-task space to mitigate task leakage, (2) refreshable trace generation under configurable LLM backbones, and (3) automated provision of cost-free, deterministic step-level labels for fine-grained AD evaluation. Beyond offering the paradigm itself, we run MAADBench with five state-of-the-art LLM backbones and release the MAADBench-Full dataset with 5,200 step-labeled traces. Benchmarking 25 AD methods on the MAADBench dataset reveals substantial limitations in current approaches: they rely heavily on supervision, struggle with subtle MAS-specific anomalies, and lack robustness across LLM backbones. These gaps point to a rich research agenda for MAS-specific anomaly detection, with MAADBench providing a systematic and refreshable testbed for method development and evaluation. We open-source MAADBench-Full at this https URL.

---


### 148. [How Medical VLMs Underutilize Their Vision Encoders: A Dermatology Perspective](https://arxiv.org/abs/2609.36557)

**<font color=#1a73e8>作者：</font>** Janet Wang, Yunbei Zhang, Xiao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical Vision-Language Models (VLMs) show significant promise for clinical image understanding, offering accurate diagnosis with interpretable reasoning. However, a critical performance gap exists between their strong vision encoders and the full multimodal model: in dermatology, the MedSigLIP encoder outperforms MedGemma by an average of 10.26 percentage points even when both use zero target-task labels; few-shot linear probing provides further evidence of strong visual representations. This gap motivates an investigation of how visual information is used in end-to-end diagnosis and why plausible-sounding predictions can lack grounding in image evidence. Using dermatology as our primary testbed, we systematically investigate three hypotheses for this phenomenon. We further provide a mechanistic analysis of the model's internal attention patterns, showing that a simple describe-then-decide prompting strategy increases vision attention by 30-40% during generation. Task-specific fine-tuning improves dermatology classification but reduces cross-domain medical question-answering performance in our evaluation. To address these challenges, we combine label-free prompting with low-label encoder-assisted reranking while keeping the VLM frozen. We validate the interventions across five VLM backbones in dermatology and provide supporting representation and attention analyses across additional medical modalities.

---


### 149. [ThinkingGuard: Decoding Implicit Hazards via Step-by-Step Risk Attribution in Multimodal Large Language Models](https://arxiv.org/abs/2609.36562)

**<font color=#1a73e8>作者：</font>** Ruochen Zhang, Yao Huang, Yitong Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Multimodal Large Language Models (MLLMs) are increasingly deployed in safety-critical domains, their reliability is threatened by multimodal implicit risks. Unlike explicit threats, these hazards emerge when individually benign text and neutral visual entities logically converge to induce unsafe outputs. Current detection methods fail to address this because they overlook the underlying risk activation mechanisms that govern cross-modal risk activation, leading to single-modality shortcut learning and hallucinated rationalizations. To bridge this gap, we first construct TriggerBench, the first dataset explicitly modeling risk compositionality (5,600 instances). By formally isolating Key Elements and Trigger Elements to build counterfactual contrastive pairs, TriggerBench eliminates risk residues and forces models to perform genuine logical deduction rather than superficial pattern matching, which provides a rigorous foundation for both large-scale training and fine-grained evaluation. Building on this, we propose a Step-Supervised Structured Reasoning training framework and employ it to train ThinkingGuard, a specialized guard model. Inspired by Situation Awareness theory, we decouple implicit risk identification into progressive cognitive stages, and utilize a step-reward Monte Carlo Tree Search algorithm to explore optimal reasoning trajectories, which are then distilled into the model through Dual-Constraint Preference Alignment. Extensive experiments across both standard and implicit safety benchmarks demonstrate that ThinkingGuard achieves strong performance. Project resources are available at this https URL.

---


### 150. [Visual sensitivity is not claim retractability: persistence-aware credit assignment for multimodal reinforcement learning](https://arxiv.org/abs/2609.36572)

**<font color=#1a73e8>作者：</font>** Zhongan Bi, Kepeng Lin, Xuanang Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) has been extended to Large Vision-Language Models (LVLMs), and perception-aware methods further encourage policies to rely on visual evidence. Yet relying on the image does not guarantee that visual claims are supported by it. Before RL training, 27.81% of the correctly answered responses of Qwen2.5-VL-7B on four multimodal reasoning benchmarks contain at least one direct visual claim that the image does not support. Since outcome-level RL rewards each response as a whole, these claims inherit the positive credit of the correct answer. We introduce a fixed-rollout counterfactual diagnostic that re-scores the same response under an intervened image to separate Evidence-Function Sensitivity (EFS), how strongly the model's predictions change, from claim persistence, whether the model keeps supporting the same claim rather than retracting it. The diagnostic reveals Sensitivity-Persistence Decoupling (SPD): under DAPO and VPPO, EFS increases and claims become more retractable overall, yet unsupported claims become significantly more persistent, whereas GRPO raises EFS without this deterioration. We therefore propose Persistence-Aware Credit Gating (PACG), which attenuates positive credit for unusually persistent visual claims and leaves all other credit unchanged. It requires no supported/unsupported labels and adds no inference cost. On Qwen2.5-VL-7B, PACG raises the nine-benchmark average over three seeds from 58.1% to 59.9% with DAPO and from 59.8% to 60.9% with VPPO, while making unsupported claims more retractable. The gains extend to a larger model, a newer backbone, and the accuracy of HallusionBench also improves consistently. These results suggest that visual sensitivity and claim retractability are complementary dimensions of multimodal credit assignment.

---


> [!TIP]
> 当前位于：**101-150**（第 3/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
