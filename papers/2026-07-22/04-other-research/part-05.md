# 📦 其他研究 | 2026年07月22日

> 本类共 **386** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-386](./part-08.md)

---

### 201. [DADIR: Density-Aware Data-level Imbalanced Regression Framework](https://arxiv.org/abs/2607.17178)

**<font color=#1a73e8>作者：</font>** Shermin Shahbazi, Hossein Mohammadi, Mohsen Afsharchi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Imbalanced learning addresses predictive modeling problems with underrepresented regions of the data distribution. Although widely studied in classification, imbalanced regression remains challenging because of continuous target variables and heterogeneous density distributions. Existing data-level methods often rely on fixed target partitioning or synthetic sample generation without jointly considering density variations and local feature-space structure. We propose DADIR, a Density-Aware Data-level Imbalanced Regression framework that exploits density information throughout the balancing process. DADIR comprises three components: (1) Density-Aware Adaptive Partitioning (DAAP), which recursively partitions the target space according to density variations; (2) a Density-Regularized Conditional Variational Autoencoder (DR-CVAE), which preserves sparse-region representations while learning latent features; and (3) latent-space data balancing, which combines feature-level clustering with oversampling to generate structurally consistent synthetic samples. Together, these components identify minority regions more effectively, preserve sparse-region information, and generate realistic synthetic data. The resulting balanced dataset can be used directly with existing regression models without modifying their architecture or learning objective. Experiments on diverse imbalanced regression datasets demonstrate consistent improvements in predictive performance, particularly in underrepresented regions, while also improving overall accuracy.

---


### 202. [PocketPPD: Screening for Postpartum Depression Risk Using Passive Smartphone Sensing](https://arxiv.org/abs/2607.17185)

**<font color=#1a73e8>作者：</font>** Jia Tang, Helinyi Peng, Akihito Taya 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Postpartum depression (PPD) is a serious perinatal mental health condition affecting approximately 20% of new mothers worldwide. Common screening approaches for PPD, such as self-report questionnaires and active digital logs, rely heavily on user input and thus impose a substantial burden on participants, limiting their feasibility for long-term use. Recent passive mobile sensing (PMS) approaches have enabled low-burden detection of depressive symptoms using machine learning methods with multi-modal sensor data from off-the-shelf mobile devices including smartphones. However, the postpartum period entails distinct behavioral patterns, raising uncertainty about whether sensing-based indicators for general depression and mental disorders generalize to PPD. To address this gap, we propose PocketPPD, a PMS-based PPD screening method that detects PPD risk using maternal contextual features, such as disruptions in behavioral rhythms and shifts in stability, collected through a smartphone. In our exploratory four-week feasibility study with 61 postpartum women, the PMS-only model achieved an AUC of 0.75, while the best-performing model, integrating PMS-oriented data and self-report features, achieved an AUC of 0.83. Moreover, we find that morning and late-night routine volatility ranks among the top digital biomarkers, dynamically moderated by maternal contexts such as infant developmental stage and employment status. This work provides empirical evidence for low-burden PPD risk screening and our findings lay the groundwork for continuous perinatal mental health monitoring.

---


### 203. [Fast and Private Max-Sum Diversification](https://arxiv.org/abs/2607.17196)

**<font color=#1a73e8>作者：</font>** Ron Zadicario, Tova Milo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Result diversification is crucial for generating informative, non-redundant data summaries and query outputs. Although its various formulations have been extensively studied across an array of data-driven disciplines, existing methods fail to address the privacy concerns that arise when the underlying data is sensitive. In this work, we initiate the study of result diversification under differential privacy, focusing on the max-sum diversification (MSD) problem, a widely adopted model with the objective of maximizing a linear combination of a submodular function, quantifying relevance, and the sum of pairwise distances between selected items, quantifying diversity. We propose differentially private algorithms for MSD under both cardinality and matroid constraints, achieving nearly optimal utility guarantees. At the same time, we design more efficient algorithms that maintain strong guarantees. Notably, the proposed algorithms are faster than existing non-private methods, making them appealing even in non-private settings. Experimental evaluations on real-world datasets demonstrate that the proposed approach achieves utility comparable to that of non-private baselines even under strong privacy guarantees, and significantly improves execution times for cardinality constraints.

---


### 204. [Cross-Coordinate Correspondence Pruning for Image-to-Point Cloud Registration](https://arxiv.org/abs/2607.17200)

**<font color=#1a73e8>作者：</font>** Xin Liu, Rong Qin, Huipeng Lin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent detection-free approaches have shown significant efficacy in image-to-point cloud (I2P) registration by employing a coarse-to-fine matching pipeline. In the coarse stage, down-sampled image features and voxelized point cloud features are typically fused to establish initial coarse correspondences for subsequent refinement. However, existing methods largely overlook the critical role of point cloud density, which fundamentally dictates the quality of coarse correspondences and the final registration results. Specifically, excessively sparse point clouds lead to an insufficient number of inliers, while overly dense ones often introduce a high outlier ratio. Consequently, this creates an inherent density trade-off, thereby significantly limiting the registration accuracy of current approaches. For mitigating this trade-off, we propose a novel Cross-Coordinate Correspondences Pruning (CCP) strategy to acquire sufficient inliers while ensuring a low outlier ratio. To minimize interference from inter-modal coordinate discrepancies, we first project cross-coordinate coarse correspondences to the 2D image coordinate system for spatial unification. Subsequently, a lightweight pruning network is responsible for predicting the inlier confidences, which are used to filter coarse outliers, from coordinate geometric and modal feature dimensions. To maximize inlier recall, we further design a Multi-Density Point Ensemble (MDPE) strategy that consolidates and deduplicates pruned coarse correspondences across varying point cloud densities. Our method achieves a significant performance improvement, surpassing existing state-of-the-art methods by at least 8.6% in Registration Recall across various benchmarks.

---


### 205. [SpexPay: A Privacy-Preserving Pay-As-You-Go System for Dynamic Spectrum Sharing](https://arxiv.org/abs/2607.17218)

**<font color=#1a73e8>作者：</font>** Mohaimin Al Barat, Hexuan Yu, Shaoyu Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Dynamic Spectrum Sharing (DSS) is a cornerstone of next-generation wireless systems, yet existing solutions such as Spectrum Access Systems (SAS) rely on centralized administrators that expose sensitive operational metadata and lack cryptographic transaction accountability. Though SAS administrators, such as Google, have introduced pay-as-you-go pricing models, these approaches still face significant privacy and accountability challenges as DSS evolves toward a more open and large-scale spectrum marketplace. We present SpexPay, a privacy-preserving and auditable pay-as-you-go spectrum usage framework that enforces fine-grained, usage-linked payments without revealing user identities. Spexpay integrates BBS+ verifiable credentials, unlinkable session pseudonyms, and selective-disclosure proofs to enforce privacy-preserving access authorization, while leveraging Solidity-based smart contracts to realize automated and non-repudiable escrow settlement. By recording only pseudonymous usage evidence and hash-chained metering data on-chain, the system achieves strong unlinkability while preserving verifiable accountability and auditability. A full prototype demonstrates low end-to-end latency ($\approx$150 ms) and modest on-chain cost ($\approx$603K gas or $\approx$\$0.9), showing that SpexPay is practical for real-world DSS deployments. We also evaluated the user-side cryptographic operations on a Raspberry Pi 5 to assess scalability and suitability for edge-class hardware. Our code and artifacts are publicly available at this https URL.

---


### 206. [Semantic Context Matters: Analysis of Color Names Across Domains](https://arxiv.org/abs/2607.17221)

**<font color=#1a73e8>作者：</font>** Adilet Yerkin, Elnara Kadyrgali, Malika Ziyada 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Color naming is influenced not only by physical color values but also by the semantic context in which colors are used. This paper investigates context-dependent color naming by mapping color-name datasets from Cosmetics, Crayola, and Car-color vocabularies onto the 86 fuzzy color categories of the COLIBRI color model. Contextual variation is analyzed using category coverage, Shannon entropy, and maximum lift. The results show that the three contexts occupy the COLIBRI color space differently: Cosmetics covers 48 of 86 fuzzy categories, Crayola covers 50, and Car colors cover 40. The results demonstrated that Crayola provides the broadest and most balanced use of the fuzzy color space, Cosmetics is mainly concentrated around warm-tone regions, and Car colors are more specialized around blue and achromatic regions. These findings show that color naming cannot be fully explained by numerical color similarity alone and that semantic context plays an important role in human color interpretation. The proposed framework supports the development of context-aware color models for design analytics, product search, recommendation systems, and human-centered artificial intelligence.

---


### 207. [Robust Summarization of Doctor-Patient Conversations: TalTech Systems for the Beyond Transcription Challenge](https://arxiv.org/abs/2607.17230)

**<font color=#1a73e8>作者：</font>** Aivo Olev, Tanel Alumäe  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper describes TalTech's submissions to the Beyond Transcription Challenge (BeTraC), which requires generating SOAP notes directly from long doctor-patient conversation recordings, without intermediate transcription. After screening open-weight speech LLMs for long-audio robustness, we adapted Voxtral Mini (lightweight track) and Voxtral Small (heavyweight track) with LoRA supervised fine-tuning followed by DAPO reinforcement learning that uses the challenge metric, Open Medical Concept F1, as its reward. Our systems ranked first in both tracks, and an independent LLM-as-a-judge evaluation showed the lowest hallucination rate among all submissions, indicating that reinforcement learning against a concept-matching metric need not compromise factual reliability. We also find that fine-tuning on text transcripts transfers well to speech input and appears to improve robustness on out-of-domain real recordings.

---


### 208. [AI_LectureNote: A Retrospective Pilot Study of a Post-ASR Workflow for English-Script Rendering and Semantic Drift in Korean-English Medical Lectures](https://arxiv.org/abs/2607.17237)

**<font color=#1a73e8>作者：</font>** Kyeongeon Lee, Donghoon Chang, Seungryeol Baek 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI_LectureNote is a historical, readability-oriented post-ASR workflow for Korean-English medical lectures. It rewrites speech-to-text output into study transcripts while restoring Latin-script medical terms rather than Korean phonetic transliterations. We retrospectively evaluate the workflow on four author-recorded lectures across five conditions. In this pilot, post-processing raised the macro English-script rendering rate from 0.39 to 0.71 on the whisper-1 path and from 0.26 to 0.65 when applied to 3-minute chunked gpt-4o-transcribe output. However, English-script rendering did not imply semantic faithfulness: the two post-processed conditions showed semantic drift in 34 and 36 of 282 reference sentences and polarity failures in 11 and 13 of 101 polarity-cue rows. A descriptive cross-input comparison suggested different candidate failure patterns: polarity-failure sets overlapped more strongly across front-ends (Jaccard 0.60; 9 shared of 15 unioned failures) than general semantic-drift sets (Jaccard 0.23; 13 shared of 57 unioned drifts). This single-annotator pilot documents concrete failure modes rather than population rates and supports evaluating surface accuracy, term-script rendering, chunk-level script consistency, and medical-meaning preservation separately.

---


### 209. [Constrained Path Reasoning: Measuring When Committed Stages Earn Their Cost](https://arxiv.org/abs/2607.17240)

**<font color=#1a73e8>作者：</font>** Honglin Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When does a committed intermediate stage in an LLM reasoning pipeline earn its cost? Constrained Path Reasoning (CPR) pairs a source-aware path hypothesis with stage-level accounting. Search generates provisional states; trusted or validated invariants can constrain hard, while other proposals remain soft and revisable. CPR predicts that task-compatible commitments can factor transitions, concentrate candidate mass, induce regularity, and expose feedback when their gains exceed propagated error and execution cost. The formalism covers discrete commitments and continuous flows and measures effective branching, endpoint concentration, and cost per usable output. Across 1,180 generated QCQPs and 40 engineered degenerate polynomial instances (2,140 endpoints), residual triage recovers 63.0% of repair-all's additional feasible yield with 17.7% of its attempts. Fixed-LLM accounting (270 unique calls shared across nested arms) finds usable yield of 41.1% direct, 90.0% after formalization and deterministic execution, 20.0% after one-shot convexification, and 21.1% for the full path. In 120 paired-condition calls, a two-action rollback rule reaches 90% usable yield versus 36.7% for the feedback-conditioned selector. Two endpoint probes separate source from validation: a 72-output cross-trajectory transplant reduces entropy and acceptable mass; a 24-output same-call self-proposal pilot gives unchanged two-repeat collision entropy, 25.0% versus 8.3% usable yield, and 1/8 deterministically confirmed endpoint checks. Model-generated states supply hypotheses; trusted execution earns constraint strength.

---


### 210. [LenGuard-GPC: Length Guarding with Guided-Prompt Consistency for Spatial Reasoning Reinforce Learning](https://arxiv.org/abs/2607.17243)

**<font color=#1a73e8>作者：</font>** Xingjian Tao, Yiwei Wang, Yujun Cai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-view spatial reasoning requires vision-language models to compare visual evidence across images, align object correspondences, and infer spatial relations over long visual contexts, a setting where chain-of-thought reasoning tends to grow verbose without becoming more accurate. Reinforcement learning with verifiable rewards is a natural fit for this task, but standard GRPO reward relies on sparse outcome-level feedback and gives no signal about where a reasoning trajectory goes wrong, nor any control over its length. We propose LenGuard-GPC, a dense reward framework that addresses both problems together. For each sampled trajectory, it compares the token-wise predictive distributions under a standard prompt and a guided prompt, and uses the resulting token-sum KL divergence as a dense reward signal. Since this KL penalty accumulates over tokens and would otherwise reward shorter responses regardless of their quality, we introduce a staged length bonus that keeps reasoning length within a controlled range without simply encouraging brevity. On six multi-view spatial reasoning benchmarks, LenGuard-GPC improves accuracy over vanilla GRPO while reducing average response length.

---


### 211. [DynImmune-BERT: Dynamic Immune Repertoire Modeling with Neural ODE Driven Continuous Transformers](https://arxiv.org/abs/2607.17244)

**<font color=#1a73e8>作者：</font>** Rong Fu, Yongtai Liu, Xiaowen Ma 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Longitudinal T cell receptor repertoires contain signals of clonal expansion, contraction, disappearance, and reappearance after immune perturbation. Static repertoire language models usually summarize a sample as a bag of sequences, so the sampling interval, sequencing depth, and clone presence pattern are only weakly represented. This paper presents DynImmune-BERT, a continuous time repertoire model for patient level immune status prediction. The method combines depth adaptive centered log ratio initialization, clone presence gated Neural ordinary differential equation dynamics, bounded neighborhood self attention, event based state restart, and a hybrid transport objective that supervises dominant and rare clone mass. A low rank meta adapter initializes reappearing clonotypes while keeping the parameter count independent of the number of observed clones. The evaluation separates literature reported baselines from internally controlled temporal comparisons, reports uncertainty for small external cohorts, adds calibration and threshold diagnostics, and visualizes latent clone trajectories and attention neighborhoods. The results indicate that event aware temporal modeling can complement strong static encoders when longitudinal repertoire structure is available, while small external cohorts and protocol differences require cautious interpretation.

---


### 212. [Should Missing Modalities Always Be Necessary to Repair for Multi-modal Sentiment Analysis?](https://arxiv.org/abs/2607.17262)

**<font color=#1a73e8>作者：</font>** Yubo Gao, Haotian Wu, Xiaoyu Xu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing methods for multimodal sentiment analysis (MSA) under missing modalities usually follow a repair-first paradigm. We revisit this assumption and ask: \emph{should every missing modality be repaired?} A per-sample oracle analysis shows the answer is not always: full-modality input is optimal for only a small fraction of samples, and every modality subset is preferred by some samples. These results suggest that adding or repairing modalities may not always improve prediction, and that the utility of each modality is sample-dependent. Building on this finding, we propose \textbf{S}ufficiency-\textbf{I}nformed \textbf{E}vidential \textbf{V}al\textbf{vE} (\textbf{SIEVE}) that turns ``whether to repair'' into an explicit, learnable decision at the sample level. SIEVE compares a direct prediction branch with a repair branch, derives an empirical sufficiency signal from their per-sample loss gap, and routes each input through an evidential gate that jointly models sufficiency and its epistemic uncertainty. SIEVE is repair-agnostic: it operates as a plug-and-play decision on top of any explicit or implicit repair module, without modifying its internal design. Experiments on CMU-MOSI and IEMOCAP show that SIEVE consistently improves representative repair backbones across evaluated missing rates, and approaches the per-sample dual-branch achievable optimum.

---


### 213. [Coordinated Disentanglement with Iterative Mode Discovery Under Hidden Correlations](https://arxiv.org/abs/2607.17264)

**<font color=#1a73e8>作者：</font>** Rong Hu, Ling Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Disentangled representation learning is a powerful paradigm for robust attribute prediction. While recent methods address attribute correlations, hidden correlations remain underexplored, where data under the value of a certain attribute exhibit underlying modes correlated with other attributes. To preserve mode information and achieve disentanglement, we jointly discover modes and enforce mode-based conditional independence. Yet, the interdependency between these two modules may lead to error amplification under naive iterations. We propose Coordinated Disentanglement with Iterative mode Discovery (CoDID), an end-to-end framework featuring a dynamic architecture that adapts to evolving number of modes, and a coordination mechanism that mitigates error amplification via meta-optimization. Empirical results demonstrate the state-of-the-art performance on diverse tasks.

---


### 214. [PACE: Polar Axis-Conditioned Estimation for PairUAV Relative Localization](https://arxiv.org/abs/2607.17268)

**<font color=#1a73e8>作者：</font>** Ze Rong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> PairUAV relative localization maps two UAV images to a polar navigation command. Although heading and range share the same pairwise pose context, treating them as homogeneous coordinates forces both outputs to use the same decoder evidence and optimization state. Controlled readout probes reveal a different structure: the two axes favor different decoder-depth combinations, their best checkpoints disagree on 80.8% of a validation trajectory, and range errors exhibit a distinct high-error tail. We introduce method, Polar Axis-Conditioned Estimation, which retains a shared Reloc3r-style pair representation while assigning axis-specific readout interfaces. Heading uses mid/late relational evidence, whereas range remains attached to a direct late metric path. On the official hidden test, the strongest released raw predictor scores 0.002460; the complementary PAAER predictor scores 0.002514 with a slightly lower angle error. Deterministic challenge packaging, reported separately from learned estimation, yields the final score of 0.001874. Code, checkpoints, predictions, and reconstruction tools are available at this https URL.

---


### 215. [Node4All: Learning Node Representation Beyond Datasets](https://arxiv.org/abs/2607.17272)

**<font color=#1a73e8>作者：</font>** Dooho Lee, Jaemin Yoo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Node representation learning has advanced rapidly, yet most existing methods rely on per-dataset training and hyperparameter tuning. This dataset-specific optimization comes from the difficulty of designing reusable graph models that generalize across diverse graph datasets. In this work, we introduce Node4All, a node representation learner applicable to arbitrary graph datasets without any dataset-specific optimization.
Node4All is built on two complementary ideas. At the architectural level, we introduce the Channel Graph Transformer (CGT), which enables a single fixed parameterization to process arbitrary graph datasets. At the learning level, we propose a self-supervised learning based on a series of synthetic graphs. Together, these components enable generalization beyond individual datasets, which is infeasible with existing architectures and learning frameworks. We extensively evaluate Node4All on node classification across 25 benchmarks against 21 baselines, covering both supervised and self-supervised methods. Despite all baselines being trained and optimized for each dataset, a single Node4All, applied uniformly across the datasets, achieves a competitive ranking of 5th among 21 baselines. Moreover, Node4All supports one-shot and in-context learning with an appropriate predictor and outperforms recent graph foundation models (GFMs) in these settings. These results demonstrate that Node4All not only achieves reusability across arbitrary graph datasets, but also remains an effective solution in practice. Code and model checkpoints are available in this https URL.

---


### 216. [Between Safe Boundaries: Exploiting Temporal Consistency for Jailbreaking Text-To-Video Generation Models](https://arxiv.org/abs/2607.17279)

**<font color=#1a73e8>作者：</font>** Xingkai Peng, Jun Jiang, Jiayang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recently, text-to-video (T2V) models have been widely deployed, sparking growing concerns over their robustness against jailbreak attacks. Existing jailbreak methods, mostly adapted from text-to-image attacks, suffer notable drawbacks when applied to T2V systems. They fail to fully leverage temporal consistency, an inherent characteristic of video generation. Besides, these methods demand heavy video query optimization, which is infeasible in practical black-box scenarios. Their adversarial prompt search is also driven by heuristic local signals, lacking principled structured exploration strategies. To tackle these limitations, we propose BSB, a structured, query-efficient jailbreak framework for T2V models. BSB harnesses temporal consistency by encoding harmful intent as the transition between two individually harmless boundary states. Under this paradigm, the attack targets boundary-state pairs whose interpolation tends to produce unsafe intermediate frames during video generation. Directly evaluating all candidate pairs within the video space incurs prohibitive computation cost. Instead, BSB conducts Monte Carlo Tree Search (MCTS) in a cheaper textual proxy space and regularly calibrates search outcomes with sparse video-level evaluations. We conduct comprehensive experiments on mainstream commercial T2V models including Veo 3.1, Sora 2, Seedance and Kling v1. Results show BSB surpasses all existing jailbreak baselines, delivering an average 18.6% relative gain in attack success rate over the strongest competitor across evaluated models. Our findings identify temporal consistency as an understudied yet vital attack surface for T2V models and verify that structured search facilitates effective vulnerability discovery under constrained query budgets.

---


### 217. [An Iterative Geometric Approach to Optimizing Separating Hyperplanes](https://arxiv.org/abs/2607.17282)

**<font color=#1a73e8>作者：</font>** Akos Hajnal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Given a binary-labeled linearly separable dataset, and the objective is to compute the maximum-margin separating hyperplane, also known as the hard-margin Support Vector Machine (SVM) classifier. This paper investigates whether, if given an initial separating hyperplane, can it be exploited to reach this unique optimum more efficiently. We present a geometric approach that gradually improves the alignment of the hyperplane, starting from an initial separating hyperplane, while preserving separation and continuously increasing its margin until convergence to the global optimum. At each iteration, the method considers only local information, namely the current active set, and aims to re-align the hyperplane according to the optimal separating hyperplane of this reduced subset. Consequently, the original convex quadratic optimization problem is addressed through a sequence of smaller subproblems. The paper presents the algorithm in detail, together with a preliminary experimental evaluation and several theoretical findings. The results suggest that, when an initial separating hyperplane is available, the proposed method can be competitive on larger datasets and, in some cases, can outperform state-of-the-art approaches that solve the optimization problem directly.

---


### 218. [Lossless but Not Free: An Empirical Anatomy of Speculative Decoding on Consumer Hardware](https://arxiv.org/abs/2607.17283)

**<font color=#1a73e8>作者：</font>** Param Chordiya  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Single-stream autoregressive decoding of large language models is bound by memory bandwidth: each generated token requires one full forward pass through the target model, and successive passes cannot be parallelized. Speculative decoding restructures this computation: a small draft model proposes $K$ tokens autoregressively, the target model scores all of them in one batched pass, and a rejection-sampling rule provably preserves the target model's output distribution. We present a from-scratch, device-agnostic (CUDA/MPS/CPU) implementation and an empirical study across five draft/target backend configurations on a consumer Apple-silicon laptop. Distribution equivalence is verified at three levels, culminating in a two-sample test over roughly 9,200 real-model tokens per method ($\chi^2 = 162.5$, dof $= 200$, $p = 0.976$) and exact greedy-sequence agreement. The best configuration reaches a measured $1.61\times$ wall-clock speedup at $K=6$, on an acceptance profile declining from 69.7% at $K=1$ to 37.8% at the optimum, while three of five configurations decelerate, either because the draft fails to out-speed a small target or because the quantized Metal backend executes "parallel" verification serially, an effect we isolate and quantify. The failures are as instructive as the successes: speculative decoding pays off only when verification is genuinely batch-parallel and the draft/target latency gap is real.

---


### 219. [Lookahead Branching for Neural Network Verification](https://arxiv.org/abs/2607.17290)

**<font color=#1a73e8>作者：</font>** Liam Davis, Duo Zhou, Huan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we investigate the effect of lookahead branching strategies in neural network verification. We present a general recipe to integrate lookahead into any branch-and-bound verifier and demonstrate how one of the current state-of-the-art branching heuristics, FSB, can be viewed as a special instantiation of the lookahead branching strategy. We also describe how, in addition to improving the quality of branching decisions, lookahead can generate additional lemmas that accelerate verification. We instantiate the method in two representative branch-and-bound-based verifiers (Marabou and $\alpha$-$\beta$-CROWN), and demonstrate that lookahead leads to consistent speedups in verification time and up to $57\%$ more solved instances. Code is available at this https URL.

---


### 220. [DRNOISE: Benchmarking Deep Research Agents in Misleading Evidence Environments](https://arxiv.org/abs/2607.17291)

**<font color=#1a73e8>作者：</font>** Jun Nie, Zhiqin Yang, Zhenheng Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep research agents increasingly operate over the open web, where relevant records coexist with redundant summaries, outdated reports, and misleading documents. Existing evaluations offer limited insight into whether agents preserve sound evidential standards when an ordinary-looking false document is deliberately seeded into a searchable environment and offers a direct shortcut to a conflicting answer. We introduce DRNOISE, a 100-task benchmark for answer recovery under misleading evidence. Each task has a unique gold answer supported by two corroborating indirect record chains; the paired noisy condition adds one plausible document that states a conflicting answer directly. The benchmark spans ten families of evidence operations. Across agents with strong clean-task performance, this single intervention causes 66-88 percentage-point accuracy drops. Trace analyses identify verification inertia as the dominant failure mode: agents often retrieve truthful records but stop before completing and reconciling the evidence chain, instead deferring to the answer-like document. Generic verification prompts reduce but do not close this gap. The setting is especially relevant to open-web deployment, where plausible falsehoods arrive through ordinary-looking pages rather than explicit attacks. Reliable deep research therefore requires more than retrieval and citation; it requires active reconciliation of direct claims with record-level evidence.

---


### 221. [Learning-Driven Adaptive Audit Scheduling: A Sequential Decision Approach to Off-Chain Data Integrity](https://arxiv.org/abs/2607.17305)

**<font color=#1a73e8>作者：</font>** Changting Lin, Fan Li, Weihang Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We model cryptographic auditing of off-chain data as a Constrained MDP (CMDP) under partial observability: the storage node's hidden type and corruption state make the problem a POMDP, while a miss-rate ceiling rho imposes an explicit security constraint. We propose DRQN-CMDP, a Deep Recurrent Q-Network whose GRU layer maintains a belief over the latent node type, paired with Lagrangian dual ascent that adapts the miss-rate penalty lambda automatically. A pairing-free homomorphic-MAC primitive supplies O(1) on-chain verification cost. Across 13 methods--four DQN variants, PPO, A2C, PPO-Lagrangian, a stateful Bayesian heuristic, three fixed-rule baselines, and an oracle-informed heuristic--DRQN-CMDP achieves a favourable balance: 83% lower gas than fixed high-frequency auditing, single-digit miss rate (7.5%), and moderate detection latency--a combination no other method matches across all three objectives simultaneously.

---


### 222. [The Optimization Trilemma: Efficiency, Comfort and Fairness in Decentralized Multi-agent Coordination](https://arxiv.org/abs/2607.17311)

**<font color=#1a73e8>作者：</font>** Jovan Nikolic, Maciej Krzysztof Zuziak, Evangelos Pournaras  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The problem of fair multi-agent coordination in decentralized settings is one of the most pressing challenges for building efficient collaborative systems. Resource allocation is based on optimized collective arrangements accounting for agents' needs. Such coordination should not only be computationally efficient but also account for fairness, i.e., equitable redistribution of costs incurred by all agents. Recent literature has proposed several algorithms that efficiently determine optimal plan combinations balancing system-wide efficiency and individual discomfort of agents in a centralized setting. However, these works do not address equitable resource optimization in fully decentralized scenarios, specifically, the optimized redistribution of discomfort among coordinating agents so that none experiences a discomfort level that could lead to loss of incentive or polarization that can disrupt planned operations. In this work, we study the problem of optimizing three objectives: (i) system-wide efficiency, (ii) individuals' comfort and (iii) fairness (i.e., balancing of incurred discomfort costs) in decentralized multi-agent coordination. We design a novel model to optimize those three orthogonal objectives, without any substantial increase in communication and computational overhead. Through experiments on two real-world datasets, we validate the model and demonstrate that it can achieve fairer optimization outcomes, while satisfying agents' preferences and system goals.

---


### 223. [Rationalizing Boltzmann Rationality: An Axiomatic Characterization of Entropy-Regularized Policies](https://arxiv.org/abs/2607.17316)

**<font color=#1a73e8>作者：</font>** Silviu Pitis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The softmax policy $\pi(a \mid s) \propto \exp(\beta Q(s,a))$ is the default model of stochastic choice in reinforcement learning (RL). Various justifications based on robustness, exploration, and optimization have been offered in the RL literature, but none uniquely derives the softmax form from first principles. This leaves a basic tension unresolved: the entropy bonus in the soft Bellman equation violates the Independence axiom that underwrites the Markov decision process (MDP) reward structure. We dissolve this tension by distinguishing two kinds of randomness: chance and choice. By restricting von Neumann-Morgenstern (VNM) Independence to environmental lotteries over base prospects, we show that imposing independence of irrelevant alternatives (IIA) and monotonicity on the policy and value functions at choice nodes uniquely determines the Boltzmann policy, the entropy-regularized representation, and the soft Bellman equation. The choice between the soft and hard Bellman equations thus reduces to a design decision: whether the agent values its own ability to choose. We develop RL-specific consequences, including return monotonicity and convergence under generalized discounting, and synthesize the independent lines from economics and information theory that arrive at the same structure, offering a normative assessment of when IIA is appropriate for agent design.

---


### 224. [TAPAS: Throughput-adaptive Perception for Autonomous Systems](https://arxiv.org/abs/2607.17317)

**<font color=#1a73e8>作者：</font>** Aman Vyas, Vasista Kodumagulla, Zain Taufique 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autonomous systems rely on a perception module to navigate through dynamic environments. In real-world scenarios, the perception module's throughput requirements vary at runtime due to changes in scene complexity. However, existing perception strategies assume a fixed FPS and static model-to-cluster mapping, resulting in either over/under provision of throughput requirements or unnecessary energy consumption across diverse scenes. Addressing this challenge requires tightly coupled \textit{scene complexity awareness} to estimate an appropriate FPS target and \textit{dynamic model-to-cluster mapping} to deliver the required throughput at minimum energy. We propose a throughput-adaptive perception strategy for mobile/edge platforms, enabling intelligent runtime resource allocation based on varying FPS targets. We use Reinforcement Learning (RL) with RRM (Reward Reasoning Model) and a GRU (Gated Recurrent Unit) agent to orchestrate perception tasks across heterogeneous mobile/edge platforms. We evaluate TAPAS on Jetson Orin NX across KITTI and unseen nuScenes. On the \textit{KITTI} dataset's test sequences, TAPAS achieves 93-100% throughput met rate while saving energy by 76%. On the unseen \textit{nuScenes} dataset, TAPAS maintains 97% throughput met rate with 64% lower energy compared to \textit{SOTA} approaches, proving its robustness.

---


### 225. [Rethinking the Suitability of Reinforcement Learning Algorithms Under Practical Transfer Constraints](https://arxiv.org/abs/2607.17326)

**<font color=#1a73e8>作者：</font>** Hany Hamed, Abhishek Naik, Colin Bellinger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transfer-oriented reinforcement learning requires evaluating algorithms along dimensions that go beyond standard sample efficiency. We focus on two dimensions: practical efficiency, which asks whether conclusions about algorithm suitability change under wall-clock rather than interaction-based budgets, and robustness under dynamics mismatch, which asks how different learning paradigms respond to variability in the training distribution induced by domain randomization. We provide two insights to reinforcement-learning practitioners. First, comparing the sample efficiency of different algorithms is often an insufficient criterion in transfer-oriented settings. The wall-clock time required to train a decent policy is an important consideration for practitioners, and we find that the sample-inefficient PPO algorithm can produce a performant policy faster than relatively more sample-efficient algorithms such as SAC and TD-MPC2, validating the common understanding of massively parallel training paradigms. Second, domain randomization can help different kinds of algorithms learn robust policies. In particular, although PPO, SAC, and TD-MPC2 represent different RL paradigms - on-policy, off-policy, and model-based learning and planning, respectively - we find that domain randomization affects all three algorithms in a similar way. To the best of our knowledge, this is the first controlled comparison of the effect of domain-randomization coverage on PPO, SAC, and TD-MPC2 under the same transfer protocol. Taken together, these two insights highlight the importance of evaluating RL algorithms not only by sample efficiency, but also by practical considerations such as training time and the algorithms' ability to produce usable policies.

---


### 226. [Physical Time-Lock Puzzles](https://arxiv.org/abs/2607.17328)

**<font color=#1a73e8>作者：</font>** Niloufar Sayadi, Chenglu Jin, Phuong Ha Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Traditional time-lock puzzles enforce delayed access to encrypted secrets by relying on inherently sequential computational steps. However, since software-based constructions impose no fundamental bound on the physical execution speed of individual steps, they remain vulnerable to hardware acceleration and improved implementations. In practice, this renders existing schemes ``step-lock'' rather than true ``time-lock'' puzzles, making long-term delay guarantees highly speculative against decades of unpredictable hardware advancement. To address this fundamental limitation, we introduce the Physical Time-Lock Puzzle (P-TLP), a new paradigm that anchors solving delay directly to the intrinsic, hardware-bounded evaluation latency of silicon hardware. By leveraging noisy Physical Unclonable Functions (PUFs) as non-parallelizable delay oracles, P-TLPs establish resistance against both parallel computation and algorithmic acceleration under the random oracle model. To tolerate PUF evaluation noise while maintaining a tightly concentrated and predictable solving-delay window, we propose a composite puzzle architecture that combines multiple independent basic puzzles. We formally prove the optimality of a sequential greedy solving strategy and derive tightly concentrated solving-delay windows using Hoeffding and Berry-Esseen bounds. We additionally prove early-solve hardness, establishing that adversaries with substantial classical computation budgets cannot bypass the physically-enforced PUF evaluation bottleneck. We validate our theoretical analysis with an FPGA prototype built around a configurable Ring Oscillator PUF, confirming that our analytical delay predictions tightly match empirical measurements. Our results demonstrate that P-TLPs can deliver highly predictable, long-term delay guarantees, enabling practical deployment in high-value applications such as digital legacy management.

---


### 227. [MIS-HCC: Hierarchical Channel Clustering for Efficient Medical Image Segmentation](https://arxiv.org/abs/2607.17329)

**<font color=#1a73e8>作者：</font>** Bo Zhao, Haoran Yu, Lifei Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image segmentation models require both high accuracy and lightweight design to accommodate real-world medical applications. The deployment of these models on resource-limited medical platforms remains a significant challenge due to their high computational and parameter requirements. Existing pruning methods for model compression mostly overlook the intrinsic connections and similarity between the internal structures of complex deep neural networks. As a result, compressed models may not effectively retain the basic features of the pretrained network. To solve this problem, we propose a hierarchical clustering compression method for medical image segmentation models (MIS-HCC). This approach employs hierarchical clustering to partition channels and fuse their parameters efficiently. Specifically, it leverages the Wasserstein distance to represent similarity of channels within layers of pre-trained network, forming a similarity matrix that guides the clustering process. Channels within each cluster are then fused to produce a compressed network. Experimental results on three medical image datasets application demonstrate that MIS-HCC outperforms the state-of-the-art methods in both accuracy and compression efficiency, offering an effective solution for deploying medical image segmentation models on resource-limited medical platforms.

---


### 228. [When Drift Detectors cry Wolf: False Alarm Rates in continuous ML Monitoring](https://arxiv.org/abs/2607.17336)

**<font color=#1a73e8>作者：</font>** Raj Shekhar Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Drift detection is a core component of production machine learning monitoring systems, where detectors are used to compare incoming data with a reference distribution and trigger alerts when changes occur. However, these detectors are often evaluated in research settings that emphasize detection accuracy under synthetic shifts, while overlooking false alarms under continuous monitoring. In production environments, models are monitored repeatedly over time and across many features, and even small false positive rates can accumulate into frequent alerts, leading to alarm fatigue. We empirically analyze false positive behavior across five commonly used drift detectors: PSI, KS, MMD, LSDD, and adversarial validation. Consistent with existing literature, PSI exhibits strong sensitivity to batch size, producing frequent false alarms at small sample sizes; however, we further observe that its behavior stabilizes and improves substantially once batch sizes exceed approximately 200 samples. In contrast, KS, MMD, and LSDD display persistent fluctuations across batch sizes, while remaining comparatively more reliable than PSI in low-data regimes. Applying a Bonferroni correction reduces false positive rates, but often at the cost of reduced true positive sensitivity, reinforcing the well-known stability - sensitivity trade-off in drift detection. This work provides a systematic comparison of false positive behavior across multiple drift detectors under continuous monitoring conditions. We identify tradeoffs across detector families and provide practical guidelines for selecting and calibrating drift detectors in production ML systems.

---


### 229. [Orthogonal Knowledge Refreshing for Domain-Incremental Object Detection](https://arxiv.org/abs/2607.17340)

**<font color=#1a73e8>作者：</font>** Aoting Zhang, Dongbao Yang, Chang Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Domain-incremental object detection (DIOD) requires models to continually adapt to new domains while preserving prior knowledge. Recently, parameter-efficient fine-tuning offers a promising avenue, wherein a pre-trained model is frozen and a small number of learnable parameters are injected for downstream tasks. However, these methods risk overwriting critical past knowledge, triggering inter-domain interference and performance degradation. To address this challenge, we propose Orthogonal Knowledge Refreshing (OKR), a simple yet effective framework for DIOD. OKR incrementally constructs independent domain-specific subspaces via dedicated low-rank branches for each domain, which are seamlessly fused for a holistic decision, enabling conflict-free capacity expansion without domain selection during inference. To minimize knowledge interference during fusion, we present a gradient-based orthogonal refreshing strategy that projects gradient updates of new domains onto the orthogonal complement of the fused historical subspace, supporting continual adaptation without forgetting. Moreover, to mitigate semantic fragmentation across domains, we enforce topology-aware consistency, aligning the semantic structures of old and new domains. Extensive experiments validate the superiority of OKR, outperforming the best exemplar-free method by significant margins of +5.6% and +6.5% mAP on the Pascal VOC and BDD100K series, respectively.

---


### 230. [Understanding From Human Perspective: A Multi-agent System for Interactive Egocentric Medical Image Segmentation](https://arxiv.org/abs/2607.17341)

**<font color=#1a73e8>作者：</font>** Rongjun Ge, Dongyang Wang, Heng Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive egocentric medical image segmentation (IEMIS) plays an important role in smart-glasses-assisted medical image review, segmenting the medical targets a clinician refers to from their egocentric view. Once it succeeds, the object-level visual evidence it provides strengthens the review and underpins fine-grained analysis and clinical decision-making. However, the instruction and the video both come from the user's egocentric perspective, which poses two challenges. (1) Semantic ambiguity leaves the model unable to confirm the user-intended target. (2) Visual variability makes the segmentation jump from frame to frame. In this paper, we propose EgoMed-Agent, a multi-agent system that understands the target from the human perspective through two workflows. (1) The \textit{Target Confirmation Workflow} grounds the instruction against candidate targets with a reliability score, confirming the target when the grounding is reliable and asking the user to clarify when it is not, thereby confirming the segmentation target. (2) The \textit{Localization-Guided Propagation Workflow} couples mask propagation with per-frame target localization, using the localized target to correct the propagated mask whenever the two diverge, so the segmentation stays on the target across the egocentric video. Extensive experiments show that EgoMed-Agent reaches 71.34\% average Dice, far above the best text-prompted baseline (11.70\%). Our code is available at \href{this https URL}{our project page}.

---


### 231. [A multiverse-consensus pipeline for reproducible feature selection in untargeted LC-MS metabolomics](https://arxiv.org/abs/2607.17345)

**<font color=#1a73e8>作者：</font>** Mohammed Saeed Al-Huraibi, Ihsan Yozgat, Ahmet Kaplan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Background: Untargeted LC-MS metabolomics requires a long chain of preprocessing decisions, each with several equally defensible options. Analysts typically commit to one pipeline and report the resulting feature shortlist. How strongly that shortlist depends on choices that were never varied stays invisible. Results: We adapt multiverse analysis to untargeted metabolomics feature selection. We present an auditable, configuration-driven pipeline that (i) applies a ten-stage quality-control filter cascade in which every feature's fate is logged, and (ii) runs the downstream analysis as a multiverse over four contrasting preprocessing philosophies, each combined with four feature-ranking methods under bootstrap stability selection and label-permutation testing. Only features recurring across paths enter a tiered consensus. On a demonstration dataset of five breast-cancer cell lines (30,370 detected features), the four single pipelines individually returned shortlists of 4-20 features whose pairwise agreement was as low as Jaccard = 0.05. The multiverse consensus retained 15 features (>=2/4 paths), of which one recurred across all four, although two paths (sharing normalization and drift-correction methods) dominate the consensus. A pipeline-wide label-permutation test found no false discoveries in 50 null permutations. Conclusions: Reporting only preprocessing-robust features, with a complete kept/dropped audit trail, converts hidden analytical degrees of freedom into an explicit, inspectable output. We discuss scope and limitations, including single-batch design and the need for independent validation.

---


### 232. [DeeperRadar: End-to-End MIMO Radar Design and Multi-Modal Fusion for Autonomous Vehicle Perception](https://arxiv.org/abs/2607.17351)

**<font color=#1a73e8>作者：</font>** Eli Goldenshluger, Barak Pinkovich, Chaim Baskin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> DeeperRadar is a radar-centric, sensor-stack-conditioned framework that co-designs radar sensing and multi-modal 3D detection for autonomous mobility by learning a sparse acquisition pattern end-to-end with the fusion model. A learnable MIMO design module is trained end-to-end within a fusion network that operates directly on raw radar ADC data together with camera images and LiDAR point clouds. During training, the design module is supervised by the other sensors, enabling the system to learn both which receiver antennas to activate and the effective number of them. At deployment, the design module is removed and replaced by the learned sparse subsampling mask, leaving the downstream model architecture unchanged. Evaluated on the RADIal dataset, DeeperRadar discovers sparse, task-aware radar configurations that match or exceed full-array baselines while using fewer receivers, potentially reducing radar cost and integration complexity. These results show that learned optimal MIMO radar design depends on the fusion stack and the downstream perception task.

---


### 233. [Self-Modifying Lean Proof Agents with Verifier-Grounded Benchmark Coevolution](https://arxiv.org/abs/2607.17352)

**<font color=#1a73e8>作者：</font>** Yuqing Li, Zeguan Wu, Yu Gan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Designing effective Lean proof agents is a central challenge in formal mathematical reasoning. Beyond building stronger provers, recent work emphasizes the workflow around Lean: how an agent decomposes proof obligations, uses tools and compiler feedback, diagnoses failures, repairs proofs, and maintains structured proof context. Motivated by code-level self-evolving agents, we study whether such workflows can be evolved rather than hand-designed. We present a self-evolving Lean proof agent in which a small fixed, trusted runtime wraps a fully mutable workspace: the proof workflow, prompts, and tools. Unlike most self-evolving systems, which optimize against a fixed external benchmark, our system coevolves the agent and its benchmark. Between generations, the highest-scoring agent (the champion) revises the active task distribution through a mastery-throttled curriculum update that introduces harder proof obligations only after the current level is mastered, and a single-anchor recalibration re-runs the champion on the updated benchmark to keep scores comparable as difficulty rises. All evolution stays inside a Lean-grounded verification loop: however the agent rewrites itself, a success counts only when its behavior yields Lean-verified proofs under a trusted snapshot, and each attempt must emit a machine-readable, Lean-grounded proof context whose representation may evolve but whose groundedness is enforced. We run the coevolving trajectory and a fixed-benchmark baseline for 15 active generations and compare them on a held-out miniF2F test split. The best coevolving agent reaches a 45.1% held-out solve rate, versus 12.7% for the seed and 32.0% for the best fixed-benchmark agent, showing that verifier-grounded self-evolution can improve Lean proof workflows under a coevolving benchmark.

---


### 234. [Chebyshev Manifold Adaptation](https://arxiv.org/abs/2607.17377)

**<font color=#1a73e8>作者：</font>** Jiawen Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The paper presents a new parameter-efficient adaptation method called ChebyMA (Chebyshev Manifold Adaptation). ChebyMA adopts weight matrices through a multi-surface superposition of Chebyshev polynomial bases evaluated on learnable coordinates and combined via trainable coefficient matrices, replacing standard linear projections with highly expressive continuous function approximation. Theoretically, we establish an Approximation Expressivity Theorem, proving from the perspective of function approximation theory that single-manifold ChebyMA guarantees convergence in Frobenius norm error of reconstruction. Besides, drawing on Kolmogorov $n$-width intuition, we demonstrate the expressive advantages of multi-manifold superposition ($S > 1$) in decoupling high-dimensional complex features. Experimental results on Computer Vision CIFAR datasets(CIFAR-10, CIFAR-100)\cite{CIFAR} and Natural Language Processing (AG News, SST-2) datasets demonstrate that ChebyMA consistently achieves a superior parameter-accuracy Pareto front compared to standard full-parameter fine-tuning, LoRA\cite{LoRA}, TLoRA\cite{TLoRA}, and StelLA\cite{StelLA}. ChebyMA significantly outperforms other tested methods in tested datasets, validating its solid theoretical foundation for generality with purely vectorized computations.

---


### 235. [Team DACTYL at PAN 2026: Bayesian Data Mixing and Empirical X-risk Minimization for AI-text Detection](https://arxiv.org/abs/2607.17382)

**<font color=#1a73e8>作者：</font>** Shantanu Thorat  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing research shows that AI-generated text detection classifiers achieve strong in-distribution (ID) performance but do not maintain the same performance on out-of-distribution (OOD) texts, suggesting overfitting to dataset-specific features. However, combining different training datasets doesn't always improve performance and, in some cases, can even encourage shortcut learning. To address this issue, we fine-tune BERT-tiny models with Bayesian classification heads to select texts across three different datasets to use as a consolidated training set. We trained three different classifiers: fine-tuned DeBERTa-V3-large and ModernBERT-large classifiers via empirical X-risk minimization, and an MCGrad model that calibrates the predictions from the ModernBERT-large classifier. The DeBERTa-V3-large-large classifier achieves a mean score of 0.882 on the PAN 2026 test set across five metrics: AUROC, $F_1$, C@1, Brier score, and $F_{0.5u}$. ModernBERT-large achieves a score of 0.96 while MCGrad achieves the best score of the three with a mean score of 0.974, ranking second on the leaderboard. Our results highlight that careful dataset curation can lead to strong OOD performance. We release our ModernBERT-large and DeBERTa-V3-large models at this https URL .

---


### 236. [Automating Visual Recognition of Leprosy in Wild Chimpanzees](https://arxiv.org/abs/2607.17395)

**<font color=#1a73e8>作者：</font>** Katie I. Murray, Anna C. Bowland, Marina Ramon 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Leprosy (Mycobacterium leprae) has been confirmed in wild western chimpanzees (Pan troglodytes verus) in West Africa, presenting as clear and progressive visual symptoms. Manual review of camera-trap footage at landscape scale is infeasible, motivating the need for automated screening. We present the first deep learning pipeline for wildlife leprosy detection and contribute the PanLep300 dataset of 125,670 annotated bounding-box crops across 953 tracks from 303 camera-trap videos with ecologically-motivated splits that withhold whole individuals and camera installations. We benchmark spatial (2D), temporally aggregated (2.5D), and video-based (3D) classification approaches to investigate which approach is best suited to automated leprosy detection in wild apes. We find that simple aggregation of crop-level predictions consistently matches or outperforms both learned temporal models and end-to-end video architectures -- consistent with leprosy's static cutaneous presentation. We further find that performance is suppressed when tracklets contain frames of partially visible individuals -- as commonly occurs at the start and end of a track -- and demonstrate that this can be addressed through targeted construction and aggregation strategies.

---


### 237. [The PanAf-SBR Dataset: Social Behaviour Recognition for Wild Great Apes](https://arxiv.org/abs/2607.17399)

**<font color=#1a73e8>作者：</font>** Maciej Braszczok, Otto Brookes, Xiaoxuan Ma 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Behavioural shifts in wild great ape populations, particularly the breakdown of social structures, can serve as an early indicator of population decline. Automating the detection of behaviours indicative of these shifts is therefore a critical task for conservation. Several valuable datasets have recently been introduced for the automated recognition of great ape behaviour, yet few include fine-grained social behaviour annotations, and those that do are captured either in captive settings or via aerial platforms such as UAVs. We address this gap by introducing PanAf-SBR, the first wild great ape camera trap dataset annotated with social behaviours. PanAf-SBR extends PanAf500 with 100 additional videos covering 36,063 frames. These come with 81,096 annotations including bounding boxes, segmentation masks, intra-video identities, and seven social behaviour classes defined under the action giver and receiver convention of ChimpACT. We use this data together with the AlphaChimp architecture to establish the first benchmarks for fine-grained social behaviour recognition in wild great apes from camera trap footage. We further conduct bidirectional transfer learning experiments between PanAf-SBR and the captive ChimpACT dataset, finding that cross-dataset pre-training is highly beneficial for specific classes rather than of uniform benefit. Finally, we examine the role of background context by inverting the segmentation masks to suppress non-ape pixels.

---


### 238. [Does Super-Resolution Preserve Defect Evidence? A Low-False-Call Benchmark for Semiconductor Inspection](https://arxiv.org/abs/2607.17401)

**<font color=#1a73e8>作者：</font>** Shaoliang Yang, Jun Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Super-resolution can make inspection images appear sharper without preserving the evidence needed to detect a defect. We study this failure mode with a benchmark that separates reconstruction from detection and evaluates both at a predeclared low false-positive rate. Ten end-to-end repetitions combine independently generated line/space and contact-hole images with model training, calibration, clean controls, weak defects, and a held-out defect morphology. Every reconstruction is scored by the same local residual detector, while direct and jointly trained detectors form a separate comparison track. Reconstruction fidelity and inspection utility diverge: the two learned reconstruction models attain the highest structural similarity yet detect fewer defect pixels than bicubic interpolation in every paired repetition. A direct DeepLabV3 detector reaches $0.1984\pm0.0385$ recall at $0.000174\pm0.000084$ false-positive rate and satisfies the held-out feasibility criterion in all ten repetitions. An illustrative joint model, DPU-WaferSR, passes independent clean calibration but exceeds the held-out limit in all ten repetitions, demonstrating that calibration success does not guarantee transfer. Weak-defect recall remains near zero for every feasible method. Applying the unchanged policies to 4,591 public Carinthia-S masks further reveals large method-dependent shifts on real SEM texture. These results support a simple conclusion: super-resolution for inspection should be judged by preserved task evidence and operating-point transfer, not reconstruction quality alone.

---


### 239. [CORAL: Learning Amyloid Fibril Ligand Docking with Cooperative Binding Rewards](https://arxiv.org/abs/2607.17412)

**<font color=#1a73e8>作者：</font>** Yasheng Sun, Bohan Li, Youqi Tao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A hallmark of neurodegenerative diseases such as Alzheimer's and Parkinson's is the aberrant aggregation of proteins into amyloid fibrils, and small molecules that selectively bind to these fibrils hold promise as diagnostics, imaging probes, and therapeutics. Predicting how such ligands bind to fibril targets, however, presents two fundamental challenges. First, resolved co-crystal structures of amyloid-ligand complexes are exceptionally scarce; even with recent advances in cryo-EM only a handful have been structurally characterized, making supervised training of docking models impractical for this target class. Second, amyloid fibrils present a binding mode fundamentally different from globular proteins: ligands intercalate into longitudinal cross-$\beta$ grooves and stack cooperatively along the fibril axis, a geometry that existing docking models are not designed to capture. To address these challenges, we present CORAL (COopeRative Amyloid Ligand docking), a reinforcement learning framework that trains a generative docking model to produce ligand pose distributions tailored to the cross-$\beta$ groove geometry. Our reward explicitly incorporates cooperative ligand-ligand stacking energy alongside protein-ligand docking affinity, directly capturing the distinctive binding geometry of amyloid fibrils. We further introduce a curated evaluation set of amyloid-ligand complexes constructed from model-generated poses validated by domain experts. Experiments on both experimentally resolved structures and this evaluation set demonstrate improved pose quality and binding affinity correlation over existing docking baselines.

---


### 240. [Grounded verification of chemical and materials reasoning: detection is the bottleneck](https://arxiv.org/abs/2607.17417)

**<font color=#1a73e8>作者：</font>** Can Polat, Mustafa Kurban, Erchin Serpedin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models confabulate chemical objects (molecular formulas, space groups, formation energies) in fluent reasoning traces, concentrated on long-tail entities where confidence is least trustworthy. Deterministic, database-grounded verification can catch and repair such errors without the coverage cost of blanket retrieval; the binding constraint, we find, is detection, not repair. Our tiered verifier extracts each checkable claim, checks it against authoritative databases and physics, and feeds the reference into a gated correction loop. Across four models and 528 condition-pinned prompts, gated correction cuts committed-formula error from 22% to 4% at $3.2\times$ fewer retrievals than blanket augmentation, beating a conversational oracle. Repair succeeds wherever a flag fires (80--97%); the bottleneck is in-loop detection recall. Grounding improves the final answer only when the verifier's scope reaches the deliverable (83% to 90%), and the lift appears only where extractable long-tail error exists: absent on near-ceiling physical constants, large on isotope half-lives (11% to 0%).

---


### 241. [Kernelized Linear Attention: Breaking the Capacity Wall with Symmetric Cones](https://arxiv.org/abs/2607.17419)

**<font color=#1a73e8>作者：</font>** Ayoub Ghriss, Sourav Chakraborty  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear attention promises constant-time recurrent inference but degrades sharply on associative recall. We formulate attention recall as a spherical-packing problem and introduce Kernelized Linear Attention Activations (KATA), a framework whose feature maps are derived from first principles by certifying nonnegative attention weights through a self-dual homogeneous cone. Building on this observation, we show that rank-one positive semi-definite (PSD) features offer a favorable capacity--interference tradeoff. KATA recovers a parameter-free convex output gate and characterizes associative capacity through the Welch interference floor. For tolerances above this floor, KATA enlarges the state without adding parameters and admits spherical codes with exponentially many keys in the projection dimension. We implement KATA as fused Triton kernels at two operating points: a flash-attention-style forward up to ${\sim}1.6\times$ FlashAttention-2 throughput, and an exact $O(T)$ chunked-state form that reaches ${\sim}11\times$ FlashAttention-2 forward throughput at $131$k tokens. An associative scan of the first-order feature lowers the inter-chunk recurrence depth to $O(\log(T/C))$ for chunk size $C$ and averages ${\sim}2.4\times$ the throughput of a matched sequential linear-attention baseline. On long-range MQAR and repeated-key overwrite, several KATA variants outperform Gated DeltaNet, with parameter counts and state sizes reported alongside accuracy. Induction preserves near-perfect recall, while kernel benchmarks show that the maps can be implemented efficiently. KATA retains $0.985$ MQAR at a $16\times$ out-of-distribution length, approaching the softmax with roughly one quarter of the KV-cache entries. Experiments on 340M-parameter LLMs reveal a feature-dependent fluency trade-off and clarify how positional embeddings, delta rules, and decay gates interact with feature geometry.

---


### 242. [Decoder-Preserving Sparse Autoencoders: Which Readouts Survive Sparse Compression?](https://arxiv.org/abs/2607.17425)

**<font color=#1a73e8>作者：</font>** Aniket Deshpande  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) compress model activations into sparse codes, but equal reconstruction error and sparsity can preserve different linearly decodable signals. We formalize this ambiguity as a matrix-valued distortion between optimal ridge-prediction operators and train decoder-preserving SAEs by combining this distortion with reconstruction loss. In a rank relaxation, an isotropic task prior saturates per-mode omission costs without changing PCA's ordering, whereas a structured prior can change which modes are retained. A controlled sparse experiment shows that a declared prior protects held-out combinations from its task subspace. On GPT-2 small block 8, DPSAE reduces held-out decoder distortion by 10.6--11.4% across three paired runs while matching reconstruction NMSE. The same checkpoints pass an average natural-text output-KL noninferiority test, but one matched Pythia pair shows no improvement in probes restricted to a few sparse features. These results show that reconstruction quality does not determine which refitted linear readouts survive sparse compression, and that readout preservation is distinct from learning cleaner benchmark concepts or preserving every frozen-model behavior.

---


### 243. [Abliteration Is Not a Scalpel: Off-Target Effects of Refusal Removal on Decision Disposition Across Model Families](https://arxiv.org/abs/2607.17427)

**<font color=#1a73e8>作者：</font>** Aleksander Fafuła  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Abliteration - deleting a model's refusal direction from its weights - is the standard recipe behind popular "uncensored" open-weight models. We show the surgery is not clean. As a disposition probe we use 21,600 decisions under uncertainty - weekly up/down calls on 60 Warsaw Stock Exchange equities over 18 weeks, replayed through a frozen pipeline so the decision-layer model is the only variable. The task elicits no refusals at all, so any between-arm delta is pure side effect. Holding provenance constant (official BF16 checkpoints, a single abliteration author, an identical serving stack, one byte-identical frozen prompt), we compare base and abliterated arms of two Mixture-of-Experts families, Gemma-4-26B-A4B-it and Qwen3-30B-A3B-Instruct-2507. Three effects replicate across both families (weeks-clustered bootstrap CIs excluding zero): abliterated models are systematically more optimistic (+12.2 pp Gemma, +7.4 pp Qwen; the confirmed preregistered endpoint), justify themselves at greater length, and use fewer explicit uncertainty words in forced self-critiques (both exploratory). A fourth effect reverses sign: the same operation makes Gemma-abliterated less confident and Qwen-abliterated more (family CIs non-overlapping) - one weight surgery, opposite shifts in expressed confidence. Capability covariates rule out instruction-following degradation as the driver, and no arm shows economic skill: the apparent edge of abliterated arms is regime beta, not alpha. Our provenance audit also caught two independent contamination channels - a mismatched-quantizer pilot pair and a stale community chat template that silently mangled the rendered prompt - suggesting toolchain artifacts are the rule in studies of community-modified checkpoints. Whoever deploys an "uncensored" model as an agent is deploying a measurably different decision-maker, not the base model minus refusals.

---


### 244. [Intermittent Control Is Not Diluted Control: A Switching Effect in Artificial Agency](https://arxiv.org/abs/2607.17432)

**<font color=#1a73e8>作者：</font>** Veronique Ziegler  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Adaptive agents do not always regulate under the same timing conditions. Sometimes stabilization can begin before a disturbance has fully entered the internal state; at other times the agent can only recover after disruption has taken hold. A simple expectation is that an agent moving between these conditions should behave like a weighted average of the two fixed cases: the more time spent in reactive recovery, the greater the regulatory burden.
This paper shows that expectation can fail. In a simulated adaptive agent with retained state history, at an operating point where sustained reactive control is more costly than sustained anticipatory control, intermittent access to anticipatory control reduces the mean regulatory burden below the value predicted by a fixed-mode mixture. The effect appears under both periodic and stochastic switching schedules: losing anticipatory access does not simply dilute its benefit, and restoring it intermittently can reorganize the later regulatory burden. High-statistics runs (N = 1000 matched replicates per schedule) resolve a negative nonlinear switching penalty across every tested schedule. The effect is small but consistent: about half a percent of the mean gain, with 63-68% of replicates falling below zero. Late-window diagnostics reveal no unresolved upward accumulation of regulatory burden.
The result identifies a design-relevant timing principle. In history-dependent adaptive systems, the burden of remaining organized is not set only by how much time an agent spends in each mode; the order in which disturbance and recovery enter the state can change the subsequent burden. Intermittent anticipatory control may therefore act less like a partial failure of regulation than like a mechanism for reducing the long-term burden of recovery.

---


### 245. [An Explainable FFT-Based Spatial-Frequency Fusion Framework for Deepfake Detection](https://arxiv.org/abs/2607.17441)

**<font color=#1a73e8>作者：</font>** Pamela Kirui, Cho Hyuk, Qingzhong Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deepfake generation has raised growing concerns regarding digital media authenticity, misinformation, identity fraud, and public trust. Recent studies show that combining spatial and frequency features leads to stronger detection results than using independently. This paper presents MSCA-FFT, a Fast Fourier Transform (FFT)-based multi-scale cross-attention framework for image-level deepfake detection. The model combines a partially fine-tuned Xception spatial branch with an FFT-based frequency branch. The frequency branch processes the log-scaled FFT magnitude spectrum through shallow convolutional layers, avoiding inverse frequency-to-image reconstruction used in DCT-based pipelines. The spatial and frequency representations are refined by transformer encoders, fused through cross-attention, and passed to an MLP classifier for real/fake prediction. Experimental results show that MSCA-FFT achieves consistently higher performance than the DCT-based state-of-the-art spatial-frequency fusion method and the compared baseline models. The ablation study further indicates that the FFT-based frequency branch provides complementary spectral cues when fused with spatial features. In addition, FFT-based frequency analysis and Grad-CAM/LIME explanations show consistent evidence around manipulation-sensitive facial regions, including the eyes, mouth, nose, and facial boundaries.

---


### 246. [Calibrated Alzheimer's Conversion Risk in Mild Cognitive Impairment: Persistent Homology of Clinical Trajectories with Conformal Guarantees](https://arxiv.org/abs/2607.17442)

**<font color=#1a73e8>作者：</font>** Navin Bondade  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Background. Predicting conversion from mild cognitive impairment (MCI) to Alzheimer's disease (AD) is central to trial enrichment and care planning, yet existing models provide no individual-level uncertainty estimates and rarely include transparent leakage audits. We introduce the first application of persistent homology to longitudinal clinical trajectory point clouds for this task, and the first split-conformal individual risk guarantee for any AD-conversion model. Methods. We analysed 741 MCI subjects (240 converters, 32.4%) from ADNI with a uniform 4-year follow-up cap. Five leakage sources were corrected; without them a naive pipeline achieved AUC=0.934, inflated by +0.075. Vietoris-Rips persistent homology and sublevel-set proxies were combined with trajectory slopes and engineered features (76 total) in a stacking ensemble evaluated by 5-fold cross-validation. Results. Cox and Random Survival Forest models with TDA features achieved concordance C=0.799 and C=0.826 versus C=0.753 and C=0.812 without (+0.045 and +0.014). The primary nested AUC is 0.840 (same-fold bound 0.866); external AUC was 0.879 on a zero-overlap ADNI-2/GO/3 cohort. H0 persistence entropy was the top SHAP feature and significantly associated with APOE4 dosage (Spearman r=-0.191, p<0.0001, Bonferroni-corrected). Cross-conformal coverage was 90.4%+-2.2% (target 90%); empirical external coverage 96.9%. Maximum fairness gap in false-negative rate across seven subgroups was 0.092. Conclusions. We propose H0 persistence entropy as a topological biomarker of cognitive decline and demonstrate that a leakage-audited, conformally calibrated pipeline reaches competitive accuracy with individual-level uncertainty quantification not previously available for this task.

---


### 247. [Multilingual Sentence Embeddings for Linguistic-Integrated Reliability Audit](https://arxiv.org/abs/2607.17466)

**<font color=#1a73e8>作者：</font>** Ummugul Bezirhan, Ji Yoon Jung, Matthias von Davier  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual assessment systems commonly rely on translation for scoring and quality-control processes. We evaluate whether multilingual sentence embeddings can replace translated English input for Linguistic-Integrated Reliability Auditing (LiRA) across 11 PIRLS constructed-response items and three embedding models. Native-language embeddings reproduced translation-based reliability estimates closely while recovering responses excluded after translation failure, with no meaningful change in reliability.

---


### 248. [DA-MergeLoRA: Hypernetwork-Based LoRA Merging for Few-Shot Test-Time Domain Adaptation](https://arxiv.org/abs/2607.17467)

**<font color=#1a73e8>作者：</font>** Siobhan Reid, Zhixiang Chi, Li Gu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot Test-Time Domain Adaptation (FSTT-DA) seeks to adapt models to novel domains using only a handful of unlabeled target samples. This setting is more realistic than typical domain adaptation setups, which assume access to target data during source training. However, prior FSTT-DA approaches fail to effectively leverage source domain-specific knowledge, relying on shallow batch normalization updates, prompt-based methods that treat the model as a black box, or ensembling strategies that do not capture cross-domain relationships. To address these limitations, we introduce a new FSTT-DA framework that integrates LoRA fine-tuning with model merging. In our approach, separate LoRA modules are fine-tuned on CLIP's vision encoder for each source domain. Since LoRA modifies only a small fraction of the model's parameters, it retains the base model's generalized knowledge while internally learning domain-specific features. To adapt the learned knowledge to a specific target domain, we propose a hypernetwork trained via meta-learning that generates per-column merging factors to combine LoRA modules. Given a small batch of target images, the hypernetwork produces merging weights that fuse source LoRA modules into a single adapted representation. Our results demonstrate state-of-the-art performance across various domain adaptation datasets. Our code is publicly available at this https URL.

---


### 249. [TraversRL: Traversable Pedestrian Pathway Generation With Reinforcement Learning](https://arxiv.org/abs/2607.17479)

**<font color=#1a73e8>作者：</font>** Bin Han, Robert Wolfe, Bill Howe  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatically generating pedestrian pathways from aerial images requires producing a connected network suitable for routing, not just detecting where sidewalks appear. Sidewalks and crossings, in contrast to roads, may be partially occluded, implicitly defined, and exhibit complex connectivity patterns. Existing segmentation-based approaches focus on labeling pixels to infer segments, but often produce disconnected or fragmentary graphs that are unreliable for navigation. We introduce TraversRL, a vision-conditioned model that iteratively grows a pathway network from an aerial image, simulating a traveler navigating the built environment. TraversRL uses an action space of short and long direction-distance segments designed to adapt to complex patterns and span occlusions, and uses a combination of graph-level and step-wise rewards to balance overall connectivity with precise edge placement. Across three visual backbones and three intersection datasets, TraversRL substantially improves buffered IoU with the ground-truth graph relative to a state-of-the-art segmentation baseline, and more than doubles metrics of connectivity. Moreover, combining global and local rewards produces cleaner graphs with fewer spurious branches while further improving overall performance. These results demonstrate that modeling pathway extraction as a sequential decision process from the perspective of a traveler, while optimizing for final graph quality with reinforcement learning, produces significantly more reliable pedestrian networks.

---


### 250. [Panache: One-Pass Motif Discovery at Every Window Length](https://arxiv.org/abs/2607.17481)

**<font color=#1a73e8>作者：</font>** Tej Sanibh Ranade  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Motif discovery, the search for recurring patterns within a time series, is a core primitive of exploratory data analysis. A pattern, however, is defined by its duration, which analysts rarely know in advance. To resolve this unknown duration, an interval of window lengths is defined, and the accepted method is to try every length in that interval. Existing pan matrix profile (PMP) methods compute one z-normalized matrix profile per length, so $L$ lengths cost $L$ quadratic self-joins over the same series. We introduce Panache, to our knowledge the first one-pass streaming algorithm for z-normalized PMP motif discovery. It replaces the repeated self-joins with a single scan whose runtime is near-linear in the series length. The key observation is that mean-centering a subsequence changes only its DC Fourier coefficient, so the non-DC spectrum of every z-normalized subsequence can be maintained online by sliding-DFT recurrences and running statistics. This spectral state is the key under which similar subsequences collide in an occupancy-controlled hash directory and, through Parseval's theorem, yields a lower bound that rejects most colliding pairs before any exact computation. Panache computes every data-dependent parameter itself, leaving only a resource budget to tune. At the default budget, it recovers all top-20 pan-motifs against exact fixed-exclusion ground truth on 17 UCR configurations, and is faster than every CPU and GPU baseline benchmarked in this paper. On Wafer at five million samples over 51 lengths, Panache completes one pass in 2.9 minutes and emits the exact motifs in 6.0 minutes, against 7.95 hours for the fastest exact CPU baseline and 38.3 minutes for SCAMP on an H100 GPU.

---


> [!TIP]
> 当前位于：**201-250**（第 5/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-386](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
