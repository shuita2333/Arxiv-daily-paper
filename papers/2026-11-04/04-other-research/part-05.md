# 📦 其他研究 | 2026年11月04日

> 本类共 **633** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-633](./part-13.md)

---

### 201. [Mitigating Catastrophic Forgetting in Task-Free Federated Continual Forecasting via Two-Tier Replay under Concept Drift](https://arxiv.org/abs/2611.01098)

**<font color=#1a73e8>作者：</font>** Khaled Hallak, Oudom Kem  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated time-series forecasting is increasingly important in applications where temporal data are distributed across privacy-sensitive clients, such as environmental monitoring, smart cities, and industrial sensing. A central limitation of current continual-learning protocols is that they usually assume predefined task boundaries, whereas deployed forecasting systems receive an uninterrupted stream and must decide autonomously when adaptation is necessary. This paper addresses catastrophic forgetting in task-free federated forecasting under concept drift. We introduce a drift-aware continual-learning protocol in which each client monitors prediction-window RMSE, calibrates a robust median threshold from the offline base period, and triggers adaptation only after persistent degradation. To mitigate forgetting, we propose a TwoTierReplay mechanism that separates fixed offline representative memory from online memory. The offline tier preserves long-term knowledge learned during the base phase, while the online tier captures recent distributional changes after drift. Experiments on the Beijing Multi-Site Air- Quality dataset with 12 clients, three forecasting targets, and three horizons show that TwoTierReplay achieves the best stability-plasticity score in all nine target-horizon configurations. It improves over the strongest baseline by approximately 11.4%. These results suggest that explicit temporal structuring of replay memory is a practical and effective mechanism for task-free federated continual forecasting.

---


### 202. [Acceptance and Responsibility Attribution Toward Autonomous Ambulances Across Driving Conditions: A Preliminary Survey of Fire Service Personnel](https://arxiv.org/abs/2611.01132)

**<font color=#1a73e8>作者：</font>** Hirotake Yamazoe, Shingo Yamaguchi  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Traffic incidents involving ambulances and fire engines during emergency-response driving can have serious consequences. Although autonomous driving technologies may reduce workload and improve safety, their introduction into emergency services requires consideration of first responders' trust, willingness to ride (WTR), and perceptions of responsibility. We surveyed 34 fire service personnel from a single fire station in Himeji, Japan, to examine their evaluations of autonomous ambulances and responsibility attribution under non-emergency and emergency driving conditions. Emergency driving was associated with lower perceived usefulness for improving safety, trust, and WTR, as well as greater anxiety. In contrast, responsibility attribution remained largely stable, with 30 participants ($88.2\%$) selecting the same primary responsible party across conditions and the onboard crew most frequently selected in both. Among these 30 participants, 26 ($86.7\%$) also assigned the same responsibility share. Open-ended responses revealed concerns about system reliability, the complexity of emergency driving, and the need for human judgment, as well as considerations regarding operator and organizational responsibility. These findings suggest that acceptance of autonomous ambulances is sensitive to driving conditions, while responsibility judgments may also reflect perceived professional roles and responsibilities.

---


### 203. [World Models Need Not Be Right to Rank Policies Right: Relative Bounds and Audit Limits](https://arxiv.org/abs/2611.01139)

**<font color=#1a73e8>作者：</font>** Ahanaf Hasan Ariq, Hasaan Ahmad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Selecting a reinforcement-learning (RL) policy usually requires additional environment interaction, while learned world models offer cheap but potentially biased evaluations. This raises two distinct questions: can shared model errors preserve pairwise rankings despite poor absolute values, and do they make a small number of real audits more informative? We derive an exact pairwise simulation identity and a relative bound separating common-mode Bellman residuals from policy-specific error. The analysis motivates RAVEL (Relative Auditing of Value Errors in Learned models), a selective policy tournament whose eliminations use held-out real outcomes. We test 45 SAC, TD3, and PPO policies per task in DMC cheetah-run and walker-walk. At rollout horizon 500, model rankings remain strong (Kendall tau = 0.962 and 0.800), and same-run differential-error ratios are 0.674 and 0.106. Yet mean paired audit-error correlations are only 0.007 and 0.090, and pairing changes standard deviation by -2.5 percent and +1.9 percent. Simultaneous intervals attain 99.98 percent and 99.75 percent coverage, but certify only 13.2 percent and 0 percent of decisions at eight audits. RAVEL improves low-budget walker-walk regret, whereas real-only successive halving is better at the largest budget, rejecting the precommitted twofold efficiency target. Frozen-model optimization lowers real return without increasing predicted return on average. Thus ranking fidelity, useful audit covariance, and upward model exploitation are distinct properties, separated in part by closed-loop trajectory divergence.

---


### 204. [EMG-Hybrid: A Dual-Engine Elite Memory--Guided Adaptive Optimization Framework for High-Dimensional Feature Selection](https://arxiv.org/abs/2611.01140)

**<font color=#1a73e8>作者：</font>** Saba Zare, Mohammad Taheri  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Feature selection in ultra-high-dimensional, noisy datasets remains a critical challenge due to exponential search space growth, where conventional binary metaheuristics often suffer from premature convergence. To address this, EMG-Hybrid is introduced as a novel three-level hierarchical optimization architecture designed around decoupled operational planes, feedback-driven scheduling, and isolated state refinement. At Level 1, a Dual-Engine Controller monitors population Shannon entropy and empirical fitness velocity, functioning as an architectural master-switch that dynamically routes execution between global exploration and local intensification. This control loop conditions the Level 2 active optimization plane, where an Adaptive Black Hole Gravity (ABHG) execution layer performs aggressive feature manifold pruning via a distance-decoupled penalty kernel driven by fitness similarities and Hamming metrics. To structurally isolate macro-exploration from micro-exploitation, Level 3 encapsulates an autonomous Elite Memory Archive that preserves high-fidelity sub-schemas and hosts a discrete bitwise Differential Evolution (DE) micro-refinement sandbox for resolving complex parameter epistasis. Theoretically, uniform combinatorial bounds derived via Vapnik--Chervonenkis (VC) dimension criteria demonstrate that this multi-level restriction mitigates high-dimensional overfitting. Empirical results across manifolds scaling up to $d > 100{,}000$ features, complemented by high-performance computing (HPC) profiling under lock-free atomic Compare-and-Swap (CAS) primitives, indicate strong performance gains over state-of-the-art baselines. The framework exhibits near-linear parallel speedups, sub-quadratic runtime scaling, and substantial dimensionality reduction, offering a scalable and structurally innovative paradigm for large-scale data mining.

---


### 205. [Side-Channel Attack Prevention for Post Quantum Cryptography Algorithms: A 3D-Shield Approach](https://arxiv.org/abs/2611.01144)

**<font color=#1a73e8>作者：</font>** Carl Benda, Eren Kurshan, Aydin Aysu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Despite their theoretical quantum attack resistance, practical implementations of post-quantum cryptography (PQC) algorithms remain susceptible to side-channel attacks. This includes all standard algorithms selected the National Institute of Standards and Technology (NIST) such as Kyber/ML-KEM, Dilithium/ML-DSA, Falcon/FN-DSA and SPHINCS+/SLH-DSA. This paper proposes an alternative defense for side-channel resilience based on 3D integration that uses 3D hardware to shield the underlying cryptographic activity by introducing decoy keys and physical shielding through stacking. The proposed approach can complement other security measures (such as masking and shuffling) on protecting Number Theoretic Transform (NTT) that move computation to dedicated NTT chips. We outline the construction of our approach and validate the effectiveness on a generic attack targeting intermediate computation inside an NTT butterfly.

---


### 206. [Enhancing Edge AI System Security with a Stacked Hardware Security Controller for Robust and Energy-Efficient Anomaly Detectio](https://arxiv.org/abs/2611.01150)

**<font color=#1a73e8>作者：</font>** Carl Benda, Eren Kurshan, Paul Franzon  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In recent years, the growing adoption of Edge AI systems has been accompanied by a surge in security threats. Edge AI deployments face an rapidly evolving spectrum of security threats, from side-channel information leakage to ad- versarial model manipulation and physical device tampering. Conventional security mechanisms such as malware scanners and resource-intensive firewall solutions are unsuitable due to edge AIs typically limited computational resources, strict energy budgets and thermal constraints especially in battery-powered and field-deployed environments. This paper proposes a stacked, hardware-based security mechanism that enables low-overhead, continuous detection of anomalous execution patterns. Anomaly detection utilizing hard- ware performance counters and physical sensors outperforms software-based alternatives by providing key capabilities such as tamper-resistant root-of-trust isolation, negligible runtime overhead, and resilience against compromised operating systems. Experimental analysis shows that adversarial or malicious ap- plications produce observable deviations in sensor and thermal readings on Edge AI systems and hardware-based anomaly detection provides effective and low-overhead anomaly detection.

---


### 207. [SHield: Watermarking 4D Gaussian Splatting via Spherical Harmonic Coefficient Perturbation](https://arxiv.org/abs/2611.01162)

**<font color=#1a73e8>作者：</font>** Kunal Bhosikar, Prajas Wadekar, Venkata Sai Pranav Bachina 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 4D Gaussian Splatting (4DGS) models are computationally expensive to train but distributed as easily copied parameter files. Existing watermarks protect these assets by fine-tuning the scene against a neural decoder to extract bit strings from rendered video, a heavy process vulnerable to the temporal dynamics of dynamic scenes. However, if the threat model targets the redistributed file itself, verification can be vastly simplified. Because the canonical Spherical-Harmonic (SH) coefficients of 4DGS are time- and view-invariant, parameter-space perturbations can be recovered via deterministic arithmetic. We propose **SHield**, the first non-blind, decoder-free watermarking approach that natively embeds full-resolution RGB images into 4DGS files. SHield tiles a zero-mean payload across the SH coefficients of a key-selected Gaussian subset, applying a brief anchored optimization to preserve visual fidelity. To verify ownership, it geometrically re-associates the key using canonical Gaussian centres to survive file tampering and recovers the payload in closed form. Across 30 scenes (D-NeRF, HyperNeRF, DyNeRF), SHield guarantees near-perfect payload recovery (Pearson $r \geq 0.991$) on all 150 tested models with a mean rendering penalty of $\leq 0.13$~dB. Held-out evaluation yields perfect detection on 400 true trials and zero false positives across $1{,}600$ wrong-subset null trials. We also strictly bound the method's robustness: SHield survives INT8 quantization and $30\%$ opacity pruning for the image payload, and on aggressive SH-degree-1 truncation bit payloads are still decodable.

---


### 208. [Lightweight Representation Learning for Low Tucker Rank Tensors](https://arxiv.org/abs/2611.01168)

**<font color=#1a73e8>作者：</font>** Hiroki Hasegawa, Yukihiko Okada  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low Tucker rank tensors provide compact representations of multidimensional dependencies, but standard learning pipelines can incur substantial computational and memory overhead from redundant intermediate quantities. We reduce this overhead without modifying the underlying representation objective or parameterization. Our approach combines three complementary components: (i) sequential extraction of only task-required spectral components, avoiding unnecessary full decompositions; (ii) factor-wise multilinear contractions without materializing large Kronecker operators; and (iii) compact latent-state updates without storing full ambient tensor iterates. These components preserve the algebraic operations and learning trajectories of the original algorithms while reducing their computational and memory footprints. Across five low Tucker rank tensor estimators, our implementations match the original trajectories to numerical precision (relative discrepancies of $10^{-16}$ to $10^{-13}$), while reducing per-iteration runtime by up to $3.12\times$ and resident memory by up to $616\times$ ($99.8\%$) on the main order-3 benchmark at $n=100$, with memory reductions exceeding $900\times$ across the full evaluation suite. These results show that substantial computational redundancy can be eliminated from Tucker representation learning without changing the underlying model or learned representation.

---


### 209. [Fast and Exact Relative-Position Attention via Structure-Aware Kernels](https://arxiv.org/abs/2611.01182)

**<font color=#1a73e8>作者：</font>** Delyan Boychev, Ivo Petrov, Dimitar I. Dimitrov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Relative-position attention mechanisms offer compelling alternatives to RoPE across various transformer architectures, delivering superior performance in domains such as audio. These mechanisms typically modify attention scores by adding content-position or bias-position terms. Unlike RoPE, which encodes position via per-token rotations directly on the queries and keys, relative-position terms generally require pairwise offset-dependent computation or lookups, complicating their integration into fused attention kernels and introducing severe memory, bandwidth, and compute overheads as sequences scale. To address this bottleneck, we propose an exact attention algorithm that incorporates additive relative-position terms into FlashAttention-style tiled computation. Our method (1) uses offset-aware tiling to avoid redundant indexing and memory accesses, (2) computes only the necessary key/query-relation products and reuses them across token pairs in both forward and backward passes, and (3) uses offset-based gradient sharding and aggregation, eliminating atomic contention. We provide a unified, efficient Triton implementation across diverse relative-position attention mechanisms and evaluate it against naive and specialized implementations. For 8K-token sequences, our method speeds up the forward (backward) pass by 1.8-6.4$\times$ (2.0-21$\times$) and reduces peak memory up to 2.9-128$\times$ (1.4-54$\times$) over the strongest baseline for each mechanism, enabling long-context end-to-end transcription that is 1.8$\times$ faster and uses 2.4$\times$ less memory. Our method thus provides a drop-in, hardware-efficient solution for scaling relative-position attention transformers.

---


### 210. [Satisfied, Not Solving: Wireheading of Bounded Homeostatic Rewards in Reinforcement Learning](https://arxiv.org/abs/2611.01183)

**<font color=#1a73e8>作者：</font>** Chase J. Metoyer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bounded intrinsic rewards are often assumed to be safe from exploitation: if a signal can yield at most a fixed amount, gaming it should not pay. We test this for a homeostatic satiation reward, in which needs build up and relieving them is rewarding, and give the agent a cheap action that resets its needs. In MiniGrid DoorKey-8x8, PPO agents with this action solved 2 of 80 seeds, against 71 of 80 on the same seeds without it; in KeyCorridorS3R1, 0 of 20 against 20 of 20. Their policies stayed near uniform. The reward does not ask for this: a telescoping argument caps any policy's satiation return at the needs' starting drive, and a post-hoc computation shows that, at every growth rate we trained, a solving trajectory beats that cap on all sampled layouts. In DoorKey with advantage normalization on, a satisfaction signal the agent could fill itself was worse than none (11 of 20 solved with task reward alone, 1 of 20 with the tamperable signal), and a per-press cost of 0.1 restored the task in every seed. Farming of positive reward cycles appeared in DoorKey but not persistently in KeyCorridorS3R1. All predictions were pre-registered, and hash-locked from round 3 on; 9 of our 23 hypotheses were not supported, and we report each.

---


### 211. [Zeroth-Order Policy Optimization for Scheduling in Queueing Networks](https://arxiv.org/abs/2611.01186)

**<font color=#1a73e8>作者：</font>** Deyi Wang, Qining Zhang, Lei Ying  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning in queueing network scheduling presents significant challenges because of the countably infinite state space and the high stochasticity in transitions. In this paper, we propose zeroth-order policy optimization algorithms that are easy to implement and rely solely on estimates of the average cost, a single scalar quantity, without requiring the estimation of value or advantage functions. Our analysis focuses on back-pressure guarded policies and establishes uniform smoothness of the average cost objective with respect to the policy parameters. Building on this property, we establish finite-time convergence guarantees to an $\epsilon$-stationary policy for the proposed algorithms. Numerical experiments on multiple queueing networks, including systems beyond classical exponential service distribution, demonstrate competitive performance, outperforming gradient-based RL methods like PPO and traditional queueing baselines.

---


### 212. [ArSciKids: Arabic Curriculum-Aligned Datasets for Scientific Experiment and Multiple-Choice Question Generation in Primary Education](https://arxiv.org/abs/2611.01191)

**<font color=#1a73e8>作者：</font>** Taghrid Housari, Massa Rankoussi, Jafar Abdul Majeed 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite growing interest in Arabic natural language processing, curriculum-aligned educational resources remain scarce compared with English, and few public datasets for Arabic curriculum content with structured, generation-ready annotations are available, particularly for primary-school science. We introduce ArSciKids, a collection of two Arabic datasets designed for curriculum-aligned educational content generation: (1) a scientific-experiments dataset containing 999 manually curated records from official primary-school science textbooks in Saudi Arabia, Syria, and Jordan, and (2) an assessment-question dataset containing 2,167 multiple-choice questions collected from the Saudi Manhaji educational platform. The experiment records are structured with titles, objectives, tools, procedures, observations, conclusions, keywords, and grade levels, while the assessment records contain lesson references, questions, four answer options, correct answers, and explanations. Both datasets cover grades 1-6 and consist of real-life Arabic educational content rather than machine-translated or synthetically generated material. We assess the usefulness of these resources for generation by fine-tuning ten open models spanning sub-billion to several-billion parameter scales using LoRA. Models are evaluated using automatic metrics, including ROUGE and BLEU, and answer accuracy for multiple-choice generation. Moreover, we evaluate the results using a five-criterion human evaluation protocol. The results show substantial differences across model scales and tasks. ArSciKids will be publicly available, and we hope that it provides a manually curated, structured foundation for research on Arabic educational NLP, curriculum-aware generation, and low-resource language modeling.

---


### 213. [Projecting the Public: Reflections and Recommendations for Empirical Visualization Studies of General Audiences](https://arxiv.org/abs/2611.01198)

**<font color=#1a73e8>作者：</font>** Mandi Cai, Jack McNiel, Erik C. Nisbet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Calls for shifting visualization research to general audiences outside of professional contexts have been put forward since the early 2000s, but expanding outwards means contending with a diversity in visualization's communicative purpose beyond transmitting insights from data. After our own experiences studying public-facing visualizations, we sought a set of considerations to help early-career visualization researchers reason through designing empirical visualization studies for the general public that confronts the various ways visualizations are interpreted. We examined literature on guiding paradigms of research, reviewed 73 visualization papers that specify a focus on audiences broader than domain experts, and conducted 15 semi-structured interviews with authors of such papers, to derive the following: (1) a conceptualization of any experiment as 3 elements-casting audience, constructing experimental setting, and projecting audience impressions and interactions into measurable constructs (2) an account of interviewees' aspirations for each element of study design, versus the real challenges that occurred. We detail their approaches to navigate the gaps between aspirations and reality when working with general audiences and summarize them as actionable recommendations. The conceptual framework is intended to help junior researchers scope and outline experimental designs of visualizations "for the masses", while the recommendations provide concrete guidance for putting those designs into practice. The 73 papers are filterable and visualized on our study website, and our code to sample the papers is on GitHub.

---


### 214. [GraCo: A Unified Toolkit of Graph Coarsening Algorithms and Metrics](https://arxiv.org/abs/2611.01200)

**<font color=#1a73e8>作者：</font>** Antonin Joly  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph coarsening aims to reduce a graph to a smaller one that preserves chosen properties of the original. It is increasingly used to scale graph learning to large graphs, as a non-differentiable step applied once before training. Many coarsening methods have been proposed in recent years, each with its own implementation, notation and evaluation. In this work, we introduce GraCo, a unified toolkit of graph coarsening methods. It relies on a single definition: a coarsening is fixed by a partition of the nodes and by the Laplacian the coarsened graph is consistent with. The coarsened graph, and the reduction and lifting matrices that map signals from the original graph to the coarsened one and back, follow from these two choices. We implement 17 methods from the literature and a random baseline, grouped into five families, with the same notation, inputs and outputs. We also build a collection of metrics from different papers, applicable to any coarsening. We check the implementations on a synthetic stochastic block model, then we report the runtime and peak memory of each method on Cora, PubMed, ogbn-arxiv and ogbn-products. GraCo is open-source and available at this https URL.

---


### 215. [A Batched Hartigan's $k$-Means Clustering](https://arxiv.org/abs/2611.01207)

**<font color=#1a73e8>作者：</font>** Edward Raff, Michael Slawinski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hartigan's $k$-means algorithm has theoretical advantages over the standard Lloyd's variant, which has become synonymous with "$k$-means". Yet, Hartigan's algorithm is far slower in practice due to its inherently sequential calculations. We devise a Batched Hartigan's method that enables vectorized calculation by exploiting the triangle inequality to expose a set of parallel-safe updates and a smaller set of sequential updates. This makes Hartigan's method competitive with Lloyd's in execution speed for the first time.

---


### 216. [A Large-Scale Evaluation of Cookie Notice Privacy and Accessibility for Blind and Low Vision Users](https://arxiv.org/abs/2611.01211)

**<font color=#1a73e8>作者：</font>** James M. Clarke, Maryam Mehrnezhad  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present the first large-scale privacy and accessibility evaluation of cookie notices across 2,061 domains for blind and low vision (BLV) users. Using a Playwright-based crawler, a custom NVDA screen reader add-on, and the Lighthouse and WAVE accessibility tools, we measure UK GDPR/PECR compliance, tracker activity across pre-interaction, post-accept, and post-reject phases, and cookie notice accessibility for screen reader users. We find that 51 % of sites display a cookie notice, of which (at least) 50 % violate UK GDPR/PECR requirements. Accepting a notice produces a mean five-fold increase in tracker activity, and degrades page landmark structure on one in five sites. While 95 % of notices are readable by a screen reader, only 37 % carry a meaningful title, 39 % are announced immediately on page load, and 42 % use descriptive button labels. We reveal a systemic correlation: cookie notices failing legal privacy requirements disproportionately exhibit the weakest screen reader accessibility. This compounding privacy burden on BLV users demands urgent intervention from developers, regulators, and standards bodies.

---


### 217. [Optimal Conversion from Zero-Concentrated to Gaussian Differential Privacy](https://arxiv.org/abs/2611.01218)

**<font color=#1a73e8>作者：</font>** Yu-Wei Chen, Aaradhya Pandey, Jordan Awan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Gaussian differential privacy (GDP) and zero-concentrated differential privacy (zCDP) are two competing privacy accounting frameworks, but they share similar minimax lower bounds in various estimation problems. Moreover, it is known that a mechanism satisfying $\mu$-GDP satisfies $(\mu^2/2)$-zCDP, whereas the converse fails to hold at the same calibration. In this paper, we establish the optimal reverse conversion, showing that every $\rho$-zCDP mechanism satisfies $\mu_{\mathrm{zCDP}}(\rho)$-GDP, where $\mu_{\mathrm{zCDP}}(\rho)=2\Phi^{-1}((1+e^{-t_\rho})^{-1})$ and $t_\rho$ uniquely solves the equation $\rho=t_\rho\tanh(t_\rho/2)$. We also obtain simplified bounds $\sqrt{\pi\rho}\leq\mu_{\mathrm{zCDP}}(\rho)\leq\sqrt{8\rho}$, with sharp constants, which imply equivalence of the two frameworks up to constants. This explains why their minimax risks agree up to a constant rescaling of the privacy budget. We show that the squared conversion is strictly convex, which implies that converting zCDP to GDP before applying composition or group privacy yields a tighter GDP guarantee than converting afterward. We also derive the sharp conversion from bounded-range and logistic DP mechanisms (e.g., exponential mechanism) to GDP, where converting before composition but after group privacy gives the tighter guarantee.

---


### 218. [Modeling Fat-shift for Improved Head Segmentation from MRI Scans using a Probabilistic Model](https://arxiv.org/abs/2611.01222)

**<font color=#1a73e8>作者：</font>** Merle Diedrichsen, Koen Van Leemput, Douglas N. Greve 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Personalized computational head models for biophysical simulations rely on accurate whole-head segmentations from T1-weighted (T1w) magnetic resonance imaging (MRI) scans. While T1w scans provide excellent contrast for intracranial anatomy, extracerebral tissues have partly almost no signal (compact bone) and also suffer from the so-called chemical shift artifact, which affects the fatty tissues in MRI and causes them to spatially shift in the frequency encoding direction of the scan. This artifact occurs primarily in two structures of the head: the spongy bone, a fatty compartment inside the compact bone, and the subcutaneous fat, located directly underneath the skin. The frequency-encoding direction is often set in the superior-inferior direction, causing the fatty tissues to shift down and, as a result, making the skull appear thinner than it actually is. Existing segmentation methods do not model this artifact, consequently leading to inaccurate labeling of the skull and scalp, which introduces a bias in biophysical simulations. The direction and magnitude of the fat-shift can be determined from the scan parameters, thus making it possible to explicitly model the shift and to recover the correct anatomy. This study introduces a probabilistic model that uses variational inference to segment head and brain structures from a T1w scan while accounting for the fat-shift artifact. The proposed Fat-shift-informed Label Optimization of the Whole head (FLOW) method reconstructs extracerebral anatomy more accurately than a fat-shift-agnostic segmentation approach while maintaining high segmentation accuracy in all other structures. FLOW-based fat-shift corrected segmentations significantly reduce bias in electric field simulations compared to a segmentation method that does not model the shift.

---


### 219. [When Benign Is Unverified: Label-Signal Mismatch and Abstention-First Triage in Graph-Based Memory Forensics](https://arxiv.org/abs/2611.01225)

**<font color=#1a73e8>作者：</font>** Viraj Rajeshbhai Chudasama, Eduardo Palmieri, Dipo Dunsin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine-learning triage for memory forensics is usually validated on corpora whose benign class is asserted by provenance and never verified. We report a validation study of a graph-based triage pipeline for Windows memory images: Volatility 3 output is compiled into typed heterogeneous graphs and scored by a temperature-scaled GINE classifier and two one-class encoders, fused with rule risk under an abstention gate. On MalVol-25 a transparent rule layer contradicts the benign label on every control (15/15 and 18/18 flagged; at least 11 of 15 paired controls rated HIGH or CRITICAL), and mean injection and command-and-control counts run higher on controls than on infected captures. We call this rule-label discordance label-signal mismatch; it shows the benign class is unverified, not compromised. Leave-one-family-out AUROC over matched pairs is provably three-valued, so a reported mean and standard deviation identify the fold composition. The learned model (0.786 +- 0.311; 9/4/1, scored in-sample by a frozen checkpoint) equals a logistic model over rule-derived attributes (0.786 +- 0.410; 11/0/3) in mean only, and its significance rests on dropping four saturated ties. The fusion path sends 97.7% of snapshots to analyst review, 95.3% with every gate disabled. Two public feature-level corpora show the same defect: on CIC-MalMem-2022 every benign row carries injected regions and one host-population feature reaches AUROC 0.997 under leave-one-family-out validation; on the Sihwail et al. (2021) sample the injection indicator fires on 53% of benign rows. We close with seven reporting artefacts for learned triage on corpora whose ground truth is asserted.

---


### 220. [Precision Through Play: Enhancing Fundamental Laparoscopic Skill Acquisition Via Gamified XR and Pseudo-Haptics](https://arxiv.org/abs/2611.01229)

**<font color=#1a73e8>作者：</font>** Bita koohestani, Ashkan Rezaei, Azam Bastanfard  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Extended Reality (XR) technologies have shown potential to improve laparoscopic skills acquisition. Among fundamental skills in laparoscopic surgery is accurate instrument handling. Appropriate instrument alignment and a perpendicular path ensure movement efficiency and improved performance. This work introduces an interactive XR platform designed to support an immersive, engaging, and accessible environment that facilitates continuous practice. This platform incorporates a gamification layer enriched by pseudo-haptics that generate a motivational feedback loop, allowing trainees to continuously practice instrument manipulation and angle control. The platform monitors instrument orientation, computes angular deviation from an ideal reference vector, and assigns scores based on user performance. A point-based scoring component reinforces correct technique and penalizes deviations in tool alignment beyond predefined thresholds. Furthermore, a pseudo-haptic feedback mechanism is integrated to provide real-time tactile feedback when deviation exceeds tolerance. Combined with low-cost hardware and accessible deployment, the framework aims to increase training scalability, engagement, and improve skill acquisition. Preliminary evaluations indicate that integrating gamified feedback significantly improves precision, reduces angular variance, and encourages sustained practice.

---


### 221. [Reproducing INP-Former: Reconstructing Intrinsic Normal Prototypes for Industrial Anomaly Detection](https://arxiv.org/abs/2611.01230)

**<font color=#1a73e8>作者：</font>** Yunfei Liang, Juan Pablo Osorio Rivera  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We reproduce the central claims of INP-Former, a reconstruction-based method for multi-class industrial anomaly detection. INP-Former extracts Intrinsic Normal Prototypes (INPs) from each test image and uses them to guide a decoder that reconstructs normal features, without a stored memory bank. Using the authors' released code, we reproduce the reported performance on MVTec AD and VisA and extend the evaluation to MVTec AD 2, where image AUROC with the default settings is 63.4, compared with 99.7 on MVTec AD. On MVTec AD, a five-seed ablation shows that most of the performance comes from the INP mechanism, while the two auxiliary losses add small changes whose direction depends on the metric. A paired comparison with both losses disabled confirms the benefit of INP on MVTec AD 2. The default of six prototypes transfers less well: the plateau beyond four prototypes reproduces on MVTec AD and VisA, but on MVTec AD 2 a single prototype outperforms six in AU-PRO on the public split and on both hidden test splits. We also measure practical trade-offs in resolution, backbone size, training length, and LoRA adaptation, and examine performance by defect size, lighting condition, and a stricter AU-PRO limit. Several conclusions from the original benchmarks, including the default prototype count, do not carry over to harder data. Code: this https URL

---


### 222. [Mathematical Formulation and Comparative Performance Evaluation of Machine Learning Algorithms for Maize Land Suitability Prediction](https://arxiv.org/abs/2611.01239)

**<font color=#1a73e8>作者：</font>** Haimanot Bitew, Ayisheshim Almaw, Habtamu Zegeye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Addressing the food needs of a growing population is one of the major challenges of developing countries like Ethiopia. Various policies aimed at increasing food production have been enacted by governments and development partners. Although efforts in this regard have been made, there is still inadequate emphasis on increasing food production through the use of high technology practices. Precision agriculture using technology has been utilized to increase crop yield. Precision agriculture also relies on identifying land for a crop, which is a key factor that affects crop yield. Traditional methods of assessing land suitability for crop production are time-consuming, costly and unreliable. Against this background, the aim of this study was to assess the potential of machine learning (ML) in improving the speed and accuracy of assessing land suitability for maize, a staple crop in Ethiopia, as compared to traditional methods. The study is investigated in three areas (Burie, Shindi and Tilili) in the Amhara region. Data collection was done through the local agriculture offices and survey teams. The data were coded, scaled and balanced. Various feature extraction techniques, which included Univariate Feature Selection(UFS), Recursive Feature Elimination with Cross-Validation(RFECV) and Sequential Feature Selection(SFS), and various classifiers, which were K-nearest neighbor (KNN), gradient boosting (GB),random forest (RF) with mathematical formulations were employed. The best models were constructed through combining GBOOST and SFS and achieved an accuracy of 99.41% and 99.35% for both precision and recall. Our results showed that using machine learning is a reliable method of assessing land suitability for maize in Ethiopia.
Keywords: Maize, Gradient boosting,Land suitability,Machine learning, Mathematical formulations

---


### 223. [MedAstra: ASR-less Speech Retrieval with Diagnostic Grounding for Medical QA](https://arxiv.org/abs/2611.01261)

**<font color=#1a73e8>作者：</font>** Elahe Khatibi, Ziyu Wang, Amir M. Rahmani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Spoken medical question answering can fail when automatic speech recognition (ASR) corrupts a clinically important term before retrieval. We present MedAstra, a framework that maps frozen WavLM speech representations through a lightweight adapter into a frozen E5 text embedding space. This enables a dense retrieval path that accepts a waveform without a query transcript. Retrieved passages and speech-linked textual metadata support answer generation with entity alternatives, diagnostic contrasts, relation heuristics, and bounded retrieval refinement. ASR-less refers to the initial speech retrieval interface; lexical retrieval, string-based entity correction, and the text generator require textual inputs. The deterministic speech embedding does not constitute a calibrated model of acoustic uncertainty. Reported retrieval results reach 87.6 Recall@10 for the speech-only retriever and 90.4 for the hybrid configuration, compared with 81.0 for transcript-first dense retrieval. Medical QA and ablations provide descriptive system comparisons, with input-provenance and evaluation limitations stated explicitly. We distinguish controlled synthetic acoustic tests from real clinical speech, qualify component attribution, and specify the remaining comparisons needed to assess speech-only QA and clinical generalization.

---


### 224. [Does Random Search Discover Task Experts? Revisiting Neural Thickets](https://arxiv.org/abs/2611.01262)

**<font color=#1a73e8>作者：</font>** Julian Asilis, Guanzhe Hong, Vatsal Sharan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretrained models are typically viewed as generalists, requiring bespoke post-training to achieve task-specific expertise. Gan & Isola (2026) recently proposed a striking alternative: that pretrained models lie in a dense neural thicket of task specialists, which can be surfaced with simple Gaussian weight perturbations. We examine this neural thicket of task-specific experts and identify several key findings that question this perspective. First, we find that the apparent lift of the best-of-N selected perturbation decays quickly with selection-set size m, strongly suggesting overfitting to the selection questions. In fact, for 10 of the 12 model-task pairs we study, a simple null model of pure selection noise predicts more than 75 percent of the top expert's reward lift. Second, the top experts' advantage often vanishes on held-out questions or remains within the run-to-run variability of the unperturbed pretrained model. Third, we find that majority voting over the top-K selected perturbations, termed RandOpt(N, K) by Gan & Isola (2026), is often matched or outperformed by majority voting over K samples from the base model. Overall, our results suggest that random weight perturbations may be ineffective at uncovering task experts around pretrained models, and that task adaptation requires more sophistication than random search. Code and artifacts are available at this http URL.

---


### 225. [EZ-Ar-VC: Robust Arabic Voice Anonymization with Generalization across Dialects and Code-Switching](https://arxiv.org/abs/2611.01268)

**<font color=#1a73e8>作者：</font>** Injy Hamed, Adarsh Arigala, Rufael Marew 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Voice conversion (VC) models can be used to anonymize speech data while preserving naturalness. Existing models, however, are mainly optimized for English and other high-resource languages, and they fail to generalize well to Arabic due to its distinct phonology. In this work, we comprehensively evaluate existing zero-shot VC systems for Arabic speech, identifying limitations in pronunciation preservation. We then train an Arabic-centric model based on EZ-VC on diverse Arabic speech, and demonstrate strong performance in intelligibility, naturalness, and pronunciation preservation, while maintaining high speaker dissimilarity. Through subjective evaluation, we further demonstrate its robustness to code-switching and cross-dialectal conversion, as well as its generalization to Arabic dialects with limited representation in the training data. Our findings highlight the limitations of zero-shot VC and the importance of target-language adaptation for robust voice anonymization.

---


### 226. [Learning momenta for Hamiltonian-based models](https://arxiv.org/abs/2611.01269)

**<font color=#1a73e8>作者：</font>** Ignacio Puiggros T., A. Srikantha Phani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> There has been increasing interest in methodologies that incorporate physics priors into neural network architectures to enhance their modeling capabilities. Among these methodologies, Hamiltonian neural networks (HNNs) and their variants have gained considerable attention. These architectures explicitly encode Hamiltonian mechanics both in their structure and loss function, resulting in desirable properties and additional modeled information. A crucial limitation of HNNs is their reliance on data on the target system's generalized momenta. This severely hampers their applicability when the analytical form of the generalized momenta is unknown, which frequently is the case in real-world applications. The goal of the present work is to develop a general extension of Hamiltonian-based architectures that addresses this issue by simultaneously learning the system's generalized momenta, Hamiltonian structure, and dynamics from data. The proposed architecture learns the generalized momenta when their analytical form is unknown, and only (potentially non-sequential) data on the state and its derivatives is available. A dissipative mass-spring system, a double pendulum, and a rolling disk under nonholonomic constraints are considered as canonical examples to assess the performance of the proposed architecture.

---


### 227. [DriftingPlanner: Drifting Generative Models for One-Step Trajectory Planning in End-to-End Autonomous Driving](https://arxiv.org/abs/2611.01283)

**<font color=#1a73e8>作者：</font>** Ziming Liu, Yizhan Qu, Leichen Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end planners decode the ego trajectory either by coordinate regression, which is fast but blends plausible maneuvers into one trajectory that may follow none of them, or by diffusion and flow matching, which model the trajectory distribution but need several inference steps. Drifting models move this iteration into training: a one-step generator learns to follow an attraction--repulsion field between generated and ground-truth samples. Drifting was developed for class-conditional image generation, where every class supplies many positive samples. In planning, every scene is its own condition. Pooling scenes would attract the generated trajectories of one scene to the ground truth of unrelated scenes, whereas computing the field per scene leaves a single positive, the expert trajectory. Mutual repulsion then holds the generated trajectories on a shell around it, so any single generated trajectory deviates from the ground truth. We present DriftingPlanner, a trajectory planner trained with the drifting loss alone, without any coordinate regression term. It computes the field per scene and removes the shell at inference: it decodes every noise vector together with its negation in one batched pass, and averaging each antithetic pair cancels the linear part of the displacement from the shell center. On NAVSIM navtest, DriftingPlanner reaches a state-of-the-art 93.75 PDMS, and with single-step inference its drifting decoder comes within 0.13 PDMS of the best diffusion or flow matching setting, which needs ten inference steps.

---


### 228. [[Re] Pure Noise to the Rescue of Insufficient Data](https://arxiv.org/abs/2611.01295)

**<font color=#1a73e8>作者：</font>** Seungjae Ryan Lee, Seungmin Brian Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We examine the main claims of Zada, Benou, and Irani (2021), which states that in an image classification task with imbalanced training data, (i) using pure noise to augment minority-class images encourages generalization by improving minority-class accuracy. This method is paired with (ii) a new batch normalization layer that normalizes noise images using affine parameters learned from natural images, which improves the model's performance. Moreover, (iii) this improvement is robust to varying levels of data augmentation. Finally, the authors propose that (iv) adding pure noise images can improve classification even on balanced training data. We implemented the training pipeline from the description of the paper using PyTorch and integrated authors' code snippets for sampling pure noise images and batch normalizing noise and natural images separately. We reproduced the main claims that (i) oversampling with pure noise improves generalization by improving the minority-class accuracy, (ii) the proposed batch normalization (BN) method outperforms baselines, (iii) and this improvement is robust across data augmentations. Our results also support that (iv) adding pure noise images can improve classification on balanced training data. However, additional experiments suggest that the performance improvement from OPeN may be more orthogonal to the improvement caused by a bigger network or more complex data augmentation.

---


### 229. [Best-of-Both-Worlds FTRL for Linear Bandits: The Interplay of Information Acquisition, Corruption, and Geometry](https://arxiv.org/abs/2611.01299)

**<font color=#1a73e8>作者：</font>** Canzhe Zhao, Vincent Y. F. Tan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study \textit{best-of-both-worlds} (BOBW) algorithms for linear bandits, which aim to simultaneously guarantee $\gO(\sqrt T)$ regret in the adversarial regime and $\gO(\log T)$ regret in the stochastic regime over $T$ rounds. For finite action sets, we introduce \emph{information-acquisition follow-the-regularized-leader} (\IAFTRL{}), the first BOBW algorithm based purely on the follow-the-regularized-leader (FTRL) framework that attains an $\gO(\cstar\log T)$-type regret in the stochastic regime, where $\cstar$ is the information-acquisition complexity that characterizes instance-dependent optimality in linear bandits, while retaining the $\gO(\sqrt{T})$ regret guarantee in the adversarial regime. This resolves the open problem posed in~\cite{LeeEtAl2021,KongZ023,ItoT23,ZhaoItoLi2025}.

---


### 230. [Accelerating posterior sampling in Bayesian inverse problems with diffusion models: an online-offline perspective](https://arxiv.org/abs/2611.01300)

**<font color=#1a73e8>作者：</font>** Duc-Lam Duong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian inverse problems require both informative prior models and computationally feasible posterior inference. Score-based diffusion models provide expressive learned priors, but their use for inversion introduces a conditioning problem: the score of a noised posterior is generally unavailable from a prior score alone. This selective survey reviews the principal approaches to that problem, including likelihood guidance, spectral and projection methods, sequential Monte Carlo corrections, and amortized conditional training. We organize methods by how they split cost between offline preparation and online inference, and compare their assumptions, advantages and limitations, with emphasis on computational speedups. Some ongoing directions and open questions are gathered at the end.

---


### 231. [Inferring missing locations in human mobility data using memory effects](https://arxiv.org/abs/2611.01319)

**<font color=#1a73e8>作者：</font>** Pablo Rosillo-Rodes, Antònia Tugores, David Sánchez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Empirical datasets used to characterize human mobility are sparse in space and time, owing to technological factors such as coverage and battery, or to the erratic nature of online interactions. Missing data can bias the conclusions drawn from them, so filling the gaps in incomplete timelines is a key challenge in computational social science. Here, we propose a simple imputation method in which the informativeness of an observation decays with its bidirectional temporal distance from the missing entry, at a rate set by a single parameter per individual. On synthetic and real Twitter data, a power-law decay, selected by Bayesian model comparison, yields accurate imputations (macro-AUROC above 0.9 overall, and above 0.8 for the most mobile users) and matches a gap-aware continuous-time Markov chain, outperforming it among the most mobile users. The method is robust to moderate noise and generalizes across countries and European administrative regions.

---


### 232. [Urban functional knowledge transfer through global representations amid uneven data](https://arxiv.org/abs/2611.01327)

**<font color=#1a73e8>作者：</font>** Junyuan Liu, Xinglei Wang, Guangsheng Dong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Urban functional observations are unevenly distributed worldwide, limiting analysis of how places are organised and used. AlphaEarth Foundations (AEF) provides a globally consistent physical representation. Whether this representation can support transfer of functional knowledge to locations with sparse or absent functional observations, and what governs transfer, remain unclear. We introduce POI-aligned Urban Embedding (PURE), which learns physical-functional relationships between POI-derived semantics and AEF. Across five urban analysis tasks covering 142 countries and territories, PURE increases mean $R^2$ from 0.792 to 0.830, with gains across widely different levels of POI availability. When target-city POIs are excluded, country-level alignment retains 87.9% of its performance gain. Cross-country experiments show that transfer is selective rather than universal, with larger gains between physically similar and geographically closer contexts, particularly among pairs within the same continent. Our findings reveal spatially structured urban functional knowledge transfer, offering a route to reduce reliance on dense local observations.

---


### 233. [Same Function, Different Mechanism: Implementation-Local Geometry Beyond Accuracy](https://arxiv.org/abs/2611.01328)

**<font color=#1a73e8>作者：</font>** Miroslav Lžičař  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Two models can make exactly the same predictions yet respond differently when their implementations are perturbed. A lookup table can change one case independently; a shared rule couples changes across cases. We compare these mechanisms through an implementation chart: a specified local family of logit perturbations around a fixed predictive distribution. Our main result counts the independent prediction changes allowed by exact finite-group sharing: the active dimension is the number of input-output orbits minus the number of input orbits. For softened modular addition, lookup and shared cyclic charts therefore have ranks $p^2(p-1)$ and $p-1$ despite identical predictions. The classical Fisher pullback connects these dimensions to local KL curvature; mechanism-preserving reparameterizations leave the rank unchanged. We also bound the spectral tail under approximate sharing and separate quadratic rank from higher-order learning coefficients. Trained modular-addition models verify that chart rank is measurable, while controlled compiled transformers distinguish compiler-supported intermediate charts from matched alternatives. Negative controls show where this discrimination fails. The framework evaluates specified mechanism hypotheses; it does not infer a unique mechanism from predictions or predict training dynamics.

---


### 234. [Profile-aware diagnostics of discarded parameter-Hessian mass](https://arxiv.org/abs/2611.01335)

**<font color=#1a73e8>作者：</font>** Maxim Bolshim, Alexander Kugaevskikh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A discarded parameter-Hessian fraction depends on the diagonal profile and parameter partition; it is not the Fisher information discarded by K-FAC. We compare off-block squared Frobenius mass with group-size and measured diagonal-profile references at specified weights, inputs and coordinates. Similar initial fractions in ResNet-18 and its skip-free twin accompany different profiles. On the same saved trained ResNet-18 states, changing from stage groups to layers moves estimated mass from below to above the profile envelope. An approximate joint conditional Monte Carlo screen resolves this crossing in 6/6 seed/input cells; the skip-free network has 2 resolved and 4 unresolved comparisons. A separate comparison of nine saved states under two geometry draws splits the full model residual into off-group Hessian action and its remainder: gradient, within-group action and damping. At unit correction scale, off-group input alone increases loss in 17 of 18 state-geometry comparisons; in nine of those cases, the full candidate has lower loss than the remainder-only candidate. After correction-norm matching, seven of the ten comparisons that initially favoured full favour the remainder. These finite-loss contrasts depend on scale and do not establish a restoration benefit.

---


### 235. [Bilinear Hulls for Support Splitting: Characterization, Optimization, and Applications](https://arxiv.org/abs/2611.01337)

**<font color=#1a73e8>作者：</font>** Yusuke Aikawa, Keita Ishizuka, Tomoki Moriya  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Sendrier's Support Splitting Algorithm (SSA) is the standard solver for the Permutation Equivalence Problem (PEP); its cost is dominated by a term that grows exponentially in the hull dimension. We study, mathematically, how much this cost can be lowered by replacing the standard inner product, on which the hull is defined, with an alternative bilinear form. Two structural results give a complete answer: only a narrow two-parameter family of bilinear forms produces a hull on which SSA can still operate, namely those whose matrix in the standard basis is a linear combination of the identity and the all-ones matrix; and even within this family the hull dimension drops by at most one (with the reduction achieved on every self-dual code whose length is coprime to the field characteristic). Together, these results give a tight upper bound: since SSA on a code with hull dimension $h$ has cost dominated by $q^h$, replacing the standard hull with $\mathrm{Hull}_M$ lowers this dominant term from $q^h$ to at best $q^{h-1}$, so no bilinear-form generalization of the inner product can reduce the SSA cost by more than a factor of $q$, the field size. Going beyond this requires invariants outside the bilinear framework. As an application, we verify that PEP-based SPECK admits the factor-$q$ cost reduction, while LEP-based LESS and PKP-based PERK lie outside our framework. A SageMath implementation of the bilinear-hull preprocessing confirms feasibility at SPECK's recommended length $n = 252$.

---


### 236. [Unified dynamics of training, learning, inference, and reinforcement in neural networks](https://arxiv.org/abs/2611.01345)

**<font color=#1a73e8>作者：</font>** Mian Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite their remarkable success, neural networks remain largely black boxes, and the mechanisms underlying their behavior are still poorly understood. Nine nanoGPT experiments established training-learning-inference relations: realized updates elicit state-dependent finite-amplitude responses; learning persistently reorganizes distributed functional support, with target-specific readout-boundary crossings determining capability transitions; inference recruits learned support without changing the learned state. Factors identified in the fifth experiment yielded a direct predictor of post-update capability transitions, achieving 91.43% accuracy and 91.49% four-way macro recall across 5,088 targets. We tested these relations and prediction across five additional neural architectures. In a seventh system, concentrated correct feedback eroded previously mastered skills; rebalanced feedback restored their accuracy from 70.31% to 99.48%. Linking inference consequences to subsequent training closes these relations into unified training-learning-inference-reinforcement dynamics.

---


### 237. [Sentiment sensing: comparative analysis of multilingual sentiment dynamics](https://arxiv.org/abs/2611.01348)

**<font color=#1a73e8>作者：</font>** Mara Sabina Bernardi, Elisa Di Nuovo, Francesca Torti 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-country sentiment analysis faces three fundamental challenges: language-specific biases distort comparisons, compositional data constraints invalidate standard statistics and temporal dynamics lack rigorous testing frameworks. We introduce sentiment sensing, a framework that addresses these gaps through integrated statistical methods. By combining compositional data analysis, functional data methods, and non-parametric inference, sentiment sensing enables valid multilingual comparisons and statistically defensible detection of sentiment shifts. Our framework has been tested in two case studies, analyzing news articles from the 27 countries of the European Union on the topics of energy and artificial intelligence. Sentiment sensing focuses on multilingual sentiment analysis enabling rigorous comparative science.

---


### 238. [FACET: Feasibility-Automaton Complete Enumeration and Truncation-Free Scoring of Molecular Formulas from MS/MS](https://arxiv.org/abs/2611.01352)

**<font color=#1a73e8>作者：</font>** Xujun Che, Depeng Xu, Xiuxia Du  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Determining the neutral molecular formula of a precursor ion from its tandem mass (MS/MS) spectrum is the first step in identifying an unknown small molecule. Existing methods trade recall, whether the correct formula is among the candidates, against the cost of examining each candidate. Methods that examine each candidate in depth must first shorten the list, by limiting element counts or truncating it, and that is where the correct formula is lost. End-to-end regressors are fast but guarantee neither validity nor recall. We present FACET, which separates deciding which formulas to consider from deciding which one to choose. A feasibility automaton builds a formula one element count at a time and admits exactly the formulas that fit the precursor mass and satisfy the ring-and-double-bond and valence constraints. Run as an exhaustive search, it enumerates the complete feasible set, so every candidate is valid and recall is fixed by the chemical constraints rather than by a trained model. A small neural scoring head then ranks every feasible formula from one pass of a pretrained spectrum encoder, so no candidate is discarded. On the NPLIB1 benchmark FACET reaches top-1 accuracies of $0.859$ with the adduct known and $0.729$ with it unknown, compared with $0.766$ and $0.660$ for the strongest established method, and its recall is the highest. On the external CASMI 2022 set its recall is $1.000$, and with the adduct unknown it is the most accurate of the methods compared.

---


### 239. [Learned Surrogates of Three-Dimensional Magnetohydrodynamic Turbulence](https://arxiv.org/abs/2611.01356)

**<font color=#1a73e8>作者：</font>** Semih Kacmaz, E. A. Huerta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Three-dimensional magnetohydrodynamic (MHD) turbulence, the flow of astrophysical and fusion plasmas, is costly to simulate. We present, to our knowledge, the first learned surrogates of three-dimensional resistive MHD turbulence, and compare three standard backbones in that role: a convolutional UNet, a shifted-window transformer and a Fourier neural operator. They are trained as autoregressive emulators of decaying MHD turbulence at a resolution of $128^3$ and Reynolds numbers of 1000, 3000 and 6000, on 500 simulations per Reynolds number, each with one two-stage procedure, single steps and then short rollouts, and stopped by one rule. Over a window of about one large-eddy turnover time, the UNet and the transformer reach relative velocity errors of 0.018 to 0.053 and keep the current sheets, the enstrophy, the current density and the energy spectra of the simulation; which of the two is the more accurate depends on the Reynolds number, the UNet leading at 3000 and 6000 and the transformer at 1000. Applied with the same backbones and training procedure to two public benchmarks, the models reach the lowest error reported to date on the isotropic turbulence set of FactFormer, 39% below the best published model. On the compressible MHD set of The Well, their rollout errors are a third to a half below those of the best of The Well's baselines. They also match a 1.3 B-parameter pretrained foundation model in its rollout windows, with 20-62 times fewer parameters. The code, the configuration of every model, the evaluation scripts and the data generator with the seed of every simulation will be released upon publication.

---


### 240. [Interpreting Classical Readability Formulae as Surprisal](https://arxiv.org/abs/2611.01359)

**<font color=#1a73e8>作者：</font>** Yo Ehara  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Surprisal correlates closely with reading time and is widely used in the cognitive science of reading as a measure of processing difficulty. Classical readability formulae such as the Flesch-Kincaid Grade Level, which scores a text by the US school grade expected to read it, are the most widely used practical measures of text difficulty, but their coefficients are unitless regression constants and have never been related to surprisal. We theoretically show that these coefficients can be interpreted as surprisal: every formula of the classical additive shape is a sum of per-word and per-sentence cross-entropies under a memoryless model, and once that model is tied to the language through Zipf's law and the formula is read as its linearisation at a reference text, each coefficient factorises into a scale in grades per nat, a Zipf slope and a reference sentence length. A grade thereby becomes a quantity in surprisal. Because the formula outputs grades and children's vocabulary has been measured by grade, the interpretation recovers the vocabulary growth the formula implicitly assumes and lets it be checked against development: holding sentence length fixed, the word coefficient of the Flesch-Kincaid formula converts to 0.18 nat of unigram surprisal per word per grade (0.15 to 0.19 across the regression-derived formulae), and normative root-word vocabulary growth (Biemiller and Slonim, 2001), converted through Zipf's law, gives 0.16 nat per year at the frontier of the known vocabulary. The word coefficient is one year of vocabulary growth, and the grade is a vocabulary scale. The identification also yields a diagnostic (the sentence-length terms are not those of a memoryless surprisal) and extends to a Japanese formula.

---


### 241. [Reasoning Across Scales: Learning Challenges and Opportunities for Immersive Technologies in Chip Design Education](https://arxiv.org/abs/2611.01361)

**<font color=#1a73e8>作者：</font>** Satya Kamala Immidisetty, Dishita Turakhia  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As demand for semiconductor talent grows, education must prepare learners for the complexity of modern chip design. Instruction typically relies on lectures, textbooks, software exercises, and limited laboratory experiences. Although foundational, these approaches offer limited support for understanding the spatial, multi-scale, and interconnected nature of chip design. Virtual reality (VR) can help learners visualize and interact with complex structures and processes, but its educational opportunities remain underexplored.
We examined this gap through chip design curriculum analysis and semi-structured interviews with five participants representing instructional and learner perspectives. We characterized four learning demands: descriptive knowledge, procedural knowledge, relational and design-focused reasoning, and strategic decision-making. We identified challenges in connecting abstraction levels, interpreting spatial structures and temporal behavior, bridging theory and practice, and reasoning about design trade-offs and downstream consequences. Drawing on these findings and prior research, we mapped learning demands to six immersive affordances: spatial visualization, multi-scale navigation, interactive manipulation, temporal dynamics visualization, immediate feedback, and collaboration.
These findings motivate Cross-Scale Spatial Reasoning (CSSR) as a conceptual lens for understanding how learners connect physical structures, design representations, and engineering consequences across the chip design pipeline. We contribute an empirically informed account of learning challenges, a structured mapping of learning demands to immersive affordances, and concrete design opportunities for immersive semiconductor education. These contributions guide the development and evaluation of immersive environments that support reasoning across scales, representations, and design processes.

---


### 242. [Cross-Scale Spatial Reasoning: A Learning-Centered Framework for Designing Immersive Learning Environments](https://arxiv.org/abs/2611.01364)

**<font color=#1a73e8>作者：</font>** Dishita Turakhia  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Understanding complex scientific and engineering systems often requires learners to connect structures, processes, and behaviors across different spatial scales and levels of organization. Although research on spatial cognition, scale, multiple representations, and systems thinking has examined aspects of this challenge, these perspectives do not always provide explicit guidance for designing learning activities that require learners to integrate information across levels. Immersive technologies offer opportunities to explore otherwise inaccessible structures, coordinate representations, and investigate system behavior, but their educational value depends on the reasoning they support. This paper proposes Cross-Scale Spatial Reasoning (CSSR) as an integrative framework for understanding how learners establish and use spatial and structural relationships across scales or organizational levels. We describe five interrelated processes: scale navigation, cross-scale relational mapping, representational coordination, dynamic and causal reasoning, and consequence-oriented reasoning. Building on these processes, we develop a learning-centered framework that connects reasoning objectives to immersive design mechanisms, instructional scaffolding, and assessment. Illustrative applications in biology, semiconductor design, manufacturing, and architecture show how the framework can inform domain-specific learning activities. We also propose testable research propositions and approaches for evaluating cross-scale understanding, instructional effectiveness, and transfer. Rather than treating immersion as an educational outcome in itself, CSSR provides a basis for designing and studying learning environments that help learners explain how complex systems work across levels.

---


### 243. [IMPACT: Image-Conditioned Motion with Physics-Aware Collision and Trajectory Guidance for Video Generation](https://arxiv.org/abs/2611.01372)

**<font color=#1a73e8>作者：</font>** Shiwei Yang, Yunlong Yu, Zhao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visually realistic video generation does not guarantee physically consistent motion. Generated objects may exhibit implausible collision responses or rebounds without energy dissipation, while even physically valid motion predictions may not be faithfully realized during synthesis. We propose \textbf{IMPACT}, a physics-state-driven image-to-video framework that addresses these challenges by coupling explicit dynamics prediction with complementary sparse--dense physical guidance. A learnably calibrated Physics State Generator unifies continuous free-flight dynamics with discrete collision responses, linking impact timing, post-impact velocity, rebound attenuation, and eventual settling within a coherent physical-state sequence. To translate this evolution into effective generative constraints, IMPACT derives sparse trajectories and dense region-level motion priors from the same physical rollout. Sparse trajectories constrain global object displacement, while dense priors guide diffusion sampling to encourage coherent object-region motion and suppress unwanted background changes. Their shared physical basis coordinates global and local motion guidance to reduce prediction--generation mismatch. Experiments on 100 controlled sphere--plane collision scenes spanning different material combinations and visual environments demonstrate improved physical plausibility over representative general-purpose, physics-grounded, and motion-controllable baselines. The project repository is available at this https URL

---


### 244. [State-Augmented Learning for Post-Deployment Adaptation of Coexisting O-RAN Applications](https://arxiv.org/abs/2611.01376)

**<font color=#1a73e8>作者：</font>** Wonhyeok Ko, Yeonseo Jeong, Songnam Hong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fixed control policies in Open RAN can require retraining when service requirements, traffic loads, or interacting applications change. We propose ATTUNE, a state-augmented learning method for an energy saving application that coexists with a learned mobility load balancing application under a service constraint. ATTUNE conditions the energy saving policy on a Lagrange multiplier and updates this scalar during operation using measured service degradation, while keeping both applications' network parameters fixed. To train a single policy across service requirements, ATTUNE samples target service levels uniformly and maps them to multipliers through an adaptive table. This procedure accounts for policy-dependent multiplier responses and improves energy savings compared with training over a widened fixed multiplier range. We characterize the induced distribution of service levels and the convergence and fluctuations of the online update. An exact finite-window identity establishes convergence of average measured degradation to the target when the projection corrections vanish on average. Simulations show that a single ATTUNE policy achieves energy savings comparable to policies trained separately for each service requirement. It adapts to changes in the target, load, and partner application without retraining, increases energy savings at light load, and maintains target tracking for separately trained application pairs. No statistically significant increase in cell switching is detected in the evaluated comparisons.

---


### 245. [Vocabulary Aligned Explanations for Computer Vision Models](https://arxiv.org/abs/2611.01391)

**<font color=#1a73e8>作者：</font>** Erfan Mirhaji, Nikhil Krishnaswamy, Jill Zarestky 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optimizing vision models for accuracy does not force the model to learn and utilize human-understandable and domain-specific concepts and rules. We propose explaining image classifications through domain-specific concepts, visual evidence, and expert knowledge expressed as logical rules. We introduce FLUENT (Framework for Localized, Uncertainty-Aware Explanations in Normative Terminology), a post-hoc framework that ranks expert-authored rules combining jointly required, alternative, and absent concepts. To account for prediction errors, FLUENT combines predicted labels and concept states with empirically estimated likelihoods and concept priors. It scores each rule by calculating support over satisfying assignments to the concepts mentioned in that rule, then normalizes these scores to express relative confidence among candidate explanations. The selected rule is illustrated through occlusion-based highlights for positive concept mentions in the query image and localized examples in retrieved reference images for negative mentions. These illustrations are intended to show end users unfamiliar with the domain what the concepts named in an explanation look like. FLUENT combines domain knowledge and model accuracy, and delivers visual concept highlights and explicit rule confidence to explain an image in the vocabulary of an application domain.

---


### 246. [RadPose: ISAC-based RF 3D Human Pose Estimation](https://arxiv.org/abs/2611.01400)

**<font color=#1a73e8>作者：</font>** Geo Jie Zhou, Kunzhe Song, Ruxin Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human pose estimation under adverse lighting and occlusion conditions remains challenging for camera- and LiDAR-based systems. Although mmWave radars provide robustness to illumination and occlusion, they rely on dedicated hardware and licensed spectrum, limiting scalability. In this paper, we present RadPose, a learning-based monostatic integrated sensing and communication (ISAC) framework that enables mmWave communication devices to perform 3D human pose estimation. Unlike specialized radars, RadPose leverages monostatic full-duplex operation to extract channel impulse responses (CIRs) directly from standard OFDM communication signals, generating 3D radio point clouds without additional sensing hardware. To address the sparsity and noise of RF observations, RadPose employs a cross-frame transformer-based pose inference network with semantic-guided spatial attention and target-driven temporal attention for robust spatio-temporal aggregation. It further adopts a joint-aware inverse kinematics refinement module based on graph convolution to enforce skeletal topology, bone-length consistency, and anatomical plausibility. Extensive experiments demonstrate RadPose achieves competitive accuracy compared to state-of-the-art radar-based approaches while maintaining robust performance in unseen and occluded scenarios. The dataset and source code are available at this https URL.

---


### 247. [Gamification Box: Automated Personalized Rewards for Improved Task Experience](https://arxiv.org/abs/2611.01424)

**<font color=#1a73e8>作者：</font>** Ali Utku Ozaslan, Sadra Sadraddini, Deniz Marti  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We introduce a gamified rewarding system, called "Gamification Box", and conduct a user study to examine its effects on task experience and performance. Gamification Box provides an interface for automated rewards that are intrinsically enjoyable activities, such as watching short video clips. In a controlled user experiment, 118 participants completed a short-term memory task involving meaningless syllables under either a gamified reward condition or a non-rewarded control condition. Participants in the gamified condition reported significantly greater perceived task enjoyment than those in the control group. Importantly, this increase in perceived enjoyment did not come at the cost of performance: no significant differences were observed in free recall or recognition accuracy between conditions. These findings suggest that while gamified rewards may not directly enhance immediate performance, they function as a motivational regulator, thereby improving task enjoyment. The primary benefit of such systems may therefore lie in supporting sustained effort over time, where cumulative performance gains are more likely to emerge.

---


### 248. [Uncertainty-Aware Joint Generative Modeling of Fault Event Sequences and Sensor Time Series in Solar PV Plants](https://arxiv.org/abs/2611.01425)

**<font color=#1a73e8>作者：</font>** Jiayu Huang, Boyang Xu, Yongming Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents a multimodal generative model designed to simulate a solar energy plant system for predictive maintenance and fault prediction. We propose a novel approach to enhance system generation through conditional generation by leveraging both event sequences and time-series data and improve next event prediction. The framework employs a Transformer Hawkes Process (THP) to encode event data and an iTransformer to encode time-series data, integrated via a co-attention mechanism that effectively captures cross-modal dependencies between discrete events and continuous signals. From these integrated representations, we employ two specialized decoders for simulation: a Conditional Latent Diffusion Model (CLDM) for modeling future sensor trajectories and the Score Matching-based UnceRtainty quantiFication for Transformer Hawkes Process (SMURF-THP) for high-fidelity event prediction. This dual-decoder strategy supports uncertainty-aware, history-conditioned simulation by rolling the model forward for a specified number of generation iterations, producing finite stochastic scenarios rather than deterministic extrapolations over the full observational record. Evaluated on a comprehensive dataset from the Red Rock Solar Site in Arizona, our approach improves aggregate event-prediction F1 relative to baselines and supports applications in predictive maintenance, fault detection, and energy optimization for solar power systems.

---


### 249. [Renormalized Cellular Intelligence: When Does Model Reduction Preserve Collective Capability?](https://arxiv.org/abs/2611.01441)

**<font color=#1a73e8>作者：</font>** Xuening Wu, Yanlan Kang, Qianya Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> As multi-agent systems grow in size and complexity, understanding which features of their interactions support collective capability becomes increasingly difficult. Can a simpler description preserve both task performance and the measured contribution of interactions between agents? Preserving collective dynamics alone is insufficient: reduction can alter decision-relevant information or give a non-communicating baseline access to pooled observations, distorting the measured advantage of interaction. We introduce Renormalized Cellular Intelligence (RCI), a framework for specifying and auditing capability preservation across scales. RCI treats the task, interacting dynamics, matched baseline, decision interfaces, and resource budget as a joint object of reduction. It specifies dynamical closure, decision compatibility, and preservation of the intended baseline comparison, and bounds the resulting error in relative capability gain. An exact analytical construction demonstrates task-score preservation, while a counterexample shows how closed reduced dynamics can erase the measured interaction gain. Using cellular systems as models of locally interacting agents, we evaluate three reduction candidates on five frozen learned models without retraining. The final candidate reduces the evolving state from eight to five dimensions per cell (37.5%). Within-run uncertainty bounds support relative gain above a prespecified threshold for the fixed model collection, yet the candidate fails the closure and decision-preservation requirements for a complete RCI certificate. RCI provides explicit criteria for distinguishing positive interaction gains from

---


### 250. [Correctness and Predictive Uncertainty in Bayesian TSK Fuzzy Regression: A Reproducible Evaluation on Tabular and Building-Meter Data](https://arxiv.org/abs/2611.01447)

**<font color=#1a73e8>作者：</font>** Zhiren Xiao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uncertainty estimates from fuzzy regression are informative only when the implementation is correct and the comparison protocol makes the sources of variation visible. We revisit a first-order Takagi--Sugeno--Kang (TSK) regression implementation and rebuild its dense, conjugate Bayesian, BIC-based, and rule-level spike-and-slab estimators using corrected code. The corrected pipeline freezes the Gaussian membership partition at training time, uses a scaled conjugate prior, evaluates firing strengths in the log domain, and reports direct posterior-predictive quantiles for Bayesian methods. Across 30 outer 80/20 splits on three targets from two UCI regression datasets, corrected TSK-LS obtains $R^2=0.957$, $0.923$, and $0.786$ on Energy-Heating, Energy-Cooling, and Concrete, respectively; rule-level Gibbs sampling with Bayesian model averaging obtains $0.957$, $0.922$, and $0.784$. We then evaluate the same workflow on a bounded chronological sample of the Building Data Genome 2 meter data that covers 158 buildings across 17 sites. In a common-unit evaluation, every method is scored on the same 47,400 test rows and every trained model uses 94,800 train--validation rows. Persistence has RMSE $27.710$, compared with $29.083$ for both TSK-LS and Bayesian TSK; the pre-specified building-level mean RMSE difference between Bayesian TSK and persistence is $+0.0447$ with a 95% site-cluster bootstrap interval of $[-1.5536,1.5665]$. The Bayesian TSK 90% intervals have PICP $0.980$ and MPIW $116.469$. Taken together, the evidence supports a narrower conclusion: spike-and-slab model averaging is a reproducible implementation option, but it does not provide a demonstrated accuracy or calibration advantage across the tested tabular and building-meter settings.

---


> [!TIP]
> 当前位于：**201-250**（第 5/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-633](./part-13.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
