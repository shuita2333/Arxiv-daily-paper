# 📦 其他研究 | 2026年05月06日

> 本类共 **511** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**451-500**（第 10/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-511](./part-11.md)

---

### 451. [SCGNN: Semantic Consistency enhanced Graph Neural Network Guided by Granular-ball Computing](https://arxiv.org/abs/2605.02617)

**<font color=#1a73e8>作者：</font>** Genhao Tian, Taihua Xu, Shuyin Xia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Capturing semantic consistency among nodes is crucial for effective graph representation learning. Existing approaches typically rely on $k$-nearest neighbors ($k$NN) or other node-level full search algorithms (FSA) to mine semantic relationships via exhaustive pairwise similarity computation, which suffer from high computational complexity and rigid neighbor selection, limiting scalability and introducing noisy connections. In this paper, we propose the Semantic Consistency enhanced Graph Neural Network (SCGNN), a novel plug-and-play framework that leverages granular-ball computing (GBC) to efficiently capture semantic consistency in a scalable manner. Unlike node-level FSA methods, SCGNN models group-level semantic structure by adaptively partitioning nodes into granular balls, significantly reducing computational cost while improving robustness to noise. To effectively utilize the discovered group-level semantic consistency, we design a dual enhancement strategy. Specifically, (1) a structure enhancement module constructs an anchor-based graph structure, where each anchor is a virtual node representing the group-level semantic carried by a granular ball, then injecting group-level semantic information into the graph structure; and (2) a supervision enhancement module performs label consistency checking (LCC) by combining GBC predictions with model-generated pseudo-labels, thereby producing more reliable supervision signals. SCGNN is compatible with various GNN backbones. During the forward propagation of SCGNN, the vanilla graph and the augment graph are jointly encoded, and their predictions are fused; during the backpropagation, the supervision enhancement module provides enhanced supervision signals to guide parameter updates.

---


### 452. [Synthetic Users, Real Differences: an Evaluation Framework for User Simulation in Multi-Turn Conversations](https://arxiv.org/abs/2605.02624)

**<font color=#1a73e8>作者：</font>** Yu Lu Liu, Hyokun Yun, Tanya Roosta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> There is growing interest in exploring user simulation as an alternative to gathering and scoring real user-chatbot interactions for AI chatbot evaluation. For this purpose, it is important to ensure the realism of the simulation, i.e., the extent to which simulated dialogues reflect real dialogues users have with chatbots. Most existing methods evaluating simulation realism produce coarse quality signal and remain solely at the level of individual dialogues. To support more rigorous evaluation in this area, we propose realsim, an evaluation framework that enables practitioners to take a distributional view of real vs. simulated dialogues along 8 dimensions, covering attributes related to the communicative functions of the interaction, user states, and the surface form of user messages. We then instantiate the framework with a curated dataset of 1K multi-turn task-focused real user-chatbot dialogues that cover 16 domains of chatbot applications. Overall, we find that simulated users tend to struggle at capturing communication frictions that real users introduce to interactions, which could make evaluations based on such simulations overly optimistic. We also observe variability in performance across different domains, which may indicate a need for domain-specific user simulators.

---


### 453. [Rethinking Low-Light Image Enhancement: A Log-Domain Intensity--Chromaticity Decoupling Perspective](https://arxiv.org/abs/2605.02627)

**<font color=#1a73e8>作者：</font>** Guangrui Bai, Yifan Mei, Yahui Deng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Explicit reconstruction constraints derived from the decoupled representation are further imposed to suppress abnormal channel amplification and chromatic noise. Experiments on LOLv2-Real, MIT-Adobe FiveK, and LSRW show that the proposed method achieves competitive or superior quantitative and visual performance, reaching 29.71 dB PSNR and 0.89 SSIM on LOLv2-Real. DarkFace experiments further indicate improved downstream face detection under low-light conditions. Code and pretrained models are available at: this https URL.

---


### 454. [Mapping Discourse Reframing: A Multi-Layer Network Approach to Italian HPV Vaccine Discourse on X (2010-2024)](https://arxiv.org/abs/2605.02629)

**<font color=#1a73e8>作者：</font>** Lorella Viola  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding how online narratives travel through coalitions is critical for identifying information disorder, yet computational analyses often rely on conservative network constructions that erase initially sparse but salient signals. This paper proposes a novel multi-layer framework that captures low-frequency signals of emerging information disorder allowing for locating where online discourse is reframed and amplified over time. The use case is 14 years of Italian discourse on X regarding the Human Papillomavirus (HPV) vaccine across three pivotal epochs (2010-2024). Utilizing hashtag co-occurrence networks, we introduce a dual-layer approach. We first identify robust core discourse coalitions through conservative community detection, revealing a stable prevention-oriented backbone contrasted with increasingly separable skepticism coalitions. We then introduce a coverage layer and project fringe hashtags into core coalitions based on weighted connectivity. Using a manually labelled set of skeptical and conspiratorial seed tweets, we demonstrate that this core-coverage projection significantly improves the recovery of long-tail, problematic hashtags while preserving an interpretable coalition structure. Our findings characterize the structural maturation of polarized narratives and provide a methodology for mapping how discourse is reframed and amplified by information disorder over time.

---


### 455. [AutoFocus: Uncertainty-Aware Active Visual Search for GUI Grounding](https://arxiv.org/abs/2605.02630)

**<font color=#1a73e8>作者：</font>** Ruilin Yao, Shegnwu Xiong, Tianyu Zou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have enabled autonomous GUI agents that translate natural language instructions into executable screen coordinates. However, grounding performance degrades in high-resolution interfaces, where dense layouts and small interactive elements expose a resolution gap between modern displays and model input constraints. Existing zoom-in strategies rely on fixed anchors, heuristic grids, or reinforcement learning, lacking a principled mechanism to adaptively determine where refinement is needed and how much spatial uncertainty should be explored. We propose AutoFocus, a training-free, uncertainty-aware active visual search framework for GUI grounding. Our key insight is that token-level perplexity in coordinate generation naturally reflects spatial uncertainty. Rather than committing to a single prediction, AutoFocus samples multiple coordinate hypotheses and converts their axial perplexities into an anisotropic gaussian spatial probability field, explicitly modeling directional uncertainty. Based on this field, we generate global and local region proposals and introduce Shape-Aware Zooming to balance tight localization with contextual preservation. A visual prompt-based aggregation step then selects the most consistent prediction via structured comparison. Extensive experiments on ScreenSpot-Pro and ScreenSpot-V2 demonstrate consistent improvements across both general-purpose and GUI-specialized VLMs.

---


### 456. [CNNs for Vis-NIR Chemometrics: From Contradiction to Conditional Design](https://arxiv.org/abs/2605.02636)

**<font color=#1a73e8>作者：</font>** Dário Passos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Near-infrared (NIR; a.k.a.\ NIRS) deep-learning studies in chemometrics increasingly report mutually inconsistent conclusions regarding convolutional neural network (CNN) design, including small versus large kernels, shallow versus deep architectures, raw spectra versus preprocessing, and single-domain training versus transfer learning. As a result, the same architecture can appear superior in one study and inferior in another, creating a practical impasse for chemometric practitioners. In this review, we argue that these contradictions are not evidence of irreconcilable methods but a structurally expected consequence of uncontrolled moderating variables. Specifically, we trace recurring disagreements to (i) the indirect nature of Vis--NIR measurement in water-dominated matrices, (ii) mismatch between effective receptive field (ERF) and the width of informative spectral structure, and (iii) validation design (including split strategy, hyperparameter tuning budget, and exposure to deployment-like shifts) acting as a hidden hyperparameter that can dominate model ranking. Building on evidence from published chemometrics and spectroscopy studies, we propose a conditional design framework that links architecture and preprocessing choices to spectral physics, dataset regime, and intended deployment scenario. Overall, the proposed perspective moves DL Chemometrics from template-driven architecture selection toward reproducible, physics-aware, and deployment-aligned model comparison.

---


### 457. [ViewSAM: Learning View-aware Cross-modal Semantics for Weakly Supervised Cross-view Referring Multi-Object Tracking](https://arxiv.org/abs/2605.02638)

**<font color=#1a73e8>作者：</font>** Jiawei Ge, Xintian Zhang, Jiuxin Cao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-view Referring Multi-Object Tracking (CRMOT) aims to track multiple objects specified by natural language across multiple camera views, with globally consistent identities. Despite recent progress, existing methods rely heavily on costly frame-level spatial annotations and cross-view identity supervision. To reduce such reliance, we explore CRMOT under weak supervision by leveraging the capabilities of foundation models. However, our empirical study shows that directly applying foundation models such as SAM2 and SAM3, even with task-specific modifications, fails to accurately understand referring expressions and maintain consistent identities across views. Yet, they remain effective at producing reliable object tracklets that can serve as pseudo supervision. We therefore repurpose foundation models as pseudo-label generators and propose a two-stage framework for weakly supervised CRMOT, using only object category labels as coarse-grained supervision. In the first stage, we design an Affinity-guided Cross-view Re-prompting strategy to refine and associate SAM3-generated tracklets across cameras, producing reliable cross-view pseudo labels for subsequent training. In the second stage, we introduce ViewSAM, a CRMOT model built upon SAM2 that explicitly models view-aware cross-modal semantics. By formulating view-induced variations as learnable conditions, ViewSAM bridges the gap between view-variant visual observations and view-invariant textual expressions, enabling robust cross-view referring tracking with only approximately 10% additional parameters. Extensive experiments demonstrate that ViewSAM achieves SOTA performance under weak supervision and remains competitive with fully supervised methods.

---


### 458. [Trustworthy AI Suffers from Invariance Conflicts and Causality is The Solution](https://arxiv.org/abs/2605.02640)

**<font color=#1a73e8>作者：</font>** Ruta Binkyte, Ivaxi Sheth, Zhijing Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As artificial intelligence (AI), including machine learning (ML) models and foundation models (FMs), is increasingly deployed in high-stakes domains, ensuring their trustworthiness has become a central challenge. However, the core trustworthy AI objectives, such as fairness, robustness, privacy, and explainability, are hard to achieve simultaneously, especially while preserving utility. This position paper argues that causality is necessary to understand and balance trade-offs in performance and multiple objectives of trustworthy AI. We ground our arguments in re-interpreting trustworthy AI trade-offs as incompatible invariance requirements under different changes to the data-generating process. We then illustrate that causality provides a unifying framework for understanding how trade-offs in trustworthy AI arise, and how they can be softened or resolved through selective invariance. This perspective applies to both classical ML models and large-scale FMs. Our paper discusses how causal assumptions may be applied explicitly or implicitly in modern large-scale systems. Finally, we outline open challenges and opportunities for using causality to build more trustworthy AI.

---


### 459. [Dramaturgies of Deception: AI Humanizers and the Performance of Legitimacy in Higher Education Assessment](https://arxiv.org/abs/2605.02649)

**<font color=#1a73e8>作者：</font>** Jasper Roe, Mike Perkins, Peter Bannister 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) has disrupted assessment in higher education and accelerated a cycle of compounding performances. Institutional policies demand the demonstration of independent authorship, while commercial AI-enabled services allow students to simulate independent thought and writing. This has led to enhanced institutional surveillance, including AI detectors, which are subsequently circumvented using other technologies. AI humanizers, internet-based services that alter AI-generated text to avoid automated or human detection, are a recent symptom of this performative cycle. Little is known about how these services operate, how they appeal to users, and what they imply for educational assessment and integrity. This paper presents an exploratory, systematic investigation of AI humanizer websites, framed through Goffman's sociological account of dramaturgy. Using a systematic search and custom rubric, we cataloged 55 humanizer sites, assessed their performance of identity, and conducted an in-depth multimodal critical discourse analysis of a purposive sample of three sites. Findings show that humanizers are readily available, offer free and premium paid services, and appear to perform similar functions. These include the deletion and discursive absence of misconduct, the framing of AI humanization as a rational and defensible response to surveillance and flawed detection, and appeals to mystification through advanced technology and implied endorsement by universities and corporations. We argue that humanizer services should be viewed as a diagnostic signal: a legible node in a feedback loop of performative assessment. Disrupting this cycle requires structural assessment reform rather than technological solutionism.

---


### 460. [CARD: Coarse-to-fine Autoregressive Modeling with Radix-based Decomposition for Transferable Free Energy Estimation](https://arxiv.org/abs/2605.02657)

**<font color=#1a73e8>作者：</font>** Ziyang Yu, Yi He, Wenbing Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating free energy differences quantifies thermodynamic preferences in molecular interactions, which is central to chemistry and drug discovery. Despite fruitful progress, existing methods still face key limitations: classical computational approaches remain prohibitively expensive due to their reliance on extensive molecular dynamics simulations, while deep learning-based methods are constrained by either less-expressive generative models or input dimensions tied to a specific system, resulting in negligible generalization. To address these challenges, we propose CARD, a generative framework that employs a novel radix-based decomposition to bijectively convert 3D coordinates into mixed discrete-continuous sequences, enabling coarse-to-fine autoregressive modeling with enhanced expressiveness. Notably, the model corresponds to a distribution with zero free energy, serving as a proposal for absolute free energy computation of arbitrary systems without relying on alchemical pathways. Experiments across diverse tasks demonstrate that CARD matches the accuracy of classical computational methods on unseen systems with diverse topologies, while achieving an approximately 40-fold speedup in inference.

---


### 461. [Deciphering Shortcut Learning from an Evolutionary Game Theory Perspective](https://arxiv.org/abs/2605.02658)

**<font color=#1a73e8>作者：</font>** Xiayang Li, Kuo Gai, Shihua Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Shortcut learning causes deep learning models to rely on non-essential features within the data. However, its formation in deep neural network training still lacks theoretical understanding. In this paper, we provide a formal definition of core and shortcut features and employ evolutionary game theory to analyze the origins of shortcut bias by modeling data samples as players and their corresponding neural tangent features as strategies, assuming the existence of core and shortcut subnetworks. We find that gradient descent (GD) and stochastic gradient descent (SGD) lead to two distinct stochastically stable states, each corresponding to a different strategy. The former primarily optimizes the shortcut subnetwork, while the latter primarily optimizes the core subnetwork. We investigate the influence of these strategies on shortcut bias through a continuous stochastic differential equation, and reveal the impact of data noise and optimization noise on the formation of shortcut bias. In brief, our work employs evolutionary game theory to characterize the dynamics of shortcut bias formation and provides a theoretical view on its mitigation.

---


### 462. [Human Activity Recognition Method for Moderate Violence Detection](https://arxiv.org/abs/2605.02659)

**<font color=#1a73e8>作者：</font>** Luis Angel Aparicio Borjas, Victor Elias Nieto, Juan Irving Vasquez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physical violence in public spaces is a significant public health concern, with minor incidents such as pushing often serving as precursors to more severe escalations. This research develops an automated system for the real-time detection of moderate physical violence, specifically pushing, in surveillance camera footage. The proposed solution integrates state-of-the-art computer vision models, utilizing YOLO11 and YOLO11-Pose for human detection and skeletal keypoint extraction. By calculating body inclination and joint angles between shoulders and hips, a Random Forest classifier was trained to distinguish between normal behavior and aggressive physical contact. The system's performance was evaluated through three progressive case studies representing increasing levels of difficulty. In controlled environments with frontal views, the model achieved a precision of 0.98. In the most challenging scenario, featuring high-altitude, steep-angle recordings from real-world surveillance infrastructure, the system maintained a precision of 0.72 despite significant perspective distortion and visual noise. These results demonstrate the feasibility of using skeletal analysis for early violence intervention in urban security contexts.

---


### 463. [AcademiClaw: When Students Set Challenges for AI Agents](https://arxiv.org/abs/2605.02661)

**<font color=#1a73e8>作者：</font>** Junjie Yu, Pengrui Lu, Weiye Si 等 78 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Benchmarks within the OpenClaw ecosystem have thus far evaluated exclusively assistant-level tasks, leaving the academic-level capabilities of OpenClaw largely unexamined. We introduce AcademiClaw, a bilingual benchmark of 80 complex, long-horizon tasks sourced directly from university students' real academic workflows -- homework, research projects, competitions, and personal projects -- that they found current AI agents unable to solve effectively. Curated from 230 student-submitted candidates through rigorous expert review, the final task set spans 25+ professional domains, ranging from olympiad-level mathematics and linguistics problems to GPU-intensive reinforcement learning and full-stack system debugging, with 16 tasks requiring CUDA GPU execution. Each task executes in an isolated Docker sandbox and is scored on task completion by multi-dimensional rubrics combining six complementary techniques, with an independent five-category safety audit providing additional behavioral analysis. Experiments on six frontier models show that even the best achieves only a 55\% pass rate. Further analysis uncovers sharp capability boundaries across task domains, divergent behavioral strategies among models, and a disconnect between token consumption and output quality, providing fine-grained diagnostic signals beyond what aggregate metrics reveal. We hope that AcademiClaw and its open-sourced data and code can serve as a useful resource for the OpenClaw community, driving progress toward agents that are more capable and versatile across the full breadth of real-world academic demands. All data and code are available at this https URL.

---


### 464. [An explainable hypothesis-driven approach to Drug-Induced Liver Injury with HADES](https://arxiv.org/abs/2605.02669)

**<font color=#1a73e8>作者：</font>** Maciej Wisniewski, Bartosz Topolski, Pawel Dabrowski-Tumanski 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Drug-induced liver injury (DILI) remains a leading cause of late-stage clinical trial attrition. However, existing computational predictors primarily rely on binary classification, a framing that limits generalization and yields no mechanistic insight to guide translational decisions. We argue that DILI prediction is better posed as an explainable hypothesis-generation problem.
To support this shift, we introduce the DILER Benchmark, a dataset that extends beyond binary labels by augmenting a curated set of molecules with mechanistic hepatotoxicity hypotheses derived from biomedical literature. We further present HADES, an agentic system designed to generate transparent and auditable reasoning traces. By combining molecular-level predictions, metabolite decomposition, structural understanding, and toxicity pathway evidence, HADES mechanistically assesses DILI risk.
Evaluated on the DILER Benchmark, HADES outperforms existing models in binary classification, achieving a ROC-AUC of 0.68 on the Test Set and 0.59 on the challenging Post-2021 Set, compared with 0.63 and 0.50 for DILI-Predictor, respectively. More importantly, we establish a baseline for mechanistic hypothesis generation, where HADES achieves a Hypothesis Alignment Fuzzy Jaccard Index of 0.16. This result underscores the inherent complexity of the task while highlighting the need for advanced explainable approaches in predictive toxicology.

---


### 465. [The 2026 ACII Dyadic Conversations (DaiKon) Workshop & Challenge](https://arxiv.org/abs/2605.02672)

**<font color=#1a73e8>作者：</font>** Panagiotis Tzirakis, Alice Baird, Jeffrey Brooks 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The 2026 ACII Dyadic Conversations (ACII-DaiKon) Workshop & Challenge introduces a benchmark for modeling interpersonal affect and social dynamics in dyadic conversations. Although conversational affect modeling has advanced rapidly, most benchmarks remain speaker-centric and underrepresent coupled, time-evolving processes between partners, including directional influence, conversational timing coordination, and rapport development. To address this gap, ACII-DaiKon presents three coordinated sub-challenges built on a shared dataset: (1) directional interpersonal influence prediction, (2) turn-taking prediction (next-speaker and time-to-next-speech), and (3) rapport trajectory prediction across full interactions.
The challenge is built on the Hume-DaiKon dataset, comprising 945 dyadic conversations (743.4 hours of audiovisual data) collected under naturalistic conditions across five languages. The benchmark supports multimodal modeling, temporal reasoning, and cross-context generalization through fixed train/validation/test splits, standardized metrics, and released baseline systems. Evaluation uses Concordance Correlation Coefficient (CCC), Pearson correlation, Macro-F1, and Mean Absolute Error (MAE) depending on the sub-challenge.
Baseline experiments establish initial reference performance, with best test results of 0.40 CCC and 0.50 Pearson for influence prediction, 0.66 Macro-F1 and 1.50~s MAE for turn-taking, and 0.68 CCC and 0.70 Pearson for rapport trajectory modeling. These results indicate that while current methods capture coarse dyadic patterns, robust modeling of directional dependence and long-horizon interpersonal dynamics remains challenging. The workshop provides a shared platform for rigorous comparison and cross-disciplinary discussion on data validity, evaluation protocols, and culturally aware modeling for dyadic interaction.

---


### 466. [Spectral Model eXplainer: a chemically-grounded explainability framework for spectral-based machine learning models](https://arxiv.org/abs/2605.02684)

**<font color=#1a73e8>作者：</font>** Jose Vinicius Ribeiro, Rafael Figueira Goncalves, Fabio Luiz Melquiades 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spectral-based machine learning models have been increasingly deployed in chemometrics and spectroscopy, where predictive accuracy is as important as explainability. Current employed eXplainable Artificial Intelligence (XAI) methods are largely adapted from tabular or generic multivariate domains, assigning relevance to isolated spectral variables rather than to the chemically meaningful spectral zones. Widely adopted tools such as SHapley Additive exPlanations (SHAP), Permutation Feature Importance (PFI), and Variable Importance in Projection scores (VIP) were not designed for the physical continuity and high collinearity of spectral data, and their variable-level outputs require post-hoc aggregation to recover zone-level information. This study introduces the Spectral Model eXplainer (SMX), a post-hoc, global, model-agnostic XAI framework that explains spectral classifiers through expert-informed spectral zones. SMX summarizes each zone via PCA, defines quantile-based logical predicates, estimates predicate relevance with perturbation in stochastic subsamples, and aggregates bag-wise rankings in a directed weighted graph summarized by Local Reaching Centrality. A key component is threshold spectrum reconstruction, which back-projects predicate boundaries to the original spectral domain in natural measurement units, enabling direct visual comparison with measured spectra. The method was evaluated on eight real spectral datasets (six based on X-ray Fluorescence--XRF and two based on Gamma-ray Spectrometry) and one synthetic benchmark with known gr

---


### 467. [MSMixer: Learned Multi-Scale Temporal Mixing with Complementary Linear Shortcut for Long-Term Time Series Forecasting](https://arxiv.org/abs/2605.02689)

**<font color=#1a73e8>作者：</font>** Ahmed Cherif  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-term time series forecasting requires models that simultaneously capture rapid oscillations, medium-range periodicities, and slowly evolving macro-trends from a fixed look-back window. Existing lightweight MLP-based models typically operate on a single temporal resolution, limiting their ability to explicitly model patterns at multiple scales. We propose MSMixer, a channel-independent multi-scale MLP architecture that addresses this limitation through three complementary innovations: (i) three parallel scale branches at down-sample factors {1x, 4x, 16x} with independent MLP blocks, (ii) a learnable softmax gate that dynamically weighs branch outputs, and (iii) a DLinear complementary shortcut that provides full-window trend and seasonality context. MSMixer contains only 112K parameters at H=96 and runs at O(T) complexity. Evaluated on four ETT benchmarks with standard chronological splits and three random seeds, MSMixer achieves the lowest average MSE (0.357) among lightweight models, outperforming DLinear (0.386, -7.4%) and NLinear (0.365, -2.1%), winning 12 of 16 configurations. Against five Transformer-based baselines from the literature, MSMixer achieves best or second-best MSE in 9 of 16 configurations while using 5x fewer parameters than PatchTST. Ablation and sensitivity analyses confirm the complementary contributions of the multi-scale branches and the DLinear shortcut.

---


### 468. [Reflecthernet: Exfiltrating 100BASE-TX Ethernet Traffic Using a Retroreflector Hardware Trojan](https://arxiv.org/abs/2605.02702)

**<font color=#1a73e8>作者：</font>** Pierre Granier, Matthieu Davy, Philippe Besnier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Electromagnetic eavesdropping is a well-established attack vector for remotely monitoring a target activity, most notably displays, over considerable ranges. Other targets have been considered resistant to such attacks or do not exhibit sufficient electromagnetic leakage for practical exploitation. Radio-frequency retroreflector attacks (RFRA) were developed to enable covert, active monitoring of a target by implanting a minimal hardware Trojan. These implants, typically implemented using discrete components such as transistors or diodes, do not betray their presence by emitting signals themselves; rather, they modulate the electromagnetic reflectivity of the target depending on the probed signal line data. Prior RFRA work has demonstrated their viability against video links and low-speed peripheral interfaces. In this work, we extend the applicability of RFRA to high-speed targets by presenting a successful attack on the 100BASE-TX Ethernet standard. We describe the design and realization of a compact implant capable of recovering the MLT-3 encoded signaling used in Fast Ethernet, as well as a dedicated demodulation and interpretation pipeline that mitigates errors introduced by the radio channel and maximizes the amount of recovered information. Experimental results validate the feasibility of covertly monitoring Fast Ethernet traffic using RF retroreflection and highlight the viability of such attacks for high-speed links.

---


### 469. [ProPACT: A Proactive AI-Driven Adaptive Collaborative Tutor for Pair Programming](https://arxiv.org/abs/2605.02703)

**<font color=#1a73e8>作者：</font>** Anahita Golrang, Kshitij Sharma, olga viberg  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Effective pair programming depends on coordination of attention, cognitive effort, and joint regulation over time, yet most adaptive learning systems remain individual-centric and reactive. This paper introduces ProPACT, a proactive AI-driven adaptive collaborative tutor that treats collaboration itself as the object of instruction. ProPACT constructs a multimodal dyadic learner model based on Joint Visual Attention (JVA), Joint Mental Effort (JME), and individual mental effort, and employs an XGBoost-based forecasting model to predict emerging suboptimal collaboration states up to 30 seconds in advance. These predictions drive a hierarchical adaptive policy that delivers minimally intrusive scaffolds while fading support during productive collaboration. A within-subject study with 26 pair-programming dyads shows that proactive feedback significantly improves debugging success, task efficiency, feedback uptake, and post-intervention gains in JVA and JME, demonstrating the potential of forecast-driven dyadic adaptivity for real-time collaborative learning regulation.

---


### 470. [Federated Reinforcement Learning for Efficient Mobile Crowdsensing under Incomplete Information](https://arxiv.org/abs/2605.02705)

**<font color=#1a73e8>作者：</font>** Sumedh J. Dongare, Patrick Weber, Andrea Ortiz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mobile crowdsensing (MCS) is a distributed sensing architecture that utilizes existing sensors on mobile units (MUs) to perform sensing tasks. A mobile crowdsensing platform (MCSP) publishes the sensing tasks and the MUs decide whether to participate in exchange for money. The MCS system is dynamic: the task requirements, the MUs' availability, and their available resources change over time. The MUs aim to find an efficient task participation strategy to maximize their income while the MCSP focuses on maximizing the number of completed tasks. As optimal strategies require perfect non-causal information about the MCS system, which is unavailable in realistic scenarios, the main challenge is to find an efficient task participation strategy for the MUs under incomplete information. To this end, a novel fully decentralized federated deep reinforcement learning algorithm, FDRL-PPO, is proposed. FDRL-PPO enables every MU to learn its own task participation strategy based on its experiences, available resources, and preferences, without relying on perfect non-causal information about the MCS system. To replenish their batteries, the MUs rely on energy harvesting. As a result, their available energy varies over time, leading to varying availability and fragmented learning experiences. To mitigate these challenges, the proposed approach leverages federated learning, enabling MUs to collaboratively improve their models without sharing private raw data like their own experiences. By exchanging only learned models, MUs collectively compensate for individual limitations, and find more scalable, robust, and efficient task participation strategies. Comprehensive evaluations on both synthetic and real-world datasets show that FDRL-PPO consistently outperforms benchmark algorithms in terms of task completion ratio, fairness in task completion, energy consumption, and number of conflicting proposals.

---


### 471. [SAIL: Structure-Aware Interpretable Learning for Anatomy-Aligned Post-hoc Explanations in OCT](https://arxiv.org/abs/2605.02707)

**<font color=#1a73e8>作者：</font>** Tienyu Chang, Tianhao Li, Ruogu Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical coherence tomography (OCT), a commonly used retinal imaging modality, plays a central role in retinal disease diagnosis by providing high-resolution visualization of retinal layers. While deep learning (DL) has achieved expert-level accuracy in OCT-based retinal disease detection, its "black box" nature poses challenges for clinical adoption, where explainability is essential for clinical trust and regulatory approval. Existing post-hoc explainable AI (XAI) methods often struggle to delineate fine-grained lesion structures, respect anatomical boundaries, or suppress noise, limiting the trustworthiness of their explanations. To bridge these gaps, we propose a Structure-Aware Interpretable Learning (SAIL) framework that integrates retinal anatomical priors at the representation level and couples them with semantic features via a fusion design. Without modifying standard post-hoc explainability methods, this representation yields sharper and more anatomically aligned attribution maps. Comprehensive experiments on diverse OCT datasets demonstrate that our structure-aware method consistently enhances interpretability, producing clinically meaningful and anatomy-aware explanations. Ablation studies further show that strong interpretability requires both structural priors and semantic features, and that properly fusing the two is critical to achieve the best explanation quality. Together, these results highlight structure-aware representations as a key step toward reliable explainability in OCT.

---


### 472. [An Empirical Study of Agent Skills for Healthcare: Practice, Gaps, and Governance](https://arxiv.org/abs/2605.02709)

**<font color=#1a73e8>作者：</font>** Gelei Xu, Ningzhi Tang, Xueyang Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Healthcare automation is shaped by local procedures and organizational constraints, so agent capabilities rarely transfer unchanged across settings. Agent skills, self-contained directories that package reusable procedures for AI agents, are emerging as a procedural layer for adapting healthcare agents across diverse healthcare settings. We present the first empirical analysis of healthcare agent skills, drawing on 557 healthcare-related skills filtered from 58,159 public skills on ClawHub and annotated along ten dimensions covering function, deployment context, autonomy, and safety. We find that public healthcare skills emphasize patient-facing workflow automation and monitoring rather than the diagnostic and treatment-oriented tasks foregrounded in healthcare-agent research; coverage of the healthcare lifecycle and specialized clinical inputs remains uneven; and general technical risk does not reliably capture clinical risk. These findings position healthcare skills as a procedural layer not yet addressed by current benchmarks and risk frameworks.

---


### 473. [Augmenting Interface Usability Heuristics for Reliable Computer-Use Agents](https://arxiv.org/abs/2605.02729)

**<font color=#1a73e8>作者：</font>** Jiateng Liu, Rushi Wang, Bingxuan Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent advances have enabled general computer-use agents that interpret screens and execute grounded actions from human instructions, yet they still struggle to generalize to unseen and evolving interfaces. While improving agent capability remains important, agent compatible interface design offers a complementary path by aligning interaction semantics with agent prior knowledge. In this paper, we revisit Nielsen 10 usability heuristics through the lens of computer-use agents, identifying which principles naturally transfer, where implicit design assumptions create agent specific failures, and how safe additive augmentations can improve robustness without harming human usability. To evaluate these ideas, we introduce UI-Verse, a suite of controlled environments built around functionally similar interfaces with different applied heuristics. Experiments show that our augmented heuristics consistently improve task completion and modestly improve efficiency, with combined heuristics yielding further gains. Human studies further show that these designs preserve the original interaction workflow without observable usability regressions. Overall, our findings highlight interface design as a practical complementary avenue for improving the reliability and generalization of computer use agents.

---


### 474. [Perceptual Flow Network for Visually Grounded Reasoning](https://arxiv.org/abs/2605.02730)

**<font color=#1a73e8>作者：</font>** Yangfu Li, Yuning Gong, Hongjian Zhan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the success of Large-Vision Language Models (LVLMs), general optimization objectives (e.g., standard MLE) fail to constrain visual trajectories, leading to language bias and hallucination. To mitigate this, current methods introduce geometric priors from visual experts as additional supervision. However, we observe that such supervision is typically suboptimal: it is biased toward geometric precision and offers limited reasoning utility. To bridge this gap, we propose Perceptual Flow Network (PFlowNet), which eschews rigid alignment with the expert priors and achieves interpretable yet more effective visual reasoning. Specifically, PFlowNet decouples perception from reasoning to establish a self-conditioned generation process. Based on this, it integrates multi-dimensional rewards with vicinal geometric shaping via variational reinforcement learning, thereby facilitating reasoning-oriented perceptual behaviors while preserving visual reliability. PFlowNet delivers a provable performance guarantee and competitive empirical results, particularly setting new SOTA records on V* Bench (90.6%) and MME-RealWorld-lite (67.0%).

---


### 475. [Coherent Hierarchical Multi-Label Learning to Defer for Medical Imaging](https://arxiv.org/abs/2605.02734)

**<font color=#1a73e8>作者：</font>** Joshua Strong, Pramit Saha, Emma Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning to Defer (L2D) enables a model to predict autonomously or defer to an expert, but prior work largely assumes flat label spaces. We study the first L2D setting with hierarchical multi-label decisions, motivated by medical-imaging workflows in which findings are organised by clinical taxonomies. In this setting, deferral is a delegation action rather than a label assignment, so treating it as an independent per-label decision can produce deferral incoherence, including taxonomic contradictions, delegation violations, and deferrals of labels already implied by the model's own assertions. We formalise coherent hierarchical deferral under a Selective-Exclusion handoff contract, characterise the Bayes-optimal coherent deferral rule, and show that even nodewise Bayes L2D can be action-incoherent. We then propose two remedies: exact coherent projection, a dynamic-programming decoder over the coherent action set, and Taxonomic Belief Propagation (TBP) with Recursive Policy Optimisation (RPO), a contract-aware joint action model trained through the same recursion used at inference. Across real-reader and controlled-expert medical-imaging benchmarks, naive binary-relevance L2D exhibits non-trivial incoherence. Projection removes it exactly, and fast TBP+RPO drives incoherence near zero while retaining strong utility.

---


### 476. [SIAM: Head and Brain MRI Segmentation from Few High-Quality Templates via Synthetic Training](https://arxiv.org/abs/2605.02737)

**<font color=#1a73e8>作者：</font>** Romain Valabregue, Ines Khemir, Eric Badinet 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic training has recently advanced brain MRI segmentation by enabling contrast-agnostic models trained entirely on generated data. However, most existing approaches rely on hundreds of automatically labeled templates, introducing systematic biases and limiting their flexibility to incorporate new anatomical structures. We present the Segment It All Model (SIAM), a 3D whole-head segmentation framework for 16 anatomical structures, trained using only six high-quality, manually annotated templates. SIAM extends domain randomization to both intensity and shape domains: synthetic image generation ensures contrast variability, while high-resolution spatial transformations model anatomical differences in cortical thickness and deep nuclei morphology. Unlike prior synthetic models, SIAM simultaneously segments brain as well as extra-cerebral tissues, including cerebrospinal fluid, vessels, dura mater, skull, and skin, enabling fully automated, preprocessing-free analysis. Evaluation across eight heterogeneous datasets (N=301), that include multiple contrasts (T1-weighted, T2-weighted, CT) and span a wide range of ages, demonstrates that SIAM matches or outperforms state-of-the-art methods for brain structures, in addition to extending automated segmentation to non-brain structures. The model also exhibits superior consistency across contrasts and repeated acquisitions, together with improved sensitivity to subtle gray matter atrophy. We openly release the model and the label templates at this https URL.

---


### 477. [AI and Open-data Driven Scalable Solar Power Profiling](https://arxiv.org/abs/2605.02738)

**<font color=#1a73e8>作者：</font>** Shiliang Zhang, Sabita Maharjan, Damla Turgut  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Solar photovoltaic (PV) deployment is expanding rapidly, yet detailed, up-to-date information on the spatial distribution and capacity of rooftop PV remains limited. This paper presents an open, scalable framework for detecting solar panels from open data and generating city-level solar power profiles. We leverage foundation vision AI models to detect solar panel geometries from open-source satellite imagery. This avoids manual data labeling and case-specific model training while maintaining robustness across heterogeneous imagery. Detected solar panels are converted into georeferenced polygons, yielding spatially explicit and incrementally extensible inventories. By integrating open weather data, we translate panel footprints into regional solar power profiles. The framework reduces dependency on proprietary imagery, manual labeling, and closed-source models, and offers a transparent and scalable approach for solar planning and analysis. We released the data and an API resulted from this work. For any user-specified building location, our API retrieves aerial imagery, detects rooftop solar panels, and returns georeferenced polygons. This empowers researchers and developers to scan user-defined areas to build solar panel maps and associated solar production profiles, thus facilitating advanced analysis like distributed solar production integration, local power flow optimization, energy tariff design, and infrastructure planning.

---


### 478. [Triple Spectral Fusion for Sensor-based Human Activity Recognition](https://arxiv.org/abs/2605.02743)

**<font color=#1a73e8>作者：</font>** Ye Zhang, Longguang Wang, Qing Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The field of sensor-based human activity recognition (HAR) mainly uses posture, motion and context data of Inertial Measurement Units (IMUs) to identify daily activities. Despite the advancements in learning-based methods, it is challenging to perform information fusion from the temporal perspective due to the complexities in fusing heterogeneous sensor data and establishing long-term context correlations. This paper proposes a novel triple spectral fusion framework tailored for HAR. First, we develop an adaptive complementary filtering technique for noise suppression and organize each IMU's sensors into posture and motion modality nodes. Given that IMU nodes form a dynamic heterogeneous graph, we then apply adaptive filtering within the graph Fourier domain to merge both homogeneous and heterogeneous node information. Furthermore, an adaptive wavelet frequency selection approach is implemented to suppress context redundancy and shorten the length of features. This approach enhances both timestamp-based graph aggregation and the correlation of long-term contexts. Our framework uses adaptive filtering in the Fourier, graph Fourier, and wavelet domains, enabling effective multi-sensor fusion and context correlation. Extensive experiments on ten benchmark datasets demonstrate the superior performance of our framework. Project page: this https URL.

---


### 479. [Virtual Scanning for NSCLC Histology: Investigating the Discriminatory Power of Synthetic PET](https://arxiv.org/abs/2605.02746)

**<font color=#1a73e8>作者：</font>** Fatih Aksu, Laura Ciuffetti, Francesco Di Feola 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate histological differentiation between adenocarcinoma (ADC) and squamous cell carcinoma (SCC) is critical for personalized treatment in non-small cell lung cancer (NSCLC). While [$^{18}$F]FDG PET/CT is a standard tool for the clinical evaluation of lung cancer, its utility is often limited by high costs and radiation exposure. In this paper, we investigate the feasibility of "virtual scanning" as a feature-enhancement strategy by evaluating whether synthetic PET data can provide complementary feature representations to supplement anatomical CT scans in histological subtype classification.
We propose a framework that leverages a 3D Pix2Pix Generative Adversarial Network (GAN), pretrained on the FDG-PET/CT Lesions dataset, to synthesize pseudo-PET volumes from anatomical CT scans. These synthetic volumes are integrated with structural CT data within the MINT framework, a multi-stage intermediate fusion architecture.
Our experiments, conducted on a multi-center dataset of 714 subjects, demonstrate that the inclusion of synthetic metabolic features significantly improves classification performance over a CT-only baseline. The multimodal approach achieved a statistically significant increase in the Area Under the Curve (AUC) from 0.489 to 0.591 and improved the Geometric Mean (GMean) from 0.305 to 0.524. These results suggest that synthetic PET scans provide discriminatory metabolic cues that enable deep learning models to exploit complementary cross-modal information, offering a potential feature-enhancement strategy for clinical scenarios where physical PET scans are unavailable.

---


### 480. [Does it Really Count? Assessing Semantic Grounding in Text-Guided Class-Agnostic Counting](https://arxiv.org/abs/2605.02752)

**<font color=#1a73e8>作者：</font>** Giacomo Pacini, Luca Ciampi, Nicola Messina 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-world text-guided class-agnostic counting (CAC) has emerged as a flexible paradigm for counting arbitrary object classes by using natural language prompts. However, current evaluation protocols primarily focus on standard counting errors within single-category images, overlooking a fundamental requirement: the ability to correctly ground the textual prompt in the visual scene. In this paper, we show that several state-of-the-art CAC models often struggle to determine which object class should be counted based on the given prompt, revealing a misalignment between textual semantics and visual object representations. This limitation leads to spurious counting responses and reduced reliability in real-world scenarios. To systematically address these limitations, we propose a new evaluation framework focused on model robustness and trustworthiness. Our contribution is two-fold: (i) we introduce PrACo++ (Prompt-Aware Counting++), a novel test suite featuring two dedicated evaluation protocols -- the negative-label test and the distractor test -- paired with new specialized metrics; and (ii) we present the MUCCA (MUlti-Category Class-Agnostic counting) evaluation dataset, a new collection of real-world images featuring multiple annotated object categories per scene, unlike existing CAC benchmarks that typically include a single category per image. Our extensive experimental evaluation of 10 state-of-the-art methods shows that, despite strong performance under standard counting metrics, current models exhibit significant weaknesses in understanding and grounding object class descriptions. Finally, we provide a quantitative analysis of how semantic similarity between prompts influences these failures. Overall, our results underscore the need for more semantically grounded architectures and offer a reliable framework for future assessment in open-world text-guided CAC methods.

---


### 481. [Seeing Realism from Simulation: Efficient Video Transfer for Vision-Language-Action Data Augmentation](https://arxiv.org/abs/2605.02757)

**<font color=#1a73e8>作者：</font>** Chenyu Hui, Xiaodi Huang, Siyu Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models typically rely on large-scale real-world videos, whereas simulated data, despite being inexpensive and highly parallelizable to collect, often suffers from a substantial visual domain gap and limited environmental diversity, resulting in weak real-world generalization. We present an efficient video augmentation framework that converts simulated VLA videos into realistic training videos while preserving task semantics and action trajectories. Our pipeline extracts structured conditions from simulation via video semantic segmentation and video captioning, rewrites captions to diversify environments, and uses a conditional video transfer model to synthesize realistic videos. To make augmentation practical at scale, we introduce a diffusion feature-reuse mechanism that reuses video tokens across adjacent timesteps to accelerate generation, and a coreset sampling strategy that identifies a compact, non-redundant subset for augmentation under limited computation. Extensive experiments on Robotwin 2.0, LIBERO, LIBERO-Plus, and a real robotic platform demonstrate consistent improvements. For example, our method improves RDT-1B by 8% on Robotwin 2.0, and boosts $\pi_0$ by 5.1% on the more challenging LIBERO-Plus benchmark. Code is available at: this https URL.

---


### 482. [Unified Map Prior Encoder for Mapping and Planning](https://arxiv.org/abs/2605.02762)

**<font color=#1a73e8>作者：</font>** Zongzheng Zhang, Sizhe Zou, Guantian Zheng 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online mapping and end-to-end (E2E) planning in autonomous driving remain largely sensor-centric, leaving rich map priors, including HD/SD vector maps, rasterized SD maps, and satellite imagery, underused because of heterogeneity, pose drift, and inconsistent availability at test time. We present UMPE, a Unified Map Prior Encoder that can ingest any subset of four priors and fuse them with BEV features for both mapping and planning. UMPE has two branches. The vector encoder pre-aligns HD/SD polylines with a frame-wise SE(2) correction, encodes points via multi-frequency sinusoidal features, and produces polyline tokens with confidence scores. BEV queries then apply cross-attention with confidence bias, followed by normalized channel-wise gating to avoid length imbalance and softly down-weight uncertain sources. The raster encoder shares a ResNet-18 backbone conditioned by FiLM with scaling and shift at every stage, performs SE(2) micro-alignment, and injects priors through zero-initialized residual fusion, so the network starts from a do-no-harm baseline and learns to add only useful prior evidence. A vector-then-raster fusion order reflects the inductive bias of geometry first, appearance second. On nuScenes mapping, UMPE lifts MapTRv2 from 61.5 to 67.4 mAP (+5.9) and MapQR from 66.4 to 71.7 mAP (+5.3). On Argoverse2, UMPE adds +4.1 mAP over strong baselines. UMPE is compositional: when trained with all priors, it outperforms single-prior models even when only one prior is available at test time, demonstrating powerset robustness. For E2E planning with the VAD backbone on nuScenes, UMPE reduces trajectory error from 0.72 to 0.42 m L2 on average (-0.30 m) and collision rate from 0.22% to 0.12% (-0.10%), surpassing recent prior-injection methods. These results show that a unified, alignment-aware treatment of heterogeneous map priors yields better mapping and better planning.

---


### 483. [FoR-Net: Learning to Focus on Hard Regions for Efficient Semantic Segmentation](https://arxiv.org/abs/2605.02764)

**<font color=#1a73e8>作者：</font>** Hsin-Jui Pan, Sheng-Wei Chan, Meng-Qian Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present FoR-Net, a lightweight architecture for semantic segmentation that focuses on identifying and enhancing hard regions. Instead of relying on heavy global modeling, FoR-Net adopts an efficient strategy that selectively emphasizes informative regions through a learned importance map and a Top-K activation mechanism. Specifically, a selector module predicts region-wise importance, enabling the model to focus on challenging areas such as thin structures and object boundaries. Multi-scale reasoning is achieved using convolutional branches with different receptive fields, allowing diverse spatial context aggregation. We evaluate FoR-Net on the Cityscapes benchmark under limited computational resources. Despite its lightweight design and standard training configuration, FoR-Net achieves competitive performance and demonstrates improved consistency in challenging regions. These results suggest that region-focused reasoning provides a simple yet effective inductive bias for efficient semantic segmentation.

---


### 484. [TOC-SR: Task-Optimal Compact diffusion for Image Super Resolution](https://arxiv.org/abs/2605.02767)

**<font color=#1a73e8>作者：</font>** Sowmya Vajrala, Akshay Bankar, Manjunath Arveti 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have recently demonstrated strong performance for image restoration tasks, including super-resolution. However, their large model size and iterative sampling procedures make them computationally expensive for practical deployment. In this work, we present TOC-SR, a framework for building efficient one-step super-resolution models by first discovering a compact diffusion backbone. Starting from a sixteen-channel latent diffusion model, we construct parameter-efficient surrogate blocks using feature-wise generative distillation and perform architecture discovery using epsilon-constrained Bayesian Optimization to minimize model complexity while preserving generative fidelity. The resulting compact diffusion backbone achieves a 6.6x reduction in parameters and a 2.8x reduction in GMACs compared to the expanded diffusion model. We then adapt this backbone for super-resolution and distill the diffusion process into a single-step generator. Experiments demonstrate that the proposed approach enables efficient super-resolution while maintaining strong reconstruction quality.

---


### 485. [Linearizing Vision Transformer with Test-Time Training](https://arxiv.org/abs/2605.02772)

**<font color=#1a73e8>作者：</font>** Yining Li, Dongchen Han, Zeyu Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While linear-complexity attention mechanisms offer a promising alternative to Softmax attention for overcoming the quadratic bottleneck, training such models from scratch remains prohibitively expensive. Inheriting weights from pretrained Transformers provides an appealing shortcut, yet the fundamental representational gap between Softmax and linear attention prevents effective weight transfer. In this work, we address this conversion challenge from two perspectives: architectural alignment and representational alignment. We identify Test-Time Training (TTT) as a linear-complexity architecture whose two-layer dynamic formulation is structurally aligned with Softmax attention, enabling direct inheritance of pretrained attention weights. To further align representational properties, including key shift-invariance and locality, we introduce key instance normalization and a lightweight locality enhancement module. We validate our approach by linearizing Stable Diffusion 3.5 and introduce SD3.5-T$^5$ (Transformer To Test Time Training). With only 1 hour of fine-tuning on 4$\times$H20 GPUs, SD3.5-T$^5$ achieves comparable text-to-image quality to the fine-tuned Softmax model, while accelerating inference by 1.32$\times$ and 1.47$\times$ at 1K and 2K resolutions.

---


### 486. [A decoupled diffusion planner that adapts to changing cost limits by using cost-conditioned generation for safety and reward gradients for performance](https://arxiv.org/abs/2605.02777)

**<font color=#1a73e8>作者：</font>** Rufeng Chen, Zhaofan Zhang, Zhejiang Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline safe reinforcement learning often requires policies to adapt at deployment time to safety budgets that vary across episodes or change within a single episode. While diffusion-based planners enable flexible trajectory generation, existing guidance schemes often treat reward improvement and constraint satisfaction as competing gradient objectives, which can lead to unreliable safety compliance under cost limits. We reinterpret adaptive safe trajectory generation as sampling from a constrained trajectory distribution, where the budget restricts the trajectory region, and reward shapes preferences within that region. This perspective motivates Safe Decoupled Guidance Diffusion (SDGD), which conditions classifier-free guidance on the cost limit to bias sampling toward trajectories satisfying the specified limit, while using reward-gradient guidance to refine trajectories for higher return. Because direct reward guidance can increase return while also steering samples toward trajectories with higher cumulative cost, we introduce Feasible Trajectory Relabeling (FTR) to reshape reward targets and discourage such directions. We further provide a first-order sampling-time analysis showing that FTR suppresses reward-induced cost drift under a prefix-restorative alignment condition. Extensive evaluations on the DSRL benchmark show that SDGD achieves the strongest safety compliance among baselines, satisfying the constraint on 94.7% of tasks (36/38), while obtaining the highest reward among safe methods on 21 tasks.

---


### 487. [Fine-Grained Graph Generation through Latent Mixture Scheduling](https://arxiv.org/abs/2605.02780)

**<font color=#1a73e8>作者：</font>** Nidhi Vakil, Hadi Amiri  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Structure aware graph generation aims to generate graphs that satisfy given topological properties. It has applications in domains such as drug discovery, social network modeling, and knowledge graph construction. Unlike existing methods that only provide coarse control over graph properties, we introduce a novel conditional variational autoencoder for fine-grained structural control in graph generation. The approach refines the decoder's latent space by dynamically aligning graph- and property-driven representations to improve both graph fidelity and control satisfaction. Specifically, the approach implements a mixture scheduler that progressively integrates graph and control priors. Experiments on five real-world datasets show the efficacy of the proposed model compared to recent baselines, achieving high generation quality while maintaining high controllability.

---


### 488. [HumanSplatHMR: Closing the Loop Between Human Mesh Recovery and Gaussian Splatting Avatar](https://arxiv.org/abs/2605.02784)

**<font color=#1a73e8>作者：</font>** Yeheng Zong, Pou-Chun Kung, Yike Pan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurately recovering human pose and appearance from video is an essential component of scene reconstruction, with applications to motion capture, motion prediction, virtual reality, and digital twinning. Despite significant interest in building realistic human avatars from video, this paper demonstrates that existing methods do not accurately recover the 3D geometry of humans. ViT-based approaches are not consistently reliable and can overfit to 2D views, while NeRF- and Gaussian Splatting-based avatars treat pose and appearance separately, limiting rendering generalization to new poses. To resolve these shortcomings, this paper proposes HumanSplatHMR, a joint optimization framework that refines 3D human poses while simultaneously learning a high-fidelity avatar for novel-view and novel-pose synthesis. Our key insight is to close the loop between geometric pose estimation and differentiable rendering. Unlike prior human avatar methods that rely on accurate human pose obtained through motion capture systems or offline refinement, which are impractical in in-the-wild scenarios, our approach uses only human mesh estimates from a state-of-the-art human pose estimator to better reflect real-world conditions. Therefore, instead of using the human pose only as a deformation prior, HumanSplatHMR backpropagates photometric, segmentation, and depth losses through a differentiable renderer to the pose parameters and global position. This coupling refines the global 3D pose over time, improving accuracy and alignment while producing better renderings from novel views. Experiments show consistent improvements over pose recovery baselines that omit image-level refinement and avatar baselines that decouple pose estimation from avatar reconstruction.

---


### 489. [Edge-Efficient Image Restoration: Transformer Distillation into State-Space Models](https://arxiv.org/abs/2605.02794)

**<font color=#1a73e8>作者：</font>** Srinivas Soumitri Miriyala, Sowmya Vajrala, Sravanth Kodavanti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a modular framework for hybrid image restoration that integrates transformer and state-space model (SSM) blocks with a focus on improving runtime efficiency on edge hardware. While transformers provide strong global modeling through self-attention, their attention kernels incur substantial latency on mobile devices, especially for high-resolution inputs. In contrast, SSMs such as Mamba offer lineartime sequence modeling with lower runtime overhead but may underperform on fine grained restoration tasks. To balance accuracy and efficiency, we train lightweight SSM blocks as feature-distilled surrogates of transformer blocks and use them to construct hybrid U-Net-style architectures. To automatically discover effective block combinations, we introduce Efficient Network Search (ENS), a multi-objective search strategy that selects task-specific hybrid configurations from pre-aligned components. ENS optimizes restoration quality while penalizing transformer usage, serving as a lightweight proxy for latency and enabling architecture discovery without repeated hardware profiling. On a Snapdragon 8 Elite CPU, the Restormer baseline requires 10119.52 ms for inference. In contrast, ENS-discovered hybrids significantly reduce runtime: ENS-Deblurring runs in 2973 ms (3.4x faster), ENS-Deraining in 5816 ms (1.74x faster), and ENS-Denoising in 8666 ms (1.17x faster), while maintaining competitive restoration quality.

---


### 490. [Analyzing Unsolicited Internet Traffic: Measuring IoT Security Threats via Network Telescopes](https://arxiv.org/abs/2605.02795)

**<font color=#1a73e8>作者：</font>** Shereen Ismail, Taelyn Dyer, Raul Martinez 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Network telescopes serve as a critical passive monitoring tool for capturing unsolicited Internet traffic, providing insights into global scanning and reconnaissance behavior. This study analyzes a 10-day dataset during January 2025 consisting of approximately 22 million packets collected by the ORION network telescope at Merit Network. By employing privacy-preserving metadata analysis and lightweight behavioral heuristics, we identify scanning and backscatter patterns without payload inspection. Our results reveal a highly structured and centralized ecosystem, where the top 1% of source IP addresses generate over 81% of total traffic. A significant finding is the dominance of Port 23 (Telnet) and Port 2323 (Telnet Alt), which highlights the persistent nature of IoT security threats and widespread attempts to exploit weak credentials in legacy IoT devices. Furthermore, synchronized surges in packet volume and Shannon entropy indicate coordinated, multi-vector reconnaissance campaigns. These findings offer a practical framework for identifying large-scale threat activity and support cybersecurity research and education.

---


### 491. [Exploring Instant Photography using Generative AI: A Design Probe with the UnReality Camera](https://arxiv.org/abs/2605.02805)

**<font color=#1a73e8>作者：</font>** Michael Yin, Angela Chiang, Robert Xiao  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI has increasingly been used for artistic creation, but little work has explored how it shapes the experiential meaning of practice. We consider how generative AI might transform the embodied and tangible process of instant photography through the UnReality Camera, an AI-mediated instant camera. The UnReality Camera prints a photo of the environment augmented by a user's spoken words as generative input. In a design probe, we explored how generative AI shapes people's perceptions of both photographic output and the broader photographic process. Although users valued artistic control, they also appreciated the creativity afforded by stochastic unpredictability. The waiting period for an unpredictable output elicited anticipatory suspense, and the camera's physical form evoked ownership and connection despite artificial generation. We discuss how people make sense of instant photography's experiential qualities when generative AI is embedded, and how their opposing affordances reshape interpretations of each other's experiential meaning.

---


### 492. [AIs and Humans with Agency](https://arxiv.org/abs/2605.02810)

**<font color=#1a73e8>作者：</font>** David Mumford  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper compares agency in humans with potential agency in AI programs. Human agency takes many years to develop, as the frontal lobe is activated. Early attempts to endow LLMs agency have met serious obstacles. Progress requires a new architecture where actions and plans are formulated jointly with the human actors in each real world setting.

---


### 493. [IConFace: Identity-Structure Asymmetric Conditioning for Unified Reference-Aware Face Restoration](https://arxiv.org/abs/2605.02814)

**<font color=#1a73e8>作者：</font>** Axi Niu, Jinyang Zhang, Senyan Qing  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Blind face restoration is highly ill-posed under severe degradation, where identity-critical details may be missing from the degraded input. Same-identity references reduce this ambiguity, but mismatched pose, expression, illumination, age, makeup, or local facial states can lead to overuse of reference appearance. We propose \textbf{IConFace}, a unified reference-aware and no-reference framework with identity--structure asymmetric conditioning. References are distilled into a norm-weighted global AdaFace identity anchor for image-only modulation, while the degraded image is reinforced as the spatial structure anchor through low-rank residuals and block-wise degraded cross-attention with two-route memory. The resulting single checkpoint exploits references when available and falls back to no-reference restoration when absent, improving identity consistency, fine-detail recovery, and degraded-only restoration quality in a unified model.

---


### 494. [FlexSQL: Flexible Exploration and Execution Make Better Text-to-SQL Agents](https://arxiv.org/abs/2605.02815)

**<font color=#1a73e8>作者：</font>** Quang Hieu Pham, Yang He, Ping Nie 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-to-SQL over large analytical databases requires navigating complex schemas, resolving ambiguous queries, and grounding decisions in actual data. Most current systems follow a fixed pipeline where schema elements are retrieved once upfront and the database is only revisited for post-hoc repair, limiting recovery from early mistakes. We present FlexSQL, a text-to-SQL agent whose core design principle is flexible database interaction: the agent can explore schema structure, inspect data values, and run verification queries at any point during reasoning. FlexSQL generates diverse execution plans to cover multiple query interpretations, implements each plan in either SQL or Python depending on the task, and uses a two-tiered repair mechanism that can backtrack from code-level errors to plan-level revisions. On Spider2-Snow, using gpt-oss-120b, FlexSQL achieves a 65.4\% score, outperforming strong open-source baselines that use stronger, larger models such as gpt-o3 and DeepSeek-R1. When integrated into a general-purpose coding agent (as skills in Claude Code), our approach yields over 10\% relative improvement on Spider2-Snow. Further analysis shows that flexible exploration and flexible execution jointly contribute to the effectiveness of our approach, highlighting flexibility as a key design principle. Our code is available at: this https URL

---


### 495. [SCPRM: A Schema-aware Cumulative Process Reward Model for Knowledge Graph Question Answering](https://arxiv.org/abs/2605.02819)

**<font color=#1a73e8>作者：</font>** Jiujiu Chen, Yazheng Liu, Sihong Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models excel at complex reasoning, yet evaluating their intermediate steps remains challenging. Although process reward models provide step-wise supervision, they often suffer from a risk compensation effect, where incorrect steps are offset by later correct ones, assigning high rewards to flawed reasoning paths. This issue is further exacerbated in knowledge graph (KG) reasoning, as there may exist multiple paths between the start and end entities in the KGs, and a risky step can make the reasoning path flawed. Those limitations are problematic in risk-sensitive tasks such as medical and legal KG reasoning. To address the issues, we propose a Schema-aware Cumulative Process Reward Model (SCPRM) that evaluates reasoning paths by conditioning on the reasoning prefix , and incorporating schema distance between current reasoning step and the implicit target parsed from the query, which provides cumulative and future rewards to guide the path explorations. We further integrate SCPRM into Monte Carlo Tree Search (MCTS) as SCPRM-MCTS to conduct multi-hop reasoning on KGs for question answering (QA) tasks. Across medical and legal KGQA and CWQ, SCPRM-MCTS improves the performance of Hits@k by an average of 1.18% over strong baselines, demonstrating more accurate and risk-sensitive reasoning evaluation.

---


### 496. [InsureConnect: Blockchain and Digital Identity for the Property Insurance Market](https://arxiv.org/abs/2605.02824)

**<font color=#1a73e8>作者：</font>** João Eduardo Travassos, Miguel Correia  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper presents InsureConnect, a blockchain-based system for improving transparency, authentication, and auditability in property-insurance workflows after natural disasters. The system combines Self-Sovereign Identity (SSI), Decentralized Identifiers (DIDs), Verifiable Credentials (VCs), satellite imagery, Hyperledger Fabric, and IPFS to register identities, insurance contracts, and damage claims. Property images are stored off-chain in IPFS, while content hashes and signed records are maintained on a permissioned blockchain. Users interact with the system through a desktop application, while chaincode enforces role-based access control and validates digital signatures. The prototype was evaluated under concurrent request loads from 50 to 3000 requests, measuring latency, throughput, and dropped connections. The results indicate that the system sustains increasing throughput under load, although latency rises and dropped connections appear at higher concurrency levels.

---


### 497. [First-Order Efficiency for Probabilistic Value Estimation via A Statistical Viewpoint](https://arxiv.org/abs/2605.02827)

**<font color=#1a73e8>作者：</font>** Ziqi Liu, Kiljae Lee, Yuan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Probabilistic values, including Shapley values and semivalues, provide a model-agnostic framework to attribute the behavior of a black-box model to data points or features, with a wide range of applications including explainable artificial intelligence and data valuation. However, their exact computation requires utility evaluations over exponentially many coalitions, making Monte Carlo approximation essential in modern machine learning applications. Existing estimators are often developed through different identification strategies, including weighted averages, self-normalized weighting, regression adjustment, and weighted least squares. Our key observation is that these seemingly distinct constructions share a common first-order error structure, in which the leading term is an augmented inverse-probability weighted influence term determined by the sampling law and a working surrogate function. This first-order representation yields an explicit expression for the leading mean squared error (MSE), which characterizes how the sampling law and the surrogate jointly determine statistical efficiency. Guided by this criterion, we propose an Efficiency-Aware Surrogate-adjusted Estimator (EASE) that directly chooses the sampling law and surrogate to minimize the first-order MSE. We demonstrate that EASE consistently outperforms state-of-the-art estimators for various probabilistic values.

---


### 498. [HAAS: A Policy-Aware Framework for Adaptive Task Allocation Between Humans and Artificial Intelligence Systems](https://arxiv.org/abs/2605.02832)

**<font color=#1a73e8>作者：</font>** Vicente Pelechanoa, Antoni Mestre, Manoli Albert 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deciding how to distribute work between humans and AI systems is a central challenge in organisational design. Most approaches treat this as a binary choice, yet the operational reality is richer: humans and AI routinely share tasks or take complementary roles depending on context, fatigue, and the stakes involved. Governing that distribution -- balancing efficiency, oversight, and human capability -- remains an open problem. This paper presents Human-AI Adaptive Symbiosis (HAAS), an implemented framework for adaptive task allocation in software engineering and manufacturing. HAAS combines two coupled components: a rule-based expert system that enforces governance constraints before any learning occurs, and a contextual-bandit learner that selects among feasible collaboration modes from outcome feedback. Task-agent fit is represented through five auditable cognitive dimensions and a five-mode autonomy spectrum -- from human-only to fully autonomous -- embedded in a reproducible benchmark spanning both domains. Three empirical findings emerge. First, governance is not a binary switch but a tunable design variable: tighter constraints predictably convert autonomous AI assignments into supervised collaborations, with domain-specific costs and benefits. Second, in manufacturing, stronger governance can improve operational performance and reduce fatigue simultaneously -- a workload-buffering effect that contradicts the usual framing of governance as pure overhead. Third, no single governance setting dominates across all contexts; moderate governance becomes increasingly competitive as the learner accumulates experience within the governed action space. Together, these findings position HAAS as a pre-deployment workbench for comparing and inspecting human--AI allocation policies before organisational commitment.

---


### 499. [A Closed-Form Persistence-Landmark Pipeline for Certified Point-Cloud and Graph Classification](https://arxiv.org/abs/2605.02836)

**<font color=#1a73e8>作者：</font>** Sushovan Majhi, Atish Mitra, Žiga Virk 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce PLACE (Persistence-Landmark Analytic Classification Engine), a closed-form pipeline for classifying point clouds and graphs through their persistent-homology signatures. Three quantitative guarantees -- a margin-based excess-risk rate, a closed-form descriptor-selection rule, and a per-prediction certificate -- are derived from training labels alone, with no learned weights or held-out calibration. The embedding sums Mitra-Virk single-point coordinate functions over a sparse landmark grid; closed-form weights maximize a structural distortion constant $\lambda(\nu)$ (a Lipschitz lower bound on $\mathcal{D}_n$ under non-interference). (i) An $O(kR/(\Delta\sqrt{m_{\min}}))$ margin bound, driven by class-mean separation $\Delta$ and embedding radius $R$, matched by a sample-starved minimax lower bound. (ii) The Mahalanobis margin under Ledoit-Wolf-shrunk covariance is the strongest closed-form descriptor selector on a heterogeneous 64-descriptor chemical-graph pool (mean Spearman $\rho \approx +0.54$ across 10 benchmarks, positive on 9 of 10); the isotropic surrogate $\Delta/\sqrt\ell$ admits a closed-form selection-consistency rate on homogeneous (14-15 descriptor) protein/social pools. (iii) A training-time-decided certificate with no per-prediction overhead, in non-asymptotic Pinelis and asymptotic Gaussian plug-in forms. Empirically, PLACE is the strongest diagram-based method on Orbit5k and matches the strongest topology-based baseline within statistical noise on MUTAG and COX2. The remaining gaps fall into two diagnosable regimes: descriptor blindness on NCI1/NCI109, and pool-coverage limits elsewhere. Both radii exceed the firing threshold $\hat\Delta/2$ on every benchmark at our training-set sizes, dominated by the $\sqrt\ell$ scaling of the multivariate-norm bound; the per-prediction certificate is constructive but not yet operational at these sizes.

---


### 500. [TRACE: Temporal Reasoning over Context and Evidence for Activity Recognition in Smart Homes](https://arxiv.org/abs/2605.02841)

**<font color=#1a73e8>作者：</font>** Yingtian Shi, Abivishaq Balasubramanian, Jessica Herring 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human activity recognition (HAR) in smart homes remains challenging because many daily activities exhibit similar local sensor patterns, while minimally intrusive sensing provides sparse and ambiguous observations. As a result, methods based on short temporal or event windows often fail to capture the broader temporal and behavioral context needed for reliable activity understanding. We present TRACE (Temporal Reasoning over Context and Evidence), a contextual activity recognition framework for smart homes that integrates multi-source sensor evidence with user-specific contextual priors to improve activity interpretation. Rather than treating recognition as a local classification problem, TRACE leverages contextual reasoning to resolve ambiguities, reduce fragmented predictions, and infer more semantically specific activities. We evaluate TRACE on public benchmarks and in a deployment study conducted in our smart-home environment. Results show that TRACE improves recognition accuracy for semantically complex activities, produces more temporally coherent predictions that better align with user-specific routines, and maintains robust performance under cross-domain transfer and missing-modality conditions. These findings demonstrate the value of contextual reasoning for advancing smart-home HAR.

---


> [!TIP]
> 当前位于：**451-500**（第 10/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-511](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
