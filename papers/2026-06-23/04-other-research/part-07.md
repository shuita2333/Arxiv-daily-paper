# 📦 其他研究 | 2026年06月23日

> 本类共 **654** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-654](./part-14.md)

---

### 301. [Learning by Shifting: Temporal View Construction for Time Series Contrastive Learning](https://arxiv.org/abs/2606.21957)

**<font color=#1a73e8>作者：</font>** Abdul-Kazeem Shamba, Kerstin Bach, Gavin Taylor  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supervised learning demands large quantities of labeled data, a bottleneck that is expensive and reliant on domain-specific expertise. Self-supervised learning, particularly contrastive learning, has emerged as a compelling alternative, enabling rich representation learning directly from unlabeled data. Yet its success hinges critically on the design of positive and negative sample pairs. Existing approaches for time series rely on hand-crafted augmentations and masking heuristics that embed strong domain assumptions, often limiting generalization across diverse temporal patterns and potentially introducing spurious correlations. In this work, we challenge this paradigm by demonstrating that explicitly encoding temporal shift invariance through a simple, deterministic view construction is sufficient to learn strong representations for time series classification. By exploiting temporal structure, our method, Shift Invariant Feature Training (ShiFT), achieves state-of-the-art performance on six diverse real-world time series benchmark datasets, as well as the UCR and UEA archives, while reducing training time. Beyond empirical performance, we present a systematic analysis of contrastive learning dynamics in time series settings, examining the effects of batch size and the number of negatives on downstream performance. Our findings provide practical insights for designing efficient contrastive learning frameworks for time series representation learning. The source code is publicly available at this https URL.

---


### 302. [OpenBioRQ: Unsolved Biomedical Research Questions for Agents](https://arxiv.org/abs/2606.21959)

**<font color=#1a73e8>作者：</font>** Minbyul Jeong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A working citation looks like proof -- but the fact that a link resolves does not mean the cited paper supports the claim. I find that current agentic models rarely fabricate citations (over $99\%$ resolve), yet roughly $15.9\%$ link to the wrong paper. Existing benchmarks miss this failure mode: when a question has a fixed answer key, a model can reproduce the expected source from that key rather than independently verifying that the source supports the claim. I introduce \textbf{\openbiorq{}}, a retrieval-grounded agentic benchmark of $12{,}553$ unsolved biomedical research questions across $12$ domains that treats open questions as a faithfulness-and-abstention probe. To my knowledge, this is the first biomedical benchmark to combine an agentic setting -- where the model must issue multiple tool calls -- with unsolved questions that have no answer key. Openness is verified against real follow-up evidence rather than a model's parametric knowledge. Difficulty is empirical: I anchor it on questions that three open-weight reference models fail to answer, rather than on subjective hardness labels. On this hardest subset, held-out models from the same lineage as the difficulty anchors solve only ~17%, while three independent frontier agents (Gemini-3-Pro, Opus-4.7, GPT-5.5) span a wide 29-60% range. The benchmark is thus hard, non-saturating (the best agent still leaves ~33-40\% unsolved), and discriminating across capability tiers. Beyond difficulty, I observe agentic collapse on the hardest questions, where agents stop using their tools. For the most collapse-prone model, blocking tool access entirely barely changes its score -- so tools stop paying off exactly where they are needed most. A frozen per-question checklist raises inter-judge agreement from Spearman 0.35 to 0.82.

---


### 303. [A Standard Processing Pipeline for High-accuracy Measurement of Few-shot Regression on Laser Induced Breakdown Spectroscopy](https://arxiv.org/abs/2606.21960)

**<font color=#1a73e8>作者：</font>** Hao Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Laser-induced breakdown spectroscopy (LIBS) faces challenges in high-accuracy quantitative measurement under few-shot scenarios due to spectral noise and data scarcity. Traditional preprocessing methods often fail to preserve subtle spectral features or capture nonlinear correlations. This work proposes a standardized processing pipeline integrating diffusion-based denoising, attention-based autoencoder for dimensionality reduction, group shuffling data augmentation, and ordinary least squares regression. The diffusion module employs a 3D UNet architecture to remove spectral noise while preserving essential emission features. The attention-autoencoder captures nonlinear spectral correlations, effectively reducing high-dimensional spectral data to compact latent representations. Group shuffling data augmentation enhances model robustness by creating synthetic samples through feature group permutation. Experimental results on multiple elemental concentrations demonstrate that our Diffusion-DA-AE pipeline achieves superior performance with a mean RMAE of 0.2847, representing 37.7\% and 37.6\% improvements over baseline autoencoder and traditional PCA-PLS regression, respectively. The framework's effectiveness validates its generalizability and establishes a new benchmark for few-shot LIBS regression.

---


### 304. [Integrating Facial Generation into Full-Duplex Spoken Dialogue Systems](https://arxiv.org/abs/2606.21970)

**<font color=#1a73e8>作者：</font>** Jingjing Jiang, Atsumoto Ohashi, Ryuichiro Higashinaka  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Full-duplex spoken dialogue models, such as Moshi, enable natural, low-latency voice conversations. However, they remain limited to the audio modality, lacking the facial expressions that are integral to human communication. We present Moshi-Face, the first full-duplex dialogue model that jointly processes the user's audio and facial input while simultaneously generating speech and facial motion. We first construct a vector-quantized variational autoencoder (VQ-VAE) as a face codec that encodes 3D head meshes extracted from facial videos into compact discrete tokens, referred to as face tokens, and conversely reconstructs 3D meshes from these tokens. We then extend Moshi with a Face Transformer module that generates face tokens non-autoregressively, enabling Moshi-Face to produce synchronized audio and face tokens in real time. Experiments show that Moshi-Face achieves audiovisual alignment at low latency while preserving the dialogue quality of the original audio-only model.

---


### 305. [REBA: A Revealed Belief Automaton Framework for Online Planning in Continuous POMDPs](https://arxiv.org/abs/2606.21971)

**<font color=#1a73e8>作者：</font>** Xiangwei Chen, Lingling Fang, Andreas Holzinger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Online planning in continuous partially observable Markov decision processes (POMDPs) using $\omega$-regular specifications requires handling continuous belief dynamics within the finite symbolic memory in order to track temporal progress. Existing methods based on either direct search in belief space or predefined discrete abstractions suffer from drawbacks, e.g., lack of symbolic memory for long-horizon logical progress or difficult to certify from noisy online beliefs. As such, obtaining reliable symbolic states online from continuous observations remains a challenge. To address this issue, we introduce the Revealed Belief Automaton (REBA), an event-driven framework that advances the research from global belief-space discretization to a fundamental new way of thinking, namely online certification of revelation events. Specifically, we propose an online revelation method that, through information-theoretic gates, can dynamically analyse and establish belief abstraction from the continuous belief space by discovering reliable anchors among noisy beliefs. We then develop an incremental topology adaptation mechanism over the certified anchors to realise the online finite Belief Automaton. By combining with the $\omega$-regular specification, REBA is able to support formal parity policy synthesis without a predefined discrete abstraction, which in turn can guide the Monte Carlo Tree Search process to perform online search beyond its local horizon. In addition, we design an error decomposition analysis which can assess the effectiveness and reliability of this discrete guidance for the underlying continuous POMDP. Empirical evaluations in patrolling and navigation scenarios show that REBA matches or exceeds all evaluated baselines, with primary metric gains of +17.0\% to +47.4\% over state-of-the-art approaches.

---


### 306. [Human vs Machine Mathematical Difficulty on Project Euler: An Experimental Analysis](https://arxiv.org/abs/2606.21972)

**<font color=#1a73e8>作者：</font>** David Holmes, Johannes Schmitt  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study how the effort and success probability of frontier AI systems scale with human difficulty on problems from Project Euler, an online platform of computational mathematics problems. Our dataset, from the MathArena benchmark, consists of 3840 attempts across 50 problems and 26 model configurations, with problem difficulty measured by the site's public human solve times. Motivated by a proposal of Timothy Gowers, we test a power-law relation $t_{\text{machine}} = a \cdot t_{\text{human}}^b$ between generated-token cost per successful answer and human time, and find $b < 1$ for 20 of the 25 models with usable fits, including the strongest base models; this operationalization therefore does not support an earlier prediction that machines scale worse than humans with difficulty. We also investigate whether success probability on the tested problems can be modeled by a simple exponential decay $p_{\text{success}} = e^{c t_{\text{human}}}$, predicting a linear relation between $\log p_{\text{success}}$ and $t_{\text{human}}$. Using a binning approach for data aggregation we find moderate empirical support (median bin-level $R^2 = 0.92$ across the 22 best-covered configurations) for this model. Following METR, we also fit logistic success curves and extract 50\% task-length horizons $h_{50}$; the strongest configurations in our 20 April 2026 snapshot reach roughly $2.5$--$4.3$ hours on our fastest-five human baseline, with a log-linear fit through the state-of-the-art frontier giving a descriptive doubling time of about $75$~days for the SOTA $h_{50}$.

---


### 307. [SPOTR: Spatio-temporal Pooling One-Token Reconstruction for Universal Physiological Signal Self-supervised Learning](https://arxiv.org/abs/2606.21973)

**<font color=#1a73e8>作者：</font>** Yiyu Gui, Mingzhi Chen, Yuesheng Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physiological signals such as EEG, ECG, and PPG are widely used in clinical monitoring. Recent self-supervised learning (SSL) methods offer an attractive way to leverage unlabeled recordings, yet they still fall short in practice. In particular, current SSL methods struggle across heterogeneous datasets, often distorting clinically meaningful structures or learning shortcuts from temporal and cross-channel redundancy. Consequently, existing SSL methods often deliver limited performance under linear probing, a lightweight adaptation setting that better matches real-world medical scenarios. Moreover, most Transformer-based SSL models encode a flattened spatiotemporal token sequence, incurring high computation and memory cost, and are typically developed within a single modality. To address these limitations, we present SPOTR (Spatio-temporal Pooling One-Token Reconstruction), a compress-reconstruct pretraining framework that introduces a single-token global bottleneck for physiological signals. SPOTR compresses each waveform into a single-token representation and reconstructs the signal conditioned only on this representation. Meanwhile, SPOTR introduces an efficient spatio-temporal compaction module to reduce computation and memory cost. Pretrained on 20 datasets spanning EEG, iEEG, ECG, and PPG, SPOTR consistently outperforms the strongest baseline under linear probing, improving average AUC by 18.49%, 21.71%, 17.86%, and 4.64%, respectively. Compared with a representative general-purpose time-series foundation model, SPOTR achieves around 78% lower latency and 52% lower peak GPU memory on average. The code can be found at this https URL.

---


### 308. [IRumAI: Reinforcement Learning for Indian Rummy](https://arxiv.org/abs/2606.21975)

**<font color=#1a73e8>作者：</font>** Vignesh Mohan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite its massive player base and complex hidden-information dynamics, Indian Rummy has received no reinforcement learning attention. Existing agents rely on combinatorial search, which is tactically strong but slow at inference. We present IRumAI, the first RL agent for the domain. IRumAI integrates Proximal Policy Optimization (PPO), meld-aware observation encoding, deadwood-driven reward shaping, and a dual-branch convolutional architecture. IRumAI is RL-trained solely against weak heuristics, after a one-time behaviour-cloning warm-start on stronger demonstration data. It generalises to defeat the entire baseline hierarchy, including a 53.9% win rate against the strongest search-based opponent unseen during RL training. Bypassing explicit search, IRumAI requires just 0.33 ms per action, which is over 7,000x faster than the state-of-the-art heuristic. Ablations validate our architectural choices, and linear probing reveals that the network implicitly models the opponent's hidden hand from public interactions.

---


### 309. [CoDMD: Copula-aware Distribution Matching Distillation for Fast Video Generation](https://arxiv.org/abs/2606.21982)

**<font color=#1a73e8>作者：</font>** Wenhu Zhang, Kun Cheng, Changyuan Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step distillation for video diffusion models has attracted significant attention, driven by the urgent demand for efficient deployment in real-world scenarios. However, Distribution Matching Distillation (DMD), a leading paradigm, tends to degrade under limited NFE budgets, manifesting in video generation as layout instability, oversaturation, and broken motion dynamics. We trace this failure to a structural limitation: standard DMD is an intra-sample distribution-matching objective with coordinate-wise gradients, and thus imposes no explicit constraint on the relational geometry across batch elements or temporal frames, leaving the underlying copula largely unregulated. Combined with the mode-seeking tendency of its reverse-KL objective, this absence of relational guidance makes DMD prone to collapsing into local optima in the few-step regime. Motivated by this insight, we propose Copula-aware DMD (CoDMD), a lightweight relational regularizer that reuses score estimates already produced by the frozen teacher and the online fake model to construct pairwise relation matrices across samples and frames. These are matched through a supplementary distributional objective that requires no additional networks, datasets, or sampling trajectories. On the Wan-2.1-T2V model series at 1.3B & 14B scales, CoDMD distills 50-step teachers into 4-step students, achieving an approximate 25$\times$ speed-up while attaining VBench scores of 84.46 & 84.87, outperforming prior trajectory-based (rCM 82.81 & 84.05) and distribution-based (DMD 83.38 & 83.81) methods.

---


### 310. [Adding Robust Code-Switching Capabilities to High Performance Multilingual ASR](https://arxiv.org/abs/2606.21990)

**<font color=#1a73e8>作者：</font>** Enes Yavuz Ugan, Alexander Waibel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Code-switching (CSW) remains challenging for large multi-lingual ASR systems in real-world deployment. While fine-tuning on synthetic CSW data is possible, it generally degrades strong monolingual baselines. Our goal is to preserve these capabilities while extending models to handle complex code-switching, including morphological variations across languages. We propose Bayesian factorized adaptation, which learns to efficiently integrate switching-relevant knowledge into strong pretrained models without overwriting existing capabilities. Requiring only a small amount of synthetic data, our approach reduces transcription errors by 32.87% on code-switched words while improving overall WER by 5.31%, all while maintaining mono-lingual performance. Our results demonstrate that effective CSW adaptation depends more on knowledge integration than data complexity.

---


### 311. [Prefix-Guided On-Policy Distillation: Mining Golden Trajectories from Rollouts](https://arxiv.org/abs/2606.21994)

**<font color=#1a73e8>作者：</font>** Qingfei Zhao, Huan Song, Shuyu Tian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) improves reasoning models by applying dense teacher supervision on student-sampled trajectories. However, scaling OPD to long-horizon mathematical reasoning exposes a reliability and efficiency problem: standard OPD assigns every sampled candidate the same long rollout budget, even though some trajectories may quickly become weakly aligned with the teacher and provide less useful supervision. Prior analyses suggest that successful OPD depends on local teacher-student compatibility, which can be measured by top-k overlap on student-visited prefixes. When this overlap is low, continuing to generate or train on long suffixes may waste computation and introduce noisy learning signal. To address this, we introduce Prefix-Guided On-Policy Distillation (PG-OPD), a simple rollout-allocation framework that uses fixed-length prefixes to estimate trajectory value before expensive long-horizon generation. PG-OPD first decodes every sampled candidate to the same prefix length, computes teacher-student top-k overlap within an early probe window of that prefix, and selectively continues high-overlap candidates to a fixed long length. Low-overlap candidates stop at the fixed prefix, avoiding unnecessary suffix generation. Across diverse teacher-student combinations on AMC, AIME, and HMMT benchmarks, PG-OPD improves average accuracy by up to 4.80 points while reducing training time by up to 2.46x. These results suggest that prefix-level compatibility provides a practical signal for directing OPD computation toward trajectories that remain learnable from the teacher.

---


### 312. [CFAgentBench: A Reproducible Environment and Benchmark for Autonomous Construction-Finance Agents](https://arxiv.org/abs/2606.22000)

**<font color=#1a73e8>作者：</font>** Rishi Srivastava  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce CFAgentBench, a reproducible, self-hostable environment and benchmark for autonomous construction-finance agents: a CFO/controller-class agent operating across the real software stack a US construction finance team runs - ERP, project management, email, documents, pay applications, payroll, certified payroll, lien waivers, and bank/treasury portals. It contains 1,014 machine-gradeable task specifications across 8 domains and 77 families, every family grounded in a real source; a self-validated subset of 40 tasks (54 with a project-management extension) is compiled into oracle-validated executable evaluators, the runnable suite reported here. Following WebArena, the benchmark runs on an executable environment rather than static traces: 35 mock applications (31 reconciled to one company book, plus 4 PM platforms) over 9 archetypes, each implementing a uniform self-hostable app contract, so every task is graded by functional correctness - a state diff plus forbidden-side-effect checks plus required-output regexes - with an LLM judge used only for reply quality, never as reward. A distinguishing principle is a money-movement guard: 278 instances embed a payment, payroll, e-signature, or e-filing step where the correct behavior is to stop and stage for human approval, and executing even the correct transaction fails the task. The public split (n=711) is sized for a 95% Wilson half-width of +/-4.1%; a private, contamination-protected split (n=303) is reserved for remote scoring. In a first three-model open-weight sweep (k=5), the strongest agent reaches pass^1 = 0.67 but only pass^5 = 0.38 - losing 43% of its successes when required to repeat them under temperature-0 decoding. The within-model pass^1 to pass^5 collapse and sharp per-domain heterogeneity are clear evidence that single-attempt accuracy overstates deployable construction-finance competence.

---


### 313. [Load Testing for Machine Learning Model Serving Systems at Scale](https://arxiv.org/abs/2606.22013)

**<font color=#1a73e8>作者：</font>** Amr S. Abdelfattah, Nakul Tirumalai, Indu Mohanan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning (ML) model serving has become a dominant consumer of GPU infrastructure, yet capacity planning in these systems remains largely ad hoc. Under-provisioning leads to service-level objective (SLO) violations and production incidents, while over-provisioning results in substantial resource waste. This paper presents \sys, an industrial load testing framework for ML serving systems that systematically estimates serving capacity through an adaptive, feedback-driven search strategy. The approach leverages real-time performance signals, incorporating dampening, spike tolerance, and convergence detection to efficiently identify maximum sustainable throughput under SLO constraints. We evaluate \sys through a longitudinal analysis of 14 industrial case studies spanning four ML architecture classes: recommendation, ranking, vision, and NLP. This study demonstrates that systematic load testing leads to substantial improvements in GPU resource efficiency and operational reliability. Prior to adopting \sys, a significant fraction of model launches were under-provisioned, resulting in recurring incidents; these issues were substantially reduced after deployment. Our results show that ML-specific design decisions are critical to accurate capacity estimation: workload calibration using recorded traffic reduces estimation error from approximately 30\% to 2--6\%, while proper warmup handling yields a 22.2\% improvement in accuracy. Further analysis reveals key factors influencing prediction error, including model size and co-location effects. This paper distills six lessons and derive architectural guidelines for ML load testing, offering actionable insights for building reliable and efficient ML serving systems.

---


### 314. [Cluster-Specific Localized Drift Detection for Efficient Batch Model Adaptation under Controlled Distribution Shift](https://arxiv.org/abs/2606.22026)

**<font color=#1a73e8>作者：</font>** Ignacio Cabrera Martin, Marcello Trovati, Almas Baimagambetov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning systems deployed in dynamic environments frequently operate under nonstationary data distributions, where controlled distribution shift can progressively degrade predictive performance. However, many widely used tabular benchmark datasets lack explicit temporal structure, limiting reproducible evaluation of drift adaptation methods. This work proposes a cluster-induced distribution shift simulation framework that transforms static tabular datasets into controlled evolving data streams through structured perturbations across featurespace partitions. Using this framework, six adaptation strategies are systematically evaluated: static learning, sliding-window retraining, global ADWIN retraining, cluster-local ADWIN retraining, random subspace drift detection, and feature-partitioned drift detection. Experiments are conducted on five benchmark datasets covering both classification and regression tasks using diverse predictive model families, including linear models, k-Nearest Neighbours, tree ensembles, boosting methods, and adaptive online learners.

---


### 315. [Topological summaries of fingerprint ridge patterns carry identity information](https://arxiv.org/abs/2606.22029)

**<font color=#1a73e8>作者：</font>** Chad M. Topaz, Niny Arcila-Maya, Elizabeth Munch 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fingerprints are the most widely deployed biometric. Verifying whether two impressions come from the same finger typically relies on minutiae, small landmarks such as skin ridge endings and bifurcations. These landmarks are extracted through a multi-stage pipeline of image enhancement, skeletonization, minutiae detection, and alignment. We investigate an alternative: using topological data analysis to represent the full pattern of skin ridges and valleys directly, bypassing minutiae detection and the downstream matching pipeline. We apply persistent homology, a topological tool that tracks how loops in the ridge pattern form and fill in across spatial scales, producing multi-scale summaries of ridge geometry. We develop and compare a range of verification methods on a standard benchmark dataset, FVC2000 DB1. Even the simplest topological summaries, with no trained parameters, substantially outperform geometry-only baselines. A trained method achieves an AUC of 0.91, while an optimal-transport method excels at the strictest false-accept thresholds, suggesting they capture different aspects of the ridge pattern. Fusing these two approaches yields the best performance at every low false-accept threshold we examine. Our results establish that these topological summaries capture substantial fingerprint identity information, far more effective for verification than raw pixel-level geometry. Because the entire pipeline is openly specified, it offers a transparent complement to minutiae-based systems, and we provide a modular framework for constructing, evaluating, and combining topological verification methods.

---


### 316. [A Completion-Aware Framework for Impactful Counterfactual Explainability in Graph Neural Networks](https://arxiv.org/abs/2606.22033)

**<font color=#1a73e8>作者：</font>** Maria Myrto Villia, Filippos Gouidis, Theodore Patkos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this study, we propose a novel pipeline for generic, model-agnostic, local-level counterfactual explainability in graph neural networks (GNNs). Although counterfactual explainers capable of both adding and removing edges have emerged in recent years, the need for generic and efficient solutions remains unmet, particularly concerning qualitative explanation generation. Our approach couples progress in factual explainability with missing edge prediction models rooted in link prediction research, in order to enhance the quality, robustness and intuitiveness of explanations. A multi-faceted experimental analysis conducted on real-world and synthetic graph classification benchmarks, both binary and multi-label, demonstrates the advancements in comparison to state-of-the-art baselines across diverse metrics.

---


### 317. [Attractor Domain Theory: A Mathematical Framework for Cardiovascular Attractor Analysis with Wearable Photoplethysmography (PPG) Validation](https://arxiv.org/abs/2606.22039)

**<font color=#1a73e8>作者：</font>** Timothy Oladunni, Farouk Ganiyu Adewumi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The cardiovascular system evolves along a bounded trajectory in physiological state space that converges to a compact geometric object: the cardiac attractor. A wearable photoplethysmograph (PPG) or electrocardiograph (ECG) observes a one-dimensional projection of this attractor; by Takens' embedding theorem, delay coordinates reconstruct its full geometry. Three decades of nonlinear cardiac dynamics have extracted Lyapunov exponents, recurrence statistics, and sample entropy from reconstructed attractors, yet no principled account exists of which attractor properties capture which cardiovascular quantities, or why, leaving feature selection as a search problem and negative results uninterpretable. We introduce Attractor Domain Theory (ADT), which proves that the reconstructed attractor's information partitions into three mutually non-redundant domains: the Geometry Domain G (delay embedding; native capability: artifact rejection), the Ergodic Domain S (asymptotic statistical invariants; native capability: stability estimation), and the Variational Domain V (finite-time Lyapunov exponent field; native capability: hemodynamic inference). We prove a Domain Sufficiency Theorem (the Parseval analog for attractor information) and establish that three domains are necessary and sufficient. Geometry Domain validation via the SCSI framework across 176,742 PPG segments from four datasets yields AUC = 0.757 [0.686-0.828] and NPV = 0.966 after correcting three systematic evaluation artifacts (+0.179 net inflation). Ablation confirms C_NL as the dominant Geometry Domain component (Delta AUC = -0.413) and intra-domain redundancy across five components.

---


### 318. [IDAG-Edit: Multi-Object Video Editing via Instance-Decoupled Attention and Guidance](https://arxiv.org/abs/2606.22042)

**<font color=#1a73e8>作者：</font>** Yuan-Zhih Lin, Huu-Thang Nguyen, Huu-Phu Do 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based video editing has made significant progress; however, achieving precise and temporally consistent object-level control, especially in multi-object scenarios, remains challenging due to attention leakage, identity drift, and unstable temporal dynamics. In this work, we propose IDAGEdit, a training-free framework for fine-grained multi-object video editing with strong temporal consistency. The framework adopts Layout-guided Attention Modulation to facilitate coherent multi-object editing, while Instance-level Masks are introduced to preserve individual object identity and enforce localized attention within each object region, thereby enabling fine-grained, object-level editing. Extensive qualitative and quantitative evaluations demonstrate that our method improves temporal stability and multi-object controllability over state-of-the-art video editing approaches.

---


### 319. [Gradient-Descent Steps to Success over Mean Accuracy: A Paradigm Shift for ML](https://arxiv.org/abs/2606.22053)

**<font color=#1a73e8>作者：</font>** Riccardo Poli, Ahmet Yilmaz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traditional evaluation of machine learning (ML) models typically focuses on achieving the maximum possible accuracy irrespective of the computational cost. In this article, we propose a paradigm shift towards evaluating performance based on computational effort-explicitly defined here as the total number of gradient descent steps required to reach an acceptable level of accuracy with high probability. Building upon the concept of computational effort originally introduced by Koza for Genetic Programming, we extend this metric to any ML model trained via gradient descent. Furthermore, we demonstrate that minimising this effort acts as a novel form of Automatic Machine Learning (AutoML). By evaluating it across 11 diverse ML models and five standard classification datasets, we uncover significant insights into the dynamics of gradient-based learning. Our findings reveal that optimal hyper-parameters consistently favour unusually large learning rates. Crucially, we demonstrate that the rapid, aggressive landscape traversal enabled by these large rates not only promotes generalisation-as seen in phenomena like superconvergence-but also statistically minimises the expected computational effort for training. Furthermore, we identify distinct phase transitions in the optimal search strategy: while a single training run suffices for lower accuracy targets, reaching a model's performance limit requires a dramatic shift towards conducting numerous independent, short restarts. Finally, we illustrate how this effort-based paradigm provides a robust framework for model selection, allowing practitioners to choose optimal algorithms based on the difficulty of a problem as perceived by different models for a given target accuracy, or to maximise the achievable accuracy for a fixed budget of gradient descent steps.

---


### 320. [Provably Efficient Policy-Reward Co-Pretraining for Adversarial Imitation Learning](https://arxiv.org/abs/2606.22056)

**<font color=#1a73e8>作者：</font>** Tian Xu, Zexuan Chen, Zhilong Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial imitation learning (AIL) achieves high-quality imitation compared to behavioral cloning (BC), but demands substantial online environment interaction. Recent empirical work has explored initializing AIL algorithms with BC pretrained policies to address this limitation, yet a rigorous theoretical understanding of pretraining's role in AIL remains elusive. This paper provides a systematic theoretical analysis and introduces principled pretraining algorithms for accelerating AIL. We begin by analyzing AIL with policy pretraining alone, identifying reward error as the dominant source of suboptimality. This reveals a critical and previously overlooked gap: the absence of reward pretraining. Motivated by this finding, we develop a principled policy-reward co-pretraining approach grounded in a reward shaping analysis. Our analysis uncovers a fundamental connection between expert policies and shaping rewards, which naturally gives rise to CoPT-AIL, an approach that jointly pretrains both policy and reward through a single BC procedure. We prove that CoPT-AIL achieves an improved imitation gap bound over standard AIL, establishing the first theoretical guarantee for the benefits of pretraining in AIL. Experimental results confirm CoPT-AIL's superior performance over existing AIL methods.

---


### 321. [The Cognitive Trajectory Laboratory: Modeling the Creative Process Through Time in Art Therapy](https://arxiv.org/abs/2606.22057)

**<font color=#1a73e8>作者：</font>** Nicholas Davis  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Art therapy has demonstrated effectiveness across diverse clinical populations, and its theoretical traditions have generated valuable perspectives on symbolism, expression, narrative reconstruction, meaning-making, physiological responses, and neurobiological processes. While these approaches provide important accounts of therapeutic experience and change, they have placed comparatively less emphasis on how cognition, regulation, and interaction dynamics evolve during the creative process itself, making it difficult to analyze how creativity and therapeutic outcomes emerge through time. As a result, art therapy research continues to rely heavily on qualitative interpretation, outcome measures, and retrospective self-report, while the dynamics of therapeutic change remain difficult to quantify. This paper proposes an enactive, dynamical framework for understanding and measuring cognitive change in art therapy through the analysis of creative interaction dynamics over time. Within this framework, therapeutic change is hypothesized to be reflected in cognitive trajectories, temporally unfolding patterns of engagement that reveal shifts in stability, exploration, and adaptation. To operationalize this framework, the paper introduces the Cognitive Trajectory Laboratory (CTL), an instrumented drawing environment that transforms interaction traces into cognitive trajectories unfolding through time, enabling the identification of emergent properties, significant events, and overarching chapters of the creative process. By making the dynamics of creative engagement measurable, the proposed framework and accompanying laboratory provide new methodological tools for art therapy assessment and research while creating opportunities for longitudinal analysis of therapeutic change. Implications are discussed for process-oriented evaluation and computational modeling of creative engagement.

---


### 322. [NL2Scratch: An Executable Benchmark and Evaluation for Block-Based Programming](https://arxiv.org/abs/2606.22061)

**<font color=#1a73e8>作者：</font>** Heejin Do, Alexandre Ballenghien, Yang Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Block-based programming environments such as Scratch are widely used in early programming education, yet natural-language-to-code (NL2Code) research has focused primarily on text-based languages. Scratch programs are event-driven, visually compositional, and distributed across concurrent scripts, making conventional NL2Code assumptions and evaluation insufficient. We introduce NL2Scratch, an executable benchmark for natural-language-to-Scratch generation comprising 311,648 parser-valid NL--program pairs, whose program side is extracted from real Scratch projects and paired with semantically aligned NL descriptions. For reliable evaluation beyond surface overlap, we propose Semantic Alignment Consistency (SAC), an interpretable slot-level metric for measuring semantic agreement between descriptions and programs. With SAC, we construct a semantically validated pool of 23,594 examples, and a slot-balanced 800 diagnostic benchmark. Experiments across instruction-tuned and fine-tuned LLMs reveal a notable gap between lexical similarity and semantic alignment: models achieving token-level F1 above 0.93 often fail to attain perfect SAC, particularly on longer examples. Errors concentrate on operational slots like actions, conditions, and numeric arguments, exposing failure modes largely invisible under conventional metrics.

---


### 323. [Guarded Equivalence Predicates for Scalable Formal Hardware Information-Flow Verification](https://arxiv.org/abs/2606.22063)

**<font color=#1a73e8>作者：</font>** Liangtao Dai, Yimin Gao, Melika Morsali 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Formal hardware information-flow verification is a principled way to rule out secret-dependent functional or timing observations, but scaling such proofs remains difficult. Self-composition reduces information-flow verification to safety checking over two circuit copies, creating relational proof obligations that are hard for a generic PDR engine to discover from bit-level logic alone. Recent PDR-based techniques exploit this duplicated structure through copy symmetry and global cross-copy equivalence predicates. These predicates are effective when corresponding internal signals agree throughout the reachable state space, but they do not capture equalities that are relevant only in a specific control context. We observe that such contextual relations arise naturally in hardware IFV proofs: an internal signal pair may need to agree only within a control phase, transaction window, loop state, or protocol region. We introduce guarded equivalence predicates to expose these relations to PDR. Rather than treating a proposed contextual equality as an assumption, the verifier submits the corresponding mismatch condition as an auxiliary blocking obligation. Guards are proposed from relational counterexamples-to-induction using CTI-local extraction and state-split search; only candidates proved unreachable by the backend affect the proof. Across 12 IFV benchmarks and two PDR backends, guarded predicates convert two contextual baseline timeouts into completed proofs within 34.2--89.5s under an 1800s limit, while reducing proof time by up to 10.8x on additional benchmarks.

---


### 324. [New Smooth Loss functions for Robust Regression that Closely Approximate Absolute Error and Provide Improved Performance on Datasets With Significant Outliers](https://arxiv.org/abs/2606.22068)

**<font color=#1a73e8>作者：</font>** Mathew Mithra Noel, Arindam Banerjee, Yug D. Oswal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The performance of supervised machine learning models is directly related to the quality of the training dataset. In particular, the presence of significantly many outliers in the training data can lead to low accuracy because popular loss function like the Mean Squared Error (MSE) assign very high importance to large errors. The Mean Absolute Error (MAE) loss assigns equal importance to all errors and is most robust to outliers, but suffers from being non-differentiable at the origin. MAE also has large derivative values close to its minimum leading to instability and oscillations during training. Thus differentiable approximations to MAE namely Huber and Log-Cosh losses were introduced for robust regression tasks. This paper introduces two new infinitely differentiable loss functions that more closely approximate the MAE loss and provide improved performance on regression tasks with significantly many outliers in the training dataset. A comparison of the performance of regression models with different loss functions on a wide variety of benchmarks and datasets is presented to demonstrate the superior performance of the Square Root Loss (SRL) and Smooth Mean Absolute Error (SMAE) losses proposed in this paper. The SRL loss is shown to be strictly convex and the SMAE loss is shown to be strictly quasi-convex. Given the fundamental importance of linear regression, two new robust linear regression models are presented.

---


### 325. [A Controlled Study of CLIP-Based Body-Scene Fusion for Emotion Recognition in Context](https://arxiv.org/abs/2606.22072)

**<font color=#1a73e8>作者：</font>** Zubair Abbas, Muhammad Umair, Muqaddas Hameed  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Apparent emotion in natural images is often not visible from the face alone. The face may be small, hidden, or neutral, while posture and scene context carry much of the evidence. This work studies context-aware emotion recognition on EMOTIC with an image-only two-stream model. A ResNet-18 body stream encodes the target-person crop, and a CLIP ViT-B/16 scene stream encodes the full image. The fused feature predicts 26 categorical emotion labels and the continuous valence, arousal, and dominance values. This study examines whether small context-debiasing or rare-class training changes still help after adding a CLIP scene encoder. The clean two-stream model is compared with simplified CCIM-style intervention, CLEF-lite context-bias subtraction, ASL tuning, and class-balanced sampling under the same implementation pipeline. No tested variant improves over the clean two-stream model, which achieves 34.52% mAP on the EMOTIC test split. CLIP gives the model broad scene semantics, but the simplified causal, counterfactual, and rare-class changes do not automatically improve performance. Most remaining errors are in rare and subtle emotion categories, so the next step should focus on label relationships and finer subject-context interaction.

---


### 326. [Frequency-Domain Neural ODEs for Modeling Non-Linear Dynamical Systems](https://arxiv.org/abs/2606.22075)

**<font color=#1a73e8>作者：</font>** Mohammed Ashraf, Ayman A. El-Badawy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard continuous-depth models, such as Neural Ordinary Differential Equations (NODEs), offer significant advantages in modeling physical systems by learning continuous vector fields rather than discrete temporal steps. However, when applied to complex dynamical systems, standard NODEs frequently struggle with highly nonlinear dynamics. This paper investigates the Frequency-domain Neural ODE (FNODE), an architecture that projects continuous temporal dynamics into the frequency domain using the Fast Fourier Transform (FFT). By operating in the frequency domain, the model provides better generalization to the dynamical system. The architecture is empirically evaluated against discrete models, specifically Gated Recurrent Units (GRUs) and Long Short-Term Memory (LSTMs), and other continuous-depth variants, including Augmented Neural ODE (ANODE), across four distinct dynamical systems: the Lotka-Volterra model, the forced Duffing oscillator, the Van der Pol oscillator, and the Lorenz system. To rigorously assess generalization and robustness, curriculum and ensemble learning are used to evaluate the model's convergence by estimating confidence intervals across different ensemble models. The empirical results demonstrate that the FNODE architecture achieves better generalization while exhibiting remarkable convergence stability.

---


### 327. [Learning Cross-View Semantic Priors for Single-Reference Unseen Object Pose Estimation](https://arxiv.org/abs/2606.22076)

**<font color=#1a73e8>作者：</font>** Jiahong Chen, Jinghao Wang, Ziwen Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-reference unseen object 6D pose estimation reduces object onboarding by estimating poses of arbitrary novel objects from only one reference view. Recent correspondence-based pipelines have achieved robust performance with vision foundation model (VFM) features. However, they typically treat these features as intra-view descriptors, leaving dense visual-semantic cues, including appearance, structure, and context, insufficiently exchanged across views before geometric decoding. Consequently, the decoded point features may lack joint semantic and geometric discriminability, making correspondence estimation still difficult in challenging cases. Instead of processing features independently, we build the correspondence pipeline around an early cross-view semantic prior. Specifically, cross-view semantic interaction (CVSI) enables dense query and reference VFM tokens to exchange semantic context and form a cross-view prior. Nevertheless, direct CVSI may disturb the VFM token structure, while the resulting semantic prior still needs 3D representation consistency for rigid correspondence. To make this CVSI prior reliable for 3D correspondence learning, we introduce two complementary training-time constraints: the intra-view structure preservation (IVSP) loss preserves the original intra-view token affinity structure during interaction, while the reference-anchored geometric consistency (RAGC) loss enforces spatial representation consistency of decoded point features. The final pose is recovered from learned correspondences through weighted SVD. We further construct a challenging view-pair protocol from the BOP Challenge datasets YCB-V and TUD-L to evaluate robustness in difficult matching scenarios. Extensive experiments on six benchmarks under different view-pair settings show that our method achieves state-of-the-art performance while maintaining comparable inference speed.

---


### 328. [Where Does the Signal Live? A Web Data Recipe for Medical Encoder Pretraining](https://arxiv.org/abs/2606.22079)

**<font color=#1a73e8>作者：</font>** Bofeng Huang, Jacques Sun, Diane Bouchacourt 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Web data curation has been widely studied for decoder Large Language Model (LLM) pretraining. Encoders for dense-terminology domains such as medicine, by contrast, are pretrained on small, manually-curated corpora that limit scalability and writing style diversity, a bottleneck even more severe in non-English clinical settings. Whether web-scale data curation also benefits encoder Masked Language Modeling (MLM) in a dense-terminology domain remains an open question. To address this, we introduce two complementary levers. Medical-term density filtering selects documents rich in medical terms. Signal-amplifying rephrasing uses an LLM to rewrite documents into denser variants with broader entity contexts. We instantiate the recipe on French medical NLP. The medical-term density filter outperforms the widely-used educational quality filter on downstream medical tasks, and the two complement each other. Signal-amplifying rephrasing alone improves on raw web data, and mixing it with filtered web data produces the largest gain. The recipe yields FineMed, a French medical pretraining corpus, and DoctoBERT, a state-of-the-art French medical encoder family evaluated on both the public benchmark DrBenchmark and a proprietary clinical Named Entity Recognition (NER) task.

---


### 329. [BAC-JEPA: Label-Efficient Breast Arterial Calcification Segmentation via Synthetic Mammography-Guided Supervision](https://arxiv.org/abs/2606.22089)

**<font color=#1a73e8>作者：</font>** Scott Chase Waggener, Lakshman Tamil  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Breast arterial calcification (BAC) on screening mammograms is an emerging cardiovascular risk biomarker, but quantitative use requires reproducible segmentation and expert pixel-level labels are costly. We present BAC-JEPA, a label-efficient segmentation framework trained on procedurally generated arterial calcification inserted into real mammographic backgrounds with exact masks. Candidate backgrounds were selected from model-screened mammograms with low predicted BAC response; the generator samples arterial structure, disease burden, radiographic appearance, and hard-negative distractors including nonarterial calcifications and metallic objects. Synthetic masks are paired with mammography self-supervised Vision Transformer encoders and a high-resolution convolutional decoder to produce full-resolution segmentation maps. The study used 75,472 mammography studies from 34,956 patients for background selection and representation learning, trained on synthetic images from 10,000 backgrounds, selected checkpoints with 1,000 development backgrounds, and evaluated transfer on all 1,000 human-labeled BacSeg synthetic 2D mammograms. On held-out synthetic validation data, the larger backbone achieved IoU 0.5325 and Dice 0.6357. On BacSeg, image-level classification from segmentation probability maps reached AUROC 0.8719, with 0.8547 for the smaller backbone. Four-view inference required 110.68--213.63 ms on an RTX 5090 GPU, and severe-preset synthetic image generation averaged 2.7071 s per image on a multicore workstation. These results indicate that BAC-specific synthetic supervision can produce useful image-level transfer without human pixel-level training masks, while expert-reviewed real-mammogram segmentation remains necessary for clinical validation and calibration.

---


### 330. [Cross-View Yaw Estimation in Location Uncertainty with Line-Aligning Yaw Scoring](https://arxiv.org/abs/2606.22094)

**<font color=#1a73e8>作者：</font>** Taeho Kang, Nairan Zhang, Yelin Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate yaw estimation is a bottleneck in cross-view localization between ground view and Bird's Eye View (BEV). Existing methods couple yaw with translation and rely on height or projection assumptions that degrade under large yaw ambiguity. We disentangle yaw from location accuracy and introduce LAYS, a radially invariant line-consensus voting method. By exploiting the radial invariance of our formulation, we achieve sub-degree yaw precision via 3D voting over all candidate poses, while eliminating the need for accurate location. Our key observation is that a ground-image column matched to BEV pixels induces the same yaw across all camera positions along the radial direction of the pixels. LAYS matches BEV pixels to ground columns using feature similarity and accumulates the induced yaw votes into discrete 3D bins, where correct correspondences along the radial line concentrate into a sharp peak for the correct yaw. Experiments on Mapillary, Ford, KITTI, and VIGOR show significant gains under unknown yaw, particularly for normal FoV with unknown yaw (+28$\sim$45\%p), and using LAYS as a yaw prior improves downstream 3-DoF localization.

---


### 331. [Plurification in/of language technology -- The integration of culture in next-generation AI](https://arxiv.org/abs/2606.22097)

**<font color=#1a73e8>作者：</font>** Gertraud Koch, Fausto Giunchiglia  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The paper explores how "culture" can be operationalised in Natural Language Processing (NLP) and what this reveals about the possibilities and limits of considering a plurality of cultural backgrounds in technological design. It proposes that cultural alignment cannot be achieved only by adding more examples of "other cultures", rather it requires plural epistemologies: allowing multiple, locally grounded ways of knowing. To analyze how this plurality of knowing can be addressed in NLP, the paper uses a socio-technical model of language technology (LT) design, the five layers of technological activity model, for collecting and systematizing approaches to culture in NLP. The analysis shows that while NLP research has made progress toward more culturally sensitive systems, many approaches remain partial, addressing "culture" primarily at the level of output or representation while leaving deeper questions of power, governance, and social context unresolved. The paper concludes that operationalising culture requires much more than technical adaptation; it suggests a reflexive and plural socio-technical approach that navigates potentials and limits of computational formalisation for accounting multiple linguistic and socio-cultural backgrounds.

---


### 332. [OphthaDT: Generative Digital Twins for Forecasting Visual Acuity Trajectories in Ophthalmology](https://arxiv.org/abs/2606.22101)

**<font color=#1a73e8>作者：</font>** Pietro Belligoli, Nikita Makarov, Sayedali Shetab Boushehri 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Precision medicine in ophthalmology requires accurate longitudinal predictions, but the fragmented nature of multimodal clinical data remains a barrier to forecasting. We introduce OphthaDT, an LLM-based digital twin for ophthalmology that serializes longitudinal patient histories from 3,220 patients across four Phase III clinical trials into structured narratives to forecast best corrected visual acuity (BCVA). In benchmarks spanning up to 100 weeks, OphthaDT demonstrated the lowest prediction error in neovascular age-related macular degeneration (nAMD), achieving an average mean absolute error (MAE) reduction of 6.0% compared to all baselines. In diabetic macular edema (DME), OphthaDT demonstrated competitive performance against all baselines while outperforming Random Forest and XGBoost by an average MAE reduction of 2.6% and 6.9%, respectively. Results reveal that OphthaDT's predictive advantage scales with trajectory complexity: whereas linear models remain effective for the more stable treatment responses of DME, OphthaDT's capacity is better suited for capturing the high longitudinal variability of nAMD. Finally, OphthaDT handles irregular sampling without imputation, positioning LLM-based clinical trajectory modeling as a methodology that could reduce patient burden and accelerate drug development.

---


### 333. [Accurate identification and measurement of the precipitate area by two-stage deep neural networks in novel chromium-based alloys](https://arxiv.org/abs/2606.22112)

**<font color=#1a73e8>作者：</font>** Zeyu Xia, Kan Ma, Sibo Cheng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The performance of advanced materials for extreme environments is underpinned by their microstructure, including the size and distribution of reinforcing phases. Chromium-based superalloys are a recently proposed alternative to conventional face-centred-cubic superalloys for high-temperature applications, such as Concentrated Solar Power, and their development requires efficient measurement of precipitate volume fraction and size distribution from electron microscopy images. Traditional fixed-threshold image processing is sensitive to background noise, generalises poorly across materials, and requires substantial manual measurement effort. To address these bottlenecks, this study proposes DT-SegNet, an end-to-end two-stage deep learning scheme based on YOLOv5 and SegFormer for object detection and segmentation in electron microscopy images. The approach combines the training efficiency of convolutional neural networks at the detection stage with the segmentation accuracy of a Vision Transformer. Numerical experiments show that DT-SegNet substantially outperforms state-of-the-art segmentation tools offered by Weka and ilastik across metrics including accuracy, precision, recall, and F1-score. The model provides a useful tool for alloy-development microstructure examinations and helps address the large datasets associated with high-throughput alloy development.

---


### 334. [Surgical Anatomy Recognition with Context Learning using Foundation Representations](https://arxiv.org/abs/2606.22124)

**<font color=#1a73e8>作者：</font>** Ronald L. P. D. de Jong, Tim J. M. Jaspers, Raf A. H. Vervoort 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate recognition of anatomical structures is essential for safe and effective minimally invasive surgery (MIS), yet it remains underexplored in surgical computer vision due to limited annotated data and methods tailored primarily to natural scenes. In this work, we present a combined dataset and model framework to advance anatomy-aware perception in MIS. First, we introduce ATLAS-120k, a large-scale clip-level semantic segmentation dataset comprising over 120,000 annotated frames from 100 surgical videos spanning 14 procedures and multiple modalities, including laparoscopic and robot-assisted surgery. The dataset captures substantial procedural variability and was created using a scalable annotation pipeline that integrates expert manual labeling, automated propagation, iterative refinement, and surgeon verification to ensure high-quality annotations. Second, we propose ATLAS (Anatomy Recognition with Context Learning using Foundation Representations), a video semantic segmentation model specifically designed for surgical anatomy recognition. Unlike conventional approaches that emphasize object tracking, ATLAS leverages foundation-model embeddings together with lightweight temporal reasoning to incorporate contextual cues such as procedure type, surgical phase, and short-term visual memory. This design enables temporally consistent and accurate predictions while maintaining real-time feasibility. Together, the dataset and model establish a practical foundation for robust surgical scene understanding and support the development of clinically applicable guidance systems for minimally invasive surgery. The models, dataset annotations and annotation platform are publicly available at: this https URL.

---


### 335. [Feed-forward Motion In-betweening for Any 4D](https://arxiv.org/abs/2606.22131)

**<font color=#1a73e8>作者：</font>** Hiroki Nishizawa, Hubert P. H. Shum, Yoshihiro Fukuhara 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 4D dynamics (3D geometry evolving over time) is a fundamental representation of the physical world and plays a crucial role in world modeling (e.g., animation and games). Owing to the scarcity of large-scale, long-horizon 4D mesh data with arbitrary shapes, early text-to-4D methods rely on distillation or test-time optimization from video diffusion priors, making inference prohibitively slow. Recent feed-forward generators greatly reduce inference cost but offer limited spatiotemporal controllability, and short-horizon generation often leads to error accumulation in long-horizon sequences. We propose a novel feed-forward in-betweening framework for arbitrary 4D meshes with keyframe conditioning. Building on universal mesh-animation latents, we introduce a frame-wise mesh VAE that encodes each frame into topology-agnostic latent tokens anchored by a reference mesh for keyframe conditioning. We further introduce a keyframe-conditioned rectified flow model with an MMDiT backbone that synthesizes non-keyframe frames conditioned on sparse keyframes. Experiments show strong performance and improved controllability on both DyMesh16 and DyMesh32 benchmarks.

---


### 336. [Meta-Reinforcement Learning via Evolution for Multi-Objective Combinatorial Supply Chain Optimisation](https://arxiv.org/abs/2606.22146)

**<font color=#1a73e8>作者：</font>** Rifny Rachman, Bahrul Ilmi Nasution, Josh Tingey 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Meta-reinforcement learning is a promising approach to multi-objective optimisation because it enables rapid policy adaptation across changing environments and preference settings. However, conventional few-shot methods usually fine-tune from a single shared meta-policy, which can reduce solution diversity and limit exploration of the Pareto front, especially in high-dimensional combinatorial problems such as supply chain optimisation. We propose a population-based Meta-reinforcement learning framework that combines decomposition with evolutionary search in scalarisation weight space. The framework maintains a population of weight vectors, each associated with a distinct meta-policy trained through gradient-based meta-learning, and iteratively refines this population through elitist selection, crossover, and mutation guided by hypervolume and entropy contributions. We evaluate the method in a multi-objective supply chain setting with conflicting economic, environmental, and social goals, and further test its generality on standard reinforcement learning problems. The results show that the proposed approach yields more diverse, better distributed Pareto front approximations, improves cross-task adaptation, increases hypervolume by up to 32\% over Meta-multi-objective reinforcement learning in the complex case, and attains the lowest average Hausdorff distance among all compared methods.

---


### 337. [Parameterized Representations via Implicit Stochastic Modulation for High-Dimensional and High-Order Neural PDE Solvers](https://arxiv.org/abs/2606.22150)

**<font color=#1a73e8>作者：</font>** Zhangyong Liang, Huanhuan Gao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Solving high-dimensional and high-order PDEs is challenged by the coupled growth of spatial dimensionality and derivative order. Recent stochastic derivative estimators reduce this cost by replacing full derivative tensors with randomized dimension or Taylor estimators, but they are mostly designed for fixed physical parameters and require retraining for each new parameter. We show that direct conditional parameterization of such solvers entangles physical parameters with the high-order automatic differentiation graph, causing extra memory growth and parameter-induced variance amplification. We propose Parameterized Representations via Implicit Stochastic Modulation (PRISM), a plug-and-play framework for parameterized high-dimensional and high-order stochastic neural PDE solvers. PRISM uses a hyper-generator to map physical parameters to affine modulators that scale and shift a purely spatial latent manifold, while keeping parameter branches value-connected but spatial-tangent-disconnected. This design preserves unbiased stochastic dimension and Taylor estimators, removes the parameter encoder from high-order spatial AD, and provides a variance-aware Lipschitz envelope over the parameter space. We prove parameterized unbiasedness, estimation-error bounds, and convergence under bounded stochastic variance. Experiments with PRISM-STDE and PRISM-SDGD on nonlinear parameterized PDEs show stable zero-shot generalization, reduced memory usage, and scalability up to 100,000 dimensions on a single GPU, with efficient low-rank SVD adaptation for unseen parameters.

---


### 338. [Drowning in Routine: Signal Dilution in Multi-Turn Agent Training](https://arxiv.org/abs/2606.22164)

**<font color=#1a73e8>作者：</font>** Yann Pernot, Vi Retault  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-turn agents interleave consequential decisions with routine execution: some actions change the downstream return distribution, while others are necessary but reward-equivalent. The cost of trajectory-level credit assignment, often attributed to long horizons, is in fact governed by decision density $\rho$: the fraction of turns whose actions affect the return. When decision density is low, routine turns create signal dilution: they add gradient variance to trajectory-level estimators such as GRPO without adding expected signal. Under explicit assumptions, the resulting turn-level to trajectory-level signal-to-noise ratio scales as $\rho^{-1/2}$, provided critic error remains controlled. The same analysis identifies the complementary regime: at high decision density, trajectory-level methods can remain competitive while avoiding the cost of a critic. In a controlled environment where $\rho$ is exactly tunable, the predicted scaling is recovered with $R^2 = 0.999$, and the training-step gap widens significantly as $\rho \to 0$.

---


### 339. [Early-Exit Graph Neural Networks for Link Prediction](https://arxiv.org/abs/2606.22167)

**<font color=#1a73e8>作者：</font>** Roman Knyazhitskiy, Andrea Giuseppe Di Francesco  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks are great for link prediction in various network-like structures; however, the question of their speed/quality tradeoff has been barely studied. While in practice the time it takes to do inference matters little for small benchmarks, the latency does limit applicability in large-scale domains. In this work, we explore early-exiting strategies that can be applied to Graph Neural Networks to solve the problem of link-prediction faster. We use no auxiliary losses to enforce early exiting, allowing it to emerge as an implicit property of the architecture. We show that our method enables early exiting in several setups, moving the Pareto frontier on the HeaRT benchmark for GCN and SAS-GNN backbones. Our findings show that inference speed of GNNs on many link-prediction problems can be improved, while losing little, or even winning in terms of prediction quality. The code is available in our repository: this https URL.

---


### 340. [From Convolution to Transformer: A Comparative Study of U-Net Variants for Brain Tumor and Retinal Vessel Segmentation](https://arxiv.org/abs/2606.22168)

**<font color=#1a73e8>作者：</font>** Khoa Pham, Sindhuja Penchala, Jiacheng Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image segmentation plays an important role in computer aided diagnosis, treatment planning, and disease monitoring. U-Net has been widely used for biomedical image segmentation because of its encoder decoder structure and skip connections. However, conventional convolution based U-Net models may have limited ability to capture long range dependencies and global contextual information, which can affect performance in complex segmentation tasks. This paper presents a comparative study of five U-Net based architectures: U-Net 3D, Residual U-Net, Attention U-Net, UNETR, and Swin UNETR. The models are evaluated on two benchmark datasets: BraTS 2023 for brain tumor segmentation and DRIVE for retinal vessel segmentation. Experimental results show that Swin UNETR achieves the best overall performance, with Dice scores of 0.8965 on BraTS 2023 and 0.8078 on DRIVE. The results suggest that transformer based U-Net variants are effective for segmentation tasks requiring global contextual modeling, while residual learning remains useful for fine structure segmentation. This study provides practical insights into model selection for medical image segmentation across volumetric MRI and retinal imaging tasks.

---


### 341. [Gated MLPs as Symmetry-Broken Rank-1 Bilinear Attention](https://arxiv.org/abs/2606.22172)

**<font color=#1a73e8>作者：</font>** Nathan Breslow  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We show that the conventional gated MLP can be viewed as a rank-1 approximation to a bilinear attention mechanism with two distinct factors corresponding to the query and the key. We further show that moving the nonlinearity onto one factor breaks the exchange symmetry between the two factors and, for non-homogeneous activations, the inverse-scaling symmetry as well. This perspective may help explain why gated MLPs are effective in practice and inform the design of future architectures.

---


### 342. [Dual-Stream EEG Decoding for 3D Visual Perception](https://arxiv.org/abs/2606.22182)

**<font color=#1a73e8>作者：</font>** Ninon Lizé Masclef, Taisija Demcenko, Antonella Catanzaro 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper explores a novel brain decoding model for 3D shape perception through a dual pathway architecture mirroring biological vision. Our bio-inspired approach implements separate decoding modules for object identity and spatial orientation, inspired by ventral and dorsal pathways, during continuous rotations. We employ circular regression for angle prediction and develop EEG-conditioned multiview diffusion for 3D reconstruction. Our approach successfully decodes both object identity and spatial orientation from EEG signals and enables 3D reconstruction from neural activity, with interpretability analyses revealing temporally structured involvement of ventral, dorsal, and motor-related channels rather than a static ventral dominance in supporting object and angle decoding.

---


### 343. [Resolving Multi-Target Association in OFDM-based ISAC via Vision-aided Multi-Modal Learning](https://arxiv.org/abs/2606.22195)

**<font color=#1a73e8>作者：</font>** Meng Hua, Chenghong Bian, Deniz Gunduz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Orthogonal frequency division multiplexing (OFDM)-based integrated sensing and communication (ISAC) systems commonly extract target parameters by peak-searching a delay-Doppler map (DDM) constructed from reflected pilots. In multi-target scenarios, this results in ambiguity: the DDM does not reveal which physical target produced which peak, and two targets within the same delay-Doppler resolution cell cannot be separated. We propose a vision-assisted OFDM-ISAC framework that resolves both limitations by fusing wireless and visual modalities. The transmitter encodes an onboard street-view image with deep joint source-channel coding (DeepJSCC) and transmits it over the same OFDM waveform used for sensing; the receiver reconstructs the image, runs a fine-tuned YOLOv5 detector and fuses the resulting per-target features (bounding-box coordinates and class labels) with the DDM and transmitter-receiver geometry through a learned multi-modal network. To stabilize training of the high dimensional delay and Doppler classifiers, we introduce a Kullback Leibler loss against triangular soft labels centered on the ground-truth bin. On a Blender-rendered vehicular testbed, the proposed framework achieves a 16 cm localization root mean square error (RMSE) and a 10.8 ns delay RMSE. An ablation study confirms that removing the visual modality causes a 60x degradation in localization. These results highlight the potential of vision to overcome the data-association and resolution limits of single-modality ISAC.

---


### 344. [Multi4D: High-Fidelity Dynamic Gaussian Splatting via Multi-Level Competitive Allocation](https://arxiv.org/abs/2606.22197)

**<font color=#1a73e8>作者：</font>** Rui Wang, Quentin Lohmeyer, Siyu Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic 3D Gaussian splatting faces a fundamental tension between motion consistency and visual fidelity. Deformation-based approaches preserve temporal correspondence but suffer from motion over-factorization, oversmoothing high-frequency dynamics. In contrast, 4D-primitive methods capture fine visual details yet incur temporal overparameterization, breaking object identity and leading to severe storage overhead. To resolve this, we introduce Multi4D, a framework for high-fidelity dynamic Gaussian Splatting based on multi-level competitive allocation. Instead of a monolithic representation, we distribute modeling capacity across three structured levels: static structure, persistent dynamic geometry, and transient appearance primitives. Through shared rasterization and residual-driven optimization, these levels dynamically compete to explain photometric error, enabling adaptive specialization without pre-assigned decomposition. This allocation preserves long-term motion consistency while capturing fine dynamic detail, achieving state-of-the-art rendering quality and real-time performance with significantly fewer dynamic primitives. Furthermore, because our representation explicitly tracks compact persistent Gaussians over time, semantic features can be embedded afterward, enabling Multi4D to achieve state-of-the-art 4D segmentation accuracy with an order-of-magnitude speedup. Project page: this https URL

---


### 345. [2.5D Root of Trust: Securing the Chiplet Ecosystem](https://arxiv.org/abs/2606.22198)

**<font color=#1a73e8>作者：</font>** Charles Williams, Mohammed Nabeel, Gino Chacon 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The semiconductor industry is rapidly transitioning from monolithic systems-on-chip toward heterogeneous, multi-vendor 2.5D chiplet ecosystems integrated via silicon interposers. While this paradigm shift offers immense benefits in yield, cost, and time-to-market, it radically expands the attack surface. Integrating chiplets from untrusted foundries and design houses introduces vulnerabilities to hardware Trojans, IP piracy, and system-level communication exploits. Critically, chip-level security features and conventional Root of Trust (RoT) proposals are insufficient in this context: any component, including the interconnect fabric itself, may be sourced from an untrusted vendor. This perspective paper surveys state-of-the-art security strategies for interposer-based 2.5D integration, focusing on three threat categories: interconnect attacks (snooping, spoofing, and man-in-the-middle), cache coherence exploits including complex forging attacks, and microarchitectural side-channel threats. We examine design-time defenses via 2.5D split manufacturing and, more crucially, runtime defenses that establish an active interposer as a physically isolated 2.5D RoT. By embedding so-called transaction monitors and coherence message checkers within the trusted interposer fabric, the system enforces memory access permissions by construction and neutralizes coherence-level attacks without need for modifying/securing the commodity chiplets. Finally, we review the EDA flows required to realize these defenses and show they concurrently improve power and signal integrity while reducing overall system footprint.

---


### 346. [Neural Conjugate Aggregation: Identifiable Unsupervised Multi-Sensor Regression under Heterogeneous Sensor Bias](https://arxiv.org/abs/2606.22200)

**<font color=#1a73e8>作者：</font>** Muhammed Faruk Aytin, Zehra Demir, Alper Ünal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study regression-based data fusion under uncertainty, where multiple noisy and biased measurement sources are available but ground-truth labels are absent during training. This setting arises in sensor networks, simulation ensembles, and scientific monitoring systems where supervision is costly or infeasible. We propose the Neural Conjugate Aggregation Model (NCAM), a hierarchical Bayesian framework that combines neural networks with conjugate Gaussian inference for unsupervised multi-source fusion. NCAM learns source-specific bias and reliability conditioned on contextual covariates, yielding an analytically tractable posterior over a latent target variable with decomposed epistemic and aleatoric uncertainty. Structural non-identifiability is resolved through sensor anchoring and variance regularization, enabling stable and interpretable posterior aggregation. To complement Bayesian uncertainty with finite-sample guarantees, we integrate locally adaptive Monte Carlo conformal prediction, producing heteroscedastic prediction intervals with coverage guarantees under exchangeability assumptions. Experiments on synthetic and real-world air-quality datasets demonstrate improved predictive accuracy and well-calibrated uncertainty compared to unsupervised baselines, including mean aggregation, probabilistic PCA, and Kalman filtering.

---


### 347. [Lexical Consensus: Grounded Word Learning and Shared Meaning in Artificial Agents](https://arxiv.org/abs/2606.22207)

**<font color=#1a73e8>作者：</font>** Patricio M. Vera  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence systems are commonly evaluated through task performance and behavioral imitation, but such evaluations leave open whether an artificial agent can acquire, stabilize, and use new lexical meanings from grounded experience. This paper introduces Lexical Consensus, an experimental framework for studying grounded word learning over a structured perceptual substrate. Using frozen DINOv2 visual embeddings, Carroll-style nonce words, and interpretable lexical learners plus linear baselines, we test whether agents can acquire artificial labels for visual concepts, generalize them bidirectionally, and stabilize them across controlled settings.
The main result is a robust perceptual-coherence gradient: native categories are easiest to learn, coherent overextensions remain learnable, mid-range disjunctive concepts degrade, and far-disjunctive concepts approach chance. A pre-registered CIFAR-100 dissociation experiment confirms that this gradient is governed by perceptual distance rather than semantic relatedness: perceptual distance predicts acquisition accuracy (partial R^2 = 0.245, p < 1e-7), while semantic distance adds no significant explanatory power (partial R^2 = 0.002, p = 0.660).
Bidirectional evaluation shows that naming and retrieval are distinct: exemplar-based mechanisms outperform centroid prototypes in label-to-image retrieval, exposing a memory-fidelity dimension separate from naming accuracy. Falsification controls, homogeneous candidate-pool evaluations, and null results on representational restructuring indicate that frozen perceptual geometry both enables lexical grounding and limits what can be acquired without representational adaptation.

---


### 348. [Sequential Minimal Optimization Algorithm for One-Class Support Vector Machines With Privileged Information](https://arxiv.org/abs/2606.22210)

**<font color=#1a73e8>作者：</font>** Andrey Lange, Dmitry Smolyakov, Evgeny Burnaev  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> One of the powerful techniques in data modeling is accounting for features that are available at the training stage, but are not available when the trained model is used to classify or predict test data -- the Learning Using Privileged Information paradigm (LUPI). Sequential Minimal Optimization (SMO) methods have been developed for supervised Support Vector Machines (SVM), unsupervised one-class SVM, and SVM with privileged information (SVM+). The missing brick in this research has long been a one-class SVM with privileged information (OC-SVM+). In this paper, we propose an SMO algorithm for OC-SVM+ that significantly outperforms non-sequential algorithms for training the OC-SVM+ model. Its finite-time convergence is established. The experiments show how privileged information affects a descriptive domain in the space of original features. Comparative benchmark tests demonstrate that our algorithm is superior over interior point algorithms.

---


### 349. [TRACE: A Threat Modelling Methodology for Distributed, Cloud-First, and Decentralized Organisations](https://arxiv.org/abs/2606.22214)

**<font color=#1a73e8>作者：</font>** Stefan Beyer  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Established threat modelling methodologies (STRIDE, PASTA, Trike, OCTAVE, LINDDUN, attack trees, and adversary-behaviour catalogues such as MITRE ATT&CK) were designed for software products and enterprises with a discernible security perimeter, a single owning organisation, and a clean separation between technical and operational risk. Modern organisations violate all three assumptions: they run on cloud and SaaS control planes they do not own, distribute privileged authority across founders, contractors, vendors, signers, committees, and automation, and expose value through human approval ceremonies and supply-chain edges rather than a network boundary. The dominant failures are authorised-but-malicious actors, collusion across nominally independent parties, control-plane and CI/CD compromise, and operational mishandling of high-value actions, which existing methods largely omit. We present TRACE, a methodology that treats threat actors, roles, assets, critical invariants, and trust/authority edges as first-class, evidence-linked objects spanning three layers: protocols, systems, and organisations. We compare nine widely used frameworks across ten dimensions, show where each falls short in distributed, cloud-first, zero-trust settings, and specify TRACE: its core model, three application pillars, sequential gated workflow, and an evidence-and-traceability discipline for human-AI co-working in which language models accelerate coverage while senior reviewers retain judgement over invariants, severity, and collusion. TRACE was developed through Web3 security practice but is stack-agnostic. We discuss its relationship to zero trust architecture and accountable Byzantine consensus, its limitations, and open questions around empirical validation.

---


### 350. [MultiMem: Measuring and Mitigating Memorization in Multi-Modal Contrastive Learninga](https://arxiv.org/abs/2606.22220)

**<font color=#1a73e8>作者：</font>** Wenhao Wang, Franziska Boenisch, Michael Backes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Memorization in machine learning models enables high performance on rare in-distribution samples by capturing their atypical patterns. However, it also causes harmful retention of noise and outliers, degrading generalization. While memorization has been extensively studied in both supervised and self-supervised learning in the vision domain, it remains unexplored in multi-modal contrastive learning. We address this gap by introducing MultiMem, the first metric designed to quantify memorization in multi-modal contrastive learning. Through our systematic analysis, we demonstrate that cross-modal semantic misalignment has the strongest influence on memorization, with text being the dominant modality driving memorization, followed by video, image, and audio. We show that targeted augmentations applied across all modalities effectively reduce memorization as measured by our MultiMem metric and improve model performance. Overall, this work establishes the first framework for measuring and mitigating memorization in multi-modal contrastive learning, preventing harmful data retention and contributing to higher-performing models.

---


> [!TIP]
> 当前位于：**301-350**（第 7/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-654](./part-14.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
