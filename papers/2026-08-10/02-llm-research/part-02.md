# 🧠 大模型相关研究 | 2026年08月10日

> 本类共 **79** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究。

> [!TIP]
> 当前位于：**51-79**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-79**

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


> [!TIP]
> 当前位于：**51-79**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-79**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
