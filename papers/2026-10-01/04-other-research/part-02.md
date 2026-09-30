# 📦 其他研究 | 2026年10月01日

> 本类共 **447** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-447](./part-09.md)

---

### 51. [PowerZooJax: A JAX-based Power System Benchmark for Reinforcement Learning](https://arxiv.org/abs/2609.36052)

**<font color=#1a73e8>作者：</font>** Zhanhua Pan, Xiao Liu, Zhilong Cao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Power system operation is a safety-critical sequential decision-making problem, making it a natural testbed for reinforcement learning (RL). However, existing RL environments for power systems are often narrow in scope and computationally limited by CPU-based simulation workflows, making large-scale evaluation difficult. We introduce PowerZooJax, a JAX-based benchmark suite for RL in power system operation. It provides five constrained Markov decision process tasks spanning generation, transmission, distribution, distributed energy resources, and data center microgrid. By rewriting power flow, economic dispatch, market clearing, and device dynamics as JAX computation graphs, PowerZooJax keeps the entire training and evaluation loop on the GPU. Experiments show substantial speedups over CPU-based simulations and demonstrate standardized evaluation of policy returns, safety violations, and out-of-distribution stress conditions. Our open-source benchmark is available at: this https URL.

---


### 52. [GeoWind2Plan: Mission-Time 3D Urban Wind Prediction for Energy-Efficient UAV Planning](https://arxiv.org/abs/2609.36056)

**<font color=#1a73e8>作者：</font>** Shaoxiang Qin, Yucheng Zhao, Fuyuan Lyu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In urban low-altitude flight, buildings reshape ambient wind into spatially varying 3D flow, making unmanned aerial vehicle (UAV) energy depend on local wind exposure as well as path length. However, building-resolved wind information is rarely available when a mission must be planned. Computational fluid dynamics (CFD) can produce high-fidelity urban flow fields, but each simulation is tied to a fixed inflow boundary condition and can take hours to days, which is incompatible with urban UAV missions that typically last minutes to tens of minutes. We present GeoWind2Plan, a geometry-to-wind-to-planning framework for mission-time 3D urban wind prediction and energy-efficient UAV planning. Given only a background wind vector, 3D building geometry, and a start-goal pair, GeoWind2Plan transforms the building geometry into a reference-wind frame, predicts mission-relevant 3D wind patches with a localized geometry-conditioned neural operator, stitches them into a queryable local wind field, and optimizes a feasible 3D path and speed profile using a physically grounded UAV energy model. Rather than pursuing CFD-perfect reconstruction, GeoWind2Plan targets decision-useful wind prediction: trajectories are planned with predicted wind and evaluated under high-fidelity CFD wind. Across held-out urban domains, wind speeds, and mission wind-angle regimes, GeoWind2Plan performs corridor-localized wind inference in about 3 seconds, compared with roughly 8 hours for CFD. Under CFD evaluation, trajectories planned with GeoWind2Plan reduce energy by 6.9%, 12.7%, and 4.5% in tailwind, headwind, and crosswind missions relative to wind-agnostic planning, recovering 87.9%, 85.7%, and 75.0% of CFD-reference savings. These results show that fast, corridor-localized 3D urban wind prediction can make wind-aware UAV energy planning practical at mission time.

---


### 53. [Mirror-Score: Calibrated, Inference-only Scoring Exposes the Limits of Sequence-compatibility Ranking in D-peptide Design](https://arxiv.org/abs/2609.36057)

**<font color=#1a73e8>作者：</font>** Jiada Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> D-peptides combine protease resistance with high target specificity, but computational design of D-peptide binders remains immature. Mirror-Peptidizer introduced an in silico mirror-image screening pipeline using target reflection, backbone generation, and ProteinMPNN sequence design, but its raw ProteinMPNN negative log-likelihood (NLL) ranking was not validated against measured affinities, and only 4 of 9 tested MDM2 designs bound detectably. We introduce Mirror-Score, a calibrated, inference-only scoring framework for heterochiral D-peptide/L-protein complexes, and a public benchmark of 31 crystal complexes across four target families, including 18 with literature-verified affinities. Raw ProteinMPNN NLL is not a valid affinity ranker: its pooled Spearman correlation with affinity is 0.19, and correlations reverse between MDM2/CHIP (+0.62) and gp41 (-0.70). We therefore evaluate Boltz-2 mirror-space cofolding confidence. For the complete viral-entry family (7 structures representing 3 peptides), interface predicted local distance difference test (pLDDT) achieves structure-level leave-one-out Spearman rho = 0.90 (p = 0.006) and correctly orders all three peptides by affinity, whereas NLL fails (structure-level rho = 0.18). Because only three independent chemotypes are represented, this result indicates directional consistency rather than a statistically validated predictor. Cross-family calibration does not transfer at current sample sizes, supporting family-matched calibration as the practical deployment mode. We also specify a prospective design protocol for the antimicrobial-resistance targets LasR and LecB from Pseudomonas aeruginosa, including mirrored structures, ligand-derived hotspot maps, diffusion-model-ready inputs, and Mirror-Score ranking. Code, benchmark data, structures, and analysis scripts are openly available at this https URL.

---


### 54. [Introducing the CZAR Loss: A Tailored Objective Function for Financial Log-Return Predictions](https://arxiv.org/abs/2609.36061)

**<font color=#1a73e8>作者：</font>** Joel Pfeffer, J. M. Diederik Kruijssen, Florian Stecker 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In quantitative finance, standard regression losses are misaligned with the economics of return prediction. As the conditional mean of financial log-returns is close to zero, symmetric losses such as the mean squared and mean absolute errors make the constant zero forecast a near-optimal solution, penalizing models with genuine but noisy directional skill. This applies both during training, where predictions shrink toward zero, and during evaluation, where trivial forecasters can lead loss-based rankings. Under a Gaussian linear prediction model, we show that all symmetric monotonic losses share a universal breakeven directional accuracy against the zero predictor, which rises sharply and becomes unobtainable as the prediction noise approaches the standard deviation of the returns. We introduce the CZAR (Composite Zero-Agnostic Return) loss function, a piecewise quadratic loss built around five key requirements: convexity in the prediction, asymmetry with true return direction that vanishes at zero, near-linear penalization of undershoots and wrong-direction predictions, divergence for large errors, and an adaptive loss floor for evaluation. CZAR is provably convex in the prediction at fixed true value, has closed-form gradient and Hessian suitable for custom objectives in gradient-boosted libraries, and its four hyperparameters reduce to a single choice through correlated defaults. In idealized tests, the minimum directional accuracy required for a CZAR-evaluated forecaster to outperform the zero predictor under mean log loss remains near the 50% chance level, whereas the corresponding threshold for symmetric losses rises sharply with prediction noise. This advantage persists under heavy-tailed return distributions. In a LightGBM experiment on intraday BTC log-returns, CZAR-trained models reduce the `zero-returns bias' and improve directional accuracy on large-magnitude returns.

---


### 55. [Understanding Decision-Making Mechanisms in Neural Routing Solvers](https://arxiv.org/abs/2609.36063)

**<font color=#1a73e8>作者：</font>** Fatemeh Askari, Mazdak Teymourian, Mohammad Izadi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural Combinatorial Optimization (NCO) has achieved strong empirical success, yet the internal mechanisms driving model decisions remain largely unexplored. In this paper, we investigate three representative autoregressive NCO models spanning two encoder-decoder configurations: AM and POMO (heavy-encoder, light-decoder), and LEHD (light-encoder, heavy-decoder). Through behavioral analyses, representation probing, and causal interventions, we examine how these models construct solutions and use internal representations during decoding. Our results suggest that AM and POMO predominantly follow a persistent geometric pattern throughout solution construction, whereas LEHD contains linearly accessible information about multiple future actions. Causal experiments further provide evidence for the role of future-node representations in LEHD's decision-making. We also observe that LEHD relies strongly on the current-node representation for immediate local decisions, while the start-node representation plays a broader navigational role over the subsequent route. Cross-instance alignment analyses additionally indicate that LEHD maps current-node representations into a relatively shared latent region, which may provide a stable reference for evaluating subsequent decisions. Across the Traveling Salesman Problem and the Capacitated Vehicle Routing Problem, these results reveal distinct decision-making patterns across these architecturally distinct solvers and provide a foundation for more interpretable analyses of NCO solvers. Code and additional visualizations are provided in the this https URL.

---


### 56. [LongCat-DeepResearch Technical Report](https://arxiv.org/abs/2609.36071)

**<font color=#1a73e8>作者：</font>** Meituan LongCat Team, He Zhu, Yue Xu 等 31 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present LongCat-DeepResearch, a deep research system that combines an enhanced LongCat model with a multi-agent workflow for producing comprehensive, evidence-grounded reports. The workflow separates global planning from detailed investigation and coordinates revision at the section level. Multiple planning agents first explore external sources and refine an actionable research plan, termed ResearchSpec. Research agents then investigate and draft their assigned sections in parallel, gathering additional evidence in separate contexts as their analyses develop. Once the sections are assembled, global review guides targeted local revisions, reducing reliance on repeated full-report rewriting. This workflow also supports the construction of research tasks and trajectories for the mid-training and post-training of LongCat's general-purpose models. LongCat-DeepResearch achieves 55.25 on DeepResearchBench, 51.35 on DeepResearchBench II, and 79.83 on ResearchRubrics. On an in-house benchmark, it scores 76.04, ranking second among four compared systems. Development-set analyses show benefits from combining planning perspectives, while further planning refinement has mixed effects. Additional editing improves average automatic readability preference across two benchmarks, with different trends on each.

---


### 57. [GEM-KMeans: Memory-Efficient and Accurate Clustering on Massive Scale with GPU Optimization](https://arxiv.org/abs/2609.36074)

**<font color=#1a73e8>作者：</font>** Peng Xu, Nihar Koganti, Volodymyr Kindratenko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Memory-efficient scaling on clustering problems without sacrificing statistical accuracy is of central interest for large-scale data analysis and machine learning problems. Nonnegative low-rank (NLR) matrix factorization for $K$-means is a scalable clustering method, which connects to semidefinite relaxations with optimal average-case exact recovery guarantees. However, a direct GPU implementation of NLR requires multiple large factor-sized buffers and substantial data movements that are essentially memory-bound. In this paper, we introduce GEM-KMeans, a spectrally normalized yet mathematically equivalent NLR formulation that fuses the gradient update, nonnegative projection, and sufficient statistics for normalization and iterate movement into a matrix-multiplication epilogue. Instead of retaining three massive factor-sized arrays, our IO-aware GPU implementation materializes only one single factor with small tile-reduction arrays as additional storage in the High Bandwidth Memory (HBM). We derive explicit memory costs and spectrally normalized smoothness bounds for optimizing the clustering objective function. Accurate clustering is demonstrated at massive scales on synthetic and real datasets, where performance gains of GEM-KMeans over existing GPU-accelerated Lloyd's algorithms involve data-dependent runtime tradeoffs.

---


### 58. [Early Learning Shapes Later Directions Of Representation Change In Continual Learning](https://arxiv.org/abs/2609.36081)

**<font color=#1a73e8>作者：</font>** Yuantao Deng, Jinnuo Liu, Kaizhen Tan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Representations continually change as a network learns new tasks. We ask whether early representational changes naturally form a geometric structure that continues to shape later learning. We identify a low-dimensional subspace of early representation drift, which we call a scaffold, and test whether it is reused across subsequent tasks. Across four pretrained visual encoders and two datasets, later representational changes consistently favor this early-defined subspace over matched random alternatives. This reuse is history-dependent: when networks experience different early tasks but identical later training inputs, each network preferentially reuses the scaffold induced by its own learning history. The same preference appears in individual optimizer updates, even though the network's dominant local response directions shift away from the original scaffold. Finally, constraining motion within the scaffold slows new-task acquisition more than matched random constraints, while effects on old-task retention are less consistent. In summary, these results suggest that early experience leaves a persistent geometric imprint on how neural networks adapt to future tasks.

---


### 59. [Data Unlearning via Inverse Distillation](https://arxiv.org/abs/2609.36099)

**<font color=#1a73e8>作者：</font>** Aleksei Leonov, Nikita Kornilov, Zhenhe Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-step matching models, including flow and diffusion models, produce high-quality outputs but incur substantial inference costs and may reproduce unwanted components of their training datasets. We introduce Inverse Distillation Unlearning (IDU), a unified framework that simultaneously distills a teacher multi-step matching model into an efficient one-step student generator and suppresses outputs corresponding to a designated training subset. We first formulate distillation as a min-max objective over a data distribution and then represent this distribution as a mixture of the forget-set and the generated distributions. This allows us to compare this mixture with the teacher's training distribution and recover only the retained data at the optimum. Our method requires only a pretrained full-data teacher and data from the forget set, without access to retained training examples, extra feature extractors or classifiers. Extensive experiments on MNIST and CIFAR-10 datasets under flow-matching and score-based diffusion settings demonstrate that IDU substantially reduces the generation frequency of forgotten classes while preserving generation quality on the retained classes. To the best of our knowledge, IDU is the first unified framework for simultaneous unlearning and distillation in unconditional flow-matching and score-based models.

---


### 60. [Why Backdooring Neural Networks is so Easy?](https://arxiv.org/abs/2609.36117)

**<font color=#1a73e8>作者：</font>** Issam Seddik, Mohamed El Amine Seddik  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Securing modern AI systems against backdoor attacks remains an open challenge and requires fundamentally principled estimates of the adversary's budget -- the poison fraction $\pi$ and trigger strength $\alpha$ needed to construct successful yet stealthy attacks. Motivated by recent empirical evidence that poisoning large language models can require a nearly constant number of malicious samples even as clean datasets grow, we derive an exact closed-form analysis of a quadratic neuron trained on a poisoned Gaussian mixture. We show, perhaps counterintuitively, that the same feature-learning dynamics that make neural networks powerful can also make them more vulnerable to backdoors. Specifically, with clean accuracy preserved to first order, $O(\pi)$, we demonstrate that lazy learning imposes the inverse-square-root scaling $\alpha \propto \pi^{-1/2}$ for a successful attack, while feature learning induces a quadratic detector whose loss margin scales as $O(\alpha^4)$, improving the attack budget to $\alpha \propto \pi^{-1/4}$. Consequently, nonlinear feature learning substantially reduces the trigger strength required at small poison fractions, thereby in a sense making feature learners more backdoor vulnerable. These results provide a theoretical mechanism consistent with large-scale empirical observations and demonstrate that security audits based on linear heuristics can systematically underestimate backdoor vulnerability in the widely adopted feature-learning regimes.

---


### 61. [AdaST: Adaptive Coupling for Spatial-Temporal Forecasting](https://arxiv.org/abs/2609.36119)

**<font color=#1a73e8>作者：</font>** Zhenyu Lei, Chenghao Liu, Yushun Dong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spatial-temporal (ST) forecasting underpins many real-world systems such as traffic, climate, and energy networks. While existing methods implicitly assume strong spatiotemporal coupling, we observe that real-world ST data exhibits distinct coupling regimes, ranging from temporal-dominated and spatial-dominated to strongly coupled patterns. This mismatch causes current models to suffer from spurious dependencies and degraded performance when one correlation dominates. To overcome this limitation, we aim to dynamically modulate spatial and temporal modeling based on the data's inherent coupling structure. However, three key challenges exist: unknown coupling structure, heterogeneous coupling dynamics, and suboptimal spatial modeling. We propose AdaST, an adaptive ST forecasting framework that tackles these challenges through a decompose-recompose paradigm. AdaST factorizes inputs into components capturing different coupling patterns using heterogeneity-aware experts. Each component is processed by role-aligned modules, and a correlation-informed adaptive recomposer integrates them for final prediction. Extensive experiments confirm that AdaST significantly outperforms state-of-the-art baselines, validating the necessity of an adaptive approach.

---


### 62. [Reasoning with Neural Cellular Automata](https://arxiv.org/abs/2609.36126)

**<font color=#1a73e8>作者：</font>** Mayalen Etcheverry, Pietro Miotti, Aidan Sirbu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern AI architectures used to solve visual reasoning tasks typically rely heavily on global connectivity and synchronization. As biological systems demonstrate, though, sophisticated computation can be performed in a more decentralized fashion. In this work, we test the reasoning capabilities of Neural Cellular Automata (NCAs), networks of recurrent cells that use strictly local connectivity and asynchronous updates. NCAs have been extensively studied in artificial life experiments, but it is unclear whether they can perform complex multi-step reasoning. We show that NCAs produce spatio-temporal dynamics capable of solving challenging visual reasoning tasks, including large mazes, Sudoku, and ARC-AGI-1. Furthermore, we provide evidence that NCAs generalize out-of-distribution when running with larger grids, longer rollouts, or parallel trials; and that the latter can be made more efficient via pruning of redundant trajectories. We find that these generalization capabilities depend on training with sample replay and stochastic perturbations, and that stochasticity remains beneficial at test time. Finally, we show that NCAs are robust reasoners capable of dynamically modulating compute to recover efficiently from damage, and that they can scale to solve reasoning in raw pixel space.

---


### 63. [A Character-Level Neural Approach to Sinhala Sandhi Splitting](https://arxiv.org/abs/2609.36131)

**<font color=#1a73e8>作者：</font>** Yasas Ekanayaka, Deshan Sumanathilaka  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sinhala Sandhi splitting recovers the constituent words or morphemes hidden inside a phonologically merged surface form. The task is important for Sinhala NLP because Sandhi obscures lexical boundaries, but no prior published work has established a neural benchmark for Sinhala Sandhi splitting. We present a character-level sequence-to-sequence study based on SandhiLex, using native Sinhala Unicode input and evaluating recurrent encoder-decoder models for affixational and more complex lexicalized, derivational, and etymological Sandhi. The central challenge is the hard subset lexicalized, derivational, and etymological Sandhi, where our best model, a bidirectional LSTM encoder with a unidirectional LSTM decoder, reaches only 68.40\% exact-match accuracy (82.08\% character-level accuracy), well below the 94.00\% achieved on the more regular affixational subset. Ablations show that bidirectional encoding is the largest contributor to performance, while native Sinhala script improves exact match accuracy over romanized input. Qualitative analysis indicates that many errors are near misses involving boundary adjacent characters or plausible but incorrect phonological substitutions. These results establish an empirical baseline for Sinhala Sandhi splitting and identify data scale, Sandhi type conditioning, and attention-based decoding as the main directions for future work.

---


### 64. [Hardware-Aware Functional Kolmogorov-Arnold Networks for Efficient Medical Image Enhancement and Segmentation](https://arxiv.org/abs/2609.36134)

**<font color=#1a73e8>作者：</font>** Mohammad Sadegh Sirjani  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Functional Kolmogorov-Arnold Networks (FunKAN) achieve state-of-the-art accuracy on MRI Gibbs artifact removal and anatomical segmentation, but their 11.6 M parameters and 8.7 GFLOPs are too large for edge medical devices. We present FunKANLite, a two-stage, hardware-aware compression of FunKAN for point-of-care use. FunKANLite-TR reduces the spatial prior and replaces the ResBlock offset predictor with a depthwise-separable block. It has 1.9x fewer parameters than FunKAN and no loss in accuracy. We then distill FunKANLite-TR into FunKANLite-ST, which lowers the Hermite basis rank, factorizes the spatial prior into a low-rank form, and halves the filter widths. FunKANLite-ST has 5.6x fewer parameters and 3.7x fewer GFLOPs than FunKAN. It stays within 1.4 percentage points IoU of FunKAN on BUSI, GlaS, and CVC-ClinicDB, and reaches 33.95 dB PSNR on IXI. On an NVIDIA Jetson Orin Nano and a Raspberry Pi 5, FunKANLite-ST reduces energy per inference by up to 68% and raises throughput by 2.9x.

---


### 65. [Learning Continuous Patient Trajectories from Electronic Health Records](https://arxiv.org/abs/2609.36144)

**<font color=#1a73e8>作者：</font>** Silas Ruhrberg Estévez, Kara Liu, Christopher Chiu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electronic health records provide irregular observations of latent patient states that evolve continuously over time. Recent autoregressive models condition on clinical histories to forecast future events as sequences of discrete observations. Conversely, multi-marginal flow matching provides a continuous-time formulation, but using multiple observations to supervise training paths does not itself give the learned dynamics access to preceding patient history. We introduce EHRFlow, a multi-marginal flow-matching framework that conditions on encoded patient history, thereby allowing future dynamics to depend on the patient's prior clinical trajectory. Our proposed framework accommodates irregular observation times and supports forecasting at arbitrary horizons. Across controlled synthetic benchmarks, EHRFlow improves clinical-code forecasting and latent-state recovery. On real-world clinical datasets comprising more than one million patients, including an independent external validation cohort, EHRFlow improves horizon-averaged top-5 clinical-code accuracy over autoregressive and history-independent flow-matching baselines. Finally, in a controlled counterfactual simulation, conditional guidance approximates the known effect of an antihypertensive intervention without training a task-specific outcome model.

---


### 66. [Privacy-Friendly Cohort Determination: Sealed, CSP-Independent In-Browser ML Inference of Professional Segments for Identity-Less Advertising](https://arxiv.org/abs/2609.36153)

**<font color=#1a73e8>作者：</font>** Om Shankar Tiwari, Navnit Shukla, Guanyu Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> B2B advertising targets a viewer's professional attributes (employer size and industry, function, seniority) and has obtained them by matching identities across sites. Safari and Firefox block third-party cookies, Google retired the Privacy Sandbox cohort APIs in 2025, and reverse-IP firmographics decay under remote work. We present SIF (Sealed Inference Frame), which infers coarse professional cohorts on the device and emits only a locally differentially private, taxonomy-coded label into the OpenRTB bid stream, with no cross-site identifier. It rests on a property of the web platform we make precise: a navigated cross-origin iframe is the only way third-party code obtains a policy it controls, so inference runs in WebAssembly even where the publisher's CSP forbids it, and a nested worker served with default-src 'none' gives the model no network. Even a malicious model leaks at most about 5 bits per site per week. Labels pass through a memoised k-ary randomised response keyed to the publisher's first-party identifier, which gives $\varepsilon$-local differential privacy, defeats averaging, and links requests no better than the identifier already sent. An org-conditional k-anonymity rule suppresses cells, more strictly on corporate networks than at home. Cohorts ride OpenRTB this http URL in a LinkedIn-aligned taxonomy, and attribution uses LinkedIn's click-scoped li_fat_id without bridging identities. We report a crawl of CSP deployment on 7,969 top sites and 431 B2B publishers, Heavy-Ad budgets, closed-form privacy-utility trade-offs, a re-identification simulation, and an assessment of which attributes are predictable at all: company type and size are, seniority largely is not. On-device is a design property, not a consent exemption.

---


### 67. [More Features Are Not More Evidence: Limits of Training-Free Human Activity Recognition with Jev](https://arxiv.org/abs/2609.36154)

**<font color=#1a73e8>作者：</font>** Orhan Konak  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> General-purpose models promise sensor-based decisions without training a task-specific classifier, which could reduce the dependence of Human Activity Recognition (HAR) on labeled data. Yet it remains unclear whether such models can directly interpret deterministic descriptions of physical sensor signals well enough to replace or complement trained HAR models. We study this question using Jev, a fixed general-purpose probabilistic decision model, on 1,800 class-balanced accelerometer windows from WISDM, UCI341, and PAMAP2. Jev receives no labeled examples, retrieval context, or HAR-specific parameter updates. We evaluate three deterministic sensor representations and compare 5,400 Jev decisions with a generative baseline and three supervised HAR models. Jev remains far below supervised recognition, with its strongest representation reaching macro-F1 of 0.038, 0.118, and 0.089 across the three datasets, compared with 0.686 to 0.907 for the supervised models. More numerical features do not improve Jev. Instead, they reduce recognition on all three datasets, while augmenting the same numerical evidence with a deterministic semantic rendering partially recovers performance, although the experiment does not isolate semantics from the accompanying serialization and redundancy changes. Jev is fast and inexpensive to query, but its probabilities are not reliably calibrated for recognition. A post-hoc fusion analysis finds a small improvement on WISDM that does not replicate on UCI341 or PAMAP2. These results show that training-free sensor decisions depend not only on the information available in the signal, but also on whether the model can use the representation through which that information is exposed. The sensor-to-model interface should therefore be treated as part of the model evaluation rather than as a neutral preprocessing step.

---


### 68. [Encoder-Sharing Hierarchical Federated Multi-Task Learning for VANETs](https://arxiv.org/abs/2609.36157)

**<font color=#1a73e8>作者：</font>** M. Saeid HaghighiFard, Sinem Coleri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most federated learning frameworks for vehicular ad hoc networks assume that all vehicles collaboratively train a single model for a common task. This assumption limits their applicability to practical vehicular environments, where vehicles may perform heterogeneous but related perception tasks with different output spaces. This paper proposes encoder-sharing hierarchical multi-task federated learning (EN-HMTFL), which integrates cluster-based hierarchical federated learning with a globally shared encoder and vehicle-local decoders. EN-HMTFL enables vehicles performing different tasks to collaboratively learn a transferable feature representation while preserving their task-specific models locally. Only the encoder is exchanged and aggregated through the hierarchy, whereas raw data and local decoder parameters remain at the vehicles. The proposed framework is evaluated on the MNIST and GTSRB datasets in different vehicular scenarios. Across the evaluated scenarios, EN-HMTFL improves accuracy by up to 24.0% relative to the compared representation-sharing benchmark. In scenarios where EN-HMTFL converges earlier, the reduction reaches up to 69 communication rounds (28.8%).

---


### 69. [Boosting Metric Depth Completion via Training-Free Adaptive Response Geometry](https://arxiv.org/abs/2609.36168)

**<font color=#1a73e8>作者：</font>** Mia Zhang, Jizong Peng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Depth completion aims to recover dense metric depth from sparse sensor measurements, increasingly leveraging visual foundation models as geometric priors. However, aligning these priors to true metric scale typically relies on rigid affine assumptions in predefined coordinate systems, leaving systematic calibration errors. Linearity in depth calibration depends on the response coordinate. We introduce adaptive response geometry, which makes the fixed choice of depth, log depth, or disparity an image-level unknown. A continuous response family unifies these coordinates and defines an explicit depth-dependent gain. We derive the response-gradient relation and estimate the response parameters in metric space. Hard-Dirichlet residual reconstruction completes the calibrated prior. Under deliberately incomplete metric observations, the training-free pipeline achieves macro AbsRel 0.0301 and macro NMed 14.04°, improving both aggregate measures over PriorDA, LDCM, and Any2Full. Linearity diagnostics examine how the selected response changes the depth relation and its metric error.

---


### 70. [Exploring Learning Models for Topological Relationship Recognition from Image Data](https://arxiv.org/abs/2609.36172)

**<font color=#1a73e8>作者：</font>** Saptak Das, Monidipa Das  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Figuring out how objects relate to each other, like whether they touch, overlap, stay completely separate or one sits inside another, matters a lot in fields like GIS, biomedical imaging, and robotics. Even though machine learning has come a long way, people haven't really focused on spotting these topological relationships in images. The main roadblocks? Not enough good datasets and no clear way to measure results. So, we rolled up our sleeves and built a new dataset. It's pretty sizable: over 11,000 labelled images showing all those essential relationships. We ran tests with some classic machine learning models, Naive Bayes, KNN, Random Forest, SVM, and Artificial Neural Networks, and threw in some deep learning stars like VGG16 and InceptionResNetV2. For the dataset itself, we used segmentation, contour detection, and grayscale normalization to tease out solid feature vectors. The results? Deep learning methods, especially VGG16, pulled ahead, with validation accuracy hitting 89.55%. That's a big jump compared to the traditional models. This shows how powerful transfer learning is for analyzing topological relationships in images, and it gives researchers a new standard to aim for in future work on spatial reasoning and topological classification.

---


### 71. [Fair Policy Optimization in Major-Minor Weakly Coupled Markov Decision Processes](https://arxiv.org/abs/2609.36174)

**<font color=#1a73e8>作者：</font>** Xiaohui Tu, Yossiri Adulyasak, Erick Delage  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider fair resource allocation in sequential decision-making environments modeled as major-minor weakly coupled Markov decision processes (M2WCMDP). In this framework, resource constraints couple the action spaces of a major sub-Markov decision process (sub-MDP) and a population of minor sub-MDPs that would otherwise operate independently. Instead of using the traditional utilitarian (total-sum) objective, we optimize a general class of monotone, concave, permutation-invariant, normalized fairness functions. With homogeneous minor sub-MDPs, we prove that the problem under symmetry reduces to optimizing the platform-plus-mean-participant utilitarian objective over the class of \textit{permutation-invariant} policies, which allows us to exploit efficient algorithms that optimize the utilitarian-based objective to solve this fairness-aware problem. For more general settings, we introduce a count-proportion-based deep reinforcement learning approach with a priority-based sampler that generates feasible count actions. The generality of our framework means that the proposed algorithms and theoretical guarantees transfer to any domain with a symmetric M2WCMDP structure. We consider two applications: the machine replacement problem and the joint control of pricing and taxi relocation problem on a New York City-calibrated dataset. We validate our theoretical findings with comprehensive experiments, confirming the effectiveness of our proposed method in achieving strong fairness-aware performance while remaining scalable.

---


### 72. [FD-AA: A Lightweight Focal-Diffuse And Attenuation-Aware Head for Incidental Abdominal Abnormality Detection in Chest CT](https://arxiv.org/abs/2609.36189)

**<font color=#1a73e8>作者：</font>** Haoyan Ding, Kritika Iyer, Halid Yerebakan 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Routine chest CT captures upper-abdominal structures that may contain clinically relevant incidental abnormalities. Detecting these findings requires feature extraction from organs with different spatial extents and attenuation patterns. We propose FD-AA, a lightweight organ-aware classification head adaptable for frozen 3-D CT encoders. Within each organ, an attenuation-aware module preserves sparse focal evidence, while masked generalized-mean pooling captures diffuse anomaly patterns. In seven abdominal organs, FD-AA with Pillar-0 achieved state-of-the-art (SOTA) performance in both the CT-RATE test set (AUC = 0.798) and the external RAD-ChestCT dataset (AUC = 0.713). More specifically, FD-AA improved macro AUC/AP from 0.763/0.346 to 0.798/0.405 over direct classification using frozen Pillar-0 only (p = 0.034/0.016). Such performance gain generalizes across multiple frozen encoders (AUC improvement on MedicalNet +9.8%, CT-CLIP +14.7%, ResNet +3.7%), demonstrating the effectiveness of FD-AA across different feature representations. These results support the effectiveness of integrating focal-diffuse aggregation with explicit HU evidence for incidental abdominal abnormality detection.

---


### 73. [PreviewDiff: Multimodal Critic-Guided Search over Diffusion Latents](https://arxiv.org/abs/2609.36199)

**<font color=#1a73e8>作者：</font>** Vighnesh Subramaniam, Boris Katz, Brian Cheung 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models can produce striking images and videos, but they still struggle with the compositional details that make a generation faithful to a prompt, such as object counts, attribute binding, spatial relations, and temporally grounded actions. A common way to improve prompt satisfaction is to spend more compute at test time through Best-of-N sampling, but final-sample selection is fixed. Best-of-N can only choose among completed outputs and cannot repair a promising trajectory before it fails. We introduce PreviewDiff, a training-free test-time search method that turns diffusion sampling from scalar search into a multimodal critic-guided search over intermediate latents. At selected denoising checkpoints, PreviewDiff decodes a partial preview, asks a multimodal judge to score and critique it, and uses the resulting natural-language feedback to branch over semantic prompt edits and locally re-noised latent continuations. These branches are then scored and selectively rolled forward, allowing verifier compute to guide generation while the sample is still editable. Across image and video generation benchmarks, PreviewDiff consistently improves over budget-matched Best-of-N selection and strong scalar-search baselines. Ablations show that earlier interventions and increased search width provide the largest gains, while deeper search and additional semantic variants offer complementary improvements. PreviewDiff demonstrates that multimodal feedback is most useful not only as a final verifier, but as an active controller inside the denoising process.

---


### 74. [Representable but Unlearned: Encoding Rank and the Interaction-Prediction Floor](https://arxiv.org/abs/2609.36208)

**<font color=#1a73e8>作者：</font>** Zahra Khodagholi, Niloofar Yousefi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Input encodings can restrict which measured contrasts a predictor can jointly reproduce, even when no single contrast is forced to vanish. We compute the attainable contrast space from an encoder's equivalence classes and a fixed contrast design, without labels, loss, or a fitted model; projecting the recorded contrasts onto that space gives an empirical error floor for any unrestricted decoder on those classes. On a 140-rectangle siRNA interaction panel, a graph neural network's training-only feature mask merges 165 endpoint states into 90 classes and cuts the rank of the 140 interaction contrasts to 72. The resulting floor is 0.009980, which is 14.6% of the fitted model's interaction squared error; the fitted model reaches 0.068335, slightly worse than a control predicting no interaction at all. A minimum of three restored chemistry columns recovers full rank. Refitting without the mask removes the floor entirely, yet interaction MSE improves by only 0.000017 under the reported protocol, and the restored columns remain absent from every training input. On a released RNA-splicing predictor, whose encoding is injective on the measured states, the same computation returns the full design rank of 1,986 and a floor of exactly zero. These results separate what an encoding permits from what a fitted model achieves; they do not identify what limits the remaining error. The rank check needs no fits and bounds what any amount of training under a fixed encoding can recover. The project repository is available at this https URL.

---


### 75. [On the spectral properties of generative denoiser Jacobians](https://arxiv.org/abs/2609.36210)

**<font color=#1a73e8>作者：</font>** Alexandros Graikos, Nebojsa Jojic, Dimitris Samaras  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative denoising models, such as diffusion and flow-matching, learn to sample from complex distributions by training a deep neural network denoiser to recover clean data from noise-corrupted samples. While such models are typically compared on the quality of their synthesized samples, these metrics provide limited insight into how the underlying denoiser, which drives generation, differs. In this work, we propose to analyze the spectrum of the denoiser Jacobian as a tool to characterize these differences. Across pre-trained denoising models, we observe that better generative performance is associated with larger Jacobian eigenvalues. Motivated by this, we introduce a regularization scheme that controls the Jacobian spectrum by training the denoiser on perturbed inputs, with perturbations suppressing or amplifying Jacobian responses. On ImageNet, we test whether directly modifying the Jacobian spectral properties leads to improved generations. Our findings suggest that denoisers benefit from both strengthening responses along data-relevant principal eigen-directions and suppressing the noisy, data-irrelevant ones. This establishes the denoiser Jacobian as a useful tool for identifying differences between generative denoising models.

---


### 76. [EnergyEminence: Source-Aware Environmental Calibration and Evaluation in a Physics-Grounded Grid Digital Twin](https://arxiv.org/abs/2609.36215)

**<font color=#1a73e8>作者：</font>** Huy Trinh, Michael Mai, Yu Nong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Power-grid digital twins must combine data-driven prediction with physically meaningful state evolution while preserving the provenance of environmental observations. This paper presents an early-stage EnergyEminence testbed that couples an IEEE 118-bus-style graph-temporal predictor, nonlinear AC cascade simulation, and operator-dashboard-like temporal replay. In addition, we introduce a shared bounded calibration that converts wildfire-detection confidence and spatial extent into source-comparable wildfire interpretable and explainable evidence. We then evaluate it with visually diverse fire and hard-negative videos. Sixteen synthetic environmental videos are curated to generate 160 source-tracked grid scenarios, and a source-video-disjoint test yields 10 true positives, 8 false positives, 22 true negatives, and no false negatives. The errors occur in stressed, non-cascading scenarios conditioned on an unseen growing-fire source. Our diagnostic then reveals environmental shortcut learning that is obscured by scenario-level random splitting. The paper therefore contributes a data-centric and inspectable evaluation workflow for multimodal grid-resilience models, together with evidence supporting separation of environmental alerting from electrical cascade inference

---


### 77. [Preconditioned Physics-Informed Neural Operator Training](https://arxiv.org/abs/2609.36216)

**<font color=#1a73e8>作者：</font>** Shizheng Wen, Siddhartha Mishra, Marius Zeinhofer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators are typically trained in a supervised fashion, which requires a dataset to be generated with a classical solver. Training them physics-informed, i.e., purely from the governing equations, removes this large offline cost and allows fresh samples to be drawn at every optimization step, but has so far been limited to simplified problems and trails supervised training in accuracy. The obstacle is the ill-conditioning of physics-informed losses, which differential operators induce and which worsens as the discretization is refined. We therefore propose a preconditioned residual loss function and show mesh-independent conditioning for elliptic problems and greatly improved conditioning for saddle point problems. Realized through geometric and algebraic multigrid, the construction applies to linear and nonlinear equations, steady or time-dependent, on structured and unstructured meshes, is agnostic to the neural operator architecture, and adds no cost at inference. On the Poisson, Allen-Cahn and stationary Stokes equations, the resulting label-free training matches supervised training and is four to twenty-five times more accurate than previous physics-informed operator learning methods.

---


### 78. [Sparse-View Interpretable 3D Animal Behavior Representations for Neural Encoding and Decoding](https://arxiv.org/abs/2609.36217)

**<font color=#1a73e8>作者：</font>** Xinming Dai, Qihang Jin, Tianshu Tan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A deeper understanding of brain function requires a precise, structured characterization of this http URL, extracting behavioral representations from video in a form suitable for scientific analysis remains a fundamental challenge. Many prior studies represent behavior via pose estimation or nonlinear video embeddings. However, pose tracking discards rich information beyond predefined keypoints, while nonlinear video embeddings lack interpretability. We address this limitation with SABLE (Sparse-view Animal Behavior Latent Embeddings), a self-supervised framework that leverages a geometric inductive bias to learn behavior this http URL augmenting a multi-view transformer with priors from monocular depth and pose estimation, SABLE reconstructs 3D animal behavior from extremely sparse views while learning explicit 3D latent structure. Without ground-truth 3D labels, it reliably recovers 3D behavior from two-view videos, whereas state-of-the-art (SOTA) methods fail or yield degenerate solutions. Across the International Brain Lab and Cheese3D datasets, we demonstrate that SABLE learns 3D representations that match or exceed prior SOTA performance in neural encoding and decoding. Once pretrained across animals, SABLE serves as an off-the-shelf model that generalizes zero-shot to unseen animals without animal-specific calibration or retraining. Our method establishes 3D-aware video embeddings that capture complex behavior, opening new avenues for studying brain-behavior relationships.

---


### 79. [Mutually Adversarial Self-Training with Evolving Data for Unified Multimodal Models](https://arxiv.org/abs/2609.36224)

**<font color=#1a73e8>作者：</font>** Wentao Zhou, Weijie Gan, Jiayun Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models (UMMs) combine image generation and visual understanding in a shared backbone. Since generation and understanding are inverse tasks, recent studies self-train UMMs by letting the two branches cooperatively supervise each other. We introduce MATE (Mutually Adversarial self-Training with Evolving data), a reinforcement-learning-based post-training framework in which the two branches instead challenge each other, and the challenges evolve as the model trains. MATE lets generation and understanding take turns to be challenger and solver. Given an image, the understanding branch proposes several candidate descriptions that the generation branch must turn back into similar images, and vice versa. The candidates are screened for consistency with the image or prompt they were proposed from, and the solver is trained on the candidate it handles worst. The adversary thus comes from the model's own outputs, and no separate adversary is trained. Moreover, the candidates that defeat one branch become the sources of the next challenges to the other in the next epoch, which keeps the challenges evolving with the model and turns the training into self-play in data space. On Janus-Pro-1B, MATE improves GenEval by 2.4 points, DPG-Bench by 1.7 points, and the average over nine understanding benchmarks by 0.7 points, while strengthening consistency across repeated image-text cycles.

---


### 80. [An Empirical Study and Assessment of EU AI Act Compliance Checkers](https://arxiv.org/abs/2609.36228)

**<font color=#1a73e8>作者：</font>** Zhen Tao, Alize Kahraman, Shidong Pan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The EU AI Act introduces extensive compliance requirements for organizations that develop, deploy, or integrate AI systems. Many of these requirements are directly relevant to security and privacy, while also addressing closely related issues such as data governance, transparency, accuracy, and robustness. However, stakeholders such as small-to-medium businesses and individual developers often lack the legal expertise required to interpret these obligations and translate them into engineering and governance practices. This disconnect creates challenges for implementing the EU AI Act and may lead to missing safeguards or misdirected development and deployment efforts. To address this, various automated EU AI Act compliance checkers (AIACCs) have emerged, claiming to streamline compliance assessments and provide practical guidance. In this paper, we present the first empirical study and assessment of AIACCs. We characterize 12 mainstream AIACCs across multiple dimensions, evaluate their legal coverage and alignment, and analyze checker-generated compliance reports for structure, determinacy, and actionability. We find that the quality of AIACCs varies significantly and that they currently can only serve as early-stage orientation tools. Specifically, we observe inconsistent interaction modes and user-friendliness, a tendency to overly simplify or omit key obligations, and a failure to provide determinate, actionable guidance. As a result, reliance on the current generation of AIACCs may foster a false sense of compliance. With our study, we provide a critical baseline of the current AIACC landscape. We further offer design principles for the implementation of more reliable compliance-support tools.

---


### 81. [MERID: Multimodal Exploration via Recursive Self-Improvement Agents for Major Depression Analysis](https://arxiv.org/abs/2609.36235)

**<font color=#1a73e8>作者：</font>** Lei Liu, Zhaokang Liang, Qingcheng Zeng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Major depressive disorder (MDD) severely impacts daily activities and quality of life. Detecting MDD involves multimodal data, such as interview recordings and sensor measurements. This is particularly challenging, as these heterogeneous modalities often demand distinct, customized prediction pipelines. Existing efforts to address this challenge have explored both manually engineered multimodal architectures and agent-assisted pipeline development. Despite their progress, it remains challenging to autonomously revise pipelines based on experimental feedback and carry verified improvements forward into subsequent designs. To this end, we propose Multimodal Exploration via Recursive Self-Improvement Agents for Major Depression Analysis (MERID). The framework develops depression pipelines through experience-based recursive self-improvement (RSI). Grounded State Construction (GSC) grounds experience by aligning multimodal records with subject-level depression targets. Coupled Pipeline Exploration (CPE) jointly modifies representations, fusion, and predictors to build successor pipelines for classification and severity estimation. Evidence-Guided Evolution (EGE) guides revisions through feedback and verifies gains under uncertainty in small depression cohorts before inheritance. Extensive experiments on depression benchmarks show that MERID achieves the best results on multiple tasks compared with multimodal and agent-based baselines. Further analysis highlights the value of acoustic and linguistic cues for depression detection. Our code is available at this https URL

---


### 82. [Transversal Pooling Neural Networks](https://arxiv.org/abs/2609.36237)

**<font color=#1a73e8>作者：</font>** Emily J. King, Dustin G. Mixon, Michael Perlmutter 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many learning tasks require stability to small transformations while retaining sensitivity to larger ones. We introduce \emph{transversal pooling neural networks}, which generalize spatial max pooling to affine group actions. We establish equivariance to a chosen subgroup and derive explicit stability bounds for individual pooled wavelet coefficients under affine perturbations of the input. Experimentally, we demonstrate the utility of our networks in low-data environments and for predicting tropical cyclone intensification.

---


### 83. [ChronoSRL: Temporal Geometry for Self-Supervised Reinforcement Learning](https://arxiv.org/abs/2609.36238)

**<font color=#1a73e8>作者：</font>** Nico Bohlinger, Jan Peters  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A goal that is close in space can be far away in time. Obstacles, terrain, and the agent's own capabilities determine how long it takes to get there. Yet, critics in contrastive and survival reinforcement learning do not measure the distances in their representation space in units of time. We therefore introduce ChronoSRL, which gives the critic's embeddings an explicit temporal geometry. The distance between state-action and goal embeddings is trained to match the time that the agent takes to reach the goal (goal-reaching time), while goals that were not reached, and goals from other trajectories, are pushed at least one discount horizon away. Furthermore, reaching a goal quickly once does not mean that reaching it is reliable in general, so the policy should not follow the temporal distance directly. Instead, we build on survival reinforcement learning and predict from our temporal embeddings not only the full distribution of goal-reaching times but also the time spent near the goal. Thereby, the policy is trained to favor actions that reach the goal sooner and more reliably and that keep the agent near it. ChronoSRL learns faster and reaches higher performance than contrastive, action-chunked contrastive, and survival reinforcement learning baselines on seven standard locomotion and navigation benchmarks, even with much smaller networks. To test the limits of self-supervised reinforcement learning, we introduce velocity tracking, goal-position reaching, and box climbing tasks with a quadruped robot in a realistic sim-to-real locomotion setup, and show how the shaping terms that are typical for robotics can be naturally incorporated into our framework. ChronoSRL is the only one of the tested self-supervised reinforcement learning methods that learns to stay at the commanded velocities and goal positions, and climbs the highest boxes.

---


### 84. [Can Representation Learning Decouple from Loss Minimization? Polar Updates Have an Answer](https://arxiv.org/abs/2609.36240)

**<font color=#1a73e8>作者：</font>** Akash Kumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Does representation learning stop when the training loss stops improving? We study this question for matrix Muon, whose polar-normalised updates have a step length set by the gradient's rank rather than its norm. Near the edge of stability, full-batch Muon on teacher-student problems enters approximately period-2 loss oscillations that persist for thousands of steps: the cycle-mean loss stays flat or rises, yet the weights keep moving and the learned features continue to align with the teacher subspace. For linear teacher-student learning toys, we derive explicit cycle and alignment formulas and conditional plateau and decay bounds. For a population mean-field ReLU model, we prove that, under stated dimension, initialisation and small-head conditions, the leading eigenspace of the average gradient outer product (AGOP) recovers the teacher subspace exactly during a loss plateau, before the loss later drops. In all 33 ReLU, GELU and SiLU teacher configurations we study, direction-only alignment metrics show the student AGOP aligned with, or still aligning to, the teacher subspace during the period-2 oscillations; projected head refitting on selected configurations shows that the learned directions are useful for prediction, and further measurements distinguish AGOP alignment from weight-mass concentration. In deep residual ReLU students, freezing the downstream layers while the first layer trains with full-batch exact polar updates recreates a nearly flat cycle-mean loss with improving input-AGOP alignment; freezing and unfreezing switch between this plateau and loss decrease, and the effect is sensitive to momentum and to the choice of orthogonaliser.

---


### 85. [Think Before You Restore: Risk-Aware Manchu Manuscript Restoration with Stroke-Guided Attention](https://arxiv.org/abs/2609.36243)

**<font color=#1a73e8>作者：</font>** Mingqiu Liang, Dongdong Wang, Siyang Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Full-page blind restoration of historical Manchu manuscripts is challenging due to scarce annotations, unknown degradation regions, and fragile connected strokes. Generic restoration models may improve visual quality but often modify intact content, leading to over-restoration. We propose SAGE-Restore (Stroke-Aware Gated rEstoration), a selective restoration framework that first assesses where restoration is needed and then uses this assessment to guide restoration candidate generation and pixel-level selection. Its encoder predicts patch-level repair probabilities from complementary appearance and stroke-structural cues to condition restoration candidate generation, while the corresponding repair logits are refined into a pixel-level soft gate that selectively controls where the restoration candidate is applied. We further introduce a fidelity-aware evaluation protocol that jointly measures degraded-region recovery, intact-content preservation, and their balance. SAGE-Restore achieves the highest R-Recovery (0.463) and RFS (0.626), while maintaining high U-Fidelity (0.968), demonstrating an effective balance between restoration and content preservation.

---


### 86. [CoRe: Co-Evolving Reward Models for Mitigating Latent Reward Hacking in Video Diffusion Models](https://arxiv.org/abs/2609.36245)

**<font color=#1a73e8>作者：</font>** Zhaolong Su, Yujin Han, Feng Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Latent reward models (LRMs) enable efficient alignment of video diffusion models by scoring intermediate states directly in latent space. However, we find that optimizing against a fixed latent reward rapidly leads to latent reward hacking: the predicted reward stays high while perceptual and motion quality deteriorate. Our analysis identifies distributional escape as the central cause: within a few hundred updates, the generator moves beyond the reward model's training support, where its scores no longer reflect video quality. Based on this insight, we introduce CoRe, a co-evolving reward framework that treats latent-space alignment as a dynamic interaction between the generator and the reward model. Rather than optimizing against a stationary proxy, CoRe continually refits the reward model on the generator's current samples while anchoring it to real-video preferences, so the generator cannot gain reward by drifting away from the data. On Wan2.1-T2V-1.3B, experiments show that CoRe consistently improves generation quality over both the pretrained model and prior alignment methods, while avoiding the quality collapse of fixed-reward optimization.

---


### 87. [Action Chunking Proximal Policy Optimization with Feedback Correction](https://arxiv.org/abs/2609.36250)

**<font color=#1a73e8>作者：</font>** Sanghyun Hahn, Jonghyun Choi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Action chunking provides temporal abstraction in reinforcement learning by selecting short action sequences instead of individual actions, but many existing approaches face two limitations in high-dimensional robotic control. First, many rely on value functions over action chunks, which can be difficult to learn as action dimensionality and chunk length grow. Second, executing chunks open-loop removes within-chunk feedback, limiting reactivity in contact-rich tasks. We present Action Chunking PPO (ACPPO), a PPO extension that uses a chunked actor while retaining a standard state-value critic, thereby avoiding chunked Q-functions. We further propose ACPPO-Corr, which augments the chunk planner with a stepwise feedback corrector that adjusts planned actions online within each chunk. Across 25 simulated robotics tasks from IsaacGym and Bi-DexHands, spanning locomotion, arm manipulation, and dexterous hand-object interaction, ACPPO-Corr achieves the strongest aggregate performance among evaluated methods and performs best on both decision-frequency-sensitive and decision-frequency-neutral task subsets. Ablations show that moderate chunk lengths work best and that corrector regularization is important for balancing chunk-level planning with local feedback. These results suggest that action chunking can be effective in online PPO when chunk-level planning is paired with closed-loop correction. The code is available at: this https URL.

---


### 88. [The Signed Geometry of One-Shot Recourse: On-Path Validity and the Signed-Curvature Criterion](https://arxiv.org/abs/2609.36252)

**<font color=#1a73e8>作者：</font>** Hazar Yueksel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Closed-form recourse moves a rejected user along the unit gradient $\hat g$ of the classifier score $f$ by the promised distance $d_p=|f(x)|/\|\nabla f(x)\|$, at which the linearized score reaches zero. We ask when this one-shot step succeeds and what additional model queries change. To leading order the step ends on the favorable side exactly when the path curvature $\kappa=\hat g^\top\nabla^2 f(x)\,\hat g$ is nonnegative. Across 80 shallow models, the fraction of rejected users whose step ends there and the fraction with $\kappa\ge0$ correlate at $r=0.985$, although on Fashion-MNIST the first falls below the second by 8.2 points on average. No rule that uses only the score value and gradient can be valid for every score with path curvature bounded by $K$ without overshooting some by order $Kd_p^2/\|\nabla f(x)\|$. When the curvature is also Lipschitz and the step is short, one evaluation of $f$ at the promised point attains the minimax rate among deterministic one-query rules that know the curvature bound and its Lipschitz constant, and split-conformal calibration makes such a rule reach the first crossing or abstain with probability at least $1-\delta$. Training with an asymmetric curvature penalty lets 99-100% of paths cross within the promised step on undershoot-prone shallow data, at about 4-22 times the overshoot of symmetric penalties (Fashion-MNIST, COMPAS). Because $\kappa$ and $d_p$ depend on how the score is scaled, part of this gain can be a longer promised step, and at matched validity a smaller audit of briefly trained models finds no uniform advantage over tuned inflation. Where a per-user line search along the ray is affordable, it is exact to grid resolution and preferable.

---


### 89. [CyFA: Linear Sequence Modeling with Relative-Time-Partitioned Memory](https://arxiv.org/abs/2609.36259)

**<font color=#1a73e8>作者：</font>** Yixiao Chen, Shuojin Yang, Shi-Min Hu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear RNNs offer linear-time sequence processing and constant-memory decoding, but their fixed-size recurrent states must accommodate all past key--value associations. Existing forgetting mechanisms and Delta Rule updates reduce interference by selectively clearing or correcting the state, yet earlier associations can still become difficult to retrieve. We introduce CyFA (Cyclic Flow Attention), a Linear RNN with relative-time-partitioned memory. At each step, a learned clock controls the cyclic transport applied jointly to the key and value states before the current key--value pair enters the age-zero slot, thereby organizing stored associations across relative-time slots. We further derive an exact change to absolute-clock coordinates that expresses CyFA as two scalar-decay linear attention recurrences and enables efficient chunk-wise training. Across 400M--1.4B pretraining experiments with matched recurrent-state sizes, CyFA improves recall-intensive performance while maintaining competitive language modeling and high computational efficiency. At 400M, CyFA outperforms KDA on FDA (42.60 vs. 26.07) while requiring only 46.7% and 48.3% of KDA's forward and backward core-operator execution times, respectively. Our code is publicly available at \href{this https URL}{this https URL}.

---


### 90. [Paired Multimodal Scaling Laws](https://arxiv.org/abs/2609.36263)

**<font color=#1a73e8>作者：</font>** Marcus Ma, Shrikanth Narayanan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing multimodal scaling laws fit multimodality terms empirically after testing and never vary how much data is multimodally paired at fixed data budgets. We investigate how, under the same total data per modality, changing the number of paired data affects loss curves in multimodal classification tasks. We train models in three different environments and run experiment sweeps varying data sizes and pairing budget. Pairing ratios have a dramatic impact on loss and this impact is directly tied to how much information synergy the task contains. Only paired data is able to reduce synergistic loss, while unpaired data can reduce redundant or unimodal information up until unimodal floors. Unlike traditional scaling laws where loss drops immediately in power law decay, synergy acquisition is gated, requiring a critical threshold of paired data before synergistic loss falls at all. We introduce a new family of multimodal scaling laws where total data-attributable loss is the sum of four individual power laws corresponding to the four different information channels of redundancy, a unique channel per modality, and synergy, and show how this law is both more theoretically sound and empirically valid across our experiments. This law predicts multimodal loss in our experiments more accurately than existing laws, with 3.2% error on fit tests versus 10.4% error for the best pairing extension of published laws.

---


### 91. [Stochastic Optimization Under Power-Law Spectra: Tight Bounds and Shuffling Analysis](https://arxiv.org/abs/2609.36271)

**<font color=#1a73e8>作者：</font>** Thomas Dybdahl Ahle, Yaroslav Bulatov, Christopher De Sa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work has established that power-law spectral conditions on data enable tight convergence bounds for deterministic gradient descent, resolving the conflict between classical exponential bounds and observed power-law learning curves. In this work, we extend this result to the stochastic regime of high-dimensional machine learning. We provide two main contributions: (1) We generalize the power-law spectral theory to Stochastic Gradient Descent (SGD), showing that the same spectral exponents govern stochastic dynamics; (2) For the fundamental case of isotropic Gaussian data, we provide a precise analysis of data shuffling, deriving exact constants that prove Single Shuffle is strictly superior to Flip-Flop and IID sampling. Our results bridge the gap between abstract spectral theory and practical stochastic training choices, offering a unified picture of how data geometry drives optimization speed.

---


### 92. [From Surfaces to Volumes: Registered Geometry for Protein Representation Learning](https://arxiv.org/abs/2609.36277)

**<font color=#1a73e8>作者：</font>** Siyuan Chen, Cai Zhou, Jinrui Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing protein geometry models typically represent molecular surfaces using local geometric features such as sampled points, normals, and curvature. While effective for capturing exposed molecular shape, these representations do not explicitly model the volumetric organization beneath the surface or provide a consistent coordinate system for residue-wise volumetric structure. We introduce Protein-TetSphere, a registered residue-wise volumetric representation for proteins. Each protein chain is tetrahedralized to obtain local volumetric regions associated with individual residues, which are then registered to a shared fixed-topology tetrahedral reference and represented in a common Laplacian basis. This registration establishes consistent volumetric coordinates across residues, enabling local three-dimensional deformation to be integrated with surface and chemical information in a multimodal protein representation. We evaluate Protein-TetSphere on ligand-binding pocket classification, protein--protein interface prediction, and de novo protein binder design. Across the three tasks, Protein-TetSphere improves ligand-binding pocket balanced accuracy from $0.795$ to $0.826$, Pinder-Pair/Site AUROC from $0.914/0.852$ to $0.932/0.866$, and binder-design success from $14.95\%$ to $19.90\%$ on the BoltzGen Challenge Set and from $27.62\%$ to $32.19\%$ at the ProtDBench backbone level. These results show that registered volumetric geometry provides complementary spatial information beyond molecular surfaces across protein recognition, interaction, and design.

---


### 93. [GNA: Granular Neighbor Assembly for Retrieval-Augmented Multivariate Time-Series Forecasting](https://arxiv.org/abs/2609.36281)

**<font color=#1a73e8>作者：</font>** Vincent Uhse  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep forecasters predict from a fixed-length lookback window, and lengthening it gives diminishing returns at a growing cost. Retrieval augmentation instead shows the model how similar past situations continued. Retrieving a whole past window gives every variate the continuation of the same past moment. In multivariate series, however, the best past match differs from variate to variate. We present GNA (Granular Neighbor Assembly), a retrieval layer for forecasting backbones that assembles neighbors at two granularities: whole past windows, which keep the variates coherent, and per-variate neighbors, in which each variate takes its future from its own best-matching past. A learned gate decides, per forecast step and variate, how much to trust these futures against a persistence forecast, next to the backbone's own forecast. Candidates come from an embedding trained to predict each window's future, and retrieval is strictly causal: a past window is used only once its future has been observed. With the same lookback for every model and the same retrieval constants for all datasets, GNA improves two Transformer backbones in 85 of 96 dataset-horizon settings, gives the lowest MSE on 8 of 12 standard benchmarks and beats its backbone in every seed on 10 of them. Both granularities are needed, and neighbors of mismatched queries are worse than none. Retrieval helps most where the lookback says least: the gate shifts trust to retrieved futures further ahead. Where it fails, on hourly non-stationary series at long horizons, the loss is consistent with a drifting level of the retrieved futures.

---


### 94. [The Universal Classifier for Graph Learning](https://arxiv.org/abs/2609.36302)

**<font color=#1a73e8>作者：</font>** Ben Finkelshtein, André Linhares, Petar Veličković 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While foundation models have revolutionized natural language processing and computer vision by leveraging universal vocabularies, Graph Machine Learning (GML) remains fractured due to the absence of a unified feature and structural representation across diverse domains. Existing works claiming to be Graph Foundation Models (GFMs) are typically restricted to node-level predictions or require fixed feature dimensions, failing to provide a truly task-agnostic backbone for the full spectrum of graph learning applications. In this paper, we introduce the Universal Classifier (UC), which supports arbitrary feature and class cardinalities, unifying node-, edge-, and graph-level objectives under a single similarity-based classification objective. The UC reformulates all node-, edge-, and graph-level prediction tasks as maximizing similarity in the latent space: by lifting heterogeneous features and labels into 3D latent tensors, the model learns transferable features independent of specific input schemas. This architecture allows a single pre-trained model to generalize to node classification, node regression, and link prediction across unseen graphs with varying feature semantics. Experiments show strong zero-shot transfer performance across node-, link-, and graph-level tasks.

---


### 95. [HeurEvo: Agentic Evolution of Hybrid Solver-Augmented Heuristics for Time-Critical Mathematical Optimization](https://arxiv.org/abs/2609.36303)

**<font color=#1a73e8>作者：</font>** Feijie Wu, Hugo Barbalho, Konstantina Mellou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in agentic heuristic design use AI agents and execution feedback to automate algorithm discovery for challenging optimization problems. In many practical settings, high-quality solutions must be obtained under strict runtime constraints, motivating hybrid approaches that combine problem-specific heuristics with powerful mathematical programming solvers. However, existing approaches typically improve heuristic components within predefined procedures or tune solver configurations in isolation. This limits holistic adaptation of where to allocate computation, how to leverage solvers, and how to refine the overall algorithmic structure. To address these limitations, we propose HeurEvo, an automated plan--code--component co-evolution framework that jointly evolves the high-level algorithmic structures, their implementations, and a shared pool of reusable components. A planner determines which algorithmic components to use, how to combine them, and how to allocate runtime across stages, a coder realizes the resulting plan as executable code, while a component evolver updates the shared component pool. Within an island-based evolutionary framework, plans and implementations co-evolve with feedback from an interpreter agent that analyzes execution results and identifies opportunities for improvement. Across diverse combinatorial optimization benchmarks and challenging MIPLIB instances, HeurEvo finds high-quality solutions within tight runtime budgets, often matching or surpassing state-of-the-art optimization solvers given hours or days of computation. On several nonlinear geometry problems such as hexagon packing, it also improves upon the best previously reported results. These results highlight the value of jointly searching over algorithmic structure and implementation for agentic heuristic design.

---


### 96. [Cheap and Powerful Tests for Supervised Subspaces: Per-Component Inference for PLS](https://arxiv.org/abs/2609.36307)

**<font color=#1a73e8>作者：</font>** Paweł Lenartowicz, Hubert Plisiecki  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Partial Least Squares (PLS) regression extracts a few outcome-aligned directions in a high-dimensional X and is widely used across applied science, but inference on the resulting fit is either expensive, biased and discouraged, or absent. We reduce inference to held-out OLS refits of the supervised subspace, a primitive shared by PLS, supervised PCA, and linear probes, and supply two tests using held-out correlations: a Nadeau-Bengio corrected asymptotic t-test as a fast approximation, and a permutation test with comparable power, finite-sample valid under outcome-predictor independence and iid rows. Held-out predictions are unchanged under any orthogonal rebasing of the supervised span, so an interpretable basis such as varimax inherits the joint claim but not a per-axis p-value; per-component claims come from a fixed-sequence test on the PLS extraction order. We validate on synthetic geometries, two NIR chemometric datasets, and cross-lingual word-embedding regressions; the exact test also transfers to supervised PCA and a ridge probe. The proposed tests have more power than CV-permutation-Q^2, at a fraction of its cost. A pre-run check on n and the spectrum of X says when the approximation is safe. We release a Rust library with Python, R, and Julia bindings, plus a Python text pipeline.

---


### 97. [CheatBench: Measuring Reward Gaming in AI Agents](https://arxiv.org/abs/2609.36308)

**<font color=#1a73e8>作者：</font>** Long Phan, Stephen K. Yang, Jason J. Lim 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has helped AI agents solve increasingly difficult tasks, but high rewards do not always reflect the work users intended. In recent incidents and controlled evaluations across the AI industry, agents trained to maximize reward have accessed unauthorized information, attempted to evade monitoring systems, and even breached sandbox protections to attack external systems. As agents become more capable, this behavior could pose increasingly serious risks. To measure this problem, we introduce CheatBench, a benchmark of cheating in AI agents across mathematical research, knowledge work, coding, visual tasks, and other domains. Its environments combine challenging assignments with opportunities to cheat, allowing researchers to study how agents pursue a goal when honest work is difficult. CheatBench supports comparisons across models and task categories, providing a testbed for measuring and reducing cheating as agents take on more consequential responsibilities. We publicly release CheatBench at this https URL

---


### 98. [Learning Samples Importance: Parameterizing Dual Variables in Everywhere Learning](https://arxiv.org/abs/2609.36310)

**<font color=#1a73e8>作者：</font>** Ignacio Boero, Jonathan Nixon, Alejandro Ribeiro  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Everywhere learning provides a principled framework for training AI models under constraints that must hold throughout the data distribution. In the dual domain, these pointwise constraints give rise to functional dual variables. In this work, we propose to learn these dual variables, motivated by the fact that their values encode useful information about the underlying constrained problem. By representing the dual variable as a parametric function of each sample, we enable the learned multiplier to be evaluated on new, unseen samples. This contrasts with standard empirical dual formulations, which assign an independent multiplier to each training sample. We characterize the error in the recovered primal solution induced by restricting the dual variable to a parametric function class and show that it is controlled by how well this class approximates the optimal statistical multiplier. Moreover, we show that the learned parametric multiplier retains the sensitivity interpretation of the optimal statistical multiplier, yielding approximate sensitivity guarantees that extend beyond the samples used for training. We empirically validate our theory across a variety of everywhere learning tasks, showing that the resulting constrained problems can be solved efficiently and that the learned dual variables provide meaningful representations of sample-level sensitivity.

---


### 99. [Fractional State Space Transition for Long Sequence Modeling](https://arxiv.org/abs/2609.36314)

**<font color=#1a73e8>作者：</font>** Ivan Kobyzev, Abbas Ghaddar, Ali Nasiri-Sarvi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State Space Models (SSMs) compress sequence history into a bounded recurrent state, making the resulting memory law a central architectural choice for long-context performance. Most modern SSMs rely on ODE-based dynamics that lead to exponential forgetting, limiting their ability to retain information over broad temporal ranges. We introduce FRAC, a selective SSM architecture derived from fractional dynamics that replaces this exponential decay with power-law long memory. To make fractional dynamics practical, FRAC approximates the heavy-tailed target kernel with a finite-state, log-spaced sum of exponential modes. This construction turns fractional memory into an efficient recurrent module with parallel training and prefill, while retaining bounded-state autoregressive decoding. Extensive experiments, including 1.3B-parameter language modeling, demonstrate that FRAC consistently improves long-context performance over state-of-the-art SSM baselines while staying competitive on short-context. These results show that fractional dynamics provide a practical and effective prior for long-context SSMs.

---


### 100. [PyroStack: A Multi-Band Spatio-Temporal Sub-Daily Dataset for Wildfires in the United States](https://arxiv.org/abs/2609.36315)

**<font color=#1a73e8>作者：</font>** Arya Kondur, Giosue Migliorini, Cameron Schmitt 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wildfires are an increasing hazard to ecosystems, air quality, and human systems, creating a growing need for datasets that support systematic development and evaluation of models for predicting fire spread across diverse landscapes. Effective prediction requires integrating meteorological conditions, fuels, vegetation, and topography at spatial and temporal resolutions suitable for both physical simulation and data-driven approaches. However, existing datasets often lack the resolution and coverage needed to capture these interacting controls. The PyroStack dataset addresses this gap by providing a harmonized, event-based collection of wildfire and environmental data across the contiguous United States and Alaska. It integrates satellite-derived fire observations with atmospheric reanalysis, vegetation, fuel characteristics, and topographic information into a unified framework spanning 6994 wildfires that occurred between 2012 and 2024 across a wide range of ecosystems and climate conditions. PyroStack offers spatial resolutions ranging from 30 m to 9 km and hourly temporal resolution, along with fire progression data at 12-hour intervals to support model initialization and evaluation. By combining broad spatial coverage with fine spatial and temporal detail, the dataset enables systematic analysis of wildfire dynamics and supports both physics-based and machine learning approaches, providing a foundation for benchmarking and improving fire spread models, with future extensions aimed at incorporating additional regions and fire suppression data streams to further advance wildfire prediction.

---


> [!TIP]
> 当前位于：**51-100**（第 2/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-447](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
