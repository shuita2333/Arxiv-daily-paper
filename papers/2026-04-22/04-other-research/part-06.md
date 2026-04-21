# 📦 其他研究 | 2026年04月22日

> 本类共 **535** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-535](./part-11.md)

---

### 251. [The First Challenge on Mobile Real-World Image Super-Resolution at NTIRE 2026: Benchmark Results and Method Overview](https://arxiv.org/abs/2604.17306)

**<font color=#1a73e8>作者：</font>** Jiatong Li, Zheng Chen, Kai Liu 等 94 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper provides a review of the NTIRE 2026 challenge on mobile real-world image super-resolution, highlighting the proposed solutions and the resulting outcomes. The challenge aims to recover high-resolution (HR) images from low-resolution (LR) counterparts generated through unknown degradations with a x4 scaling factor while ensuring the models remain executable on mobile devices. The objective is to develop effective and efficient network designs or solutions that achieve state-of-the-art real-world image super-resolution performance. The track of the challenge evaluates performance using a weighted combination of image quality assessment (IQA) score and speedup ratios. The competition attracted 108 registrants, with 16 teams achieving a valid score in the final ranking. This collaborative effort advances the performance of mobile real-world image super-resolution while offering an in-depth overview of the latest trends in the field.

---


### 252. [Generalizable Face Forgery Detection via Separable Prompt Learning](https://arxiv.org/abs/2604.17307)

**<font color=#1a73e8>作者：</font>** Enrui Yang, Yuezun Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detecting face forgeries using CLIP has recently emerged as a promising and increasingly popular research direction. Owing to its rich visual knowledge acquired through large-scale pretraining, most existing methods typically rely on the visual encoder of CLIP, while paying limited attention to the text modality. Given the instructive nature of the text modality, we posit that it can be leveraged to instruct Deepfake detection with meticulous design. Accordingly, we shift the focus from the visual modality to the text modality and propose a new Separable Prompt Learning strategy (SePL) that enables CLIP to serve as an effective face forgery detector. The core idea of SePL is to disentangle forgery-specific and forgery-irrelevant information in images via two types of prompt learning, with the former enhancing detection. To achieve this disentangle, we describe a cross-modality alignment strategy and a set of dedicated objectives. Extensive experiments demonstrate that, with this simple adaptation, our method achieves competitive and even superior performance compared to other methods under both cross-dataset and cross-method evaluation, highlighting its strong generalizability. The codes have been released at this https URL

---


### 253. [SkillFlow:Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents](https://arxiv.org/abs/2604.17308)

**<font color=#1a73e8>作者：</font>** Ziao Zhang, Kou Shi, Shiting Huang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As the capability frontier of autonomous agents continues to expand, they are increasingly able to complete specialized tasks through plug-and-play external skills. Yet current benchmarks mostly test whether models can use provided skills, leaving open whether they can discover skills from experience, repair them after failure, and maintain a coherent library over time. We introduce SkillFlow, a benchmark of 166 tasks across 20 families in which task construction within each family follows a Domain-Agnostic Execution Flow (DAEF) that defines an agent workflow framework, allowing these tasks to share a consistent workflow. Agents are evaluated under an Agentic Lifelong Learning protocol in which they begin without skills, solve tasks sequentially within each family, externalize lessons through trajectory- and rubric-driven skill patches, and carry the updated library forward. Experiments reveal a substantial capability gap. For Claude Opus 4.6, lifelong skill evolution improves task success from 62.65% to 71.08% (+8.43 points). However, high skill usage does not necessarily imply high utility: Kimi K2.5 gains only +0.60 points despite 66.87% skill usage, while Qwen-Coder-Next reaches only a 44.58% task completion rate and still regresses relative to the vanilla setting. SkillFlow contributes a structured testbed for this direction and an in-depth empirical analysis of skill discovery, patching, transfer, and their failure modes under lifelong evaluation.

---


### 254. [Knows: Agent-Native Structured Research Representations](https://arxiv.org/abs/2604.17309)

**<font color=#1a73e8>作者：</font>** Guangsheng Yu, Xu Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Research artifacts are distributed primarily as reader-oriented documents like PDFs. This creates a bottleneck for increasingly agent-assisted and agent-native research workflows, in which LLM agents need to infer fine-grained, task-relevant information from lengthy full documents, a process that is expensive, repetitive, and unstable at scale.
We introduce Knows, a lightweight companion specification that binds structured claims, evidence, provenance, and verifiable relations to existing research artifacts in a form LLM agents can consume directly. Knows addresses the gap with a thin YAML sidecar (KnowsRecord) that coexists with the original PDF, requiring no changes to the publication itself, and validated by a deterministic schema linter. We evaluate Knows on 140 comprehension questions across 20 papers spanning 14 academic disciplines, comparing PDF-only, sidecar-only, and hybrid conditions across six LLM agents of varying capacity. Weak models (0.8B--2B parameters) improve from 19--25\% to 47--67\% accuracy (+29 to +42 percentage points) when reading sidecar instead of PDF, while consuming 29--86\% fewer input tokens; an LLM-as-judge re-scoring confirms that weak-model sidecar accuracy (75--77\%) approaches stronger-model PDF accuracy (78--83\%). Beyond this controlled evaluation, a community sidecar hub at this https URL has already indexed over ten thousand publications and continues to grow daily, providing independent evidence that the format is adoption-ready at scale.

---


### 255. [Interpolating Discrete Diffusion Models with Controllable Resampling](https://arxiv.org/abs/2604.17310)

**<font color=#1a73e8>作者：</font>** Marcel Kollovieh, Sirine Ayadi, Stephan Günnemann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion models form a powerful class of generative models across diverse domains, including text and graphs. However, existing approaches face fundamental limitations. Masked diffusion models suffer from irreversible errors due to early unmasking, while uniform diffusion models, despite enabling self-correction, often yield low-quality samples due to their strong reliance on intermediate latent states. We introduce IDDM, an Interpolating Discrete Diffusion Model, that improves diffusion by reducing dependence on intermediate latent states. Central to IDDM is a controllable resampling mechanism that partially resets probability mass to the marginal distribution, mitigating error accumulation and enabling more effective token corrections. IDDM specifies a generative process whose transitions interpolate between staying at the current state, resampling from a prior, and flipping toward the target state, while enforcing marginal consistency and fully decoupling training from inference. We benchmark our model against state-of-the-art discrete diffusion models across molecular graph generation as well as text generation tasks, demonstrating competitive performance.

---


### 256. [R-FLoRA: Residual-Statistic-Gated Low-Rank Adaptation for Single-Image Face Morphing Attack Detection](https://arxiv.org/abs/2604.17321)

**<font color=#1a73e8>作者：</font>** Raghavendra Ramachandra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face morphing attacks pose a substantial risk to the reliability of face recognition systems used in passport issuance, border control, and digital identity verification. Detecting morphing attacks from a single facial image remains challenging owing to the lack of a trusted reference and the diversity of attack generation methods. This paper presents a new Single-Image Face Morphing Attack Detection (S-MAD) framework that integrates high-frequency Laplacian residual statistics with representations from a frozen, foundation-scale vision transformer. The approach employs residual-statistic-gated low-rank adapters (R-FLoRA) and feature-wise residual fusion (Res-FiLM) to enhance sensitivity to local morphing artefacts while preserving the semantic context of the backbone. A novel residual-contrastive alignment loss further regularises the fused token space, improving discrimination under unseen morphing conditions. Comprehensive experiments on four ICAO-compliant datasets, encompassing seven morph generation techniques, demonstrate that the proposed method consistently surpasses nine recent state-of-the-art S-MAD algorithms in detection accuracy and cross-domain (or dataset) generalisation. With a frozen backbone and minimal trainable parameters, the model achieves real-time efficiency and interpretability, making it suitable for real-life scenarios in biometric verification systems.

---


### 257. [Analysing Human Interaction with Electronic Displays in Microgravity](https://arxiv.org/abs/2604.17322)

**<font color=#1a73e8>作者：</font>** Pradipta Biswas, Himanshu Vishwakarma, Mukund Mitra 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human Space Flight missions often require interaction with touchscreen displays. This paper presents a study of investigating human machine interaction with touchscreen using both finger and stylus in the International Space Station. The study also reports cognitive state of astronauts in the form of spatial 2-back test and mental well-being through self-reported scales. We presented a series of results comparing pointing and selection performance among ISS crews, ground crews and university students, finger-based touching and stylus-based touching in microgravity and mental well-being scores. We reported that finger-based pointing is statistically significantly faster than stylus-based pointing in microgravity based on analysis of 420 pointing tasks in ISS from 2 astronauts. We also did not find any significant difference among pointing performance and mental state of astronauts and students on ground. Results from the study can be used to predict pointing and selection time from dimension and position of GUI (Graphical User Interface) elements for cockpits of spacecraft.

---


### 258. [A Universal Avoidance Method for Diverse Multi-branch Generation](https://arxiv.org/abs/2604.17323)

**<font color=#1a73e8>作者：</font>** Kyeongman Park, Minha Jhang, Kyomin Jung  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern generative models still lack human-level creativity, particularly in multi-branch diversity. Prior approaches to address this problem often incur heavy computation or strong dependency on model architecture. Therefore, we introduce UAG(Universal Avoidance Generation), a model-agnostic and computationally efficient generation strategy that penalizes similarity among previously generated outputs. Thus, UAG can enhance multi-branch diversity across both diffusion and transformer models, with minimal additional computation. In experiments, our method achieves up to 1.9 times higher diversity, runs 4.4 times faster, and requires only 1/64 of the FLOPs compared to state-of-the-art methods. The full code is this https URL.

---


### 259. [SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated Attention](https://arxiv.org/abs/2604.17324)

**<font color=#1a73e8>作者：</font>** Dongxin Guo, Jikun Wu, Siu Ming Yiu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph transformers achieve strong results on molecular and long-range reasoning tasks, yet remain hampered by over-smoothing (the progressive collapse of node representations with depth) and attention entropy degeneration. We observe that these pathologies share a root cause with attention sinks in large language models: softmax attention's sum-to-one constraint forces every node to attend somewhere, even when no informative signal exists. Motivated by recent findings that element-wise sigmoid gating eliminates attention sinks in large language models, we propose SigGate-GT, a graph transformer that applies learned, per-head sigmoid gates to the attention output within the GraphGPS framework. Each gate can suppress activations toward zero, enabling heads to selectively silence uninformative connections. On five standard benchmarks, SigGate-GT matches the prior best on ZINC (0.059 MAE) and sets new state-of-the-art on ogbg-molhiv (82.47% ROC-AUC), with statistically significant gains over GraphGPS across all five datasets ($p < 0.05$). Ablations show that gating reduces over-smoothing by 30% (mean relative MAD gain across 4-16 layers), increases attention entropy, and stabilizes training across a $10\times$ learning rate range, with about 1% parameter overhead on OGB.

---


### 260. [Rethinking the Comparison Unit in Sequence-Level Reinforcement Learning: An Equal-Length Paired Training Framework from Loss Correction to Sample Construction](https://arxiv.org/abs/2604.17328)

**<font color=#1a73e8>作者：</font>** Fei Ding, Yongkang Zhang, Runhao Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper investigates the length problem in sequence-level relative reinforcement learning. We observe that, although existing methods partially alleviate length-related phenomena, a more fundamental issue remains insufficiently characterized: the comparison units used during training lack inherent comparability. Building on this observation, we propose a new perspective: the length problem should not be viewed merely as a loss-scaling or normalization bias, but rather as a \emph{comparison unit construction} problem. We further establish a sample-construction-based training framework that, instead of applying post-hoc corrections to unequal-length responses, proactively constructs equal-length, alignable, and comparable training segments during generation. Within this framework, we propose EqLen, a concrete method applicable to group-relative comparison algorithms such as GRPO, GSPO, and RLOO. Through dual-track synchronous generation, prefix inheritance, and segment masking, EqLen efficiently collects effective equal-length training segments and enables stable

---


### 261. [Neuro-Symbolic Resolution of Recommendation Conflicts in Multimorbidity Clinical Guidelines](https://arxiv.org/abs/2604.17340)

**<font color=#1a73e8>作者：</font>** Shiyao Xie, Jian Du  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical guidelines, typically developed by independent specialty societies, inherently exhibit substantial fragmentation, redundancy, and logical contradiction. These inconsistencies, particularly when applied to patients with multimorbidity, not only cause cognitive dissonance for clinicians but also introduce catastrophic noise into AI systems, rendering the standard Retrieval-Augmented Generation (RAG) system fragile and prone to hallucination. To address this fundamental reliability crisis, we introduce a Neuro-Symbolic framework that automates the detection of recommendation redundancies and conflicts. Our pipeline employs a multi-agent system to translate unstructured clinical natural language into rigorous symbolic logic language, which is then verified by a Satisfiability (SAT) solver. By formulating a hierarchical taxonomy of logical rule interactions, we identify a critical category termed Local Conflict - a decision conflict arising from the intersection of comorbidities. Evaluating our system on a curated benchmark of 12 authoritative SGLT2 inhibitor guidelines, we reveal that 90.6% of conflicts are Local, a structural complexity that single-disease guidelines fail to address. While state-of-the-art LLMs fail in detecting these conflicts, our neuro-symbolic approach achieves an F1 score of 0.861. This work demonstrates that logical verification must precede retrieval, establishing a new technical standard for automated knowledge coordination in medical AI.

---


### 262. [Robust Diabetic Retinopathy Grading Using Dual-Resolution Attention-Based Deep Learning with Ordinal Regression](https://arxiv.org/abs/2604.17341)

**<font color=#1a73e8>作者：</font>** Afshan Hashmi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diabetic retinopathy (DR) is a leading cause of vision impairment worldwide, and automated grading systems play a crucial role in large-scale screening programs. However, deep learning models often exhibit degraded performance when deployed across datasets acquired under different imaging conditions. This study presents a robust dual-resolution deep learning framework for DR grading that integrates attention-based feature fusion with ordinal regression to improve cross-dataset generalization. The proposed method employs two parallel EfficientNet backbones operating at different spatial resolutions to capture complementary retinal features. A learnable attention mechanism adaptively fuses multi-resolution representations, while an ordinal regression formulation based on the cumulative link model (CORAL) explicitly accounts for the ordered nature of DR severity levels. To mitigate domain discrepancies between datasets, a preprocessing strategy combining circular cropping, contrast enhancement, and histogram matching is applied. The model was trained on the APTOS 2019 dataset and evaluated on both an internal validation split and an external Messidor-2 test set. Experimental results demonstrate strong grading performance, achieving a quadratic weighted kappa (QWK) of 0.88 on the APTOS validation set and 0.68 on the unseen Messidor-2 dataset, indicating improved robustness for cross-dataset DR grading applications.

---


### 263. [FLARE: Task-agnostic embedding model evaluation through a normalization process](https://arxiv.org/abs/2604.17344)

**<font color=#1a73e8>作者：</font>** Jingzhou Jiang, Yixuan Tang, Yi Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When task-specific labels are not available, it becomes difficult to select an embedding model for a specific target corpus. Existing labelless measures based on kernel estimators or Gaussian mixes fail in high-dimensional space, resulting in unstable rankings. We propose a flow-based labelless representation embedding evaluation (FLARE), which utilizes normalized streams to estimate information sufficiency directly from log-likelihood and avoid distance-based density estimation. We give a finite sample boundary, indicating that the estimation error depends on the intrinsic dimension of the data manifold rather than the original embedding dimension. On 11 datasets and 8 embedders, FLARE reached Spearman's $\rho$ of 0.90 under the supervised benchmark and remained stable in high-dimensional embeddings ($d \geq 3{,}584$) as the existing labelless baseline collapsed.

---


### 264. [Logical Computational Linguistics](https://arxiv.org/abs/2604.17346)

**<font color=#1a73e8>作者：</font>** Glyn V. Morrill, Oriol Valentín  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this book we promote logical computational linguistics as opposed to statistical computational linguistics. In particular, we provide a logical semantic interface. This book assembles more than twenty years of research work on type logical grammar, and adds new ideas and material.
Chains of statistical dependencies of less than one hundred per cent confidence tend monotonically to zero. Chains of logical dependencies of any length maintain one hundred per cent confidence end to end.
We aspire to enable perfect syntactic and semantic processing in life-critical NLP applications.

---


### 265. [SOCIA-EVO: Automated Simulator Construction via Dual-Anchored Bi-Level Optimization](https://arxiv.org/abs/2604.17351)

**<font color=#1a73e8>作者：</font>** Yuncheng Hua, Sion Weatherhead, Mehdi Jafari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated simulator construction requires distributional fidelity, distinguishing it from generic code generation. We identify two failure modes in long-horizon LLM agents: contextual drift and optimization instability arising from conflating structural and parametric errors. We propose SOCIA-EVO, a dual-anchored evolutionary framework. SOCIA-EVO introduces: (1) a static blueprint to enforce empirical constraints; (2) a bi-level optimization to decouple structural refinement from parameter calibration; and (3) a self-curating Strategy Playbook that manages remedial hypotheses via Bayesian-weighted retrieval. By falsifying ineffective strategies through execution feedback, SOCIA-EVO achieves robust convergence, generating simulators that are statistically consistent with observational data. The code and data of SOCIA-EVO are available here: this https URL.

---


### 266. [Still Between Us? Evaluating and Improving Voice Assistant Robustness to Third-Party Interruptions](https://arxiv.org/abs/2604.17358)

**<font color=#1a73e8>作者：</font>** Dongwook Lee, Eunwoo Song, Che Hyun Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While recent Spoken Language Models (SLMs) have been actively deployed in real-world scenarios, they lack the capability to discern Third-Party Interruptions (TPI) from the primary user's ongoing flow, leaving them vulnerable to contextual failures. To bridge this gap, we introduce TPI-Train, a dataset of 88K instances designed with speaker-aware hard negatives to enforce acoustic cue prioritization for interruption handling, and TPI-Bench, a comprehensive evaluation framework designed to rigorously measure the interruption-handling strategy and precise speaker discrimination in deceptive contexts. Experiments demonstrate that our dataset design mitigates semantic shortcut learning-a critical pitfall where models exploit semantic context while neglecting acoustic signals essential for discerning speaker changes. We believe our work establishes a foundational resource for overcoming text-dominated unimodal reliance in SLMs, paving the way for more robust multi-party spoken interaction. The code for the framework is publicly available at this https URL

---


### 267. [T-DuMpRa: Teacher-guided Dual-path Multi-prototype Retrieval Augmented framework for fine-grained medical image classification](https://arxiv.org/abs/2604.17360)

**<font color=#1a73e8>作者：</font>** Zixuan Tang, Shen Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fine-grained medical image classification is challenged by subtle inter-class variations and visually ambiguous cases, where confidence estimates often exhibit uncertainty rather than being overconfident. In such scenarios, purely discriminative classifiers may achieve high overall accuracy yet still fail to distinguish between highly similar categories, leading to miscalibrated predictions. We propose T-DuMpRa, a teacher-guided dual-path multi-prototype retrieval-augmented framework, where discriminative classification and multi-prototype retrieval jointly drive both training and prediction. During training, we jointly optimize cross-entropy and supervised contrastive objectives to learn a cosine-compatible embedding geometry for reliable prototype matching. We further employ an exponential moving average (EMA) teacher to obtain smoother representations and build a multi-prototype memory bank by clustering teacher embeddings in the teacher embedding space. Our framework is plug-and-play: it can be easily integrated into existing classification models by constructing a compact prototype bank, thereby improving performance on visually ambiguous cases. At inference, we combine the classifier's predicted distribution with a similarity-based distribution computed via cosine matching to prototypes, and apply a conservative confidence-gated fusion that activates retrieval only when the classifier's prediction is uncertain and the retrieval evidence is decisive and conflicting, otherwise keeping confident predictions unchanged. On HAM10000 and ISIC2019, our method yields 0.68%-0.21% and 0.44%-2.69% improvements on 5 different backbones. And visualization analysis proves our model can enhance the model's ability to handle visually ambiguous cases.

---


### 268. [Towards Generalizable Deepfake Image Detection with Vision Transformers](https://arxiv.org/abs/2604.17376)

**<font color=#1a73e8>作者：</font>** Kaliki V Srinanda, M Manvith Prabhu, Hemanth K Mogilipalem 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In today's day and age, we face a challenge in detecting deepfake images because of the fast evolution of modern generative models and the poor generalization capability of existing methods. In this paper, we use an ensemble of fine-tuned vision transformers like DINOv2, AIMv2 and OpenCLIP's ViT-L/14 to create generalizable method to detect deepfakes. We use the DF-Wild dataset released as part of the IEEE SP Cup 2025, because it uses a challenging and diverse set of manipulations and generation techniques. We started our experiments with CNN classifiers trained on spatial features. Experimental results show that our ensemble outperforms individual models and strong CNN baselines, achieving an AUC of 96.77% and an Equal Error Rate (EER) of just 9% on the DF-Wild test set, beating the state-of-the-art deepfake detection algorithm Effort by 7.05% and 8% in AUC and EER respectively. This was the winning solution for SP Cup, presented at ICASSP 2025.

---


### 269. [Back to Repair: A Minimal Denoising Network\ for Time Series Anomaly Detection](https://arxiv.org/abs/2604.17388)

**<font color=#1a73e8>作者：</font>** Kadir-Kaan Özer, René Ebeling, Markus Enzweiler  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce JuRe (Just Repair), a minimal denoising network for time series anomaly detection that exposes a central finding: architectural complexity is unnecessary when the training objective correctly implements the manifold-projection principle. JuRe consists of a single depthwise-separable convolutional residual block with hidden dimension 128, trained to repair corrupted time series windows and scored at inference by a fixed, parameter-free structural discrepancy function. Despite using no attention, no latent variable, and no adversarial component, JuRe ranks second on the TSB-AD multivariate benchmark (AUC-PR 0.404, 180 series, 17 datasets) and second on the UCR univariate archive by AUC-PR (0.198, 250 series), leading all neural baselines on AUC-PR and VUS-PR. Component ablation on TSB-AD identifies training-time corruption as the dominant factor ($\Delta$AUC-PR $= 0.047$ on removal), confirming that the denoising objective, not network capacity, drives detection quality. Pairwise Wilcoxon signed-rank tests establish statistical significance against 21 of 25 baselines on TSB-AD. Code is available at the URL this https URL.

---


### 270. [Deep learning based Non-Rigid Volume-to-Surface Registration for Brain Shift compensation Using Point Cloud](https://arxiv.org/abs/2604.17389)

**<font color=#1a73e8>作者：</font>** Eashrat Jahan Muniya, Gernot Kronreif, Ander Biguri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Soft-tissue deformation remains a major limitation in image-guided neurosurgery, where intra-operative anatomy can deviate substantially from pre-operative imaging due to brain shift, compromising navigation accuracy and surgical safety. Existing compensation methods often rely on intra-operative MRI, CT, or ultrasound, which are disruptive and difficult to integrate repeatedly into the surgical workflow. In contrast, partial 3D cortical surfaces can be reconstructed as point clouds from stereoscopic microscopes or laser range scanners (LRS), capturing only a limited portion of the exposed cortex. This makes point cloud registration a practical alternative without interrupting surgery; however, such partial and noisy observations make deformation estimation highly challenging. In this study, we propose a deep learning-based framework for non-rigid volume-to-surface registration, enabling dense displacement field estimation from sparse intra-operative surface observations without explicit point correspondences or volumetric intra-operative imaging. The network leverages multi-scale point-based feature extraction and a hierarchical deformation decoder to capture both global and local deformations. The key contribution lies in integrating partial intra-operative surface information into the full pre-operative point cloud domain, enabling implicit correspondence learning and dense deformation recovery under limited visibility. Quantitative results demonstrate accurate recovery of fine-scale deformations, achieving an Endpoint Error (EPE) of 1.13 +/- 0.75 mm and RMSE of 1.33 +/- 0.81 mm under challenging partial-surface conditions. The proposed approach supports automatic, workflow-compatible brain-shift compensation from sparse surface observations.

---


### 271. [MESA: A Training-Free Multi-Exemplar Deep Framework for Restoring Ancient Inscription Textures](https://arxiv.org/abs/2604.17390)

**<font color=#1a73e8>作者：</font>** Vasileios Toulatzis, Ioannis Fudos  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ancient inscriptions frequently suffer missing or corrupted regions from fragmentation, erosion, or other damage, hindering reading, and analysis. We review prior image restoration methods and their applicability to inscription image recovery, then introduce MESA (Multi-Exemplar, Style-Aware) -an image-level restoration method that uses well-preserved exemplar inscriptions (from the same epigraphic monument, material, or similar letterforms) to guide reconstruction of damaged text. MESA encodes VGG19 convolutional features as Gram matrices to capture exemplar texture, style, and stroke structure; for each neural network layer it selects the exemplar minimizing Mean-Squared Displacement (MSD) to the damaged input. Layer-wise contribution weights are derived from Optical Character Recognition-estimated character widths in the exemplar set to bias filters toward scales matching letter geometry, and a training mask preserves intact regions so synthesis is restricted to damaged areas. We also summarize prior network architectures and exemplar and single-image synthesis, inpainting, and Generative Adversarial Network (GAN) approaches, highlighting limitations that MESA addresses. Comparative experiments demonstrate the advantages of MESA. Finally, we provide a practical roadmap for choosing restoration strategies given available exemplars and metadata.

---


### 272. [Who Watches the Watchmen? Humans Disagree With Translation Metrics on Unseen Domains](https://arxiv.org/abs/2604.17393)

**<font color=#1a73e8>作者：</font>** Finn Schmidt, Jan Philip Wahle, Terry Ruas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic evaluation metrics are central to the development of machine translation systems, yet their robustness under domain shift remains unclear. Most metrics are developed on the Workshop on Machine Translation (WMT) benchmarks, raising concerns about their robustness to unseen domains. Prior studies that analyze unseen domains vary translation systems, annotators, or evaluation conditions, confounding domain effects with human annotation noise.
To address these biases, we introduce a systematic multi-annotator Cross-Domain Error-Span-Annotation dataset (CD-ESA), comprising 18.8k human error span annotations across three language pairs, where we fix annotators within each language pair and evaluate translations of the same six translation systems across one seen news domain and two unseen technical domains. Using this dataset, we first find that automatic metrics appear surprisingly robust to domain-shifts at the segment level (up to 0.69 agreement), but this robustness largely disappears once we account for human label variation. Averaging annotations increases inter-annotator agreement by up to +0.11. Metrics struggle on the unseen chemical domain compared to humans (inter-annotator agreement of 0.78-0.83 vs. 0.96).
We recommend comparing metric-human agreement against inter-annotator agreement, rather than comparing raw metric-human agreement alone, when evaluating across different domains.

---


### 273. [Speculative Decoding for Autoregressive Video Generation](https://arxiv.org/abs/2604.17397)

**<font color=#1a73e8>作者：</font>** Yuezhou Hu, Jintao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video diffusion is emerging as a promising paradigm for streaming video synthesis, with step distillation serving as the primary means of accelerating inference. Whether speculative decoding, the dominant acceleration strategy for large language models, can be effectively adapted to autoregressive video generation remains an open question, because video blocks are continuous spatiotemporal tensors with no token-level distribution for exact rejection sampling. We introduce SDVG, which brings speculative decoding to block-based autoregressive video diffusion by replacing token verification with an image-quality router. A 1.3B drafter proposes candidate blocks via four denoising steps; each block is VAE-decoded and scored by ImageReward using worst-frame aggregation--taking the minimum per-frame reward to catch single-frame artifacts that averaging would mask. Blocks scoring above a fixed threshold tau are accepted into the 14B target's KV cache; the rest are regenerated by the target. Two additional design choices prove critical: the first block is always force-rejected to anchor scene composition, and tau serves as a single knob that traces a smooth quality-speed Pareto frontier. On 1003 MovieGenVideoBench prompts (832x480), SDVG retains 98.1% of target-only VisionReward quality (0.0773 vs. 0.0788) at a 1.59x speedup with tau=-0.7, and reaches 2.09x at 95.7% quality retention--while consistently outperforming draft-only generation by over +17%. The framework is training-free, requires no architectural changes, and can be seamlessly integrated into existing autoregressive video generation pipelines.

---


### 274. [Phase-Scheduled Multi-Agent Systems for Token-Efficient Coordination](https://arxiv.org/abs/2604.17400)

**<font color=#1a73e8>作者：</font>** Mohit Dubey  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS) powered by large language models suffer from severe token inefficiency arising from two compounding sources: (i) unstructured parallel execution, where all agents activate simultaneously irrespective of input readiness; and (ii) unrestricted context sharing, where every agent receives the full accumulated context regardless of relevance. Existing mitigation strategies - static pruning, hierarchical decomposition, and learned routing - treat coordination as a structural allocation problem and fundamentally ignore its temporal dimension. We propose Phase-Scheduled Multi-Agent Systems (PSMAS), a framework that reconceptualizes agent activation as continuous control over a shared attention space modeled on a circular manifold.
Each agent i is assigned a fixed angular phase theta_i in the range [0, 2*pi], derived from the task dependency topology; a global sweep signal phi(t) rotates at velocity omega, activating only agents within an angular window epsilon. Idle agents receive compressed context summaries, reducing per-step token consumption. We implement PSMAS on LangGraph, evaluate on four structured benchmarks (HotPotQA-MAS, HumanEval-MAS, ALFWorld-Multi, WebArena-Coord) and two unstructured conversational settings, and prove stability, convergence, and optimality results for the sweep dynamics. PSMAS achieves a mean token reduction of 27.3 percent (range 21.4-34.8 percent) while maintaining task performance within 2.1 percentage points of a fully activated baseline (p < 0.01, n = 500 per configuration), and outperforms the strongest learned routing baseline by 5.6 percentage points in token reduction with 2.0 percentage points less performance drop. Crucially, we show that scheduling and compression are independent sources of gain: scheduling alone accounts for 18-20 percentage points of reduction, robust to compression degradation up to alpha = 0.40.

---


### 275. [On the Generalization Bounds of Symbolic Regression with Genetic Programming](https://arxiv.org/abs/2604.17402)

**<font color=#1a73e8>作者：</font>** Masahiro Nomura, Ryoki Hamano, Isao Ono  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Symbolic regression (SR) with genetic programming (GP) aims to discover interpretable mathematical expressions directly from data. Despite its strong empirical success, the theoretical understanding of why GP-based SR generalizes beyond the training data remains limited. In this work, we provide a learning-theoretic analysis of SR models represented as expression trees. We derive a generalization bound for GP-style SR under constraints on tree size, depth, and learnable constants. Our result decomposes the generalization gap into two interpretable components: a structure-selection term, reflecting the combinatorial complexity of choosing an expression-tree structure, and a constant-fitting term, capturing the complexity of optimizing numerical constants within a fixed structure. This decomposition provides a theoretical perspective on several widely used practices in GP, including parsimony pressure, depth limits, numerically stable operators, and interval arithmetic. In particular, our analysis shows how structural restrictions reduce hypothesis-class growth while stability mechanisms control the sensitivity of predictions to parameter perturbations. By linking these practical design choices to explicit complexity terms in the generalization bound, our work offers a principled explanation for commonly observed empirical behaviors in GP-based SR and contributes towards a more rigorous understanding of its generalization properties.

---


### 276. [STRIDE: Strategic Iterative Decision-Making for Retrieval-Augmented Multi-Hop Question Answering](https://arxiv.org/abs/2604.17405)

**<font color=#1a73e8>作者：</font>** Wei Chen, Lili Zhao, Zhi Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-hop question answering (MHQA) enables accurate answers to complex queries by retrieving and reasoning over evidence dispersed across multiple documents. Existing MHQA approaches mainly rely on iterative retrieval-augmented generation, which suffer from the following two major issues. 1) Existing methods prematurely commit to surface-level entities rather than underlying reasoning structures, making question decomposition highly vulnerable to lexical ambiguity. 2) Existing methods overlook the logical dependencies among reasoning steps, resulting in uncoordinated execution. To address these issues, we propose STRIDE, a framework that separates strategic planning, dynamic control, and grounded execution. At its core, a Meta-Planner first constructs an entity-agnostic reasoning skeleton to capture the abstract logic of the query, thereby deferring entity grounding until after the reasoning structure is established, which mitigates disambiguation errors caused by premature lexical commitment. A Supervisor then orchestrates sub-question execution in a dependency-aware manner, enabling efficient parallelization where possible and sequential coordination when necessary. By dynamically deciding whether to retrieve new evidence or infer from existing facts, it avoids redundant queries and error propagation, while fusing cross-branch information and reformulating failed queries to enhance robustness. Grounded fact extraction and logical inference are delegated to specialized execution modules, ensuring faithfulness through explicit separation of retrieval and reasoning. We further propose STRIDE-FT, a modular fine-tuning framework that uses self-generated execution trajectories from STRIDE, requiring neither human annotations nor stronger teacher models. Experiments show that STRIDE achieves robust and accurate reasoning, while STRIDE-FT effectively enhances open-source LLMs.

---


### 277. [EvoMaster: A Foundational Agent Framework for Building Evolving Autonomous Scientific Agents at Scale](https://arxiv.org/abs/2604.17406)

**<font color=#1a73e8>作者：</font>** Xinyu Zhu, Yuzhu Cai, Zexi Liu 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The convergence of large language models and agents is catalyzing a new era of scientific discovery: Agentic Science. While the scientific method is inherently iterative, existing agent frameworks are predominantly static, narrowly scoped, and lack the capacity to learn from trial and error. To bridge this gap, we present EvoMaster, a foundational evolving agent framework engineered specifically for Agentic Science at Scale. Driven by the core principle of continuous self-evolution, EvoMaster empowers agents to iteratively refine hypotheses, self-critique, and progressively accumulate knowledge across experimental cycles, faithfully mirroring human scientific inquiry. Crucially, as a domain-agnostic base harness, EvoMaster is exceptionally easy to scale up -- enabling developers to build and deploy highly capable, self-evolving scientific agents for arbitrary disciplines in approximately 100 lines of code. Built upon EvoMaster, we incubated the SciMaster ecosystem across domains such as machine learning, physics, and general science. Evaluations on four authoritative benchmarks (Humanity's Last Exam, MLE-Bench Lite, BrowseComp, and FrontierScience) demonstrate that EvoMaster achieves state-of-the-art scores of 41.1%, 75.8%, 73.3%, and 53.3%, respectively. It comprehensively outperforms the general-purpose baseline OpenClaw with relative improvements ranging from +159% to +316%, robustly validating its efficacy and generality as the premier foundational framework for the next generation of autonomous scientific discovery. EvoMaster is available at this https URL.

---


### 278. [DuConTE: Dual-Granularity Text Encoder with Topology-Constrained Attention for Text-attributed Graphs](https://arxiv.org/abs/2604.17411)

**<font color=#1a73e8>作者：</font>** Lexuan Liang, Tao Zou, Xuxiang Ta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-attributed graphs integrate semantic information of node texts with topological structure, offering significant value in various applications such as document classification and information extraction. Existing approaches typically encode textual content using language models (LMs), followed by graph neural networks (GNNs) to process structural information. However, during the LM-based text encoding phase, most methods not only perform semantic interaction solely at the word-token granularity, but also neglect the structural dependencies among texts from different nodes. In this work, we propose DuConTE, a dual-granularity text encoder with topology-constrained attention. The model employs a cascaded architecture of two pretrained LMs, encoding semantics first at the word-token granularity and then at the node granularity. During the self-attention computation in each LM, we dynamically adjust the attention mask matrix based on node connectivity, guiding the model to learn semantic correlations informed by the graph structure. Furthermore, when composing node representations from word-token embeddings, we separately evaluate the importance of tokens under the center-node context and the neighborhood context, enabling the capture of more contextually relevant semantic information. Extensive experiments on multiple benchmark datasets demonstrate that DuConTE achieves state-of-the-art performance on the majority of them.

---


### 279. [TransXion: A High-Fidelity Graph Benchmark for Realistic Anti-Money Laundering](https://arxiv.org/abs/2604.17420)

**<font color=#1a73e8>作者：</font>** Keyang Chen, Mingxuan Jiang, Yongsheng Zhao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Money laundering poses severe risks to global financial systems, driving the widespread adoption of machine learning for transaction monitoring. However, progress remains stifled by the lack of realistic benchmarks. Existing transaction-graph datasets suffer from two pervasive limitations: (i) they provide sparse node-level semantics beyond anonymized identifiers, and (ii) they rely on template-driven anomaly injection, which biases benchmarks toward static structural motifs and yields overly optimistic assessments of model robustness. We propose TransXion, a benchmark ecosystem for Anti-Money Laundering (AML) research that integrates profile-aware simulation of normal activity with stochastic, non-template synthesis of illicit this http URL jointly models persistent entity profiles and conditional transaction behavior, enabling evaluation of "out-of-character" anomalies where observed activity contradicts an entity's socio-economic context. The resulting dataset comprises approximately 3 million transactions among 50,000 entities, each endowed with rich demographic and behavioral attributes. Empirical analyses show that TransXion reproduces key structural properties of payment networks, including heavy-tailed activity distributions and localized subgraph structure. Across a diverse array of detection models spanning multiple algorithmic paradigms, TransXion yields substantially lower detection performance than widely used benchmarks, demonstrating increased difficulty and realism. TransXion provides a more faithful testbed for developing context-aware and robust AML detection methods. The dataset and code are publicly available at this https URL.

---


### 280. [A unified convergence theory for adaptive first-order methods in the nonconvex case, including AdaNorm, full and diagonal AdaGrad, Shampoo and Muo](https://arxiv.org/abs/2604.17423)

**<font color=#1a73e8>作者：</font>** S. Gratton, Ph. L. Toint  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A unified framework for first-order optimization algorithms fornonconvex unconstrained optimization is proposed that uses adaptivelypreconditioned gradients and includes popular methods such as full anddiagonal AdaGrad, AdaNorm, as well as adpative variants of Shampoo andMuon. This framework also allows combining heterogeneous geometriesacross different groups of variables while preserving a unifiedconvergence analysis. A fully stochastic global rate-of-convergenceanalysis is conducted for all methods in the framework, with andwithout two types of momentum, using reasonable assumptions on thevariance of the gradient oracle and without assuming boundedstochastic gradients or small enough stepsize.

---


### 281. [Neural Adjoint Method for Meta-optics: Accelerating Volumetric Inverse Design via Fourier Neural Operators](https://arxiv.org/abs/2604.17425)

**<font color=#1a73e8>作者：</font>** Chanik Kang, Hyewon Suk, Haejun Chung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Meta-optics promises compact, high-performance imaging and color routing. However, designing high-performance structures is a high-dimensional optimization problem: mapping a desired optical output back to a physical 3D structure requires solving computationally expensive Maxwell's equations iteratively. Even with adjoint optimization, broadband design can require thousands of Maxwell solves, making industrial-scale optimization slow and costly. To overcome this challenge, we propose the Neural Adjoint Method, a solver-supervised surrogate that predicts 3D adjoint gradient fields from a voxelized permittivity volume using a Fourier Neural Operator (FNO). By learning the dense, per-voxel sensitivity field that drives gradient-based updates, our method can replace per-iteration adjoint solves with fast predictions, greatly reducing the computational cost of full-wave simulations required during iterative refinement. To better preserve sensitivity peaks, we introduce a stage-wise FNO that progressively refines residual errors with increasing emphasis on higher-frequency components. We curate a meta-optics dataset from paired forward/adjoint FDTD simulations and evaluate it across three tasks: spectral sorting (color routers), achromatic focusing (metalenses), and waveguide mode conversion. Our method reduces design time from hours to seconds. These results suggest a practical route toward fast, large-scale volumetric meta-optical design enabled by AI-accelerated scientific computing.

---


### 282. [Long-CODE: Isolating Pure Long-Context as an Orthogonal Dimension in Video Evaluation](https://arxiv.org/abs/2604.17428)

**<font color=#1a73e8>作者：</font>** Zhijiang Tang, Jiaxin Qi, Bing Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As video generation models achieve unprecedented capabilities, the demand for robust video evaluation metrics becomes increasingly critical. Traditional metrics are intrinsically tailored for short-video evaluation, predominantly assessing frame-level visual quality and localized temporal smoothness. However, as state-of-the-art video generation models scale to generate longer videos, these metrics fail to capture essential long-range characteristics, such as narrative richness and global causal consistency. Recognizing that short-term visual perception and long-context attributes are fundamentally orthogonal dimensions, we argue that long-video metrics should be disentangled from short-video assessments. In this paper, we focus on the rigorous justification and design of a dedicated framework for long-video evaluation. We first introduce a suite of long-video attribute corruption tests, exposing the critical limitations of existing hort-video metrics from their insensitivity to structural inconsistencies, such as shot-level perturbations and narrative shuffling. To bridge this gap, we design a novel long-video metric based on shot dynamics, which is highly sensitive to the long-range testing framework. Furthermore, we introduce Long-CODE (Long-Context as an Orthogonal Dimension for video Evaluation), a specialized dataset designed to benchmark long-video evaluation, with human annotations isolated specifically to genuine long-range characteristics. Extensive experiments show that our proposed metrics achieve state-of-the-art correlation with human judgments. Ultimately, our metric and benchmark seamlessly complement existing short-video standards, establishing a holistic and unbiased evaluation paradigm for video generation models.

---


### 283. [MoVE: Translating Laughter and Tears via Mixture of Vocalization Experts in Speech-to-Speech Translation](https://arxiv.org/abs/2604.17435)

**<font color=#1a73e8>作者：</font>** Szu-Chi Chen, I-Ning Tsai, Yi-Cheng Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent Speech-to-Speech Translation (S2ST) systems achieve strong semantic accuracy yet consistently strip away non-verbal vocalizations (NVs), such as laughter and crying that convey pragmatic intent, which severely limits real-world utility. We address this via three contributions. First, we propose a synthesis pipeline for building scalable expressive datasets to overcome the data scarcity limitation. Second, we propose MoVE, a Mixture-of-LoRA-Experts architecture with expressive-specialized adapters and a soft-weighting router that blends experts for capturing hybrid expressive states. Third, we show pretrained AudioLLMs enable striking data efficiency: 30 minutes of curated data is enough for strong performance. On English-Chinese S2ST, while comparing with strong baselines, MoVE reproduces target NVs in 76% of cases and achieves the highest human-rated naturalness and emotional fidelity among all compared systems, where existing S2ST systems preserve at most 14% of NVs.

---


### 284. [DEM Refinement and Validation on the Lunar Surface Using Shape-from-Shading with Chandrayaan-2 OHRC Imagery](https://arxiv.org/abs/2604.17436)

**<font color=#1a73e8>作者：</font>** Aaranay Aadi, Jai Gopal Singla, Nitant Dube  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This study presents a Shape from Shading (SfS) framework to enhance sub-metre resolution lunar digital elevation models (DEMs) using imagery from the Orbiter High Resolution Camera (OHRC) aboard Chandrayaan-2. The framework applies SfS to an independent OHRC image of the same region, enabling SfS not just as a refinement tool, but as a source of new topographic data, unconstrained by stereo baseline limitations. The method is applied across three lunar sites, including the Cyrillus crater, the Vikram landing region, and the lunar south pole (Mons Mouton), with a systematic three-stage parameter sweep on the SfS smoothness weight. Results show measurable topographic enhancement, particularly in surface slope statistics, revealing fine-scale crater morphology previously unresolved. A limiting case is also characterized, where large pitch angle separation between the shading image and stereo pair reduces SfS sensitivity, and partial footprint coverage of the shading image is identified as a factor influencing spatially variable enhancement quality.

---


### 285. [Attention Is not Everything: Efficient Alternatives for Vision](https://arxiv.org/abs/2604.17439)

**<font color=#1a73e8>作者：</font>** Nur Mohammad Kazi, Ibteshum Khaled, Md. Luthful Hasan Galib 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently computer vision has seen advancements mainly thanks to Transformer-based models. However many non-Transformer methods are still doing well being a direct competition of Transformer-based models. This review tries to present a comprehensive taxonomy of such methods and organize these methods into categories like convolution-based models, MLP-based models, state-space-based and more. These methods are looked at in terms of how efficient they are, how well they scale, how easy they are to understand and how robust they are. A total of 40 papers were chosen for this study. The goal is to give a view of non-Transformer methods and find out what challenges and opportunities exist for future computer vision research.

---


### 286. [HyKey: Hyperspectral Keypoint Detection and Matching in Minimally Invasive Surgery](https://arxiv.org/abs/2604.17446)

**<font color=#1a73e8>作者：</font>** Alexander Saikia, Chiara Di Vece, Zhehua Mao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose: 3D reconstruction in minimally invasive surgery (MIS) enables enhanced surgical guidance through improved visualisation, tool tracking, and augmented reality. However, traditional RGB-based keypoint detection and matching pipelines struggle with surgical challenges, such as poor texture and complex illumination. We investigate whether using snapshot hyperspectral imaging (HSI) can provide improved results on keypoint detection and matching surgical scenes. Methods: We developed HyKey, a HYperspectral KEYpoint detection and description model made up of a hybrid 3D-2D convolutional neural network that jointly extracts spatial-spectral features from HSI. The model was trained using synthetic homographic augmentation and epipolar geometry constraints on a robotically-acquired dual-camera RGB-HSI laparoscopic dataset of ex-vivo organs with calibrated camera poses. We benchmarked performance against established RGB-based methods, including SuperPoint and ALIKE. Results: Our HSI-based model outperformed RGB baselines on registered RGB frames, achieving 96.62% mean matching accuracy and 67.18% mean average accuracy at 10 degree on pose estimation, demonstrating consistent improvements across multiple evaluation metrics. Conclusion: Integrating spectral information from an HSI cube offers a promising approach for robust monocular 3D reconstruction in MIS, addressing limitations of texture-poor surgical environments through enhanced spectral-spatial feature discrimination. Our model and dataset are available at this https URL

---


### 287. [SegTTA: Training-Free Test-Time Augmentation for Zero-Shot Medical Imaging Segmentation](https://arxiv.org/abs/2604.17451)

**<font color=#1a73e8>作者：</font>** Yihong Yao, Chunlei Li, Canxuan Gang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Increasingly advanced data augmentation techniques have greatly aided clinical medical research, increasing data diversity and improving model generalization capabilities. Although most current basic models exhibit strong generalization abilities, image quality varies due to differences in equipment and operators. To address these challenges, we present SegTTA, a framework that improves medical image segmentation without model retraining by combining four augmentations (Gamma correction, Contrast enhancement, Gaussian blur, Gaussian noise) with weighted voting across multiple MedSAM2 checkpoints. Experiments demonstrate consistent improvements across three diverse datasets: healthy uterus segmentation, uterine myoma detection, and multi class hepatic structure segmentation. Ablation studies reveal that large organs benefit from intensity augmentations while small lesions require noise augmentations. The voting threshold controls the coverage precision trade off, enabling task specific optimization for different clinical requirements. Ultimately, on a multiclass hepatic vessel dataset, compared to MedSAM2 baselines, our method achieves an increase of 1.6 in mIoU and 1.9 in aIoU, along with a reduction of approximately 2.0 in HD95. Code will be available at this https URL.

---


### 288. [HSG: Hyperbolic Scene Graph](https://arxiv.org/abs/2604.17454)

**<font color=#1a73e8>作者：</font>** Liyang Wang, Zeyu Zhang, Hao Tang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scene graph representations enable structured visual understanding by modeling objects and their relationships, and have been widely used for multiview and 3D scene reasoning. Existing methods such as MSG learn scene graph embeddings in Euclidean space using contrastive learning and attention based association. However, Euclidean geometry does not explicitly capture hierarchical entailment relationships between places and objects, limiting the structural consistency of learned representations. To address this, we propose Hyperbolic Scene Graph (HSG), which learns scene graph embeddings in hyperbolic space where hierarchical relationships are naturally encoded through geometric distance. Our results show that HSG improves hierarchical structure quality while maintaining strong retrieval performance. The largest gains are observed in graph level metrics: HSG achieves a PP IoU of 33.17 and the highest Graph IoU of 33.51, outperforming the best AoMSG variant (25.37) by 8.14, highlighting the effectiveness of hyperbolic representation learning for scene graph modeling. Code: this https URL.

---


### 289. [From Adaptation to Generalization: Adaptive Visual Prompting for Medical Image Segmentation](https://arxiv.org/abs/2604.17455)

**<font color=#1a73e8>作者：</font>** Evren Çetinkaya, Sangmin Lee, Jung Uk Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual prompting has emerged as a powerful method for adapting pre-trained models to new domains without updating model parameters. However, existing prompting methods typically optimize a single prompt per domain and apply it uniformly to all inputs, limiting their ability to generalize under intra and inter-domain variability, which is especially critical in the medical field. To address this, we propose APEX, an Adaptive Prompt EXtraction framework that retrieves input-specific prompts from a learnable prompt memory. The memory stores diverse, domain-discriminative prompt representations and is queried via domain features extracted from the Fourier spectrum. To learn robust and discriminative domain features, we introduce a novel Low-Frequency Feature Contrastive (LFC) learning framework that clusters representations from the same domain while separating those from different domains. Extensive experiments on two medical segmentation tasks demonstrate that APEX significantly improves generalization across both seen and unseen domains. Furthermore, it complements any existing backbones and consistently enhances performance, confirming its effectiveness as a plug-and-play prompting solution in medical fields. The code is available at this https URL

---


### 290. [TrafficClaw: Generalizable Urban Traffic Control via Unified Physical Environment Modeling](https://arxiv.org/abs/2604.17456)

**<font color=#1a73e8>作者：</font>** Siqi Lai, Pan Zhang, Yuping Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Urban traffic control is a system-level coordination problem spanning heterogeneous subsystems, including traffic signals, freeways, public transit, and taxi services. Existing optimization-based, reinforcement learning (RL), and emerging LLM-based approaches are largely designed for isolated tasks, limiting both cross-task generalization and the ability to capture coupled physical dynamics across subsystems. We argue that effective system-level control requires a unified physical environment in which subsystems share infrastructure, mobility demand, and spatiotemporal constraints, allowing local interventions to propagate through the network. To this end, we propose TrafficClaw, a framework for general urban traffic control built upon a unified runtime environment. TrafficClaw integrates heterogeneous subsystems into a shared dynamical system, enabling explicit modeling of cross-subsystem interactions and closed-loop agent-environment feedback. Within this environment, we develop an LLM agent with executable spatiotemporal reasoning and reusable procedural memory, supporting unified diagnostics across subsystems and continual strategy refinement. Furthermore, we introduce a multi-stage training pipeline with supervised initialization and agentic RL with system-level optimization, further enabling coordinated and system-aware performance. Experiments demonstrate that TrafficClaw achieves robust, transferable, and system-aware performance across unseen traffic scenarios, dynamics, and task configurations. Our project is available at this https URL.

---


### 291. [Machine Learning Hamiltonian Dynamical Systems with Sparse and Noisy Data](https://arxiv.org/abs/2604.17470)

**<font color=#1a73e8>作者：</font>** Vedanta Thapar, Abhinav Gupta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning has become a powerful tool for discovering governing laws of dynamical systems from data. However, most existing approaches degrade severely when observations are sparse, noisy, or irregularly sampled. In this work, we address the problem of learning symbolic representations of nonlinear Hamiltonian dynamical systems under extreme data scarcity by explicitly incorporating physical structure into the learning architecture. We introduce Adaptable Symplectic Recurrent Neural Networks (ASRNNs), a parameter-cognizant, structure-preserving model that combines Hamiltonian learning with symplectic recurrent integration, avoiding time derivative estimation, and enabling stable learning under noise. We demonstrate that ASRNNs can accurately predict long-term dynamics even when each training trajectory consists of only two irregularly spaced time points, possibly corrupted by correlated noise. Leveraging ASRNNs as structure-preserving data generators, we further enable symbolic discovery using independent regression methods (SINDy and PySR), recovering exact symbolic equations for polynomial systems and consistent polynomial approximations for non-polynomial Hamiltonians. Our results show that such architectures can provide a robust pathway to interpretable discovery of Hamiltonian dynamics from sparse and noisy data.

---


### 292. [UniMesh: Unifying 3D Mesh Understanding and Generation](https://arxiv.org/abs/2604.17472)

**<font color=#1a73e8>作者：</font>** Peng Huang, Yifeng Chen, Zeyu Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in 3D vision have led to specialized models for either 3D understanding (e.g., shape classification, segmentation, reconstruction) or 3D generation (e.g., synthesis, completion, and editing). However, these tasks are often tackled in isolation, resulting in fragmented architectures and representations that hinder knowledge transfer and holistic scene modeling. To address these challenges, we propose UniMesh, a unified framework that jointly learns 3D generation and understanding within a single architecture. First, we introduce a novel Mesh Head that acts as a cross model interface, bridging diffusion based image generation with implicit shape decoders. Second, we develop Chain of Mesh (CoM), a geometric instantiation of iterative reasoning that enables user driven semantic mesh editing through a closed loop latent, prompting, and re generation cycle. Third, we incorporate a self reflection mechanism based on an Actor Evaluator Self reflection triad to diagnose and correct failures in high level tasks like 3D captioning. Experimental results demonstrate that UniMesh not only achieves competitive performance on standard benchmarks but also unlocks novel capabilities in iterative editing and mutual enhancement between generation and understanding. Code: this https URL. Website: this https URL.

---


### 293. [Privatar: Scalable Privacy-preserving Multi-user VR via Secure Offloading](https://arxiv.org/abs/2604.17476)

**<font color=#1a73e8>作者：</font>** Jianming Tong, Hanshen Xiao, Krishna Kumar Nair 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-user virtual reality enables immersive interaction. However, rendering avatars for numerous participants on each headset incurs prohibitive computational overhead, limiting scalability. We introduce a framework, Privatar, to offload avatar reconstruction from headset to untrusted devices within the same local network while safeguarding attacks against adversaries capable of intercepting offloaded data. Privatar's key insight is that domain-specific knowledge of avatar reconstruction enables provably private offloading at minimal cost. (1) System level. We observe avatar reconstruction is frequency-domain decomposable via BDCT with negligible quality drop, and propose Horizontal Partitioning (HP) to keep high-energy frequency components on-device and offloads only low-energy components. HP offloads local computation while reducing information leakage to low-energy subsets only. (2) Privacy level. For individually offloaded, multi-dimensional signals without aggregation, worst-case local Differential Privacy requires prohibitive noise, ruining utility. We observe users' expression statistical distribution are slowly changing over time and trackable online, and hence propose Distribution-Aware Minimal Perturbation. DAMP minimizes noise based on each user's expression distribution to significantly reduce its effects on utility, retaining formal privacy guarantee. Combined, HP provides empirical privacy against expression identification attacks. DAMP further augments it to offer a formal guarantee against arbitrary adversaries. On a Meta Quest Pro, Privatar supports 2.37x more concurrent users at 6.5% higher reconstruction loss and 9% energy overhead, providing a better throughout-loss Pareto frontier over quantization, sparsity and local construction baselines. Privatar provides both provable privacy guarantee and stays robust against both empirical and NN-based attacks.

---


### 294. [Unveiling Deepfakes: A Frequency-Aware Triple Branch Network for Deepfake Detection](https://arxiv.org/abs/2604.17477)

**<font color=#1a73e8>作者：</font>** Qihao Shen, Jiaxing Xuan, Zhenguang Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Advanced deepfake technologies are blurring the lines between real and fake, presenting both revolutionary opportunities and alarming threats. While it unlocks novel applications in fields like entertainment and education, its malicious use has sparked urgent ethical and societal concerns ranging from identity theft to the dissemination of misinformation. To tackle these challenges, feature analysis using frequency features has emergedas a promising direction for deepfake detection. However, oneaspect that has been overlooked so far is that existing methodstend to concentrate on one or a few specific frequency domains,which risks overfitting to particular artifacts and significantlyundermines their robustness when facing diverse forgery patterns. Another underexplored aspect we observe is that different features often attend to the same forged region, resulting in redundant feature representations and limiting the diversity of the extracted clues. This may undermine the ability of a model to capture complementary information across different facets, thereby compromising its generalization capability to diverse manipulations. In this paper, we seek to tackle these challenges from two aspects: (1) we propose a triple-branch network that jointly captures spatial and frequency features by learning from both original image and image reconstructed by different frequency channels, and (2) we mathematically derive feature decoupling and fusion losses grounded in the mutual information theory, which enhances the model to focus on task-relevant features across the original image and the image reconstructed by different frequency channels. Extensive experiments on six large-scale benchmark datasets demonstrate that our method consistently achieves state-of-the-art performance. Our code is released at this https URL Deepfake.

---


### 295. [Trustworthy deep domain adaptation for wearable photoplethysmography signal analysis with decision-theoretic uncertainty quantification](https://arxiv.org/abs/2604.17480)

**<font color=#1a73e8>作者：</font>** Ciaran Bench  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In principle, deep generative models can be used to perform domain adaptation; i.e. align the input feature representations of test data with that of a separate discriminative model's training data. This can help improve the discriminative model's performance on the test data. However, generative models are prone to producing hallucinations and artefacts that may degrade the quality of generated data, and therefore, predictive performance when processed by the discriminative model. While uncertainty quantification can provide a means to assess the quality of adapted data, the standard framework for evaluating the quality of predicted uncertainties may not easily extend to generative models due to the common lack of ground truths (among other reasons). Even with ground truths, this evaluation is agnostic to how the generated outputs are used on the downstream task, limiting the extent to which the uncertainty reliability analysis provides insights about the utility of the uncertainties with respect to the intended use case of the adapted examples. Here, we describe how decision-theoretic uncertainty quantification can address these concerns and provide a convenient framework for evaluating the trustworthiness of generated outputs, in particular, for domain adaptation. We consider a case study in photoplethysmography time series denoising for Atrial Fibrillation classification. This formalises a well-known heuristic method of using a downstream classifier to assess the quality of generated outputs.

---


### 296. [Coevolving Representations in Joint Image-Feature Diffusion](https://arxiv.org/abs/2604.17492)

**<font color=#1a73e8>作者：</font>** Theodoros Kouzelis, Spyros Gidaris, Nikos Komodakis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Joint image-feature generative modeling has recently emerged as an effective strategy for improving diffusion training by coupling low-level VAE latents with high-level semantic features extracted from pre-trained visual encoders. However, existing approaches rely on a fixed representation space, constructed independently of the generative objective and kept unchanged during training. We argue that the representation space guiding diffusion should itself adapt to the generative task. To this end, we propose Coevolving Representation Diffusion (CoReDi), a framework in which the semantic representation space evolves during training by learning a lightweight linear projection jointly with the diffusion model. While naively optimizing this projection leads to degenerate solutions, we show that stable coevolution can be achieved through a combination of stop-gradient targets, normalization, and targeted regularization that prevents feature collapse. This formulation enables the semantic space to progressively specialize to the needs of image synthesis, improving its complementarity with image latents. We apply CoReDi to both VAE latent diffusion and pixel-space diffusion, demonstrating that adaptive semantic representations improve generative modeling across both settings. Experiments show that CoReDi achieves faster convergence and higher sample quality compared to joint diffusion models operating in fixed representation spaces.

---


### 297. [A Probabilistic Consensus-Driven Approach for Robust Counterfactual Explanations](https://arxiv.org/abs/2604.17494)

**<font color=#1a73e8>作者：</font>** Marcin Kostrzewa, Maciej Zięba, Jerzy Stefanowski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Counterfactual explanations (CFEs) are essential for interpreting black-box models, yet they often become invalid when models are slightly changed. Existing methods for generating robust CFEs are often limited to specific types of models, require costly tuning, or inflexible robustness controls. We propose a novel approach that jointly models the data distribution and the space of plausible model decisions to ensure robustness to model changes. Using a probabilistic consensus over a model ensemble, we train a conditional normalizing flow that captures the data density under varying levels of classifier agreement. At inference time, a single interpretable parameter controls the robustness level; it specifies the minimum fraction of models that should agree on the target class without retraining the generative model. Our method effectively pushes CFEs toward regions that are both plausible and stable across model changes. Experimental results demonstrate that our approach achieves superior empirical robustness while also maintaining good performance across other evaluation measures.

---


### 298. [Edit Fidelity Field: Semantics-Aware Region Isolation for Training-Free Scene Text Editing](https://arxiv.org/abs/2604.17500)

**<font color=#1a73e8>作者：</font>** Guandong Li, Mengxia Ye  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scene text editing (STE) has achieved remarkable progress in accurately rendering target text through diffusion-based methods. However, we identify a critical yet overlooked problem: edit spillover -- when editing a target text region, existing methods inadvertently modify non-target regions, particularly neighboring text. Through systematic evaluation on 50 real-world scenes across four categories, we reveal that state-of-the-art diffusion editing models exhibit a spillover rate of 94%, meaning nearly all non-target text regions are altered during editing. To address this, we propose the Edit Fidelity Field (EFF), a semantics-aware continuous field that controls per-pixel editing fidelity. Unlike binary masks, EFF leverages OCR-detected text regions to construct a four-zone field: Edit Core (fully editable), Transition Zone (smooth decay), Protected Zone (non-target text, explicitly locked), and Background (strictly preserved). EFF operates as a training-free, model-agnostic post-processing module applicable to any diffusion-based STE method. We further propose per-region spillover quantification, a novel evaluation protocol that measures edit leakage at each non-target text region individually. Experiments demonstrate that EFF reduces spillover rate from 94% to 25% while improving non-target region preservation by +91.4 dB PSNR.

---


### 299. [From Admission to Invariants: Measuring Deviation in Delegated Agent Systems](https://arxiv.org/abs/2604.17517)

**<font color=#1a73e8>作者：</font>** Marcelo Fernandez  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous agent systems are governed by enforcement mechanisms that flag hard constraint violations at runtime. The Agent Control Protocol identifies a structural limit of such systems: a correctly-functioning enforcement engine can enter a regime in which behavioral drift is invisible to it, because the enforcement signal operates below the layer where deviation is measurable. We show that enforcement-based governance is structurally unable to determine whether an agent's behavior remains within the admissible behavior space A0 established at admission time. Our central result, the Non-Identifiability Theorem, proves that A0 is not in the sigma-algebra generated by the enforcement signal g under the Local Observability Assumption, which every practical enforcement system satisfies. The impossibility arises from a fundamental mismatch: g evaluates actions locally against a point-wise rule set, while A0 encodes global, trajectory-level behavioral properties set at admission time. We define the Invariant Measurement Layer (IML), which bypasses this limitation by retaining direct access to the generative model of A0. We prove an information-theoretic impossibility for enforcement-based monitoring; separately, we show IML detects admission-time drift with provably finite detection delay, operating in the region where enforcement is structurally blind. Validated across four settings: three drift scenarios (300 and 1000 steps), a live n8n webhook pipeline, and a LangGraph StateGraph agent -- enforcement triggers zero violations while IML detects each drift type within 9-258 steps. Paper 2 of a 4-paper Agent Governance Series: atomic boundaries (P0, https://doi.org/10.5281/zenodo.19642166), ACP enforcement (P1, arXiv:2603.18829), fair allocation (P3, https://doi.org/10.5281/zenodo.19643928), irreducibility (P4, https://doi.org/10.5281/zenodo.19643950).

---


### 300. [Explainable Attention-Based LSTM Framework for Early Detection of AI-Assisted Ransomware via File System Behavioral Analysis](https://arxiv.org/abs/2604.17522)

**<font color=#1a73e8>作者：</font>** Prabhudarshi Nayak, Gogulakrishnan Thiyagarajan, Debashree Priyadarshini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Ransomware continues to evolve as one of the most disruptive cyber threats, with recent variants increasingly leveraging automated and AI-assisted techniques to evade traditional signature-based defenses. Early detection of such attacks remains a significant challenge, particularly when malicious behavior closely resembles legitimate system activity. This study proposes an explainable attention-based Long Short-Term Memory (LSTM) framework for the early detection of AI assisted ransomware variants through analysis of file system behavioral patterns. The proposed model captures temporal dependencies in file operation sequences, while an attention mechanism highlights critical behavioral indicators associated with ransomware activity. To improve transparency and trust in automated detection systems, explainable artificial intelligence (XAI) techniques are incorporated to interpret model predictions and identify influential behavioral features. Experimental evaluation using ransomware behavioral traces demonstrates that the proposed framework can effectively distinguish malicious activity at early stages of execution with high detection performance and low false-positive rates. The findings suggest that combining sequence-aware deep learning models with explainability mechanisms can significantly enhance the reliability and interpretability of next-generation ransomware defense systems. This work contributes toward the development of intelligent and transparent cyber-defense mechanisms capable of addressing emerging AI-driven malware threats.

---


> [!TIP]
> 当前位于：**251-300**（第 6/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-535](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
