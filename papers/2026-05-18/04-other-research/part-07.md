# 📦 其他研究 | 2026年05月18日

> 本类共 **337** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-337**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-337**

---

### 301. [EverAnimate: Minute-Scale Human Animation via Latent Flow Restoration](https://arxiv.org/abs/2605.15042)

**<font color=#1a73e8>作者：</font>** Wuyang Li, Yang Gao, Mariam Hassan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose EverAnimate, an efficient post-training method for long-horizon animated video generation that preserves visual quality and character identity. Long-form animation remains challenging because highly dynamic human motion must be synthesized against relatively static environments, making chunk-based generation prone to accumulated drift: (i) low-level quality drift, such as progressive degradation of static backgrounds, and (ii) high-level semantic drift, such as inconsistent character identity and view-dependent attributes. To address this issue, EverAnimate restores drifted flow trajectories by anchoring generation to a persistent latent context memory, consisting of two complementary mechanisms. (i) Persistent Latent Propagation maintains a context memory across chunks to propagate identity and motion in latent space while mitigating temporal forgetting. (ii) Restorative Flow Matching introduces an implicit restoration objective during sampling through velocity adjustment, improving within-chunk fidelity. With only lightweight LoRA tuning, EverAnimate outperforms state-of-the-art long-animation methods in both short- and long-horizon settings: at 10 seconds, it improves PSNR/SSIM by 8%/7% and reduces LPIPS/FID by 22%/11%; at 90 seconds, the gains increase to 15%/15% and 32%/27%, respectively.

---


### 302. [Analyzing Codes of Conduct for Online Safety in Video Games at Scale](https://arxiv.org/abs/2605.15047)

**<font color=#1a73e8>作者：</font>** Jiuming Jiang, Shidong Pan, Daniel W Woods 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Online video games have become major online social spaces where users interact, compete, and create together. These spaces, however, expose users to a wide spectrum of online harms, including harassment, discrimination, inappropriate content, privacy breach, cheating, and more. The shape and severity of such harms vary across game design, mechanics, and community context. To mitigate these harms, game companies issue Codes of Conduct (CoCs) that articulate online safety rules and direct players to safety resources. However, it remains unclear how prevalent CoCs are, what safety, security and privacy violations they govern, and whether they meet growing regulatory and industry expectations. We develop and leverage CONDUCTIFY, a pipeline for identifying and analyzing CoCs at scale. Applied to Steam, the largest PC game marketplace, it located the available CoCs for 350 of the 9,586 multiplayer titles on Steam. We found that CoCs are more available among popular, adult-oriented, and community-driven games, while most multiplayer games operate without CoCs despite regulatory and industry recommendations. Although over 80% of the games with CoCs available consistently address traditional security and safety violations, their governance approaches vary substantially across types of violations. A further asymmetry emerges in specificity. Compared with harms related to gameplay mechanics, the articulations of interpersonal harm and the underage player safety are often less specific, despite their relevance to many game communities. Together, these results inform the improvement of online safety governance and CoC enforcement practices, and building better safety infrastructure for the community of players and developers.

---


### 303. [Separating Intrinsic Ambiguity from Estimation Uncertainty in Deep Generative Models for Linear Inverse Problems](https://arxiv.org/abs/2605.15050)

**<font color=#1a73e8>作者：</font>** Yuxin Guo, Dongrui Deng, Pulkit Grover  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently, deep generative models have been used for posterior inference in inverse problems, including high-stakes applications in medical imaging and scientific discovery, where the uncertainty of a prediction can matter as much as the prediction itself. However, posterior uncertainty is difficult to interpret because it can mix ambiguity inherent to the forward operator with uncertainty propagated through inference. We introduce a structural decomposition of posterior uncertainty that isolates intrinsic ambiguity. A cascade formulation makes this ambiguity accessible for calibration analysis, enabling qualitative diagnostics and simulation-based calibration tests that reveal failure modes that remain hidden when models are selected by reconstruction quality alone. We first validate the approach on a Gaussian example with analytical posterior structure, then illustrate the decomposition on accelerated magnetic resonance imaging (MRI), and finally apply the calibration diagnostics to electroencephalography (EEG) source imaging.

---


### 304. [DiffusionOPD: A Unified Perspective of On-Policy Distillation in Diffusion Models](https://arxiv.org/abs/2605.15055)

**<font color=#1a73e8>作者：</font>** Quanhao Li, Junqiu Yu, Kaixun Jiang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has emerged as a powerful tool for improving diffusion-based text-to-image models, but existing methods are largely limited to single-task optimization. Extending RL to multiple tasks is challenging: joint optimization suffers from cross-task interference and imbalance, while cascade RL is cumbersome and prone to catastrophic forgetting. We propose DiffusionOPD, a new multi-task training paradigm for diffusion models based on Online Policy Distillation (OPD). DiffusionOPD first trains task-specific teachers independently, then distills their capabilities into a unified student along the student own rollout trajectories. This decouples single-task exploration from multi-task integration and avoids the optimization burden of solving all tasks jointly from scratch. Theoretically, we lift the OPD framework from discrete tokens to continuous-state Markov processes, deriving a closed-form per-step KL objective that unifies both stochastic SDE and deterministic ODE refinement via mean-matching. We formally and empirically demonstrate that this analytic gradient provides lower variance and better generality compared to conventional PPO-style policy gradients. Extensive experiments show that DiffusionOPD consistently surpasses both multi-reward RL and cascade RL baselines in training efficiency and final performance, while achieving state-of-the-art results on all evaluated benchmarks.

---


### 305. [Deceptive Cookies: Consent by Design -- A Mixed Methods Study](https://arxiv.org/abs/2605.15056)

**<font color=#1a73e8>作者：</font>** Liv Hilde Sjøflot, Tobias A. Opsahl  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> While companies increasingly rely on data, especially when it comes to targeted advertising, adapting content to users, selling data and training machine learning models, the collection of data raises privacy concerns. One way of collecting data is by using HTTP cookies when interacting with a website. Legal regulations require service providers to collect consent for some forms of cookie collection, which is often acquired through \emph{cookie consent banners}, but their effectiveness has been debated. This study aims to understand what influences users' experience and behaviour when managing their cookie consent, by investigating the gap between their stated privacy preferences and their actual actions. A mixed methods approach was used, collecting data from a usability test and a survey (N=20). The results showed that although participants generally want to reject cookie collection, they often end up accepting because of deceptive patterns in the cookie consent banner design. It also showed that they were more willing to consent to websites they trusted and if they expected it would improve their user experience. Although the current EU legislation states that withdrawing consent must be as easy as giving it, withdrawing consent took on average more than 20 times longer than giving it. This suggests that cookie consent banners in their current form are not ideal with respect to user autonomy, often leading users to \emph{consent by design}.

---


### 306. [Computational Imaging Priors for Wireless Capsule Endoscopy: Monte Carlo-Guided Hemoglobin Mapping for Rare-Anomaly Detection](https://arxiv.org/abs/2605.15062)

**<font color=#1a73e8>作者：</font>** Chengshuai Yang, Lei Xing, Gregory Entin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background. RGB-trained capsule-endoscopy classifiers underperform on small-vessel vascular findings by
conflating hemoglobin contrast with bile and illumination falloff. Thus, here we test whether a Monte
Carlo-inspired analytic model can compute hemoglobin from RGB signal built upon extracted classifier.
Methods. On Kvasir-Capsule (47,238 frames, video-level 70/15/15 split, 11 evaluable classes) we evaluate two
software-only configurations against RGB-only EfficientNet-B0 across 6 seeds: (i) a prior P_blood =
sigma(alpha * (H_norm - 0.5)) * Phi(r) fused as 2 zero-init auxiliary channels; (ii) a distillation head
training a 3-channel RGB backbone to predict P_blood. Significance: paired DeLong, McNemar, bootstrap CIs
with Bonferroni correction.
Results. Across 6 seeds (n=6,423), the analytic prior provides a small but direction-consistent macro-AUC
improvement: RGB-only 0.760 +/- 0.027, input-fusion 0.783 +/- 0.024 (paired Delta = +0.023, sign-positive on
5/6 seeds), distillation 0.773 +/- 0.028. The largest robust per-class lift is on Lymphangiectasia, where AUC
rises from RGB 0.238 +/- 0.057 to input-fusion 0.337 +/- 0.019, sign-consistent across all 6 seeds. On rare
focal-vascular classes (Angiectasia, Blood - fresh) the prior's per-seed effects are bimodal: seed=42 reaches
Angiectasia AUC 0.528 -> 0.916, but the cross-seed mean is 0.646 -> 0.608 with sigma_PI = 0.23 - reported as
a high-variance per-seed exemplar.
Conclusion. A Monte Carlo-inspired analytic prior provides a small, direction-consistent macro-AUC
improvement on Kvasir-Capsule across 6 seeds with the largest robust per-class lift on Lymphangiectasia; the
distillation variant runs on plain 3-channel RGB and yields a free interpretability heatmap.

---


### 307. [After the Interface: Relocating Human Agency in the Age of Conversational AI](https://arxiv.org/abs/2605.15064)

**<font color=#1a73e8>作者：</font>** Mengke Wu, Mike Yao  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As AI systems take on greater autonomy, a quiet anxiety has settled over the HCI community: human agency is eroding. Users no longer control execution, interfaces recede, and machines decide. We argue that this anxiety, while understandable, reflects a framing problem rather than an empirical finding. Agency has not diminished but has relocated. As interaction has shifted from command- and feature-based paradigms toward conversational, generative, and agentic AI, human agency migrates from interface affordances to interaction itself: articulating goals, evaluating outputs, and negotiating outcomes. To make this relocation visible, we revisit control as a diagnostic lens, distinguish process control and outcome control, and map different systems across this space to show that what looks like agency's disappearance is actually its redistribution. We take seriously the objection that outcome-based agency may be illusory in systems that produce plausible but unverifiable outputs, and argue that this concern reveals what agency in human-AI interaction truly requires. This paper invites the CUI community to reconsider what agency means, where it lives, and what it demands, including who gets to have it and who holds responsibility when it fails, before the consequences become impossible to overlook.

---


### 308. [Croissant Baker: Metadata Generation for Discoverable, Governable, and Reusable ML Datasets](https://arxiv.org/abs/2605.15079)

**<font color=#1a73e8>作者：</font>** Rafi Al Attrach, Rajna Fani, Sebastian Lobentanzer 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Croissant has emerged as the metadata standard for machine learning datasets, providing a structured, JSON-LD-based format that makes dataset discovery, automated ingestion, and reproducible analysis machine-checkable across ML platforms. Adoption has accelerated, and NeurIPS now requires Croissant metadata in every submission to its dataset tracks. Yet in practice Croissant generation usually starts with uploading data to a public platform, a path infeasible for governed and large local repositories that hold much of the high-value data ML increasingly relies on. We release Croissant Baker, a local-first, open-source command-line tool that generates validated Croissant metadata directly from a dataset directory through a modular handler registry. We evaluate Croissant Baker on over 140 datasets, scaling to MIMIC-IV at 886 million rows and 374 Parquet files. On held-out comparisons against producer-authored or standards-derived ground truth, Croissant Baker reaches 97-100% agreement across multiple domains.

---


### 309. [ML-Embed: Inclusive and Efficient Embeddings for a Multilingual World](https://arxiv.org/abs/2605.15081)

**<font color=#1a73e8>作者：</font>** Ziyin Zhang, Zihan Liao, Hang Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The development of high-quality text embeddings is increasingly drifting toward an exclusionary future, defined by three critical barriers: prohibitive computational costs, a narrow linguistic focus that neglects most of the world's languages, and a lack of transparency from closed-source or open-weight models that stifles research. To dismantle these barriers, we introduce ML-Embed, a suite of inclusive and efficient models built upon a new framework: 3-Dimensional Matryoshka Learning (3D-ML). Our framework addresses the computational challenge with comprehensive efficiency across the entire model lifecycle. Beyond the storage benefits of Matryoshka Representation Learning (MRL) and flexible inference-time depth provided by Matryoshka Layer Learning (MLL), we introduce Matryoshka Embedding Learning (MEL) for enhanced parameter efficiency. To address the linguistic challenge, we curate a massively multilingual dataset and train a suite of models ranging from 140M to 8B parameters. In a direct commitment to transparency, we release all models, data, and code. Extensive evaluation on 430 tasks demonstrates that our models set new records on 9 of 17 evaluated MTEB benchmarks, with particularly strong results in low-resource languages, providing a reproducible blueprint for building globally equitable and computationally efficient AI systems.

---


### 310. [Novel Dynamic Batch-Sensitive Adam Optimiser for Vehicular Accident Injury Severity Prediction](https://arxiv.org/abs/2605.15083)

**<font color=#1a73e8>作者：</font>** Daniel Asare Kyei, Alimatu Saadia-Yussiff, Maame G. Asante-Mensah 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The choice of optimiser is important in deep learning, as it strongly influences model efficiency and speed of convergence. However, many commonly used optimisers encounter difficulties when applied to imbalanced and sequential datasets, limiting their ability to capture patterns of minority classes. In this study, we propose Dynamic Batch-Sensitive Adam (DBS-Adam), an optimiser that dynamically scales the learning rate using a batch difficulty score derived from exponential moving averages of gradient norms and batch loss. DBS-Adam improves training stability and accelerates convergence by increasing updates for difficult batches and reducing them for easier ones. We evaluate DBS-Adam by integrating it with Bi-Directional LSTM networks for accident injury severity prediction, addressing class imbalance through SMOTE-ENN resampling and Focal Loss. Four experimental configurations compare baseline Bi-LSTM models and alternative architectures to assess optimiser impact. Rigorous comparison against state-of-the-art optimisers (AMSGrad, AdamW, AdaBound) across five random seeds demonstrated DBS-Adam's competitive performance with statistically significant precision improvements (p=0.020). Results indicate that DBS-Adam outperforms standard optimisation approaches, achieving 95.22% test accuracy, 96.11% precision, 95.28% recall, 95.39% F1-score, and a test loss of 0.0086. The proposed framework enables effective real-time accident severity classification for targeted emergency response and road safety interventions, demonstrating the value of DBS-Adam for learning from imbalanced sequential data.

---


### 311. [PickleFuzzer: A Case Study in Fuzzing for Discrepancies Between Python Pickle Implementations](https://arxiv.org/abs/2605.15084)

**<font color=#1a73e8>作者：</font>** Justin Applegate, Andreas Kellas  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Python's native serialization protocol, pickle, is a powerful but insecure format for transferring untrusted data. It is frequently used, especially for saving machine learning models, despite known security challenges. While developers sometimes mitigate this risk by restricting imports during unpickling or using static and dynamic analysis tools, these approaches are error-prone and depend heavily on accurate interpretations of the Pickle Virtual Machine (PVM) opcodes. Discrepancies across Python's three native PVM modules can lead to incorrect detection of malicious payloads and undermine existing defenses.
To efficiently and scalably identify discrepancies, we present PickleFuzzer, a custom generation-based fuzzer that identifies inconsistencies across pickle implementations. PickleFuzzer generates pickle objects, passes them to each implementation, and detects differences in thrown exceptions or changes to key internal states. It generates pickle objects using a grammar, which we developed to account for the missing pickle specification. It determines discrepancies by comparing the execution behaviors of each test implementation, rather than requiring a specification-derived oracle. PickleFuzzer detected 14 new discrepancies between the pickle implementations. Four discrepancies are critical and can be used to bypass security-critical scanning tools like those deployed on the popular model hosting platform, Hugging Face. We disclosed all findings to the Python Software Foundation for remediation, and additionally disclosed the security issues to a bug bounty platform and were awarded a $750 bounty. We demonstrate that differential testing is a viable approach for identifying security-relevant discrepancies in important pickle implementations, and our work can lead to promising future directions for finding deeper pickle bugs with more directed fuzzing.

---


### 312. [SAGE3D: Soft-guided attention and graph excitation for 3D point cloud corner detection](https://arxiv.org/abs/2605.15088)

**<font color=#1a73e8>作者：</font>** Batuhan Arda Bekar, Can Sarı, Hüseyin Can Gülkan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present SAGE3D, a hybrid Transformer-based model for corner detection in airborne LiDAR point clouds. We propose a multi-stage solution built on a hierarchical encoder-decoder architecture that progressively downsamples point clouds through Set Abstraction layers and recovers per-point predictions via Feature Propagation. We introduce two innovations: Soft-Guided Attention, which injects ground-truth corner labels as a log-prior into attention logits during training to improve precision; then an Excitatory Graph Neural Network positioned at strategic resolutions in the hierarchy, employing positive-only message passing where high-confidence corners reinforce predictions through learned boosting, optimizing for recall. The hierarchical design enables multi-scale feature extraction while our guided attention and excitatory modules ensure corner signals are amplified rather than diluted across scales.

---


### 313. [CoralLite: μCT Reconstruction of Coral Colonies from Individual Corallites](https://arxiv.org/abs/2605.15093)

**<font color=#1a73e8>作者：</font>** Jess Jones, Leonardo Bertini, Kenneth Johnson 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The life history of an individual coral is archived within the accreting skeleton of the colony. While reef-forming coral colonies (e.g. massive \emph{Porites} sp.) may live for hundreds of years and deposit calcareous structures many metres in height and width, their living tissue is a thin outer surface layer comprised of asexually-dividing polyps that only survive a few years. To understand the rate and timing of polyp division and the consequences for colony skeletal growth, scientists need to track the skeletal corallite deposited around each polyp. Here we propose CoralLite, an annotated {\mu}CT scan dataset of entire calcareous skeletons and an associated, first corallite deep learning reconstruction baseline. CoralLite combines fully quantified volumetric segmentations with cross-slice linking for visualisations of 3D models for each corallite up to colony scale. For segmentation, we propose and evaluate in detail a hybrid V-Trans-UNet architecture applicable to segmenting tiled {\mu}CT virtual slabs of \emph{Porites} sp. colonies. The model is pre-trained on weakly annotated data and topology-aware fine-tuned using fully annotated slice sections with 8k+ manual corallite region annotations. On unseen slices of the same colony, the resulting model reaches 0.94 topological accuracy at mean Dice scores of 0.77 on the same colony and projection axis, and 0.63 mean Dice scores on a different, biologically unrelated specimen. Whilst our experiments are limited in scale and context, our results show for the first time that visual machine learning can effectively support full 3D individual corallite modelling from {\mu}CT scans of coral skeletons alone. For reproducibility and as a baseline for future research we publish our full dataset of 697 {\mu}CT slices, 37 partial or full slice annotations, and all network weights and source code with this paper.

---


### 314. [Dual-Dimensional Consistency: Balancing Budget and Quality in Adaptive Inference-Time Scaling](https://arxiv.org/abs/2605.15100)

**<font color=#1a73e8>作者：</font>** Rongman Xu, Yifei Li, Tianzhe Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have demonstrated remarkable abilities in reasoning. However, maximizing their potential through inference-time scaling faces challenges in trade-off between sampling budget and reasoning quality. Current strategies remain inefficient as they typically treat sampling width and depth as orthogonal objectives, where width consensus methods risk reinforcing hallucinations, while depth pruning mechanisms prematurely truncate complex yet valid reasoning chains. Therefore, we propose Dual-Dimensional Consistency (DDC), a unified framework that bridges path quality with adaptive termination. By coupling Confidence-Weighted Bayesian protocol with a Trend-Aware Stratified Pruning, our method ensures that computational resources are concentrated on high quality reasoning paths, filtering hallucinations while accelerating consensus. Evaluations across five benchmarks demonstrate that this approach reduces token consumption by over 10 times while maintaining or exceeding the accuracy of strong baselines across various LLMs.

---


### 315. [Improving Multi-turn Dialogue Consistency with Self-Recall Thinking](https://arxiv.org/abs/2605.15102)

**<font color=#1a73e8>作者：</font>** Renning Pang, Tian Lan, Leyuan Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) based multi-turn dialogue systems often struggle to track dependencies across non-adjacent turns, undermining both consistency and scalability. As conversations lengthen, essential information becomes sparse and is buried in irrelevant context, while processing the entire dialogue history incurs severe efficiency bottlenecks. Existing solutions either rely on high latency external memory or lose fine-grained details through iterative summarization. In this paper, we propose Self-Recall Thinking (SRT), a framework designed to address long-range contextual dependency and sparse informative signals in multi-turn dialogue. SRT identifies helpful historical turns and uses them to generate contextually appropriate responses, enabling the model to selectively recall and reason over context during inference. This process yields an endogenous reasoning process that integrates interpretable recall steps without external modules. SRT incorporates: (1) Dependency Construction: Generating and converting it into self-recall chains; (2)Capability Initialization: Training to enable reasoning chains with recall tokens capability; (3)Reasoning Improvement: Refining accuracy via verifiable rewards to optimize recall and reasoning for correct answers. Experiments on multiple datasets demonstrate that SRT improves F1 score by 4.7% and reduces end-to-end latency by 14.7% over prior methods, achieving a balance between reasoning latency and accuracy, and outperforming state-of-the-art baselines.

---


### 316. [Proposal and study of statistical features for string similarity computation and classification](https://arxiv.org/abs/2605.15110)

**<font color=#1a73e8>作者：</font>** E.O. Rodrigues, D. Casanova, M. Teixeira 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptations of features commonly applied in the field of visual computing, co-occurrence matrix (COM) and run-length matrix (RLM), are proposed for the similarity computation of strings in general (words, phrases, codes and texts). The proposed features are not sensitive to language related information. These are purely statistical and can be used in any context with any language or grammatical structure. Other statistical measures that are commonly employed in the field such as longest common subsequence, maximal consecutive longest common subsequence, mutual information and edit distances are evaluated and compared. In the first synthetic set of experiments, the COM and RLM features outperform the remaining state-of-the-art statistical features. In 3 out of 4 cases, the RLM and COM features were statistically more significant than the second best group based on distances (P-value < 0.001). When it comes to a real text plagiarism dataset, the RLM features obtained the best results.

---


### 317. [Learning from Language Feedback via Variational Policy Distillation](https://arxiv.org/abs/2605.15113)

**<font color=#1a73e8>作者：</font>** Yang Li, Erik Nijkamp, Semih Yavuz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from verifiable rewards (RLVR) suffers from sparse outcome signals, creating severe exploration bottlenecks on complex reasoning tasks. Recent on-policy self-distillation methods attempt to address this by utilizing language feedback to generate dense, token-level supervision. However, these approaches rely on a fixed, passive teacher to interpret the feedback. As the student policy improves, the teacher's zero-shot assessment capabilities plateau, ultimately halting further learning. To overcome this, we propose Variational Policy Distillation (VPD), a framework that formalizes learning from language feedback as a Variational Expectation-Maximization (EM) problem. VPD co-evolves both policies: in the E-step, the teacher is actively refined on trajectory outcomes via an adaptive trust-region update, translating textual feedback into a dynamically improved target token distribution. In the M-step, the student internalizes this dense distributional guidance on its own on-policy rollouts. By continuously improving the teacher's ability to extract actionable signals from textual critique, VPD overcomes the limitations of passive distillation. Evaluated across diverse sources of diagnostic feedback on scientific reasoning and code generation tasks, VPD consistently outperforms both standard RLVR and existing self-distillation baselines. Finally, by stress-testing our framework on rigid mathematical reasoning and cold-start regimes, we illuminate the fundamental bounds of feedback-driven self-distillation compared to pure environment-driven RL.

---


### 318. [DriveCtrl: Conditioned Sim-to-Real Driving Video Generation](https://arxiv.org/abs/2605.15116)

**<font color=#1a73e8>作者：</font>** Haonan Zhao, Yiting Wang, Jingkun Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale labelled driving video data is essential for training autonomous driving systems. Although simulation offers scalable and fully annotated data, the domain gap between synthetic and real-world driving videos significantly limits its utility for downstream deployment. Existing video generation methods are not well-suited for this task, as they fail to simultaneously preserve scene structure, object dynamics, temporal consistency, and visual realism, all of which are critical for maintaining annotation validity in generated data. In this paper, we present DriveCtrl, a depth-conditioned controllable sim-to-real video generation framework for realistic driving video synthesis. Built upon a pretrained video foundation model, DriveCtrl introduces a structure-aware adapter that enables depth-guided generation while preserving the scene layout and motion patterns of the source simulation, producing temporally coherent driving videos that remain aligned with the original simulated sequences. We further introduce a scalable data generation pipeline that transforms simulator videos into realistic driving footage matching the visual style of a target real-world dataset. The pipeline supports three conditioning signals: structural depth, reference-dataset style, and text prompts, while preserving frame-level annotations for downstream perception tasks. To better assess this task, we propose a driving-domain-specific knowledge-informed evaluation metric called Driving Video Realism Score (DVRS) that assesses the realism of generated videos. Experiments demonstrate that DriveCtrl consistently outperforms the base model and competing alternatives in realism, temporal quality, and perception task performance, substantially narrowing the sim-to-real gap for driving video generation.

---


### 319. [Usable but Conventional: An Empirical Study on the UX of AI-Generated Interface Prototypes](https://arxiv.org/abs/2605.15124)

**<font color=#1a73e8>作者：</font>** Karoline Romero, Igor Wiese, Renato Balancieiri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper investigates User Experience (UX) with prototypes generated by Generative Artificial Intelligence (GenAI) tools. An empirical survey with 92 participants evaluated AI-generated and human-created prototypes without prior identification of authorship. We measured UX using the UEQ-S, covering pragmatic and hedonic dimensions. Results indicate positive evaluations in pragmatic aspects, such as usability and efficiency, and neutral or negative evaluations in hedonic aspects, including originality and innovation. We concluded that GenAI can produce functional interfaces but tends to reinforce visual and structural patterns that affect perceptions of originality.

---


### 320. [Training ML Models with Predictable Failures](https://arxiv.org/abs/2605.15134)

**<font color=#1a73e8>作者：</font>** Will Schwarzer, Scott Niekum  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating how often an ML model will fail at deployment scale is central to pre-deployment safety assessment, but a feasible evaluation set is rarely large enough to observe the failures that matter. Jones et al. (2025) address this by extrapolating from the largest k failure scores in an evaluation set to predict deployment-scale failure rates. We give a finite-k decomposition of this estimator's forecast error and show that it has a built-in bias toward over-prediction in the typical case, which is the safety-favorable direction. This bias is offset when the evaluation set misses a rare high-failure mode that the deployment set contains, leaving the forecast to under-predict at deployment scale. We propose a fine-tuning objective, the forecastability loss, that addresses this failure mode. In two proof-of-concept experiments, a language-model password game and an RL gridworld, fine-tuning substantially reduces held-out forecast error while preserving primary-task capability and achieving safety similar to that of supervised baselines.

---


### 321. [Forgetting That Sticks: Quantization-Permanent Unlearning via Circuit Attribution](https://arxiv.org/abs/2605.15138)

**<font color=#1a73e8>作者：</font>** Saisab Sadhu, Pratinav Seth, Vinay Kumar Sankarapu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard unlearning evaluations measure behavioral suppression in full precision, immediately after training, despite every deployed language model being quantized first. Recent work has shown that 4-bit post-training quantization can reverse machine unlearning; we show this is not a tuning artefact but a systematic dual failure: gradient-based methods that achieve meaningful forgetting lose it under compression, while methods that survive quantization barely change the model. Both failures trace to the same root cause: across all baselines, per-parameter updates lie 47-828x below the NF4 quantization bin width; updates diffused across billions of parameters cannot clear quantization bin boundaries, a consequence we formalize as a sparsity-permanence tradeoff. We present MANSU (Mechanistic-Aligned Null-Space Unlearning), which resolves both modes by combining causal circuit attribution to isolate the minimal forget-set subgraph, circuit-restricted null-space projection with a diagonal-Fisher retain bound, and a per-parameter magnitude floor guaranteeing quantization survival by construction. We additionally introduce Circuit Attribution Divergence (CAD), a mechanistic verification metric distinguishing structural erasure from behavioral suppression, a distinction existing metrics cannot make. Across multiple model families and hazard benchmarks, MANSU is the first method to jointly satisfy all four properties with margin on each (meaningful forgetting, retain preservation, non-positive PTQ gap, and structural erasure), while gradient-based baselines recover up to +0.05 accuracy under compression.

---


### 322. [Causal Forcing++: Scalable Few-Step Autoregressive Diffusion Distillation for Real-Time Interactive Video Generation](https://arxiv.org/abs/2605.15141)

**<font color=#1a73e8>作者：</font>** Min Zhao, Hongzhou Zhu, Kaiwen Zheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time interactive video generation requires low-latency, streaming, and controllable rollout. Existing autoregressive (AR) diffusion distillation methods have achieved strong results in the chunk-wise 4-step regime by distilling bidirectional base models into few-step AR students, but they remain limited by coarse response granularity and non-negligible sampling latency. In this paper, we study a more aggressive setting: frame-wise autoregression with only 1--2 sampling steps. In this regime, we identify the initialization of a few-step AR student as the key bottleneck: existing strategies are either target-misaligned, incapable of few-step generation, or too costly to scale. We propose \textbf{Causal Forcing++}, a principled and scalable pipeline that uses \emph{causal consistency distillation} (causal CD) for few-step AR initialization. The core idea is that causal CD learns the same AR-conditional flow map as causal ODE distillation, but obtains supervision from a single online teacher ODE step between adjacent timesteps, avoiding the need to precompute and store full PF-ODE trajectories. This makes the initialization both more efficient and easier to optimize. The resulting pipeline, \ours, surpasses the SOTA 4-step chunk-wise Causal Forcing under the \textit{\textbf{frame-wise 2-step setting}} by 0.1 in VBench Total, 0.3 in VBench Quality, and 0.335 in VisionReward, while reducing first-frame latency by 50\% and Stage 2 training cost by $\sim$$4\times$. We further extend the pipeline to action-conditioned world model generation in the spirit of Genie3. Project Page: this https URL and this https URL .

---


### 323. [MeMo: Memory as a Model](https://arxiv.org/abs/2605.15156)

**<font color=#1a73e8>作者：</font>** Ryan Wei Heng Quek, Sanghyuk Lee, Alfred Wei Lun Leong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) achieve strong performance across a wide range of tasks, but remain frozen after pretraining until subsequent updates. Many real-world applications require timely, domain-specific information, motivating the need for efficient mechanisms to incorporate new knowledge. In this paper, we introduce MeMo (Memory as a Model), a modular framework that encodes new knowledge into a dedicated memory model while keeping the LLM parameters unchanged. Compared to existing methods, MeMo offers several advantages: (a) it captures complex cross-document relationships, (b) it is robust to retrieval noise, (c) it avoids catastrophic forgetting in the LLM, (d) it does not require access to the LLM's weights or output logits, enabling plug-and-play integration with both open and proprietary closed-source LLMs, and (e) its retrieval cost is independent of corpus size at inference time. Our experimental results on three benchmarks, BrowseComp-Plus, NarrativeQA, and MuSiQue, show that MeMo achieves strong performance compared to existing methods across diverse settings.

---


### 324. [Position: Behavioural Assurance Cannot Verify the Safety Claims Governance Now Demands](https://arxiv.org/abs/2605.15164)

**<font color=#1a73e8>作者：</font>** Pratinav Seth, Vinay Kumar Sankarapu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This position paper argues that behavioural assurance, even when carefully designed, is being asked to carry safety claims it cannot verify. AI governance frameworks enacted between 2019 and early 2026 require reviewable evidence of properties such as the absence of hidden objectives, resistance to loss-of-control precursors, and bounded catastrophic capability; current assurance methodologies (primarily behavioural evaluations and red-teaming) are epistemically limited to observable model outputs and cannot verify the latent representations or long-horizon agentic behaviours these frameworks presume to regulate. We formalize this structural mismatch as the audit gap, the divergence between required and achievable verification access, and introduce the concept of fragile assurance to describe cases where the evidential structure does not support the asserted safety claim. Through an analysis of a 21-instrument inventory, we identify an incentive gradient where geopolitical and industrial pressures systematically reward surface-level behavioral proxies over deep structural verification. Finally, we propose a technical pivot: bounding the weight of behavioral evidence in legal text and extending voluntary pre-deployment access with mechanistic-evidence classes, specifically linear probes, activation patching, and before/after-training comparisons.

---


### 325. [Does Synthetic Layered Design Data Benefit Layered Design Decomposition?](https://arxiv.org/abs/2605.15167)

**<font color=#1a73e8>作者：</font>** Kam Man Wu, Haolin Yang, Qingyu Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in image generation have made it easy to produce high-quality images. However, these outputs are inherently flattened, entangling foreground elements, background, and text within a fixed canvas. As a result, flexible post-generation editing remains challenging, revealing a clear last-mile gap toward practical usability. Existing approaches either rely on scarce proprietary layered assets or construct partially synthetic data from limited structural priors. However, both strategies face fundamental challenges in scalability. In this work, we investigate whether pure synthetic layered data can improve graphic design decomposition. We make the assumption that, in graphic design, effective decomposition does not require modeling inter-layer dependencies as precisely as in natural-image composition, since design elements are often intentionally arranged as modular and semantically separable components. Concretely, we conduct a data-centric study based on CLD baseline, which is a state-of-the-art layer decomposition framework. Based on the baseline, we construct our own synthetic dataset, SynLayers, generate textual supervision using vision language models, and automate inference inputs with VLM-predicted bounding boxes. Our study reveals three key findings: (1) even training with purely synthetic data can outperform non-scalable alternatives such as the widely used PrismLayersPro dataset, demonstrating its viability as a scalable and effective substitute; (2) performance consistently improves with increased training data scale, while gains begin to saturate at around 50K samples; and (3) synthetic data enables balanced control over layer-count distributions, avoiding the layer-count imbalance commonly observed in real-world datasets. We hope this data-centric study encourages broader adoption of synthetic data as a practical foundation for layered design editing systems.

---


### 326. [Evidential Reasoning Advances Interpretable Real-World Disease Screening](https://arxiv.org/abs/2605.15171)

**<font color=#1a73e8>作者：</font>** Chenyu Lian, Hong-Yu Zhou, Jing Qin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Disease screening is critical for early detection and timely intervention in clinical practice. However, most current screening models for medical images suffer from limited interpretability and suboptimal performance. They often lack effective mechanisms to reference historical cases or provide transparent reasoning pathways. To address these challenges, we introduce EviScreen, an evidential reasoning framework for disease screening that leverages region-level evidence from historical cases. The proposed EviScreen offers retrospection interpretability through regional evidence retrieved from dual knowledge banks. Using this evidential mechanism, the subsequent evidence-aware reasoning module makes predictions using both the current case and evidence from historical cases, thereby enhancing disease screening performance. Furthermore, rather than relying on post-hoc saliency maps, EviScreen enhances localization interpretability by leveraging abnormality maps derived from contrastive retrieval. Our method achieves superior performance on our carefully established benchmarks for real-world disease screening, yielding notably higher specificity at clinical-level recall. Code is publicly available at this https URL.

---


### 327. [OpenDeepThink: Parallel Reasoning via Bradley--Terry Aggregation](https://arxiv.org/abs/2605.15177)

**<font color=#1a73e8>作者：</font>** Shang Zhou, Wenhao Chai, Kaiyuan Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-time compute scaling is a primary axis for improving LLM reasoning. Existing methods primarily scale depth by extending a single reasoning trace. Scaling breadth by sampling multiple candidates in parallel is straightforward, but introduces a selection bottleneck: choosing the best candidate without a ground-truth verifier, since pointwise LLM judging is noisy and biased. To address this, we introduce OpenDeepThink, a population-based test-time compute framework that selects via pairwise Bradley-Terry comparison. Each generation, the LLM judges random pairs of candidates and aggregates votes via Bradley-Terry into a global ranking; top-ranked candidates are preserved and the top three quarters are mutated using the natural-language critiques produced during comparison; the bottom quarter is discarded. OpenDeepThink raises Gemini 3.1 Pro's effective Codeforces Elo by +405 points in eight sequential LLM-call rounds (~27 minutes wall-clock). The pipeline transfers across weaker and stronger models without retuning, and on the multi-domain HLE benchmark, gains appear concentrated in objectively verifiable domains and reverse in subjective ones. We release CF-73, a curated set of 73 expert-rated Codeforces problems with International Grandmaster annotation and 99% local-evaluation agreement against the official verdict.

---


### 328. [From Plans to Pixels: Learning to Plan and Orchestrate for Open-Ended Image Editing](https://arxiv.org/abs/2605.15181)

**<font color=#1a73e8>作者：</font>** Anirudh Sundara Rajan, Krishna Kumar Singh, Yong Jae Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern image editing models produce realistic results but struggle with abstract, multi step instructions (e.g., ``make this advertisement more vegetarian-friendly''). Prior agent based methods decompose such tasks but rely on handcrafted pipelines or teacher imitation, limiting flexibility and decoupling learning from actual editing outcomes. We propose an experiential framework for long-horizon image editing, where a planner generates structured atomic decompositions and an orchestrator selects tools and regions to execute each step. A vision language judge provides outcome-based rewards for instruction adherence and visual quality. The orchestrator is trained to maximize these rewards, and successful trajectories are used to refine the planner. By tightly coupling planning with reward driven execution, our approach yields more coherent and reliable edits than single-step or rule-based multistep baselines.

---


### 329. [Warp-as-History: Generalizable Camera-Controlled Video Generation from One Training Video](https://arxiv.org/abs/2605.15182)

**<font color=#1a73e8>作者：</font>** Yifan Wang, Tong He  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-controlled video generation has made substantial progress, enabling generated videos to follow prescribed viewpoint trajectories. However, existing methods usually learn camera-specific conditioning through camera encoders, control branches, or attention and positional-encoding modifications, which often require post-training on large-scale camera-annotated videos. Training-free alternatives avoid such post-training, but often shift the cost to test-time optimization or extra denoising-time guidance. We propose Warp-as-History, a simple interface that turns camera-induced warps into camera-warped pseudo-history with target-frame positional alignment and visible-token selection. Given a target camera trajectory, we construct camera-warped pseudo-history from past observations and feed it through the model's visual-history pathway. Crucially, we align its positional encoding with the target frames being denoised and remove warped-history tokens without valid source observations. Without any training, architectural modification, or test-time optimization, this interface reveals a non-trivial zero-shot capability of a frozen video generation model to follow camera trajectories. Moreover, lightweight offline LoRA finetuning on only one camera-annotated video further improves this capability and generalizes to unseen videos, improving camera adherence, visual quality, and motion dynamics without test-time optimization or target-video adaptation. Extensive experiments on diverse datasets confirm the effectiveness of our method.

---


### 330. [When Are Two Networks the Same? Tensor Similarity for Mechanistic Interpretability](https://arxiv.org/abs/2605.15183)

**<font color=#1a73e8>作者：</font>** ML Nissen Gonzalez, Melwina Albuquerque, Laurence Wroe 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability aims to break models into meaningful parts; verifying that two such parts implement the same computation is a prerequisite. Existing similarity measures evaluate either empirical behaviour, leaving them blind to out-of-distribution mechanisms, or basis-dependent parameters, meaning they disregard weight-space symmetries. To address these issues for the class of tensor-based models, we introduce a weight-based metric, tensor similarity, that is invariant to such symmetries. This metric captures global functional equivalence and accounts for cross-layer mechanisms using an efficient recursive algorithm. Empirically, tensor similarity tracks functional training dynamics, such as grokking and backdoor insertion, with higher fidelity than existing metrics. This reduces measuring similarity and verifying faithfulness into a solved algebraic problem rather than one of empirical approximation.

---


### 331. [VGGT-Edit: Feed-forward Native 3D Scene Editing with Residual Field Prediction](https://arxiv.org/abs/2605.15186)

**<font color=#1a73e8>作者：</font>** Kaixin Zhu, Yiwen Tang, Yifan Yang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-quality 3D scene reconstruction has recently advanced toward generalizable feed-forward architectures, enabling the generation of complex environments in a single forward pass. However, despite their strong performance in static scene perception, these models remain limited in responding to dynamic human instructions, which restricts their use in interactive applications. Existing editing methods typically rely on a 2D-lifting strategy, where individual views are edited independently and then lifted back into 3D space. This indirect pipeline often leads to blurry textures and inconsistent geometry, as 2D editors lack the spatial awareness required to preserve structure across viewpoints. To address these limitations, we propose VGGT-Edit, a feed-forward framework for text-conditioned native 3D scene editing. VGGT-Edit introduces depth-synchronized text injection to align semantic guidance with the backbone's spatial poses, ensuring stable instruction grounding. This semantic signal is then processed by a residual transformation head, which directly predicts 3D geometric displacements to deform the scene while preserving background stability. To ensure high-fidelity results, we supervise the framework with a multi-term objective function that enforces geometric accuracy and cross-view consistency. We also construct the DeltaScene Dataset, a large-scale dataset generated through an automated pipeline with 3D agreement filtering to ensure ground-truth quality. Experiments show that VGGT-Edit substantially outperforms 2D-lifting baselines, producing sharper object details, stronger multi-view consistency, and near-instant inference speed.

---


### 332. [FutureSim: Replaying World Events to Evaluate Adaptive Agents](https://arxiv.org/abs/2605.15188)

**<font color=#1a73e8>作者：</font>** Shashwat Goel, Nikhil Chandak, Arvindh Arun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI agents are being increasingly deployed in dynamic, open-ended environments that require adapting to new information as it arrives. To efficiently measure this capability for realistic use-cases, we propose building grounded simulations that replay real-world events in the order they occurred. We build FutureSim, where agents forecast world events beyond their knowledge cutoff while interacting with a chronological replay of the world: real news articles arriving and questions resolving over the simulated period. We evaluate frontier agents in their native harness, testing their ability to predict world events over a three-month period from January to March 2026. FutureSim reveals a clear separation in their capabilities, with the best agent's accuracy being 25%, and many having worse Brier skill score than making no prediction at all. Through careful ablations, we show how FutureSim offers a realistic setting to study emerging research directions like long-horizon test-time adaptation, search, memory, and reasoning about uncertainty. Overall, we hope our benchmark design paves the way to measure AI progress on open-ended adaptation spanning long time-horizons in the real world.

---


### 333. [RAVEN: Real-time Autoregressive Video Extrapolation with Consistency-model GRPO](https://arxiv.org/abs/2605.15190)

**<font color=#1a73e8>作者：</font>** Yanzuo Lu, Ronglai Zuo, Jiankang Deng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Causal autoregressive video diffusion models support real-time streaming generation by extrapolating future chunks from previously generated content. Distilling such generators from high-fidelity bidirectional teachers yields competitive few-step models, yet a persistent gap between the history distributions encountered during training and those arising at inference constrains generation quality over long horizons. We introduce the Real-time Autoregressive Video Extrapolation Network (RAVEN), a training-time test framework that repacks each self rollout into an interleaved sequence of clean historical endpoints and noisy denoising states. This formulation aligns training attention with inference-time extrapolation and allows downstream chunk losses to supervise the history representations on which future predictions depend. We further propose Consistency-model Group Relative Policy Optimization (CM-GRPO), which reformulates a consistency sampling step as a conditional Gaussian transition and applies online Reinforcement Learning (RL) directly to this kernel, avoiding the Euler-Maruyama auxiliary process adopted in prior flow-model RL formulations. Experiments demonstrate that RAVEN surpasses recent causal video distillation baselines across quality, semantic, and dynamic degree evaluations, and that CM-GRPO provides further gains when combined with RAVEN.

---


### 334. [Aligning Latent Geometry for Spherical Flow Matching in Image Generation](https://arxiv.org/abs/2605.15193)

**<font color=#1a73e8>作者：</font>** Tuna Han Salih Meral, Kaan Oktay, Hidir Yesiltepe 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent flow matching for image generation usually transports Gaussian noise to variational autoencoder latents along linear paths. Both endpoints, however, concentrate in thin spherical shells, and a Euclidean chord leaves those shells even when preprocessing aligns their radii. By decomposing each latent token into radial and angular components, we show through component-swap probes that decoded perceptual and semantic content is carried predominantly by direction, with radius contributing much less. We therefore project data latents onto a fixed token radius, use the radial projection of Gaussian noise as the spherical prior, finetune the decoder with the encoder frozen, and replace linear interpolation with spherical linear interpolation. The resulting geodesic paths stay on the sphere at every timestep, and their velocity targets are purely angular by construction. Under matched training, the method consistently improves class-conditional ImageNet-256 FID across different image tokenizers, leaves the diffusion architecture unchanged, and requires no auxiliary encoder or representation-alignment objective.

---


### 335. [VGGT-$Ω$](https://arxiv.org/abs/2605.15195)

**<font color=#1a73e8>作者：</font>** Jianyuan Wang, Minghao Chen, Shangzhan Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent feed-forward reconstruction models, such as VGGT, have proven competitive with traditional optimization-based reconstructors while also providing geometry-aware features useful for other tasks. Here, we show that the quality of these models scales predictably with model and data size. We do so by introducing VGGT-$\Omega$, which substantially improves reconstruction accuracy, efficiency, and capabilities for both static and dynamic scenes. To enable training this model at an unprecedented scale, we introduce architectural changes that improve training efficiency, a high-quality data annotation pipeline that supports dynamic scenes, and a self-supervised learning protocol. We simplify VGGT's architecture by using a single dense prediction head with multi-task supervision and removing the expensive high-resolution convolutional layers. We also use registers to aggregate scene information into a compact representation and introduce register attention, which restricts inter-frame information exchange to these registers, in part replacing global attention. In this way, during training, VGGT-$\Omega$ uses only about 30% of the GPU memory of its predecessor, allowing us to train with 15x more supervised data than prior work and to leverage vast amounts of unlabeled video data. VGGT-$\Omega$ achieves strong results for reconstruction of static and dynamic scenes across multiple benchmarks, for example, improving over the previous best camera estimation accuracy on Sintel by 77%. We also show that the learned registers can improve vision-language-action models and support alignment with language, suggesting that reconstruction can be a powerful and scalable proxy task for spatial understanding. Project Page: this http URL

---


### 336. [RefDecoder: Enhancing Visual Generation with Conditional Video Decoding](https://arxiv.org/abs/2605.15196)

**<font color=#1a73e8>作者：</font>** Xiang Fan, Yuheng Wang, Bohan Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation powers a vast array of downstream applications. However, while the de facto standard, i.e., latent diffusion models, typically employ heavily conditioned denoising networks, their decoders often remain unconditional. We observe that this architectural asymmetry leads to significant loss of detail and inconsistency relative to the input image. To address this, we argue that the decoder requires equal conditioning to preserve structural integrity. We introduce RefDecoder, a reference-conditioned video VAE decoder by injecting high-fidelity reference image signal directly into the decoding process via reference attention. Specifically, a lightweight image encoder maps the reference frame into the detail-rich high-dimensional tokens, which are co-processed with the denoised video latent tokens at each decoder up-sampling stage. We demonstrate consistent improvements across several distinct decoder backbones (e.g., Wan 2.1 and VideoVAE+), achieving up to +2.1dB PSNR over the unconditional baselines on the Inter4K, WebVid, and Large Motion reconstruction benchmarks. Notably, RefDecoder can be directly swapped into existing video generation systems without additional fine-tuning, and we report across-the-board improvements in subject consistency, background consistency, and overall quality scores on the VBench I2V benchmark. Beyond I2V, RefDecoder generalizes well to a wide range of visual generation tasks such as style transfer and video editing refinement.

---


### 337. [EntityBench: Towards Entity-Consistent Long-Range Multi-Shot Video Generation](https://arxiv.org/abs/2605.15199)

**<font color=#1a73e8>作者：</font>** Ruozhen He, Meng Wei, Ziyan Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-shot video generation extends single-shot generation to coherent visual narratives, yet maintaining consistent characters, objects, and locations across shots remains a challenge over long sequences. Existing evaluations typically use independently generated prompt sets with limited entity coverage and simple consistency metrics, making standardized comparison difficult. We introduce EntityBench, a benchmark of 140 episodes (2,491 shots) derived from real narrative media, with explicit per-shot entity schedules tracking characters, objects, and locations simultaneously across easy / medium / hard tiers of up to 50 shots, 13 cross-shot characters, 8 cross-shot locations, 22 cross-shot objects, and recurrence gaps spanning up to 48 shots. It is paired with a three-pillar evaluation suite that disentangles intra-shot quality, prompt-following alignment, and cross-shot consistency, with a fidelity gate that admits only accurate entity appearances into cross-shot scoring. As a baseline, we propose EntityMem, a memory-augmented generation system that stores verified per-entity visual references in a persistent memory bank before generation begins. Experiments show that cross-shot entity consistency degrades sharply with recurrence distance in existing methods, and that explicit per-entity memory yields the highest character fidelity (Cohen's d = +2.33) and presence among methods evaluated. Code and data are available at this https URL.

---


> [!TIP]
> 当前位于：**301-337**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-337**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
