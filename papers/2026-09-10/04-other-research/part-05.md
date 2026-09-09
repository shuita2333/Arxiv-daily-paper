# 📦 其他研究 | 2026年09月10日

> 本类共 **542** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-542](./part-11.md)

---

### 201. [The Interface of Theseus: The Rise of Just-In-Time Interfaces](https://arxiv.org/abs/2609.06770)

**<font color=#1a73e8>作者：</font>** Michael S. Bernstein  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Our community creates interfaces---pre-constructed, static artifacts. These interfaces are effortful to create, so we invest great effort and care into each of them. Yet the equilibrium is shifting: we can now construct nearly any software, bespoke, within moments. When construction is cheap, we may soon live in a future in which interfaces are constructed in real time. This is a world of just-in-time interfaces: rapid, discardable, on-demand interfaces tailored to our needs in the moment. Will our community still create traditional interactive systems in this world? Or will we create interface generators, ``this http URL'' guides for AI consumption? I argue that we ought to lean into a future of rapid, bespoke, on-demand interfaces.

---


### 202. [AuthBench: A Large-Scale Multilingual Benchmark for Authorship Representation across Genres and Lengths](https://arxiv.org/abs/2609.06771)

**<font color=#1a73e8>作者：</font>** MaoXun Huang, Zhenxing Zhang, Claire Cardie  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Authorship signals matter in settings where writing style carries identity: digital forensics, plagiarism analysis, account linking, misinformation investigation, and machine-generated text detection. Yet current authorship benchmarks remain fragmented, usually covering only a narrow language set, a single genre, or a limited document-length regime, which makes it difficult to assess whether modern representations truly generalize. We introduce AuthBench, a large-scale multilingual benchmark for authorship representation that is designed to make this evaluation broad, standardized, and realistic. AuthBench contains 428,150 documents written by 153,825 individuals across ten widely used languages, 9 primary genres, 66 fine-grained genres, and four document-length buckets. It supports two complementary tasks: authorship attribution, formulated as same-author retrieval and authorship verification, formulated as same-author binary decision. We benchmark 47 neural models and three non-neural baselines under a unified zero-shot protocol. Results show that authorship representation remains far from solved: the best retrieval model reaches only 0.258 Success@5, while the best verification model achieves 0.076 EER and 0.968 ROC-AUC. The leaderboard also reveals a meaningful task split, with different model families leading retrieval and verification, and large performance differences across languages, genres, and lengths.
These findings position AuthBench not only as a new benchmark, but as a diagnostic resource for studying when and why authorship representations succeed or fail. We release AuthBench, its evaluation toolkit, and benchmark data at this https URL and this https URL.

---


### 203. [Robustness-Aware Evaluation and Enhancement of Mutation-Based Fuzzing for Bug Discovery](https://arxiv.org/abs/2609.06773)

**<font color=#1a73e8>作者：</font>** Zirui Liu, Mengfan Xu, Juan Zhai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mutation-based fuzzing is widely used to discover software vulnerabilities, but its randomness complicates rigorous evaluation and reliable bug detection. Prior work measures this variability empirically but lacks a theory with computable convergence and sample-complexity guarantees. We address both problems. First, we estimate robustness from independent campaigns by measuring variation in bug-trigger rates after accounting for compute. For $M$ campaigns of length $T$, finite-trial error decreases at the standard $M^{-1/2}$ rate, while finite-length error is bounded when temporal bug correlations decay. We then introduce splitting, a black-box wrapper that copies a fuzzer's queue state after a bug trigger and continues from that state in multiple branches, directing more effort toward the discovered region. For any realized split tree, branching cannot reduce the raw number of bug-triggering events relative to a single continuation path. Expected detection also improves when states receiving more branches tend to yield more bugs later. In a simplified model, splitting reduces variance per unit compute when $p<\sqrt{2}-1$, where $p$ is the fraction of time spent in the bug region. At matched compute, splitting finds more real bugs per CPU-hour than the baseline in 38 of 40 Magma ground-truth cells (median +52\%; 34 of 38 individually significant) and never finds fewer distinct bugs. It changes CVE-2019-19926 from undetected (0/20 trials) to reliably detected (20/20; Fisher $p<10^{-4}$), with six additional detection improvements, five involving CVEs. On FuzzBench, splitting finds more unique bugs in 53 of 70 pairs and reduces cross-campaign variation in 66 of 70, with a median reduction of about $10\times$. Every branch counts toward the compute budget. With about 0.14\% overhead, splitting provides a practical way to measure and improve fuzzers.

---


### 204. [Unified Multi-Layer Subspace Modeling for Cross-Domain OOD Detection](https://arxiv.org/abs/2609.06785)

**<font color=#1a73e8>作者：</font>** Gerhard Krumpl, Henning Avenhaus, Horst Possegger  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Out-of-Distribution (OOD) detection remains a fundamental challenge for neural networks, whose predictions can be overconfident on inputs that deviate from the training distribution. Most post-hoc OOD detection methods derive scores from a single representation level (eg., logits or penultimate features) or combine multiple layers via depth selection or OOD-calibrated weighting. However, because OOD shifts are diverse, the most informative representation level can vary strongly across OOD types and domains, making fixed-layer choices and OOD-calibrated aggregation brittle. In this paper, we propose PRISM (Projected Representation with Intermediate-layer Subspace Modeling), a model-agnostic post-hoc OOD detection method that models a unified multi-layer feature representation rather than aggregating independently scored layers. PRISM fuses intermediate and deep features into a single hierarchical embedding, estimates an in-distribution (ID) principal subspace, and then combines two complementary signals: (i) a class-conditional Mahalanobis distance in the projected subspace and (ii) the residual energy orthogonal to the learned manifold. This simple design avoids OOD-tuned layer weighting while capturing both in-subspace semantic deviations and off-subspace anomalies. Across diverse benchmarks spanning natural images, medical imaging, and industrial visual inspection, PRISM achieves consistent state-of-the-art cross-domain OOD detection performance with a single default configuration across all evaluated domains and architectures. We further show that PRISM incurs minimal inference overhead, making it practical for real-world deployment.

---


### 205. [When Speech Meets Lips: Interpretable Audio-Visual Synchronization for L2 Pronunciation Assessment](https://arxiv.org/abs/2609.06788)

**<font color=#1a73e8>作者：</font>** Bowen Yu, Mingyu Huang, Yishen Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic Pronunciation Assessment (APA) systems have achieved strong performance with transformer-based models and self-supervised speech representations. However, most methods rely only on acoustic signals and overlook temporal synchronization between speech and articulatory movements, limiting diagnostic feedback on timing mismatches important for L2 pronunciation training. We propose an interpretable audio-visual synchronization framework that explicitly models speech-lip temporal alignment through feature encoding, cross-attention fusion, lag estimation, stability quantification, and visualization. The framework introduces frame-level lag trajectories and a Lag Stability Index (LSI) to quantify synchronization robustness. We also interviewed 30 participants, including 10 instructors and 20 students with diverse first-language backgrounds, to assess its effectiveness. By transforming implicit alignment into interpretable representations, the framework connects automatic scoring with actionable Computer-Aided Pronunciation Training feedback. Datasets and supplemental materials are available at this https URL.

---


### 206. [Efficient Hardware Information-Flow Tracking for Pre-Silicon Security Testing](https://arxiv.org/abs/2609.06791)

**<font color=#1a73e8>作者：</font>** Yu-Wei Fan, Yuheng Yang, Christine Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Register-Transfer Level (RTL) simulation is widely used to test hardware before it is fabricated. To allow testing for security related information flow properties, such as confidentiality and integrity, taint logic can be automatically added to the design to track how information flows through it. However, taint logic instrumented by the state-of-the-art, such as CellIFT, makes simulation-based testing prohibitively expensive: On our evaluation of Mega-BOOM (136K cells), it increases the instrumented design to 5.81x the original cell count and causes a 143.72x simulation slowdown. The taint logic could be simplified to improve simulation speed, but it will inevitably trade off its precision. This lightweight, imprecise taint logic will introduce false positives and may eventually result in even more overhead to check these false positives. This paper explores the research question of where precision is actually needed in the design to overcome the overhead of false positives. It presents CEGAR-T, a framework that automatically synthesizes taint logic that minimizes the taint-logic instrumentation overhead while guaranteeing no false positives (relative to the precise CellIFT baseline). We have implemented CEGAR-T and evaluated it on the safe instruction set problem for timing side-channel security across open-source RISC-V cores. Over all evaluated cores, CEGAR-T reduces both instrumentation and simulation overhead, in geometric-mean, from 5.64x to 1.42x and from 34.65x to 1.79x, respectively, without compromising the precision benefit of the CellIFT baseline.

---


### 207. [Train Smarter, Not Harder: Switching Signal-Guided Training in Active Learning](https://arxiv.org/abs/2609.06806)

**<font color=#1a73e8>作者：</font>** Nagham Omar, Maya Rozenshtein, Evgeny Mishlyakov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training strategy, namely whether to retrain from scratch or fine-tune from the previous checkpoint, is an overlooked decision variable in active learning. We show that this choice has exploitable structure: retraining is most useful in early rounds, when each batch can substantially reshape the labeled distribution, while fine-tuning becomes safer once the model trajectory stabilizes. We propose HybridAL, an adaptive training schedule that monitors an online stabilization signal and switches from retraining to fine-tuning after sustained stabilization. Two complementary signals, spectral exponent change $\Delta\alpha$ (weight-based) and accuracy change $\Delta$Acc (validation-based), span different points on the time-calibration trade-off. Across three encoder backbones and six text-classification tasks (five seeds each), HybridAL keeps endpoint macro-F1 non-inferior to retraining and fine-tuning at a 0.010 margin, saves up to 49% of retraining time, and recovers a substantial fraction of retraining's calibration advantage as measured by negative log-likelihood (NLL). Compared with schedules that switch at a pre-committed round, HybridAL obtains lower NLL at moderate additional cost, showing that trajectory-dependent switching provides a stronger time-calibration trade-off than fixed early switching.

---


### 208. [Comparative Study of Anatomical and Learned Features in AI Models for Structural Brain MRI](https://arxiv.org/abs/2609.06807)

**<font color=#1a73e8>作者：</font>** Boyang Yu, Miquel Lopez Escoriza, Long Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we comprehensively evaluate three popular feature-extraction paradigms in AI-based neuroimaging modeling: (1) computation of anatomical surfaces and volumes, (2) supervised learning with convolutional neural networks (CNNs), and (3) unsupervised pretraining of vision transformer (ViT) foundation models, followed by supervised finetuning. Our study is based on 18 publicly available datasets containing 3D structural T1-weighted MRI scans from approximately 80,000 participants across seven distinct clinical tasks. We observe that a linear model based on anatomical features matches the diagnostic performance of complex nonlinear features learned by sophisticated AI frameworks, including foundation models trained on thousands of scans. Conversely, CNNs and pretrained ViTs learn features that implicitly capture relevant anatomical information, bypassing the need for explicit feature extraction. Building upon these insights, we propose Anatomy Segmentation Pretraining (ASP), a novel method to incorporate anatomical information during foundation-model pretraining, which outperforms existing models in biological age estimation.

---


### 209. [Disparity Has a Sign: Stereo Matching Beyond the Zero-Disparity Plane](https://arxiv.org/abs/2609.06809)

**<font color=#1a73e8>作者：</font>** Jian Shi, Xinge Yang, Chaoyang Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern stereo matching models fail when disparity crosses zero, with end-point error (EPE) rising by 4.6-37$\times$. Yet stereoscopic content, from cinema 3D to VR, routinely contains objects behind the zero-disparity plane (ZDP), corresponding to negative disparities. The blind spot cascades through datasets, architectures, and evaluation protocols, all of which inherit the non-negative geometry. Rectified parallel cameras place ZDP at infinity, so every finite depth yields $d=fB/z \ge 0$ by construction, and nothing within the standard pipeline can violate, or even measure, a negative disparity. To measure it, we propose \textit{ZDPShift}, a benchmark of $21{,}495$ stereo pairs from seven cinematographer-authored open movies, each frame rendered at five zero-disparity-plane positions with dense signed ground truth. Six state-of-the-art image and video stereo matching models collapse once the plane moves. On identical scene content, FoundationStereo goes from $2.24$ px EPE to $75.33$px, with every backbone leaving roughly half of all pixels exceeding a three-pixel disparity error. What is missing, however, is not the underlying matching capability. % The capability itself, however, is already present. Training on supervision synthesized from SceneFlow, which adds no new data or parameters, keeps the error flat across the signed range. Training only the decoder, with the pretrained matching features frozen, performs comparably across all six backbones, with EPE jittering within $0.2$px. Thus, the pretrained features already extend to the negative regime they were never trained on, and only the output convention discarded it. Meanwhile, positive-regime accuracy on KITTI, Middlebury, ETH3D, and Sintel is largely preserved.

---


### 210. [Unsound Search with Policy and Value Networks in Legends of Code and Magic](https://arxiv.org/abs/2609.06816)

**<font color=#1a73e8>作者：</font>** Dustin Rubin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decision-time search in perfect and imperfect information games with enumerable belief states are effective methods for game AI. Collectible card games are imperfect information games with large belief states. Legends of Code and Magic is a collectible card game competition where the belief states are $2^{101}$. The Legends of Code and Magic (LoCM) champion, ByteRL, plays with no search. Other works claim sound enumeration-based search is unusable in the genre due to the number of belief states. We measured three previously defined properties that predict where theoretically unsound perfect information Monte Carlo's defects are cheap and found LoCM sits in the favorable region. Starting with imitation learning of the runner-up policy, NeteaseOPD, we created a policy and value feed-forward network. Our agent searches over worlds sampled from a prior over the opponent's deck built from the runner-up's drafts. Using our strictest configuration in the battle phase we beat ByteRL with a win percentage of 51.35% 95% CI [50.37, 52.33], over 10,000 pre-registered games using the LoCM official referee and time limit. Search is not a minor factor on the matchup between our agent and ByteRL. Without search this agent scores 26.8% and adding search adds +24.6 points. Unsound search in imperfect information games could be exploitable. We replicate a published best-response attack against ByteRL. We then apply the same attack protocol to two search configurations of our agent, and each one resists it better than ByteRL at every iteration. In LoCM unsound search gives us a stronger and more resilient agent.

---


### 211. [Formation of structural attractors in neuromorphic systems](https://arxiv.org/abs/2609.06826)

**<font color=#1a73e8>作者：</font>** Yurii Parzhyn, Alexander Schwarzmann, Mykyta Lapin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper examines the theory of Invariant Structural Learning (ISL), which proposes a non-optimization approach to concept formation. Learning is interpreted as convergence to structural attractors in a hypergraph space, rather than as the minimization of a global loss function. The paper presents the ISL model, including its mathematical formalization, computational verification, and a hypothetical neurobiological interpretation. The mathematical section introduces the formal apparatus of the structural reduction process and proves its finite convergence, the existence and uniqueness of class structural attractors, and the self-organization of attractor maps. The computational section demonstrates the feasibility of the proposed approach on classical image recognition tasks, utilizing the proposed learning mechanism without backpropagation and with extremely small training datasets. Finally, the neurobiological section formulates hypotheses regarding the possible implementation of structural attractors in dendritic trees, neural coding as a projection of internal attractor dynamics, and the development of neural architectures supporting the proposed learning concept. These hypotheses are discussed in the context of modern experimental data in the fields of dendritic computations, synaptic plasticity, and the structural organization of neural circuits. The proposed neurobiological mechanisms are presented as testable hypotheses rather than established biological facts. The results demonstrate the mathematical consistency and computational feasibility of the proposed model, while the neurobiological hypotheses outline potential directions for its experimental verification.

---


### 212. [Constrained Bayesian Optimization for Hierarchical Federated Learning in IoT Networks for Plant Disease Classification](https://arxiv.org/abs/2609.06830)

**<font color=#1a73e8>作者：</font>** Athanasios Papanikolaou, Athanasios Tziouvaras, Apostolos Xenakis 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The deployment of Hierarchical Federated Learning (HFL) in resource-constrained Internet of Things (IoT) environments requires careful configuration to balance predictive performance with energy consumption and execution time. This challenge is particularly relevant to smart agriculture, where distributed IoT devices can support automated plant disease classification while operating under limited computational and communication resources. This paper presents a constrained Bayesian Optimization framework for the efficient configuration of HFL deployments. The proposed approach jointly explores the deep learning backbone architecture, aggregation strategy, and number of communication rounds, while the federation size is determined according to the spatial coverage requirements of the agricultural deployment. A weighted objective function captures user-defined trade-offs among energy consumption, execution time, and predictive performance, while explicit constraints ensure compliance with deployment-specific resource and accuracy requirements. The framework is evaluated on an IoT-based plant disease classification task considering multiple deep learning architectures, federated aggregation strategies, and communication-round settings. Experimental results across 30 independent optimization runs show that the proposed approach explores only 11.11% of the search space, while consistently identifying solutions within 1% of the exhaustive-search optimum, with a mean optimality gap of only 0.056%.

---


### 213. [Skynet: Workflow-Level Anomaly Detection for Agentic AI via Semantic and Structural Modeling](https://arxiv.org/abs/2609.06835)

**<font color=#1a73e8>作者：</font>** Chaoyu Zhang, Hexuan Yu, Heng Jin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems execute complex tasks through long-horizon workflows of planning, tool use, and multi-agent coordination. Task failures in these systems often originate from a single step, such as an injected prompt or a flawed plan, and are then amplified through downstream dependencies as the corrupted step propagates across many subsequent agents and tool calls. Existing defenses either target a specific class of attacks or failures, or inspect individual prompts and steps in isolation. Both leave the global dependency structure of a workflow unexamined, and miss the inconsistencies that only emerge when the execution is viewed as a whole. We argue that anomaly detection for agentic AI must reason at the workflow level, where global execution structure exposes signals that local checks cannot see. We present Skynet, a principled workflow-level anomaly detection framework that turns observed multi-agent execution into directed workflow graphs and scores them against learned benign behavior. Skynet jointly models the semantic execution context and the structural organization of inter-agent delegation, tool invocation, and data-flow dependencies, and trains only on benign workflows. Because training never sees attacks or failures, this design naturally extends to zero-day detection: any execution that violates benign workflow regularities surfaces as off-manifold geometry under a single decision rule. We evaluate Skynet on three public agentic safety and failure benchmarks. It sustains high recall together with a sub-1% false positive rate, with per-workflow and per-step latencies low enough for online monitoring of agentic AI runtimes.

---


### 214. [A Shared-Backbone Approach for Multi-Task MedMNIST Classification](https://arxiv.org/abs/2609.06838)

**<font color=#1a73e8>作者：</font>** Stefan-Dorian Gavril, Andrei Arhire, Adrian Iftene  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-task biomedical classification requires models to generalize across disparate modalities and class distributions. We study 11 heterogeneous MedMNIST datasets using the harmonic mean of per-task macro-F1. We evaluate three backbones with task-specific linear heads. We identify a resolution domain shift between the MedMNIST API and evaluation environment. Resolving this inconsistency and optimizing architecture-specific regularization substantially improved performance. Our best configuration, a ConvNeXt-Tiny backbone with label smoothing, achieved a leaderboard harmonic-mean macro-F1 of 0.73294 in the Tensor Reloaded: Multi-Task MedMNIST competition, ranking sixth at the close of the official competition phase. Our implementation is publicly available at: this https URL

---


### 215. [RAIDAL: Redundancy-Aware Information Density Active Learning for CTC-Based Continuous Sign Language Recognition](https://arxiv.org/abs/2609.06843)

**<font color=#1a73e8>作者：</font>** Rafael A. Diniz Augusto, Gabriel L. Oliveira, Erickson R. Nascimento  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continuous sign language recognition (CSLR) is a key technology for accessibility, yet its development remains limited by the high cost of annotating continuous video streams. Active learning offers a path toward mitigating this cost, but standard acquisition functions are not designed for weakly aligned sign language videos, where sign executions are interleaved with rest poses, irregular pauses, sign-like motion, and temporally redundant frames. This temporal redundancy can undermine sample selection, as acquisition scores may be influenced by timesteps from regions that are not associated with the decoded gloss sequence, distorting the video's estimated informativeness. In this work, we show that modern CSLR models already contain a mechanism for identifying gloss-level temporal evidence: the CTC decoder. Although typically used only during inference, its alignment peaks indicate where the model localizes each predicted gloss in the feature sequence, providing a source of temporal structure for active learning acquisition functions at zero additional labeling cost. Thus, we introduce RAIDAL (Redundancy-Aware Information Density Active Learning), which repurposes the CTC decoder to restrict representation-based scoring to decoder-aligned gloss regions, rather than exposing the acquisition function to the entire unfiltered video. Across three datasets and two architectures, RAIDAL achieves its strongest data-efficiency gains over competing baselines in large-vocabulary, budget-limited settings, while remaining competitive in the smaller-vocabulary, large-budget setting. The code used in this work is publicly available at this http URL.

---


### 216. [Learning transferable human physiology from two million hours of sleep with SleepFM-2](https://arxiv.org/abs/2609.06849)

**<font color=#1a73e8>作者：</font>** Rahul Thapa, Christopher Sun, William Theodor Lehn-Schioler 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sleep provides a nightly window into health by capturing coordinated activity across the brain, heart, muscles and respiratory system. We introduce SleepFM-2, a sleep foundation model developed and evaluated on 282,511 polysomnography recordings from 26 cohorts, including 235,865 used for pretraining. These data span more than two million hours of multimodal physiology. Compared with SleepFM, SleepFM-2 improves disease prediction and sleep scoring, supports arousal, limb movement and respiratory event detection, and transfers to wearable sensing and subjective sleep phenotypes. A model combining its PSG representation with age, sex and BMI met a prespecified discrimination and significance criterion for 215 subsequently recorded EHR phenotypes in two held-out cohorts, including one health system unseen during pretraining. For 155 phenotypes, the PSG representation added reproducible information beyond demographics. SleepFM-2 also outperformed a 480-feature baseline derived from the same recordings. Its disease scores revealed a reproducible principal component associated with reduced sigma-band spatial coupling and increased hypnodensity entropy. The frozen encoder performed within the observed range of expert scorers for sleep events and transferred to wakeful EEG, headband and in-ear EEG, wrist PPG and wrist accelerometry. It improved sleep staging across six accelerometry cohorts and achieved disease-prediction performance in UK Biobank similar to models pretrained directly on accelerometry. Finally, SleepFM-2 captured aspects of subjective sleep not recovered by conventional PSG summaries, particularly reports of the recorded night. These results show that multimodal sleep physiology can provide a transferable representation of human health across diseases, clinical tasks, sensors and subjective experience.

---


### 217. [You Are What You Read: Misalignment via In-Context Persona Induction](https://arxiv.org/abs/2609.06851)

**<font color=#1a73e8>作者：</font>** Kyuhee Kim, Benjamin Berczi, Cozmin Ududec  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Broad misalignment has been produced by finetuning on narrow data, harmful or benign, and in context only by demonstrations of the undesirable behaviour itself. We show that benign data suffices in context, with no finetuning and no demonstration of harmful behaviour in the prompt. Biographical facts that converge on a single figure, placed in a model's context as ordinary conversational turns, lead it to answer as that figure on questions the facts never touch. We call this persona induction. Across nine personas and thirteen models, identity adoption rises sigmoidally with the number of facts and crosses 50% within 3 to 10 of them. Misalignment then tracks which figure is described. Harmless personas reach full adoption with near-zero misalignment, while harmful ones voice their characteristic views on unrelated questions, at rates up to 80%. A formatting instruction can gate when the persona activates. Because each fact is individually benign, accumulated biographical context is flagged by content filters on 3% of inputs against 24-33% for an equivalent direct instruction.

---


### 218. [Feature Superposition in Neural Networks: From Theory to Practice](https://arxiv.org/abs/2609.06862)

**<font color=#1a73e8>作者：</font>** Dai Shi, Xiaoyu Li, Andi Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Superposition refers to neural networks representing more features than they have dimensions. It offers a possible explanation for polysemantic neurons and motivates methods for recovering interpretable features from neural activations. Theoretical models typically start with a given set of input features and assumptions about how their values vary across inputs, then study how a network encodes those values in a lower-dimensional hidden representation. Empirical work, by contrast, seeks to identify the features encoded in trained networks and determine their role in computation. In this survey, we review the geometry, learning, and computation of superposed representations, explaining how feature statistics and decoder choice affect the conclusions. To connect these theoretical accounts with evidence from trained networks, we compare practical methods for recovering and analyzing features and examine what their evaluations establish. Since accurate activation reconstruction alone does not establish feature identity or causal use, we discuss the methods' documented failures and applications in light of the evidence available for these different claims. Finally, we assess previously stated open problems and identify remaining theoretical and empirical questions about superposition in trained networks. We hope our work can pave the way for a deeper understanding of superposition and more reliable methods for interpreting neural networks.

---


### 219. [PPIM: Pennes Physics-Informed Mamba for Heat-Source-Conditioned 3D Bioheat Simulation](https://arxiv.org/abs/2609.06869)

**<font color=#1a73e8>作者：</font>** Dongyun Lee, Kyungho Yoon, Minwoo Shin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Three-dimensional bioheat simulation aims to predict transient temperature distributions in biological tissue and is commonly modeled using the Pennes bioheat equation, which combines thermal diffusion, perfusion-mediated heat loss, and external heat generation. In this study, we consider a controlled 3D Pennes bioheat simulation under a localized heat-source condition inspired by microwave ablation (MWA). To evaluate neural approximation performance, we compare three neural partial differential equation (PDE) solvers under the same controlled simulation: a spatial Fourier-feature physics-informed neural network (PINN), a generic PINNMamba temporal subsequence model, and Pennes Physics-Informed Mamba (PPIM). PPIM builds on the temporal subsequence model by incorporating conditioned heat-source input and Pennes-aware state-space model (SSM) decay initialization. All three neural models are trained under the same conditions with the same Pennes residual, and an explicit finite-difference method (FDM) solution is used only as the numerical reference. In a representative 600~s run, PPIM achieved the lowest MAE, relative $L_1$ error, and relative $L_2$ error among the evaluated neural solvers. Error maps further showed that the remaining PPIM errors were more concentrated near the heat-source region than across the rest of the domain. These results indicate that PPIM is effective for approximating the FDM reference final temperature field in this controlled simulation. The source code is available at this https URL.

---


### 220. [Organization of Valence and Arousal in Vision-Language Representations of Built Environments: Insights from the EMOIS Dataset](https://arxiv.org/abs/2609.06870)

**<font color=#1a73e8>作者：</font>** Madoka Yonekura, Katsunori Kohda, Nobuhiko Muramoto 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual perception of built environments contributes to the affective impressions that people form in everyday life. However, how these impressions are represented within vision foundation models remains largely unexplored. To support the systematic investigation of this subject, we introduce the Emotional Impression of Spaces (EMOIS) dataset, comprising 1,544 real-world built-environment images. Each image is annotated with image-evoked valence and arousal ratings collected from Japanese adults by conducting a large-scale web-based survey, with approximately 120 ratings per image. Using Contrastive Language--Image Pre-training (CLIP) representations, we perform predictive and geometric analyses to systematically investigate how valence and arousal are encoded and organized within the representation space. These analyses reveal that valence exhibited stronger and more coherent organization than arousal. Cross-dataset analyses with the Open Affective Standardized Image Set (OASIS), a benchmark dataset of general affective photographs, reveal differences in affective organization between the two datasets. Regression analyses demonstrate high predictive performance for valence and arousal within EMOIS, with mean coefficients of determination of 0.865 and 0.807, respectively, across repeated internal hold-out evaluations. Finally, we present an example-based interface illustrating how learned representations can support qualitative interpretation of predicted affective values. These findings can help elucidate affective representations of built environments and establish EMOIS as a densely annotated resource for future affective computing research in this domain.

---


### 221. [Exact Record Omission in Delta Attention: A Transport Criterion, Its Cost, and a Replay Certificate](https://arxiv.org/abs/2609.06872)

**<font color=#1a73e8>作者：</font>** Vishwajith Ramesh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When a user asks an assistant to forget a record, the test is whether the memory now matches the state it would hold if the record had never been stored. Independently encoded rows can be removed directly; a recurrent memory folds records into an evolving state. One hope is a receipt: save the difference the record made when it arrived, carry it forward through later updates, and subtract it, so that deletion costs one fixed-size edit no matter how long the conversation runs. We show that a transported receipt reaches exact omission if and only if the changes the record induces in later updates cancel out on net, and we measure whether they do on the released 48B Kimi Linear hybrid. They do not: after 4,096 further tokens the record still leaves an imprint of about 4.5% of the state norm that none of the tested receipt classes removes, recomputing half the suffix closes less than half the gap, and the per-token log a receipt needs costs more than a full checkpoint after 88 tokens. The same write-rule classification held on Mamba-2, Falcon-H1, and RWKV-7 with predictions recorded before the runs. Restoring a checkpoint from before the record and replaying the surviving suffix matches the never-stored state exactly on every array we check. In the hybrid suffix sweep, masking the record's attention rows brings sampled recovery close to the never-stored floor even though the recurrent imprint remains, and an auditor who rebuilds the reference can still detect it. Among the evaluated methods, checkpoint replay achieves exact omission, with work proportional to the replayed suffix.

---


### 222. [Novel Methods for Catheter and Guidewire Segmentation in X-ray Fluoroscopy under a Federated Learning Setting](https://arxiv.org/abs/2609.06876)

**<font color=#1a73e8>作者：</font>** Chayun Kongtongvattana  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Endovascular procedures rely on real-time manipulation of thin instruments, catheters and guidewires, under X-ray fluoroscopy guidance, where accurate visual analysis is essential for procedural safety. Learning-based methods are constrained by structural complexity, data scarcity, and privacy regulations precluding centralised training across institutions. This thesis presents a structure-aware federated learning framework for catheter and guidewire analysis, with four contributions evaluated on real-animal and phantom data.
A benchmark dataset, CathAction, is introduced for catheterisation analysis, with over 600,000 annotated frames and 40,000 segmentation masks. A shape-sensitive loss transforms masks into signed distance maps compared in a structural feature space, improving Dice coefficient by up to 2.9 points across five backbones.
This is extended to federated learning with shape-sensitive loss, preserving geometric consistency under heterogeneous client data and outperforming federated averaging by up to three points in mean intersection-over-union as clients scale from four to eight. Federated learning with projected gradient descent adds adversarial optimisation, raising mean intersection-over-union by over ten points on real-animal data.
Finally, a structure-aware diffusion framework synthesises catheter and guidewire video sequences, combining structural supervision with a domain-adaptive reconstruction objective, reducing Frechet video distance over a strong baseline while maintaining visual fidelity. Incorporating synthetic sequences into federated training raises the Dice score from 44 to 51 percent under data scarcity, with gains across four held-out sites.
Together, these contributions advance privacy-preserving catheter and guidewire analysis, supporting collaborative training without centralising patient data or large amounts of manual annotation.

---


### 223. [Learning Adaptive SED for heterogeneous load balancing](https://arxiv.org/abs/2609.06881)

**<font color=#1a73e8>作者：</font>** Sanne van Kempen, Jaron Sanders, Fiona Sloothaak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study a two-server load balancing system with heterogeneous service rates that are a priori unknown to the dispatcher. The goal is to route customers according to the Shortest--Expected--Delay (SED) policy, but this requires knowledge of the service rates. Empirical policies that route based on estimates perform poorly: due to estimation error, the empirical policy disagrees with the oracle on an infinite region of the state space. We propose an online learning algorithm that converges to SED while learning the service rates. The algorithm carefully balances empirical SED routing with forced exploration phases that guarantee sufficient sampling of both servers. We prove that our algorithm achieves finite regret; this differs from classical Multi-Armed Bandit settings where regret typically grows logarithmically in time. Finally, numerical experiments demonstrate the performance of our algorithm and highlight the regimes in which forced exploration is especially beneficial.

---


### 224. [Noisy-Space Policy Gradient for Diffusion Policies in Offline Reinforcement Learning](https://arxiv.org/abs/2609.06882)

**<font color=#1a73e8>作者：</font>** Mahmoud Selim, Cristina Cipriani, Karl H. Johansson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion policies offer a powerful and expressive parameterization for continuous control. Yet, their integration with reinforcement learning remains conceptually and algorithmically challenging. In this work, we address this gap by introducing a noisy-space action-value (Q-)function that assigns values to diffusion latents through the distribution of executed actions induced by the denoising process. We show that this construction admits a precise semantic interpretation and derive a noisy-space policy gradient (NSPG) that optimizes noisy latents using only clean action-space value estimates. Building on this result, we formulate a KL-regularized policy improvement over noisy latents and show that the resulting objective admits a diffusion-compatible regression form, avoiding backpropagation through the denoising process. Empirical results on state-based D4RL benchmarks and vision-based OGBench tasks demonstrate that the proposed noisy-space objective provides a principled and effective basis for training diffusion policies in offline reinforcement learning. Project webpage: this https URL

---


### 225. [Dynamic-Programming-Guided Hierarchical BPE and Empirical Analysis of Vocabulary Pruning](https://arxiv.org/abs/2609.06898)

**<font color=#1a73e8>作者：</font>** Kenny Shao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Byte Pair Encoding (BPE) constructs vocabularies through greedy pair merging, but the resulting merge order does not necessarily allocate a fixed model-visible vocabulary optimally for compression. We propose Dynamic-Programming-Guided Hierarchical BPE (DH-BPE), a vocabulary-construction method that combines token exposure under exact minimum-token segmentation with the hierarchical dependencies induced by BPE training. Starting from a modestly overshot BPE candidate vocabulary, DH-BPE uses dynamic programming to measure candidate utility and applies exposure-guided, dependency-aware pruning to select a fixed-size model-visible vocabulary. We compare DH-BPE against Standard BPE and recent vocabulary-optimization baselines, including Pruned BPE, MinGram, and MinGram-PP, in primary evaluations at 12K and 16K target vocabulary sizes, with an additional 18K evaluation against MinGram only. Across the primary 12K and 16K comparisons, DH-BPE consistently improves aggregate compression over Standard BPE, Pruned BPE, and MinGram under a shared exact minimum-token DP encoder. MinGram-PP achieves stronger aggregate compression in the primary comparisons, but DH-BPE outperforms it at overshoot factors f = 2.0 and f = 3.0 in cross-corpus evaluation; at 12K, MinGram-PP reverses this ordering only with the substantially larger candidate pools at f = 4.0 and f = 5.0. Qualitative analysis further shows that DH-BPE balances later, more complete BPE merges with reusable subword components, providing a practical approach to improving vocabulary allocation under a fixed model-visible vocabulary budget.

---


### 226. [Constrained Online Learning with Noisy Constraint Values](https://arxiv.org/abs/2609.06921)

**<font color=#1a73e8>作者：</font>** Vaneet Aggarwal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study constrained online convex optimization with adversarial constraints when constraint values and gradients are observed through unbiased noise. Gaussian value noise of standard deviation $\sigma$ yields a worst-case lower bound of $\Omega(\min\{\sigma,1\}T/\log^7T)$ on the maximum of expected regret and expected hard violation, even with known gradients. This rules out any jointly $O(T^{1-\delta})$ guarantee for fixed $\delta>0$ and fixed positive noise level. We therefore study budget violation: the largest cumulative overspend over any window within a fixed horizon. We introduce \LEDGER, which tracks observed net consumption in a nonnegative balance and sets constraint weights before the current feedback noise. Under common feasibility and conditional finite-variance feedback, for fixed problem parameters, \LEDGER\ achieves $O(\sqrt T/V)$ expected regret and $O(\sqrt V\,T^{3/4}+\sigma\sqrt T)$ expected budget violation for $V\in[T^{-1/2},1]$. This gives the pair $(O(\sqrt T),O(T^{3/4}))$ at $V=1$ and $(O(T^{2/3}),O(T^{2/3}))$ at $V=T^{-1/6}$, without a Slater condition. The budget-focused endpoint $V=T^{-1/2}$ gives $(O(T),O(\sqrt T))$. The same update yields $O((1+E[P_T])\sqrt T/V)$ expected dynamic regret for predictable feasible comparator paths, without common feasibility or path-length input. Its budget bound instead depends on the shortest feasible path, up to a dimension factor.

---


### 227. [Emo-DVS: A Multimodal Benchmark for Privacy-Aware Emotion Recognition with Event Cameras](https://arxiv.org/abs/2609.06928)

**<font color=#1a73e8>作者：</font>** Jiaqi Chen, Qinfu Xu, Hao Zhuang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Emotion analysis is a fundamental task in computer vision, but its practical deployment remains constrained by the privacy risks inherent to conventional RGB cameras. Bio-inspired event cameras present a promising hardware-level solution because they capture asynchronous brightness changes, thereby reducing exposure of facial identity details while leveraging high dynamic range for robust perception under challenging illumination conditions. Despite these advantages, existing event-based methods struggle in complex real-world settings due to limited dataset scales, simple acquisition conditions, and reliance on single-modality visual cues. To address these, we establish a challenging tri-modal benchmark with event, audio, and text modalities and propose the Information-Guided Gated Fusion (IGF) framework, which first pre-trains an event encoder on the FAU subset of Emo-DVS to capture fine-grained facial dynamics, then employs adaptive modality gating to suppress modality-specific noise, and finally leverages mutual information maximization to align robust cross-modal representations. To alleviate data scarcity, we introduce Emo-DVS, the first large-scale event-based emotion analysis dataset, which couples dynamic illumination with the Facial Action Unit (FAU) subset and emotion subset. Extensive experiments demonstrate that IGF achieves state-of-the-art performance.

---


### 228. [Sub-Pixel Affine Registration of Space Debris Images via the Radon Point Spread Function](https://arxiv.org/abs/2609.06929)

**<font color=#1a73e8>作者：</font>** Shenshen Luan, Miaomiao Tian, Shuai Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inter-frame affine misalignment caused by platform jitter and attitude adjustments poses a fundamental challenge for multi-frame analysis of point targets in optical surveillance. Conventional registration methods rely on spatial intensity correlations or distinctive image features, both of which are largely absent in low-signal-to-noise-ratio point target imagery. We introduce the Radon Point Spread Function (RPSF) to characterize point targets in the Radon-transformed domain, and derive a closed-form framework that jointly estimates inter-frame translation and rotation from as few as four scalar RPSF samples per frame pair. The method requires no iterative optimization, feature extraction or interpolation, which is suitable for resource-constrained onboard processing. Simulation results confirm sub-pixel translation accuracy and a mean rotation error of 0.2556° at 1° Radon angular resolution. Validation on five real space debris datasets including both ground-based and in-orbit observations yields a mean calibration error below 0.5 pixels, substantially exceeding the precision required for reliable multi-frame processing.

---


### 229. [PCSDiff: Diffusion-Based Bias Correction and Super Resolution Toward Practical Operational Medium-Term Precipitation Forecast](https://arxiv.org/abs/2609.06942)

**<font color=#1a73e8>作者：</font>** Yuze Sun, Shiyi Wang, Jiancheng Pan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Medium-range precipitation forecasts are impaired by persistent systematic biases, lead-time-dependent error accumulation, and coarse spatial resolution, restricting their reliability for flood-drought risk assessment. Existing AI correction techniques lack dedicated modeling for multi-day dynamic bias evolution and proper meteorological constraints, often generating over-smoothed rainfall structures, and cannot meet operational deployment demands. This work introduces PCSDiff, a cascaded task-decoupled diffusion framework targeting 10-day precipitation bias correction and downscaling. To jointly counteract temporal error drifts and reconstruct physically plausible local precipitation details, PCSDiff integrates the Precipitation Intensity-aware Multi-branch Decoder (PIMD) module for dynamic multi-day error mitigation using synoptic-temporal features, followed by a two-phase conditional diffusion super-resolution module to restore fine-scale precipitation patterns. Evaluated against CMA-CRA observations over China after global-data training, PCSDiff cuts RMSE by 16.1% and lifts ACC by 13.9% relative to raw ECMWF forecasts at 3-10-day lead times, and consistently outperforms mainstream deep-learning baselines on both general and extreme-precipitation metrics. Benefiting from a streaming inference pipeline, our method achieves low-latency rolling forecasting for practical meteorological operations.

---


### 230. [Particle Dynamics of Flow Matching and Classifier-Free Guidance from a Stagewise Geometry Perspective](https://arxiv.org/abs/2609.06947)

**<font color=#1a73e8>作者：</font>** Jian-Feng Cai, Zhengyi Su, Chao Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow matching, together with classifier-free guidance (CFG), is widely used in generative modeling, yet much of the theoretical understanding remains distribution-wise. Since practical sampling follows individual trajectories, distribution-level guarantees alone do not fully capture how trajectories interact with the data geometry or how guidance reshapes it. To overcome this limitation, we establish a unified stagewise geometric theory of attraction and absorption for both continuous dynamics and explicit Euler discretization. Specifically, with $t\in[0,1]$ running from noise to data, we show that unconditional flow trajectories are successively attracted toward a neighborhood of the global mean, the data convex hull, and a neighborhood of a possibly nonconvex local cluster. Across these stages, the corresponding distance satisfies a common contraction estimate, yielding an ${O}(1-t)$ decay of the distance in the final stage. For CFG, the same structure persists with an extrapolated mean, an inflated conditional convex hull, and, near the target cluster, the restored local geometry of conditional flow matching. We further show that a general time schedule $a(t)$ replaces the $O(1-t)$ decay by $O(1-a(t))$. Together, these results provide a unified particle-level geometric account of flow matching and CFG across continuous and discrete sampling.

---


### 231. [PRG-Fusion: Orchestrating Generative Priors with Reconstruction Evidence for Driving View Synthesis](https://arxiv.org/abs/2609.06948)

**<font color=#1a73e8>作者：</font>** Sipeng He, Jialei Chen, Zhen Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthesizing photorealistic driving videos along specified trajectories is essential for scalable closed-loop simulation. Reconstruction-based methods leverage neural rendering to synthesize geometrically consistent views, but often exhibit diverse artifacts and missing content when the viewpoint deviates from the training trajectory. In contrast, generative models can synthesize realistic views along arbitrary trajectories from vehicle sensor data, yet often struggle to maintain temporal and geometric consistency across frames. To combine the strengths of both, we propose PRG-Fusion, a framework for driving view synthesis that uses reconstruction evidence to orchestrate generative priors across regions. Specifically, we extract region-wise degradation evidence from reconstructed driving scenes and convert it into Preserve, Repair, and Generate (PRG) labels. At inference, these labels serve as a unified routing policy for region-aware spatiotemporal synthesis, orchestrating 3DGS appearance preservation, LiDAR-guided structural correction, and video-prior-driven content completion across Preserve, Repair, and Generate regions, respectively. We then follow a two-stage training paradigm, first establish geometric control from sparse LiDAR projections and subsequently learning appearance control from dense 3DGS renderings. Extensive experiments on Waymo demonstrate that PRG-Fusion achieves state-of-the-art overall performance in novel trajectory video synthesis, with superior visual quality and geometric fidelity while maintaining competitive view consistency under large trajectory shifts.

---


### 232. [Joint-Conditioned Stereo Surface Reasoning for Interaction Field Estimation](https://arxiv.org/abs/2609.06955)

**<font color=#1a73e8>作者：</font>** Yanlin Jin, Yifan Yang, Bowen Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predicting hand--object interaction fields requires locating the nearest object-surface point for each hand joint, often from small and partially occluded image regions. We view this task as joint-conditioned surface-endpoint estimation: each joint has its own nearest endpoint, while endpoints from the same hand can draw on shared local surface evidence. This structure motivates Joint-Conditioned Stereo Surface Reasoning (JSSR). A temporal-stereo network jointly predicts 3D joints, a direct interaction field, and per-view endpoint evidence. Calibrated candidate search evaluates endpoint hypotheses using joint-specific image compatibility and cross-view correspondence. A hand-shared candidate support lets joints draw on common surface evidence, and a learned residual gate controls the geometric correction when observations are ambiguous. Our system built on this method ranked third on the SHOW3D Interaction Field Challenge leaderboard.

---


### 233. [MSSP: Multi-Scale Spatially-Constrained Partition for Unsupervised Semantic Segmentation of 3D Point Clouds](https://arxiv.org/abs/2609.06959)

**<font color=#1a73e8>作者：</font>** Zhenghao Zhang, Xinjie Wang, Wei Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D point cloud semantic segmentation is essential for real-world spatial understanding, yet the prohibitive cost of human annotations motivates unsupervised approaches that require no labels. Existing superpoint-based methods typically rely on spectral analysis at a fixed granularity, failing to capture the hierarchical semantic structures inherent in complex indoor scenes. To bridge this gap, we present a Multi-Scale Spatially-Constrained Partition (MSSP) framework that combines multi-scale spectral analysis with spatially-constrained clustering. Multi-scale spectral analysis constructs enriched superpoint descriptors across multiple clustering granularities; however, the resulting high-dimensional feature space calls for a structural prior to translate into cleaner segmentation. Spatially-constrained clustering supplies this prior by restricting superpoint merging to physically adjacent regions, imposing the spatial coherence needed for multi-scale features to be effective. Extensive experiments on S3DIS and ScanNet show that MSSP achieves the best mIoU among unsupervised methods on the main benchmarks, with particularly significant gains on S3DIS. Notably, our ablation reveals a regularize-then-enrich interaction: multi-scale features alone do not improve final segmentation, yet become highly effective when coupled with spatial regularization, underscoring that spatial coherence is aprerequisite for multi-scale representations in superpoint clustering.

---


### 234. [SSP-DMGTimeNet: Physics-Constrained Learning for Spatiotemporal Trajectory Prediction of Vehicle Platoons](https://arxiv.org/abs/2609.06961)

**<font color=#1a73e8>作者：</font>** Yuhang Wang, Kailang Ma, Zirui Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing car-following prediction methods mainly optimize trajectory accuracy, while rarely considering whether predicted disturbances propagate realistically along a vehicle platoon. This limitation may lead to accurate but string-unstable predictions. We propose SSP-DMGTimeNet, a physics-constrained learning framework for spatiotemporal trajectory prediction of vehicle platoons. The model combines multi-scale temporal representations with cross-vehicle interaction features to capture complex and time-varying platoon dynamics. A propagation-delay-aware causal attention mechanism explicitly models upstream-to-downstream disturbance propagation by learning response delays between adjacent vehicles and accumulating them along the platoon. In addition, time- and frequency-domain string-stability losses relieve disturbance amplification across both adjacent vehicles and arbitrary sub-platoons during training. Experiments on HighD show that SSP-DMGTimeNet achieves an unstable-window rate of 0.65\% for five-vehicle platoons and a maximum head-to-tail amplification of 0.898 on the ground-truth excitation subset, while maintaining competitive trajectory prediction performance. In zero-shot evaluation on NGSIM US-101 and I-80, the model achieves velocity MAEs of 1.316~m/s and 1.252~m/s, with unstable-window rates of 3.90\% and 4.10\%, respectively. These results demonstrate that incorporating platoon-level physical constraints can effectively balance trajectory prediction accuracy and disturbance propagation stability.

---


### 235. [DPSF-Net: A Dual-Prior Spatial-Frequency Network for Real-World Remote Sensing Image Dehazing](https://arxiv.org/abs/2609.06962)

**<font color=#1a73e8>作者：</font>** Mei Lu, Shangliang Shao, Shanliang Yao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world remote sensing image dehazing (RSID) remains challenging because atmospheric scattering, spatially non-uniform haze and colour distortion jointly degrade structural and spectral information. Most deep learning methods rely on RGB inputs and spatial-domain feature extraction, which limits their ability to separate global background haze from local surface details. Here, we propose DPSF-Net, a dual-prior spatial-frequency network built on MCAF-Net for real-world RSID. The network uses hazy RGB images and dark channel prior (DCP) maps as joint inputs, allowing physical degradation cues to guide end-to-end feature learning. A spatial-frequency residual interaction block introduces a FourierUnit branch into multi-directional spatial interaction to model large-scale haze components. A prior-guided feature attention module adaptively fuses prior and attention features to reduce colour shift and structural distortion. A selective kernel complementary fusion module screens multi-scale skip features through bidirectional residual complementary gating and selective kernel fusion. Extensive experiments demonstrate that DPSF-Net achieves state-of-the-art performance on the real-world RRSHID remote sensing image dehazing benchmark and remains competitive across multiple synthetic datasets. Moreover, the proposed method strikes a favourable balance among restoration quality, parameter count and computational complexity, supporting the effectiveness of dual-prior spatial-frequency modelling.

---


### 236. [Lightweight Detection of Electromagnetic Signal Injection Attacks on Image Sensors](https://arxiv.org/abs/2609.06973)

**<font color=#1a73e8>作者：</font>** Youqian Zhang, Chunxi Yang, Eugene Yujun Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Electromagnetic signal injection attacks (ESIA) pose a growing threat to image sensors, which are increasingly used in different intelligent systems. By emitting electromagnetic interference, adversaries can manipulate pixel values, potentially misleading downstream artificial intelligence (AI) models and causing unsafe decisions in these systems. We present a lightweight detection method that leverages optically black pixels, which are non-exposed pixels already present in many modern image sensors, to identify the attacks. Our detection approach achieves an area under the receiver operating characteristic curve (ROC-AUC) of up to 99.6\% and an Equal Error Rate (EER) as low as 0.027 across diverse attack conditions. Our method requires minimal computational overhead and no hardware modifications, making it a practical and effective defense for securing vision-based systems against ESIA.

---


### 237. [AF-Mamba: Efficient Long-Term Signal Modeling for Early Prediction of Atrial Fibrillation Onset](https://arxiv.org/abs/2609.06984)

**<font color=#1a73e8>作者：</font>** Yongbin Lee, Ki H. Chon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Atrial fibrillation (AF) is the most common cardiac arrhythmia and is associated with increased risks of stroke and heart failure. The growing availability of wearable and portable ECG monitoring enables continuous assessment of cardiac rhythm outside clinical settings. Predicting AF before its onset could provide additional lead time for timely clinical assessment and potentially improve the management of patients at risk of AF-related complications. This study focuses on predicting AF onset one hour in advance using long-term RR intervals (RRIs). To address this challenge, we propose a deep learning architecture that integrates temporal convolutional networks (TCNs) for local features encoding with Mamba, a selective state-space model capable of long-range sequence modeling. This hybrid TCN-Mamba design enables efficient training and inference on one-hour input windows, overcoming limitations of Transformers' quadratic scaling and recurrent networks' vanishing gradients. In subject-wise 5-fold testing, the proposed model achieved a sensitivity of 0.889, specificity of 0.943, F1-score of 0.813, AUROC of 0.974, and AUPRC of 0.933. In paired cross-dataset holdout evaluation, AF-Mamba maintained discriminative performance across unseen AF and NSR datasets, achieving a mean AUROC of 0.897. Compared against state-of-the-art AF prediction models and general time-series models, AF-Mamba achieved competitive predictive performance while providing a favorable performance-efficiency trade-off for long RRI sequences. These findings demonstrate the potential of AF-Mamba for accurate AF prediction one hour in advance and real-time continuous ambulatory monitoring.

---


### 238. [AV-SafetyBench: A Safety Benchmark for Text-to-Audio-Video Generation](https://arxiv.org/abs/2609.06991)

**<font color=#1a73e8>作者：</font>** Suah Choi, Tae-Young Lee, Gyeong-Moon Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent text-to-audio-video (T2AV) models jointly generate video, speech, sound effects, and ambience from a single text prompt. This capability poses new challenges for safety evaluation, as unsafe content may be conveyed through the audio track or arise only when the visual and audio tracks are interpreted jointly. Existing safety benchmarks largely focus on either generated video or generated audio in isolation and are therefore not designed to capture these risks. To close this gap, we introduce AV-SafetyBench, the first safety benchmark developed specifically for T2AV generation. AV-SafetyBench comprises a four-axis, 13-category taxonomy and 5,200 manually reviewed prompts that specify visual scenes, speech, and non-speech audio. Our evaluation protocol assesses each output under three views: Full-AV, Video-Only, and Audio-Only. It then uses the Video-Only and Audio-Only judgments to assign Full-AV unsafe outputs to one of four risk sources: Video-Only, Audio-Only, AV-Both, or AV-Joint. We evaluate five open-source T2AV models and validate the automated Full-AV judgments against human annotations. Across the five models, Full-AV Unsafe Rates range from 25.1% to 49.4%. Beyond these aggregate rates, risk-source analysis reveals that, for four of the five models, Audio-Only and AV-Joint cases-unsafe outputs missed by video-only evaluation-account for 41.6-48.3% of Full-AV unsafe outputs for which a risk source could be assigned. In the Cross-Modal Harm Emergence category, AV-Joint accounts for 87.5% of unsafe outputs withan assigned risk source. Together, these findings demonstrate the value of AV-SafetyBench for evaluating T2AV safety across the visual and audio modalities and their interaction.

---


### 239. [Adaptive Complementarity in Human-AI Systems: Architecture as a State-Shaping Choice](https://arxiv.org/abs/2609.07001)

**<font color=#1a73e8>作者：</font>** Babak Heydari  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human-AI interaction can improve current performance while changing the capabilities and relationships on which future performance depends. We develop adaptive complementarity, a framework for choosing interaction architecture with these state consequences in view. Access, information exposure, task allocation, timing, and communication can alter which arrangement will be valuable later; their settings can often be reset faster than the capabilities, search patterns, or conventions they create. Three mechanisms organize the argument: information exposure and collective search, delegation and capability evolution, and strategic interdependence and information governance. Their integration yields cross-mechanism implications, including conditions under which a loss of expertise heterogeneity increases the information differentiation required to preserve independent search. We distinguish strong human-AI complementarity from advantage over another workflow and from advantage over an evolving reference policy. A knowledge-coverage illustration shows how different interaction histories can reverse current workflow rankings even at equal human competence. It also separates that result from the incremental value of state feedback, which can be small when a well-chosen stable workflow anticipates learning. The framework directs evaluation toward the states present interaction creates, their consequences for later architectural fit, and the conditions under which observing and responding to them is worthwhile.

---


### 240. [Fine-Grained Visual Preprocessing and Dual-Stream Temporal Modeling for Multimodal Sentiment Analysis on Social Media](https://arxiv.org/abs/2609.07010)

**<font color=#1a73e8>作者：</font>** Su Li, Yigong Zhang, Lei Xiong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal sentiment analysis often remains text-dominant due to raw-video noise and insufficient temporal modeling. Using CH-SIMS v2.0S, this study proposes three improvements: the NAPS pipeline---a seven-stage system integrating face tracking,identity embedding, and normalized lip-motion analysis to reduce visual noise;DS-TANet, combining an EfficientNetB2 static stream, RAFT optical-flow motion stream, motion-guided attention, and Bi-GRU temporal modeling; and DS-TAFNet, fusing visual and MacBERT-Base textual representations via concatenation fusion. With NAPS, the static visual baseline achieves 80.98\% Macro F1, comparable to the text baseline of 80.55\%; DS-TANet improves visual Macro F1 to 82.58\%;and DS-TAFNet achieves 87.49\% accuracy and 87.48\% Macro F1. These results demonstrate that improving visual input quality and temporal representation is more effective than increasing fusion complexity under limited-data conditions.

---


### 241. [ARNAI: Artifact Removal Network based on Autoencoding and Inpainting for Robust Spinal Image Segmentation and Measurement](https://arxiv.org/abs/2609.07013)

**<font color=#1a73e8>作者：</font>** Sang-Jin Park, Jinyoung Choi, Seokwon Kim 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose: This study aims to develop an AI framework applicable for postoperative imaging for automated measurement of spinopelvic parameters on radiographs with robustness to the presence of spinal implants.
Materials and Methods: We retrospectively reviewed lateral lumbar spine radiographs from two institutions (Internal: January 2017--December 2024; External: October 2021--September 2025). We developed the Restore, Segment, and Measure (RSM) framework, incorporating a novel Artifact Removal Network based on Autoencoding and Inpainting (ARNAI) to mitigate implant-related artifacts in postoperative radiographs. Segmentation and spinopelvic parameter (PT, LL, SS, SCA) measurement performance were assessed using Wilcoxon signed-rank tests and intraclass correlation coefficients.
Results: When ARNAI was added to a recent Transformer-based segmentation model, FCBFormer, the mean DSC increased to 0.870 from 0.814, with marked gains at L3--L5 and smaller improvements at L1--L2. On 91 radiographs with implants, the mean L4--L5 segmental Cobb angle error decreased to 4.7 ° from 15.6--16.2 °, an average error reduction of 70%. The ICC for L4--L5 segmental Cobb angle improved to 0.54 (Rater 1) and 0.59 (Rater 2) from 0.18, and ICCs for pelvic tilt, lumbar lordosis, and sacral slope all exceeded 0.70. The improvement in L4--L5 segmental Cobb angle error was statistically significant in the internal implant-containing cohort after correction for multiple comparisons.
Conclusion: The proposed RSM framework improved automated spinopelvic parameter measurement in implant-containing postoperative radiographs. By mitigating implant-related artifacts, ARNAI improved segmentation and downstream measurement accuracy, with the greatest benefit observed for L4--L5 segmental Cobb angle estimation, where the mean error was reduced by approximately 70%.

---


### 242. [HyperTransfer: Understanding the Equivalence between Base Optimizer and Hyperball](https://arxiv.org/abs/2609.07017)

**<font color=#1a73e8>作者：</font>** Jinghui Yuan, Hongtao Zhang, Jade Zou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyperball optimizers constrain parameter norms and update only their directions, establishing a distinct paradigm for neural network optimization. Although this geometry appears fundamentally different from that of conventional Base Optimizers, which update both parameter norms and directions, we show that the two paradigms are dynamically equivalent for scale-invariant networks. Building on this equivalence, we propose HyperTransfer, which constructs a Hyperball optimizer that reproduces the dynamics of a target Base Optimizer using only its initialization and learning-rate schedule, without running the target optimizer itself. We further derive the inverse mapping and extend the framework to non-scale-invariant networks. Experiments show that both HyperTransfer and the inverse mapping produce loss trajectories nearly identical to those of their targets, suggesting that Hyperball dynamics are governed primarily by the induced effective learning-rate schedule and optimizer state.

---


### 243. [CIPHER: Benchmarking Cross-record Inference over Privacy-Hardened Evidence Records](https://arxiv.org/abs/2609.07022)

**<font color=#1a73e8>作者：</font>** Suparno Roy Chowdhury, Manan Roy Choudhury, Dhruv Madhwal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Reasoning over privacy-constrained records requires combining structured attributes with evidence from free-text narratives. We introduce CIPHER (Cross-record Inference over Privacy-Hardened Evidence Records), a benchmark of expert-validated questions from consumer-finance, clinical, and law-enforcement records. The questions cover common tabular operations and include executable SQL supervision. We evaluate retrieval, prompting, table-specialist, and hybrid symbolic-neural systems under native redaction and surrogate-based evidence restoration. All system families exhibit substantial failures even when supporting records are provided. Most errors arise from incorrect record selection and predicate interpretation rather than arithmetic execution. Privacy transformations have non-uniform effects, sometimes obscuring necessary evidence and sometimes reducing distraction. CIPHER provides a reproducible testbed for diagnosing these failures and assessing how transformations of sensitive text affect reasoning over hybrid records.

---


### 244. [Efficient Learning and Symmetry Discovery under Exact Invariances](https://arxiv.org/abs/2609.07031)

**<font color=#1a73e8>作者：</font>** Ashkan Soleymani, Behrooz Tahmasebi, Patrick Jaillet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning with group invariances is central to many scientific and geometric learning problems, yet its computational foundations remain poorly understood. Even for classical supervised regression settings, it has been unclear whether one can efficiently compute a regression function that is exactly invariant to a given group action. Recent work showed that exact invariance can be enforced in polynomial time when the underlying group is finite and known, but left open the cases of infinite groups and unknown symmetries. In this paper, we resolve both challenges. First, we present the first polynomial-time algorithm for learning with exact group invariances that applies uniformly to finite and infinite groups. The runtime is polynomial in the data dimension and sample size, and independent of the group, while achieving strong generalization guarantees. This provides a computational explanation for the empirical success of invariant and equivariant methods in geometric machine learning and partially answers a recent open question in the literature. Second, we study learning in the symmetry discovery setting, where the invariance group is unknown. Focusing on the subgroup lattice of a finite group, we show that exact symmetries can be identified from data and exploited for learning in polynomial time. For regression over finite-dimensional feature spaces, our algorithm provably recovers the underlying symmetry, matches the minimax-optimal sample complexity of the known-symmetry setting, and runs in time polynomial in the data dimension and sample size. Our analysis relies on tools from random Cayley graphs and expander theory, which may be of independent interest.

---


### 245. [TrojanWorld: Backdooring World-Model Agents via Imagination Steering](https://arxiv.org/abs/2609.07051)

**<font color=#1a73e8>作者：</font>** Wenkai Huang, Siyuan Liang, Gaolei Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models increasingly serve as the predictive core of model-based reinforcement learning agents, enabling them to simulate future dynamics and reason over imagined trajectories before acting. Their substantial training demands make pretrained world models attractive for distribution and reuse, exposing downstream systems to model supply chain threats. Backdoor attacks offer a targeted and stealthy means of exploiting such supply chains, yet their threat to interactive world-model agents remains largely unexplored. To fill this gap, we present TrojanWorld, a backdoor framework for world-model agents that induces attacker-specified behavior by steering internal imagination. A physical object placed in the scene acts as the trigger, enabling deployment-time activation through the agent's native observation pipeline without digitally manipulating the observation stream. To achieve effective, stealthy, and persistent control, TrojanWorld combines Decision-Reflective Induction to steer trigger-conditioned imagination toward attacker-specified actions using decision feedback, Clean Behavior Anchoring to preserve trigger-free predictive and behavioral fidelity, and Causal Propagation to sustain the induced preference along subsequent trajectories after the trigger disappears. Together, these mechanisms establish an end-to-end attack chain from physical perception through corrupted imagination to malicious action selection. Experiments with the TD-MPC2, DreamerV3, and R2-Dreamer systems across the DeepMind Control, MetaWorld, MyoSuite, and RoboDesk benchmarks show that under trigger activation, TrojanWorld achieves a target-action deviation as low as 0.026 while retaining at least 98.8% of the corresponding clean performance. Even after trigger removal, the compromised agent can remain trapped in the induced behavioral trajectory, continuing to execute attacker-specified actions.

---


### 246. [CNsEMD: An Expert-Annotated Multi-Field-Strength MRI Dataset and a Hyperspherical Manifold Network for Multimodal Cranial Nerve Parcellation](https://arxiv.org/abs/2609.07058)

**<font color=#1a73e8>作者：</font>** Lei Xie, Junxiong Huang, Guoqiang Xie 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cranial nerves (CNs) play essential roles in sensory, motor, and autonomic functions. Accurate CN parcellation from multimodal magnetic resonance imaging (MRI) is crucial for neuroanatomical analysis and neurosurgical planning. However, accurate CN parcellation remains extremely challenging because CNs are very small, exhibit low image contrast, and have slender tubular morphologies and complex anatomical trajectories. Moreover, the lack of publicly available, expert-annotated datasets has impeded the development and fair benchmarking of learning-based CN analysis methods. In this work, we introduce CNsEMD, an expert-annotated multimodal dataset for CN parcellation. It comprises data from 202 subjects acquired on 3T, 5T, and 7T MRI scanners. We further propose the projective hyperspherical manifold network (PHM-Net), which learns cross-modal representations by capturing angular relationships in a shared hyperspherical embedding space. Rather than performing multimodal fusion in Euclidean space, the proposed Hyperspherical cross-modal interaction (HCI) module enables bidirectional feature exchange between T1-weighted (T1w) and direction-encoded color (DEC) representations on a unit hypersphere. The Magnitude-preserving projective hyperspherical orientation representation (PHOR) captures the axial nature of DEC orientations while preserving diffusion magnitude. The hyperspherical prototype segmentation head (HPSH) further extends angular similarity to voxel-wise classification using normalized voxel embeddings and learnable class prototypes. Extensive experimental results on the CNsEMD dataset demonstrate the effectiveness of our PHM-Net against state-of-the-art methods. CNsEMD establishes a reproducible benchmark for multimodal CN imaging, while PHM-Net provides a geometry-consistent solution for CN parcellation across diverse MRI acquisitions.

---


### 247. [PhysSAE: Mechanistic Interpretability with Sparse Autoencoders](https://arxiv.org/abs/2609.07061)

**<font color=#1a73e8>作者：</font>** Nandita N. Patil, Eshwar R. A., Gajanan V. Honnavar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-Informed Neural Networks (PINNs) embed PDE residuals into neural network training, but their internal representations remain opaque: it is unknown what physical features their hidden layers encode or whether those features have a localized causal role. We present PhysSAE, a mechanistic interpretability framework that trains overcomplete sparse autoencoders (SAEs) on PINN penultimate-layer activations and evaluates dictionary atoms through direct causal intervention in the original frozen hidden state: $h_{\mathrm{cf}} = h - \alpha z_k d_k$, bypassing the SAE decoder entirely. Across six PDE families, with 3 PINN seeds and 3 SAE seeds each---we show that (i) Our discovered SAE atoms align with independently-defined physical observables (max Pearson $|r|=0.951$, always $\gg$ permutation null), (ii) the causal footprint of top-aligned atom ablation is 1.2--4.2$\times$ more spatially concentrated canonical than PCA or ICA interventions, and (iii) top-aligned atoms outperform matched random controls on causal localization for structured physical concepts (ESF$_{80}$ advantage 0.04-0.44). Two-atom bilateral representations improve concept regression R$^2$ by $\Delta R^2\!=\!0.05\text{-}0.15$ over single atoms, while random pairs decrease it by up to 0.60. These results demonstrate that PINNs develop sparse, physically structured latent representations that can be identified and causally interrogated post-hoc, opening a path toward interpretability-aware scientific machine learning.

---


### 248. [Trust-But-Verify: Poisoning-Resilient Locally Private Graph Learning Protocols](https://arxiv.org/abs/2609.07063)

**<font color=#1a73e8>作者：</font>** Longzhu He, Li Sun, Hao Peng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Built upon local differential privacy (LDP), locally private graph learning protocols have emerged as an important paradigm for decentralized graph learning, balancing privacy protection and learning utility. Under such protocols, each user locally perturbs their node features and adjacency information before transmission, ensuring formal privacy guarantees without original data leaving the device. However, the inherently open participation nature renders these protocols critically vulnerable to data poisoning attacks, where adversaries inject carefully crafted malicious nodes to corrupt neighborhood aggregation and degrade downstream utility. Despite the severity of this threat, effective defenses in this setting remain largely unexplored. In this paper, we propose VERITAS, a poisoning-resilient locally private graph learning protocol built on a trust-but-verify paradigm. By introducing a verification list encoding graded peer trust levels, VERITAS jointly privatizes node features and graph structure on the user side, while exploiting bilateral attestation asymmetry on the server side to identify and prune malicious nodes. Concretely, VERITAS comprises four synergistic stages: (1) local data perturbation, (2) attestation-driven malicious node pruning, (3) utility restoration via dual denoising, and (4) robust private graph learning. Extensive experiments on four real-world benchmark datasets across multiple LDP mechanisms and GNN architectures demonstrate that VERITAS effectively defends against data poisoning attacks and significantly improves downstream graph learning utility under rigorous privacy guarantees.

---


### 249. [Continuous Token-Level Spatio-Temporal Context Modeling for Visual Object Tracking](https://arxiv.org/abs/2609.07070)

**<font color=#1a73e8>作者：</font>** Ding Xia, Meiqin Liu, Jing Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatio-temporal context has become increasingly crucial for visual tracking. However, most existing approaches extract spatio-temporal cues via discrete sampling strategies, which inherently deviate from the continuity of spatio-temporal context, thereby deteriorating tracking performance. To address this challenge, we propose TLCTrack, a novel tracking framework that models token-level spatio-temporal context through continuously updated salient tokens, enabling more accurate target representation. Specifically, TLCTrack incorporates three components: Masked Unidirectional Attention (MUA), Spatial Salient Token Collection (SSTC), and Temporal Salient Token Bank (TSTB) modules. By explicitly integrating spatio-temporal context, MUA extracts discriminative targetaware spatial features in the search region. To avoid the negative impact of background on feature learning, SSTC progressively suppresses background interference, thereby enhancing target spatial representation. Finally, TSTB captures high-quality spatio-temporal information through continuous salient token updates. Extensive experiments on five benchmarks demonstrate that our method achieves superior performance over state-of-the-art trackers. Code and models are available at this https URL.

---


### 250. [Single Image to Textured 3D Object Generation in Frequency Domain: From Theory to Pipeline](https://arxiv.org/abs/2609.07085)

**<font color=#1a73e8>作者：</font>** Qisen Wang, Yifan Zhao, Jia Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-view 3D reconstruction, also known as image-to-3D, is a persistently challenging task due to the extreme lack of information. Recently, diffusion models pre-trained on large-scale datasets served as 2D priors are used to solve the ill-posed task but suffer from color deviation and view inconsistency, which can be curbed by using diffusion models fine-tuned with 3D annotated data served as 3D priors. However, 3D priors lack high-frequency details, which cannot be solved by direct complementation with 2D priors in spatial domain for introducing erroneous low-frequency 2D prior guidance. In this paper, we revisit the characteristics of different diffusion priors from the frequency perspective. Based on our observations, we theoretically present a unified framework of hybrid optimization using multiple diffusion priors in frequency domain. Under this framework, we further propose Morpheus3D, a pipeline of 3D object generation from any single unposed image in the wild. Morpheus3D enhances 3D prior with high-pass image-prompt 2D prior guidance to reconstruct high-quality 3D objects while effectively suppressing view inconsistency, low-frequency color deviation, and high-frequency lacking problems. Both quantitative and qualitative experiments on the public and our collected datasets with complex textures show that our method exhibits significant improvements in generation quality.

---


> [!TIP]
> 当前位于：**201-250**（第 5/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-542](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
