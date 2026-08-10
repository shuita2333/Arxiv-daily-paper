# 🧠 大模型相关研究 | 2026年08月10日

> 本类共 **152** 篇论文：已确认 **79** 篇，待复核 **73** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-152](./part-04.md)

---

### 51. [GPTKB 2.0: Browsing, Querying, and Auditing a Disambiguated LLM-Derived Knowledge Base](https://arxiv.org/abs/2608.06992)

**<font color=#1a73e8>作者：</font>** Yujia Hu, Tuan-Phong Nguyen, Simon Razniewski  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a web demo for exploring a large-scale disambiguated knowledge base (KB) materialized from a large language model (LLM). GPTKB 2.0 contains 38.4M triples over 1.6M canonical entities, together with 207.6K consolidated relations and 66K consolidated classes. Unlike prior LLM-derived knowledge bases that largely identify entities by surface strings, GPTKB 2.0 performs context-guided disambiguation during recursive KB construction, separating homonyms and merging synonymous mentions as facts are elicited. The demo makes this process inspectable: users can browse entities, follow links across the KB, and audit the provenance of individual facts, including surface forms, candidate matches, source triples, and disambiguation decisions. The interface further supports structured SPARQL queries, natural-language questions translated to SPARQL, and entity linking from user-provided text to canonical GPTKB 2.0 entries. GPTKB 2.0 is available at this https URL, with the full KB downloadable for offline use.

---


### 52. [Beyond Foundation Models: Dimension-Aware Neural Architecture Search with Small-Data Representation Models for Cryocooler Lifetime Prediction](https://arxiv.org/abs/2608.06993)

**<font color=#1a73e8>作者：</font>** Gregor Molan, Grafika Jati, Francesco Barchi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale pretrained time-series models achieve strong results through large-scale pretraining and task-agnostic representation learning, but they rely on abundant, diverse data that industrial and scientific domains often lack. We therefore propose the FSD-RM (Family of Small-Data Representation Models) paradigm as a practical alternative for limited, domain-specific telemetry. Rather than relying on large-scale pretraining, we focus on capacity-controlled representation learning using established encoder architectures (CNN1D, LSTM, GRU, Transformer), selected for their suitability in small-data settings and interpretability.
These encoders are trained unsupervised on multivariate telemetry data and integrated into a two-stage pipeline for downstream lifetime prediction. To systematically examine architectural trade-offs under data constraints, we employ \textbf{dimension-aware neural architecture search (NAS)} to jointly optimize model capacity and input dimensionality.
Experiments on cryocooler telemetry show that the proposed approach achieves competitive predictive performance while reducing training cost and model complexity. The contribution lies in combining established representation learning techniques within a coherent, NAS-driven framework tailored to small-data regimes, with explicitly defined parameter settings and design choices. The results indicate that effective representation learning can be achieved without large-scale pretraining when appropriate inductive bias and capacity control are applied.

---


### 53. [Does More Retrieved Evidence Help Visual Retrieval-Augmented Generation with Diffusion Language Models?](https://arxiv.org/abs/2608.07006)

**<font color=#1a73e8>作者：</font>** Jiankun Wang, Yisen Gao, Ziwei Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Visual retrieval-augmented generation (RAG) commonly expands the retrieved evidence set to improve answer-page coverage, implicitly assuming that all available evidence should be passed to the generator. We show that this assumption does not hold for diffusion language models (DLMs): retrieving more pages increases answer-page recall, whereas unconditionally passing all retrieved pages to the generator often reduces answer accuracy, primarily because of semantic conflict. A latent-source analysis explains this mismatch through source-coherence loss in parallel denoising, where position-wise proposals can combine incompatible visual sources into unsupported answers. We further find that such interference is already visible in the first-step answer-block distribution, making it possible to assess evidence before decoding. To preserve retrieval coverage while limiting harmful visual exposure, we propose the Entropy-Based Candidate Filter (ECF), a training-free evidence-admission framework. To reduce irrelevant content within individual candidates, ECF constructs multi-granularity evidence units; to identify beneficial additional evidence, it uses blank-controlled block confidence and retrieval rank to determine whether and which candidate should enter the final context. Across three multimodal DLMs and five visual QA benchmarks, ECF improves answer accuracy by 2.62 percentage points on average over the strongest fixed top-$k$ input and, with LLaDA2.0-Uni, by 2.37 percentage points on average over the best competing training-free result for each dataset. These results show that broader retrieval benefits visual DLM-RAG through selective evidence admission rather than unconditional evidence expansion. Code is publicly available at this https URL.

---


### 54. [Stable Curves, Unstable Items: Item-Level Scaling Heterogeneity in Video LLMs](https://arxiv.org/abs/2608.07014)

**<font color=#1a73e8>作者：</font>** Wenzhang Sun, Chunfeng Wang, Xiangchen Yin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aggregate scaling curves suggest that Video LLMs improve smoothly or saturate as visual budgets grow. We show that this view can conceal large, opposing changes at the item level. We represent each frozen model--item pair by its response trajectory under controlled visual budgets and derive matched-grid measures of configuration complementarity, harmful transitions, and text overwrite. Across five open Video LLMs from three architecture families, four multiple-choice benchmark splits, open-ended QA and summarization, and fixed-history dialogue generation, no single budget serves all items. On the four-model matched MCQA grid, item-level oracle headroom spans $8.8$--$18.9$ accuracy points and $12.5$--$25.5\%$ of items are correct at a lower budget but wrong at a higher one. Task-appropriate continuous metrics show the same complementarity beyond multiple choice: Token-F1 oracle gaps are $2.7$--$3.7$ score points on MLVU generation and $3.8$--$4.8$ points on AVSD current-turn generation, even when mean quality improves with budget. The effect persists across frame count, spatial resolution, sampling policy, temporal--spatial allocation, and independently executed raw-video and cached pipelines, with per-item rates and membership tracking protocol choices. A controlled sampling intervention recovers $29.0\%$ of terminal regressions, and a structured frame audit identifies several recurring evidence pathways. We release per-item trajectories, protocol provenance, derived annotations, and reproducible analysis code as an auditing artifact. A confidence cascade matches fixed-$128f$ accuracy while reducing average shared frame cost by $31.7\%$, illustrating one operational use of the response matrix.

---


### 55. [ZIPBrain: Can EEG Foundation Models Be Faster, Locally Deployable, but Accurate?](https://arxiv.org/abs/2608.07033)

**<font color=#1a73e8>作者：</font>** Lingwei Li, Yirong Kan, Peng Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This work investigates whether Electroencephalograph (EEG) foundation models (EFMs) can be made faster and locally deployable without sacrificing accuracy. EEG foundation models are a major trend, offering strong general-purpose representations. However, their computational burden grows quadratically with input length, hindering deployment on resource-constrained scenario, particularly for real-time clinical monitoring. EEG's low SNR further suggests many of these tokens are redundant and compressible with little accuracy cost. We propose ZIPBrain, a novel redundancy-aware EEG token pooling module that leverages this low-SNR characteristic to reduce token count. Given a token sequence, ZIPBrain partitions tokens into redundant and unique groups, then merges each redundant token with its most similar counterpart in the unique group. Furthermore, ZIPBrain serves as a training-free, plug-and-play module that seamlessly integrates into standard Transformer encoders with negligible computational overhead. Extensive experiments across multiple EEG foundation models show ZIPBrain's strong versatility, achieving 1.3%-10.5% average improvement over baselines, while reducing wall-clock inference time by 32.7% (up to 41.8% with CUDA Graph) compared to the original EEG foundation models.

---


### 56. [Unsupervised Adaptation of PDE Foundation Models](https://arxiv.org/abs/2608.07053)

**<font color=#1a73e8>作者：</font>** Ziye Song, Zhao Wei, Xin Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pretrained partial differential equation (PDE) foundation models can generalize across different equations, but adapting them to unseen PDE systems typically requires dense solution data, which is often expensive or unavailable. To address this limitation, we propose an unsupervised PDE-based finetuning framework that eliminates the need for ground-truth solutions. We first pretrain a neighborhood attention Transformer on diverse time-dependent PDEs spanning varying spatial scales, yielding transferable representations across heterogeneous equations. In the adaptation stage, we construct a physics-based objective using the PDE residual and boundary conditions, and finetune the model on unseen equations via low-rank adaptation (LoRA). To address the uneven learning across physical quantities in standard LoRA, we introduce NSLoRA, a Newton-Schulz orthogonalized variant that rebalances adaptation. Our method achieves performance comparable to supervised LoRA finetuning without requiring any ground-truth solutions, while consistently outperforming competitive neural operator baselines and recent PDE foundation models across heterogeneous PDE benchmarks spanning multiple spatial dimensions.

---


### 57. [Transformers Struggle to Use Their Emergent World Models: Revisiting the Tower of Hanoi, and the Illusion of Thinking](https://arxiv.org/abs/2608.07077)

**<font color=#1a73e8>作者：</font>** Devin Pereira, Willem Zuidema  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Tower of Hanoi is a simple planning puzzle that in prior work has proven challenging for large reasoning models (LRMs). Current models solve the standard formulation of the puzzle, but still struggle with the flat-to-flat variant (where initial and goal states are not restricted to have all rings on a single peg). This paper presents an in-depth study of how both small, in-house Transformers and large, third-party LRMs solve this task. To understand the failures mechanistically, we first train small Transformers from scratch on precomputed solution traces. Using a variety of interpretability techniques, we show that these Transformers develop an emergent world model: a linearly decodable, geometrically faithful representation of the puzzle's state space (the Sierpinski triangle), that is causally involved in solving the puzzles. Second, we return to the large LLMs and apply our techniques to two frontier reasoning models, Qwen3.6-27B and DeepSeek-R1-Distill-Qwen-32B, that attempt to solve the task through extended chain-of-thought. Surprisingly, we find that both models encode the Sierpinski world model near-perfectly at the end of the prompt, and yet fail at the majority of tasks when there are more than 3 rings. We locate the source of this failure in the decaying representation of the world model. We probe for the representation at different stages during planning, and establish causality by showing that performance can be improved by injecting the prompt-time representation at inference. The failure of the models is thus one of maintenance of the required representations, not their absence, and performance is at least partially recoverable. These results thus reframe the reported collapse in performance from prior work: current Large Reasoning Models build a world model, and then lose it.

---


### 58. [RoRA: Role-Oriented Regional Allocation for Visual Token Pruning in MLLMs](https://arxiv.org/abs/2608.07088)

**<font color=#1a73e8>作者：</font>** Qiyanhui Lu, Han Wu, Rongjian Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) encode images as long visual token sequences, making prefilling and KV-cache storage expensive. Existing training-free pruning methods select tokens by importance, diversity, or spatial coverage, but treat retained tokens as interchangeable and do not explicitly track which object-related regions are already covered. We present RoRA, a training-free framework that casts visual token pruning as role-oriented regional evidence allocation. Given a fixed budget, RoRA partitions tokens into a protected semantic core, complementary context, and fine-grained detail. It first calibrates text-conditioned attention with a positional prior and a prompt-calibrated object prior, then builds Attention-Anchored Regions (AARs) from high-confidence anchors as lightweight proxies for covered object support. Context is explored mainly outside AARs, while a small AAR-guided budget restores local detail; pairwise similarity is used only for context-stage redundancy filtering. Under matched budgets, RoRA consistently outperforms strong training-free baselines across LLaVA and Qwen-VL families, retaining most of the unpruned accuracy even at aggressive pruning ratios, e.g., 96.5% of full performance at 88.9% pruning on LLaVA-1.5, and improving over D2Pruner by about 5% on Qwen3-VL at 75-90% pruning. At a 66.7% pruning ratio, RoRA requires only 0.7 ms for token selection and reduces end-to-end inference time by 24.6%, corresponding to a 1.33x speedup over unpruned inference on an NVIDIA H800.

---


### 59. [Human-Centered Explainable AI for TinyML Edge Devices: A Pareto-Based Selection Framework with LLM-Guided Design](https://arxiv.org/abs/2608.07091)

**<font color=#1a73e8>作者：</font>** Zeinab Dehghani, Dhavalkumar Thakker, Koorosh Aslansefat 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Edge Artificial Intelligence (Edge AI) enables the deployment of AI models directly on local edge devices, while such deployments are subject to strict resource constraints, particularly in clinical applications requiring local and timely inference. In such contexts, explainable artificial intelligence (XAI) can serve as a human-AI interface intended to support healthcare professionals' and patients' understanding of model predictions and informed decision-making. To fulfill this role, XAI method selection for TinyML deployments can be formulated as a human-centered multi-objective design problem that jointly considers qualitative stakeholder preferences, explanation quality, and proxy-based deployment cost. We propose a framework that integrates a large language model (LLM)-guided design interface that maps qualitative stakeholder preferences to candidate XAI methods, followed by deterministic feasibility filtering and Pareto-based optimization. The framework exposes trade-offs among explanation fidelity, stability, and proxy-based deployment cost while characterizing their implications for explanation quality and estimated deployment feasibility. A proof-of-concept evaluation on a skin lesion classification task illustrates how the framework systematically compares candidate XAI methods and identifies Pareto-efficient trade-offs. The present evaluation covers the computational selection stages, while physical MCU deployment and empirical human-expert validation remain outside the scope of this study.

---


### 60. [A MARL Centered Reference Architecture for Large Language Model Augmentation in Smart Manufacturing](https://arxiv.org/abs/2608.07148)

**<font color=#1a73e8>作者：</font>** Fouad Bahrpeyma, Dirk Reichelt  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern manufacturing imposes six coupled demands on adaptive control: local decisions with global consequences, partial observability, nonstationarity, reflex speed response with long horizon effects, delayed and diffuse outcomes, and dynamics that resist explicit modeling. Cooperative multiagent reinforcement learning (MARL), posed as a Dec-POMDP under centralized training with decentralized execution, is a particularly natural formalism for these demands. This paper adopts a MARL centered scope and asks where large language models (LLMs) should augment, interface with, train, or, in the strongest competitive case, replace that coordination core. A taxonomy organizes the literature through four LLM attachment points: policy, reward design, communication between agents, and hierarchical planning. A conditional capability profile separates native mechanism, reported performance, formal guarantee, and engineering maturity, and a deployment readiness analysis identifies the evidence behind each role. These stages yield the principal contribution: a three layer MARL centered reference architecture, grounded in evidence, for semantic reasoning, adaptive cooperative control, and independently assured execution. The LLM-Augmented Dec-POMDP is a descriptive comparative notation for that architecture, recording four attachment choices without introducing a new decision process class or algorithm. Under the reviewed evidence, conventional MARL is better suited to frequent, structured, decentralized coordination after task specific training, whereas LLM components are promising for semantic interpretation, reward drafting, human interaction, and slower supervisory planning. Current LLM only manufacturing controllers do not yet establish equivalence for strict real time, decentralized, safety critical control; this conclusion is bounded by the available evidence and does not assert impossibility.

---


### 61. [Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher Memory](https://arxiv.org/abs/2608.07169)

**<font color=#1a73e8>作者：</font>** Taeil Kim, Kangsan Kim, Sung Ju Hwang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory systems have shown promise for improving agent performance, but their potential remains largely unexplored for small language models, which struggle to generate sufficient successful trajectories on their own. We propose Agent Memory Distillation (AMD), a training-free framework that transfers structured knowledge from a large teacher agent to a small student agent through hierarchical memory. AMD constructs three complementary memory types from successful teacher trajectories: Workflow memory encodes task-level strategies, Subtask memory provides concrete behavioral examples at an intermediate granularity, and Function memory captures per-function calling conventions and common pitfalls. Workflow and Subtask memories are injected proactively at the start of each task, while Function memory is retrieved reactively upon tool-calling errors. We evaluate AMD on three tool-use benchmarks using four student models (4B-8B parameters) with GPT-5-mini as the teacher, achieving average accuracy gains of 27.2%p, 11.2%p, and 3.4%p on AppWorld, BFCL V3, and ToolSandbox, while consistently outperforming existing memory-based baselines. Further analysis shows that Subtask memory contributes the largest gains, teacher effectiveness depends on both teacher capability and student compatibility, and 4B-sized students benefit most from AMD.

---


### 62. [An AI4AI Framework for Visual Token Pruning](https://arxiv.org/abs/2608.07193)

**<font color=#1a73e8>作者：</font>** Zhen Liu, Wenli Huang, Wei Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Visual-token pruning can substantially reduce the inference cost of multimodal large language models (MLLMs), yet existing methods largely rely on fixed, handcrafted heuristics and costly expert trial and error. As pruning objectives, budgets, and model architectures diversify, manually navigating the expanding design space becomes increasingly difficult. This paper aims to build an AI4AI framework for visual-token pruning by addressing a natural question: Can large language models automatically design effective visual-token reduction algorithms? Although LLMs possess broad algorithmic knowledge and strong reasoning capabilities, translating such general knowledge into effective solutions for a specialized task remains nontrivial. We argue that the key lies in designing an appropriate search-state representation that connects the internal knowledge of LLMs with the structural requirements and constraints of visual-token pruning. Based on this insight, we propose AutoPrune, a training-free framework for LLM-driven visual-token pruning policy design. At its core, AutoPrune introduces a Token Pruning Domain-Specific Language (TPDSL) comprising 131 reusable atoms for budget control, token scoring, selection constraints, and token reassembly. A key property of TPDSL is that it represents each search state as a residual modification of a strong base policy. This residual formulation narrows the search space and directs the LLM's attention toward the policy components that are most consequential for performance. Experiments on 14 multimodal benchmarks and three MLLM backbones demonstrate the effectiveness, efficiency, and transferability of AutoPrune. Even when removing 94.4% of visual tokens, AutoPrune preserves more than 99% of full-token performance while reducing FLOPs by 9.9x and prefill latency by 6.4x.

---


### 63. [Authoring and Management of Transparent Research Integrity Assessments of Randomised Clinical Trial Publications Using LLM-assisted Tools and Provenance Knowledge Graphs](https://arxiv.org/abs/2608.07202)

**<font color=#1a73e8>作者：</font>** Milan Markovic, Goutham Indukuri, Somayajulu Sripada 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Systematic reviews of Randomised Controlled Trials (RCTs) are routinely used as evidence for clinical care guidelines. Such evidence has to meet high research integrity standards to prevent low quality or false research outputs influencing the clinical care. However, assessing research integrity of published RCTs is a complex process requiring manual effort, and potentially resulting in diverse opinions of the human assessors. This paper describes INSPECT-AI, an LLM-based interactive tool that assists human reviewers with research integrity assessments of published RCTs based on the community approved INSPECT-SR framework, and the Research Integrity Provenance and Evidence ontology (RIPE-O) for documenting the provenance of the assessment process. In addition, we present the Research Integrity Provenance and Evidence knowledge graph (RIPE-KG), an initial set of 140 expert research integrity assessments of 95 RCT publications generated by INSPECT-AI and described using RIPE-O.

---


### 64. [Measuring Concept Content in Text from LLM Activations: ESG Evidence from Concept Vectors and Linear Probes](https://arxiv.org/abs/2608.07208)

**<font color=#1a73e8>作者：</font>** Luc Hazenoot, Zhaochun Ren, Amirhossein Zohrehvand  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing measures of how much a text is about a concept read the surface of the text: dictionary word shares, topic proportions, embedding similarities. They score the words a text uses, not the judgment a reader forms about it. Recent work has shown that a gap exists in what Large Language Models (LLMs) know internally versus what they express in their response. This paper asks whether that internal knowledge, read by monitoring the activations of frozen, out-of-the-box LLMs, can stand in for task-specific fine-tuning when measuring concept content, and which extraction method reads it best. We extract such measures via the Recursive Feature Machine (RFM) algorithm and via linear probing, and compare these against an embedding baseline, surface baselines, and the same model's own answer to the question. We demonstrate the approach on financial text, a domain studied extensively and served by established annotated resources, using a human-annotated Environmental, Social and Governance (ESG) dataset. The best linear probe comes within 0.6 percentage points of a fine-tuned domain classifier's accuracy without any task-specific fine-tuning, and outscores the same model's own answer to the question in eleven of twelve comparisons, so the activations carry concept content the response does not report. The simple probe consistently beats the RFM concept vectors, which in turn provide what classification alone does not: a continuous score intended to reflect how strongly a concept is present in a text, whose validation awaits graded labels.

---


### 65. [Recipes for Creativity: Iterative Generation and Evaluation in Large Language Models](https://arxiv.org/abs/2608.07243)

**<font color=#1a73e8>作者：</font>** Rens Anderson, Tessa Verhoef, Amirhossein Zohrehvand  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative models are often evaluated through singular artifacts, whereas human creativity typically emerges through iterative generation, appraisal, and refinement. This pilot study examines whether iterative search improves LLM creativity by adapting FunSearch to recipe generation for the 2024 Pillsbury Bake-Off and evaluating outputs against human benchmarks using TTCT-based LLM evaluation. Across two experiments, we test iteration count, generator temperature, and in-loop selection-scorer model size. Results show that iterative generation-selection can produce recipes with creativity scores comparable to human benchmarks, but additional iterations alone do not improve creativity. The in-loop evaluator matters most: a smaller selection scorer yields significantly higher scores across most TTCT dimensions, while temperature has limited effects except for originality. These findings suggest that evaluator design is a first-order design variable in subjective creative search.

---


### 66. [Why Knowing Both Hops Is Not Enough: Understanding Two-Hop Generalization in Language Models](https://arxiv.org/abs/2608.07261)

**<font color=#1a73e8>作者：</font>** Zili Zhang, Yilin Wang, Heng Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can solve complex multi-hop problems yet exhibit puzzling failures on simple two-hop queries: although a model may correctly store each individual hop, it often fails to combine them. To understand the internal mechanisms of this phenomenon, we train transformers from scratch in a controlled symbolic environment. Our experiments reveal a pattern in two-hop generalization: models generalize reliably when the second hop follows the training distribution, but always fail when it deviates.
Through mechanistic analysis, we provide a complete explanation for these distinct generalization behaviors: in settings where models generalize successfully, performance is driven by the emergence of consistent intermediate representations for the same entities across contexts, whereas failures on settings where the second hop is out-of-distribution arise from a mismatch across layers: lower layers correctly construct these intermediate representations, but upper layers, while trained on corresponding atomic facts, primarily learn to map them to outputs rather than to reason over them.
Driven by this insight, we propose a recurrent-style training strategy, which enables transformers to reuse their reasoning circuitry across input forms and substantially improves generalization on out-of-distribution two-hop queries.

---


### 67. [Grammar Engineering Meets LLMs: Development of Cantonese and Irish ParGram Treebanks](https://arxiv.org/abs/2608.07283)

**<font color=#1a73e8>作者：</font>** Chit-Fung Lam, Elaine Uí Dhonnchadha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Grammar engineering requires expertise in linguistic formalism and computational implementation, especially in parallel grammar projects that balance cross-linguistic consistency with language-specific properties. This paper presents the development of Cantonese and Irish treebanks within the Parallel Grammar (ParGram) Project, where linguistic parallelism is maintained at an abstract functional level. We also investigate the methodological potential and limitations of using multilingual LLMs to support grammar engineering, focusing on Cantonese-Irish translation and the generation of formal syntactic structures using OpenAI's gpt-oss-120b model. The results show that translation performance was generally unsatisfactory and unaffected by prompt language. For syntactic structure generation, the model produced some structurally meaningful outputs, but performed poorly on tasks requiring cross-linguistic abstraction. Nonetheless, LLM-generated outputs may still offer some reference value by suggesting alternative analyses and (partially) capturing predicate-argument relations. Overall, our findings highlight both the potential and limitations of using LLMs in collaborative grammar engineering, while underscoring the continued importance of expert-driven analysis and verification.

---


### 68. [Foundation Models Adaptation for Multi-View Multi-modal Cardiac MRI Segmentation and Direct Ejection Fraction Estimation](https://arxiv.org/abs/2608.07291)

**<font color=#1a73e8>作者：</font>** Sina Amirrajab, Cian M Scannell, Volker Vehof 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models have shown strong transferability in cardiac MRI (CMR), but their effectiveness for heterogeneous multi-view and multi-sequence CMR analysis remains unclear. In this work, we explore the effectiveness of fine-tuning and combining different CMR foundation models for the Universal Multi-Sequence, Multi-Center and Multi-View CMR Segmentation (CMR-Multi) Challenge. CineMA was fine-tuned for cine and late gadolinium enhancement (LGE) segmentation across short-axis and long-axis views. For direct left-ventricular ejection fraction (LVEF) estimation, we used two recent frozen CMR foundation models to extract embedding vectors that were then combined using attention-based multiple-instance learning for LVEF regression. In the challenge validation set, cine segmentation achieved Dice scores of 0.862, 0.883, and 0.902 for short-axis, two-chamber and four-chamber cine MRI, respectively. LGE segmentation achieved Dice scores between 0.621 and 0.846 across views. The direct LVEF regression model achieved an MAE of 4.96 percentage points and a Pearson correlation of 0.91. These results indicate that foundation models can be effectively adapted and combined for multi-view CMR analysis, while accurate LGE scar segmentation remains a challenging task.

---


### 69. [Same Attention, Different Truths: Put Logit-Lens over Visual Attention to Detect and Mitigate LVLM Object Hallucination](https://arxiv.org/abs/2608.07302)

**<font color=#1a73e8>作者：</font>** Zichuan Wang, Songlin Yang, Bo Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) often suffer from object hallucination, generating objects that are absent from the image. Prior work largely attributes this to insufficient visual attention. However, we find that both real and hallucinated objects receive equally strong visual attention in the model's mid-to-late layers, suggesting that the key issue may not be how much the model attends, but what it attends to and why. To this end, we decode the visual features of high-attention regions using Logit Lens, and observe that regions corresponding to real objects can be correctly decoded to the target object tokens, whereas those for hallucinated objects cannot. Building on this, we identify two hallucination mechanisms: (i) visual uncertainty, triggered by semantically similar or confusable regions; masking these regions eliminates the hallucination. (ii) contextual prior, triggered by strong co-occurrence priors; even when the initially attended region is masked, the hallucination persists and attention drifts to other regions. Based on these findings, we propose a simple yet effective training-free Detect-Mitigate framework comprising a Logit-Lens Consistency Check to detect hallucination and targeted remedies: High-Attention Regions Masking (HARM) for visual uncertainty hallucination, and Visual Evidence Enhanced Decoding (VEED) for contextual prior hallucination. Our approach achieves state-of-the-art results on multiple hallucination benchmarks. Code will be available.

---


### 70. [Geo-Spatial Concept Probing of Large Language Models: Abstraction, Compositionality, and Grounding](https://arxiv.org/abs/2608.07353)

**<font color=#1a73e8>作者：</font>** Karim Radouane, Jose G Moreno, Lynda Tamine  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding concepts is fundamental to generalization. Despite their impressive performance on a wide range of tasks, Large Language Models (LLMs) still struggle with genuine concept understanding. Prior work has evaluated conceptual understanding in LLMs using natural-language benchmarks or narrowly scoped synthetic tasks, but these settings often conflate multiple skills or lack precise control over the underlying concepts and their properties. To support controlled probing of concepts in LLMs, we design tests on their core properties: abstraction, compositionality, and groundness. We set up a concept-centric benchmark, targeting spatial concepts such as direction, distance, topology, and their compositions, and use question answering tasks serving as a proxy. We conduct extensive experiments across multiple LLM architectures and training regimes to analyze how model scale and design impact conceptual understanding. The results reveal clear limitations in current LLMs and provide insights into the factors shaping their ability to acquire and compose structured concepts. Our findings shed light on how concept-based LLMs can be redesigned for improved information access and knowledge management. The code will be available at this https URL.

---


### 71. [People Are Not Just Their Countries. Disentangling Social Determinants of LLM Value Alignment Across Europe](https://arxiv.org/abs/2608.07367)

**<font color=#1a73e8>作者：</font>** Maria-Louisa Wightman, Guillaume Bied, Tijl De Bie  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) are increasingly used as a primary source of information and advice, understanding their alignment to humans in terms of values becomes a pressing concern. A growing literature has leveraged large scale surveys to investigate to what extent LLMs' and humans' stated values and opinions align. With limited exceptions, studied populations have been defined country borders or cultural bounds. Yet, this focus neglects the role that socio-demographic divides may play for value alignment disparities.
Relying on the European Social Survey, we address this knowledge gap by considering value alignment displayed with respect to 10 prominent commercial LLMs in terms of 15 socio-demographic variables as well as country of residence. Our analyses reveal that LLMs are indeed unequally aligned to the values of different socio-demographic groups, notably those defined by education, income, occupation and religion. When examining alignment at the individual level, a respondent's country, taken as a stand-alone variable, explains a substantial amount of variation that is on par with the full set of considered socio-demographics. Further disentangling the respective role of country-level and socio-demographic factors, we find they are complementary in explaining value alignment patterns, with their relative weights varying across the subset of questions considered.

---


### 72. [GeoBenchLLM: A Comprehensive Benchmark for Evaluating LLMs on Geo-Related Tasks](https://arxiv.org/abs/2608.07411)

**<font color=#1a73e8>作者：</font>** Rodrigo Ferreira Rodrigues, Karim Radouane, Jose G Moreno 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In the context of geodata, existing Large Language Models have often been studied in a homogeneous setting, which has considerably limited insights into their generalization capabilities. In this paper, we present \benchName, a comprehensive benchmark for probing LLMs on geo-related tasks. We leverage a careful selection of twelve publicly available datasets from diverse geo-related tasks and domains, and evaluate a set of LLMs on geo-spatial and temporal understanding using our benchmark. Our results show that reasoning and size have a strong impact on overall performance. GeoBenchLLM is publicly available at this https URL.

---


### 73. [Beyond Post-Hoc Temperature Scaling: Bilevel Optimization for LLM Calibration](https://arxiv.org/abs/2608.07419)

**<font color=#1a73e8>作者：</font>** Ruochen Jin, Zhanliang Wang, Zongyu Dai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Preference alignment often makes large language models (LLMs) overconfident and poorly calibrated. Traditional post-hoc temperature scaling is inherently domain-dependent: a temperature fitted on one domain does not generalize across domains. This motivates us to modify model parameters during training to improve calibration. We propose maximizing the entropy of predictive distributions as the calibration objective, which directly targets overconfidence by discouraging overly concentrated predictions. Inspired by temperature scaling, we realize this through a bilevel optimization formulation, where the lower level trains the model under a parametric loss and the upper level selects loss hyperparameters to maximize entropy. To make the framework practical at LLM scale, we adopt an efficient first-order approximation that avoids explicit second-order computation. Across both multiple-choice and open-ended generative question answering, experiments demonstrate that our method yields well-calibrated LLMs with particular advantages in out-of-domain generalization.

---


### 74. [A Picture is Worth a Thousand Tokens: How Vision Language Models Cut AI Energy Costs While Improving Accuracy](https://arxiv.org/abs/2608.07427)

**<font color=#1a73e8>作者：</font>** Bhavika Jalli, Nikhil Korati Prasanna, Jayanta Choudhury  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM inference accounts for over 90% of AI operational energy, scaling directly with input token count---a critical inefficiency for telecom network analytics and numerical time-series data analysis (NTSDA), where raw multivariate KPI windows from 4G/5G cell sites expand into thousands of floating-point tokens. Vision-Language Models (VLMs) eliminate this mismatch by encoding time-series as 2D plots, achieving 3.6-10.4x input token reduction across Llama-3.2-90B, Qwen2.5-VL-72B, and Pixtral-12B architectures. This translates to 1.8-2.5x measured inference energy reduction, saving approximately 7.2 MJ/day at telecom edge deployments and CloudRAN that monitor 200 cells per 15-minute interval. Critically, efficiency gains do not sacrifice accuracy: a fine-tuned Llama-3.2-90B-Vision VLM achieves 220.7% higher precision than its text-only counterpart and outperforms LSTM and ARIMA baselines by over 144% on telecom anomaly detection. On public benchmarks, Pixtral-12B achieves a 20.6x improvement in J/F1 score at mean F1 = 0.82. At 24 KPIs, text representations exceed the 128K context window of most production LLMs, rendering text-only processing infeasible without truncation, while visual representations remain within standard limits. These results establish VLMs as an energy-efficient and accuracy-superior modality for numerical time-series workloads, providing empirical grounding for AI inference systems that treat energy consumption as a first-class engineering constraint.

---


### 75. [TEPA: Revoking Stale Memories for Conflict-Robust Language Agents](https://arxiv.org/abs/2608.07429)

**<font color=#1a73e8>作者：</font>** Yan Zhou, Yue Ouyang, Kaiyang Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term memory enables language agents to reuse past facts, preferences, and task experience. Persistence also creates a central falsifiability problem: when the world changes, stale memories can remain retrievable and pollute the prompt. We characterize this failure mode as memory pollution: degradation caused by active memories that newer conflicting evidence has superseded. We introduce TEPA, a revocable evidence-memory mechanism that makes validity an explicit state of memory. TEPA represents observations as keyed precedents and revokes active precedents when fresh evidence contradicts them under the same key, allowing retrieval to draw from current evidence while preserving revoked history for audit. Across controlled hidden-regime drift, real file-backed executable drift, and preference-update streams, revocation prevents stale active memory from remaining in the retrieval set after reversal. In controlled drift over 50 seeds, append-only and last-write-wins memory fell below no memory during full reversal (append-only and last-write-wins both 0.210, no memory 0.309, TEPA 0.950), and the same pattern reproduced under real file execution (append-only 0.203, no memory 0.298, TEPA 0.950). On clean MemoryAgentBench SH-6k, TEPA matches a strong last-write-wins cache, confirming that current-key replacement is the decisive operation for single-hop fact consolidation. Boundary tests on multi-hop and very long-context MemoryAgentBench settings expose retrieval-chain and context-selection bottlenecks beyond fact-level validity tracking. Together, these results establish lifecycle revocation as a core memory operation for agents that must falsify, audit, and later re-promote evolving knowledge.

---


### 76. [Fisher-R1: Training LLM Agents for Reliable Hypothesis Testing](https://arxiv.org/abs/2608.07437)

**<font color=#1a73e8>作者：</font>** Jiacheng Miao, Jin Mu, Guanhua Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable hypothesis testing is the foundation of many empirical scientific claims. Large language model (LLM) agents are increasingly used to automate this process, as they can inspect datasets, generate code, and produce analyses end-to-end. However, we show that they frequently make subtle inferential errors that lead to incorrect conclusions despite correctly executed analyses. Existing benchmarks fail to capture this failure mode, as they rarely assess whether a reported p-value is statistically valid given the assumptions underlying the data. We address this gap by building P-Bench, a benchmark comprising 425 open-ended, realistic hypothesis-testing tasks spanning economics, biology, and medicine. Each task requires an agent to select a statistical method, compute a p-value, and draw a conclusion given only a scientific hypothesis and a dataset. We further introduce Fisher-R1, an open-weight LLM agent trained for rigorous hypothesis testing using synthetic tasks and reinforcement learning. On P-Bench, Fisher-R1-14B substantially improves over its backbone and outperforms strong proprietary and open-source baselines, including GPT-5.4 and DeepSeekV4-Pro, achieving a 21% average relative improvement in single-trial success over DeepSeek-V4-Pro, with gains up to 26% on the most challenging tasks. Our results demonstrate that current LLM agents lack reliable statistical reasoning for hypothesis testing and that reinforcement learning on tasks with verified statistical reward substantially improves reliability.

---


### 77. [PsychoAgent: An Affect-Sensitive Cognitive Architecture for Conflict-Aware Memory in LLM Agents](https://arxiv.org/abs/2608.07438)

**<font color=#1a73e8>作者：</font>** Mohammad Amanlou, Parham Abed Azad, Farbod Davoodi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human-like cognition does not select past experience by topical similarity alone: affective significance and unresolved conflict also shape what becomes accessible. We present PsychoAgent, a cognitive architecture for LLM agents that separates factual and affective memory and integrates both through a conflict-aware executive controller. Affective memories are first filtered by semantic relevance and then re-ranked by salience, preserving topical fit while allowing emotionally important traces to enter the prompt. Across three controlled conflict scenarios, the full architecture retrieved more conflict-critical memories than semantic-affective and single-memory RAG baselines (0.933 vs. 0.500 and 0.667), with a small semantic-similarity cost. Five blinded raters evaluated 27 outputs. After within-rater standardization, the full architecture had the highest overall mean (+0.22 SD), but corrected pairwise differences were not significant. A three-day illustrative trace further shows persistent affect, offline memory recombination, and selective memory reweighting. The findings support affect-sensitive retrieval as an inspectable mechanism for modeling human-like conflict effects in LLM agents.

---


### 78. [An Exploratory Evaluation of LLM-Assisted Rewriting of Moderate-Complexity Financial Sentences for DisCoCat-Based Sentiment Analysis](https://arxiv.org/abs/2608.07439)

**<font color=#1a73e8>作者：</font>** Brian Llinas, Nikos Chrisochoides  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Quantum natural language processing (QNLP) provides a grammar-aware framework for text modeling, and Distributional Compositional Categorical (DisCoCat) is one of its theoretically grounded formulations. Prior work on financial sentiment analysis has identified practical limitations of DisCoCat, including parser sensitivity, high simulation cost, and difficulty handling longer sentences. We study an LLM-assisted preprocessing workflow that uses controlled rewriting to compress, simplify, or decompose moderate-complexity financial sentiment sentences into parser-compatible, circuit-efficient variants while preserving sentiment-bearing meaning. We compare prompting strategies, language models, and filtering configurations with the low-complexity-only DisCoCat baseline of Stein et al. At the circuit level, the strongest compression variants reduce average qubit and gate counts by more than 70 percent relative to the raw moderate-complexity subset. Across repeated training runs, GPT-4.1-mini with Prompt B achieves the highest observed mean accuracy, $0.550 \pm 0.035$, compared with $0.521 \pm 0.050$ for the baseline. Larger training splits do not necessarily improve downstream performance; across evaluated configurations, training-split size has a moderately negative association with accuracy (Pearson $r=-0.446$). These results provide exploratory evidence that LLM-assisted rewriting can make some moderate-complexity inputs usable within the evaluated DisCoCat configuration, while highlighting prompt design, filtering, and circuit-aware preprocessing as considerations for more scalable QNLP-based financial sentiment analysis.

---


### 79. [CreativeInstruct: Scalably Teaching LLMs to Balance Quality, Creativity, and Diversity](https://arxiv.org/abs/2608.07460)

**<font color=#1a73e8>作者：</font>** Ananya Sahu, Mohit Bansal, Elias Stengel-Eskin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While post-training improves the capabilities of large language models (LLMs), it generally lowers their output diversity and creativity, negatively impacting tasks that explicitly require creativity (e.g., story generation) as well as those that require it implicitly, e.g., reinforcement learning (RL). We instead propose CreativeInstruct, a scalable instruction-tuning method that teaches LLMs to balance creative, base-model-like generations with the quality of post-trained models, by learning to inject special [StartCreativity] spans that bias generation toward creativity. Furthermore, we introduce a structural diversity metric based on graph edit distance, which captures narrative level variation missed by purely lexical and semantic metrics. On narrative generation, CreativeInstruct matches or exceeds the diversity of both multi-model baselines and distilled variants of their outputs, without sacrificing quality or requiring multiple models at inference time. These results are mirrored in our human evaluation, where we find that annotators rate CreativeInstruct generations as more creative than the post-trained LLMs' generations in 70.3% of cases. We also show the benefits of creative models as a substrate for RL: GRPO applied to a CreativeInstruct checkpoint improves by ~4% on AMC and ~5% points on MATH over the same training applied to the post-trained checkpoint.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 80. [Separating Decision-Rule Misalignment from Readout-Coverage Limitations in Speech Language Models](https://arxiv.org/abs/2608.06409)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Linkai Peng, Baorian Nuchged  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech language models are increasingly evaluated on paralinguistic tasks by the accuracy of prompted answers, but answer accuracy combines failures at different stages of the audio-to-answer computation. We introduce a generation-aligned diagnostic ladder that compares the emitted answer, the option logits, an affine readout of those logits, and a linear readout of the hidden state at the same answer token. Successive differences separate endpoint, decision-rule, and readout-coverage gaps. Across five systems and two emotion corpora, state decoding exceeds generation by 27.8 accuracy points on average, and both the decision-rule and readout-coverage gaps are positive in all ten conditions. A label-free logit correction improves generated accuracy in every condition, showing that part of the decision-rule gap is actionable. In rank-matched comparisons, emotion information outside the native readout generalizes to held-out speakers and survives controls for measured acoustic descriptors, but replacing the selected readout-external directions usually has little effect on emitted answers. These results distinguish information availability from behavioral use and localize performance losses across the decision rule and the state-to-answer readout.

---


### 81. [Latent Fact-Checking: Detecting Misinformation through Activation Engineering](https://arxiv.org/abs/2608.06417)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Pedro Barcelos, Otávio Parraga, Marcelo M. Mussi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The proliferation of misinformation online has driven demand for scalable detection systems. While most existing approaches rely on surface-level linguistic features or external knowledge retrieval, we examine truthfulness as a geometric property of a language model's representation space. We introduce a misinformation detection framework grounded in activation engineering, which leverages the latent geometry of transformer models. Our approach elicits a misinformation direction in the residual stream by contrasting activations from paired truthful and false statements, following the difference-in-means principle of Contrastive Activation Addition (CAA). At inference time, the last-token activation of an unseen claim is projected onto this direction, and the projected representation is fed to an Multilayer Perceptron (MLP) for classification. The procedure requires no fine-tuning of the backbone model, no external evidence retrieval, and no task-specific supervision beyond the contrastive pairs used to estimate the direction. We evaluate the method across 11 models from the Gemma, Llama, and Qwen families, ranging from 270M to 12B parameters, on three fact-checking benchmarks: AVeriTeC, LIAR, and FACTors. The falsehood direction is recoverable across model scales and architectural families, and last-token projection matches or surpasses zero-shot and few-shot prompting baselines on LIAR and FACTors, with the largest gains observed for smaller models. Performance on AVeriTeC is more limited, which we attribute to its evidence-grounded labeling scheme. These findings provide evidence that truthfulness is a structured, linearly separable concept in the latent space of pretrained language models, and point toward interpretability-driven misinformation detection as a practical complement to retrieval-based pipelines. The code is available on this https URL.

---


### 82. [NTDH: Complex Reasoning for Comprehensive Affective Analysis](https://arxiv.org/abs/2608.06425)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Tianlei Zhu, Zhiwei Liu, Yuyan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Comprehensive affective analysis is challenging for two reasons: it spans heterogeneous prediction tasks with continuous, ordinal, and multi-label outputs, and affective meaning is context-dependent, requiring conflicting cues to be reconciled rather than mapped directly to labels. Existing methods learn this mapping directly and do not model the reconciliation explicitly. We recast the task as a complex-reasoning problem, which yields one output interface across heterogeneous label spaces and a trajectory over which a verifiable reward can be optimised; to our knowledge, this is the first such treatment covering both sentiment and emotion. The obstacle is on the data side: affective reasoning traces must be synthesised, and generic synthesis is misaligned with the targets, tolerances, and phenomena of affect, and discards or leaks its failure cases. We propose NTDH, which addresses these four failures. Naturalisation sets the training answer to the gold label, so it is correct by construction. A Tolerance-aware gate checks each answer against the task's own scoring margin. Domain-aware strategies refine the reasoning using ideas from affective science. Directional Hints report only the type and direction of an error, without exposing the target. We train Qwen3-8B with SFT and then GRPO under the same tolerance used for verification (up to a more permissive construction gate on the multi-label subtask), and a component ablation quantifies the data-quality effect of each part. Using 16,302 training records, about 14x fewer than comparable instruction-tuned systems, the final policy improves over its SFT checkpoint on five of six official-test metrics and achieves the strongest EI-reg result among the compared systems, at a Pearson correlation of 0.862.

---


### 83. [Test-Time Adaptation with Online Personalized Energy-Based Cache for Fine-Grained Video Expression Recognition](https://arxiv.org/abs/2608.06467)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Masoumeh Sharafi, Muhammad Osama Zeeshan, Soufiane Belharbi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial expression recognition (FER) in videos is challenging because models must identify subtle, temporally evolving affective states that vary across individuals. Although vision-language models provide transferable visual-semantic representations, models trained on subject-independent data often degrade under subject-specific distribution shifts at inference time. Existing test-time adaptation (TTA) methods commonly update model parameters during inference, increasing computational cost and latency. Cache-based methods avoid parameter updates, but they usually require enough target samples to form reliable class prototypes, which is difficult early in adaptation and for rarely observed classes. We introduce Energy-Based Cache Personalization (EB-CaP), a subject-based online TTA method for video FER that generates class-specific prototypes personalized to each target video. EB-CaP uses a lightweight energy-based model to sample prototypes from the current unlabeled video and populate a personalized cache online, without accumulating large amounts of target data or storing diverse source prototypes. Its energy function relies only on pretrained CLIP: similarities between the target video embedding and class text embeddings guide prototype sampling. In parallel, positive and negative caches store reliable and uncertain target embeddings. An adaptive entropy gate controls cache updates according to the evolving confidence distribution, while a diversity gate limits redundant samples. Final predictions combine cache-derived scores with the current CLIP scores. Experiments on BioVid, StressID, and BAH show that EB-CaP outperforms state-of-the-art TTA methods while maintaining low computational and memory overhead. Code is available at this https URL.

---


### 84. [ConstructCIE: A Dataset for Extracting Causal Information from Construction Accident Narratives](https://arxiv.org/abs/2608.06495)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hung Nguyen, Jaehoon Lee, Namgyun Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Construction accident narratives contain rich causal information, but the evidence is often implicit, long-span, and distributed. We introduce ConstructCIE, a manually annotated dataset for Causal Information Extraction from OSHA construction accident reports. The dataset uses a hierarchical schema for accident types, causal factors, sub-causal factors, and supporting evidence spans. We evaluate supervised sequence taggers and instruction-tuned LLMs in an end-to-end hierarchical extraction setting. Results show that most evaluated models achieve strong accident-type prediction and recover broad causal meaning but remain limited in precise span-level extraction. JHE generally achieves stronger exact and soft matching, while IHE sometimes achieves higher keyword F1. Error distributions vary by extraction strategy, but evidence-selection and span-boundary errors remain common. These findings show that reliable Causal Information Extraction for construction accidents requires stronger domain grounding and more accurate evidence extraction.

---


### 85. [Don't `Well, Actually' Me Unless You Know What You're Talking About: Weak Presupposition Verification Degrades General QA Performance](https://arxiv.org/abs/2608.06539)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shenran Wang, Vered Shwartz, Hila Gonen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> False-presupposition QA (FPQA) tests LLMs on their ability to identify false presuppositions in questions and abstain or correct them rather than reinforcing false assumptions. The common approach reduces the task to prompting LLMs to extract presuppositions and fact checking each presupposition. While the performance on dedicated benchmarks keeps improving, evaluation largely focuses on questions with false presuppositions (FPQs) while ignoring the performance on ``normal'' questions (TPQs). Since many benchmarks over-represent FPQs compared to their natural occurrence, the result is that performance on these benchmarks doesn't reflect real-world QA performance. Through extensive experiments across various model families, sizes, and benchmarks, we show that methods that perform better on FPQs tend to perform worse on TPQs. Our analysis reveals this is the result of weak fact checking modules that reject also true presuppositions. We hope our findings will help guide future work toward FPQA methods that generalize well to realistic settings.

---


### 86. [TradeVerse: A Longitudinal Benchmark of Political Negotiation in International Trade](https://arxiv.org/abs/2608.06549)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Debodeep Banerjee, Amitangshu Dasgupta  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly being applied to tasks involving institutional and political texts, but existing benchmarks evaluate them on isolated documents or single tasks. In realpolitik, negotiations are longitudinal data, where participating parties can align or argue over multiple iterations and each turn is an outcome of the previous turns, hence, understanding one turn requires tracking everything before it. We introduce TradeVerse, a benchmark built from the World Trade Organisation (WTO) specific trade concerns, where member states challenge one another and exchange arguments over multiple rounds, sometimes for years. We, in TradeVerse, reconstruct minutes of $1170$ meetings, spanning across 5 groups and $89$ product groups and define three tasks: first, the system has to analyze the longitudinal meeting records and predict the harmonized system codes (HS chapters) of the products under discussion in the particular meeting, second, we examine whether the system, upon analyzing the anonymized content of the meeting, can guess the name of the responding country and third, we ask the system to play the role of the responding country and provide the statement for the very last round. All labels are recovered directly from the proceedings, requiring no manual annotation. Our experiments highlight the challenges these tasks pose for current LLMs. To the best of our knowledge, TradeVerseis the first benchmark to investigate potential of LLMs in understanding longitudinal political trade negotiations.

---


### 87. [Quantization Damage Is Multiplicative, Not Additive](https://arxiv.org/abs/2608.06564)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zekun Wu, Swati Dhiman, Adriano Koshiyama  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantization is how large language models are actually deployed, and below four bits it is known to hurt. What nobody can say is which of the model's decisions will change at a given bit-width. The damage is silent: a compressed agent stops calling its tools, then loses half its safety refusals, yet benchmark scores barely move. Prior work assumes quantization adds noise of a roughly fixed size, which would make confident decisions safe. We measure the decision itself instead. The margin of a two-way decision is the model's score for the option it picks minus the score of its best alternative; we track it before and after quantization across 16 models from 8 model families, three quantization methods, and bit-widths from 8 down to 2. Quantization does not add fixed-size noise to the margin. It multiplies the margin by a factor that collapses with bit-width (median 0.86 at 4 bits, 0.33 at 3, 0.00 at 2); we call this margin shrinkage. This contraction reduces the protection a large margin affords; the model's own small biases pick the direction of failure: at 3 bits the decision to call a tool collapses toward inaction while the choice of which tool is untouched. In fitted statistical comparison, additive-noise accounts never win on the damaged tool and safety decisions. The fitted relation predicts flip rates within a median of 1.8 percentage points on held-out decisions, though no flip was used in the fit; per decision, the predicted flip probabilities are calibrated uncertainty estimates (expected calibration error 0.004 over 131,758 predictions). The same form holds in every model we measure, but the constants are each model's own and do not transfer. A small paired margin set, measured per model and bit-width, estimates which decisions break without full generative evaluation; under our cost-matched tests, nothing repairs damage more cheaply than one more bit.

---


### 88. [Model Confidence Under Answer-Preserving Attacks: An Informativeness-Manipulability Frontier](https://arxiv.org/abs/2608.06571)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Reza Khanmohammadi, Ivan Brugere, Simerjot Kaur 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deployed vision-language systems often gate their answers on confidence, making confidence robustness relevant to oversight. We study confidence readouts under white-box, image-only attacks constrained to preserve the generated answer byte-identically. Under a reachability assumption, an unmovable readout cannot outperform the answer-string accuracy prior, whose pooled value is 0.617. Independently of that assumption, a uniform amplitude certificate below a measurable threshold guarantees adversarial discrimination above the same floor. Across four vision-language models, three visual question answering benchmarks, five deployed confidence channels and two defense estimators, direct or surrogate-aimed attacks produce itemwise feasible perturbations that refute this uniform certificate in all 84 estimator-by-cell combinations. Coordinated correctness-label-aware attacks drive adversarial discrimination to or below the answer-string floor in all sixty deployed-channel cells, including all fifty-nine that begin above it. Hidden-state interventions and an open-ended text-model activation-space replication show that comparable confidence movement can be induced at the representation level rather than only through adversarial images. None of four tested defense families establishes a robust alternative under the specific evaluation applied to it. In a confidence-gated simulation, a coordinated token-probability attack transferred to a hidden-state gate causes up to 84.8% of previously rejected wrong answers to become accepted. After reweighting to each benchmark's natural correctness prevalence, accepted accuracy falls below the no-gate baseline in eight of twelve cells under transfer and all twelve under a direct gate-aimed attack. Under the studied threat model and budget, confidence is therefore an integrity-sensitive rather than intrinsically robust oversight signal.

---


### 89. [NxN E-valuation: Hypothesis Certification via a Conformal CRT Null](https://arxiv.org/abs/2608.06621)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Bin Wang, Yan Zhong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose NxN E-valuation, a handy, e-value-based hypothesis-certification algorithm that lets a hypothesis be verified without building any case-specific certification procedure---such as constructing a dedicated null hypothesis---as long as a large enough dataset is available. The method is especially suited to LLM-based exploration systems, where LLMs are remarkably good at proposing hypotheses but suffer badly from hallucination; this hallucination prevents us from harvesting LLM outputs directly, and existing remedies each fall short. The most common solutions include letting the LLM verify or correct itself circular verification and held-out testing (where false hypotheses can still pass via spurious correlations), among other remedies detailed in the introduction. To resolve this, NxN E-valuation exploits the naturally existing large training set and lets different samples serve as null hypotheses for one another. This design directly realizes a conditional randomization test (CRT) that certifies each hypothesis. The approach can be a universally better replacement for at least LLM circular verification and held-out-data testing, provided the LLM's generations are hypotheses that apply to each individual sample.

---


### 90. [Cryptanalytic Extraction of Isolated Bias-Free GLU Feed-Forward Blocks by Antipodal Separation](https://arxiv.org/abs/2608.06631)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Chunhui Shi, Xinwen Fu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cryptanalytic extraction has been demonstrated for ReLU networks, for networks using componentwise activations such as GELU or SiLU, and for a Transformer's final projection matrix. These methods do not recover the bias-free Gated Linear Unit (GLU) feed-forward blocks used in many modern language models. Such a block multiplies an activated linear projection by a second learned linear projection within each hidden unit, a two-branch structure absent from the network classes and final-layer setting addressed by those methods. We give a constructive, multi-stage forward-query recovery primitive for isolated bias-free GLU blocks. Finite-difference curvature supplies gate-direction candidates, and paired observations at x and -x separate gate magnitude, orientation, and value-branch coupling. Across high-precision targets, six Qwen layers, an 8,192-unit Llama subproblem, and a full-dimensional Gemma block all reach sub-percent median validation error. Four finite-precision configurations remain below 5 percent median error, but none reproduces every stored weight. These isolated-block experiments are not an end-to-end model-API attack: deriving the required internal block responses from final model outputs remains unsolved.

---


### 91. [When Semantics Saturate or Emerge: Adaptation-Conditional Semantic Utility in Source-Free Cross-Domain Few-Shot Learning](https://arxiv.org/abs/2608.06673)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Wei Liu, Xing Deng, Haijian Shao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language descriptions in source-free cross-domain few-shot learning (SF-CDFSL) are often selected according to zero-shot accuracy obtained with a frozen vision--language model. This paper asks whether that ranking remains valid after target-domain visual adaptation. Under a strictly paired protocol, we compare a generic class-name template with fixed detailed class descriptions before and after visual Low-Rank Adaptation (LoRA) on EuroSAT, CropDisease, ISIC, and ChestX. Let $\deltazero$ and $\deltalora$ denote the Detailed-minus-Base accuracy before and after adaptation, respectively. Two recurring regimes emerge. In \emph{semantic saturation}, $\deltazero>0$ but $0<\deltalora\ll\deltazero$: on EuroSAT and CropDisease, initial gains of 8.13--21.54 percentage points contract to 0.69--2.96 points after LoRA. In \emph{semantic emergence}, $\deltazero\leq0$ but $\deltalora>0$: on ISIC and ChestX, detailed descriptions become more useful only after the visual representation is updated. Training trajectories and sample-level decomposition show that saturation is driven mainly by Base-LoRA recovering errors already solved by detailed semantics, whereas emergence is associated with prediction turnover and newly formed Detailed-only correct decisions. Fixed-point-free shuffled-semantic controls, a second CLIP backbone, and multiple random seeds support the broad pattern while identifying ChestX 1-shot as a weak boundary case. These findings establish that zero-shot prompt quality is an incomplete proxy for adaptation-anchor quality and motivate evaluating language on both sides of the adaptation boundary.

---


### 92. [Policy-Masked Private Experts: Auditable and Reversible Capability Access Control in Sparse MoE Models](https://arxiv.org/abs/2608.06690)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhuoheng Huang, Mukesh Singh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Most language-model access controls regulate behavior while leaving the same computation available to every request. We study a different systems question: can trusted authorization determine which newly trained parameters are reachable by the forward pass? Policy-Masked Private Experts freezes a pretrained sparse Mixture-of-Experts (MoE) model, trains a disjoint expert branch, and selects the public or private pool before top-k routing. The resulting claim is narrow but testable: under the declared trusted computing base (TCB), an unauthorized request executes no private expert. It does not imply that the public model lacks the same semantic capability.
We test this separation between execution control and task utility in Qwen3-30B-A3B and DeepSeek-V2-Lite. Three Qwen BF16 seeds update all 32 private experts while the public fingerprint remains unchanged. Across 64 adversarial scenarios and 96 deny/fail-closed events, unauthorized private execution is zero; independent hooks exactly match 11,616 routed private rows and allow-deny-allow recovery is exact. On two prospectively frozen Qwen benchmarks, the private branch improves exact tool use by 5.0 percentage points (pp) (five versus zero discordances; one-sided Holm p = 0.03125, corresponding two-sided exact p = 0.0625) and 21.3 pp (percentile-bootstrap 95% CI [13.3, 29.3], Holm p = 0.000031). Three arm-blinded model evaluators retain a positive external effect of 18.7 pp (95% CI [9.3, 28.0]). A parameter-matched Lora has similar external utility, but a post-hoc request gate leaves 1,225 adapter calls under deny; the disjoint expert branch leaves none. DeepSeek reproduces the route invariant and gains 27.0 pp. A valid sealed evaluation is near-neutral. These results support auditable, reversible control over a trained parameter path, while showing that useful transfer remains distribution dependent.

---


### 93. [A Multi-Agent Framework for Automated Coarse-Grained Molecular Dynamics of Polymers](https://arxiv.org/abs/2608.06694)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Joohee Choi, Junhyeong Lee, Seunghwa Ryu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coarse-grained (CG) molecular dynamics extends polymer simulation beyond the scales accessible to all-atom (AA) methods, but bottom-up CG modeling is laborious. The CG resolution is a design choice, so a transferable parameter set is generally not available and the potentials are derived anew for each polymer mapping. Here we present CGMas, a multi-agent framework that automates topology construction, equilibration, mapping, potential derivation, and validation from a natural-language specification of the polymer and target resolution. A large-language-model (LLM) reasoning agent infers the AA topology from polymer name, while layered self-correction resolves physical errors common to unsaturated, heteroatom-containing, and polar polymers. Downstream agents equilibrate the system, map it onto CG representation, derive potentials through Boltzmann inversion, and benchmark the model against its atomistic reference. CGMas completed all 27 homopolymer and copolymer tasks, matched the AA density to within 5% in 22, and reduced simulation from 38-88 min to 1 min, establishing agentic LLMs as a route to automated polymer coarse-graining.

---


### 94. [MolBioKG: Grounding Out-of-Graph Molecules in Biomedical Knowledge Graphs via Multi-Resolution Structural Anchoring](https://arxiv.org/abs/2608.06713)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yiming Zhang, Hikaru Shindo, Shuan Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Biomedical knowledge graphs (KGs) accelerate drug discovery, but standard pipelines assume query molecules already exist as graph entities, leaving unregistered molecules disconnected. We address this cold-start challenge, termed the out-of-graph molecule problem, by introducing MolBioKG. This two-layer system grounds unseen molecules in biomedical evidence via multi-resolution structural anchoring. It connects an index of 2.74 million molecules (represented by scaffolds, fragments, functional groups, and fingerprints) to a 9.6-million-edge KG. Given only a SMILES string, MolBioKG retrieves structurally related graph entities and traverses their biomedical neighborhoods without task-specific training. It features two inference mechanisms: static multi-anchor retrieval using Reciprocal Rank Fusion, and Adapt-KG, a tool-using LLM policy for adaptive traversal. Evaluated across in-graph link recovery, complex multi-hop reasoning, and out-of-graph generalization, MolBioKG outperforms strong baselines. Notably, it raises Hits@10 from 0.585 to 0.876 in multi-hop reasoning and out-of-graph target recall from 0.145 to 0.269, all while ensuring predictions retain traceable structural anchors and source-attributed KG evidence.

---


### 95. [Solver-Guided Reasoning for Mixed-Equilibrium Strategies](https://arxiv.org/abs/2608.06741)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Han Wang, Philippe Beardsell, Boning Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning in large language models (LLMs) is often grounded in human text, human demonstrations, and human-generated rationales. For equilibrium reasoning in complex games, however, relying on human data can be suboptimal. In fact, human play is often guided by intuition and heuristics and can deviate substantially from game equilibrium. This discrepancy is amplified in games with mixed-strategy equilibria, where human data is heavily biased toward pure strategies. Consequently, conditioning LLMs on this data yields weak game strategies. To grant LLMs the reasoning capacity in games, in this work, we study how to elicit equilibrium play using solver output. We propose Mixed-Strategy Decision Tree (MDT), which articulates the silent optimality of the equilibrium into sparse strategic rules that both humans and LLMs could understand. Using solver output rather than human annotation allows us to extend the input to arbitrarily new states and continuations. We instantiate this study on No-Limit Texas Hold'em by querying a solver oracle for over \textbf{250 million mixed-strategy decisions}; MDT together with other techniques \textbf{reduces the $\ell_1$ distance to the equilibrium by $52.6\%$} across $8$ different LLM configurations. A Route-only ablation tests the incremental contribution of the shadow-based contrast, while complete River-endgame and Liar's Dice experiments evaluate strategic fidelity and portability beyond the original NLH communication setting.

---


### 96. [Progressive Content Refinement with Decaying Reward Joint LinUCB](https://arxiv.org/abs/2608.06750)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shion Ishikawa, Pablo Loyola, Young-joo Chung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Iterative refinement has significantly enhanced Large Language Model (LLM) performance; however, existing methods ranging from feedback-based Self-Refine to traditional bandit approaches often rely on static options or overlook the saturation effect. This neglect leads to over-exploitation, where the continuous use of identical prompts or arms results in diminishing rewards over time.
To address this challenge, we propose a novel contextual bandit algorithm that explicitly incorporates reward decay modeling. Utilizing an Expectation-Maximization (EM) algorithm, our method simultaneously estimates both arm-specific and decay parameters. Furthermore, by embedding prompts as arms, we facilitate the joint learning of arm values, distinguishing our approach from the traditional disjoint Linear Upper Confidence Bound (LinUCB) framework.
Experimental results on Sentiment Reversal and GSM8K benchmarks demonstrate that our method achieves significant performance gains over strong baselines. Finally, our ablation study confirms that the integration of reward decay modeling within the bandit framework is crucial for mitigating over-exploitation and optimizing the iterative refinement process.

---


### 97. [Mind the Gap: A Dual Knowledge Graph Framework for Unified Multi-task User Intent Inference](https://arxiv.org/abs/2608.06752)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Tzu-Cheng Peng, Chien Chin Chen, Chih-Hao Ku 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper proposes DKG-MTI, a dual knowledge graph framework for unified multi-task user intent inference from online travel reviews. Existing approaches often rely on hierarchical pipelines that suffer from error propagation or retrieval methods that ignore structural relationships in domain knowledge. To address these limitations, we introduce an inference-only knowledge augmentation framework that dynamically constructs a User-Specific Intent Knowledge Graph from each review and aligns it with a Global Hotel Knowledge Graph through structure-aware semantic smoothing. The aligned knowledge is combined with the original review and processed by a large language model to simultaneously predict aspect ratings and generate reverse user intent statements. Experiments on TripAdvisor reviews show that DKG-MTI consistently outperforms strong LLM and retrieval-based baselines in both classification and intent generation tasks, demonstrating the effectiveness of structure-aware knowledge alignment for scalable and explainable intent inference.

---


### 98. [Retrieval-Constrained Policy Optimization for Attack Technique Extraction from Cyber Threat Intelligence](https://arxiv.org/abs/2608.06778)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jiayun Zhang, Junshen Xu, Zejun Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mapping cyber threat intelligence (CTI) text to MITRE ATT&CK techniques is essential for structured threat analysis, yet manual annotation is costly and does not scale. The ATT&CK taxonomy comprises several hundred attack techniques, and a single CTI passage may describe multiple techniques, making accurate and complete extraction challenging. Existing automated approaches fall short in different ways: multi-label classifiers struggle with severe class imbalance and the large label space, while LLM-based methods--retrieval pipelines and fine-tuned generators--optimize token-level objectives that treat technique annotation as sequence generation rather than set prediction, lacking direct supervision on whether the predicted technique set is correct and complete. We propose TTP-R1, a two-stage framework that combines retrieval-augmented supervised fine-tuning (SFT) with reinforcement learning using verifiable rewards (RLVR). A hybrid retriever first narrows the large label space to a candidate set, and a fine-tuned LLM learns to select the correct techniques. We then apply Group Relative Policy Optimization with a decomposed reward that directly supervises the precision, recall, and output format of the predicted technique set. Across four CTI benchmarks, TTP-R1 achieves the best average F1, improving sub-technique-level F1 by 7.4 percentage points over Claude Sonnet 4.5 with retrieval augmentation, while running 28x faster when served as an 8B-parameter model on a single GPU.

---


### 99. [Multi-Perspective Triad Interaction Graph Neural Network for Cognitive Distortion Detection](https://arxiv.org/abs/2608.06785)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jun Seo Kim, Hye Hyeon Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cognitive distortion detection is a key task in computational mental health, yet existing approaches often overlook the psychological structure of distorted thoughts. We propose MTI-GNN (Multi-Perspective Triad Interaction Graph Neural Network), which models Beck's cognitive triad---negative views of the self, world, and future---as complementary perspectives for classification. An LLM decomposes each utterance into the three perspectives, from which perspective-specific similarity graphs are constructed and encoded by a Multi-Perspective GNN. A Triad Interaction module models cross-perspective dependencies through sequential source-conditioned updates and feature-wise gating, while Prototype-Guided Perspective Fusion performs label-conditioned aggregation. Label-expanded supervision incorporates all available distortion annotations during training. We evaluate MTI-GNN on 9,764 samples from four Korean, English, and Chinese datasets spanning ten distortion categories. MTI-GNN significantly outperforms all supervised variants and exceeds eight prompted generative models under zero-shot and few-shot settings. Leave-one-perspective-out ablations show that all three perspectives contribute significantly, while human expert evaluation provides preliminary evidence of their alignment with the intended cognitive dimensions.

---


### 100. [Understanding and Improving Model Editing for Secure Code Generation](https://arxiv.org/abs/2608.06848)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Weifeng Sun, Quanjun Zhang, Yuchen Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are widely used for code generation, yet they can reproduce vulnerable implementations learned from insecure training patterns. Prior work has mainly explored inference-time hardening, which reduces insecure generations without modifying the target model but relies on auxiliary components and adds runtime overhead. We conduct the first systematic study of model editing as a model-level hardening mechanism for secure code generation. We evaluate 3 state-of-the-art editing methods across diverse LLM families and compare them with CoSec, a representative inference-time approach, focusing on security, robustness, generalization, and functional correctness. Model editing yields larger security gains than CoSec on seen vulnerability types, improving security ratios by 15%-25% over vanilla models, with gains remaining stable under prompt perturbations. However, these improvements transfer unreliably to unseen vulnerabilities and can reduce functional correctness. To mitigate this trade-off, we propose SafeEdit, a post-edit refinement method combining functional tuning with edit-aware regularization. Across eight target LLMs, SafeEdit improves Pass@1 over UltraEdit by 11.73/13.70/15.50 percentage points at T=0.1/0.4/0.8 while largely preserving security. Compared with CoSec, it achieves relative security-ratio gains of 7.54%-12.04%. Additional evaluation on CodeGuard+ confirms improved joint secure-and-correct generation. SafeEdit and CoSec are also complementary, and their combination can further improve security while maintaining strong functional correctness. Overall, our results provide evidence-backed guidance for applying model editing to secure code generation.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-152](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
