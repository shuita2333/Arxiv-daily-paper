# 🧠 大模型相关研究 | 2026年09月11日

> 本类共 **148** 篇论文：已确认 **136** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-148**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-148**

---

### 101. [Active Adaptation, Not Static Defense: Temporal Dynamics of Preventative Steering in Adversarial Fine-Tuning](https://arxiv.org/abs/2609.10142)

**<font color=#1a73e8>作者：</font>** Jing Guan, Yachao Yang, Zhaoliang Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models remain fragile against malicious fine-tuning, motivating training-time defenses against harmful persona drift. Preventative Steering injects undesirable-trait persona vectors during fine-tuning and removes them at evaluation time, yet the mechanism behind its lasting protection remains unclear. Analyzing its temporal optimization dynamics, we find that the defense emerges from an early compensatory adaptation phase followed by a steady-state phase where the corrective signal decays; in parameter space, attention output projections emerge as the dominant residual-write route for defensive updates. Through Intervention Delta Preservation (IDP) and IDP Continuation experiments, we further show that preserving or reinjecting the weight offset fails to maintain protection, indicating that preventative steering relies on active adaptation rather than a static defense. Motivated by this finding, we propose Progressive Intensity Scheduling (PIS), which starts with a moderate injection strength and increases it after static-strength alignment begins to decay. Across the evaluated Qwen2.5 and Gemma-3 models, PIS improves safety robustness over static-strength steering while reducing harmful trait expression.

---


### 102. [Kernel-Managed Shared Memory for System-Wide Personalization](https://arxiv.org/abs/2609.10144)

**<font color=#1a73e8>作者：</font>** Ryan Lum, Yongfeng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI systems become more useful when they can adapt to the people using them, but in multi-agent systems, useful context learned by one agent often remains unavailable to others. We present kernel-managed shared memory, a system-level abstraction in which specialized agents write structured, tagged memories while the agent-system kernel, not individual agents, governs retrieval, privacy enforcement, and prompt injection. We implement and evaluate this design on AIOS and compare it against three alternatives across three assistant models (GPT-4o, Llama-3.1:8B, Qwen-2.5:7B) and 1,800 total trials. Against an unmanaged external memory backend (Mem0) using identical underlying storage, kernel-managed retrieval and injection improve personalization scores by 2.4-4.0 points on a 5-point scale (e.g., 1.05 to 4.69 profile usage on GPT-4o), with every comparison significant at p < 10^-18. Against standard retrieval-augmented injection, gains are similarly large and consistent across all three models. Against full, unfiltered context concatenation, a soft ceiling on available context rather than on response quality, kernel-managed injection statistically matches performance on two of three models and shows a small, model-specific deficit on the third, while using substantially shorter prompts: end-to-end latency is 15-61% lower across all three models, with corresponding reductions in per-call token usage and inference cost. These results indicate that centralizing memory management in the agent-system kernel, rather than leaving retrieval and privacy enforcement to individual agents, delivers most of the personalization benefit of unconstrained context at a fraction of its cost.

---


### 103. [YallaMorph: A Benchmark for Evaluating Arabic Morphological Generation in Large Language Models](https://arxiv.org/abs/2609.10153)

**<font color=#1a73e8>作者：</font>** Mahmoud Reda, Salam Khalifa, Reham Marzouk 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Arabic morphology remains challenging for large language models, since fluent generation does not guarantee accurate morphosyntactic control. Existing Arabic evaluations mainly target downstream tasks and do not directly test controlled morphological generation from explicit lexical and feature-based input. We introduce YallaMorph, a large-scale benchmark for Arabic morphological generation covering verbs, nouns, adjectives, their cliticized forms, and invalid configurations. We evaluate multilingual and Arabic-oriented LLMs under diacritized and undiacritized settings over 600K benchmark entries. Results show that Arabic morphological generation remains difficult, especially for cliticized, unseen, and morphologically rare forms.

---


### 104. [CompassOPD: Cross-Family On-Policy Distillation via Within-Family Likelihood Shifts](https://arxiv.org/abs/2609.10154)

**<font color=#1a73e8>作者：</font>** Naibin Gu, Qingyi Si, Chenxu Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) provides dense token-level supervision on student-generated trajectories. Although OPD performs strongly when teacher and student belong to the same model family, we find that its effectiveness degrades in cross-family settings even after tokenizer alignment, with substantially stronger external teachers offering little additional improvement. To understand this disconnect, we decompose the cross-family OPD signal into two components: an offset between a low-capability teacher-family reference and the student, and the within-family log-likelihood shift from that reference to the strong teacher. Standard OPD transfers both components together, allowing the offset to dominate the update direction and obscure the changes associated with teacher capability improvements. We propose CompassOPD, which removes this offset and transfers the within-family shift, while a frozen student reference anchors updates to the student's initial policy. Thus, both teacher-side and student-side changes are measured within their respective model families. Experiments across three student families and multiple teacher families show that CompassOPD consistently outperforms standard cross-family OPD, improving average reasoning accuracy by up to 5.50 points. For an MoE teacher, we further construct the reference directly from the teacher checkpoint by reducing expert activation, eliminating the need for a separate reference checkpoint while retaining a 3.43-point gain over OPD.

---


### 105. [From Retrieval to Weights: Parametric Individualization of Small Language Models with Individual Text Corpora](https://arxiv.org/abs/2609.10155)

**<font color=#1a73e8>作者：</font>** Christoph Wigbels, Ali Abusaleh, Markus T. Jansen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We approach a cognitive simulation perspective on episodic and semantic memory in multiple-choice question answering by incorporating text from individual text corpora (ITC) into retrieval-augmented generation and DoRA fine-tuning. We web-crawl the search histories of 515 participants who answered 36 multiple-choice knowledge items and analyze a stratified subsample of 150 participants. For each participant, one DoRA adapter consolidates their ITC into a small language model (SLM) whose baseline correctness falls below the participants' lowest quartile. The adapter measurably writes the ITC into the weights: it fits its own participant's held-out text better than other participants' texts (dz =1.27), an individuality effect that increases with ITC size in rank order. On the generalized knowledge test, however, the adapter adds knowledge rather than alignment with the individual: log-loss match improves, whereas match accuracy under a bias-corrected PMI readout does not, and retrieval adds nothing on top. Our results demonstrate that ITCs can be consolidated into the weights of SLMs, an encouraging basis for individualized tutoring agents, and we discuss how to move from there toward a realistic simulation of episodic and semantic memory at the individual level.

---


### 106. [Beyond Surface Imitation: Contrastive Modeling for Reasoning Path Alignment in Multimodal In-Context Learning](https://arxiv.org/abs/2609.10177)

**<font color=#1a73e8>作者：</font>** Mingbo Yang, Wenqiang Wang, Zhaolu Kang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) is widely used in multimodal large language models (MLLMs) and achieves strong performance across a wide range of multimodal tasks. However, existing multimodal ICL methods often rely on surface level imitation of in-context demonstrations, making it difficult for MLLMs to align their responses with the reasoning path required by the given multimodal input. This limitation becomes more pronounced in complex multimodal tasks, thereby restricting further improvements in MLLM performance. To address this issue, we propose a new multimodal ICL framework that combines contrastive demonstration modeling with the self-refinement capability of MLLMs. Specifically, our framework reformulates each demonstration by explicitly contrasting a suboptimal response with a better response under the same input, together with a reasoning path that reveals how the response should be refined. This contrastive formulation makes the reasoning path toward the desired response more explicit and guides the MLLM beyond superficial imitation. Furthermore, because effective refinement depends on the current response, we introduce a response-conditioned retrieval mechanism to select demonstrations whose reasoning paths are more relevant to the current response. In addition, we use a lightweight alignment controller to predict response quality and determine whether further refinement is needed. Experiments on three types of multimodal tasks show that the proposed framework consistently improves MLLM performance, with particularly notable gains on visual question answering (VQA).

---


### 107. [3rd Place Solution to Human Motion Challenges in Real-World and Clinical Settings (MoCha) @ECCV2026: Language-Aligned Motion Representations for Domain-Generalizable UPDRS-Gait Severity Estimation](https://arxiv.org/abs/2609.10187)

**<font color=#1a73e8>作者：</font>** Soojie Kim, Muhammad Munsif, Minkyung Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we introduce language-aligned motion representations for domain-generalizable UPDRS-Gait severity estimation, aiming to learn semantically structured motion features that generalize across heterogeneous clinical domains. We first learn motion representations using a Bi-GRU backbone that captures the temporal dynamics of SMPL sequences. Prior to model training, motion captions are generated offline using Qwen2.5-7B-Instruct. The backbone is then trained with both classification and text-alignment objectives to learn discriminative and semantically structured motion representations while accounting for the class imbalance present in the training data. We subsequently adapt the learned backbone independently to each source domain so that the model can capture domain-specific motion characteristics. The resulting source-specific models are then merged at the parameter level to consolidate complementary knowledge across source domains into a single domain-generalized model. To further mitigate class imbalance, we perform GPT-5.5-based pseudo labeling, and our final merged models for each site do not use any class-prior correction during inference. The resulting model is evaluated under the unseen-site setting of the MoCha Challenge, using Macro F1 as the primary evaluation metric. Our method achieves a macro-F1 of 0.57 on the hidden test set with only 637K active parameters at inference, ranking 3rd among 58 leaderboard entries in the MoCha 2026 Challenge. The challenge attracted 1,669 submissions from 112 participants and offered monetary prizes sponsored by Machine Medicine Technologies.

---


### 108. [Who Argues What? Joint Argument-Entity Detection and Classification in Political Debates](https://arxiv.org/abs/2609.10192)

**<font color=#1a73e8>作者：</font>** Lucio La Cava, Stefano Francesco Monea, Sergio Greco  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Political debates are often analyzed through Argument Mining (AM) to investigate the key arguments that drive them. However, political arguments are rarely interpretable from argumentative spans alone, as claims and premises generally depend on the entities (e.g., people, events, locations, parties) they mention. Existing AM resources and methods typically annotate argumentative spans and roles, but do not provide a paired debate-entity layer for asking which Debate Named Entities (DNE), e.g., actors and events, are invoked within debates. In this work, we address these data and methodological gaps by (i) introducing DNE-ElecDeb, an entity-enriched version of the USElecDeb dataset that adds DNEs in both argumentative and non-argumentative spans and defines Debate Named Entity Recognition (DNER) as the task of detecting DNEs, and (ii) proposing Joint Argument and Entity Tagging (JAET), a generative framework that fine-tunes decoder-only LLMs to insert inline argument and entity tags into debate turns while preserving the original transcript. Under BIO-tagging evaluation, JAET improves relative F1 on the joint AM+DNER task by +27.3%, resp. +41.9%, under the untyped, resp. typed setting over the strongest sequential AM-DNER pipelines, demonstrating that such gains cannot be recovered by composing two independent modules. Notably, similar margins replicate on Persuasive Essays (+26.6%, resp. +52.7%), showing effective generalization to domains orthogonal to political debates. By unifying argumentative and entity-level representations within a single view, our contributions pave the way for richer political debates understanding.

---


### 109. [UOT-Gap: A Variational Principle for the Modality Gap in Vision-Language Models via Unbalanced Optimal Transport](https://arxiv.org/abs/2609.10224)

**<font color=#1a73e8>作者：</font>** Zonglin Yang, Huilan Ma, Xudan Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models such as CLIP embed images and text in a shared space, where modality-specific distributions often remain separated. Existing accounts connect this modality gap to initialization, contrastive dynamics, and information imbalance, while its distributional and pairwise contributions to retrieval remain unresolved. We introduce UOT-Gap, a training-free variational diagnostic that models frozen image and text embeddings with unbalanced entropic optimal transport (UOT). The UOT optimum separates transport, coupling complexity, and marginal mass variation; a complementary pair-aware residual compares observed image-caption pairs with the UOT soft matching. On Flickr8K and COCO-1K with frozen CLIP, OpenCLIP, and SigLIP encoders, caption degradation reduces Flickr8K Recall@1 from 0.559 to 0.003. Across six dataset-model conditions, the pair-aware residual tracks retrieval degradation with mean absolute Spearman 0.973, compared with 0.392 for the mean gap. The association remains stable across five random COCO-1K subsets at $0.954\pm0.026$, with a minimum of 0.943. UOT barycentric updates reduce the transport objective while degrading retrieval, distinguishing geometric objective descent from task improvement. These results establish UOT-Gap as a diagnostic for caption quality, modality alignment, and retrieval robustness.

---


### 110. [$Φ$-Bench: Can Large Language Models Engineer the Infrastructure That Powers Them?](https://arxiv.org/abs/2609.10226)

**<font color=#1a73e8>作者：</font>** Leilei Ding, Shumin Wang, Yuting Huang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated remarkable capabilities in reasoning and code generation, raising the prospect that they could assist in developing and optimizing the very infrastructure that powers them. However, existing benchmarks mainly focus on isolated kernels, predefined operators, or pre-specified optimization targets, and therefore fail to evaluate the ability of LLMs to perform open-ended, long-horizon LLM infrastructure engineering. To address this gap, we present $\Phi$-Bench, a benchmark for systematically evaluating LLMs on engineering the LLM infrastructure stack. Derived from optimization problems studied in frontier research and grounded in real-world code repositories, $\Phi$-Bench provides broad coverage of the LLM infrastructure stack and spans tasks of varying complexity, ranging from localized kernel-level function completion to long-horizon implementation and end-to-end system optimization. Extensive experiments on frontier LLMs reveal their current capabilities and limitations in engineering complex LLM infrastructure, offering insights into the challenges that remain on the path toward autonomous optimization of future AI infrastructure.

---


### 111. [The Answer Path and the Grounding Instruction in LLM Question Answering over Knowledge Graphs](https://arxiv.org/abs/2609.10237)

**<font color=#1a73e8>作者：</font>** Arquimedes Canedo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A graph retrieval-augmented generation pipeline chooses which triples to put in the prompt, a syntax to write them in, an order to write them in, and a sentence telling the model what to do with them. We vary all four over six large language models and two knowledge-graph question answering benchmarks. Two of the four choices move the answer and the other two are flat. The first is whether the answer path, the triples needed to reach the answer, is in the prompt at all. Holding the number of triples fixed and replacing every triple that is not on the chain with material from an unrelated entity changes answer accuracy by +0.003 F1, while removing the chain costs most of what the graph was worth. Retrieval budget belongs on recall, and precision in the range we can test buys nothing. There is no retriever here: subgraphs come from gold SPARQL, so precision describes the context we build, not a system setting. The second is the grounding instruction. With no facts in the prompt, telling a model to answer using only the provided facts drops F1 from 0.299 to 0.035, a factor of 8.63. That figure describes an evaluation with an empty context arm rather than a working pipeline, and an experiment that applies the instruction to its context arm but not to its no-context baseline manufactures a spurious finding that graph context hurts at depth. We found one in our own results and retract it. Syntax, triple order and subgraph size produce no effect we can measure at multi-hop depth. The comparison that would price the grounding instruction against correct context is not measurable with a format-sensitive scorer, because the instruction determines the response format; we report it as an open contrast rather than a number.

---


### 112. [Two-Token Features and Small-Large Ensembles for VLM Hallucination Detection](https://arxiv.org/abs/2609.10244)

**<font color=#1a73e8>作者：</font>** Eli Schwartz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present our system for the SHROOM-Visions 2026 shared task on character-level VLM hallucination detection. A small ($4$B-parameter) VLM is fine-tuned as a per-token classifier reading a two-token feature from its own hidden states, and is ensembled with a $\sim$400B zero-shot VLM judge at prediction time. Both components see off-the-shelf OCR of any visible in-image text. We use synthetic hallucination data generated by the large model as a source of ensemble diversity, and use validation to select feature layer, training data and OCR grounding. Our official entry reaches mean Cor $0.487$ / Cor-lbl $0.387$ on the hidden test set, placing $6$th/$28$ (EN), $6$th/$21$ (FR), $8$th/$21$ (IT) and $7$th/$22$ (ZH) on the task's primary Cor-lbl metric.

---


### 113. [DiSCo: A Distribution-First Steering and Cultural Prior Evaluation Framework for Measuring Cultural Preference Bias in LLMs](https://arxiv.org/abs/2609.10253)

**<font color=#1a73e8>作者：</font>** Bhuvan Arora, Devesh Saraogi, Sravya Varada 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in globally used assistants, yet their default choices in culturally grounded everyday situations can systematically favour some cultures over others, affecting localisation, user trust, and equitable behaviour. Existing cultural benchmarks evaluate accuracy against a single "correct" answer, making it difficult to characterise an LLM's cultural preference prior when multiple culturally grounded responses are all valid; they also conflate default preferences with context-driven adaptation. We propose DiSCo, a distribution-first forced-choice evaluation framework that isolates default cultural priors and tests steerability via a four-level context gradient (C0--C3). Using DiSCo-Bench (304 items) derived from BLEnD spanning 12 cultures, we evaluate six diverse instruction-tuned LLMs. Default priors are heavily concentrated, with UK and US together absorbing approximately 35\% of all selections despite representing only 2 of 12 cultures. Most critically, prompt-based steering consistently widens the selection gap between high- and low-resource cultures, and injecting explicit cultural facts produces negligible distributional disruption, confirming that cultural preference bias cannot be resolved through prompt-based personalisation alone.

---


### 114. [What Should an Agent Forget? Separating What Is Stored from What Is Used](https://arxiv.org/abs/2609.10263)

**<font color=#1a73e8>作者：</font>** Yuhang Li, Yuchen Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Persistent language agents need stored experience to remain available across time, while each answer requires evidence suited to a particular question. A superseded fact can mislead a current-state answer and still be essential for a historical query. We present RD-Forget, a training-free framework that separates what an agent stores from what it uses. A retained source archive preserves observations, and a query-conditioned memory view controls their influence on the current answer. A frozen language-model curator extracts relevant evidence, groups facts into semantic slots, and preserves the relations needed for multi-hop reasoning. Same-slot replacement links suppress superseded values in current-state contexts, while intent-aware retrieval makes earlier evidence eligible again. A rate-distortion formulation guides construction of the answer-time view within a memory budget. Experiments span conversational memory, knowledge updating, fact consolidation, long-context reasoning, and personalization under a shared answering pipeline. The results associate accurate answers with both query-relevant evidence construction and control over obsolete alternatives. Configurations without forgetting or query conditioning have the largest score deficits, while slot grouping, historical access, and relation preservation contribute complementary functions. Retaining history while selectively controlling its use offers a practical way to accommodate changing facts and future questions.

---


### 115. [Maverick: Private and Verifiable LLM Inference Made Practical via Matrix-Vector Multiplication Delegation](https://arxiv.org/abs/2609.10264)

**<font color=#1a73e8>作者：</font>** Ben Merbaum, Mohammad Amin Raeisi, Wenhao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open-source large language models (LLMs) are increasingly competitive with closed-source models while offering transparency and the ability to run inference without exposing user inputs to a service provider. However, running large-scale models locally requires substantial computational resources. In practice, users may still resort to a third-party provider, giving rise to privacy and correctness concerns. Existing solutions that address these problems often impose substantial server overhead or introduce additional trust assumptions.
In this paper, we present Maverick, a novel approach to private and verifiable LLM inference based on a protocol for delegating matrix-vector multiplication, a dominant operation in LLMs. At its core, Maverick provides, to our knowledge, the first information-theoretically sound verification protocol for matrix-vector multiplication delegation with transparent preprocessing, efficient (batch) verification, and virtually no server overhead. We combine this verification primitive with LPN-based pseudorandom masking to provide input privacy.
We implement our matrix-vector delegation primitive and use it to build an end-to-end prototype of Maverick, which we evaluate on Qwen3-4B by measuring throughput in tokens per second. We evaluate client configurations with 1-8 threads. With one client thread and a CPU server using up to 128 threads, Maverick achieves throughput gains over local inference of up to 17x when privacy masks are generated online, 45x when they are precomputed, and 44x when only verification is required. With four client threads, the corresponding gains are 13x, 18x, and 17x. When server computation is no longer the bottleneck, client-side microbenchmarks with simulated network delay show speedups of 12x-20x, 34x-135x, and 38x-157x.

---


### 116. [KVShareArena: KV-Cache Reuse Across Contexts and Model Checkpoints](https://arxiv.org/abs/2609.10266)

**<font color=#1a73e8>作者：</font>** Xi Shi, Qian Lou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM serving systems already reuse KV caches, but only when the reused text sits at the very start of the prompt. Two growing workloads break this condition: a retrieval-augmented generation server assembles a different set of retrieved chunks for every query, and a multi-agent coordinator reads reports written by other agents. Reused inside a new prompt, a cache carries the wrong positions and never attended to the other sources. The cache may also have been written by a different checkpoint of the same model family, which changes the stored values. Repair methods for such caches have appeared in three separate communities, each measured on its own terms, and existing benchmarks test only exact-prefix reuse, where nothing is lost. KVShareArena benchmarks KV-cache reuse across prompt contexts and model checkpoints on retrieved chunks and agent reports. It scores every method by the fraction of the gap it recovers between no cache and full recomputation, and charges compute, memory, and per-request latency with the cache in hand, reporting the one-time cost of building a cache separately. We find that correcting positions, which needs no recomputation, is enough until a question needs several sources at once. There, only methods that pay, by re-encoding part of the cache or by training, recover half to two thirds of the gap; unrepaired caches can be worse than no cache. Cache-compression methods that are harmless on a single prompt fall significantly behind position correction on freshly written agent reports. These patterns hold across three model boards. When a different checkpoint wrote the cache, training-free methods are barely affected, while an adapter trained on one checkpoint's caches loses quality. Harness, frozen querysets, and cost accounting ship as a pip package with an automated submission workflow and a public leaderboard.

---


### 117. [Isotropic Embedding Perturbations for Robust Vision Language Encoders](https://arxiv.org/abs/2609.10292)

**<font color=#1a73e8>作者：</font>** Hyesong Choi, Daeun Kim, Song Park 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Data augmentation is fundamental to training modern deep vision and multimodal models. While individual methods, such as RandAug, CutMix, Mixup, RandErase, and DropPath, offer strong regularization effects, their combined use has saturated in performance due to overlapping functionalities, and aggressive pixel-level manipulations may disrupt delicate cross-modal alignment. This saturation motivates the search for a new augmentation axis within the embedding space rather than the input space. We introduce Aether, a simple plug-in method that applies diffusion-style random perturbations in the embedding space via controlled alpha-mixing, specifically designed to provide isotropic regularization that remains semantically consistent. Inspired by feature-space perturbations in language models and image degradation in generative pretraining, Aether induces mild yet effective perturbations that smooth the representations without compromising the fine-grained structural information required for strong vision-language encoders. Across diverse architectures and across multiple recognition tasks, Aether delivers consistent gains over the advanced recipe combining CutMix, Mixup, DropPath, and RandAug---a level of improvement rarely observed with modern augmentation alternatives. Notably, Aether demonstrates superior effectiveness in multi-modal alignment, succeeding where traditional pixel-space augmentations fail by providing a stable, isotropic regularization signal that respects the integrity of the high-dimensional feature space.

---


### 118. [GANDR: Claim Auditing for Verifiable Legal Answer Generation](https://arxiv.org/abs/2609.10293)

**<font color=#1a73e8>作者：</font>** Chen Qian, Yimeng Wang, Yu Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In high-stakes domains such as legal practice, a language-model answer is only useful to the extent that a reader can verify each claim against the source the system cites. Current grounded-generation pipelines score the answer as a whole, so a correct conclusion can rest on fabricated or loosely matched citations and still score well. Closing this gap requires both a system built for per-claim verification and an evaluation that measures it. We introduce GANDR (Grounded ANswer DRafter), a two-agent system in which a Drafter writes an answer in a structured legal-reasoning format and a separate Critic, with the same view as a human verifier, audits each claim against its cited source and emits a per-claim audit trace on every round. We pair it with a strict correctness criterion requiring every citation to resolve to a passage the retriever returned. On a 185-item legal benchmark where all six systems share one backbone, one retrieval surface, and one citation instruction, GANDR ranks first on every primary metric, reaching 70.8% strict accuracy and leading the strongest baseline by 11.3 points (p<0.01). Reverting the protocol-anchored commit rule lowers strict accuracy by 22.7 points, and the strict lead stays positive on three further backbones, at +3.2 to +6.5 points. This lead traces to the Drafter configuration and the protocol-anchored commit, not to rewriting. Against two law-trained annotators the audit flags under-supported claims at F1 0.84 as a binary detector, while its four-way verdict labels agree only weakly and are advisory. Code is available upon request.

---


### 119. [RiLM: Parameter-Efficient Language Modeling via Geodesic Decoding](https://arxiv.org/abs/2609.10305)

**<font color=#1a73e8>作者：</font>** Fang Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models under one million parameters matter for edge deployment, domain adaptation, and reproducible research, yet a two-layer LSTM or Transformer at embedding width d = 128 still spends roughly one third of its capacity on the output matrix W_out in R^(d x |V|). We propose Riemannian Language Models (RiLM), which remove that layer entirely: context unfolds as a trajectory on a Riemannian manifold, and next-token probabilities arise from squared geodesic distance between the current state and vocabulary embeddings. The same embedding map serves input and output -- decoding is geometry. We instantiate the framework on flat R^d (Flat RiLM) and the Poincare ball H^d (HypRiLM) with a shared MLP composition map phi (~290k parameters, d = 128, |V| = 2000). Across five seeds on WikiText-2, HypRiLM reaches 54.2 +/- 0.2 validation perplexity versus 87.6 +/- 0.6 for Flat RiLM; tied and matched LSTM, Transformer, and SSM controls remain at 113-147 PPL on WT-2 -- HypRiLM leads by roughly 2x over the strongest tied recurrent baseline (SSM, 113.0 +/- 3.8). Penn Treebank and a 10k-vocabulary stress test confirm that geodesic decoding transfers across corpora and larger |V|, while hyperbolic curvature helps selectively. We also characterize boundary collapse in naive hyperbolic recurrence and show how Mobius stabilization restores trainability. Claims are scoped to controlled small-model comparisons, not full-vocabulary state of the art.

---


### 120. [TRACE: Training Reasoning Agents for Causal Exploration with Synthesized Rewards](https://arxiv.org/abs/2609.10315)

**<font color=#1a73e8>作者：</font>** Rui Sun, Zhan Shi, Bing He  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has advanced language-model reasoning in domains such as mathematics and code, where objective answers are inexpensive to check. Diagnostic reasoning over complex data lacks this advantage: establishing the true cause of an anomaly often requires costly expert investigation and may remain ambiguous after the fact. We ask whether this asymmetry of verification can instead be engineered. We sample an intervention, inject it into a controlled simulator, and generate the observations it would produce. The hidden intervention provides an oracle label and objective reward, while the agent must still investigate noisy, confounded, and distributed evidence.
We instantiate this approach in TRACE, a digital-advertising diagnostic environment with 12 root causes and fine-grained segment attribution. Agents investigate each episode using Python and SQL and must identify both the root cause and, when applicable, the affected segment assignment. On a held-out 235-episode test set, the strongest prompted baseline, Claude Opus 5, reaches 0.686 FullAttr@1. Supervised fine-tuning raises Qwen3.5-35B-A3B from 0.159 to 0.637, and subsequent RL with synthesized rewards reaches 0.757, outperforming all evaluated prompted baselines, including frontier closed-source models and a prompted Qwen3.5-122B-A10B model. The resulting policy also uses substantially fewer tool calls than the prompted 35B base. These results provide evidence that access to a scalable, objective training signal can be a more important constraint than model scale alone. More broadly, simulation-based verification can make otherwise ambiguous diagnostic reasoning tasks amenable to scalable reinforcement learning.

---


### 121. [On-Policy Distillation for Vision-Language Model Adaptation, an Effective Paradigm on Low-Quality Multimodal Data](https://arxiv.org/abs/2609.10321)

**<font color=#1a73e8>作者：</font>** Hongyuan Zhang, Xianda Guo, Yanlun Peng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation offers an efficient route to transfer a task-adapted vision-language teacher to a compact student. The training target in current vision-language distillation methods is typically constructed from the teacher prediction and applied uniformly to all training samples, making it unreliable under class and domain shifts. In this paper, we argue that distillation target construction should be treated as a dynamic training decision rather than a fixed recipe. To this end, we propose OnPoKD, an on-policy distillation framework for vision-language model adaptation. To the best of our knowledge, OnPoKD is the first framework that applies on-policy distillation to vision-language model adaptation by learning target construction as a policy decision. OnPoKD learns a lightweight controller that constructs sample-wise adaptive targets using reliability and disagreement cues from the teacher model, student model, and zero-shot prior. Instead of relying on a fixed teacher prediction, the controller dynamically balances teacher supervision, zero-shot prior guidance, and hard-label anchoring through bounded policy actions, allowing the distillation target to adapt to varying sample reliability and training stages. The policy controller is updated with validation feedback, encouraging target construction to optimize transferability rather than merely fitting the training distribution. Since the controller is only used during training, OnPoKD can be seamlessly integrated into existing vision-language distillation pipelines while preserving the original inference architecture and test-time cost. Extensive experiments on Base-to-novel generalization and Cross-dataset transfer benchmarks show that OnPoKD consistently improves over strong vision-language distillation baselines.

---


### 122. [Learning to Adapt and Calibrate: Score Distribution Alignment for Few-Shot Uncertainty Prediction in Medical VLMs](https://arxiv.org/abs/2609.10333)

**<font color=#1a73e8>作者：</font>** Xuan Cuong Ngo, Ngan Le  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Uncertainty estimation for medical vision--language models (VLMs) using conformal prediction has gained increasing attention due to its distribution-free coverage guarantees. However, standard conformal prediction relies on exchangeability between calibration and test data and typically requires a sufficiently large calibration set to obtain reliable coverage. These assumptions are difficult to satisfy in few-shot transfer settings, where only a small labeled support set is available to adapt a pretrained VLM to a new medical task, while an unlabeled query set is used for evaluation. Supervised fine-tuning on the support set changes the model parameters and consequently shifts the nonconformity score distribution, breaking exchangeability between calibration and query samples and leading to unreliable coverage under distribution shift. Existing transductive conformal adaptation methods often preserve validity by avoiding supervised updates. While this helps maintain conformal assumptions, it underutilizes the scarce labeled support data and limits task adaptation, which is the primary objective in few-shot learning. In this setting, conformal prediction should serve as an uncertainty estimation layer that supports the adapted model, rather than preventing adaptation itself. To this end, we propose AlignCP, a framework that reconciles supervised few-shot adaptation with conformal uncertainty estimation under non-exchangeability. AlignCP learns a reweighted calibration distribution that reduces the score-level discrepancy between the labeled support set and the unlabeled query set. By aligning the one-dimensional nonconformity score distributions, AlignCP aims to close the coverage gap induced by adaptation without requiring query labels.

---


### 123. [From Symbolic Perception to Logical Deduction: A Framework for Guiding Language Models in Geometric Reasoning](https://arxiv.org/abs/2609.10335)

**<font color=#1a73e8>作者：</font>** Weichen Dai, Rafael Medeiros Cabral, Ziyi Shou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Plane geometry remains a significant challenge in AI, requiring the integration of visual perception and mathematical reasoning. While Large Multimodal Models (LMMs) naturally handle visuo-linguistic inputs, they are often computationally intensive and opaque. We demonstrate that a pure Large Language Model (LLM), when equipped with specialized modules, can rival state-of-the-art LMMs on complex geometry problems. Our framework integrates a Geometric Vision Parser, which translates diagrams into symbolic form, with a Symbolic Solver that performs formal deductions, thereby mitigating hallucinations and promoting interpretable reasoning. To enable rigorous evaluation, we curate a benchmark of challenging problems from the 2025 Chinese Zhongkao examinations, ensuring data novelty and testing deeper deductive skills. Experiments demonstrate that our approach achieves performance comparable to Gemini 2.5 Pro while delivering clearer, human-like solutions.

---


### 124. [Beyond One-Size-Fits-All: Sample-Adaptive Strategy Routing for Vision Token Pruning in MLLMs](https://arxiv.org/abs/2609.10346)

**<font color=#1a73e8>作者：</font>** Haiji Liang, Pengfei Zhou, Zhenglin Wan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) process hundreds or thousands of visual tokens per image, incurring prohibitive inference costs. While existing vision token pruning methods mitigate this overhead, they implicitly assume that a single fixed pruning strategy can be applied uniformly across all inputs. Our analysis further reveals that ranking pruning methods by average benchmark accuracy conceals substantial sample-wise complementarity: although the average-best strategy excels overall, alternative strategies prove superior on a significant fraction of individual samples. To harness this diversity, we propose VIP-Router, a lightweight VIsion Pruning Router that adaptively selects the pruning strategy predicted to be best suited to each input at a specified pruning level. Conditioned on low-cost visual and textual features, VIP-Router identifies the most suitable candidate strategy while retaining full-token inference as an option when pruning is predicted to be unfavorable. Evaluated on a curated suite of pruning-sensitive visual perception benchmarks, VTC-Bench Group A, VIP-Router consistently outperforms the best fixed strategy baseline across all reduction ratios, achieving a 26.9% relative improvement in average accuracy, and a 22.0% relative increase in average utility after accounting for realized token cost. Crucially, VIP-Router operates in a plug-and-play manner without modifying underlying pruning algorithms or model weights, introducing trainable parameters equivalent to merely 0.017\% of the backbone. Furthermore, VIP-Router proves effective across various MLLM backbones and yields consistent gains on unseen benchmarks, highlighting the potential of sample adaptive routing for visual token pruning.

---


### 125. [Why Is Video Still So Expensive? A Survey of Inference-Efficiency Mechanisms in Video and Audiovisual LLMs](https://arxiv.org/abs/2609.10355)

**<font color=#1a73e8>作者：</font>** Killian Steunou, Yannis Tevissen, Mounîm A. El Yacoubi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video understanding has rapidly evolved toward video large language models (VideoLLMs): systems that couple video representations with pretrained large language models and condition generation on a textual prompt. Their strong performance on captioning, question answering, retrieval and temporal grounding comes at a computation and memory cost that grows with frame count and context length, limiting deployment in real-time, mobile and resource-constrained settings. This survey covers inference-efficiency mechanisms for visual and audiovisual VideoLLMs that report concrete reductions in parameter count, FLOPs per input, latency, memory, or visual and audio token count. We analyze bottlenecks across frame sampling, modality encoding, connector-level token reduction, and LLM prefilling and decoding. We organize methods by the pipeline stage at which they act, covering VideoLLMs developed since late 2022 together with earlier frame-sampling and vision-encoder mechanisms that remain components of current pipelines. We assemble literature-reported accuracy--cost comparisons under shared host models and input protocols wherever available, distinguish them from heterogeneous cross-paper evidence, and identify gaps in audiovisual efficiency and standardized evaluation. We maintain a repository at this https URL.

---


### 126. [Spot-the-shift: Evaluating Grounded Image Difference Captioning of Long-term Changes](https://arxiv.org/abs/2609.10356)

**<font color=#1a73e8>作者：</font>** Benedetta Liberatori, Nermin Samet, Paolo Rota 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-term change understanding from images of the same place revisited over time is a challenging task with applications in map maintenance and urban infrastructure monitoring. Prior work addresses it either through pixel-level prediction or difference captioning, neither of which is sufficient to reliably measure how well models detect and describe such changes. We introduce SPOT-THE-SHIFT, a human-verified benchmark for grounded image difference captioning of long-term changes in real-world driving scenes. Our benchmark provides natural language captions and spatial masks for structural changes across each image pair. We further propose an evaluation protocol that reliably assesses models' captioning ability, validated through human studies. Benchmarking state-of-the-art MLLMs, we find that models struggle with the fine-grained multi-image spatial capability required for this task. Finally, we develop a synthetic data generation pipeline that improves an off-the-shelf MLLM without sacrificing general capabilities.

---


### 127. [PACE: Perceived-Latency-Aware Cascading Service Routing and Filler Control for QoE-Efficient Retrieval-Augmented Dialogue Serving](https://arxiv.org/abs/2609.10372)

**<font color=#1a73e8>作者：</font>** Lin Huang, Yujuan Tan, Weisheng Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present the PACE, a framework for retrieval-augmented dialogue serving that formalizes Perceived Time-to-First-Response (PTFR) as a QoE objective and minimizes it under quality/cost constraints. Unlike prior work on cascaded routing, semantic caching, or adaptive retrieval, PACE jointly controls which answer source composes the response and what fills the waiting window. Deployed on a humanoid-robot sales service, it combines three mechanisms: a load-adaptive cascading router, a joint path-filler controller, and volatility-aware cache admission. On 75k CarQA requests, the cascade halves pure-LLM PTFR at P95 (0.29 vs 0.53s at c16). The adaptive controller reaches 0.41s P95, outperforming RAG by 2.4 times at high load with equal quality. The filler controller cuts calls by 94% with zero conflict. Volatility-aware admission reduces stale answers from 86% to 0%. A gating rule ensures the controller never worse than the baseline, with exposure bounded by one hold period. This is the first quantification of filler-answer conflict risk in deployed services.

---


### 128. [Can Foundation Models Moderate Online Content? Evaluating Instruction- vs. Example-Driven Policy Operationalization](https://arxiv.org/abs/2609.10410)

**<font color=#1a73e8>作者：</font>** Ayan Majumdar, Shounak Paul, Pushpdeep Singh 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The growing complexity of content moderation policies presents a critical challenge for their consistent operationalization. While foundation models possess the basic capabilities needed to confront this challenge, whether they can reliably moderate online content remains an unanswered question. In this paper, we systematically compare two competing paradigms for Vision-Language Model (VLM) guidance: an instruction-driven approach where models reason from policy precepts, and an example-driven approach where they generalize from prior precedents. We ground this investigation in ModerationBench, a new benchmark of 4,000 manually annotated, in-the-wild posts from the Bluesky platform. Our experiments reveal that foundation models can substantially outperform Bluesky's deployed moderation system, nearly tripling its $F_1$ score (0.60 vs. 0.22) on Random Posts in the benchmark, with both instruction- and example-driven paradigms achieving comparable peak effectiveness. Our findings thus chart a path toward reliable and adaptable policy operationalization at scale.

---


### 129. [Fortunate Recall: Ontology-Driven Memory Lifecycle Management for Persistent Coherence in LLMs](https://arxiv.org/abs/2609.10413)

**<font color=#1a73e8>作者：</font>** Ansuman Mullick, Eray Tüzün  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current LLM memory systems treat all personal facts identically, so stores grow without bound while retrieval precision degrades. The core challenge is lifecycle management: which memories should persist, which should be replaced, and at what rate, conditioned on the behavioral type of each fact. Fortunate Recall (FR) is a composable policy layer that classifies personal facts into a 10+1 behavioral ontology and applies category-specific lifecycle policies (differential temporal decay, slot-key supersession, event-time validity, and category-aware retrieval routing) as deterministic functions over LLM-extracted metadata. FR-Bank, our infrastructure-independent implementation, reaches a 76.9% pass rate on LifecycleBench, a new 516-question temporal-disambiguation benchmark, ahead of Mem0, A-MEM, Memory-R1, and MemoryOS (61% to 70.5%), and 75.2% on the full LongMemEval-S under the canonical Wu et al. judge protocol, so lifecycle policies impose no measurable cost on standard retrieval. A pre-registered ablation locates the gains: replacing the typed layer with three generic lifecycle primitives leaves correctness statistically unchanged (-1.7pp, 95% CI [-6.0, +2.7]), so the generic lifecycle metadata carries the correctness advantage, while the behavioral ontology carries calibration, halving downstream confabulation (12.0% vs 24.2%, p<0.001). End-to-end, FR-Bank cuts confabulation from Mem0's 45.1% to 22.4% over answered queries and from 32.2% to 13.0% over all queries while answering more of them correctly (31.2% vs 18.6%); the ranking replicates on the open-weight Kimi K2.5. The decomposition transfers to BEAM, an independently built benchmark: 46.8% correct vs Mem0's 32.9% over 280 questions, with the ontology's benefit concentrated in contradiction resolution and saturating near seven policy clusters. The ontology, benchmark, and code are released.

---


### 130. [TrajMark: Ownership Attribution and Segment-Level Tamper Localization for Coding-Agent Trajectories](https://arxiv.org/abs/2609.10416)

**<font color=#1a73e8>作者：</font>** Bokang Zeng, Zheng Gao, Xiaoyu Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Watermarking the final patch produced by a coding agent provides provenance evidence for the submitted artifact, but does not authenticate the visible process that produced it. Behavioral watermarking methods primarily provide a global detection or identifier-recovery signal, so a locally edited trajectory may retain sufficient ownership evidence without revealing which protected region has become inconsistent. To address this limitation, we propose TrajMark, a training-free, symmetric-key, visible-only trajectory watermarking framework that separates robust ownership attribution from fragile local integrity verification. Our framework consists of two complementary layers: a sparse owner layer that encodes a six-bit deployment identifier by rewriting a keyed subset of naturally occurring READ actions into masked linear equations, and a localization layer that inserts linked Q12 ordinary, group, and terminal seals to commit to protected critical-action segments. This separation allows ownership evidence to accumulate robustly across trajectories, while local modifications perturb nearby keyed commitments and expose the affected protocol region. We further provide a design-level analysis of owner recoverability, integrity collision probability, structural overhead, and localization behavior. Across three coding-agent frameworks and three LLMs, TrajMark recovers the exact owner in all evaluated clean full-watermark batches. Under exhaustive eligible single-site attacks it detects 95.5%-100% of edits, and under random single-action corruption it localizes 95.8% of modified sites to an accepted protocol region rather than to the individual action. Owner marking adds no trajectory actions; the integrity layer adds explicit read-only seals, and matched Pass@1 is 26.9% versus 26.3% for unwatermarked runs.

---


### 131. [Glyph: A Multi-Strategy Agentic System for Column Description and Sensitivity-Ontology Tagging of Enterprise Data Catalogs](https://arxiv.org/abs/2609.10430)

**<font color=#1a73e8>作者：</font>** Kostia Kudriavtsev, Parvez Rafi, Sha Sundaram  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Enterprise data lakes accumulate tables faster than human stewards can document or classify them, leaving columns with missing descriptions and unassigned governance labels. This documentation debt undermines data discovery, access control, and regulatory compliance. We present Glyph, a production system that frames two coupled problems, column description generation and column type annotation for data classification, as cooperating LLM agents orchestrated as stateful graphs. The Descriptor grounds generation in the pipeline source code that produces each column, retrieved on demand from an enterprise GitHub via a reasoning--acting tool loop (active Retrieval-Augmented Generation). The Tagger assigns labels from a governed 275-leaf Data Classification Ontology by running three complementary strategies in parallel (a description tagger, a line-of-business regex tagger, and a metadata tagger backed by a fine-tuned contrastive encoder over a vector database), then fuses their ranked outputs with Reciprocal Rank Fusion (RRF). We fine-tune a 6-layer MiniLM metadata encoder with an in-batch contrastive objective, lifting same-tag retrieval on an in-distribution held-out split from NDCG@10 0.55 to 0.92 (MAP@100 $0.19 \rightarrow 0.90$) relative to the stock base encoder. We report end-to-end multi-label tagging quality under a recall-weighted F2 objective across three evaluation groups, an ablation isolating each strategy and the RRF fusion, and the engineering decisions that distinguish Glyph from prior column-type-annotation work and from commercial value/regex sensitivity scanners: value-free and code-grounded design, per-tag provenance, and graceful degradation. Together these make multi-agent LLM cataloging auditable and operable as a production service.

---


### 132. [Do speech foundation models really learn words?](https://arxiv.org/abs/2609.10434)

**<font color=#1a73e8>作者：</font>** Robin Huo, Ewan Dunbar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-supervised speech foundation models are now used in a wide array of downstream applications, including traditional speech recognition and as the basis for tokens in speech-aware language models. Attempts to understand their usefulness have largely focused on probing their representations' ability to discriminate phonemes and words. However, discriminative ability for words need not imply specialized representation of words per se. Good discrimination of words may be explained by good encoding of word form (phonemes) rather than form-independent word representations encoding identity or syntactic/semantic properties. By partialling out phoneme information using residualization, we show that, in later layers, HuBERT and wav2vec 2.0 do in general learn representations which encode words with reasonable fidelity independently of local phonetic content. We show that this simple approach to disentanglement can enhance higher-order linguistic information in word discovery tasks.

---


### 133. [ConvMem: Convolutional Memory for Long-Context Reasoning](https://arxiv.org/abs/2609.10441)

**<font color=#1a73e8>作者：</font>** Hongming Zhang, Zhaozhen Gu, Fengshuo Bai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) have demonstrated impressive capabilities, they often struggle with extremely long contexts due to fixed context limits. To address this, sequential approaches like MemAgent extend the effective context by reading text in segments and iteratively updating a fixed-size memory. However, this sequential paradigm suffers from high latency and requires costly reinforcement learning (RL) training, which can lead to overfitting on specific datasets. To overcome these limitations, we propose ConvMem, a training-free, highly parallelizable framework that reformulates long-context reasoning as a hierarchical convolution. Inspired by CNNs, ConvMem treats an LLM prompted with a specific query as a convolutional kernel. This kernel summarizes text segments hierarchically, shortening the reasoning path from a linear chain into a logarithmic tree. Specifically, ConvMem integrates \textit{Configurable Strides} and \textit{Skip Connections} to ensure robust evidence capture and propagation, while employing \textit{Multi-Kernel Convolution} to decompose complex queries into disentangled semantic channels. This design not only mitigates error accumulation but also enables massive parallelization across both text segments and reasoning threads. Experiments on RULER-HotpotQA and RULER-2WikiMultiHopQA demonstrate that ConvMem outperforms training-free baselines and avoids the risk of overfitting to parametric priors often observed in RL-trained models on out-of-distribution tasks.

---


### 134. [Building Multilingual Bridges: Data Mixing as the Pillar of Generalization for In-Language Reasoning](https://arxiv.org/abs/2609.10445)

**<font color=#1a73e8>作者：</font>** Mehrnaz Mofakhami, Ananya Sahu, Alejandro R. Salamanca 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning language models have made substantial advances on a variety of complex tasks, yet their capabilities remain overwhelmingly English-centric: models primarily reason in English regardless of the language they are prompted in. This is inaccessible for non-English-speaking users, risks losing the intent of the original question, and forgoes knowledge more readily expressed in the target language. In this work, we advance L2 reasoning, the ability of a model to reason consistently in the language of the user's prompt, thus building an in-language bridge between the prompt and the answer. We approach this problem from a data-centric angle, investigating how to optimize data composition and scheduling in SFT for reasoning generalization. Building Tiny Aya L2-Thinker at 3.35B scale, we achieve an L2 reasoning rate above 93% across 60 languages on 6 benchmarks spanning math, commonsense reasoning, instruction following, open-ended generation, and cultural reasoning while keeping performance strong. We show the path to generalizing L2 reasoning to held-out languages goes through broader language coverage, readily available multilingual non-reasoning data, and a sufficient English reasoning backbone. These findings indicate that reasoning is a language-agnostic behavior that can be transferred across typologically diverse languages through careful data mixing and without requiring reasoning supervision in every target language. We release our model weights and multilingual reasoning data to support further research on accessible, in-language reasoning.

---


### 135. [Towards Tackling Application Logic Flaws through Autonomous Formal-Logic Modeling and Automated Reasoning](https://arxiv.org/abs/2609.10537)

**<font color=#1a73e8>作者：</font>** Yiwei Fang, Yichen Liu, Ze Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Logic flaws pose significant challenges in the design and implementation of modern, semantically rich systems and applications, impacting security, privacy, and trust. These flaws are inherently tied to business-specific semantics and threat models, making their discovery and reasoning difficult and hard to scale. Real-world systems often exhibit diverse application features, complex protocol logic, and domain-specific threat models, necessitating substantial human effort and domain expertise for effective security analysis. In this paper, we introduce LL-Verifier, a novel, automated framework for identifying logic vulnerabilities built on (1) large language models for autonomous modeling, and (2) logic model checkers for rigorous reasoning. LL-Verifier processes natural language inputs, in particular protocol descriptions and security goals, to automatically generate formal logic models and properties expressed in a new logic language built on a generic logic language Maude, optimized for modeling arbitrary application-level semantics. These formal models are then converted into logical state machines, enabling exhaustive, rigorous verification through logic level model checking. This approach streamlines the analysis of diverse, application-level protocols deployed in real-world scenarios, offering automated, exhaustive, and precise reasoning within their logical constraints. We evaluated the high effectiveness, efficiency, and practicality of LL-Verifier by applying it to 27 access control protocols of widely used IoT devices, which come with vendor-specific logic flows and semantics. While LL-verifier tackles a hard problem in application security, i.e., automatic logic flaws discovery, our analysis uncovers a range of sophisticated logic vulnerabilities in IoT protocols and devices with serious security and privacy implications.

---


### 136. [IdeaAMBIG: Benchmarking Implementation-Critical Gaps in Research-Idea Specifications](https://arxiv.org/abs/2609.10539)

**<font color=#1a73e8>作者：</font>** Yiling Ma, Yilun Zhao, Sihong Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A research idea may be novel, coherent, and scientifically plausible, yet its proposed method may remain insufficiently specified for faithful implementation. We study the codification readiness of implementation-facing research-method specifications, defined by whether they provide sufficient methodological information for a competent implementer or coding agent to construct the intended method without unsupported assumptions. We construct evidence-grounded specifications and their supported resolutions from papers, codebases, issue threads, and reproduction artifacts. We introduce IdeaAMBIG, a benchmark of 660 evidence-grounded instances: 163 real-world gaps from reproducibility reports and GitHub issues, and 497 controlled synthetic gaps injected into codification-ready references. IdeaAMBIG evaluates three capabilities: codification-readiness assessment, defect localization, and clarification action generation. Defect localization receives only the specification, whereas clarification additionally receives the annotated defect. Across 13 LLMs, the best model achieves 9.6% Macro Defect Recovery Rate on real-world instances but 80.6% Macro Clarification Action Success Rate when given the defect. In an oracle study, supplying the gold resolution raises the downstream codification-ready rate from 14% to 98%. Across all evaluated models, defect localization is the main bottleneck, with stronger clarification given the defect.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 137. [AgenticGen: Reward-Guided Agentic Video Generation for Advertising](https://arxiv.org/abs/2609.09187)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xingyuan Bu, Chengru Song, Hao Zhou 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Advertising video generation is not only a video synthesis task, but also a product-conditioned reasoning problem whose success is measured by online business metrics. Recent video foundation models can generate realistic clips from multimodal conditions, yet they do not optimize how a product should be transformed into an effective advertisement or how future generation should be improved from online business feedback. To close this loop, we propose AgenticGen, a reward-guided agentic framework that decomposes advertising video generation into two trainable reasoning stages, strategy selection and draft generation, thereby exposing optimization targets that online business feedback can supervise. AgenticGen learns a performance-based reward from accumulated online feedback and a complementary rubric-based reward aligned with human quality standards, then uses them to supervise policy optimization. DPO first moves the agentic policies toward online preferences, and GRPO further refines both stages with process and outcome rewards. Offline experiments validate the reward models and successive policy optimization. Online A/B experiments in the TikTok advertising system show that AgenticGen after DPO and GRPO improves CTR by 2.72%, CVR by 2.63%, and Advv by 9.61% over the SFT baseline.

---


### 138. [DuplexJail: Safety Alignment Breaks Under Spoken Interruption in Full-Duplex Models](https://arxiv.org/abs/2609.09420)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jaechul Roh, Deepak Chandran, Amir Houmansadr 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Full-duplex speech models accept user speech while generating responses, creating an underexplored attack surface. We introduce DuplexJail, which delivers fixed, request-independent spoken prompts through the user audio channel. We compare fixed-delay interruption after the harmful request ends with refusal-triggered interruption following a cue in the model's streaming text. Across four open-source models and 720 harmful requests from AdvBench and HarmBench, fixed-delay interruption raises whole-response attack success rates on AdvBench to 40.3% for PersonaPlex and 48.7% for PersonaPlex-RL, increases of +33.8 and +39.3 percentage points. The refusal-triggered policy reaches 35.6% and 48.6%, respectively, with all trials scored regardless of whether an interruption occurs. Selected conditions also increase FLM-Audio's harmful-response rate, while BayLing-Duplex shows decreases. These findings identify spoken interruption as a jailbreak attack vector and motivate evaluating safety throughout ongoing full-duplex interaction.

---


### 139. [Applying foundation model embeddings towards urban livability evaluation](https://arxiv.org/abs/2609.09429)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ayush Khot, Wen Zhou, Shaowen Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While accurate measurement of socioeconomic indicators remains challenging in data-scarce regions, which limits policy interventions and resource allocation, high-resolution geospatial data is widely available and can contain information on various livability statistics. We investigate which physical features are encoded within foundation model embeddings, such as AlphaEarth, AnySat, and TerraMind, and provide a systematic framework for identifying the most predictive geospatial indicators. By analyzing how different types of geospatial data influence urban livability predictions, our approach enables researchers to prioritize the most informative features for their specific applications. Additionally, we demonstrate how to leverage foundation model embeddings to enhance prediction performance for these outcomes. This work contributes a principled methodology for extracting actionable information from satellite imagery while accounting for complex spatial dependencies, with applications in predicting urban livability in regions with limited observation data.

---


### 140. [Infra-Bench CLS: A Global, Open-Source Benchmark for Critical Infrastructure Classification with Earth Observation Foundation Models](https://arxiv.org/abs/2609.09482)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Justin Guthrie, Edward Oughton, Konrad Wessels 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Critical infrastructure location data is often incomplete and unevenly distributed globally, especially in developing regions. Earth observation foundation models are proposed as a new step in enabling us to more efficiently understand the natural and built environment, raising questions as to their effectiveness in performing challenging downstream tasks. Yet, foundation models remain largely untested for detecting and classifying the facility-scale critical infrastructure that underpins a range of important societal and economic functions. Subsequently, Infra-Bench CLS is introduced as a benchmark to test foundation models on 18,756 Sentinel-1 SAR and Sentinel-2 multispectral facility-scale critical infrastructure asset images covering seven continents and 13 infrastructure classes, with results reported for the 10 retained classes. Using linear probing and fine-tuning for two training dataset levels (1.0x and 0.3x), seven foundation models are evaluated (SatlasPretrain S2, SatlasPretrain S1, CROMA, Prithvi-EO-2.0, AlphaEarth Foundations, OlmoEarth v1.1-Base, and DINOv3 ViT-L/16). When comparing macro F1 scores to a ResNet-18 supervised baseline of 39.2 percent, the best foundation model achieved 57.9 percent, a 48 percent improvement. Top performing classes were airports (F1 85.3 percent), train stations (F1 82.1 percent), and data centers (F1 77.6 percent). By contrast, many of the power sector classes perform poorly (F1 27.5-46.2 percent). These findings suggest foundation models can enable superior critical infrastructure classification, but future work should evaluate performance on higher-resolution imagery, particularly for poorly performing sectors, such as power.

---


### 141. [RobustSGPO: Search-Space Control for Agent Harness Evolution](https://arxiv.org/abs/2609.09646)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zibo Zhao, Jijun Shi, Mo Zhou 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Semantic-gradient-based prompt optimization (SGPO) improves agent harnesses using execution feedback, but its local update rule leaves the choice of edit scope and operation unresolved. We introduce RobustSGPO, which specifies the requested edit, constructs and checks the patch, and continues search from either the incumbent or retained snapshots. We evaluate permission scheduling, cumulative controls, and task-family transfer in the AgentX brainstorming workflow using 120 tasks, 95 runs, and 7,350 candidate attempts. Periodic $1\to2\to3$ scheduling exceeds fixed maximum permission by 0.28 test-score points. RobustSGPO increases completion on 30 held-out tasks from 60.0% to 80.0% and improves test quality from 3.77 to 4.14 under a 20-million-token budget. Category retention reduces source-task degradation after a shift, whereas random retention reaches a higher destination endpoint. Search-space control benefits quality through executable edits and alternative starting points, with measurable retention overhead.

---


### 142. [Stable Answers, Unfinished Reasoning: Why Self-Consensus Is Not a Safe Early-Exit Signal](https://arxiv.org/abs/2609.09989)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yunxiang Mo, Donghao Zhao, Hejia Geng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A natural way to cut reasoning-model inference cost is to repeatedly probe a single partial trajectory for its current answer and stop once probes agree -- self-consensus. We ask whether any such rule is both safe and token-saving, and whether one can be selected once and reused. A preregistered sweep of 3,520 consensus rules, replayed on frozen trajectories from two models and three benchmarks, clears none of three acceptance gates fixed in advance; the frontier reproduces on a held-out split and on two unseen models -- while a boundary-confidence control (DEER) swept through the same pipeline clears all three. The reason lies in the signal: agreement establishes that the current answer persists under a fixed probing procedure, not that the reasoning has terminated -- a consensus-termination gap. Stopping on it commits non-terminal answers. At a rule still saving 32% of the tokens, one stop in nine fires on an answer the trajectory itself later abandons, and most of those stops cut off a correction it would otherwise have made. Widening the agreement window does not remove them: the share levels off near 7%, and by then the saving has fallen to 8%. Probe re-wording and a hand-labelled error taxonomy show the agreed answer is often a placeholder the model had not settled on. Used on its own as the stop signal, agreement fails not because it is insufficiently strict, but because it repeatedly measures the wrong object.

---


### 143. [SalamandraTA at WMT 2026 Terminology Shared Task: Hard Examples Are Better Teachers](https://arxiv.org/abs/2609.09999)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xixian Liao, Maite Melero  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Terminology-aware translation asks for more than a correct translation: the output must use the exact terms a glossary prescribes. The standard recipe, fine-tuning on glossary-annotated translation pairs, hides an inefficiency: for most examples the glossary prescribes exactly what the model would have produced anyway, so they teach nothing about following a glossary. We therefore keep only the examples where the model's own translation contradicts the glossary. In a controlled study at fixed data volume, this selection alone raises term accuracy from 78.7% to 89.9%. The filtered data, built by a two-way synthetic pipeline on open models, is part of the instruction-tuning mixture of our public release SalamandraTA-7b-instruct v3.0, which, used exactly as released and wrapped in a document-level inference pipeline, forms the BSC submission to the WMT26 Terminology Shared Task Track 1. At the official WMT26 evaluation, our system achieves 94.2% term success at 74.6 chrF++, with only two of the twenty-two submissions outperforming it on both metrics. On last year's benchmark, it also surpasses our GRPO-based system, despite being trained solely with ordinary supervised fine-tuning.

---


### 144. [A Trust-Network-Based Federated Learning Framework for Multi-Center Aging Clock Prediction](https://arxiv.org/abs/2609.10108)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Chunxu Zhang, Bo Li, Wenliang Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Aging clocks quantify biological aging and help characterize individual health status. What protein interactions are important for accurate aging clocks, and are they zeroth-order or higher-order? Addressing these questions requires learning from large molecular datasets distributed across medical centers, where privacy constraints prevent centralized data sharing. Federated learning offers a natural solution but faces four challenges in this setting: limited local sample sizes, sparse and directional inter-center trust, the need to retain discriminative age prediction while supporting interpretation, and model drift and forgetting under heterogeneous cross-center data.
We propose TNFL, a trust-network-based federated learning framework that progressively propagates models along directed pairwise trust relations without centralized aggregation. TNFL combines an age-aware mixture-of-experts model with generative replay to preserve previously learned information and reduce forgetting and drift. Experiments across multiple molecular datasets show that TNFL enables effective aging-clock prediction with limited local data, provides interpretable age-dependent prediction patterns, and maintains stable performance across interaction orders.
To investigate the biological questions, we analyze TNFL-identified pairwise protein interactions and their higher-order organization through functional and network analyses. The identified interactions repeatedly form coordinated higher-order subnetworks spanning multiple aging-related biological systems, with several proteins recurring across subnetworks. These findings suggest that TNFL captures molecular relationships beyond isolated pairwise associations and reveals coherent higher-order biological organization associated with aging.

---


### 145. [Why Sample What You Can Enumerate? Exact Policy Optimization for Genomic Tool Selection](https://arxiv.org/abs/2609.10221)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haoyue Liu, Xiaoyu Ma, Ye Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning over a frozen reasoner has become a common recipe for teaching a policy which external tools to invoke. We show that this recipe becomes structurally mismatched in specialist scientific settings where the complete tool-subset space is enumerable. There, a small set of recurring computational capabilities covers the domain, so the space of tool subsets is combinatorial yet small enough to enumerate, and GRPO still estimates an action expectation from a handful of sampled rollouts. Worse, the approximation degrades as training succeeds: as the policy concentrates on preferred subsets it resamples them, sampled rewards collide, and the group-normalized advantage vanishes. On genomic reasoning the fraction of questions yielding no reward signal rises from 0.2% under a uniform reference policy to 20.8% after GRPO training. As a remedy, we introduce FGPO (Full-Group Policy Optimization), which (1) scores every tool subset and optimizes the exact action expectation, so each update sees the complete action space, and (2) precomputes the reward of each question--subset pair into an exhaustive table, removing frozen-reasoner calls from the training loop entirely. Across five frozen reasoners and three genomic benchmarks, FGPO outperforms GRPO in all 15 settings by 6.75 points on average and up to 14.20, while a standard on-demand GRPO schedule would require 2.4 times as many frozen-reasoner reward evaluations and, on GenomeQA, FGPO cuts invoked tools per question from 2.36 to 1.40.

---


### 146. [FreqFLD: Towards All-in-One Facial Landmark Detection via Frequency Modulation](https://arxiv.org/abs/2609.10278)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shun Ren, Kaijie Jin, Shengkai Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent progress in deep learning has significantly advanced facial landmark detection. However, most existing methods process features in a spatial-domain manner under a dataset-specific training paradigm, which overlooks the fact that facial landmark detection is inherently geometry-driven and sensitive to frequency variations, thereby limiting cross-dataset generalization under complex scenarios and hindering the development of a facial landmark detection model. To address this issue, we propose \textbf{FreqFLD}, a \textbf{freq}uency-modulated framework towards All-in-One \textbf{f}acial \textbf{l}andmark \textbf{d}etection. Specifically, FreqFLD introduces a Frequency Modulation Module (FreqMoM) to explicitly induce the frequency prior by decoupling and modulating low- and high-frequency components, which is then injected into subsequent feature modeling to enable balanced modeling of global facial structure and local landmark details. Furthermore, FreqFLD employs a Frequency-Modulated Mixture-of-Experts (FreqMoE), with expert selection adaptively conditioned on frequency-modulated priors, enabling flexible modeling of heterogeneous facial landmark patterns under diverse and challenging scenarios. To regularize frequency-consistent modeling under the All-in-One paradigm, we further introduce a Frequency-Consistent Routing (FreqCR) loss, which constrains the routing and assignment of frequency-aware experts to promote balanced expert utilization across diverse facial scenarios, thereby enabling stable expert specialization and achieving robust facial landmark detection. Extensive experiments demonstrate that the proposed FreqFLD achieves comparable performance on popular datasets. The code is available at: this https URL.

---


### 147. [Forgetting Only What Matters: Layer-Selective Unlearning toward Robust LLMs](https://arxiv.org/abs/2609.10439)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ravi Ranjan, Olivera Kotevska, Agoritsa Polyzou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) can memorize and reproduce sensitive, copyrighted, or otherwise undesirable training content, creating privacy, safety, and regulatory concerns. Machine unlearning offers a practical alternative to full retraining, but many existing methods apply broad or fixed parameter updates that can degrade utility and remain brittle under deployment changes such as post-training quantization, where forgotten knowledge may partially re-emerge. We propose Forgetting Only What Matters via Unlearning Layers (FOM-UL), a layer-level unlearning framework that selects transformer layers using a forget-to-retain significance score. This score identifies layers with high influence on the forget set and low sensitivity to the retain set, allowing FOM-UL to concentrate updates where they are most effective while leaving most of the model unchanged. This targeted update strategy improves the forgetting-utility trade-off and provides an empirical path toward quantization-resilient unlearning by reducing the chance that small, diffuse updates are erased by low-bit rounding. Across TOFU, KnowUnDo, and MUSE-style evaluations, FOM-UL reduces residual memorization compared with strong GA, NPO, KLD, SURE, ReLearn, and LUNAR-based baselines while preserving retain-set utility close to the vanilla model. Under 8-bit and 4-bit post-training quantization, FOM-UL maintains stronger memorization suppression and utility preservation than competing methods, and adversarial prompt evaluations show lower recovery of forgotten content. Overall, FOM-UL provides an efficient unlearning strategy that improves targeted forgetting, utility preservation, and deployment robustness without claiming formal guarantees of erasure.

---


### 148. [BrainTaskonomy: Learning How to Pretrain and What to Transfer in fMRI Foundation Models](https://arxiv.org/abs/2609.10518)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Junfeng Xia, Wenhao Ye, Junxiang Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> fMRI foundation models increasingly aggregate heterogeneous data across brain states, cohorts, and acquisition settings, yet pretraining domains are commonly treated as a flat mixture and downstream tasks are adapted independently. We study whether measured learning relations can organize both stages without modifying the backbone. During pretraining, a lightweight Brain-DiT proxy estimates difficulty and directed facilitation across ten fMRI domains, yielding a priority-guided cumulative domain curriculum combined with high-to-low-noise timestep scheduling and joint consolidation. During adaptation, controlled first- and higher-order transfer across fifteen tasks constructs a directed taskonomy, from which budgeted integer programming (BIP) selects directly supervised source tasks and target-specific routes. The joint priority-domain and high-to-low-timestep curriculum reduces v-NMSE, PSD-NMSE, and FC-MSE by 6.5%, 16.3%, and 10.5%, respectively, relative to uniform sampling over both dimensions, and shows strong downstream performance across six in- and out-of-domain tasks. The taskonomy reveals asymmetric, target-dependent transfer, while exploratory sealed-test evaluation shows larger descriptive gains for BIP policies when higher-order route spaces are available than for matched random controls. Together, these findings support organizing fMRI pretraining and adaptation by measured learning relations rather than treating domains and tasks as independent flat sets.

---


> [!TIP]
> 当前位于：**101-148**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-148**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
