# 📦 其他研究 | 2026年11月11日

> 本类共 **520** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**451-500**（第 10/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-520](./part-11.md)

---

### 451. [PhysOPSD: Code as Privilege for Physically Plausible Video Generation](https://arxiv.org/abs/2611.12411)

**<font color=#1a73e8>作者：</font>** Harold Haodong Chen, Rui Peng, Lingteng Qiu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While modern video generative models achieve remarkable visual fidelity, they remain noticeably brittle when generating physically plausible dynamics and complex interactions. Targeted post-training is crucial, yet supervised fine-tuning suffers from offline state mismatch, and reinforcement learning is hindered by sparse, ill-defined physical reward functions. On-Policy (Self-)Distillation (OPSD) reconciles on-policy rollouts with dense corrective feedback, shifting the core challenge to designing effective privileged context. However, conventional modalities fall short: text prompts are inherently declarative, whereas real reference videos heavily entangle physical laws with visual appearance without parametric control. To this end, we propose PhysOPSD, introducing executable code as privileged physical context for video generation. Unlike static visual observations, executable code instantiates an editable physical world with intrinsic abstraction and controllability. Powered by PhysOPSD-Engine, we translate real-world physical scenarios into verifiable simulation programs. PhysOPSD then incorporates (i) dual-level physical privilege to bridge the information gap via an intermediate bottleneck, alongside (ii) controlled physical variations under shared rollout noise to expose causal dynamic shifts. Extensive experiments demonstrate that PhysOPSD substantially improves physical plausibility across diverse backbones, outperforming SFT and RL baselines with only $3$K samples, while preserving general video generation quality.

---


### 452. [Optimal Rates for Adaptive Private $k$-PCA](https://arxiv.org/abs/2611.12419)

**<font color=#1a73e8>作者：</font>** Johanna Düngler, Amartya Sanyal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Given $n$ i.i.d. random matrices $A_i \in \mathbb{R}^{d \times d}$ with common expectation $\Sigma$, the goal of \emph{Differentially Private Stochastic PCA} is to identify a $k$-dimensional subspace capturing the leading variance directions of $\Sigma$, while preserving differential privacy~(DP) for each individual sample $A_i$. \citet{dungler2025iterative} introduced \kdppca, the first algorithm to simultaneously (1) achieve sample complexity $n=\widetilde O(d)$ for sub-Gaussian data, (2) adapt its privacy noise to the intrinsic randomness of the data, and (3) extend seamlessly to any target dimension $k\le d$. However, its sample complexity has a suboptimal dependence on $k$. We propose the first algorithm that achieves optimal sample complexity in both $d$ and $k$, while retaining properties (2) and (3) of \kdppca. Additionally, prior utility guarantees require a minimum sample size with exponential dependence on the eigengap. Our method removes this dependence. It also improves the dependence on spectral parameters, matching known lower bounds for the spiked covariance model. Unlike deflation-based approaches like \kdppca, our algorithm updates the full $d\times k$ subspace jointly rather than one eigenvector at a time. This non-deflation structure simplifies the algorithm, reduces the number of hyper-parameters, and improves computational efficiency, particularly when using block linear algebra libraries.

---


### 453. [Two-Phase Rapid Simulation-Based Inference with Differentiable Simulators](https://arxiv.org/abs/2611.12422)

**<font color=#1a73e8>作者：</font>** Uros Zivanovic, Rahul Srinivasan, Roberto Trotta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Rapid Simulation Based Inference (RSBI), a diffusion-based variational approach to likelihood-free Bayesian inference that achieves high sampling efficiency under large prior-to-posterior volumes. RSBI builds on advances in Schrödinger Bridge (SB) diffusion sampling to handle multi-modal posteriors, with an initial likelihood supplied by a distance measure via a differentiable simulator. The key innovation of this initial surrogate likelihood is that it gives a highly efficient proposal distribution, replacing sequential rounds of other methods with an efficient one-shot proposal. Subsequent refinement then transports the proposal to the true posterior as specified by the simulator and the original prior. The SB sampler is warm-started from the proposal, and its energy is corrected by a neural likelihood ratio that is learned only where the proposal places mass. As a variational method, RSBI does not suffer from prior leakage commonly observed in standard sequential posterior estimation methods. To improve mode coverage we optionally utilize the well-tempered meta-dynamics framework, which also encourages exploration of the prior volume. We observe strong performance on standard SBI benchmarks, particularly when the prior volume is increased relative to the ground truth posterior, achieving a performance degradation of only $\sim5\%$ on Two Moons under a highly constrained simulation budget. Additionally, we evaluate RSBI's performance for gravitational wave ring-down posterior estimation, in a real-world physics benchmark inspired by black hole spectroscopy.

---


### 454. [UCB-min: Combining Bandits Under Variance Heterogeneity (Extended Version)](https://arxiv.org/abs/2611.12427)

**<font color=#1a73e8>作者：</font>** Lilia Izri, Benoit Groz, Silviu Maniu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-armed bandits are a natural framework for many real-world sequential decision problems, from recommender systems and clinical trials to educational test recommendation and online advertising. The performance of these algorithms depends on how they explore different arms, and exploration strategies range from variance-independent (e.g., UCB1) to variance-aware (e.g., UCB-V). In practice the reward variance of each arm is rarely known and varies widely across arms, and the reward support is often underspecified. In these cases no single rule is uniformly best: variance-independent methods are robust but loose when variances are small, while variance-aware methods are tight only when their variance estimates and the assumed support bound are reliable. Such heterogeneous, unknown variances arise in many settings, for instance when multiple objectives are scalarized into a single reward. We propose UCB-min, a per-arm adaptive meta-algorithm that selects, for each arm, the tighter of a variance-independent and a variance-aware exploration bonus, without prior knowledge of the variance regime and without reward normalization. We prove that, with UCB-V as variance-aware base, its regret is bounded by the sum of the two base bounds at the standard exploration constant, and by their per-arm minimum, up to a constant, for a larger one. We validate it on synthetic data, an educational tutoring task, and two group-recommendation benchmarks (MovieLens, Steam), showing that UCB-min consistently tracks the best base algorithm across diverse variance regimes and datasets.

---


### 455. [Can Frontier Auto Researchers Reconstruct Human Research Decisions in AI?](https://arxiv.org/abs/2611.12429)

**<font color=#1a73e8>作者：</font>** Shengyun Si, Junjie Chu, Ye Leng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific research has long been driven by substantial human effort, from reviewing prior work and identifying research gaps to designing specific solutions. Recent advances in harness-based agent systems have given rise to increasingly capable Auto Researchers, which can autonomously carry out these tasks and, increasingly, entire end-to-end research workflows. Yet despite their rapidly growing capabilities, how closely the research decisions and outputs produced by auto researchers align with those of human experts remains underexplored. We investigate this gap through the lens of research reconstruction and study: Given comparable research context, how similar are the research decisions and outputs produced by Auto Researchers to those of human researchers in AI research? To answer this question, we introduce AutoResearcher-Human Research Similarity (AutoHRS), a stage-wise evaluation framework for assessing how faithfully auto researchers reconstruct human research artifacts across different stages of the scientific workflow. Using 152 ICLR oral papers as our corpus, we generate 456 research trajectories spanning different stages of the research process. Applying AutoHRS to these trajectories, we find that current Auto Researchers frequently fail to recover key research decisions and their resulting artifacts across multiple stages of the research process.

---


### 456. [Patching Up Circuit Learning via Parameter Sharing](https://arxiv.org/abs/2611.12436)

**<font color=#1a73e8>作者：</font>** Charles Bricout, Gennaro Gala, Viacheslav Borovitskiy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probabilistic circuits (PCs) have emerged as generative models guaranteeing tractable probabilistic inference. However, tractability comes at the price of larger model sizes than in other generative models. As such, to scale PCs to high-dimensional data such as images, previous work has devised several parameter sharing techniques as well as fast evaluation protocols that consider learning PCs on independent image patches. In this work, we revisit this practice to highlight a surprising learnability issue: models that assume independence counterintuitively can yield better likelihoods than models that do not. To break this apparent bottleneck and to scale PCs further, we introduce a recursive parameter sharing construction (RePA) that fosters efficiency without assuming independence. We show empirically that RePA can greatly reduce time and memory consumption while yielding competitive likelihoods. Inspired by these results, we further generalize the approach to data modalities that do not inherently exhibit patch-structure (NoPA), such as tabular data, showing similar efficiency improvements, with marginal changes in likelihoods and sample quality on seven tabular datasets. Code available at this https URL.

---


### 457. [Occupancy Modelling of Biased Landslide Inventories: When Does Separating Occurrence from Recording Improve on Neutralisation?](https://arxiv.org/abs/2611.12437)

**<font color=#1a73e8>作者：</font>** Abdirashid Omar, Abdikadir Ugaas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Landslide susceptibility models are trained on inventories that record where landslides were seen, not where they occurred. The established remedy fits bias-describing variables and neutralises them when mapping. We adapt occupancy-detection modelling from ecology, treating several inventories as imperfect observers of one event and separating occurrence from recording, and ask when this improves on neutralisation. We use near-complete inventories of the 2018 Hokkaido Eastern Iburi, 2015 Gorkha and 2010 Haiti earthquakes with simulated reporting bias, and three real Gorkha inventories. Compared with standard practice, the occupancy model reduces road bias in 24 of 25 paired draws and raises AUC by 0.08-0.14 on Gorkha and 0.03 on Haiti, but only 0.01-0.02 on Iburi. Its median predicted-to-true landslide rate is 0.99 (range 0.44-1.89), against 0.24-0.30 for the baselines. Rescaling the baselines with the same anchor area corrects their median but leaves larger errors (range 0.20-4.34). Cell-level probabilities remain too extreme (calibration slope 0.59). Compared with the best neutralised model, AUC is higher on Iburi (by 0.03-0.07) and lower on Gorkha and Haiti (by 0.01-0.05). Transplant experiments tie the Iburi advantage to the structure of its true landslide pattern, not to its terrain or road network. In all eight settings with a low interaction gap, computable from biased records, neutralisation was at least as accurate, including a prespecified test on Haiti; a high gap did not guarantee an advantage. The real Gorkha inventories are slope-biased, not road-biased, and there the model brings no meaningful gain. Report-based catalogues remain the main untested case.

---


### 458. [MoSTE: Mixture of Spatio-Temporal Experts for Deepfake Detection in Videos](https://arxiv.org/abs/2611.12443)

**<font color=#1a73e8>作者：</font>** Charbel Yahchouchi, Nabyl Quignon, Noemi Roggero 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalizable deepfake video detection remains challenging because forgery artifacts vary substantially across manipulation types and often combine diverse spatial and temporal inconsistencies. Existing parameter-efficient adaptation methods typically rely on a single shared representation, rendering them prone to manipulation-specific bias and limiting transfer to unseen forgeries. To address this challenge, we propose Mixture Of Spatio-Temporal Experts (MoSTE), an adaptation framework that enables conditional specialization of forensic representations. Instead of forcing one adapter to model all forgery patterns, MoSTE decomposes adaptation into parallel spatial and temporal expert pools and dynamically routes tokens to the most relevant experts through an unsupervised token-level routing mechanism. This allows experts to naturally specialize in complementary forgery cues without requiring explicit manipulation labels or multi-stage training, while effectively transferring representations from CLIP to the video domain. Extensive experiments across cross-dataset and cross-manipulation benchmarks demonstrate that MoSTE sets a new state of the art in average generalization while preserving strong performance across diverse manipulation families. Additional analysis of expert routing and attention behavior reveals the emergence of expert diversity, suggesting that MoSTE learns complementary spatio-temporal forensic features. Code is available at this https URL

---


### 459. [Learning to Select Sparse Linear Solvers with Convolutional Neural Networks](https://arxiv.org/abs/2611.12475)

**<font color=#1a73e8>作者：</font>** Artemis Pados, Alan Edelman, Emmanuel Lujan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate convolutional-neural-network (CNN) based automatic solver selection for sparse linear systems, a problem of practical importance where solver performance varies dramatically with matrix sparsity structure. A CNN is trained to regress log timing ratios between candidate solvers using spy plot images of matrix nonzero structure as input, achieving strong prediction accuracy on both held-out SuiteSparse matrices and real-world matrices from high-performance simulation codes.

---


### 460. [Perturb, Aggregate then Reconstruct: Consensus Aggregation and Fourier-Attended Multi-Decoders for Reconstruction-based Multi-View Anomaly Detection](https://arxiv.org/abs/2611.12477)

**<font color=#1a73e8>作者：</font>** Yongho Son, Junyeong Yun, Je Hyeong Hong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-view anomaly detection is crucial for industrial inspection to identify defects hidden from single viewpoints. Yet, despite their strong success in single-view applications, reconstruction-based methods remain largely underexplored in multi-view settings. A key challenge in extending these methods lies in generating view-consistent pseudo-anomalies. To address this, we propose PAR, a reconstruction-based framework for enhanced multi-view anomaly detection. First, we introduce a feature perturbation strategy coupled with a consensus aggregation module that integrates these perturbed features across viewpoints to mitigate view-inconsistent anomalies and construct highly aligned pseudo-anomaly representations. Second, we employ a view-specialized multi-decoder architecture; by assigning a dedicated decoder to each view, we increase the model's representational complexity, enabling the generation of highly feasible, localized anomaly maps rather than less precise, view-agnostic reconstructions. Last, we incorporate Fourier attention into the decoders to emphasize global frequency-domain structures over local token evidence, effectively preventing identity mapping. Extensive experiments on the Real-IAD dataset demonstrate that PAR consistently outperforms state-of-the-art methods in sample-level, image-level, and pixel-level anomaly detection. Our code is available at this https URL.

---


### 461. [Brief introduction to post-quantum cryptography in industrial applications](https://arxiv.org/abs/2611.12479)

**<font color=#1a73e8>作者：</font>** Mateusz Żarski, Jarosław Miszczak, Cédric Crettaz 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The development of Post-Quantum Cryptography (PQC) is directly motivated by the necessity to secure information in the face of the quantum threat. This paper provides an overview of recent developments relevant to PQC adoption across several industrial applications, including IoT, healthcare, civil and infrastructure engineering, and defense. We present a brief, self-contained overview of PQC and its market positioning. We perform implementation experiments on selected quantum-safe methods and quantify several aspects, such as the quantum resources required to break common cryptographic schemes, as well as the performance of the most well-known PQC algorithms. We also discuss the resistance of different PQC classes to quantum attacks and the status of PQC implementations in different programming languages. Finally, we present benchmark results on KEMs and signature algorithms to help select the appropriate algorithm for a specific application based on criteria such as algorithm performance, data lifetime, and level of data sensitivity.

---


### 462. [Text Grouping Changes Completion-Time Comparisons in Long-Form Simultaneous Speech Translation](https://arxiv.org/abs/2611.12501)

**<font color=#1a73e8>作者：</font>** Hieu Minh Truong, Dung D. Le  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Does grouping translation updates before speech synthesis change the measured completion gap between two translators? We compare StreamAtt with its fixed-audio-history baseline on ten English-German talks. For each translation, we keep the intended text and its availability times fixed and vary how updates are grouped for synthesis. Four-second grouping increases StreamAtt's mean completion lead from 106.6 to 229.1 seconds with XTTS-v2, but reduces it from 169.5 to 146.5 seconds with Piper. Both produce shorter audio; different changes in playback idle account for the opposite effects. These directions recur on a separately selected twenty-talk panel. In continuing CosyVoice 3 sessions, grouping instead leaves paired audio unchanged and delays completion on nineteen of twenty blocks. A speech-timing comparison therefore needs to specify how text enters synthesis, not just which synthesizer is used. Recognition and automatic word timing describe the outputs, but do not establish translation accuracy or intelligibility.

---


### 463. [MARS: Multiscale Appearance-Residual Streams for Video Forgery Detection](https://arxiv.org/abs/2611.12508)

**<font color=#1a73e8>作者：</font>** Ahmed Y. Radwan, Shaina Raza  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalizing deepfake detection across facial manipulation and fully generated video remains challenging due to forgery traces varying with the manipulation method and scene content. Explicit spatial and temporal feature differences offer a way to capture this variation, but also respond to natural texture and motion, motivating their joint interpretation with appearance features. We investigate whether combining multiscale feature differences with adapted appearance representations improves detection across both forgery categories. We introduce Multiscale Appearance-Residual Streams (MARS), a two-path video detector. The residual path applies fixed spatial and temporal difference-of-Gaussians operators to frozen intermediate features and models the resulting differences alongside appearance context across frames. The semantic path adapts the encoder's normalization parameters for frame classification, and a clip-dependent gate combines their predictions. Under a shared protocol across seven datasets, MARS achieves the highest average AUROC of 91.43\%, outperforming seven compared detectors. When trained on facial manipulations alone, MARS achieves 93.99\% AUROC on GenVideo and 75.50\% on DF26, demonstrating transfer to generated videos without generated-video training data. MARS also provides signed patch and frame contributions, whose faithfulness we evaluate through controlled spatial and temporal removal against random controls. MARS is publicly available for research: Project page: this https URL Github: this https URL

---


### 464. [UniHam: A Large-Scale SOC-Complete Dataset and Benchmark for Hamiltonian Learning in Materials](https://arxiv.org/abs/2611.12509)

**<font color=#1a73e8>作者：</font>** Yuewen Huang, Pin Chen, Yutong Lu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of electronic Hamiltonians would enable broad property inference while avoiding the high computational cost of Density Functional Theory (DFT). However, progress toward general-purpose materials foundation models is limited by a data bottleneck: existing Hamiltonian datasets are typically small, lack structural diversity, and often omit essential relativistic physics such as spin--orbit coupling (SOC). We therefore construct UniHam, a large-scale Hamiltonian dataset and benchmark suite comprising 100,000+ DFT-computed complex-valued Hermitian Hamiltonians with full SOC, covering 72 elements and a wide range of crystal geometries and symmetries (spanning diverse lattice types and space-group families). Building on UniHam, we benchmark two representative state-of-the-art models under a standardized protocol and introduce complementary evaluation metrics that jointly assess three dimensions: (i) Hamiltonian reconstruction accuracy, (ii) out-of-distribution (OOD) generalization across composition/symmetry shifts, and (iii) the ability to support downstream property prediction from the predicted Hamiltonians. Experiments on UniHam demonstrate that the proposed benchmark and metrics effectively differentiate model capabilities, revealing intrinsic SOC- and element-dependent failure modes, large variations in compositional OOD robustness, and the necessity of spectral-level evaluation to assess whether Hamiltonian predictions reliably support downstream electronic-structure properties. Overall, UniHam provides a reproducible, SOC-complete benchmark that can sharpen model comparisons and accelerate the development of next-generation foundation models for quantum materials.

---


### 465. [Perceived Agency During Agent-Avatar Control Transitions in Virtual Reality](https://arxiv.org/abs/2611.12529)

**<font color=#1a73e8>作者：</font>** Jingyi Zhang, Anthony Steed  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Prior beliefs about whether a virtual human (VH) is controlled by a human or a computer can shape how users interpret and respond to its behaviour. As emerging hybrid VH systems allow control to transfer between human operators and computer programs during an ongoing interaction, it remains unclear whether perceived agency updates with the actual controller or continues to reflect users' prior beliefs and first impressions. We investigated this question in a within-subject VR study with 24 participants across four conditions: always computer-controlled, computer-to-human, human-to-computer, and always human-controlled. We designed an interaction task in which participants acted as interviewers, asking the VHs a fixed set of questions. Before each interaction, participants were informed whether the VH was human- or computer-controlled, matching the actual controller at the beginning, but were unaware of possible control transitions.
We found that perceived agency was strongly influenced by the controller presented at the beginning of the interaction, with no evidence of updating following the control transitions. Social evaluations including likeability and co-presence were generally higher in conditions where human control occurred later and covered a greater proportion of the interaction. The results suggest that prior beliefs and first impressions continued to shape perceived agency, whereas social evaluations were more sensitive to the VH's actual behaviour over the interaction.

---


### 466. [K-prop: Deep Online Learning by Backpropagating Temporal Kernels](https://arxiv.org/abs/2611.12530)

**<font color=#1a73e8>作者：</font>** Bingkun Liu, Paul Haider, Federico Benitez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-recurrence represents an important component for temporal processing in neural networks, both artificial and biological, where it appears naturally in the form of leaky integration. However, due to the complex temporal dependencies of the gradient, an efficient and effective method of online training is still lacking. Here we propose K-prop, a novel online learning method for leaky neural networks. It dramatically reduces the computational and memory cost of real time recurrent learning (RTRL) by propagating kernel gains. K-prop also outperforms existing RTRL approximations and achieves performance comparable to backpropagation through time in sequence learning, classification, and reinforcement learning tasks. We further analyze how its sole approximation affects gradient quality and identify conditions under which K-prop remains accurate and effective.

---


### 467. [ML Models Are Not Ciphers: Power Analysis for Weight Extraction Is Harder Than You Think](https://arxiv.org/abs/2611.12532)

**<font color=#1a73e8>作者：</font>** Mohammed Qaiss, Peter Horvath, Michal Shagam 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Can power-analysis techniques reveal secret weights of machine-learning models? Multiple recent works demonstrate proof-of-concept attacks that can partially recover such weights. To that end, these works build on techniques from cryptographic engineering, treating the model as a ``cipher'' and its secret weights as keys.
We question the basic assumption behind such straightforward adaptations of cryptographic attacks and highlight the challenges arising when applying past techniques to fully recover all layers of deep neural networks. Unlike past works, which extract only a few weights, typically from shallow layers, we investigate the recovery of complete networks. Moreover, we target fully trained and functional models, rather than untrained, randomly initialized networks. To focus on fundamental challenges, we assume an unrealistically strong side-channel adversary that can directly observe the output of the leakage model without any added noise. With this adversary, we show that machine-learning models differ significantly from cryptographic implementations, giving rise to unique challenges that have not been observed in the prior art.
We observe two main differences between machine-learning models and ciphers. First, in contrast to the high-diffusion nonlinear integer arithmetic prevalent in cryptographic schemes, machine-learning models tend to use limited-precision floating-point arithmetic and low-diffusion linear operations. We show that these operations introduce difficulties in weight recovery, often requiring an unexpectedly large number of traces, even under ideal channel conditions. Second, we observe that, unlike ciphers, which aim to increase the data entropy, machine-learning models aim to reduce it. This reduces data variability as the algorithm progresses, hampering weight recovery in deep layers of the model.
(details can be found in the paper)

---


### 468. [WanderBench: Can World Models Explore Dynamic Worlds from Video?](https://arxiv.org/abs/2611.12557)

**<font color=#1a73e8>作者：</font>** Yuhang Chen, Jiheng Li, Jiale Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models conditioned on an input video make it possible to explore real, recorded dynamic scenes, enabling re-shooting of footage, free-viewpoint replay, and real-to-sim environments for embodied agents. Such uses require the generated rollout to stay faithful to the recorded world, yet existing benchmarks start from a single image or a text prompt, and video-conditioned generation is evaluated mainly on perceptual quality and camera following. These evaluations do not directly assess whether exploration preserves subject identity, event progression, and scene consistency upon revisiting a location. We introduce WanderBench, a benchmark for exploring dynamic worlds from video. It comprises 745 single-shot source videos of real and AI-generated content in three difficulty tiers (3-25 s), paired with camera routes given as keyboard actions, and evaluates six dimensions with 24 human-validated sub-metrics. Benchmarking eight models, we find that as clips grow longer, models keep the static scene and visual quality but lose camera control and the source dynamics, and that none keeps revisited places consistent. We further propose WanderLand, a training-free framework that conditions each frame of a frozen model on the same-instant source and, on revisits, on its own earlier static content. WanderLand improves five models on every dimension, by up to 8.3 points in source-dynamics fidelity.

---


### 469. [LawKAN: Group-Law Layers for Composition -- When Imposing a Known Law Pays Off](https://arxiv.org/abs/2611.12567)

**<font color=#1a73e8>作者：</font>** Anna Mishchenko, Nikolai Gavrilin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many tasks compose transformations by a known rule: chained rotations in robotics and navigation. Learned models relearn it, compounding error; classical estimators hardcode it and miss hardware deviations. We impose the known structure and learn only the remainder: an exact non-commutative group law sits in the node of a self-contained layer, its edges learn local increments, and a zero-initialized correction psi learns unknown deviations of the law. A pre-training criterion predicts exact representability. On fixed-angle SU(2) composition, a 54-parameter dense edge is the most accurate dense model, at 27x fewer parameters than the strongest fixed-matrix baseline, and lies 0.05 deg above the Bayes floor. On real robot arms, an isolated 306-parameter psi reaches 1.12-1.14 mm versus 1.29-1.33 mm for Gauss-Newton at N >= 60, and the recipe transfers across three vendors and two protocols. The recipe matches classical fits where the data obey the law and loses where the imposed law is not the task's.

---


### 470. [From Likelihood Convergence to Parameter Convergence in POMDPs](https://arxiv.org/abs/2611.12575)

**<font color=#1a73e8>作者：</font>** Jack Zhang, Saurabh Amin, Jiawei Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Likelihood-based methods are widely used to learn the parameters of partially observable Markov decision processes (POMDPs). While finite-sample guarantees for policy suboptimality exist for certain POMDP subclasses, analogous guarantees for parameter recovery remain less well understood. For any candidate POMDP parameter, we bound its parameter recovery error in terms of its likelihood gap to the ground truth, the structural conditioning of the observation and transition kernels, and the behavior policy used to collect data. The bound applies in both the undercomplete and overcomplete regimes, with the latter following naturally from the undercomplete analysis. Because the result applies to any sufficiently good candidate, it yields finite-sample guarantees for the maximum-likelihood estimator and any procedure producing a parameter with controlled likelihood gap. This is particularly useful for near-optimal learning in infinite-horizon POMDPs, where existing approaches largely rely on model-based planning with accurate transition and observation kernel estimates. The bound separates the contributions of the behavior policy and model, showing how data-collection choices, including action coverage, and their effects on mixing can accelerate parameter learning.

---


### 471. [TRACE: Adaptive Trust-Region Bayesian Optimization for Open-Ended Molecular Design](https://arxiv.org/abs/2611.12591)

**<font color=#1a73e8>作者：</font>** Madhav R. Muthyala, Mahsa Askari, Farshud Sorourifar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimizing molecules under small evaluation budgets requires deciding both where in chemical space to search and which candidate within that region to evaluate. We introduce Trust Region Adaptive Chemical Exploration (TRACE), a framework for open-ended molecular Bayesian optimization (BO), where candidates are generated on demand rather than selected from a fixed library. TRACE combines an objective-free graph-perturbation mechanism with a fixed, chemistry-aware Gaussian process (GP) surrogate using fragprints, a representation combining molecular fingerprints and fragment descriptors. Rather than learning the search geometry itself, TRACE makes the scale of chemical exploration explicit through a Tanimoto-similarity threshold controlling chemical extent and a cardinality budget controlling candidate-search breadth. A simple success/failure controller expands or contracts both quantities during optimization, while the GP and acquisition function select which admissible molecules to evaluate. Across six challenging molecular optimization benchmarks under matched 1,000-evaluation budgets, TRACE achieves the strongest overall sample efficiency as measured by the best molecule found as evaluations accumulate. Crossed ablations on two objectives further show that adaptive region control contributes beyond the proposal mechanism, while its benefit depends on the proposal distribution. We further apply TRACE to the stability of iron phthalocyanine (FePc), a non-precious molecular electrocatalyst whose degradation can involve loss of the Fe center. Using a first-principles density functional theory (DFT) workflow designed for accurate energy evaluation, TRACE increases the computed thermodynamic resistance to Fe dissolution from 0.42 to 2.59 eV over 80 designed evaluations.

---


### 472. [Unmasking Four Knapsack Problems in the Traveling Thief Benchmark](https://arxiv.org/abs/2611.12597)

**<font color=#1a73e8>作者：</font>** Mohammed Mizan Alanazi, Mahdi Khemakhem  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The traveling thief problem (TTP) asks a thief to choose a tour and a packing together, and the benchmark of 9,720 instances of Polyakovskiy et al. (2014) is the standard test set for comparing TTP heuristics. We show that four of these instances are not TTP instances at all. Their files give a renting rate of 0.00, so the tour has no effect on the objective and each instance reduces to a 0-1 knapsack problem. One of them belongs to the 60 categorized instances on which new methods are usually compared, and on it five of nine published methods report exactly the same value. The cause is the format of the files, which keep the renting rate with two decimals, while the rule of the generator gives a rate close to 0.003 on these instances. The same rounding may shift the rate of 949 other instances by more than 1%. Since the tour and the packing used by the generator were not published, the original rates cannot be recovered. We therefore define new rates with the same rule, applied to a fully specified reference solution that we publish, and we show with a published heuristic that the corrected instances behave as TTP instances again. We also give reference results on the corrected instances and recommendations for future studies. Finally, we present ttplib, a new open-source Python library that loads any of the 9,720 instances, including the corrected ones, without downloading the whole benchmark.

---


### 473. [Reconfiguring System-Level Protection Through Bounded Delegation in RISC-V MCUs](https://arxiv.org/abs/2611.12622)

**<font color=#1a73e8>作者：</font>** Luís Cunha, José Martins, Manuel Rodríguez 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> MCU-based embedded and cyber-physical systems increasingly require protection policies to change at runtime as resources, software, and system composition evolve. Yet widely used COTS MCU protection mechanisms are still largely designed around statically established policies. While they can restrict which domains modify protection primitives, they generally do not constrain what policy an authorized domain may create. As a result, domains may expand protection rules beyond their intended scope or interfere with boundaries established by other domains. We identify bounded configuration authority as a missing primitive for secure dynamic policy evolution and introduce an ownership-aware model in which explicit ownership and rule containment bound both configuration authority and recursive delegation. Changes to active protection-rule ranges are validated before commit, preserving protection boundaries without extending the normal access-checking datapath. We implement the model in an open-source RISC-V World Checker integrated into a CVA6-based SoC. Our FPGA evaluation shows no degradation in access latency or operating frequency, with 7.1% LUT and 1.2% FF overhead for eight rules. In an OTA update case study, direct reconfiguration under delegated authority reduces policy-transition latency by 89.5% over hypervisor mediation and 94.6% over trusted firmware mediation, while preserving established authority boundaries. All artifacts will be open-sourced to support the evolution of RISC-V specifications and system-level protection designs.

---


### 474. [Towards Reconstructing and Recognizing Objects behind Fragmented Occlusion using Video](https://arxiv.org/abs/2611.12624)

**<font color=#1a73e8>作者：</font>** Roman Pflugfelder, Michael Lindenbaum, Daniel Cremers  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Perceiving objects through fragmented occlusions, such as foliage, is a natural capability of the human visual system but remains a fundamental challenge for computer vision. This work addresses the problem of object reconstruction, or de-occlusion, in the presence of high-density, fragmented occlusions. We propose a reconstruction framework that operates on a sequence of grayscale images of a moving object, acquired by a single camera, either stationary or in motion. The algorithm estimates the object's relative positions across frames by jointly registering the images and optimizing the alignment parameters to maximize the contrast of their average, referred to as the integrated image. This integrated image serves as the reconstructed representation of the object. Experimental evaluations on both synthetic and real video sequences demonstrate the feasibility of accurate reconstruction under occlusion densities exceeding 90%. The proposed approach is competitive with synthetic aperture techniques, which are limited to static objects and require complex camera setup with careful calibration. Furthermore, we show that the integrated image enables reliable object classification under severe occlusion when used as input to standard, off-the-shelf classifiers.

---


### 475. [BioBind: Binding Biometric Deduplication to Zero-Knowledge Authentication](https://arxiv.org/abs/2611.12636)

**<font color=#1a73e8>作者：</font>** Taotao Wang, Xiaoxiao Wu, Shengli Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Biometric identity systems for decentralized applications need credentials that resist repeated enrollment and support private, publicly verifiable authentication. Capture and large-scale private deduplication run off chain while smart contracts authorize issuance and use; these stages span distinct trust domains, and a correct verdict covers only the checked inputs and gallery snapshot. Without binding and state checks, concurrent enrollments can issue duplicate credentials from correct verdicts, while substituted inputs can authorize unrelated credentials. We present BioBind, a protocol whose four backend interface conditions bind the deduplication query, gallery insertion and issued commitment to one captured vector, authenticate gallery transitions, and require a sound uniqueness verdict valid at finalization. Its encrypted instance uses bound requests, stale-session rejection and committee-confirmed migration. Capture-bound zero-knowledge authentication links credential use to the enrolled template and a fresh device-originated probe bound to the challenge. We give a conditional multi-session composition argument under explicit capture, backend and cryptographic assumptions. A prototype using LFW face features rejects the tested composition attacks; its unlinkable authentication circuit uses 31,445 constraints and about 305,000 gas. An equal-public-field baseline quantifies the cost of verifiable matching: witness-plus-proving medians are 1.989 s versus 1.119 s with device-trusted matching. Separate tests of encrypted enrollment complete three histories of 16,384 registrations without decoding errors at the tested checkpoints. Biometric accuracy bounds person-level uniqueness: on the Bosphorus database, cooperative subjects who change appearance evade deduplication in 1.8% of re-enrollment attempts at the operating threshold. Full backend integration remains open.

---


### 476. [Simulation-aided Reinforcement Learning with Control Variates](https://arxiv.org/abs/2611.12643)

**<font color=#1a73e8>作者：</font>** Omer Hemo, Ido Sefi, Mirco Mutti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) algorithms often rely on data collected from a target environment, which can be expensive and noisy. Although simulators can generate large amounts of additional data, standard simulation mixing approaches, which directly combine simulated and real experience, can degrade performance due to simulator inaccuracies, especially when they bias the solution away from the optimal policy. We propose a conservative simulation-aided learning method based on control variates, where simulated data is used solely to reduce variance in the learning process rather than directly shaping the learning target. We develop our approach for Policy-Evaluation, which is a fundamental building block of RL algorithms. Then we combine it within the actor-critic framework towards policy improvement, as well as extend it towards offline RL scenarios. Experiments on multiple MuJoCo benchmark tasks demonstrate improvements over standard simulation mixing approaches, highlighting control variates as an effective tool for simulation-aided reinforcement learning.

---


### 477. [Maurer-Inspired Two-Way Physical-Layer Authentication Against Multi-Antenna Impersonation Attacks](https://arxiv.org/abs/2611.12648)

**<font color=#1a73e8>作者：</font>** Pin-Hsun Lin, Linda Senigagliesi, Eduard A. Jorswieck  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In this work, we investigate Maurer-inspired two-way physical-layer authentication. Alice seeks authentication by Bob in the presence of a multi-antenna impersonator, Trudy. Trudy may replace the challenge to Alice, the response to Bob, or both. To create an information advantage, Bob adds artificial noise (AN) to his challenge, and Alice adds spatial AN while forwarding the received mixture. Bob predicts the response from trusted preparation, whereas Trudy observes only a noisy version of the challenge, and Alice's AN interferes with Trudy's preparation reception. Impersonation thus requires matching Bob's fresh randomness beyond the channel consistency checked by public-pilot one-way authentication. For quasi-static Gaussian multiple-input multiple-output channels with time-division duplex (TDD) reciprocity, we derive missed-detection bounds for attacks that replace the authentication challenge, the response, or both. These bounds assume attack-free initial training and preparation and account for estimation error and AN leakage. With equal antenna numbers at all nodes, we show scenarios where the proposed scheme has lower worst-case missed detection than specified one-way tests with/without AN.

---


### 478. [When Does Sliced Inference Pay Off? Resolution, Tiling and Dense Fusion for Small Object Detection](https://arxiv.org/abs/2611.12657)

**<font color=#1a73e8>作者：</font>** Stefan Becker, Jens Bayer, David Münch 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sliced inference such as SAHI is the standard remedy for small objects in high-resolution imagery, but its gains are usually measured against low-resolution baselines. We revisit sliced inference with scale as the explicit variable and ask when tiling actually pays off. We compare seven dense detectors from four families on VisDrone and DOTA, under pre-specified hypotheses, calibration-only tuning and a single evaluation on held-out test data. Two findings emerge. First, much of the benefit attributed to slicing is a resolution effect: on VisDrone, a single pass trained at a higher resolution outperforms tiling with box fusion (merging decoded boxes) for every detector that could be trained at that resolution, and at equal compute a higher resolution helps more than a larger model. Second, tiles carry complementary information that box fusion wastes. We introduce SCAHI (Slicing with Coverage-Aware Hyper Inference), which accumulates the dense outputs of all passes with weights that give every image position the same total coverage, and reads objects off a peak grid fine enough to keep crowded neighbours apart. On identical passes, SCAHI outperforms box fusion for every YOLO detector on both datasets and matches it for FCOS. On DOTA, whose images far exceed the resolution a single pass can be trained at, tiles with SCAHI beat the best single pass for every detector, by 4.3 to 5.6 mAP50 at 2048 px, and replacing only SAHI's merge step by SCAHI adds 2.3 to 4.0 mAP50. An ablation attributes the gain to the border weighting and the resolution of the peak grid. Source code is available at this https URL.

---


### 479. [Certify, Report, or Refuse: Harm-Constrained Conformal Prediction for Clinical Actions](https://arxiv.org/abs/2611.12662)

**<font color=#1a73e8>作者：</font>** Zhiyuan Li, Lequan Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Routing a melanoma case to routine follow-up is a serious action error that diagnostic coverage alone does not rule out. We present Harm-Constrained Risk-Optimal Conformal Prediction (HC-ROCP), a training-free framework that uses frozen classifier probabilities and adds a harm penalty when choosing prediction sets and actions. We test the resulting policies on disjoint calibration splits with multiplicity adjustment. HC-ROCP certifies supported claims, reports descriptive fallback policies, and refuses unsupported subgroup claims. We evaluate these outputs retrospectively on COVID-19 radiographs, ISIC 2019 dermoscopy, and EyePACS-to-APTOS retinopathy transfer. Across ten calibration seeds, HC-ROCP reduces COVID-19 severe-action errors from the exact risk-optimal baseline's 4.68\% to 0.54\%. At a 5\% budget, global claims are certified for COVID-19 and ISIC, but the rare squamous-cell-carcinoma claim is refused. At 1\%, all settings receive descriptive reports. For each budget, we also report the minimum severe-case count needed to pass the global harm gate with zero errors, providing a starting point for further data collection.

---


### 480. [Trade Promotion Optimisation for Consumer Goods](https://arxiv.org/abs/2611.12665)

**<font color=#1a73e8>作者：</font>** Ankur Verma, Namrata Gupta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Trade promotions consume a large share of consumer-goods revenue, yet most planners still set discounts with a single, often unreliable, price elasticity per item. We present an end-to-end Trade Promotion Optimisation (TPO) system built as one chain: analogue SKUs, point elasticity, elasticity curve, price recommendation, promotional lift and net lift. Elasticity is measured at post-promo time from directional price-dip events against a rolling regular price, and at promo time by a causal estimator that residualises trend, seasonality and promotion, handles stock-out censoring with a Tobit likelihood and updates itself from the first clean promotion week. Items with weak evidence borrow the point elasticity and the curvature from analogue SKUs chosen by a cross-validated ridge model over category, brand, sub-category, price line and description. The optimiser separates self-price lift from substitution and post-promo dips and adjusts for inventory and trade funding. In a four-week promotion experiment on a 39-SKU consumer brand (mean elasticity -3.06), the plan lifts units by 20.6% and revenue by 6.9% at flat margin. Analogue pooling halves elasticity error relative to hierarchy averaging.

---


### 481. [Controlled Binary Assignment Flows](https://arxiv.org/abs/2611.12668)

**<font color=#1a73e8>作者：</font>** Paul Fröhling, Christoph Schnörr  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper introduces a geometric approach to the representation and learning of time-variant parametrizations of deep assignment flows, for binary data labelings on graphs. Each edge carries an optimally controlled parameter flow in a 2-dimensional totally geodesic submanifold, based on objectives derived from a non-local linear scale space representation of the input data. The aggregation of triplets of such flows in 5-dimensional totally geodesic submanifolds is learned from data. The fusion of these flows determines the trajectory in the high-dimensional symmetric parameter space and by geometric integration the layers of binary deep assignment flows. Numerical results demonstrate the expressivity and the limitation of our highly parallel geometric local synthesis approach to high-dimensional deep assignment flow parametrizations.

---


### 482. [What Breaks Scribble-Supervised Segmentation? An Audit-Informed Benchmark for Scribble Annotation Robustness](https://arxiv.org/abs/2611.12674)

**<font color=#1a73e8>作者：</font>** Minheng Wu, Di Wen, Ruiping Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scribble-supervised segmentation is typically evaluated with a fixed annotation set, leaving robustness to distinct semantic and geometric imperfections poorly understood. Motivated by an audit of 12,031 manual PASCAL Visual Object Classes (VOC) 2012 scribbles and prior work, we introduce six controlled perturbation operators. Class corruption, spatial offset, and directional perturbation directly operationalize audit signals. Stroke-length reduction is motivated by prior scribble studies, while random dropout and fragmentation serve as diagnostic controls. Each operator reports requested and achieved changes. We evaluate manual and automatic scribbles across two image domains, two principal backbone settings, and multiple training pipelines, with an additional MiT-B1 PFA anchor evaluation. In the five-seed Tree Energy Loss (TEL)-ResNet101 VOC study, mean intersection over union (mIoU) drops from 70.08 to 1.46 under class corruption, compared with 35.57 for spatial offset, 52.20 for directional perturbation, and 63.24 for stroke-length reduction at their strongest settings. At the evaluated endpoints, semantic-anchor corruption produces the largest degradation, while geometric and support responses depend on the pipeline and dataset. Our benchmark provides a reproducible protocol for diagnosing annotation robustness beyond clean-set accuracy. The operator code is available at this https URL.

---


### 483. [Interpretability Is Not Model-Specific](https://arxiv.org/abs/2611.12675)

**<font color=#1a73e8>作者：</font>** Marcus Armstrong, Navid Ayoobi, Pradham Mummaleti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interpretability tools are usually built for one model at a time: a refusal direction, a truthfulness probe, or a steering vector is found with labeled data inside the model it explains. We ask whether such tools can be carried to other models through a map between residual streams fit only on unlabeled prompts. We transfer a refusal direction, tested causally by addition and ablation, and two read-out tools, a correctness direction and a sentiment probe, across 110 pairs of models from five families and 1B to 72B parameters and between base and instruction-tuned models, with controls for specificity and five seeds. How much transfers depends on what the map was fit on. A map fit on ordinary questions recovers 54\% of the target's own refusal steering and 16\% to 77\% of its correctness gain; adding unlabeled prompts from the region where the tool operates raises these to 102\% and 88\% to 98\%, while control directions recover at most 1\%. We prove that a linear map behaves this way whenever two models correspond linearly on the data it covers, and a label-free coverage score derived from this result tracks recovery across more than 16,000 runs and explains earlier reports that maps between models fail across domains. Carried read-out tools outperform anything the target's unlabeled representations yield. Interpretability results, once found, can be reused across models at the cost of a few unlabeled prompts.

---


### 484. [National-Scale Crop Type Mapping in Morocco Using Google AlphaEarth Foundations Embeddings and the Fields of the World Field Boundary Map](https://arxiv.org/abs/2611.12681)

**<font color=#1a73e8>作者：</font>** Walid Elbarz, Mohamed Bourriz, Vincent Simonneaux 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent geospatial foundation models have introduced a new paradigm for large-scale Earth observation by providing pretrained embedding representations that can be directly exploited for downstream tasks. In this work, we investigate the use of Google AlphaEarth Foundations embeddings for national-scale crop type mapping in Morocco. The proposed workflow operates directly on publicly available 64-dimensional pretrained embeddings using lightweight downstream classifiers, eliminating the need to process raw satellite imagery during model training and inference. The approach targets three crop categories, namely winter cereals, tree crops, and other crops. For nationwide inference, the Fields of the World global field boundary map is used to constrain predictions to agricultural parcels, enabling efficient large-scale mapping. Experimental evaluation on an independent test set over ten repeated runs achieved an average classification accuracy of (87.17 +/- 0.42%). Nationwide inference over Morocco was completed in approximately five hours, with the dominant computational cost arising from cloud-based retrieval of the embeddings rather than model execution. These results demonstrate the potential of pretrained embedding representations for computationally efficient national-scale crop type mapping.

---


### 485. [Differentiable Inverse Rendering Recovers Intrinsic Properties from Intravascular Optical Coherence Tomography](https://arxiv.org/abs/2611.12686)

**<font color=#1a73e8>作者：</font>** Ajay Manicka, Karim Kadry, Sebastian Ruiz-Lopera 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical images encode intrinsic tissue properties that indicate disease progression, yet these properties remain entangled with the system-dependent physics of image formation. Differentiable inverse rendering asks whether they are recoverable by inverting the imaging system's forward physics rather than through post-hoc correction. We address this in optical coherence tomography (OCT), focusing on the optical attenuation coefficient, a per-pixel marker of pathology and cellular composition. Conventional recovery relies on closed-form inversions limited to simplified light-tissue models, or learned methods coupled to specific imaging configurations. We instead recover per-pixel attenuation from a single OCT image by gradient descent through a differentiable physics-based forward model. We verified the method against analytical solutions, validated it on five in vitro phantoms, and applied it without modification to 29{,}269 clinical intravascular OCT images from 128 patients. The inversion needs no training data or segmentations and is portable across platforms and retrospective archives. Replacing the forward model or recovering another optical parameter leaves the optimization procedure unchanged. We demonstrate per-pixel recovery is tractable because gradient information scales to this high-dimensional problem, where gradient-free methods become intractable. Our work supports quantitative tissue characterization from OCT images and provides a framework for extension across imaging modalities and organ systems.

---


### 486. [CoilStellaration: A Dataset and Benchmark for Engineering-Aware Stellarator Coilset Generation](https://arxiv.org/abs/2611.12689)

**<font color=#1a73e8>作者：</font>** Jan-Hendrik Ewers, Santiago A. Cadena, Nicolò Foppiani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stellarators are fusion devices that use externally generated, three-dimensional magnetic fields to confine hot plasma and offer a promising route to commercial fusion. Their electromagnetic coils pose a challenging design problem: they must reproduce the target magnetic field while satisfying engineering constraints and remaining practical and cost-effective to manufacture. Finding suitable geometries is a highly nonlinear inverse problem that generally has neither a closed-form nor a unique solution. This problem lies at the heart of stellarator design. We introduce CoilStellaration, a dataset and benchmark for learning the mapping between coil geometries from target plasma magnetic fields and engineering requirements. The dataset contains 177,000 optimized filamentary coilsets targeting plasma equilibria from ConStellaration, with sampled engineering requirements and achieved geometric and magnetic-field metrics. It spans multiple coil counts and field-period numbers, supporting studies of both specialized and shared models across configurations. The benchmark asks models to predict coils conditioned on a target equilibrium and requirements on coil-coil and coil-plasma spacing, curvature, and magnetic-field error. We show that magnetic-field accuracy remains the main challenge, with learned models rarely satisfying all requirements simultaneously. However, using learned predictions to initialize conventional coil optimization can accelerate early progress. We release baseline models and evaluation code to support reproducible research on both direct coil generation and learned optimization initializations. By lowering the barrier for machine learning and optimization researchers to engage with stellarator coil design, we aim to accelerate progress toward practical, cost-effective stellarator power plants.

---


### 487. [Agnostic Marginal-Nonuniform Learning](https://arxiv.org/abs/2611.12694)

**<font color=#1a73e8>作者：</font>** Tanmay Devale, Steve Hanneke, Amirreza Shaeiri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of binary classification in the marginal-nonuniform learning framework in the agnostic setting. In this model, the constants in the learning rate may depend on the marginal distribution of the unlabeled data, but the guarantee must hold uniformly over all conditional distributions of the labels. We also study fine-grained rates.
We consider two criteria.
(1) The standard agnostic setting, where the learner competes with the best concept in the class. In this setting, an immediate consequence of standard agnostic PAC learning results gives us the optimal rate of $\tfrac{1}{\sqrt{n}}$ for every class $\mathcal{H}$ with finite $\mathrm{VC}(\mathcal{H})$ and shows that arbitrarily slow rates are necessary otherwise. This also gives us the optimal fine-grained rate of $\sqrt{\tfrac{\mathrm{VC}(\mathcal{H})}{n}}$. Therefore, the dependence on the marginal distribution does not help, which is in contrast to the realizable setting.
(2) In the relaxed agnostic setting, where the learner competes with $(1+\lambda)$ times the error of the best concept for a fixed $\lambda \in (0,1]$, the picture from the realizable setting reappears. We obtain a trichotomy of the achievable optimal rates: exponential rates of the form $e^{-n}$ arise precisely when the class is finite; linear rates of the form $\tfrac{1}{n}$ arise when the class is infinite but $\mathrm{VC}(\mathcal{H})$ is finite; and arbitrarily slow rates occur when $\mathrm{VC}(\mathcal{H})=\infty$. We also obtain the optimal fine-grained rate of $\tfrac{\mathrm{uVCE}(\mathcal{H})}{\lambda n}$, where $\mathrm{uVCE}(\mathcal{H})$ is a recently introduced combinatorial complexity dimension called the uncentered $\mathrm{VC}$-eluder dimension.

---


### 488. [TACTUS: A Robotic Palpation System for Spatially Heterogeneous Hardness Mapping of Woody Breast Myopathy](https://arxiv.org/abs/2611.12695)

**<font color=#1a73e8>作者：</font>** Chaitanya Pallerla, Yihong Feng, Avisekh Tripathy 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Woody breast (WB) myopathy is a spatially heterogeneous fibro-degenerative condition of the broiler Pectoralis major muscle. Existing mechanical reference methods rely on single-point or sequential compression measurements, limiting characterization of spatial hardness variability. This study presents TACTUS (Tactile Adaptive Conformal 3D Uniform Sensing), an automated tactile array that generates thickness-normalized, three-dimensional hardness maps at 20 anatomically distributed locations within approximately 30 s. TACTUS integrates 20 independently motorized tactuators with force-sensing resistors and encoder-driven linear actuators, alongside a LiDAR depth camera for surface profiling and adaptive compression. The system was evaluated using 100 broiler breast fillets across four WB severity classes (Normal, Mild, Moderate, Severe). TACTUS identified significant force differences among severity classes (ANOVA, p < 0.001), with the strongest differentiation in the cranial region and a significant caudal effect not detected by texture-analyzer measurements. Fillet-level TACTUS force showed moderate but significant correlation with texture-analyzer measurements (Pearson r = 0.441, p < 0.001). Semivariogram, local change entropy, and heterogeneity analyses revealed increasing and anatomically structured hardness variability with WB severity. These findings demonstrate TACTUS as an automated, operator-independent platform for spatially resolved mechanical characterization and ground-truth generation to support hyperspectral and near-infrared spectroscopy-based WB classification systems.

---


### 489. [Generalized Adaptive Boosting and the Geometry of Mistakes](https://arxiv.org/abs/2611.12696)

**<font color=#1a73e8>作者：</font>** Marco Bressan, Nataly Brukhim, Nicolò Cesa-Bianchi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Not all mistakes are alike. For example, in medical diagnosis, false positive and false negative mistakes have a different impact and should not be aggregated. By revisiting the classical theory of boosting through this lens, we introduce the notion of $Z$-learner, which returns weak hypotheses achieving joint false-positive/false-negative guarantees $(\mathrm{FP},\mathrm{FN})$ from some set $Z \subseteq [0,1]^2$. This formulation generalizes the standard notion of $\gamma$-weak learning--recovered by taking $Z=\{(z_1,z_2): z_1+z_2<1/2-\gamma\}$--and allows for more flexible notions of weak learnability that account for the impact of the distribution on the achievable learning guarantees. This raises a natural question: which sets $Z$ are boostable? We answer this by giving a complete geometric characterization that unifies, as special cases, both the classical boosting dichotomy and the recent multi-objective extension of Bressan et al. (COLT 2025). We also present an adaptive algorithm for boosting $Z$-learners without relying on the prior knowledge of $Z$, generalizing AdaBoost's ability to handle unknown margin parameters. Finally, we demonstrate that $Z$-learners can achieve confidence amplification. However, the analysis is significantly more involved than in classical boosting and relies on the centerpoint theorem from discrete and computational geometry.

---


### 490. [Fisher-Glass Learning: Classification Bounds and Subpopulation Audits](https://arxiv.org/abs/2611.12702)

**<font color=#1a73e8>作者：</font>** El Mustapha Mansouri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate classifiers can fail when background cues change without altering the correct labels. Predictive performance alone does not quantify how much task information remains after accounting for such nuisance variation. Here we extend the Fisher-glass framework to connect nuisance-adjusted information with local classification difficulty and subpopulation auditing. We derive lower bounds on local minimax excess classification risk under explicit distinguishability and decision-separation conditions, alongside statistical audits accounting for estimation error and regularization. On Waterbirds, a feature-based diagnostic of task-background alignment selects an accurately classified group, with selection frozen before held-out evaluation. Across five training seeds, background replacements preserving the extracted bird foreground and labels yield 93.2% accuracy when background type is preserved and 40.6% when it changes, a controlled difference of 52.6 percentage points. Separately, search using task labels and a fixed nuisance direction identifies an independently evaluated population with 98.8% membership-weighted accuracy and low estimated projected predictive Fisher information. Training and acquisition experiments show that information gains and predictive gains can diverge. These findings support joint assessment of predictive performance, information under declared nuisance models and controlled sensitivity when diagnosing vulnerability and evaluating model improvements.

---


### 491. [Checking DER Commands Against Grid Context Catches Credentialed Attacks Static Checks Miss](https://arxiv.org/abs/2611.12703)

**<font color=#1a73e8>作者：</font>** Benjamin Blakely  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Authorization of distributed energy resource (DER) commands judges a command by who sent it and whether its value has been seen before. An attacker holding a legitimate credential who writes ordinary values passes both tests. We add a check that judges each DER write against the grid's operating context: the bus voltages around the target, the hour, the day- ahead price, system load, and irradiance, compared with what operators wrote under similar conditions in the feeder's own benign history. We evaluate it live on the IEEE 123-bus and 8500-node feeders, driven by a measured 2024 year of price, load, and irradiance, against nine attack scenarios. A lookup trained on the same history catches none of the writes of the four scenarios that send values already familiar on the targeted device; the context check refuses 91.7% of insider-abuse writes and 64.4% of DER-aggregation writes while denying 1.28% of benign writes. In an offline test that replays recorded moments with curtailment setpoints drawn from the benign range, issued at a positive price, it refuses 47.3% and 50.5% on the two feeders, against 18.5% and 16.0% for the same check without context; live, the few setpoints tested were mostly shallow and were mostly allowed. The context check complements the lookup.

---


### 492. [Multi-Agent Screening: What Agreement and Acceptance Cannot Tell You](https://arxiv.org/abs/2611.12705)

**<font color=#1a73e8>作者：</font>** Benjamin Chang, Dell Zhang  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> When AI agents screen items for a costly human assessor, as in agentic search, e-discovery and AI reviewing of papers, only what they pass gets judged. We show what each kind of evidence can establish about their errors, even with unlimited data. Agreement shows that agents concur, not that they are right, however many there are. Acceptance by the assessor gives precision but only a lower bound on recall. Knowing which agents found which relevant items gives an upper bound on recall if agents' finds are not negatively correlated, and caps what one more agent can add if agents are interchangeable. Without assumptions about the agents, recall can be pinned down only by judging items they did not pass: a random sample of these estimates how many relevant items were missed, to any chosen accuracy, and the sample needed does not grow with the number of agents.

---


### 493. [Spaghetti Splatting: Differentiating Curvilinear Dirac Masses via Convolution](https://arxiv.org/abs/2611.12716)

**<font color=#1a73e8>作者：</font>** George Shramko, Shrisudhan Govindarajan, Rudy Lam 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In production systems, 3D geometry is represented by primitives such as points, lines, and triangles, as rendering hardware is optimized to generate images from them very efficiently. Learning such primitives from images by volume rendering is challenging, as they are Dirac masses defined at infinitesimal locations in space. EWA splatting, Poisson reconstruction, and 3D Gaussian Splatting overcome this by convolving Dirac masses with a low-frequency kernel, a recipe that generalizes along two axes: the kernel and the primitive. As points and triangles have already received significant attention, we investigate this recipe for curvilinear primitives, and introduce Spaghetti Splatting. We approximate curves by polylines whose convolution converges to that of the continuous curve, and volume render each segment so that connected segments composite without overcounting at their joints. For fast training and inference, we linearize the camera projection per segment, which also accommodates kernels beyond Gaussians, such as Beta kernels. As a point is a curve of zero length, our representation is a strict superset of 3D Gaussian Splatting. It remains competitive with the state-of-the-art on general scenes, outperforms methods specialized to line-like geometry, natively supports anti-aliasing, and produces long connected strands that are directly amenable to physics simulation.

---


### 494. [KiteNorm: Variance Regularisation for Stable and Scalable Post-LN Transformers](https://arxiv.org/abs/2611.12729)

**<font color=#1a73e8>作者：</font>** Leon A. Trochelmann, Sajad Movahedi, Shiwei Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-LayerNorm Transformers have seen limited practical adoption due to enduring difficulties in scaling them to large depths. While prior research has focused on stabilising Post-LayerNorm by improving conditioning at initialisation, stability often deteriorates when models are trained with large learning rates, forcing additional compromises. In the decoder-only settings we study, existing Post-LayerNorm methods fail to outperform strong Pre-LayerNorm baselines. We propose KiteNorm, a post-norm training method designed to break this trend by constraining hidden-state variance. This approach is motivated by a bound on the LayerNorm Jacobian suggesting that variance growth contributes to gradient vanishing, alongside empirical evidence linking it to rank collapse. KiteNorm combines residual scaling and variance regularisation to maintain stability throughout training, supported by scalarised double-normalisation that provides separately learnable scales for the skip and residual branches. Across decoder-only Transformers up to 1.3B parameters, KiteNorm improves training stability and outperforms leading baselines at their optimal learning rates, with scaling laws favouring KiteNorm across depth, width, batch size, and training budget. Ablations show that each component is necessary for the full stability and performance gains.

---


### 495. [$Σ$-LeWM: Learning World Models via S-Information for Robot Control](https://arxiv.org/abs/2611.12732)

**<font color=#1a73e8>作者：</font>** Xinrui Zu, Michael Przystupa, Zhao Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models have increasingly been applied as a model-based control method for robotics tasks such as manipulation and locomotion. While early world model architectures relied on decoders to prevent mode collapse and learn a predictable latent space, recent works on world models, such as Joint Embedding Predictive Architecture or LeWorldModel, increasingly aim to learn embeddings without a grounding decoder, utilising only a latent forward dynamics predictor and a stabilising entropy term. In this paper, we set out to demonstrate that the further introduction of two additional latent losses to LeWorldModel, a backward dynamics predictor and an inverse dynamics action predictor, enforces further structure on the latent embedding, leading to further gains in both performance and planning efficiency. These are critical properties for improving the applicability of such methods to real-time model-based control of real-world robots. We demonstrate these gains on standard world model benchmarks and two simulated robot manipulation tasks.

---


### 496. [Plant Orbiter: 3D Plant Reconstruction and Generation with Video Diffusion Orbit Cameras and 3D Gaussian Splatting](https://arxiv.org/abs/2611.12739)

**<font color=#1a73e8>作者：</font>** Zane K. J. Hartley, Yong En Kok, Lewis A. G. Stuart 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern digital phenotyping pipelines require the precise measurement of a range of 3D morphological plant traits. The accurate, high throughput acquisition of these traits helps breeders and researchers accelerate the development of new varieties, techniques and products. Recent advances in 3D technologies have enabled a rapid transition from 2D to 3D pipelines, but high throughput acquisition of digital 3D twins of plants remains a significant challenge due to complex morphology, thin structures and occlusions. In this paper we present Plant Orbiter, a new approach to generating 3D plants that leverages recent advances in video diffusion to produce high quality 3D Gaussian Splats of plants from a single image. We show that our method more accurately recreates plant morphology than other state-of-the-art methods, achieving the highest 3D F-score against all baselines, while being more practical for high throughput pipelines due to easier alignment and reduced cost of camera placement. Combined with a 2D diffusion model, we show that our method also achieves state-of-the-art results in the generation of 3D plant models from a text prompt.

---


### 497. [Clique Constraints for Exact Causal Structure Learning](https://arxiv.org/abs/2611.12747)

**<font color=#1a73e8>作者：</font>** Xiaoyu He, Pavel Rytíř, Petr Ryšavý 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Exact score-based causal structure learning supports explicit structural constraints and optimisation certificates, but its branch-and-cut search can be computationally demanding. We augment exact causal structure learning methods with an upper bound on the maximum clique size of the learned undirected skeleton, enforced at integer candidates through lazy cycle and clique constraints. On static linear-Gaussian Erdős-Rényi and scale-free DAGs, we evaluate callback order, alternative clique-cut policies, incumbent repair, fractional separation, and Big-M bounds. We report causal-recovery metrics jointly with optimality gaps, primal and dual bounds, node throughput, MIPSOL events, and callback cost. Two variants receive particular attention: B3 selects the most violated minimal (k+1)-clique inequality at each callback, whereas C3 repairs an infeasible integer candidate by deleting violating edges and refitting affected regression columns using QR-based least squares. The results do not indicate that clique constraints uniformly accelerate optimisation. However, their benefit depends on graph density, sample size, and cut-management policy, while large collections of correlated constraints can reduce node throughput. Tighter valid Big-M bounds reduced the fixed-budget optimality gap in most tested settings, without necessarily changing SHD or F1 at a fixed time limit. These findings characterize the computational trade-offs of clique-constrained exact causal learning, and identify selective separation and incumbent repair as promising directions.

---


### 498. [DeepChronos: Temporal Neuro-Symbolic Reasoning for Multi-Step Attack Detection](https://arxiv.org/abs/2611.12760)

**<font color=#1a73e8>作者：</font>** Sofia Burkow, Andrea Agiollo, Enkeleda Bardhi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern cyber threats commonly unfold as multi-step attacks comprising temporally and causally related phases. Current defenses commonly follow a detect first and correlate later paradigm. Intrusion detection systems classify events independently, while downstream systems reconstruct attack progression from the resulting alerts or audit records. In this context, learning-based detectors learn attack-step dependencies implicitly as statistical regularities in the data and cannot guarantee that their predictions follow the real attack progression. Conversely, correlation systems represent attack relationships explicitly, but apply this knowledge only after the underlying attack observations have been detected. We present DEEPCHRONOS, a neuro-symbolic network intrusion detection system that shifts the paradigm from detect first and correlate later to detection through logical progression. DEEPCHRONOS combines learned flow-level evidence with explicit attack-phase rules, temporal prerequisites, and previously inferred phases, allowing the evolving attack history to inform and constrain each detection decision. Evaluations on DARPA 2000 and AIT-LDS V2 show that DEEPCHRONOS improves macro F1 over purely neural baselines by up to 11.3%, eliminates causal violations under strict temporal constraints, and maintains millisecond-scale inference latency. These results demonstrate that integrating explicit attack progression knowledge into detection produces more accurate and temporally coherent multi-step attack predictions.

---


### 499. [Sage-Taiyi: A Metacognitive Architecture for Scientific Discovery](https://arxiv.org/abs/2611.12762)

**<font color=#1a73e8>作者：</font>** Weida Wang, Benteng Chen, Yigeng Jiang 等 90 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce Sage-Taiyi, a metacognition-inspired architecture that uses accumulated scientific understanding to guide what to investigate next and how to investigate it. Through explicit monitoring and control, the system revises its understanding of evidence, assumptions, and unresolved questions, then uses these assessments to adapt research targets and select reusable reasoning methods. On Taiyi-Bench, an AI co-scientist ideation benchmark comprising 265 tasks from 50 papers across ten disciplines, Sage-Taiyi ranks first on all eight metrics of historical rediscovery and open-ended ideation, achieving an Overall score of 54.0 compared with 47.9 for the strongest baseline, AI Scientist-v2. It also performs well on two external scientific ideation benchmarks. Five expert-guided collaborations further connect its proposals to experimental and computational validation across chemistry, materials science, and engineering. In chemistry, reaction-condition optimization raises the yield of cobalt-catalyzed carbonylation from trace amounts to 84% and photocatalytic allylic amination from 13% to 69%. These results support metacognitive regulation as an approach to scientific ideation and its progression toward practical validation.

---


### 500. [Anchor Behavior, Not Parameters: Rehearsal-Free Continual Learning with a Single Shared Prompt](https://arxiv.org/abs/2611.12777)

**<font color=#1a73e8>作者：</font>** Duy-Cuong Bui, Trung-Anh Dang, Vincent Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prompt-based continual learning adapts a frozen pre-trained vision transformer by tuning a small set of prompt tokens. Recently, one-prompt methods which share one single prompt across all tasks make this paradigm maximally parameter efficient. The open question is how a shared prompt can keep the knowledge of old classes while being updated for new ones. Existing methods protect old knowledge in parameter space, where they freeze task-specific prompts, expand new components, or sparsely gate which tokens receive gradients. However, this method sacrifices plasticity, yet the drift it still permits in shared tokens can corrupt the prompt's function on past classes. What must be preserved is the prompt's behavior. We propose TEA-Prompt, which couples (i) a token evaluation module that assigns each prompt token a continuous, input-conditional relevance score injected into the attention logits, softly specializing tokens across tasks without discarding any of them, and (ii) an attention-behavior anchoring loss that constrains each token's attention output around class-specific query regions using only compact Gaussian query statistics without stored old images, weighted by the token's past relevance. Anchoring the attention value allows the parameters to continue updating freely, as long as their interaction remains unchanged. TEA-Prompt achieves state-of-the-art accuracy with markedly lower forgetting on CIFAR-100, ImageNet-R, and CUB-200 with only 0.38M parameters. Code is publicy available at this https URL

---


> [!TIP]
> 当前位于：**451-500**（第 10/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-520](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
