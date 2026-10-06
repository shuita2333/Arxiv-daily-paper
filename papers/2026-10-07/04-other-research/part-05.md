# 📦 其他研究 | 2026年10月07日

> 本类共 **571** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

---

### 201. [PIT-GCL: Protein Interaction using Topological Graph Contrastive Learning](https://arxiv.org/abs/2610.04850)

**<font color=#1a73e8>作者：</font>** Jae Won Choi, Ryoonki Hong, Alan Liang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Protein binding prediction is central to target identification, therapeutic binder design, and large scale screening, yet remains challenging because binding depends on sequence, three dimensional geometry, and global structural organization. Recent folding models such as AlphaFold3 and Boltz-2 have substantially improved structure prediction, but their confidence outputs (pLDDT, pTM, ipTM) are not specifically designed for binary binding prediction, and dedicated structure aware predictors often require bound complex structures that are unavailable at screening scale. We introduce PIT-GCL, a dual tower structure aware framework that encodes each protein independently from its amino acid sequence, C{\alpha} point cloud, and a global persistent homology descriptor. Each tower combines residue ESM-2 embeddings with a topological summary computed from the H0 and H1 persistence landscapes of a Vietoris-Rips filtration, and processes the resulting tokens with a structure aware Transformer in which pairwise C{\alpha} distances enter as a learned attention bias. A bidirectional cross attention module then performs latent space soft docking between the two per-protein representations, and the model is trained with a combined binary cross entropy and NT-Xent contrastive objective. On three binary interaction prediction benchmarks, general PPI on PPIRef, TCRpMHC binding on STAG, and whole chain pairs on PPB-Affinity, PIT-GCL outperforms representative sequence based, structure aware, and task specific baselines on general PPI under our evaluation, and is the only method above chance on PPB-Affinity; on TCR-pMHC it leads at a fixed decision threshold but is outranked by a task specific sequence model. Because each protein is encoded independently in the first phase, its representation can be precomputed and reused across candidate pairs, which is convenient for large scale screening.

---


### 202. [One Tile, Multiple Instances: Rethinking MIL for Sparse Diagnostic Evidence](https://arxiv.org/abs/2610.04853)

**<font color=#1a73e8>作者：</font>** Runsheng Liu, Cheng Jin, Hao Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In weakly supervised Whole Slide Image (WSI) classification, feature extractors typically compress each image tile into a single global embedding. Consequently, slide-level aggregators are restricted to this coarse tile scale, concealing fine-grained sub-tile evidence from the attention mechanism. We introduce DI-MIL, a framework that decouples encoding context from instance granularity through decomposed instances. By clustering dense spatial tokens from a frozen foundation model within each tile, DI-MIL converts a single tile into multiple independently weighted instance embeddings. As a training-free post-encoding module, DI-MIL integrates seamlessly into existing pipelines without requiring re-encoding or downstream architectural modifications. We evaluate DI-MIL on cytopathology, a challenging testbed where sparse diagnostic signals are easily diluted within standard tiles. Across four datasets, three frozen foundation models, and two attention-based aggregators, DI-MIL demonstrates consistent efficacy, improving 67 of 72 metric-level comparisons, with the largest mean gains reaching 3.64 points under cytopathology-specific backbones. In a broader comparison against seven representative MIL baselines, DI-MIL paired with ACMIL achieves highest mean performance in 33 of 36 backbone-dataset-metric comparisons. Ablations show that direct smaller tiling inflates the extracted tile count by up to 43.3$\times$ with non-monotonic performance, whereas DI-MIL incurs zero additional image-extraction overhead while achieving the strongest overall results. These results establish instance construction as an orthogonal design dimension in MIL, supporting DI-MIL as a cost-efficient solution under sparse diagnostic evidence.

---


### 203. [From Memory to Guide: Spatio-Temporal Composer for Procedural Coding Memory](https://arxiv.org/abs/2610.04868)

**<font color=#1a73e8>作者：</font>** Zhixuan Tan, Pengjie Gu, Zhao Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory-augmented agents typically integrate procedural knowledge by injecting retrieved skills directly into text prompts. This approach dangerously equates readable text with reliable execution. To bridge this gap, we introduce From Memory to Guide, a novel paradigm that transitions procedural memory from passive text delivery to active, inference-time policy adaptation. We instantiate this paradigm through the Spatio-Temporal Composer, an active policy compiler that explicitly manages exactly how and when retrieved knowledge should be applied. Rather than treating skills as plug-and-play modules, Composer dynamically aligns historical knowledge with current environmental constraints (spatial adaptation) and precisely dictates its applicable lifecycle (temporal orchestration). It actively transforms static memories into strictly bounded Runtime Guides---equipping the agent with localized objectives and behavioral guardrails without requiring a single parameter update. Extensive evaluations on 13 demanding, long-horizon software engineering tasks in EngramBench demonstrate the clear advantages of this architecture. Composer not only robustly prevents context mismatch but drives an absolute pass-rate increase of 7.2 percentage points on the most complex tasks, while simultaneously slashing the main agent's token usage by 32.2%.

---


### 204. [Your Temporal Link Predictor Is Blind to Who Is Active: A Missing Factor That Transfers Across Models](https://arxiv.org/abs/2610.04869)

**<font color=#1a73e8>作者：</font>** Ji Zhang, Zixin Liu, Yiran Ding 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An interaction has two parts: someone decides to act, and then chooses whom to act on. Temporal link prediction has concentrated on the second, and we show that it is blind to the first by construction: a standard negative keeps the real source and swaps the destination, and we prove that this cancels the source's activity exactly from the optimal score, so no model trained and evaluated this way is ever rewarded for learning it. Under the harder historical and inductive negatives, whose sources differ, the same factor becomes the dominant signal. We model it with Source Node Activity Modeling (SNAM), a self-exciting event intensity fitted by an exact point-process likelihood to decayed interaction counts the history states already contain; it has fewer than 20 parameters. On their own, never looking at the destination, these parameters beat DyGFormer and TPNet on four of five datasets under historical negatives. Added to the frozen scores of TPNet, TGN, DyGFormer and DSRD, four models of different design, without retraining anything, they raise AP on almost every backbone-dataset pair in both settings, by up to 25 points. Our full model ranks first overall against eleven baselines on 13 datasets and three protocols, and on million-event streams trains an epoch 9-100x faster than TPNet and DyGFormer. We conclude that source activity is a blind spot of temporal link prediction, and a cheap, transferable one to close. Code is available at this https URL.

---


### 205. [Bounded Reasoning: Cognitive Hierarchy in Human-versus-AI Cyber Defense](https://arxiv.org/abs/2610.04878)

**<font color=#1a73e8>作者：</font>** Zahra Aref, Sheng Wei, Narayan B. Mandayam  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Human-agent evaluations often compress interaction into a single performance score, even when human and automated policies adapt differently over time. We study this in a sequential cyber-defense game on an attack graph, where a human or reinforcement-learning defender protects cloud assets against a Deep Q-Network (DQN) attacker. We compare four defender settings: a human reward-only game operationalizing the DQN information structure, a human reward-plus-transition game operationalizing the Cognitive Hierarchy Theory-driven DQN (CHT-DQN) information structure, an automated DQN defender, and an automated CHT-DQN defender. In the reward-only game, participants receive payoff and reward feedback. In the reward-plus-transition game, they also see attacker-aware transition probabilities from the CHT-DQN model. Across 80 Mechanical Turk participants and matched automated simulations, human defenders adapted to outcomes in a way the automated defenders did not: they were more likely to reselect a node after a successful defense than after a failure, in both games, an asymmetry we interpret as consistent with Prospect Theory and Cumulative Prospect Theory. The 40-round average also mixes early rounds, where the DQN attacker acts mostly at random, with late rounds, where it mostly exploits; in the final stage, mean protection ranks the reward-plus-transition human game above the reward-only human game, then the automated CHT-DQN defender, then the automated DQN defender, an ordering the overall mean hides. By contrast, the reward-plus-transition game does not produce a statistically reliable overall gain in weighted data protection over the reward-only game. These results suggest that evaluating human-agent cyber-defense systems only by an averaged task score can miss behaviorally meaningful differences in adaptation, action allocation, and bounded human reasoning.

---


### 206. [Reflection-Robust 6DoF Object Tracking with Light Fields](https://arxiv.org/abs/2610.04883)

**<font color=#1a73e8>作者：</font>** Nikolai Goncharov, Donald G. Dansereau  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tracking the 6DoF pose of a moving rigid object is fundamental to robotics and autonomous driving, but existing trackers assume that object appearance is stable across a sequence, an assumption that breaks down on reflective surfaces whose appearance changes as they mirror the environment. We introduce a light field based reflection-robust 6DoF tracker that turns this apparent nuisance into a pose cue. Per frame, our method recovers depth robustly against reflections, back-projects it into a point cloud, and estimates surface normals. It then decomposes the object's view-dependent appearance into a diffuse albedo and the environment map it reflects, resulting in a relightable surface light field. Starting from a coarse initialization, we relight it by the recovered environment map and optimize the pose on the photometric loss. Because a moving object mirrors new parts of the scene, the environment map fills in as the sequence proceeds, sharpening this signal over time. To evaluate this approach, we introduce a light field tracking dataset re-rendered from a robotic manipulation benchmark at four controlled reflectivity levels, each paired with simulated depth that reproduces how consumer RGB-D sensors fail on shiny surfaces. Additionally, we evaluate on two captured light field sequences. Our method trails the strongest baselines on diffuse objects and is the only one that holds its accuracy on fully reflective objects, where every baseline degrades.

---


### 207. [SFlexRCA: Lightweight, Scalable, and Flexible Root Cause Analysis for IIoT Edge Systems](https://arxiv.org/abs/2610.04893)

**<font color=#1a73e8>作者：</font>** Amr M. Zaki, Farhoud Jafari, Honggeun Ji 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Industrial Internet of Things (IIoT) systems generate high-dimensional sensor telemetry from interconnected components, where faults can propagate across the system. To address these challenges, we propose SFlexRCA (Scalable and Flexible Root Cause Analysis), a topology-free RCA framework designed for resource-constrained IIoT environments. SFlexRCA transforms multivariate telemetry into compact orthogonal representations and applies shared lightweight linear modeling, avoiding explicit graph construction, message passing, and per-variable or lag-specific parameter growth. We evaluate SFlexRCA on three publicly available IIoT datasets, BATADAL, SWaT, and WADI, spanning different numbers of monitored variables, temporal characteristics, and training-data regimes. SFlexRCA is compared with 10 statistical, causal, and non-causal baselines in terms of RCA accuracy, training efficiency, inference latency, and memory consumption. In addition, inference efficiency and memory consumption are evaluated on Raspberry Pi 3 and Raspberry Pi 5, while energy consumption is additionally measured on Raspberry Pi 5. We further investigate temporalcontext sensitivity, architectural and loss components, and alternative representations. Notably, SFlexRCA maintains strong localization performance on BATADAL despite its limited normal-operation training data, while its compact shared architecture avoids the parameter growth associated with causal and graph-based approaches. Its lightweight shared architecture further enables efficient deployment on resource-constrained IIoT edge devices. The SFlexRCA code is available at this https URL Analysis-Correlation-Attentive-Modeling.

---


### 208. [WLPA: A Network Management Framework for Allocating Scarce Quantum-Safe Link Postures under Weakest-Link Exposure](https://arxiv.org/abs/2610.04897)

**<font color=#1a73e8>作者：</font>** Bhanwar Gupta, Sanjeev Rana  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Network operators migrating distributed systems to post-quantum and quantum-safe cryptography face a resource-management problem: quantum key distribution (QKD) gives the strongest guarantee available but is hardware-scarce and costly, so only a fraction of a deployment's links can receive it. Default practice -- ranking links by traffic or centrality and upgrading the top scorers -- optimizes each link in isolation, while a distributed job's real security is set by whichever active link ends up weakest. We present WLPA (Weakest-Link Posture Assignment), an implementation-ready decision framework and algorithm for allocating scarce quantum-safe postures under hardware, latency, and compliance constraints. WLPA computes the optimal weakest-link posture in closed form and returns an assignment in O(|E| log |E|) time -- 125 ms for a 20,000-link network on a laptop -- with a breach-aware refinement matching an exact integer program under common conditions. Our central contribution is a dichotomy telling operators exactly when existing per-link heuristics already match this optimum and when they systematically fail: under constant upgrade cost and uniform traffic-driven risk the two coincide exactly; once costs vary or an adversary concentrates on weak targets, heuristics leave the weakest link unprotected, unboundedly. We validate WLPA across 19 experiments: four microservice topologies, a real enterprise network (SNAP email-Eu-core), a post-quantum latency benchmark, a Qiskit BB84 simulation and a real-hardware BB84 run on IBM's ibm_marrakesh processor, checks against real production traffic traces, a CVE-calibrated correlated-compromise study, Bayesian uncertainty quantification, and seven baseline methods. A concrete-security reduction grounds the framework as theoretical foundation, not primary contribution.

---


### 209. [A Systematic Analysis of the Predictive Power of LM Surprisal in Reading Chinese](https://arxiv.org/abs/2610.04898)

**<font color=#1a73e8>作者：</font>** Hongao Zhu, Muxiaoqiao Xu, Yikang Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study analyzes the predictive power of LM-derived, token-level surprisal on Mandarin Chinese reading times. We first propose the Shortest Matching Sequence (SMS), an alignment scheme that maps between the word segmentation assumed by eye-tracking corpora and the LMs' subword tokenization, as the two tokenizations often disagree in the context of Mandarin Chinese. Then, using a suite of Chinese-Pythia models (14M-1.4B) trained on scratch with 30B tokens, we examine how well surprisal predicts first fixation duration, gaze duration, and total reading time in three paragraph-level eye-tracking corpora of Mandarin Chinese (GECO-CN, HKP, and MECO). Contrary to previous null findings, our results show that surprisal is predictive of Chinese reading times. However, whether predictive power scales with model size and the amount of training is corpus-specific: bigger models predict better in GECO-CN, whereas inverse scaling emerges in HKP and, at the largest sizes, in MECO. Subsequently, we tested one possible explanation for the inverse scaling in HKP and found that checkpoints whose surprisal remains closer to $n$-gram statistics are better predictors of reading. All in all, the predictive power of surprisal on Chinese reading time measurements is corpus-specific, which cautions against drawing scaling conclusions from a single corpus.

---


### 210. [ScopeSAE: Model-Scope Feature Discovery with Interpretable Layer Selection](https://arxiv.org/abs/2610.04905)

**<font color=#1a73e8>作者：</font>** Qingwen Zeng, Zehao Fu, Shuyu Meng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) are a central tool in mechanistic interpretability. However, existing SAEs are primarily trained per layer. The modeling subspace is therefore fixed by layer identity, independent of which token-layer states actually drive each prediction. We argue that this constraint contributes to several limitations observed in layer-wise SAEs, including low feature utilization, high dictionary redundancy, and features that lack direct behavioral grounding. In this paper, we propose ScopeSAE, which selects the modeling subspace per token by attributing each prediction to its most influential token-layer state via normalized gradient-based attribution, and learns features over the resulting prediction-relevant subspace. Empirically, ScopeSAE yields an effect we term reconstruction-better-than-original. Written-back reconstructions of the SAE produce lower next-token cross-entropy than the original activations, an outcome that, to our knowledge, has not previously been reported for SAEs. Through interventional analyses and a KL fine-tuning counter-experiment, we show that this effect is attributable to ScopeSAE's prediction-relevant subspace itself rather than to architectural changes. ScopeSAE further improves effective feature count, interpretability, utilization, and dictionary redundancy over existing layer-based baselines, suggesting that choosing the SAE modeling subspace by predictive relevance leads to more useful and behaviorally meaningful features.

---


### 211. [Residual Visual Credit Optimization: Conserved Evidence Routing for Multimodal Reinforcement Learning](https://arxiv.org/abs/2610.04918)

**<font color=#1a73e8>作者：</font>** Lin Qiu, Yao Liu, Diyi Hu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards scales multimodal reasoning, but an outcome reward says how much a trajectory is worth, not how that value should be spread over the decisions that produced it. We introduce Residual Visual Credit Optimization (RVCO), which treats token credit as a conserved routing problem. A controlled visual intervention yields a per-token evidence response; robust within-trajectory coordinates remove incidental scale; and a budgeted entropic router distributes a fixed amount of sequence utility according to perceptual dependence. A residual support path guarantees positive credit at every valid position, and an analytic correction restores the prescribed credit mass exactly. The resulting field is selective, bounded, full-support, and invariant to response-local score shifts, and recovers hard token selection as a limiting case. Across four model families and seven reasoning benchmarks, RVCO improves accuracy over strong RLVR baselines while maintaining late-stage optimization stability, corruption robustness, and competitive training cost. Rewards, rollouts, and the group-relative advantage estimator are unchanged; only the geometry of token-level credit differs.

---


### 212. [TRACE: Time-Adaptive Residual Attention Control with Content-Style Decomposition for Training-Free Diffusion Style Transfer](https://arxiv.org/abs/2610.04922)

**<font color=#1a73e8>作者：</font>** Duc Khoan Le, Kim Ngoc Tran, Minh Nhat Le 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reference-guided style transfer aims to preserve the semantic structure of a content image while transferring the visual appearance of a style reference. Recent diffusion-based methods achieve impressive stylization quality by exploiting strong pretrained generative priors. However, training-free approaches still face a difficult trade-off among style fidelity, content preservation, and content leakage. Direct style injection may unintentionally transfer semantic content from the style image, while fixed guidance schedules often ignore the time- and state-dependent nature of diffusion sampling. To address these limitations, we propose TRACE, a training-free diffusion style transfer framework with Time-adaptive Residual Attention Control and Content-Style Decomposition. TRACE first performs offline CLIP-based subspace analysis to separate content and style directions from paired data. During inference, it removes content-related components from the style reference and style-related components from the content reference to reduce leakage. It then injects style information through residual cross-attention and applies uncertainty-aware guidance to adapt the guidance signal at each denoising step. Experiments show that TRACE achieves a favorable trade-off between stylization and preservation. Compared with optimal-control-based baselines, TRACE substantially improves style fidelity (+17.28 CSD and +34.10 SRA). While, compared with stylization methods, it better preserves content structure (+12.80 DINO, +5.52 CLIP-I, and -8.19 LPIPS) and reduces directional semantic leakage by 29.5% in DCL. Our code is publicly available at this https URL.

---


### 213. [TSAE: Structured Sparse Autoencoders for Interpreting Time-Series Forecasting Models](https://arxiv.org/abs/2610.04925)

**<font color=#1a73e8>作者：</font>** Baoxi Liu, Yi Xie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series forecasting informs critical decisions in energy dispatch, industrial operations, and environmental monitoring; understanding the patterns models rely on is essential for assessing reliability and identifying failures. Input attribution identifies important variables and time segments but offers limited insight into internal features, while standard sparse autoencoder (SAE) objectives do not directly constrain cross-variable structure or temporal continuity. We introduce TSAE, a structured sparse autoencoder for forecasting representations that decomposes hidden states into individually inspectable features. TSAE organizes cross-variable structure through shared and variable-routed private dictionaries, separates feature detection from magnitude estimation with gated encoding, and constrains neighboring sparse-code changes according to raw-segment similarity. These mechanisms support analysis of variable context, activation strength, and temporal evolution. Forecast-consistency fine-tuning further improves preservation of the frozen forecaster's outputs. The accompanying TSEVAL protocol separately audits fidelity, feature coherence, and physical calibration to ground feature interpretation. In three-seed experiments with frozen PatchTST on ETTh1, ETTh2, and ETTm1, TSAE achieves the lowest hidden-state reconstruction error, normalized forecast-reconstruction error (NFRE), and feature transition rate among five SAEs at comparable per-token activity. NFRE decreases by 4.3-26.4% relative to the next-best mean. Dataset-dependent tradeoffs in selectivity, physical correlation, and calibration show that fidelity and temporal-stability gains require independent semantic validation to support feature interpretation.

---


### 214. [Billion-Scale Thumbnail Optimization for Uncurated Short-Form Videos via Multi-Armed Bandits](https://arxiv.org/abs/2610.04931)

**<font color=#1a73e8>作者：</font>** Ying Han, Ling Liu, Fabio Soldo 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper introduces a real-time thumbnail optimization system deployed at a global $O(B)$ scale on a major short-form video platform. Unlike traditional long-form content, where custom thumbnails are heavily curated by creators, a considerable fraction of short-form videos are published without human-selected artwork. To address this uncurated corpus, we present a fully automated, end-to-end framework that replaces static default frames with dynamic, data-driven selections across billions of videos. To the best of our knowledge, this is the first published work demonstrating an online Multi-Armed Bandit framework successfully deployed at an $O(B)$ scale for uncurated short-form video discovery. Our solution pairs a multi-stage candidate generation pipeline with a low-latency serving infrastructure. By initializing the exploration framework with image-specific priors derived from a deep visual quality model, the system minimizes exploration costs and dynamically serves optimal thumbnails at serving time. Global deployment demonstrates statistically significant improvements in core user discovery and engagement metrics.

---


### 215. [Learning under Localized Minority Imbalance](https://arxiv.org/abs/2610.04936)

**<font color=#1a73e8>作者：</font>** Amin Hosseininasab, Steven M. Shugan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Class-imbalance methods implicitly assume that the minority class is uniformly undersampled relative to the majority class. However, in many real-world settings, minority instances may be disproportionately under-observed in certain regions of the feature space. For example, small businesses that go bankrupt may disappear from records, while those that survive remain visible, making bankruptcy appear less common among small firms than it actually is. This gives rise to localized minority imbalance (LMI), a challenge that is often overlooked and extends beyond general class-count imbalance. We show that under LMI, existing imbalance mitigation techniques can fit observation-induced biases in the training data and generalize poorly to under-observed regions of the true minority distribution. To address this, we propose a tree-based stratified approach that recursively partitions the feature space with the goal of reducing within-stratum LMI distortion. For each resulting stratum, we pair its majority instances with the full observed minority set and train a base classifier to create an ensemble. Extensive experiments over benchmark tabular datasets simulated with LMI show that our stratified ensembling approach outperforms popular and state-of-the-art imbalance mitigation techniques. We also introduce a gold-standard evaluation protocol that uses unbiased test sets, and demonstrate that conventional hold-out evaluation from the same LMI-biased data can substantially mislead performance. Overall, our results highlight that the cause of imbalance is as important as the correction method.

---


### 216. [Orchestrating Level-$K$ Policies Against Unknown Opponents in Partially-Observable Dynamic Games](https://arxiv.org/abs/2610.04937)

**<font color=#1a73e8>作者：</font>** Addison Kalanther, Sanika Bharvirkar, Daniel Bostwick 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Level-$K$ reasoning generates a hierarchy of policies specialized to opponents with different reasoning levels. When an opponent's level is unknown, a common deployment rule estimates that level and selects the corresponding response. In a dynamic, partially-observed game, this selection is repeated, with each choice shaping subsequent states and observations. The response associated with the most likely opponent level need not maximize expected return from the current history. We formulate this deployment problem as dynamic orchestration of a fixed, pretrained policy library in a partially observable Markov game. We compare classification-based orchestrators (CBOs) trained using offline data or on-policy data aggregation with a reinforcement-learning-based orchestrator (RLBO) trained to maximize expected discounted return. In pursuit-evasion experiments, on-policy training improves classification and return, yet RLBO achieves higher return than the on-policy and offline CBOs. Given a pretrained library, RLBO also reaches performance comparable to a policy trained directly over the pursuers' action space with fewer training timesteps. These findings support treating a hierarchy of level-$K$ policies as a resource for orchestration, not a prescription for deployment.

---


### 217. [D-DOIT: Training-free Adaptation of Discrete Diffusion via Doob's h-Transform](https://arxiv.org/abs/2610.04938)

**<font color=#1a73e8>作者：</font>** Jieke Wu, Qijie Zhu, Weimin Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose D-DOIT (Discrete Doob-Oriented Inference-time Transformation), a training-free and efficient adaptation method for discrete diffusion models with generic rewards. D-DOIT formulates adaptation as sampling from a reward-tilted target distribution and realizes this transport through Doob's h-transform of the discrete diffusion reverse kernel, using only reward values rather than reward gradients. Unlike continuous diffusion, masked discrete diffusion samples categorical token-reveal transitions rather than continuous state updates. D-DOIT derives the corresponding discrete Doob's h-transform, which guides sampling by reweighting reverse transition probabilities instead of adding a drift correction. To make this transformation practical, D-DOIT avoids expensive future rollouts. At each guided step, D-DOIT samples candidate next states, uses the model prediction head to complete each candidate into a clean sequence, evaluates each completion with the reward oracle, and resamples the next state with probabilities proportional to the rewards. An optional late-stage best-of-K refinement further improves sample quality by branching trajectories only near the end of denoising, avoiding the $K$-fold cost over the full trajectory. Empirically, across regulatory DNA design and protein inverse folding benchmarks, D-DOIT outperforms training-free guidance baselines. It improves enhancer activity and cell-type specificity while preserving sequence naturalness, and achieves the highest success rate in protein inverse folding.

---


### 218. [A Graph-Based Inspection and Intervention Tool for Assessing Mechanistic Learning in PINNs](https://arxiv.org/abs/2610.04939)

**<font color=#1a73e8>作者：</font>** Adwait Patkhedkar, Alifaraz Lakhani, Prathmesh Mohite 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We ask whether physically meaningful correspondences discovered inside a trained scientific model remain meaningful outside the conditions under which they were discovered. We introduce GIIT (Graph-based Inspection and Intervention Tool), which represents governing physics as a computational physics dependency graph, maps graph nodes to internal network components via sensitivity- and trend-based discovery, and tests the resulting mapping under targeted intervention. Evaluating on temporal extrapolation out-of-distribution (OOD) regimes of increasing severity, we find that temporal extrapolation is associated with layer-wise correspondence drift and reduced functional correspondence. Specifically, while the model achieves low physics residual in-distribution (1.915 x 10-4 on full ID and 1.01 x 10-4 on an ID sub-window t in [0.5, 0.8]), the functional mapping changes even before leaving the training domain, and the shift continues as the evaluation window extends beyond the training domain: residual error increases from 2.81 x 10-2 on the boundary-crossing window (t in [0.5, 1.5]) to 3.30 x 10-1 on severe OOD (t in [1, 2]), accompanied by a systematic leftward shift of internal layer mappings, where the average winner layer index drops from 5.71 (ID) to 3.00 (ID sub-window) down to 2.29 (severe OOD). Only 2 of 7 physical nodes maintain stable layer assignments across the boundary-crossing window, and only 1 of 7 under severe extrapolation, revealing potential internal functional correspondence changes before severe degradation in conventional output metrics. Additional results for linear oscillatory systems are further detailed in the appendix.

---


### 219. [Zero-Shot Time-Series Question Answering via Decoupled Perception and Reasoning](https://arxiv.org/abs/2610.04942)

**<font color=#1a73e8>作者：</font>** Jing Xie, Haochen Yuan, Yunbo Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time-series question answering (TSQA) requires grounding linguistic queries and diverse answer formats in complex numerical observations. However, existing methods heavily overfit to specific datasets and struggle to generalize when input series, question contexts, and answer requirements shift simultaneously. To address this challenge, we propose TSHarness, an agentic framework that establishes a decoupled workflow for cross-dataset zero-shot TSQA. At its core, TSHarness divides and conquers numerical perception and contextual reasoning via a structured Time-Series Perception State (TPS). Guided by a reusable memory of analytical knowledge, a learned Tool Selector adaptively invokes numerical tools to extract salient statistical and temporal features into the TPS. The answering agent then performs semantic reasoning over the TPS to generate target outputs, triggering iterative re-perception through the feedback loop when evidence is deemed insufficient. By separating numerical feature extraction from question-specific reasoning, TSHarness eliminates the need for target-side training or answer feedback, providing a generalizable, cost-efficient foundation for zero-shot TSQA.

---


### 220. [TempoBridge: Source-Conditioned Flow Matching with Optimal Transport Couplings for Single-Cell Population Transitions](https://arxiv.org/abs/2610.04945)

**<font color=#1a73e8>作者：</font>** Bowen Han, Lingbei Meng, Shihuan Luo 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Destructive single-cell measurements provide unpaired population snapshots rather than observations of the same cells across conditions. Local cell states and transition requests may also be insufficient to distinguish responses across source populations. We introduce TempoBridge, a common source-conditioned transport formulation for temporal, genetic, and chemical population transitions. Source cells initialize latent transport and provide a fixed empirical population summary. The velocity field receives this summary alongside the evolving cell state, flow time, and a structured transition descriptor. Minibatch optimal transport (OT) supplies couplings only for conditional flow-matching training paths; inference requires neither target expression nor OT computation. On held-out donors, TempoBridge achieves an Energy distance of 0.129 versus 0.144 for scGen. Genetic mean-expression $L_2$ error is 2.261 versus 3.156 for scGPT-scratch under Seen 2/2. On held-out compounds, condition-averaged drug-effect correlation is 0.598 versus 0.561 for the CellFlow adapter. Temporal ablations show higher mean distributional error after removing source context, replacing optimal transport with random pairing, or replacing flow matching with static residual regression. Together, these results demonstrate the predictive utility of a common source-conditioned transport formulation across held-out donors, gene combinations, and compounds.

---


### 221. [Bridging the EHR Divide: Asymmetric Contrastive Learning for Cross-National Medical Representation Transfer](https://arxiv.org/abs/2610.04946)

**<font color=#1a73e8>作者：</font>** Qingyang Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-system transfer of longitudinal Electronic Health Record (EHR) representations is challenging because clinical coding, patient populations, and healthcare workflows differ substantially across institutions and countries. We introduce Asymmetric Supervised Contrastive Learning (Asymmetric SupCon), a task-specific pre-training objective motivated by the heterogeneity of negative clinical outcomes. The objective clusters patients sharing a target positive outcome without explicitly attracting negative trajectories toward one another. We pre-train temporal Transformer encoders on longitudinal records from 3.98 million patients in the Taiwanese National Health Insurance Research Database (NHIRD) and transfer them to two U.S. EHR datasets, MIMIC-IV and EHRSHOT. A hybrid semantic mapping pipeline combining direct mappings with embedding-based retrieval enables transfer across heterogeneous clinical vocabularies. On MIMIC-IV, NHIRD pre-training consistently improves over random initialization while substantially narrowing the performance gap to task-specific in-domain pre-training. On EHRSHOT, the transferred models show particularly strong few-shot performance for incident disease prediction. A controlled objective ablation shows that Asymmetric SupCon achieves the best AUPRC on three of four evaluated tasks and is 0.003 AUPRC below Standard SupCon on the fourth. These results support asymmetric contrastive pre-training as an effective approach for task-specific cross-national EHR representation transfer. Code is available at this https URL.

---


### 222. [EDISCO: Equivariant DIScrete Diffusion for Euclidean Combinatorial Optimization](https://arxiv.org/abs/2610.04953)

**<font color=#1a73e8>作者：</font>** Ruogu Chen, Jie Han  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Euclidean combinatorial optimization problems (ECOPs), such as the Traveling Salesman Problem (TSP) and Capacitated Vehicle Routing Problem (CVRP), possess inherent symmetries under the two-dimensional Euclidean group E(2), including rotations, reflections, and translations. Existing learning-based methods, including recent diffusion-based methods, rely on data augmentation or regularization to approximate E(2)-equivariance. This paper presents EDISCO, the first discrete diffusion model for ECOPs with exact E(2)-invariant generative distributions over node-index solutions. EDISCO introduces an E(2)-equivariant edge-score network coupled with a categorical continuous-time Markov chain over discrete edge variables, and exact posterior sampling provides efficient multi-step inference. This design gives EDISCO a local geometric inductive bias: edge neighborhoods with the same relative geometry and combinatorial context are represented consistently regardless of absolute position or orientation, making learning more efficient and inference more robust than non-equivariant methods. EDISCO outperforms previous learning-based state-of-the-art solvers on synthetic TSP from 100 to 10000 nodes and CVRP from 50 to 2000 customers, while using only 33-50% of the training instances. Trained only on uniform synthetic data, EDISCO also outperforms competing learning-based baselines under spatial distribution shift and CVRP constraint-tightness shift. Code is available at this https URL.

---


### 223. [Trinity: One Differentiable Physics for Training, Refining and Scoring Generative Floorplanners](https://arxiv.org/abs/2610.04957)

**<font color=#1a73e8>作者：</font>** Shih-Ying Yeh, Tzu-Sian Wang, Xuehai Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Floorplanning arranges the blocks of a chip and decides their shapes under objectives that press blocks together, short wirelength and a small outline, and constraints that hold them apart, non-overlap, clusters, MIB shapes and boundary blocks. Recent diffusion placers train on reference layouts alone and leave this coupled system to guidance, post-hoc loops and a legalizer, reporting only the endpoint, which hides what the generator contributes. We re-implement four of them under one recipe on FloorSet, score raw, refined and legalized layouts on one scale, and propose Trinity, a flow-matching floorplanner whose six differentiable functions for the constraints and objectives are its training loss term, the energy of a closed-form refiner after sampling and the base of a soft cost for every stage. The network thus learns the correction prior placers apply in their samplers, and sampling needs no guidance. Stage by stage, the training term lowers a plain transformer's raw soft cost by 26% and matters most at short budgets, the shared refiner decides more of the final cost than the generator and matches a ported placer's loop in 16 to 660 times fewer steps, Trinity's refined soft cost is 36% below the best ported pipeline, the soft cost ranks settings as the contest's hard cost does, and on the FloorSet val set the pipeline reaches a mean hard cost of 1.014 in 1.63 s per case.

---


### 224. [MAGIC: Topology-Aware Analytic Graph Few-Shot Class-Incremental Learning](https://arxiv.org/abs/2610.04963)

**<font color=#1a73e8>作者：</font>** Junlin Chen, Yuhan Wang, Xuefei Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph few-shot class-incremental learning (GFSCIL) requires a model to continually recognize emerging classes from only a few labeled nodes while preserving previously acquired knowledge. Beyond the catastrophic forgetting inherited from conventional graph continual learning, GFSCIL presents two distinctive challenges: extremely limited novel-class supervision causes severe overfitting, while cross-session edges---edges connecting newly arriving nodes with historical nodes---alter historical propagation neighborhoods and thereby induce representation drift. We propose MAGIC, a replay-free GFSCIL framework that combines a frozen graph representation backbone (e.g., an intrinsically parameter-free backbone such as SGC or a pretrained graph foundation model) with closed-form analytic continual learning. To alleviate novel-session overfitting, MAGIC learns a topological prior from the base graph that can characterize both homophilous and heterophilous relations, and injects this prior through Potts Markov random field inference to refine supervision for novel classes. To mitigate representation drift, MAGIC transfers previous predictions from the old representations of affected historical nodes to their updated representations through drift-aware analytic distillation. Experiments across five datasets and eight baselines demonstrate the effectiveness of MAGIC. Under the 5-shot setting, MAGIC improves Mean Accuracy and Final Accuracy by 5.48 percentage points and 9.33 percentage points on average, and reduces Performance Drop by 10.78 percentage points on average compared with the best baselines. MAGIC also shows clear advantages under the 1- and 3-shot settings, with larger gains as the number of supports increases. Moreover, MAGIC requires substantially less training time.

---


### 225. [BACAM: Behavior-Aware Continual Agent Merging for Multi-Turn Interaction](https://arxiv.org/abs/2610.04966)

**<font color=#1a73e8>作者：</font>** Shuaitong Li, Baochen Xiong, Xiaoshan Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Model merging offers a way to integrate the capabilities of specialized experts, but existing agent merging methods typically require all of them to be available at once. We study continual agent merging, which integrates incoming experts sequentially without retaining previously merged experts. Yet merging in parameter space or feature subspaces does not ensure that the merged model acquires an incoming expert's behavior on interaction trajectories. Moreover, updates toward a new expert can disrupt the merged model's previously integrated interactive behavior. Therefore, we propose Behavior-Aware Continual Agent Merging (BACAM), which learns parameter-wise merging gates from candidate-generated trajectories using expert-guided behavioral supervision. Task-level stability-plasticity control and tensor-level conflict-aware update budgets limit interference with existing capabilities while allowing new ones to be acquired. The learned gates are folded into the model weights without additional inference-time parameters. Across four interactive tasks - web shopping, tool use, information retrieval, and embodied interaction - BACAM achieves an average success rate of 62.82%, exceeding the strongest evaluated merging baseline by 21.69 percentage points. Our code is publicly available at this https URL.

---


### 226. [Hamiltonian Metric Learning and Energy-Based Training: A Dissipative Geometric Framework for Optimization](https://arxiv.org/abs/2610.04969)

**<font color=#1a73e8>作者：</font>** Sparsho Chakraborty, Mohammad Alamgir, Nishanth M 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimization in machine learning is usually expressed through iterative rules that update model parameters using information from the loss landscape. In this work, we study an alternative viewpoint in which parameter optimization is treated as the evolution of a dissipative dynamical system. The model parameters are regarded as generalized coordinates, the loss acts as a potential energy, and a positive-definite metric defines the local kinetic geometry of parameter space. Starting from a variational formulation, we derive the corresponding Hamiltonian dynamics, the geometric force generated by a position-dependent metric, and a metric-compatible Rayleigh dissipation law. The resulting continuous system satisfies a monotonic energy-dissipation relation, while its discrete form allows the influence of curvature on the optimization trajectory to be studied directly. We illustrate the framework using a controlled CIFAR-10 image-reconstruction problem for which the optimum is known analytically. With the image Hessian used as the metric, the curvature dependence of the quadratic modal dynamics is removed. We then reparameterize the same image as a matrix product state, producing a genuinely position-dependent metric and a nonzero geometric force. Poincaré return maps provide a complementary phase-space view of the resulting contraction dynamics. These examples establish HAMLET as a geometric, energy-based framework for studying optimization as dissipative motion in parameter space. On a five-seed MNIST MLP benchmark, HAMLET attains the highest mean test accuracy (97.95\%) and the lowest mean test negative log-likelihood (0.0696) among the three evaluated optimizers.

---


### 227. [Runtime Authorization of Self-Generated Subgoals in Long-Horizon Tool-Using AI Agents](https://arxiv.org/abs/2610.04975)

**<font color=#1a73e8>作者：</font>** Genliang Zhu, Chu Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon tool-using AI agents create subgoals, replan, delegate work, and compose sibling results. Per-tool permission checks cannot establish that a changing goal graph remains within the principal-approved task. We address this authorization gap in a finite structured domain with one principal and one authorization root. Each proposed goal-graph mutation carries a version-bound witness that its continuation traces, resources, obligations, invariants, and closing condition refine the active root contract; every protected effect is rechecked at an atomic commit boundary. Free-form goal text supplies no authority.
We prove trace-policy and modeled forbidden-state preservation under explicit mediation, abstraction, freshness, and atomicity assumptions, plus conditional root-success preservation, a separation result for memoryless allowlists, exact finite-domain decidability, and universal-safety monotonicity under sound abstraction refinement. An executable model explores 340 states and 419 transitions. Across 96 matched cases covering 25 structural schemas, the complete mechanism commits zero forbidden states in 48 drifted cases and completes all 48 benign counterparts. Two public upstream runtime paths execute 258 native dispatches across 32 cases, with every case-level decision and receipt chain matching. A frozen host-local study covers 129 synthetic one-factor-at-a-time cells, all matching fixed decisions and reasons. A history-aware continuation comparator blocks every modeled bad trace prefix but commits all operations in 11 cases whose violations lie in typed resources, freshness, or explicit-join evidence outside its trace projection. Within the registered structured domains, runtime authorization preserves useful replanning while preventing self-generated subgoals from becoming a source of new authority.

---


### 228. [Robust Tensor Completion via Reflective Convolution Nuclear Norm Minimization](https://arxiv.org/abs/2610.04979)

**<font color=#1a73e8>作者：</font>** Weiguo Zhou, Feng Zhang, Wenjin Qin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust tensor completion recovers multidimensional data from partial observations corrupted by sparse gross errors. Existing convolutional low-rank models typically construct translated copies using circular continuation, which introduces artificial wrap-around neighborhoods for finite nonperiodic data. We propose reflective convolution nuclear norm minimization (RCNNM), which replaces circular shifts with endpoint-nonrepeating reflection. The resulting lifting has nonuniform entry multiplicities and satisfies a weighted Gram identity that supports both the recovery analysis and the optimization method. Under random sampling and sparse corruption, we establish high-probability exact recovery of the underlying tensor and sparse errors, together with stability under bounded dense perturbations. We further develop a two-block ADMM with a closed-form entrywise tensor update, while singular-value thresholding is implemented through the smaller right Gram matrix. Experiments on synthetic tensors, BSDS color images, and CAVE multispectral images show that RCNNM consistently improves over its circular-lifting counterpart, with the clearest gains near image boundaries. In particular, average boundary-PSNR improvements reach 3.26 dB while global reconstruction quality remains competitive.

---


### 229. [Geometry-Aware Preference Optimization for Text-to-Image Diffusion Models](https://arxiv.org/abs/2610.04980)

**<font color=#1a73e8>作者：</font>** Lei Wang, Zhen Wang, Yuexiang Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Preference alignment has become a standard practice for text-to-image diffusion models. Direct Preference Optimization (DPO) simplifies this process by eliminating explicit reward modeling. Its diffusion variant, Diffusion-DPO, has become a widely adopted baseline. Diffusion-DPO essentially encourages the likelihood of preferred samples while suppressing dispreferred ones. In this paper, we revisit DPO-style alignment methods for diffusion models from the perspective of the manifold hypothesis. Under this view, natural images concentrate near a low-dimensional manifold embedded in the high-dimensional ambient space, whereas DPO directly optimizes preference distributions in the full space without accounting for this geometric structure. This creates a mismatch in the optimization dynamics: it suppresses geometry-preserving tangential updates, while insufficiently restricting hazardous normal-direction updates. This mismatch gradually degrades image quality and diversity. To address this issue, we propose Anisotropic Geometry-Aware Preference Optimization (APO), which replaces the uniform Euclidean treatment of prediction errors with a geometry-aware anisotropic metric derived from the reference model. Concretely, APO adaptively strengthens regularization in directions where the reference denoising function is highly sensitive, while relaxing constraints in directions that permit safe semantic adjustment. This recalibrates preference optimization according to the local manifold geometry, and maintains the original manifold structure. Experiments show that APO achieves strong performance and an average win rate exceeding 60\% against various existing alignment methods across diverse benchmarks. It requires significantly fewer training steps than prior methods, and preserves generation diversity throughout training.

---


### 230. [How Long, Not How Close: A Learned Temporal Metric for Planning in Latent World Models](https://arxiv.org/abs/2610.04988)

**<font color=#1a73e8>作者：</font>** Lama Moukheiber, Haotian Xue, Yongxin Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent world models plan by rolling a frozen predictor forward under candidate action sequences and ranking the candidates by the latent distance between their imagined end state and the goal. However, this ranking breaks down when the goal lies several plans away, because the latent distance measures how closely an end state resembles the goal rather than how far it remains from reaching it. To address this, we propose TEMPO, a temporal-distance planning objective that leaves the world model untouched, learns only from the demonstrations already used to train it, and adds negligible cost to the planner's search. TEMPO learns a small map of the frozen latent in which the distance between two states of an episode reflects the number of environment steps between them, and blends this distance into the planner's cost. It requires no rewards, policies or success labels and, being a cost rather than a model, applies to frozen world models with one latent vector per state that plan by a latent distance. We evaluate TEMPO on eleven simulated environments (e.g., maze navigation, tabletop pushing, robotic arm control and three-dimensional manipulation) with the LeWM and PLDM planners. With a small MLP that adds at most 0.3% to a plan's arithmetic, TEMPO improves both planners at every goal distance, including the one-plan setting of their evaluations, raises LeWM from 36% to 99% on TwoRoom three plans from the goal, and remains competitive on a broad range of 2D and 3D navigation, reaching and manipulation tasks.

---


### 231. [Pessimistic Minimax Learning for Public-Private Information Games under Unilateral Coverage](https://arxiv.org/abs/2610.04997)

**<font color=#1a73e8>作者：</font>** Shuze Daniel Liu, Claire Chen, Jiuqi Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study offline learning in two-player zero-sum contextual games with public and private information, motivated by strategic settings such as auctions and negotiations with private valuations. We introduce unilateral prescriptive concentrability and show that asymmetric information can change offline coverage through its effect on equilibrium behavior. For finite state-action spaces, we develop a pessimistic algorithm with an $\tilde{O}(1/\sqrt{n})$ exploitability rate, matching the standard sample-size dependence for fully observed minimax games. We further develop a pessimistic policy mirror descent framework, PPA-PMD, for general function approximation and obtain a unified $\tilde{O}(1/\sqrt{n} + 1/\sqrt{T})$ exploitability rate with no-regret actor updates. Together, these results provide the first theoretical framework for offline equilibrium learning under public-private information constraints.

---


### 232. [Beyond Overparameterization: Provable Learning of Input-Convex Multi-Layer Polynomial Networks with Active Queries](https://arxiv.org/abs/2610.04999)

**<font color=#1a73e8>作者：</font>** Jinqi Tang, Qian Chen, Shihong Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The theoretical understanding of multi-layer neural networks is largely confined to overparameterized settings, which obscure parameter identifiability and incur high sample complexity. Neural tangent kernel (NTK) provides a general theory for wide networks, but does not offer efficient sample-complexity guarantees. Recent feature-learning results go beyond kernel methods for single-neuron, multi-index, and hierarchical targets. However, the analysis is often restricted to shallow or specific architectures and to the overparameterized regime. We break this paradigm to achieve parameter-level recovery of deep target networks, albeit by using active data queries. Specifically, we study $L$-layer polynomial networks with even degree-$k$ monomial activations and nonnegative higher-layer weights. This structure makes the target network input-convex, while the optimization landscape remains highly nonconvex with respect to the parameters. Leveraging input convexity and active queries, we propose \textbf{ASPIRE} (\textbf{A}ctive \textbf{S}am\textbf{P}ling for \textbf{I}terative \textbf{R}ecovery via \textbf{E}igendirections), a layerwise sampling-based diagonalization algorithm that recovers all network parameters to $\delta$-accuracy with sample complexity $ \widetilde O_{k,L}\left(d^{L^2+O(L)}\delta^{-2e}\right) $ in polynomial time. To our knowledge, this is the \emph{first} parameter-recovery guarantee for deep target networks whose exponent grows only polynomially with depth, as well as the \emph{first} justification for the effectiveness of using high-quality data in neural network training, with a remarkably \emph{exponential} separation.

---


### 233. [VisualErase: Dual-Branch Visual Trajectory Redirection for Robust Concept Erasure in Text-to-Image Diffusion Models](https://arxiv.org/abs/2610.05000)

**<font color=#1a73e8>作者：</font>** Qianlong Xiang, Miao Zhang, Kun Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept erasure is essential for the safe deployment of text-to-image diffusion models, as they may reproduce harmful, copyrighted, or privacy-sensitive content learned from unconstrained large-scale data. Existing methods typically erase unwanted concepts while preserving general generation capability by redirecting target-related text-to-image mappings. However, recent studies show that erased models may still retain visual generative trajectories of target concepts, leaving them vulnerable to adversarial recovery attacks and revealing a fundamental gap between redirecting text-to-image mappings and truly removing visual knowledge. To bridge this gap, we propose VisualErase, a new paradigm that redirects concept-bearing visual generative trajectories toward explicitly defined concept-removed outcomes. To enable this redirection, we use structure-preserving image editing to construct content-aligned, concept-removed counterparts for source images, providing explicit visual endpoints that retain non-target content. We then derive a denoising target from each source-to-counterpart pair and use a dual-branch redirection loss to align both text-conditioned and unconditional predictions with this target, since conditional supervision alone does not explicitly constrain generation without textual guidance. To mitigate the adverse effects of concept erasure on non-target generation, we jointly optimize the redirection loss with a counterpart retention loss that matches denoising predictions from the frozen pretrained model. Across style, celebrity, and nudity erasure, VisualErase limits the maximum attack success rate over seven attacks to 0%, 8%, and 0.1%, respectively, while retaining general generation quality. These results highlight the importance of visual trajectory redirection for robust concept erasure beyond text-to-image mappings alone.

---


### 234. [How corner is a corner case? Percentile control for highway scenario generation](https://arxiv.org/abs/2610.05003)

**<font color=#1a73e8>作者：</font>** Jiaxi Liu, Hang Zhou, Hangyu Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generating corner-case scenarios with appropriate adversity in a simulation environment is critical for testing an autonomous vehicle (AV) software stack's safety performance before deployment. Existing autonomous-driving scenario generators can enforce specific behavior, adversity, or feasibility conditions, but they provide limited control over how extreme a generated scenario is relative to plausible futures in the same traffic context. This study represents the adversity of a generated scenario as its percentile in the conditional distribution of future risk given the observed history. This view supports calibrated answers to two questions: how "corner" a generated corner-case scenario is and how its "cornerness" can be fine-tuned.
To this end, we formulate history-conditioned risk-percentile requests and learn a reference risk distribution that maps each requested percentile to a physical risk target. We then use a percentile-conditioned joint diffusion model with sampling-time risk guidance to generate multi-agent futures, together with a reference-based criterion for evaluating percentile realization.
Experiments use the minimum post-encroachment time (PET) between the ego and its surrounding vehicles as the risk surrogate on highD. On the primary evaluation set, our method realizes 1,422 of 1,440 requests within a 0.05 percentile tolerance (98.75%), with mean percentile error 0.00673 and PET-target error 0.00991 seconds. The resulting interface connects context-relative risk specification, physical realization, and evaluation through a common risk scale. Project website and videos of generated scenarios are available at this https URL.

---


### 235. [Physics-Augmented Graph Transformers for Patch-Antenna Forward and Inverse Design](https://arxiv.org/abs/2610.05004)

**<font color=#1a73e8>作者：</font>** Avi Epstein, Snir Nehemia, Haim Suchowski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Full-wave electromagnetic (EM) simulation enables accurate patch-antenna analysis but is computationally expensive for large-scale forward prediction and inverse design. We present a mesh-native, physics-augmented graph-learning framework that treats radiation-pattern prediction as signal reconstruction on an irregular surface mesh. For the forward problem, a GPS graph transformer is trained with Physics-Augmented Intermediate Supervision (PAIS), an auxiliary node-level objective that predicts complex surface currents, the physical intermediate linking geometry to radiation. PAIS improves multiple GNN backbones at no inference-time cost, while shuffled-current and non-physical controls show the gain comes from physical correspondence. Direction-conditioned decoding and a differentiable radiation-integral consistency loss further exploit this structure. On an 80,000-sample CST benchmark, GPS+PAIS reaches MSE 0.17 / PSNR 19.67, generalizes to a PCA split, and transfers zero-shot to canonical patches. For inverse design, surrogate-filtered diffusion beats nearest-neighbor retrieval by 32% relative MSE.

---


### 236. [Toward Lightweight Aerial 5G gNBs: Reproducible OAI Testbed on Commodity ARM Platforms](https://arxiv.org/abs/2610.05007)

**<font color=#1a73e8>作者：</font>** Marc Duboc, Ammar El Falou  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> For a battery-powered UAV base station, every gram and watt devoted to RAN-compute competes with flight-duration margin. We therefore keep the 5G Core (5GC) and central unit (CU) on the ground and design the airborne unit around only the backhaul endpoint, distributed unit (DU), and radio. The key question is then a practical one: can widely available commodity ARM computers sustain a real radio OpenAirInterface (OAI) 5G DU with useful performance over heterogeneous F1? We answer it with Raspberry Pi~5 and Jetson Orin Nano as DUs, a USRP B210, a commercial handset, and Ethernet, Wi-Fi/GRE, and 5G/WireGuard backhaul. Jetson preserves 88.4% of x86 split-DU Ethernet DL throughput and 87.5-89.0% across all three bearers; 5G/WireGuard preserves 76.4-77.1% of each host's wired DL rate. The validated Jetson/B210/RM500Q-GL electronics weigh 657.4 g and draw about 28 W under sustained traffic (757.4 g with integration allowance). A controlled link adaptation intervention raises split DL from 23.4 to 99.4 Mb/s as the dominant Modulation and Coding Scheme (MCS) moves from 3 to 26. Finally, synchronized radio, F1-U, CPU, and UHD evidence narrows the remaining monolithic-split gap to split-path scheduling/timing behavior. Beyond performance, this capability serves the emergency-response use case that motivates the aerial cell: once deployed above an affected area, it can broadcast a PWS warning message. We release the OAI patch that carries the single-segment Write-Replace Warning over F1 from CU to DU, where SIB8 is scheduled to the handset. The public artifact makes the payload, performance, and emergency-broadcast baseline reproducible with laboratory-accessible hardware.

---


### 237. [EMBER-Bench: Benchmarking Cross-Event Causal Memory in Long-Horizon Embodied Tasks](https://arxiv.org/abs/2610.05013)

**<font color=#1a73e8>作者：</font>** Aoyang Cai, Boning Zhao, Shaoxuan Xie 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lifelong physical agents must reason over extended interactions where past events continue to shape the world long after they disappear from view. Beyond recalling what happened, agents must infer how history changes the current state and constrains future actions. Yet existing embodied and video-memory benchmarks largely focus on historical retrieval and summary, leaving such history-dependent causal reasoning underexplored. We introduce EMBER-Bench, an egocentric benchmark for cross-event causal reasoning in long-horizon embodied tasks, for which we newly created the task design, video recording, and data annotation. It contains 189 household tasks and 699 QA pairs, spanning task progress, failure recovery, external interventions, and compound long-horizon tasks with distant dependencies and prerequisites, with fine-grained event and causal-chain annotations. EMBER-Bench evaluates reasoning in both directions: next-action prediction selects the next action from history, and causal traceback, given that action, identifies the historical event that makes it necessary. Input ablations that add action logs or privileged cause-and-consequence annotations to the video indicate which kind of historical information models fail to use. Among the 16 evaluated models, the highest overall accuracy is 61.2%, compared with a mean of 98.3% across two human evaluators. At paired decision points, correct traceback is not associated with correct next-action prediction. Adding action logs yields a gain of 1.6 points, whereas cause-and-consequence annotations yield an additional gain of 13.0 points on top of that. These results suggest that extracting causal information from past events and converting it into constraints on current actions remains a key difficulty for long-horizon embodied agents. Project Page: this https URL

---


### 238. [MetaKernelBench: Measuring GPU Kernel Knowledge Transfer Beyond Code](https://arxiv.org/abs/2610.05014)

**<font color=#1a73e8>作者：</font>** Xueyi Chen, Shiyu Liu, Xin Jin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent GPU kernel optimization agents retain what they learn in knowledge bases or as distilled skills. Kernel benchmarks score each attempt's implementation for correctness and speed but leave the reuse value of retained experience unmeasured. We introduce MetaKernelBench, which measures whether experience distilled from an attempt in one kernel domain-specific language (DSL) improves a fresh attempt at the same problem in another. Its 74 problems are fused subgraphs in six families, each posed as a pair of CuTe DSL and TIRx variants that differ only in the DSL. The agent first attempts each variant solo and is instructed to distill what it learns into a natural-language skill, which is transferred whether or not the source attempt passes verification. The skill is the only extra input to a skill-conditioned attempt by the same model in the other DSL. We compare each skill-conditioned attempt with the solo attempt on the same variant under matched per-attempt budgets, scoring correctness and end-to-end runtime. Across six models and both directions, paired lift over solo attempts ranges from -19% to +29%. Four models gain in both directions, yet regressions occur on 16% to 45% of problems in every model and direction. Outcomes follow the source attempt's result relative to the target's solo attempt rather than source success alone, improving in 71% of comparisons when the source stands above and regressing in 54% when it stands below. MetaKernelBench complements implementation-quality metrics by measuring same-problem cross-DSL kernel knowledge transfer.

---


### 239. [Operational Abstractions of Neural Network Concepts via Topological Representations](https://arxiv.org/abs/2610.05017)

**<font color=#1a73e8>作者：</font>** Mathieu Pont, Christoph Garth  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Concept-based methods provide a semantic level for interpreting and manipulating learned representations, but existing editing approaches are typically specialized to particular interventions and do not provide a common and editable representation of concept organization. To achieve this, we introduce Topological Concept Representations (TCR), a post-hoc operational abstraction that jointly characterizes the concepts encoded in a learned representation and their relationships. TCR constructs an intermediate concept space from concept recoverability and interaction scores, and compactly encodes its organization through topology. Interventions are expressed through modifications of this abstraction that are propagated back to the underlying learned representation. This allows different concept-level operations to share the same optimization framework and separates the desired concept organization from the mechanism to achieve it. We establish stability and reparameterization-invariance properties of TCR and its connections to existing concept-editing formulations. We use TCR to disentangle concepts as a preprocessing step for existing erasure methods, improving worst-group accuracy by 21.89 on average at comparable concept leakage. We further use TCR to transfer concepts from teacher to student models, improving concept recoverability by up to 5.54 while also improving or maintaining competitive test top-1 accuracy.

---


### 240. [LightVLN: Efficient Aerial Vision-and-Language Navigation with Compact Memory and History-Guided Local Aggregation](https://arxiv.org/abs/2610.05024)

**<font color=#1a73e8>作者：</font>** Yiming Zhao, Tianshun Li, Jingle He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aerial vision-and-language navigation (VLN) enables unmanned aerial vehicles to execute long-horizon natural-language instructions from visual observations in complex three-dimensional environments. However, recent aerial VLN models often rely on large-scale vision-language backbones and dense visual histories, imposing substantial computation and memory costs that hinder onboard deployment. We propose LightVLN, a lightweight history-aware aerial VLN framework that combines a compact 0.5B language backbone with compact representations of both historical and current observations. LightVLN compresses each historical frame into a single token using visual features already computed by the policy. It further introduces history- and instruction-conditioned local aggregation to reduce the current observation from 256 to 32 visual tokens while preserving navigation-relevant spatial information. With up to 16 historical frames, the policy uses at most 48 observation-derived tokens. On the public OpenFly dataset, LightVLN achieves 50.93% Test-Seen and 36.14% Test-Unseen success rates (SR), outperforming the evaluated 7B language-backbone baselines on most reported metrics. It also achieves 25.83% SR on AerialVLN-S Val-Seen. In a reconstructed unseen campus, we deploy LightVLN on a DJI M350 RTK with an external Jetson Orin NX 16 GB for closed-loop onboard-compute real-to-sim hardware-in-the-loop (HIL) evaluation, achieving 14.61 Hz model inference and 11.13 Hz end-to-end decision updates. These results demonstrate the effectiveness and efficiency of LightVLN for aerial navigation.

---


### 241. [SPACE-CLIPv2: Decoding Local Geometry from Frozen CLIP for Monocular Depth Estimation](https://arxiv.org/abs/2610.05029)

**<font color=#1a73e8>作者：</font>** Hyun Song, Taewan Cho, Kangmin Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language foundation models such as CLIP provide strong semantic representations, but their patch tokens are not directly optimized for dense metric geometry. SPACE-CLIP showed that frozen CLIP features can support monocular depth estimation through layer-group feature fusion, yet it leaves open how neighboring CLIP tokens should be combined to recover fine local structure. We present SPACE-CLIPv2, a frozen-backbone depth decoder that aggregates fixed local neighborhoods in CLIP token space. At selected decoder stages, the model samples a fixed token stencil, predicts aggregation weights, and injects the resulting response through a gated residual update. A token-space high-pass branch further preserves shallow local contrast. On NYU Depth V2, SPACE-CLIPv2 improves over a matched SPACE-CLIP baseline, while five-seed experiments consistently favor fixed over learned-offset sampling. Zero-shot iBims-1 evaluation further improves boundary and planar-geometry measures. These results support constrained local token aggregation as a practical mechanism for decoding geometry from frozen CLIP representations.

---


### 242. [Calibrated Weak Supervision for Post-Harvest Burned-Cropland Mapping Under Label Scarcity](https://arxiv.org/abs/2610.05040)

**<font color=#1a73e8>作者：</font>** Raunak Bhagate, Maitri Polisetty, R I Minu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mapping post-harvest burned cropland is difficult when fires are small and fragmented and reliable labels are scarce. We developed a calibrated weak-supervision framework for Punjab, India, using Sentinel-2 spectral change, VIIRS active-fire context, and MODIS MCD64A1 as a coarse external calibration and agreement reference. Three pseudo-label recipes, five feature representations, and linear, tree-based, boosted, and neural classifiers were evaluated using nested district-held-out cross-validation over three seeds and five folds. NBR and dNBR were excluded from classifier inputs. The best configuration used the very-strict recipe, a multilayer perceptron, and the full optical feature set (mean Cohen's kappa 0.395, AUROC 0.753, F1 0.747, balanced accuracy 0.703); Random Forest, XGBoost, and LightGBM were practically tied. Higher agreement with held-out pseudo-labels did not establish improved label correctness or independent burned-area accuracy. For deployment, a Random Forest with the very-strict recipe and full optical features was retained. An externally calibrated threshold of 0.60 yielded district-level MODIS agreement of R-squared 0.636, a mapped-to-MODIS burned-area ratio of 1.005, and Spearman correlation of 0.779 with district fire counts. Pixel-level MODIS agreement remained modest (F1 0.205, kappa 0.093). Zero-shot transfer to Haryana was promising (mean kappa 0.641), but Punjab cross-year stability was weak, and Sentinel-1/Sentinel-2 feature concatenation did not improve the optical baseline. Optical observations ended before the seasonal fire context, limiting coverage of late burns. The framework supports district-scale burden assessment and hotspot screening, with limited support for exact scar boundaries or temporally stable annual mapping.

---


### 243. [CI-JEPA: A Counterfactual Analysis of Latent Representations in Joint-Embedding Predictive Architectures for Self-Supervised Learning](https://arxiv.org/abs/2610.05043)

**<font color=#1a73e8>作者：</font>** Mintu Dutta, Ritesh Vyas, Mohendra Roy *  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-supervised visual representation learning learns useful features without manual annotations during representation training. The image-based joint-embedding predictive architecture (I-JEPA) predicts latent representations of masked image regions, but its objective does not explicitly model responses to specified visual interventions. We introduce CI-JEPA, a counterfactual intervention-aware extension that learns to predict the representation change $\Delta Z = Z_{\mathrm{CF}} - Z$ between an original image and a modified counterpart. We assess representation robustness through selective sensitivity: stronger responses to task-relevant semantic changes than to nuisance changes. Experiments on Flowers102 use flower-center occlusion as a candidate semantic intervention and background blur and tint as candidate nuisance interventions. With frozen-encoder linear probing, CI-JEPA achieves a best validation accuracy of 78.14\%, compared with 77.55\% for both the pretrained ViT-B/16 and the I-JEPA baseline, a gain of 0.59 percentage points. The reported mean $L_2$ representation changes are 4.42 for center occlusion, 3.48 for background tint, and 2.83 for background blur. This ordering is consistent with relative semantic selectivity for the evaluated interventions, rather than complete nuisance invariance. The accuracy comparison is complementary and does not establish improved robustness over the baselines. These controlled image modifications provide a framework for studying intervention-induced changes in JEPA representations; they do not establish causal feature discovery or robustness to all visual changes.

---


### 244. [AraYoungVoices: A Diverse L1/L2 Corpus of Arabic Child and Adolescent Speech](https://arxiv.org/abs/2610.05044)

**<font color=#1a73e8>作者：</font>** Shammur Absar Chowdhury, Zien Sheikh Ali, Houssam Eddine-Othman Lachemat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> State-of-the-art ASR systems primarily target native adult speech, leading to substantial performance gaps for children, adolescents, and L2 speakers. We introduce AraYoungVoices, a 151.72-hour Arabic read-speech corpus from 286 speakers aged 7--18, comprising AraKids (7--12) and AraTeens (13--18). The corpus includes 146 native Arabic (L1) and 140 second-language (L2) speakers, with native speakers spanning Egyptian, Gulf, Levantine, and North African dialectal backgrounds and L2 speakers representing diverse linguistic backgrounds across the Americas, Asia, Africa, and Europe. We benchmark four pretrained ASR models under zero-shot and fine-tuned settings using unseen-speaker-$\&$-unseen-prompt (USUP) and unseen-speaker-$\&$-seen-prompt (USSP) evaluations. Results show that L2 speech remains substantially more challenging than L1 speech, with the largest errors observed mainly for younger L2 speakers. Age-specific fine-tuning improves the matched age group, while joint fine-tuning provides a stronger balance across populations. ASR hypotheses are also consistently closer to the standard reading prompt than to the verbatim transcription, particularly for L2 speech, suggesting partial normalization of reading deviations.

---


### 245. [E$^2$-OPSD: Taming Entropy Overshoot in On-Policy Self-Distillation](https://arxiv.org/abs/2610.05048)

**<font color=#1a73e8>作者：</font>** Yifei Liu, Minghao Fang, Xinyu Gu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) provides dense token-level supervision without a second model: one network acts as teacher with the reference solution and as student with only the problem. We identify a specific failure mode of this recipe. During training, student token entropy rises past the teacher's and remains elevated, a pattern we call entropy overshoot. We trace it to both sides of distillation. The reference-conditioned teacher is confident along its answer-directed reasoning path, but this confidence transfers poorly to student-generated prefixes, making its supervision overly tied to answer-specific cues rather than reusable reasoning patterns; meanwhile, the forward KL used by OPSD continually diffuses the student's predictive distribution without pulling it back. We introduce E$^2$-OPSD to address both causes. Exemplar-guided teaching replaces the current answer with a retrieved solved neighboring problem, providing transferable reasoning guidance without revealing the destination and better matching student-reachable states. Entropy-aware distillation uses the student-teacher entropy gap to determine the direction and strength of each token's correction. E$^2$-OPSD improves math reasoning by up to 4.3 points in mean@16 over OPSD, while out-of-domain evaluations show gains over the corresponding base models of up to 4.9 points in mean@16 and 5.5 points in pass@8. Despite these gains, E$^2$-OPSD remains simple, requiring no additional forward passes or networks.

---


### 246. [LogSig-SSM: Time-Series Modelling with Multi-Scale Log-Signature Compression for State-Space Models](https://arxiv.org/abs/2610.05051)

**<font color=#1a73e8>作者：</font>** Felix Oury, Nicolas Calvo Peiro, Reiko J. Tanaka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series data are often sampled irregularly at high frequencies and exhibit long-range dependencies, which makes long-horizon modelling difficult. Continuous-time models such as neural controlled differential equations (NCDEs) and neural rough differential equations (NRDEs) can handle irregular sampling, but they scale poorly to long sequences. Selective state-space models (SSMs) such as Mamba scale linearly with sequence length, but they provide limited recurrent mixing across hidden dimensions within a single block. We propose LogSig-SSM (Log-Signature Compression for State-Space Models), which first compresses long multivariate time series into a shorter sequence of tokens using multi-scale windowed log-signatures, and then processes these tokens with a selective SSM backbone. LogSig-SSM is scalable and robust to irregular sampling, combining log-signature tokens that capture higher-order cross-channel interactions with a selective SSM that models long-range dependencies. The model also admits a continuous-time interpretation as an NCDE/NRDE-style system driven by a log-signature-based input, in which selectivity induces an input-dependent rescaling of the latent dynamics. Across four benchmarks, namely long-sequence classification on UEA, high-frequency physiological regression on PPG-DaLiA, multivariate weather forecasting, and irregularly sampled clinical prediction on PhysioNet Sepsis, LogSig-SSM outperforms or matches strong SSM and continuous-time baselines while training up to $30\times$ faster and using up to $37\times$ less GPU memory than Mamba on the longest sequences.

---


### 247. [CoDG-Net: Structure-Guided Style Diffusion and Collaborative Learning to Mitigate Catastrophic Forgetting in Medical Image Domain Generalization](https://arxiv.org/abs/2610.05053)

**<font color=#1a73e8>作者：</font>** Yucheng Song, Jincan Wang, Haokang Ding 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Domain Generalization (DG) for medical image segmentation is both highly challenging and critically important. However, existing medical DG methods largely overlook the issue of Catastrophic Forgetting (CF): \textbf{Models often sacrifice their ability to retain source-domain knowledge while pursuing cross-domain robustness.} This can directly threaten diagnostic safety in already-deployed clinical scenarios. To address this, we investigate data augmentation strategies and catastrophic forgetting for medical image DG segmentation. First, we propose a structure-guided style diffusion augmentation method. Constrained by anatomical structure consistency in the frequency domain, this method performs cross-domain diffusion on the amplitude spectrum, generating samples with more diverse and broader style coverage to better support domain generalization. Then, we design a collaborative learning network with a dual-branch interactive architecture (CoDG-Net), together with a novel learning bias-guided strategy that adaptively regulates knowledge transfer at both the layer level and the task level, thereby effectively mitigating catastrophic forgetting on the source domain. Experiments and ablation studies on single-source and multi-source medical DG benchmark datasets demonstrate that CoDG-Net not only outperforms existing state-of-the-art methods in target-domain segmentation performance, but also achieves a lower forgetting rate on the source-domain data. The code is available at: this https URL.

---


### 248. [Cross-chain Access Control for Permissioned Blockchain Interoperation](https://arxiv.org/abs/2610.05054)

**<font color=#1a73e8>作者：</font>** Tirthankar Sengupta, Bishakh Chandra Ghosh, Sandip Chakraborty 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As enterprise blockchains become increasingly interconnected, access control must extend beyond the boundaries of a single network. Existing approaches mainly focus on controlling access within one blockchain, while cross-chain interactions involve multiple networks that may follow different access-control policies and administrative rules. In this paper, we propose InterAcct, an end-to-end access-control framework for secure interactions across permissioned blockchain networks. To avoid exposing sensitive internal information, InterAcct converts outgoing requests into a consortium-level representation before they are shared with another network. When a response is returned, the framework securely maps it back to the original requester within the source consortium, preserving confidentiality throughout the interaction. Our experimental results show that InterAcct can enforce end-to-end access control for cross-chain request-response interactions with low additional overhead and can continue to operate effectively as the workload increases.

---


### 249. [Revealing After Overwriting: An Exponential POMDP OPE Lower Bound under History-Dependent Logging](https://arxiv.org/abs/2610.05063)

**<font color=#1a73e8>作者：</font>** Youyu Luo, Pengzhan Zhou, Zhida Qin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-step revealing can make off-policy evaluation tractable under memoryless logging. With history-dependent logging, state decodability and target-relevant evidence can separate. For every horizon $H\ge3$, we construct two exactly realizable POMDPs with four actions, at most four states per layer, a known logger, and a memoryless target. Action overlap, history coverage, and observation-only revealing remain bounded independently of $H$, yet the target values differ by $1/2$ and the KL divergence between the logged laws is $\Theta(4^{-(H-1)})$, forcing exponential sample complexity. Logger memory makes states distinguishable, while reset erases the model-distinguishing evidence preserved by the target. A separate construction retains this barrier with common, known observation-only revealing operators. Under action and history coverage, we give a finite-class OPE guarantee using common observable value representations that remain valid at every history. The sample bound depends polynomially on their second-moment cost. In the common-operator construction, the same value direction has constant marginal decoding cost but exponential history-conditioned cost. Finally, on a fixed four-action continuum, we derive matching passive and budgeted readout rates. With one known channel and unit read cost, early reads are optimal. With unknown sensor bias, early reads alone remain exponentially costly. Combining them with post-reset calibration gives sample complexity independent of $H$ when both read types receive fixed positive expected budgets per trajectory.

---


### 250. [Salvation Lies Within: Eliciting Inherent Style Transfer in Step-Distilled Diffusion Models](https://arxiv.org/abs/2610.05066)

**<font color=#1a73e8>作者：</font>** Shengyin Sun, Yiming Li, Yingzhao Lian 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adapting step-distilled text-to-image (T2I) models through post-training incurs additional computational costs and affects native few-step generation behavior. This motivates a complementary route beyond style-specific adaptation: drawing on the visual knowledge already encoded in step-distilled T2I models to elicit stylistic capabilities through language. Pursuing this direction requires textual guidance that captures how visual attributes jointly define a style and remain applicable as the depicted content changes. To explore this approach, we introduce StyleForge, a fully automatic, training-free framework that expresses reference styles as reusable rendering instructions. By integrating overall rendering characteristics with local color and lighting behavior, StyleForge organizes visual evidence from reference images into a coherent specification of how the target style should be expressed. The specification is then compiled into textual guidance that can be reused across content prompts, enabling frozen step-distilled T2I models to render different subjects and scenes in the reference style while retaining native few-step generation. Extensive experiments show relative gains of up to 29.47\% in generation quality scores over the strongest baseline, while Pareto analysis indicates that improved stylization is accompanied by strong adherence to the requested content.

---


> [!TIP]
> 当前位于：**201-250**（第 5/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
