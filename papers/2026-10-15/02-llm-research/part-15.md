# 🧠 大模型相关研究 | 2026年10月15日

> 本类共 **810** 篇论文：已确认 **758** 篇，待复核 **52** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**701-750**（第 15/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | **701-750** | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 701. [The Many Morals of AI: The cautionary bias of North American news narratives in global perspective](https://arxiv.org/abs/2610.18573)

**<font color=#1a73e8>作者：</font>** Andrew Piper, Edie Pearman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The stories told about artificial intelligence (AI) play a central role in shaping public understanding, policy debates, and expectations about technological change. News media are especially influential in this process. Using a cross-regional corpus of 12,924 English-language news articles about AI published since 2022, we examine how storytelling about AI varies across media systems in four regions: North America, China, India, and the Middle East. Leveraging large language models, we extract the implicit narrative lessons conveyed by each article---commonly known as story morals---capturing value-laden interpretations that extend beyond thematic content or sentiment. We find that North American AI coverage is uniquely characterized by narratives of caution, while under-emphasizing narratives of innovation and collaboration that are more prevalent elsewhere. However, this pattern is largely explained by a broader regional negativity bias in North American news sentiment, rather than by heightened concern about AI itself. Our findings bring into view the culturally conditioned nature of AI news narratives.

---


### 702. [Compare to Correct: Pairwise-Guided Logit Adjustment for LLM Test-Time Scaling](https://arxiv.org/abs/2610.18583)

**<font color=#1a73e8>作者：</font>** Cong Hua, Qianqian Xu, Zitai Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sampling-based test-time scaling enhances LLM reasoning by aggregating multiple reasoning paths for the same query. Existing methods use answer frequencies or path confidence to compute candidate scores, which do not explicitly characterize comparisons between competing answers. Inspired by the Condorcet principle in social choice theory, we introduce pairwise confidence comparisons between paths supporting different answers to capture answer-level comparative advantage. We combine this comparative evidence with voting support through a KL-regularized objective. Theoretically, we show that this comparative-advantage is equivalent to the adjustment to the traditional voting logits. In this way, our proposed Pairwise-Guided Logit Adjustment (PGLA) framework allows comparative evidence to compensate for weaker voting support and correct voting-based ranking errors. Experiments on 10 challenging benchmarks including mathematical reasoning, knowledge reasoning, and code generation with 7 models ranging from 1.7B to 32B parameters speak to the effectiveness of this plug-and-play term. Additional evaluations with external reward scores and online sampling further demonstrate its applicability.

---


### 703. [Decomposing and Predicting Annotation Disagreement in Harmful Content Across Languages](https://arxiv.org/abs/2610.18588)

**<font color=#1a73e8>作者：</font>** Irem Ecem Yelkanat, Faeze Ghorbanpour, Alexander Fraser  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Annotator disagreement is increasingly recognized as a meaningful property of subjective tasks, rather than merely noise to be removed. Predicting which items are likely to be contested could help allocate annotation effort and route difficult cases to human review. We propose predicting disagreement from interpretable semantic properties of the text. An LLM answers a set of binary questions covering harmful-content characteristics, disagreement-related cues such as borderline severity and missing context, and language-sensitive cues such as local slurs. A classifier predicts disagreement from these answers, and we analyze which questions contribute most to the predictions. Across four datasets in English, German, and Turkish and three open-weight LLMs, our structured question features outperform direct prompting by 10.5 ROC-AUC points and the strongest text-based baselines by 5.0 points. A compact subset of eight questions performs within 1.5 ROC-AUC points of the full twenty-question set. In leave-one-dataset-out evaluation, models retain roughly 90-95% of their in-domain ROC-AUC. Across models and datasets, questions about derogation, missing context, and decision boundaries serve as the strongest predictors, suggesting that what makes harmful content contested is partly observable in the text.

---


### 704. [Rethinking Projector Training in Multimodal LLMs](https://arxiv.org/abs/2610.18598)

**<font color=#1a73e8>作者：</font>** Fabian Gröger, Naël Ouerghemi, Shuo Wen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal LLMs are typically trained by first aligning a vision encoder with a language model via projector training on large image-caption datasets, followed by joint training of the full multimodal model. Despite its widespread use, the role of the projector training stage remains poorly understood. We find that (i) using only $10$ to $20\%$ of the data for training the projector already recovers most downstream performance gains, and (ii) projectors trained on different datasets can be linearly interpolated while largely preserving performance. These results suggest that projector training mainly performs a coarse alignment, which many different projectors achieve equally well. Motivated by these findings, we propose PORTAL, a training-free projector initialization that requires neither paired image-caption data nor gradient-based optimization, but only per-modality summary statistics. PORTAL computes an optimal-transport-based map between Gaussian approximations of the vision and language feature distributions on a shared principal subspace, so that the projector training stage can be skipped entirely. Without any paired data, PORTAL matches the standard pipeline trained on 558k image-caption pairs across six LLM backbones, two vision encoders, and 16 benchmarks. It outperforms that pipeline in $3$ of $7$ (vision encoder, LLM) settings and reaches an average $98\%$ of its score across the other four.

---


### 705. [Auditing Future-Memory Use in Point-in-Time Language Agents](https://arxiv.org/abs/2610.18602)

**<font color=#1a73e8>作者：</font>** Rongtian Ye  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Point-in-time (PIT) agents can recall post-cutoff facts even when their external evidence respects a historical cutoff. We examine whether this access predicts evidence gathering in 48 historical company-comparison tasks. Independent closed-book revenue probes identify the better-remembered company for each model on tasks with unequal recall, fixing the predicted direction before agent runs. We then compare paired runs with real or anonymized company identities while keeping external evidence PIT-valid. Both Qwen and DeepSeek recalled future facts, but neither supported the prespecified shift toward the better-remembered company. Qwen's four allocation estimates on 28 unequal-recall tasks were negative, with descriptive intervals spanning zero. A prospective DeepSeek replication showed an inverse pattern across all four metrics on 20 such tasks, with intervals below zero. These estimates remained negative after each company, pair, and future-fact omission, and all four post-hoc max-T-adjusted sign-flip p-values were below .05. In a prospectively specified follow-up, explicit future facts produced small estimated shifts away from the supplied-fact company, with intervals spanning zero, while final choices shifted toward it. The mechanism behind the natural inverse pattern remains unresolved. These findings support separate assessments of memory accessibility, search allocation, and final outputs alongside cutoff checks on external evidence.

---


### 706. [AgentStripes: An Evidence-Graded Maturity Model for AI Agents](https://arxiv.org/abs/2610.18603)

**<font color=#1a73e8>作者：</font>** Nutan Kumar Naik, Vijay Prasad Poudel, Aditya Kumar Saroj 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Benchmarks report what an Artificial Intelligence (AI) agent can do on a task suite, but not whether one released version has been engineered with the controls that make it reliable, safe and observable, or how strongly that is shown. This paper proposes AgentStripes, an evidence-graded maturity model for AI agents. It defines levels (0 to 7 stripes), process areas (12 areas holding 40 capabilities), three gates (basic, safety, proof) that hold an agent at a level however high its score, and evidence grades E0 to E5. Each applicable capability receives a rating from 0 to 3 and a separate evidence level; these are combined into a credit, aggregated into a severity-weighted score and converted into stripes that the gates limit. Instruments gather evidence, language-model judges interpret it under explicit criteria, and the arithmetic is deterministic. The model is compared with standards at topic level without a claim of conformance, and an unexecuted validation protocol is specified. An empirical evaluation (exploratory, non-confirmatory) of 30 public Python agent repositories, with static evidence only, is a demonstration and not a validation: static evidence caps every final stripe at 2, 26 repositories end at one stripe and 4 at two, and this distinction is unreliable, since re-judging changed the final stripe of 4 of 22 repositories (engine, dossier and panel changed), whereas none of 8 panel-only repeats, all at stripe 1, changed. The parameters are expert conventions without outcome based calibration, and the stripes have not been shown to predict reliability or safety.

---


### 707. [LLM2R: From Large Language Models to 3D Reassemblers](https://arxiv.org/abs/2610.18604)

**<font color=#1a73e8>作者：</font>** Zhouhan Zhong, Qiuhong Shen, Xingyi Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D part assembly aims to reconstruct a complete shape from a set of unassembled parts by predicting a rigid SE(3) transformation for each part. Because the placement of a part is rarely determined by its own geometry, the task demands reasoning over the entire part set, and existing methods, which rely on pairwise relations or iterative generation and verification, scale poorly to objects with many parts. We present LLM2R, which casts part assembly as sequence modeling with a pretrained decoder-only large language model (LLM): a Point-BERT encoder and a Q-Former compress each part into a block of geometric tokens, the blocks of all parts are concatenated, and a causal LLM adapted with Low-Rank Adaptation (LoRA) processes the sequence in one forward pass. Causal attention, however, lets the hidden states of a part observe only the parts that precede it. LLM2R therefore appends a block of learnable summary tokens after the last part: these tokens follow every part, so their states aggregate the whole assembly at a constant token cost, and a part-aware pose head fuses each part's states with them before predicting its rotation and translation. One architecture thus handles semantic and geometric assembly and predicts all poses in a single non-autoregressive pass. LLM2R achieves the highest part accuracy and success rate on all three PartNet categories, the best rotation error, translation error, and part accuracy on PartNeXt, and the lowest translation error and fastest inference on Breaking Bad, where only a fracture-specialized method is more accurate. Its advantage grows with the number of parts: at 100 parts it exceeds GARF by 33.5 points in part accuracy on Breaking Bad and Assembler by 29.1 points on PartNet, and it transfers zero-shot to unseen categories with more than 16 points higher part accuracy than the strongest of three baselines.

---


### 708. [From Hindsight to Foresight: Dissecting Clinical Evidence Acquisition in Large Language Models](https://arxiv.org/abs/2610.18605)

**<font color=#1a73e8>作者：</font>** Ziyang Ling  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often diagnose full sight, static clinical cases well yet struggle in foresight, dynamic diagnosis. Prior work has improved this limitation by quantifying the information models acquire and by developing stronger follow-up strategies to improve diagnostic accuracy. In contrast, we introduce a distinctive hindsight to systematically dissect why LLMs fail to acquire diagnostically critical evidence, tracing the failure from evidence identification, utilization and downstream diagnostic updating through not only diagnostic accuracy, but also evidence coverage, trajectory dynamics, and elicited probability and information entropy. Starting experiments from the breakdown at the level of capabilities, to the diagnosis of the pre-event state before the evidence arrives, and to the post-event state transition after the evidence arrives, our research has revealed the profound limitations and internal causes existing in the dynamic diagnostic process. At the same time, we have also conducted sufficient verification and generalization experiments to prove that these limitations are widespread. Together, these findings shift the central challenge from whether LLMs possess relevant clinical knowledge to whether they can identify, acquire, and effectively use the right evidence under clinical diagnosis and conduct a more detailed mechanism analysis to identify the exact location of the capability gap.

---


### 709. [Beyond Answer Voting: Fine-Grained Correction of LLM Reasoning through Graph Alignment across Sampled Traces](https://arxiv.org/abs/2610.18606)

**<font color=#1a73e8>作者：</font>** Haotian Liu, Yingjian Chen, Xiaohang Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly tackle tasks that require multi-step reasoning, where errors in intermediate claims can affect the final answer. Self-consistency (SC) improves reasoning by voting over sampled final answers, but its vote leaves intermediate disagreements unresolved. To address this problem, we introduce DDRG (Disagreement-Driven Verification Guided by Reasoning Graphs), a framework for selective correction from a frozen bank of reasoning traces. Our insight is that graph alignment can expose claim-level disagreements and provide correction evidence without expanding the sampled trace bank. DDRG builds source-grounded claim graphs and sends localized conflicts to an answer-blind verifier. A verifier-supported refutation that reaches the majority answer's supporting path triggers one focused repair; otherwise, DDRG returns the exact SC vote. Experimental results across five benchmarks show that native zero-shot DDRG improves macro-average accuracy over direct answering by 8.65 and 15.83 percentage points for Qwen2.5-7B and Llama3.1-8B. It also exceeds CoT, the evaluated GoT and GoV question-answering adaptations, and SC on this macro metric. DDRG links local verification to selective correction without enlarging the initial candidate bank.

---


### 710. [Jev-ToM: Evaluating Theory of Mind in Typed Decision Models](https://arxiv.org/abs/2610.18610)

**<font color=#1a73e8>作者：</font>** Kawai Chung, Chunkit Chan, Yuxuan Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dialogue and collaborative assistants repeatedly judge what a partner knows, believes, or intends. Typed decision models offer a potential alternative to generative large language models for bounded Theory of Mind (ToM) selection. We present Jev-ToM, comparing five typed decision models and seven generative baselines on 11,117 English text questions from nine ToM benchmarks across six capability groups. TypeSafe Jev reaches 73.2% source-balanced accuracy including native controls and ranks first or second across all six capabilities, leading beliefs, goals/desires/intentions, and emotions. Other typed models show distinct strengths across tasks. Separate resource comparisons suggest that Jev could reduce the cost and waiting time of repeated ToM selection. Confidence-based selection remains benchmark-dependent, and supplied reasons can repair errors or overturn correct answers depending on their attachment. Candidate expansion reveals distinct selection and output-validity problems. Related-question cues account for most of Jev's downstream gains, with task-dependent effects from predicted states. The findings motivate testing Jev as a ToM selection component in assistants, with task-specific confidence calibration, candidate design, and output validation as integration priorities.

---


### 711. [Legal-R1: Agentic Retrieval for Evidence-Based Legal Reasoning](https://arxiv.org/abs/2610.18611)

**<font color=#1a73e8>作者：</font>** Huaiwen Pang, Jiale Han, Junying Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Legal question answering requires answers that are not only plausible, but also grounded in legally valid and citable evidence. Standard retrieval-augmented generation often relies on one-shot semantic matching, which is insufficient when legal evidence must be selected according to authority, applicability, and diversity across heterogeneous sources. We introduce Legal-R1, an agentic retrieval framework for evidence-based legal reasoning. Legal-R1 decomposes legal reasoning into a multi-agent workflow, where a Lawyer agent learns when to retrieve, which legal source to query, what evidence to seek, and when the collected evidence is sufficient. A Legal Assistant agent retrieves from normative legal sources and precedent cases with authority-aware and diversity-aware selection, while a Judge agent generates the final answer from the complete evidence trajectory. We post-train only the Lawyer agent with masked supervised fine-tuning and trajectory-aware reinforcement learning. Experiments on multiple Chinese legal benchmarks show that Legal-R1 improves over general-purpose, legal-specific, and retrieval-augmented baselines.

---


### 712. [Does self-distillation improve reasoning?](https://arxiv.org/abs/2610.18613)

**<font color=#1a73e8>作者：</font>** Jason Ken Adhinarta, Raina Wu, Ashutosh Sharma 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-distillation is an emerging approach that trains a model to imitate its own predictions when conditioned on privileged information, such as correct answers or environmental feedback. Recent methods have reported better sample efficiency and generalization than reinforcement learning (RL), but it remains unclear whether these gains extend beyond in-distribution evaluations and whether they stem from privileged distillation. In this paper, we revisit two representative methods, Self-Distillation Policy Optimization (SDPO) and On-Policy Self-Distillation (OPSD), across code, science, tool use, and math reasoning tasks. We find that their reported gains do not consistently generalize to unseen problems and are largely explained by overfitting or transferring existing reasoning behavior, rather than effectively using privileged information. Moreover, self-distillation gradients show weak alignment with policy gradients that directly optimize expected reward, questioning whether they provide an effective direction for policy improvement. Our experiments across Qwen3 models (1.7B-14B) and OLMo-3-7B suggest that effectively leveraging privileged information to improve reasoning remains an open challenge. Our code is available at this https URL

---


### 713. [Can an Agent Learn to Predict Its Own Failure? Outcome-Grounded Confidence Calibration in LLM Agents](https://arxiv.org/abs/2610.18614)

**<font color=#1a73e8>作者：</font>** Ashutosh Hathidara  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Controlling an acting LLM agent means deciding, at each step of a long-horizon task, whether to trust its next action, abstain, or hand off to a human. That decision needs a per-step confidence signal predicting whether the current rollout will eventually succeed. The agent's own self-reported verbalized confidence is the natural candidate, but existing reinforcement learning methods calibrate it against the correctness of a decision at the current step. We propose a method to calibrate it against the eventual outcome of a multi-step episode: under GRPO, the group of rollouts for a task supplies success labels, and a proper scoring rule scores each step's confidence against the realized outcome. In offline RL on recorded trajectories of a Qwen2.5-7B agent in ALFWorld, TextWorld, and WebShop environments, the AUROC of step confidence against episode outcome rises from near chance to 0.68-0.85, and the top-10% of steps the agent is most confident about succeed ~4.3x more often than average. In online RL on the live ALFWorld agent, four calibration rewards improve early-step AUROC, expected calibration error goes from 0.42 to below 0.12, and selective execution improves over both the untrained agent and a format-only RL control, without degrading task success. We also introduce an evaluation protocol that separates episode depth, task difficulty, and attempt-level foresight, which shows where the gain lies: the trained agent recognizes from its first step which tasks it will fail, while telling a succeeding attempt from a failing one at the same task is harder, with some early-window signal emerging on TextWorld.

---


### 714. [VideoJev: System One Model for Video Understanding and Interaction](https://arxiv.org/abs/2610.18615)

**<font color=#1a73e8>作者：</font>** Yuhan Zhu, Xiangyu Zeng, Qingyi Si 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual agents must turn video observations into timely decisions to track progress and choose what to do next. Building on the emerging System One paradigm, we introduce VideoJev, a family of models that cast video understanding and interaction as structured decision tasks. We adapt pretrained multimodal large language models (MLLMs) by replacing autoregressive answer decoding with a shared head that scores temporal intervals and textual options against video evidence. These scores yield event spans or answer choices, unifying temporal grounding and multiple-choice video question answering. This combines the semantic flexibility of MLLMs with efficient decisions that agents can use directly. As an interaction unfolds, new goals and intermediate results prompt further queries about the same visual history. VideoJev therefore reuses visual computation through Cached inference for queries as they arrive and Joint inference for multiple queries in a single forward pass. Across three temporal grounding benchmarks, VideoJev-4B and VideoJev-35B-A3B improve mean mIoU over their backbones by 6.7 and 10.8 points, respectively, with measured inference speedups of $2.8$-$3.1\times$. On four video QA benchmarks, both achieve performance comparable to their backbones in Thinking mode, with measured inference speedups exceeding $100\times$. These results offer a unified, reusable decision interface for composing structured visual judgments into complex, open-ended workflows.

---


### 715. [Knowledge Graphs as Files: An Agent Harness Where Tool Creation and Tool Use Co-Evolve](https://arxiv.org/abs/2610.18616)

**<font color=#1a73e8>作者：</font>** Yuyang Bai, Yu Wang, Yu Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Searching text-rich knowledge graphs requires following relations while examining textual evidence. Predefined graph interfaces constrain what evidence agents can access, even when they write code to combine tool calls or process retrieved subgraphs. We propose direct knowledge graph interaction (DKGI), a harness in which language model agents create graph access tools directly over complete node and edge files. The agent writes Python code to follow relations, combine node sets, and select textual evidence, interleaving execution with shell search and file inspection. This lets agents process large node sets in bulk while returning selected text for the model to assess. Execution feedback guides tool creation and revision, while the evolving tools determine what evidence the agent gathers next. On benchmark datasets spanning three domains, training-free DKGI exceeds the strongest published baseline by at least 6.7 Hit@1 points on every graph, even with a minimal harness. Controlled ablations show the benefits of multi-turn programming over shell-only access and predefined graph tools, while trajectories show agents revising code to extend searches or address errors. These findings highlight the value of allowing tool creation and tool use to co-evolve during graph search. Our code and data are available at this https URL.

---


### 716. [MajorTOM:Elliot Pretrain, A Multi-Sensor, Multi-Temporal Pretraining Dataset for Earth Observation](https://arxiv.org/abs/2610.18624)

**<font color=#1a73e8>作者：</font>** Carmen Oliver Huidobro, Mikolaj Czerkawski, Kevin Monsalvez-Pozo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretraining generalist Earth observation foundation models requires data that combine several sensors, varied temporal sampling and, increasingly, text, yet open datasets rarely provide all three in one consistent, easily accessible form. We introduce MajorTOM:Elliot Pretrain, a collection of 279,166 tiles of 10 km drawn from the Major-TOM grid by clustering AlphaEarth embeddings. Each tile stacks Sentinel-2 L1C, Landsat-8/9, Sentinel-1 RTC, Copernicus DEM and ESA WorldCover on a shared 1056x1056-pixel, 10 m grid, complemented by cloud masks, OpenStreetMap entities and ERA5 weather. The tiles are partitioned into three temporal regimes, Monotemporal (250,000 tiles, one acquisition), Monthly (12,500 tiles, twelve acquisitions spread over the annual cycle) and Burst (16,666 tiles, six acquisitions within 30 days), and are released as 6.3 TB of Cloud Optimized GeoTIFFs indexed by TACO v3 Parquet metadata, a standard that allows cloud streaming, efficient data access, and filtering before any pixel is read. A companion library derives sensor-tagged fact sheets, captions and 16 families of vision-language tasks from these layers at load time. We test our design choices in short pretraining runs of OlmoEarth-Base. First, a 25% subset of Major-TOM Core-S2L2A curated with AlphaEarth embeddings matches or exceeds the full corpus on 8 of 9 benchmarks. Second, on Elliot-Pretrain, adding Landsat-8/9 improves or matches Sentinel-2 only pretraining on every benchmark. Third, using DEM and WorldCover as prediction targets during pretraining further improves 8 of 9 benchmarks, while giving the same maps to the encoder as inputs degrades 5 of 9. Fourth, Sentinel-1 helps on 7 of 9 benchmarks, particularly on benchmarks with radar inputs. Fifth, rule-based captions match a small language model at no cost. The dataset is openly available at this https URL.

---


### 717. [Geometric Calibration of Supervised Fine-Tuning](https://arxiv.org/abs/2610.18634)

**<font color=#1a73e8>作者：</font>** Jianzhu Bao, Jia-Chen Gu, Qingyuan Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent studies investigate the weight geometry through its spectral structure, which characterizes how the weights transform different input directions. Within this view, supervised fine-tuning (SFT) is shown to induce dense updates that perturb the spectral geometry of pre-SFT weights along their principal directions, potentially disrupting the model's prior knowledge. These observations motivate using the geometry of pre-SFT weights as a reference for refining learned SFT updates. We study this perspective as Geometric Calibration and develop SPACE Subspace Projection for Adapted Checkpoint Enhancement), a lightweight post-hoc method that selectively reverts SFT update components within the principal subspace of the pre-SFT weights while preserving those in its orthogonal complement. SPACE is a data-free, training-free method that requires only the pre- and post-SFT checkpoints. We evaluate SPACE on Qwen2.5, Qwen3, Qwen3.5, Llama-3.1, and Olmo-3 models ranging from 2B to 14B, across mathematical, coding, and medical SFT, as well as several SFT variants. Overall, SPACE mitigates out-of-domain (OOD) capability regression while further improving in-domain (ID) performance over the uncalibrated SFT checkpoints. For math SFT, SPACE yields average ID/OOD gains of 2.85/2.26 points on Qwen2.5-7B, and 2.41/1.52 points on Qwen3-14B-Base, respectively. These results highlight how the geometric relationship between SFT updates and pre-SFT weights shapes the adapted model's capabilities and, more broadly, motivate geometry-aware parameter updates for continual model improvement.

---


### 718. [To Align or Not To Align: Check Your COMPASS Before You Train](https://arxiv.org/abs/2610.18638)

**<font color=#1a73e8>作者：</font>** Fabian Gröger, Petar Damjanović, Maria Brbić  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Combining pretrained models is a common strategy for building AI systems, whether by aligning a vision encoder with a language model or merging fine-tuned checkpoints. However, finding compatible pairs typically requires costly empirical search, as compatibility is known only after alignment or merging. We propose COMPASS (COMPatibility ASsessment Score), a theoretically motivated diagnostic that estimates whether a model pair will be compatible prior to alignment or merging. Building on the observation that representational convergence is most robust at the level of local neighborhoods, COMPASS decomposes model compatibility into two cheap-to-compute axes: a pair-specific ease, defined as the $k$-NN overlap between the two encoders, and a paradigm-level ceiling, capturing the maximum overlap their training paradigms allow. Together, these two axes provide a ranking of candidate model pairs and prescribe how to act on each pair: (i) prioritize pairs that already agree and whose paradigms are compatible, (ii) invest additional compute on pairs with compatible paradigms but low initial agreement, (iii) switch the pretraining paradigm when it cannot support sufficient agreement, or (iv) deprioritize pairs that score poorly on both axes. We apply COMPASS to $72$ cross-modal alignment experiments and $392$ task-arithmetic model merges and show that compatibility estimates by COMPASS strongly correlate with downstream success, achieving average Pearson correlation of $0.91$ on cross-modal alignment tasks and $0.70$ on model merging.

---


### 719. [MultiAlloc: Budget-Aware Precision Allocation for KV Cache Quantization](https://arxiv.org/abs/2610.18642)

**<font color=#1a73e8>作者：</font>** Yangchengyu Zhou, Zhiping Wu, Runchang Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Key-Value (KV) cache constitutes a dominant source of memory consumption during large language model (LLM) inference, particularly in long-context and complex reasoning scenarios. Existing KV cache quantization methods have explored different compression granularities, including layer-wise precision adjustment and token-level information preservation. In practical deployment, however, the key challenge is not merely compression, but how to allocate limited quantization resources among heterogeneous precision preservation strategies under a fixed KV cache memory budget. We propose MultiAlloc, a profiling-guided precision allocation framework for KV cache quantization that adaptively distributes limited quantization resources between layer-wise precision enhancement and token-wise preservation. MultiAlloc employs lightweight offline profiling to characterize layer sensitivity and token importance, enabling adaptive precision allocation under a fixed memory constraint. Guided by the profiled memory--accuracy trade-off, it automatically derives an effective precision allocation strategy without online allocation search, and applies the resulting policy during inference. Extensive experiments on reasoning and long-context benchmarks demonstrate that MultiAlloc consistently improves over layer-wise, token-wise, and recent multi-granularity KV cache quantization methods under matched memory budgets across diverse models, including Mistral, Llama, DeepSeek-Qwen, and QwQ.

---


### 720. [Does Pretraining Teach Chemical Language Models Chemistry?](https://arxiv.org/abs/2610.18651)

**<font color=#1a73e8>作者：</font>** Leif Sieben, Yoel Zimmermann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chemical language models (CLMs) are pretrained on large corpora of molecules with the aim of learning representations that transfer to diverse downstream tasks. Here, we systematically study the effects of pretraining using a series of such CLMs across 64 molecular property prediction datasets. We find that the downstream gains of pretraining in CLMs do not scale and performance saturates below gradient-boosting baselines. Across the regimes evaluated, only supervised pretraining on traditional physico-chemical descriptors consistently improves downstream performance for the CLMs tested whereas some forms of pretraining result in models worse than a randomly initialized encoder. While models can resolve molecular structure well, they do so no better than a randomly initialized model, suggesting that, at best, CLMs learn descriptor-like properties in addition to low-level token statistics during pretraining, but surprisingly little chemistry beyond what classical molecular features already capture.

---


### 721. [Bayesian Test-Time Inference of Task-Aligned Similarity from Weak Interactive Feedback](https://arxiv.org/abs/2610.18656)

**<font color=#1a73e8>作者：</font>** Weida Liang, Kenji Kawaguchi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language model systems repeatedly make test-time decisions by comparing similarity: they retrieve exemplars, rank candidates, and revise responses. Yet similarity is not unique: lexical, semantic, structural, and stylistic resemblance can point to different candidates, and the task-aligned notion can change across instances. We introduce BASIS (Bayesian Axis Selection via Interactive Signals), a training-free Bayesian method that uses weak test-time feedback to infer which criterion in a supplied, task-specific library governs the current decision. It maintains a joint posterior over candidate targets and criteria, updates it from scalar scores, pairwise preferences, or verifier outputs, and selects probes by expected information gain. In a finite noisy model, we characterize when the target-criterion pair is recoverable and show why fixed-criterion and fixed-mixture rules can fail under criterion shift. Across concept recovery, reasoning exemplar selection, and response refinement, BASIS improves six-probe concept-recovery Success@1 from 56.0% to 68.1%, reasoning accuracy from 72.3% to 73.1%, and refinement win rate from 61.4% to 63.8% over tuned static mixtures. It also exceeds compute-matched best-of-N selection on reasoning (72.1%) and refinement (61.2%). Gains are largest under criterion mismatch and with larger candidate pools, and matched controls indicate that adaptive criterion weighting explains much of the benefit, with joint target-criterion inference adding further value. BASIS selects only among supplied criteria and does not discover new ones.

---


### 722. [SMI: Ontology-Grounded Semantic IDs for Hierarchy-Aware Medical Concept Representation](https://arxiv.org/abs/2610.18672)

**<font color=#1a73e8>作者：</font>** Ziyang Song, Lia Shen, Yixuan Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Biomedical language models (LMs) provide strong representations for clinical tasks, but they often fail to capture the hierarchical structure among medical concepts. This limitation is especially pronounced for rare and fine-grained clinical codes in long-tailed vocabularies, where hierarchy-agnostic LM representations become less informative as concept frequency decreases. We introduce Semantic Medical Identifier (SMI), a training-free framework for constructing ontology-grounded Semantic IDs and hierarchy-aware medical concept representations. For each diagnosis, procedure, or medication concept, SMI defines its Semantic ID as the coarse-to-fine path through an expert-defined medical ontology. SMI then aggregates frozen biomedical LM embeddings across the corresponding ontology levels to form hierarchy-aware medical concept representations that preserve coarse-to-fine clinical semantics. The base SMI uses uniform aggregation across ontology levels, while a level-weighted variant selects global level weights on validation data. Our theoretical analysis shows that SMI yields more informative medical concept representations than hierarchy-agnostic LM embeddings, particularly for rare and fine-grained clinical concepts. Experiments show that SMI captures meaningful hierarchical structure and improves clinical relation prediction. On MIMIC-IV, SMI improves mortality prediction, readmission prediction, drug recommendation, and rare drug prediction. On eICU, SMI yields more robust patient representations under cross-hospital distribution shift.

---


### 723. [From Relation-Specific Heads to Shared Interventions: Contextual Entrainment in Language Models](https://arxiv.org/abs/2610.18674)

**<font color=#1a73e8>作者：</font>** Jinghan Zheng, Jiajun Shi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models rely on prompt context to perform in-context learning, follow formats, and adapt to local evidence. This ability, however, also raises a robustness concern: models may reuse irrelevant tokens from earlier context when answering a later query. Prior work identifies this behavior as contextual entrainment and finds attention heads whose ablation reduces it, arguing that these heads are largely task- or relation-specific. But are the mechanisms behind contextual entrainment truly isolated by relation, or do relation-conditioned searches recover reusable components shared across relations? Using factual-distractor relation-completion prompts across 19 lexical-semantic subtypes, we identify attention heads whose ablation reduces entrainment and test how the resulting head sets transfer recovery ability across exact relations, semantic families, and mixed relation distributions. Same-family transfer exceeds different-family transfer, family residuals weaken once globally shared heads are removed, and subtype-specific searches repeatedly rediscover many global heads. Clean-completion and context-use probes further suggest that this shared intervention can reduce harmful copying while preserving ordinary relation completion and simple in-context abilities. Our findings provide a more precise perspective on contextual entrainment and its mitigation: harmful context following is not best addressed by searching for isolated relation-specific circuits, but by using heterogeneous attack prompts to reveal reusable intervention targets whose effects are shaped by semantic relation structure.

---


### 724. [ProAS: A Progress-Aware Advantage Shaping Framework for Multi-Turn Agentic Reinforcement Learning](https://arxiv.org/abs/2610.18683)

**<font color=#1a73e8>作者：</font>** Bowen Ding, Mingda Wan, Yuhan Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has emerged as the primary paradigm for optimizing Large Language Model (LLM) agents, yet efficient critic-free algorithms (e.g., GRPO) suffer from a fundamental uniform credit assignment dilemma that broadcasts trajectory-level advantages equally to all actions. Our analysis reveals that this uniformity inherently reinforces structurally invalid actions in preferred trajectories and ignores the downstream cascading influence of early pivotal deviations in unpreferred ones. To resolve this without introducing critic overhead, we propose Progress-Aware Advantage Shaping (ProAS), a plug-and-play framework that leverages a dynamically evolving Agentic Reference Graph (ARG) to achieve fine-grained credit assignment via Masking Unreasonable Incentives (MUI) and Asymmetric Penalty Redistribution (APR). Extensive experiments across Qwen2.5-1.5B-Instruct and Qwen2.5-7B-Instruct demonstrate that ProAS universally elevates mainstream group-based baselines to new state-of-the-art performance, achieving peak success rates of 91.9\% and 94.3\% on ALFWorld, alongside 66.7\% and 70.8\% on WebShop, respectively. Furthermore, it accelerates training convergence by up to $2.44\times$ while maintaining strong robustness against imperfect or distilled ARGs. Codes: this https URL.

---


### 725. [RSIgen: Reciprocal Self-Improvement for Agentic Visual Generation](https://arxiv.org/abs/2610.18688)

**<font color=#1a73e8>作者：</font>** Yidi Liu, Haozhe Wang, Jie Xiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Agentic visual generation produces experience that can improve the native understanding (agent) and generation roles of a unified multimodal backbone, but task success alone does not determine which role should learn. Generator updates can also make the agent's action supervision stale. We introduce RSIgen, a task-centric reciprocal self-improvement framework linking learning allocation, supervision refresh, and recursive curriculum construction. Dynamic Responsibility Routing (DRR) uses matched interventions on evidence, inputs, and supported actions to select learning recipients and construct compatible training targets. After generator learning, RSIgen re-evaluates the relative utility of tested actions with branch inputs held fixed to refresh agent supervision; the retained roles then construct the next curriculum. Across BAGEL, Qwen-Image, and Wan-Image-7B, RSIgen improves AgentGen-Bench Full Overall9 by 3.2--3.3 points over a three-cycle SearchGen adaptation with action costs. Wan controls support allocation gains at matched role-level training exposure, refresh gains at a matched adaptation budget, and benefits from updated curriculum sources while recipients continue learning. In blind evaluation on 200 real-user requests, pooled tie-adjusted preference scores against the same baseline reach 70.0% for task completion and 64.9% for visual quality.

---


### 726. [Just Respect the Semantics: Image-Token Compression via Pre-LLM Semantic Variable-Resolution Tokenization and In-LLM Relevance Pruning](https://arxiv.org/abs/2610.18690)

**<font color=#1a73e8>作者：</font>** Tianhao Fu, Austin Wang, Charles Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-token compression must reduce computation without hurting the semantics. We introduce Varest, guided by semantic fungibility: tokens within a coherent semantic region can be summarized coarsely, while object boundaries and literal text require finer distinctions. Object and text localizers guide variable-resolution merging, preserving spatial coverage and finer detail at boundaries and text. Learned [REL] registers then prune visual tokens after early decoder processing. Training across budgets enables one checkpoint per backbone. Across three backbones and 13 benchmarks, Varest outperforms 15 baselines in mean performance retention at every evaluated budget, retaining 86.10-92.33% of full-token performance with only 5.56% of the original layer-averaged image-token count.

---


### 727. [GeoReader: Learning Latent Geometry for Spatial Reasoning in Vision-Language Models](https://arxiv.org/abs/2610.18694)

**<font color=#1a73e8>作者：</font>** Rong Li, Shijie Li, Jiangyong Huang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) struggle with metric and multi-view relationships that remain implicit in RGB observations. Geometry foundation models recover this structure from RGB, but existing methods either fuse the estimated features with visual tokens and learn to use them from question answering alone, or align VLM latents with geometry features. Capturing geometry, however, does not ensure its use: zeroing the aligned latents of a released feature-alignment model leaves its accuracy unchanged. We introduce GeoReader, a framework that learns geometric representations for the VLM that reads them. First, we train lightweight Geometric Readers to produce continuous input tokens, supervising them with geometry descriptions decoded by a frozen VLM, so that the Readers express geometry in a form the target model can already read. We then freeze the Readers to preserve this interface while fine-tuning the VLM on spatial QA, with geometry injection conditioned on the question. Geometry descriptions serve only as training targets: at inference, the VLM answers directly from the continuous geometric tokens without generating a geometry chain of thought. With geometry predicted from RGB images, our approach reaches 94.3 on MindCube-Tiny with Qwen3-VL-4B and, with a multi-source QA mixture, an average of 72.5 across six additional spatial benchmarks with Qwen3.5-9B. These results suggest that a useful geometric representation is one the receiving model can use, not merely one from which geometry can be reconstructed.

---


### 728. [A Refresh Interval Does Not Fully Specify a Refresh Schedule: Learning-Rate-Dependent Placement in Kronecker-Preconditioned Language Model Training](https://arxiv.org/abs/2610.18695)

**<font color=#1a73e8>作者：</font>** Xinyu Wang, Zhiwei Zhai, Yu Gu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kronecker-preconditioned optimizers recompute a cached curvature eigendecomposition only periodically, and implementations and adaptive methods control this through the refresh frequency. We show that frequency leaves part of a schedule free: at a fixed number of refreshes, when they occur changes held-out loss at the same compute. Training GPT-style models with the Mousse optimizer across model sizes, we move the middle refreshes of a four-refresh schedule while fixing the first and last. On FineWeb the two placements exchanged rank as the learning rate rose (later placement was better at low rates, earlier placement at high ones), so a single-learning-rate comparison can report either ranking. The reversal held under controls including the published optimizer internals, and placement still mattered at the published refresh density. The learning rate at which the preference flips fell with model size, consistent with a held-out smaller model, and shifted with training length. A spectral-width staleness score predicted the same ranking at every learning rate and missed the reversal. Refresh schedules should be reported in full and compared across the learning rates at which they will be used.

---


### 729. [Unlocking Token Rewards via Training-Free Reward Attribution](https://arxiv.org/abs/2610.18704)

**<font color=#1a73e8>作者：</font>** Sitong Wu, Haoru Tan, Bin Xia 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose an extremely efficient, training-free method to extract token-level reward signals directly from an existing deep reward model. Our core idea is to attribute the overall process reward to individual tokens by estimating each token's influence. This influence is defined as the change in the final macroscopic reward (e.g., the process reward) when a token is replaced with a semantically null token. Naively calculating this influence is computationally infeasible, requiring N forward passes through the PRM for an N-token sequence. We overcome this bottleneck by proposing a highly efficient gradient-based estimator. Specifically, we use a first-order Taylor approximation, which simplifies the influence calculation to the inner product of the difference between the token embedding and the null token embedding, and the gradient of the reward with respect to the token embedding. This requires only a single forward and backward pass. The resulting token-level rewards enable standard RL algorithms to perform precise credit assignment without requiring additional reward model training. Experiments on challenging reasoning benchmarks demonstrate that our method substantially improves policy optimization efficiency and enhances the generalization of LLM reasoning capabilities. Our P2T outperforms the outcome reward by +4.9% on MathVista for Qwen2.5-VL-7B-Instruct, and +11.5% on AIME24 for Qwen2.5-Math-7B. The code will be released via this https URL.

---


### 730. [AIRRI: Towards a Human-Readable, Machine-Resistant Reading Interface](https://arxiv.org/abs/2610.18724)

**<font color=#1a73e8>作者：</font>** Emory Salaun, Syed Ayon, Kaleel Mahmood 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of image-to-text extraction systems and large language models (LLMs) poses new challenges for educational assessment by making assignment materials easy to transcribe and solve with minimal human effort. To address this problem, we present AIRRI (Artificial Intelligence Resilient Reading Interface), a framework for generating machine-resistant educational content, a dataset of higher-education assignments for evaluation, and an initial evaluation of the human readability of AIRRI machine-resistant text designs. AIRRI employs two categories of machine-resistance techniques. First, AIRRI applies image transformations including character spacing, word spacing, line spacing, character opacity variation, stripe overlays, and image noise. Second, AIRRI applies decision-based adversarial attacks: RayS, SurFree, and ADBA. We evaluate AIRRI against three image-to-text systems: Tesseract, EasyOCR, and the transformer-based GOT-OCR2 model. Our results show that AIRRI substantially degrades automated text extraction performance. AIRRI increased character error rates for EasyOCR (6.9% to 55.9%), Tesseract (2.3% to 100.0%), and GOT-OCR2 (30.7% to 48.1%). Word error rates increased for EasyOCR (24.9% to 96.7%) and Tesseract (10.7% to 100.0%). Among the evaluated decision-based attacks, ADBA consistently produced the largest degradation in image-to-text performance, while RayS and SurFree produced more moderate reductions. EasyOCR and Tesseract were generally more susceptible to both image-based and adversarial perturbations than the transformer-based GOT-OCR2 model. Our findings suggest that AIRRI can significantly reduce the reliability of image-to-text-to-LLM workflows, increasing the effort required for AI-assisted assignment completion.

---


### 731. [On the Monitorability of Natural Language Autoencoders: Identification vs Discrimination](https://arxiv.org/abs/2610.18727)

**<font color=#1a73e8>作者：</font>** Kevin Yandoka Denamganaï  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Natural Language Autoencoders (NLAs) are proposed as oversight tools for language models: an Activation Verbaliser (AV) writes an English explanation of an activation vector, and an Activation Reconstructor (AR) maps the explanation back to a vector. Their value for oversight depends on a human monitor being able to tell a true account of an activation from a false one, given the Av's explanation. We formalise NLA training and NLA oversight deployment as two different referential games from Emergent Communication: training is a generative referential game, while oversight is a discriminative, multi-modal, partially-observable referential game played over a many-to-many relation between the monitored language model's activations and the accounts that are true of them. The gap between the two games predicts that AV's explanations will identify which activation they describe without discriminating its true account from closely matched false ones, since training never asks explanations to rule anything out. Using the NLA's own AR as a maximally-sympathetic surrogate monitor model, we experimentally confirm this theoretical insight on one released checkpoint: true accounts beat accounts of other activations in all 320 comparisons, but beat fluent rivals differing in a single claim only 60.2% of the time (this http URL. 6.7%, chance at 50%, $n = 35$). A meaning-preserving rewrite by an uninvolved model costs only 2.1% of the distance to another activation's account, so the failure is not due to the NLA pair having developed private conventions in the AV's explanations. Our rival accounts test only transcript-level truths, which the monitored language model's conversation settles, so these results bound the easiest case and leave claims about the monitored model's own processing untested. We state conjectures that would make both results consequences of the framework.

---


### 732. [Segment Where You Look: Attention as the Interface Between Language Models and Segmenters](https://arxiv.org/abs/2610.18729)

**<font color=#1a73e8>作者：</font>** Eslam Abdelrahman, Hamza Omar Alkaf, Yuheng Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) that segment from language must pass the location of the referent to a pixel decoder. The dominant interface compresses it into the hidden state of a single [SEG] token, a d-dimensional vector with no spatial index, and leaves the decoder, which never sees the expression, to recover the referent's extent. We show that the VLM already computes a better signal: the [SEG] token's attention over the image tokens, which is defined on the patch grid by construction. Probing a frozen segmentation VLM, we find that this attention yields 18 to 22 more gIoU than the [SEG] hidden state when read by the same probe, that it gains nothing from the image where the hidden state does, and that it is concentrated in the late layers. Building on these findings, we introduce AttnSeg, which replaces the [SEG] embedding with this attention as the decoder's prompt. A learned, signed combination of the attention heads forms a dense spatial prompt, and an attention-guidance objective supervises it directly. A two-stage recipe first trains the VLM to localize without the decoder, then trains the decoder to refine, within the budget of standard fine-tuning. Applied to Sa2VA, AttnSeg improves ReasonSeg by 6.4 gIoU and GS-Eval by 10.2 at 4B (4.2 and 9.6 over the same model fine-tuned on the same data), and by 8.8 and 11.3 at 14B. The gains reach 13 to 18 gIoU on object parts, multiple objects, and single objects, where the referent must be singled out, and are negligible on stuff regions, which the decoder already recovers unaided. Code and models are available at this https URL

---


### 733. [SP$^2$ec: Adaptive Self-Speculative Decoding for Vision-Language Models](https://arxiv.org/abs/2610.18735)

**<font color=#1a73e8>作者：</font>** Yuqi Huang, Xingyao Li, Yunlong Hou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative Decoding (SD) has demonstrated its efficacy in accelerating large language model inference, but for Vision-Language Models (VLMs), the diverse input modalities make it difficult for a small trained drafter to achieve consistently high throughput. Self-speculative decoding reuses parts of the target model as a drafter which retains the multi-modal capability of the VLMs, yet its efficiency depends on choosing a suitable draft configuration for each prompt. We propose Single-Peak SPeculative decoding (SP$^2$ec), a training-free bandit algorithm that adapts the draft configuration during generation. SP$^2$ec exploits the single-peak throughput pattern observed in existing self-speculative methods, including SWIFT, KnapSpec, SpecVLM, and our simple cosSim. Our algorithmic design explicitly minimizes a novel notion of wall-time regret for each given query, corresponding to the empirical wall-time latency. Theoretical guarantees on the wall-time regret show that SP$^2$ec can exploit the optimal draft configuration, with negligible exploration cost. Extensive experiments on Qwen2.5-VL-7B-Instruct and LLaVA-NeXT-Mistral-7B across visual and textual tasks show consistent improvements of up to 11\% over the original self-speculative methods, demonstrating the wide applicability of the proposed SP$^2$ec algorithm.

---


### 734. [Enabling Token-wise Importance Sampling in Off-Policy RLVR with Proximal KL Regularization](https://arxiv.org/abs/2610.18738)

**<font color=#1a73e8>作者：</font>** Hao Bai, Jiarui Yao, Tong Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Off-policy data in reinforcement learning with verifiable rewards (RLVR) can arise from asynchronous generation, rollout-training mismatch, and response reuse. Token-wise importance weighting avoids multiplying likelihood ratios across a response but generally biases policy gradients. We prove that, under coverage and local expressiveness conditions, full future KL credit makes the exact proximal optimizer the update's unique stationary policy, even for mixtures of older policies, without full-response weights or a fitted critic. We further establish convergence of continuous-time tabular population updates under persistent coverage and time-varying behavior policies, and a finite-sample reward guarantee for linear logistic models under additional assumptions. These results motivate Proximal KL, a practical off-policy RLVR method that separates the proximal reference from the sampling policy and replaces PPO clipping with bounded future KL credit. Across all seven matched off-policy comparisons on Qwen3-1.7B and Qwen3-4B, spanning two learning rates, response reuse, and rollout staleness, Proximal KL outperforms GRPO in micro-averaged accuracy over eight math benchmarks by up to 2.58%. A separate on-policy comparison yields comparable aggregate accuracy. In periodic-refresh experiments, Proximal KL avoids the collapses observed in PG and CISPO, exceeds GRPO's training accuracy, and reaches higher accuracy in fewer policy updates. Ablations show that token-wise correction outperforms sequence-level and unweighted controls. With token-wise correction retained, future KL feedback reduces sensitivity to the tested baseline perturbation relative to PPO clipping. A finite future horizon improves AIME24 mean@16 and pass@16 over the full tail, while fixed-policy measurements show that truncation reduces correction variance over the tested horizons.

---


### 735. [Beyond the Verdict: Agentic Code Judging with Verifiable Feedback](https://arxiv.org/abs/2610.18760)

**<font color=#1a73e8>作者：</font>** Zheye Deng, Sha Li, Changlong Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-time scaling for large language models (LLMs) can involve generating multiple candidate solutions for selection or revising an earlier attempt. To guide selection and revision, we need a verifier that can estimate candidate correctness and provide evidence of failure. In competitive programming, however, official judging systems provide authoritative verdicts under finite submission budgets, without revealing failure explanations or failing inputs. To provide informative feedback without consuming official submissions, we formulate a task in which a model judges and diagnoses a candidate program using only the problem statement and source code, with generated counterexamples serving as checkable evidence. To evaluate this task, we build USACO-JUDGE from the USACO 2026 contests, using accepted and unaccepted programs written by human experts and multiple LLMs. We then train ARBITER, a 35B mixture-of-experts (MoE) agentic verifier, with reinforcement learning in a generic execution sandbox. Training raises counterexample success on incorrect programs from 40.61% to 62.67% and mean binary verdict accuracy on USACO-JUDGE from 71.41% to 87.41%, approaching frontier verification performance. Beyond verification, ARBITER outperforms baselines in both code selection and refinement. In an IOI 2026 case study, ARBITER-guided refinement raises GPT-OSS-120B's expected score above the gold-medal threshold under the official submission limit.

---


### 736. [Looking Complete Is Not Being Grounded: Evaluating LLM Sitreps Against Human-Authored Situation Reports](https://arxiv.org/abs/2610.18762)

**<font color=#1a73e8>作者：</font>** Sachin Kumar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluation for automatic crisis reporting should measure what practitioners need, not what is convenient to compare. Through LLM-assisted, author-approved content analysis, we derive a 15-slot information schema from professional humanitarian situation reports using qualitative content analysis, then evaluate 121 human and 261 LLM-generated reports across five disasters and three hazard types. Under google/gemini-3.7-flash on Cyclone Idai, the best machine arm is nominally above the empirical human ceiling (0.827 vs. 0.821), but the difference is statistically indistinguishable from zero (95\% bootstrap CI $[-.049,.059]$; permutation $p=.852$), and the ordering does not replicate under openai/gpt-5.6-luna. On a blind 100-item Idai sample, the author agrees with the Gemini judge at 0.910 accuracy and unweighted Cohen's $\kappa=.799$. All four judges clear the plan's raw-agreement criterion of .7; only Gemini reaches .7 on chance-corrected $\kappa$. Across the three primary events, machine reports reproduce 5.4-11.0% of same-day official figures. Across those same events, raw exact-number matching links 14.3-19.6% of official figures and 85.4-90.1% of machine figures to the social stream; manual audit confirms 45/50 declared absences, 4/25 official matches, and 24/25 machine matches semantically. The issuing-provenance gap is positive in all 12 observed event-judge cells: report date, organisation, series, and authority were not supplied at professional-report coverage in any cell. On the three primary events, ROUGE-L is uninformative, BERTScore is negatively associated with completeness after multiplicity correction, and a generic LLM judge changes sign.

---


### 737. [What Human-AI Interaction Leaves Behind: Residual Human States -- A Trajectory-Based Framework and Multi-Study Analysis](https://arxiv.org/abs/2610.18765)

**<font color=#1a73e8>作者：</font>** David Herrera-Poyatos, Carlos Peláez-González, Cristina Zuheros 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human-AI Interaction is commonly evaluated by what an artificial agent enables during use, yet interaction can also alter the human who acts next. We introduce Residual Human States, a trajectory-based framework for representing the potentially multidimensional human state carried forward after interaction with AI, relative to a relevant alternative trajectory. The framework distinguishes assisted output from human-state transition and derives four empirical propositions: multidimensionality, interaction-policy dependence, horizon dissociation, and temporal persistence. Its central claim is that assisted performance does not by itself determine the human state carried forward.
We examine these propositions through four empirical cases with different inferential roles. Published medical-training evidence illustrates how one AI interaction history can be associated with both slightly higher observed accuracy on some later unaided cases and transmission of a systematic decision bias on others. A second diagnostic-learning study shows that later unaided behaviour differs across AI-support policies, while also revealing that aggregate accuracy cannot by itself distinguish improved discrimination from a shifted response criterion. In a classroom experiment, generative-AI tutoring substantially improved assisted practice performance without a corresponding detectable gain on a subsequent unaided exam. A longitudinal reanalysis of personalised AI dialogue further shows that residual contrasts can evolve across post-interaction horizons and that such change may arise from the comparison trajectory as well as from the focal intervention.
Evaluating interactive AI systems therefore requires attention not only to contemporaneous performance, but also to which human states alternative interaction trajectories produce, relative to which counterfactuals, and how durably.

---


### 738. [BLADE: Auditing Information Use for Failure Attribution in LLM Multi-Agent Systems](https://arxiv.org/abs/2610.18780)

**<font color=#1a73e8>作者：</font>** Xiaoguang Guo, Yaohao Long, Chuxu Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model multi-agent systems extend individual agents' capabilities through collaboration across specialized roles, tools, and workflows. Yet collaboration makes failures harder to diagnose: one agent may misinterpret a correct result while others carry the mistake forward. Failure attribution therefore seeks to identify the responsible agent and decisive error step. Recent methods trace dependencies, but knowing where information came from is not the same as knowing where it went wrong. We introduce BLADE (Blame Localization via Audited Dependency Evidence), a training-free framework that moves beyond tracing information to auditing its use. Using Jev for structured probabilistic judgments, BLADE uses dependency probabilities to select relevant source-decision handoffs for auditing. At these handoffs, it examines whether receiving decisions use their sources faithfully and within task requirements, distinguishing error introduction, propagation, and repair. These findings inform a global diagnosis that considers all execution steps. Without reference answers, BLADE achieves the best or tied-best step accuracy among eight strategies under a shared Jev decision interface on 1,228 failed runs across five Who&When and Who&When Pro subsets, outperforming All-at-once by 2.2-11.1 percentage points. Making responsibility evidence explicit offers a path toward more interpretable and reliable agentic systems.

---


### 739. [Where Do LLM Ensemble Gains Come From? Decomposing Candidate Value, Diversity, and Aggregation](https://arxiv.org/abs/2610.18786)

**<font color=#1a73e8>作者：</font>** Donghwan Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM ensemble gains are often measured against a single baseline, but the value attributed to additional candidates can change with the comparison used. We study an LLM aggregator under four matched conditions: Direct (no candidates), Single-slot (one candidate in a multi-slot interface), Duplicate (one candidate repeated), and Multi-candidate (separately generated candidates). Under either non-diverse control, overall candidate gain (CIV) splits algebraically into an additional-candidate contrast (DSV) and a candidate-context contrast (CCV); the split, but not CIV, depends on the chosen control. On MultiHopRAG model diversity (k=2), the repetition gap Rep=-8.33 pp [-13.25, -3.75] quantifies the difference between gains measured against Duplicate and Single-slot. On a matched FRAMES stronger-panel extension (n=200, k=3, aggregator output limit 4096), paired Delta Rep=+9.67 pp [+6.00, +13.50]; within panels, Rep changes sign (original -6.33; stronger +3.33). In FRAMES evidence aggregation, candidate-context contrasts remain strongly negative under both non-diverse controls. Our results show why ensemble evaluations should state the reference control before attributing gains to additional candidates.

---


### 740. [SkillScaffold: Scaffolding Agentic Reinforcement Learning with Policy-Adaptive Skill Credit Assignment and Selective Injection](https://arxiv.org/abs/2610.18807)

**<font color=#1a73e8>作者：</font>** Wenlin Zhong, Hao Wang, Kun Yuan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agentic reinforcement learning (RL) enables large language models (LLMs) to learn from multi-turn interactions with verifiable outcomes. Textual skills can improve exploration by distilling prior interactions into reusable guidance. However, existing skill-based RL approaches often either assume skill injection is beneficial or rely on indirect feedback or rollout-intensive evaluation to assess its utility. Our pilot studies show that rollout-based utility estimation for skill credit assignment is costly and unstable under limited sampling, while skill benefits vary across candidates and depend on the current policy's competence on each query. To address these challenges, we introduce SkillScaffold, a policy-adaptive training scaffold that combines low-cost skill-utility estimation with selective skill injection. By reusing outcome-verified training trajectories, SkillScaffold generates candidate skills and estimates their utility through outcome-aware likelihood comparisons, without candidate-specific environment rollouts. The resulting utility guides whether and which skill to inject, retaining skill-free execution when no candidate is estimated to help. Joint training enables the Generator to produce skills tailored to the evolving Executor. Scaffolded RL encourages skill internalization for skill-free inference. Experiments on ALFWorld, WebShop, ScienceWorld, and $\tau^2$-Bench demonstrate gains over strong agentic-RL and skill-based RL baselines across both short- and long-horizon tasks. Ablations and further analyses support the importance of utility-based selection and abstention. Our code is available at this https URL.

---


### 741. [Self-Evolving Agent Harness](https://arxiv.org/abs/2610.18813)

**<font color=#1a73e8>作者：</font>** Chuyang Wei, Haoxiang Guan, Minghang Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Harness self-evolution revises an agent's software scaffolding, including prompts, memory, workflows, and executable components, while keeping model weights fixed. We formalize a feedback-driven process in which accepted revisions persist across runs. The framework separates update targets from proposal and admission mechanisms. It distinguishes changes to interpreted state from revisions to tools and code, repository-level control logic, and plugin composition. We characterize search through evolutionary optimization and examine its reliability through continual PAC-learning. Under explicit assumptions, the analysis yields an expected generalization bound, a retention bound conditional on historical regression budgets, and a high-probability admission rule using fresh, independent validation data. We examine how persistent harness revisions affect knowledge sharing and organizational workflows, with implications for scientific reliability, physical safety, and institutional accountability. Cases from prior work illustrate model--harness co-design, distributed execution, and plugin reuse. Reliable deployment requires continual validation as task distributions and evaluators change, with independent safeguards for learning, runtime privileges, and consequential actions. We provide a comprehensive 66-page discussion of related work, theory, algorithms, evaluation, applications, and the broader impact of Harness RSI, together with continuously updated code and supplementary materials, at this https URL.

---


### 742. [Back-Translation Still Matters: Leveraging Monolingual Data for Low-Resource Machine Translation with LLMs](https://arxiv.org/abs/2610.18818)

**<font color=#1a73e8>作者：</font>** Divyanshu Bathla, Parag Singla, Jitin Singla  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pre-trained Large Language Model (LLMs) are effective on many tasks in zero-shot and few-shot settings. For machine translation of low-resource languages, the obvious options are few-shot prompting and fine-tuning on a small parallel set. We ask: what if moderate amounts of low-resource monolingual data are also available? We argue that, rather than continued pretraining, a more effective use of this data is the pre-LLM era technique of back-translation (BT). The current fine-tuned LLM translates monolingual sentences in each language, and the resulting pairs train it in the reverse direction. Updates on the parallel set are interleaved for stable learning. With 1K parallel pairs on Odia and Swahili, BT beats continued pretraining into the low-resource language by 7.7 to 16.4 XCOMET-XXL points in domain. With beam-decoded intermediate translations, it also beats a model with 10 time more parallel data. In-context examples retrieved from the parallel data further improve BT. We also analyze the source, quality and amount of monolingual text. Across five low-resource languages, with Hindi as a high-resource control, and two 3B backbones, BT improves translation into the low-resource language by 16 to 173% XCOMET-XXL over parallel-only fine-tuning. Blind human evaluation on Odia and Sanskrit agrees with the automatic metrics.

---


### 743. [Read the Room Before Your Model Generates](https://arxiv.org/abs/2610.18820)

**<font color=#1a73e8>作者：</font>** Muyao Kong, Zhihao Lin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) generally rely on sampling temperature to regulate the amount of randomness in their outputs. Mainstream methods for selecting temperature typically involve fixed, heuristic global settings and context or token-level calibration, rather than a geometrically interpretable representation of the communicative scenario. In this work, we introduce a simple and interpretable temperature selection framework, the \textbf{Scenario-Actor}, which adapts decoding to the inferred situational characteristics. Scenario-Actor extracts scenario-relevant structures from Transformer hidden states and determines the temperature from scenario embedding, a structured geometric representation of the communicative setting. Empirical results show that on Llama-3.1-8B-Instruct, Scenario-Actor achieves strong goal-completion performance in interactive social scenarios, significant gains on open-ended instruction following, and competitive performance on multi-turn conversation compared to multiple baselines.

---


### 744. [OmniCompass: A Holistic Benchmark for Omni-Modal Video Grounding and Understanding](https://arxiv.org/abs/2610.18829)

**<font color=#1a73e8>作者：</font>** Xuyang Liu, Shihao Wang, Xinyu Wei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the rapid development of multimodal large language models (MLLMs), evaluating their video understanding capabilities has become increasingly important. Existing video understanding benchmarks cover only part of the evaluation dimensions, limiting systematic diagnosis of omni-modal video understanding. We introduce OmniCompass, a holistic benchmark for omni-modal video grounding and understanding. OmniCompass defines two evaluation tracks: OmniCompass-VL assesses vision-language models on tasks requiring visual evidence, while OmniCompass-AV assesses omni-modal models on tasks requiring joint audio-visual evidence. Each track includes three complementary tasks: temporal grounding (TG), spatial grounding (SG), and question answering (QA), assessing when a referenced target appears, where it is, and what happens. QA covers five perception and three reasoning categories in OmniCompass-VL, and three perception and two reasoning categories in OmniCompass-AV. OmniCompass-VL contains 820 videos and 2,460 instances across domains and three duration types: short, medium, and long. A narrative- and audio-rich subset forms OmniCompass-AV with 240 videos and 720 instances. Each instance is evaluated under two paired settings: text-only and text+image, specifying the same target through text and visual-language guidance. All instances are manually annotated with multi-round quality verification. Evaluations of 50 MLLMs show that open-source models still lag behind proprietary counterparts, particularly in audio-visual understanding. Precise temporal and spatial grounding remains challenging even for leading models, and their predictions still exhibit inconsistencies across the paired target specifications.

---


### 745. [Game2Real-Bench: Do Toy Games Reveal and Transfer to Real-World Visual Reasoning?](https://arxiv.org/abs/2610.18834)

**<font color=#1a73e8>作者：</font>** Qingan Liu, Juntong Feng, Yue Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual reasoning is an important capability for vision-language models (VLMs) to understand visual evidence, spatial structure, constraints, and state changes. Existing evaluations mainly rely on real-world data or procedurally generated tasks. Real-world data preserve natural complexity, while procedural games provide controllable generation and verifiable solutions. However, it remains unclear whether abilities measured in toy games correspond to real-world visual reasoning and whether game examples can support transfer. We introduce Game2Real-Bench, a benchmark that studies these connections across four capability groups, including fine-grained perception, spatial reasoning, constraint reasoning, and sequential planning. We construct 1,000 procedurally generated game samples with executable verification and curate 400 real-world samples aligned by shared reasoning requirements rather than visual similarity. We evaluate 25 representative VLMs and observe strong game-to-real consistency, with Pearson and Spearman correlations of 0.935. We further study one-shot game-to-real transfer on four models. Constraint reasoning improves for several models, while fine-grained perception declines with game demonstrations. We also construct Game2Real-Dataset with nearly 24K verified game samples across 18 tasks and 65 QA families. Our benchmark, dataset, and code are available at this https URL.

---


### 746. [Plan-Bench: Can Existing VLMs Go Well Beyond Perception to Reason and Plan in Embodied Worlds?](https://arxiv.org/abs/2610.18836)

**<font color=#1a73e8>作者：</font>** Juntong Feng, Qingan Liu, Jingru Dong 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have achieved strong performance in visual perception and spatial reasoning, leading to growing interest in using them as high-level planners for embodied AI. However, physical tasks require models to integrate spatial information, reason over temporal states, and generate multi-step plans under various constraints, raising the question of whether current VLMs can reliably support such reasoning and planning independently of execution. We introduce Plan-Bench, a benchmark for evaluating the high-level reasoning and multi-step planning capabilities of VLMs relevant to embodied worlds, while isolating the influence of action execution. It covers three complementary dimensions, spanning 16 subclasses and 699 curated samples. Extensive evaluation of 28 VLMs reveals room for improvement, with even the strongest model achieving only 75.0% accuracy. We further find that model scaling generally improves these capabilities. Ablation studies also indicate larger models show increasing potential as high-level planners. Overall, Plan-Bench provides a lightweight probe for evaluating VLMs' reasoning and planning capabilities relevant to embodied environments and assessing their potential as decision makers for physical tasks. Our benchmark and code are available at this https URL.

---


### 747. [RepProbe: Can Video Language Models Count Repeated Actions? A Diagnostic Benchmark](https://arxiv.org/abs/2610.18844)

**<font color=#1a73e8>作者：</font>** Mahsa Khoshnoodi, Sarah Adel Bargal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Repetition counting requires identifying and enumerating action cycles over time. While state-of-the-art video language models describe actions fluently, they fail to reliably count how many times an action repeats. To investigate this limitation, we introduce RepProbe, a benchmark of 42K real and synthetic video clips containing exactly k in [1, 20] complete repetitions, with controls for clip position, temporal coverage, and duration. These controls allow us to study the counting failure directly and locate where in the model it arises. Counting accuracy collapses at high counts across the video language models we evaluate, and controlled experiments show this collapse is not explained by frame sampling alone. We compare model outputs with linear probes trained on the final-layer representations used to generate those outputs. We find a consistent representation-to-output dissociation: substantial count information remains linearly decodable even when models fail to report the correct count. Further analysis shows this failure arises primarily at the output stage, where answers concentrate on a small set of preferred numbers rather than the available count information. The dissociation holds on both real and synthetic videos and is not explained by clip duration, position, or scene content. These results indicate that models encode repetition structure but do not reliably report it in their outputs. Project page: this https URL

---


### 748. [The Last Remote Sensing Model Built by Humans? Casting Any Earth Observation Task as Recursive Self-Improvement](https://arxiv.org/abs/2610.18845)

**<font color=#1a73e8>作者：</font>** Sijie Zhao, Zeqi Zhou, Heli Qi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Earth observation (EO) models are still built by hand. For each new task, experts design a training recipe and tune it against a benchmark. We show that this loop can be handed to an agent. Any verifiable task can be cast as a harness and a verifier, where the harness defines what the agent may use and the verifier defines what counts as success. Every EO task can be made verifiable, through labeled benchmarks, independent sensors, physical models or the repeated observation of the same place. Given only these two components, a general-purpose coding agent builds the EO model and improves it recursively on its own outputs. Settings long treated as separate research problems, from learning with a handful of labels to adapting across domains, become choices of harness and verifier. On four EO benchmarks spanning optical, SAR and multispectral time-series imagery, agent-built models surpass the state of the art and keep most of that accuracy from about 1% of the training labels. This establishes a new paradigm for EO, in which people design harnesses and verifiers and agents build the models, so EO models improve as agents do.

---


### 749. [MFG: Multi-turn Feedback Guided Molecular Optimization](https://arxiv.org/abs/2610.18851)

**<font color=#1a73e8>作者：</font>** Trieu Nguyen, Frazier N. Baker, Ruoxi Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-objective molecular optimization is a critical process in drug discovery that aims to modify a given molecule to simultaneously improve multiple properties while maintaining a similar overall structure. This process often requires iterative modifications guided by computational or experimental feedback. Recent large language model (LLM)-based methods have begun to explore this iterative approach; however, these methods are not explicitly trained to leverage such feedback, while existing approaches primarily focus on single-turn molecular optimization. To address this gap, we introduce Multi-turn Feedback Guided (MFG) molecular optimization, a reinforcement learning framework that trains an LLM to progressively optimize molecules using feedback from previous turns. MFG introduces a feedback vector capturing both property improvements and source molecule similarity, alongside a feedback-aligned reward function that promotes progressive improvement across turns. We apply MFG over $\text{GeLLM}^{3}\text{O}$, a state-of-the-art LLM model for multi-objective molecular optimization, evaluate $\text{GeLLM}^{3}\text{O-MFG}$ on ten multi-objective molecular optimization tasks. The results demonstrate that $\text{GeLLM}^{3}\text{O-MFG}$ achieves the highest average similarity-constrained success rate ($81.50%$), outperforming the base model $\text{GeLLM}^{3}\text{O}$ ($70.81%$).

---


### 750. [Two Clocks: Why Larger Rollout Batches Learn Slower but Fail on Schedule in Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2610.18853)

**<font color=#1a73e8>作者：</font>** Yuante Li, Junwei Quan, Kai Qiu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) relies on costly model-generated responses, motivating larger rollout batches and square-root learning-rate scaling. Reported to approximately preserve progress per sample with one optimizer step per rollout, this rule is less understood in practical multi-step training. We develop a two-clock framework that separates the samples needed to make progress from those consumed before collapse. Under a local quadratic model, the square-root rule preserves first-order drift per sample but not progress: larger batches take fewer, longer updates and lose more to curvature, yielding a learning-rate-dependent critical batch beyond which sample efficiency degrades. A drift-threshold hypothesis predicts a complementary failure clock whose sample count remains approximately invariant along the square-root rule. Controlled GRPO experiments on Qwen2.5-Math-1.5B across a $16\times$ batch range support both predictions. Ratio clipping delays failure, especially for larger batches, but the progress gap persists without it. Widening the clip trades stability for a transient speed gain. The progress gap reappears on another dataset, a general-purpose checkpoint, and a 7B model. Finally, we use the two-clock framework to derive a simple multi-step RLVR schedule: start below the critical batch and switch to a larger batch before failure. Our code is available at: this https URL.

---


> [!TIP]
> 当前位于：**701-750**（第 15/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | **701-750** | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
