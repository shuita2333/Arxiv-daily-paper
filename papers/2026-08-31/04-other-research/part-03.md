# 📦 其他研究 | 2026年08月31日

> 本类共 **202** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-202](./part-05.md)

---

### 101. [Beyond Client Averaging: A Client-Independent Second-Order Stationary-Bias Component in Stochastic SCAFFOLD](https://arxiv.org/abs/2608.26765)

**<font color=#1a73e8>作者：</font>** Yi-Ping Tang, Guan-Ju Peng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing constant-step analysis of stochastic \Scaf{} identifies a leading $O(\gamma/N)$ stationary mean bias and shows that higher-order bias can persist as the client count increases, but does not identify the first client-independent contribution at coefficient level. For full-participation stochastic \Scaf{} with one-dimensional homogeneous clients, fixed local-step count $H$, and bounded additive gradient noise, we prove, uniformly over $N\ge2$,
$$ \begin{aligned} \mathbb{E}_{\pi_{\gamma,N,H}}[x]-x^\star ={}& -\frac{f'''(x^\star)\sigma^2}{4f''(x^\star)^2}\frac{\gamma}{N}\\ &- \frac{f'''(x^\star)\sigma^2}{12f''(x^\star)} \frac{(H-1)(5H-1)}{H}\gamma^2 +O_H\!\left(\frac{\gamma^2}{N}+\gamma^3\right). \end{aligned} $$
Hence client averaging suppresses the leading $O(\gamma/N)$ bias but does not remove the client-independent $O(\gamma^2)$ component when its coefficient is nonzero.
The mechanism is indirect: although the direct control contribution cancels pathwise in the linear global average, the controls still alter within-round local trajectories and their second moments. Fresh gradient noise and persistent control fluctuations therefore generate local second-moment corrections that nonquadratic curvature converts into stationary mean bias. The coefficient vanishes for quadratic objectives. Numerical experiments are consistent with the predicted coefficient, its persistence as client count increases, and the stated joint remainder. The result is restricted to the one-dimensional homogeneous fixed-$H$ setting.

---


### 102. [A Hybrid Post-Quantum Encryption Architecture with Self-Hosted Key Management for SME Cloud Data Protection](https://arxiv.org/abs/2608.26777)

**<font color=#1a73e8>作者：</font>** Muhammad Shaheer Bin Junaid  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Harvesting ciphertext from cloud storage needs no quantum computer; decrypting it later does. That gap is the harvest-now-decrypt-later exposure: anything protected by RSA or ECDH today that must stay secret for decades is already compromised. Small and medium-sized enterprises are least able to respond: they neither run the infrastructure on which their data sits on nor employ a cryptographer. Bespoke migration suits firms with security budgets; a managed key service relocates trust rather than removing it. The obstacle is architectural, not cryptographic. We present Quantum Cloud Guard (QCG), a software-only three-layer architecture. No prior SME-oriented system combines its three elements: client-side hybrid post-quantum encryption, self-hosted key custody with client-verifiable ML-DSA-87 signatures on served keys, and an integrated application-layer abuse-prevention gateway. Files never leave the client: each is sealed under AES-256-GCM, its key wrapped to an ML-KEM-1024 public key from the enterprise's key service. The enterprise alone administers it; it signs every key with ML-DSA-87, so a client that pinned it detects substitution. Separating key custody from data custody is the point: a provider holding both can read the data. On a 24 MHz STM32F407, ML-KEM-1024 key generation takes 40.8 ms and decapsulation 44.0 ms; on the server every post-quantum operation stays sub-millisecond, signing adding 0.24 ms per request. The service runs on a 4.49 EUR/month virtual server. Under sustained flooding, the in-process gateway Sentinel Gate rejected 98.8% of attack traffic while a legitimate client's median latency moved from 621 to 625 ms. Being single-source, this shows filtering effectiveness, not DDoS resilience.

---


### 103. [Thresholding Post-Quantum Signatures](https://arxiv.org/abs/2608.26792)

**<font color=#1a73e8>作者：</font>** Francesco De Sclavis, Matteo Nardelli, Marco Pedicini  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Threshold signature schemes distribute the signing process among $T$ parties out of $N$. They enable a variety of applications and their research is also motivated by a recent NIST call. However, applications are dominated by pre-quantum signatures, which are more efficient but not secure in the post-quantum setting. This paper investigates existing post-quantum signatures, based on a variety of paradigms: lattice problems, one-way (hash) functions, cryptographic group actions, isogenies and multivariate systems. We propose a classification (divided by paradigm) of existing tools that are used to build $T$-out-of-$N$ schemes from digital signatures. We also include general approaches based on FHE, MPC or ZKP.

---


### 104. [Ring Forcing: Towards Precise Long-Term Memory for Autoregressive Video Diffusion](https://arxiv.org/abs/2608.26794)

**<font color=#1a73e8>作者：</font>** Bowen Xue, Brandon Y. Feng, Chenguo Lin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scaling video generation to long durations reveals a critical bottleneck: current models lack robust long-term memory. This deficiency can be studied along two critical aspects: object permanence, the ability to precisely reproduce the appearance of objects upon re-entry; and memory capacity, the ability to process ultra-long context and use information from distant history. Robust long-term memory requires both: object permanence without sufficient context handling limits the temporal scope, while long context length without permanence fails to maintain identity. To address this, we present Ring Forcing, an autoregressive video diffusion framework designed to robustly construct and precisely utilize long-term memory. Our ring-structured training strategy enforces retrieval from distant history, effectively reconciling the trade-off between strict historical adherence and generative diversity. To expand memory capacity, we introduce a compression and timestep composition strategy. Under fixed sequence length constraints, this method extends the effective historical span to minutes-long durations and achieves a comprehensive receptive field over the entire history. Furthermore, we present a sparse RoPE mechanism to enable flexible, scalable memory adaptation while fully exploiting pre-trained priors. Extensive experiments demonstrate that Ring Forcing achieves superior minutes-long coherence and object permanence, significantly outperforming state-of-the-art methods.

---


### 105. [Hyperspectral Diffusion Equivariant Imaging (HyDiff-EI): A Self-supervised Framework for Hyperspectral Image Inpainting](https://arxiv.org/abs/2608.26812)

**<font color=#1a73e8>作者：</font>** Shuo Li, Mike Davies, Mehrdad Yaghoobi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A novel Hyperspectral diffusion Equivariant Imaging (HyDiff-EI) framework for solving the hyperspectral image (HSI) inpainting problem has been presented here. Unlike conventional diffusion-based methods that rely on large-scale pretraining, HyDiff-EI is a test-time optimization framework that learns directly from a single corrupted HSI acquisition. This makes it flexible for different sensor configurations and particularly well-suited for practical remote sensing scenarios where large annotated hyperspectral datasets are limited. To address the ill-posed nature of unsupervised inpainting, we embed equivariant consistency constraints within the diffusion process. By leveraging the inherent geometric symmetries and intrinsic characteristics of HSIs, HyDiff-EI bridges the gap between generative diffusion modeling and self-consistent physical priors. We empirically show that coupling diffusion modeling with equivariant priors substantially enhances noise robustness and generalizability. Extensive experiments on real-world datasets including Chikusei, Botswana, and EMIT demonstrate that HyDiff-EI offers remarkable inpainting quality over existing self-supervised and diffusion-based algorithms in both noiseless and noisy cases.

---


### 106. [Evaluator-Dependent Patient-Adaptive ECG Lead-Channel Allocation](https://arxiv.org/abs/2608.26827)

**<font color=#1a73e8>作者：</font>** Xiaoyang Li, Zeyan Tao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Patient-conditioned acquisition policies for ECG lead-channel selection can outperform population-wide fixed protocols by tailoring the channel budget to each patient's observed cardiac state. However, the value of acquiring any given channel is defined relative to a downstream diagnostic evaluator, so marginal utilities learned under one evaluator need not transfer when the evaluator is replaced. We study this evaluator dependence empirically on PTB-XL by freezing two policies (ECG-on-Demand and MGA) trained with a controlled arbitrary-mask logistic evaluator, then scoring their unchanged acquisition trajectories with a more predictive masked raw-waveform ResNet1D. Exhaustive search provides metric-matched population-wide fixed comparators separately for each evaluator, enabling a clean interaction contrast. At budget $k=4$ on a held-out evaluation fold, ECG-on-Demand shifts from $D_\mathrm{C}=-0.011$ (favoring adaptive under the controlled evaluator) to $D_\mathrm{S}=+0.029$ (favoring fixed under the strong evaluator), yielding an NLL interaction of $+0.041$ (95% CI $[+0.030, +0.050]$). Across two policies, five budgets, and three probabilistic metrics, all 30 interaction estimates are positive with paired confidence intervals excluding zero. Three post-hoc sensitivity analyses -- common-reference scoring, training the strong evaluator on a mixture of policy-generated and random masks, and evaluator-aligned Strong-MGA policy training -- each preserve a positive interaction interval, making reference-choice and mask-distribution artifacts less plausible explanations. Evaluator-aligned training reduces but does not eliminate the gap. These results indicate that adaptive ECG channel allocation should be developed and validated jointly with its intended diagnostic backbone, and that jointly optimized sensing-diagnosis systems remain an open problem.

---


### 107. [When Relationships Break: Interpreting Network Traffic Anomalies via Dependency Violations](https://arxiv.org/abs/2608.26831)

**<font color=#1a73e8>作者：</font>** Federica Uccello, Simin Nadjm-Tehrani  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Current research on security monitoring is increasingly focusing on machine-learning-based approaches, but caveats remain. In addition to huge computational overhead, one concern is the lack of insights into "why" alerts are raised. Existing interpretability approaches rely on feature attribution methods that ignore dependencies among features or on causal modeling that requires extensive domain knowledge or computational resources. This work proposes XION, a method for modeling relationships among network-flow features based on benign traffic only. During detection, anomalies are identified through violations of expected feature dependencies. Further, XION supports post-alert analysis by identifying which feature relationships break, when they break along the attack timeline, and how dependency violations evolve relatively to other identified violations. XION is evaluated on standard IDS datasets and compared against an Isolation Forest (IF) baseline across multiple attack scenarios, including both volumetric and stealthier attacks. Results show that XION matches or exceeds IF recall in all evaluated scenarios, while requiring up to 7x less inference time. At the post-alert stage, the dependency-violation analysis reveals temporal and structural patterns consistent with known attack behaviors, which IF alone could not contribute to. Together, these findings confirm that attacks indeed disrupt feature dependencies learned from benign traffic, and that these disruptions provide additional information for understanding an alert.

---


### 108. [Rethinking Image Processing for the Age of AI: A Problem-First Framework for Scientific Progress](https://arxiv.org/abs/2608.26833)

**<font color=#1a73e8>作者：</font>** Guoping Qiu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern AI has greatly expanded the capabilities of image processing. However, the ready availability of powerful models, public datasets, and benchmark leaderboards has also en- couraged a model-first research pattern: researchers increasingly begin with an available architecture and optimize it on a public benchmark, rather than beginning with the underlying real-world imaging problem. This can produce impressive benchmark results without necessarily improving our understanding or solution of the real problem. This paper argues for a problem-first approach that distinguishes the physical imaging problem, solution principle, statistical estimator, and computational implementation, while clarifying what modern AI can achieve and which fundamental problems remain unsolved. Through case studies of super- resolution and low-light enhancement, we show how benchmark datasets may define tasks that differ substantially from the real-world problems they are intended to represent, and why performance improvements must be interpreted within the conditions under which they are obtained. We propose a six-stage workflow that places problem formulation, image acquisition, information-loss analysis, assumptions, ambiguity, and evaluation before model and dataset selection. The paper also proposes clearer standards for evidence, reproducibility, uncertainty, and claims of state-of-the-art performance. More fundamentally, it calls for a change in research culture and education so that future researchers learn to understand imaging problems deeply and use modern AI to achieve genuine scientific and technical advancement.

---


### 109. [Information Flow Control in Off-Chain Components](https://arxiv.org/abs/2608.26858)

**<font color=#1a73e8>作者：</font>** Stian Lybech, Eun-Young Kang, Riccardo Tonello 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper develops a model of a smart-contract language for a blockchain architecture with off-chain components. Off-chain components are pieces of smart contracts that execute at designated locations outside of the network of blockchain nodes, but remain synchronised with the on-chain contract state. They react to changes to the on-chain state, but may also notify the on-chain component about events in the world, e.g. stock prices, weather data etc., or even act as a bridge between different blockchains. This affords greater flexibility for the developer, but may also enable new vulnerabilities. As a concrete example, we use the model to study the problem of ensuring integrity and secrecy of data between the on-chain and off-chain components, using static information flow control techniques. This fails, even in the absence of a loop construct, because off-chain components act as separate threads and can encode a blocking construct e.g. through recursive method calls. We end the paper with a discussion of possible ways to remedy this situation.

---


### 110. [A Geometry-Driven, Framework-Agnostic Optimization for Object Pose Estimation](https://arxiv.org/abs/2608.26859)

**<font color=#1a73e8>作者：</font>** Wei Chen, Tao Zhen, Zhongchen Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current object pose estimation research remains predominantly model-centric, focusing on architectural innovations and post-processing refinements. This paper introduces a data-centric optimization by proposing a novel, physically grounded rotation representation through principal axes alignment. Our method aligns the object's coordinate system with its inherent geometric axes, derived from inertial properties, yielding three key advantages: Inherent Stability-leveraging the energy-minimizing property of principal axes provides a robust representation that is less sensitive to noise and occlusions; Symmetry-Aware Canonicalization-explicitly resolving rotational ambiguities for symmetric objects at the data level, which fundamentally eliminates label confusion during network training; and Framework Agnosticism-the optimization is applied purely at the dataset level, ensuring plug-and-play compatibility with existing networks without any architectural modification. We validate the framework across diverse category-level and instance-level models. Extensive experiments demonstrate consistent and significant accuracy improvements, while preserving the integrity of the baseline network. This work establishes a new, geometry-driven direction for enhancing pose estimation, circumventing the need for complex network redesign.

---


### 111. [Reinforcement Learning-Based Control of CAV Platoon Joining Maneuvers in Mixed Traffic](https://arxiv.org/abs/2608.26860)

**<font color=#1a73e8>作者：</font>** Biao Yin, Abderrahmane Kasmi, Nadir Farhi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Connected and automated vehicle (CAV) platooning offers a promising approach to improving road safety and traffic capacity. However, platoon control in real-world traffic is challenging due to uncertainty and heterogeneous driving behaviors. Reinforcement learning (RL) has strong potential for addressing such control problems, but its practical deployment raises challenges related to safety and learning efficiency. This paper proposes a generic modeling and simulation framework for investigating CAV platoon joining maneuvers and comparing deep reinforcement learning (DRL)-based control algorithms. The problem is particularly challenging in mixed-traffic environments, where CAVs coexist with human-driven vehicles exhibiting heterogeneous longitudinal and lateral behaviors. The objective is to achieve safe and efficient joining maneuvers by either incorporating penalties for risky behaviors into the learning process or using an external safety controller to constrain the learned policy. An agent-based modeling framework coupled with the Simulation of Urban MObility (SUMO) simulator is used to evaluate Deep Q-Network (DQN), Double Deep Q-Network (DDQN), and Proximal Policy Optimization (PPO). Results show that PPO outperforms DQN and DDQN, achieving a joining success rate of approximately 98 % and a collision rate below 1 %, largely due to risk-related penalties incorporated into the reward function. However, this improved performance requires more decision steps to complete the maneuver, revealing a trade-off between safety, joining effectiveness, and decision efficiency. An external safety controller effectively prevents collisions, although its interventions may reduce joining efficiency. The results highlight the importance of jointly considering safety and efficiency when designing RL-based controllers for CAV platoon joining in mixed traffic.

---


### 112. [FIDA: Feature Instability-Driven Attack on Self-Supervised Facial Representation](https://arxiv.org/abs/2608.26861)

**<font color=#1a73e8>作者：</font>** Zhiyang Chen, Changchun Yin, Huiqin Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning (SSL) models are vulnerable to backdoor attacks. However, the systemic risks they pose in face representation have received little attention. The entanglement of identity features in self-supervised face learning presents unique challenges for attack stealthiness. To address this gap, we propose FIDA (Feature Instability-Driven Attack), a novel backdoor attack framework. FIDA uses subtle semantic triggers for injection, but its key innovation is a novel objective called Feature Instability Loss. It trains the encoder to increase the sensitivity of triggered features along perturbation directions sampled during attack optimization . By preventing the backdoor from exhibiting the rigid feature patterns typical of previous attacks, FIDA effectively evades the evaluated perturbation-based defenses. Experiments show that FIDA achieves a high attack success rate and generally preserves benign utility across the evaluated settings , posing a significant threat to real-world multimedia applications relying on facial analysis.

---


### 113. [CGS-SLAM: Collaborative Gaussian Splatting based SLAM for Multi-Agent Reconstruction](https://arxiv.org/abs/2608.26868)

**<font color=#1a73e8>作者：</font>** Jean-Daniel de Ambrogi, Aladine Chetouani, Vincent Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in SLAM have leveraged 3DGS for photorealistic reconstruction and novel view synthesis. However, most methods rely on RGB-D input, which is unavailable on consumer-grade smartphones, and few integrate 3DGS within a collaborative framework. Therefore, we present CGS-SLAM, a hybrid decentralized/centralized system enabling multi-agent 3DGS SLAM using only RGB and inertial data. Each agent performs local tracking with inertial data as a motion prior and reconstructs a scaled map using a metric monocular depth estimator (Depth Pro). Keyframe encodings are shared among agents, enabling dynamic keyframing in regions of spatial overlaps with other agents, enhancing submap alignment. Afterwards, a central server aligns submaps using VGGT as a view alignment model. This bidirectional communication keeps communication cost low during mapping and global reconstruction in difficult GNSS-denied environments. Experiments on multiple datasets demonstrate competitive tracking performance, improved rendering quality over state-of-the-art methods, and accurate submap alignment.

---


### 114. [SysComb: Fine-Grained Transparent System Call Filtering for Attack Surface Reduction](https://arxiv.org/abs/2608.26871)

**<font color=#1a73e8>作者：</font>** Matthew Rossi, Marco Abbadini, Michele Beretta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Restricting the system calls available to applications shrinks the kernel's attack surface and greatly mitigates the impact of compromised programs. Recent approaches showcase techniques to generate system call filters, however, all existing solutions require either kernel or application modifications to activate them at runtime. This is intrusive, error-prone, and often impractical, especially when the code is maintained by external parties. This paper presents SysComb, a novel eBPF-based solution to enforce temporally-specialized system call filters based on the application state, without requiring any modification to the application or the kernel code, and thus addressing the above limitations. Moreover, SysComb lets the developer choose between two distinct enforcement strategies: seccomp-like, ensuring no new privileges are gained after a state transition is performed, and least-privilege, which applies to each state the most restrictive filter. We evaluated SysComb using widely used software, showcasing accurate state-aware system call filtering and an overhead comparable to built-in kernel solutions, demonstrating the practicality of our approach.

---


### 115. [When Is the Sharp Covariance Envelope Tight? Feature-Only Geometry for Volume-Sampled Least Squares](https://arxiv.org/abs/2608.26877)

**<font color=#1a73e8>作者：</font>** Kihun Rhee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prior analyses by Derezinski and Warmuth established all-size sampling identities, selected-OLS unbiasedness, and inverse moments for ordinary volume sampling, while their exact arbitrary-fixed-response loss and prediction-covariance formulas are at the rank-size endpoint s=d. We establish a Loewner envelope for centered coefficient covariance for every full-rank fixed pool, response, and legal budget d <= s <= m under ordinary indexed fixed-size volume sampling followed by selected unweighted least squares; its coefficient is globally sharp over the full-rank class. Global sharpness does not determine attainability on the pool in hand. Under positive loss, strict-interior budgets, and no coloops, a feature-only margin nu_A gives the exact fixed-design spectral phase: nu_A > 0 if and only if the normalized spectral envelope is strict for every compatible residual, whereas nu_A = 0 if and only if some compatible residual is spectrally tight; the same zero-margin residual is tight at every strict-interior budget. A residual-augmented change of measure supplies the response-aware mechanism and a one-sided quantitative slack bound, while support saturation proves the attainment direction. Critical equal-leverage geometry interprets the boundary, and sound lower certificates yield conservative same-primitive cardinality decisions. Frozen-feature examples show that the certificate is nonvacuous and measure the fixed-pool cost of its authorized reduction. The claims concern conditional centered, full-Gram-whitened coefficient covariance, not population generalization.

---


### 116. [Mitigating Strong-Modality Collapse in Multimodal Learning via Inverted Asymmetric Fusion](https://arxiv.org/abs/2608.26879)

**<font color=#1a73e8>作者：</font>** Mary Ogbuka Kenneth, Foaad Khosmood, Abbas Edalat  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fusing multiple modalities is expected to improve model performance. However, on the MultiHuSE dataset, early, late, and symmetric attention fusion often fail to outperform the best unimodal baseline (text). Pathway isolation of a symmetric attention fusion model reveals that the text-pathway accuracy drops from 74.9% to 56.4% after fusion in one such setting, indicating that the dominant modality can be degraded during integration. We term this strong-modality collapse and argue that it helps explain why some multimodal models fail to surpass unimodal baselines. We propose Inverted Asymmetric Fusion (IAF), which avoids forcing mutual attention across modalities. The dominant modality is preserved by passing through fusion unchanged, while weaker modalities attend to it as a contextual anchor. Before fusion, weaker modalities are strengthened using Modality-Aware Knowledge Distillation. We evaluate IAF on three benchmarks with different modality hierarchies: text-dominant datasets (MultiHuSE, UR-FUNNY) and an audio-visual-dominant dataset (MUStARD). Pathway isolation shows that IAF preserves the dominant modality's internal accuracy at its unimodal ceiling across all tested configurations, whereas symmetric fusion degrades it by up to 18.5% on MultiHuSE. IAF improves over the strongest unimodal baseline by up to 8.25%.

---


### 117. [Learning-Augmented Online Allocation under Unreliable Advice: Robustness, Exposure Fairness, and Distribution Shift](https://arxiv.org/abs/2608.26889)

**<font color=#1a73e8>作者：</font>** Fredy Pokou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning-augmented algorithms improve online decisions using predictions, but unreliable advice may harm efficiency and fairness. We study an online allocation problem with finite candidate sets, irreversible decisions, and exposure constraints. We propose a robust and fair rule combining advice with a conservative fallback and fairness correction. Under bounded-error assumptions, we prove consistency and robustness with loss proportional to prediction error. Experiments show stability under adversarial advice and significant reductions in exposure disparity.

---


### 118. [AI agents in Algorithmic Electricity Markets: On the Emergence of Tacit Collusion](https://arxiv.org/abs/2608.26896)

**<font color=#1a73e8>作者：</font>** Jakub Seredyński, Georgios Tsaousoglou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As electricity market participants increasingly adopt learning-based agents for their bidding strategies, electricity markets are becoming algorithmic. Evidence from algorithmic markets in other domains shows that tacit collusion can arise purely through independent learning. Moreover, electricity markets are typically oligopolistic and feature repeated interaction among a small number of participants, making them structurally susceptible to non-competitive behavior. In the face of these observations, this paper investigates the hypothesis that tacit collusion may emerge in electricity markets where participants' actions are controlled by autonomous learning-based algorithms. We model strategic bidding as a repeated game with imperfect public monitoring, and model the participants' emergent behavior using multi-agent reinforcement learning. We propose a multi-dimensional set of criteria (going beyond profit comparisons against Nash equilibria) to assess whether the resulting behavior constitutes tacit collusion. Our experimental results showcase that such a danger is realistic for electricity markets: there are cases where agents do learn to sustain supra-competitive outcomes that are supportive of tacit collusion indicators, even though the agents were never instructed to collude.

---


### 119. [Tether the Subject, Release the Scene: Query-Aware Memory Routing for Long-Horizon Autoregressive Video Generation](https://arxiv.org/abs/2608.26902)

**<font color=#1a73e8>作者：</font>** Chen Li, Peng Zhang, Hanyu Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming autoregressive video models generate long videos chunk by chunk, using historical memory to maintain consistency. Existing methods typically expose subject and scene queries to history through similar policies. This stabilizes the subject, but can also lock backgrounds, viewpoints, and scene structure to previously generated states even when local motion continues. We call this failure memory-anchored scene under-progression; consistency and motion metrics alone can miss it. We introduce TetherMem, a training-free, query-aware spatiotemporal memory router for frozen video generators. TetherMem separates subject and scene queries and modulates historical access with region- and age-conditioned priors: subject queries retain identity-bearing history, while scene queries reduce reliance on subject history and stale backgrounds. Across 2,400 blinded pairwise judgments from 10 annotators, TetherMem achieves the highest estimated expected preference among eight streaming long-video baselines for overall quality (0.780) and scene progression (0.769). On complete 30-second videos, it sustains changes in background, viewpoint, and scene state while preserving subject recognizability and temporal continuity.

---


### 120. [Mapping Written Words to Spoken Words in a Different Language Using Only Visual Grounding](https://arxiv.org/abs/2608.26925)

**<font color=#1a73e8>作者：</font>** Gabriel Pirlogeanu, Dan Oneata, Horia Cucu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In many low-resource settings, even just eliciting speech for data collection is difficult. One promising approach has been to ask speakers to describe images. But how do we build models from such visually grounded speech data? Given a dataset of images with Hindi spoken captions, we consider how we can map a written English keyword to spoken realisations of that word in Hindi. Previous work trained end-to-end multimodal neural models. Instead, we explore a simpler alignment-based approach built on self-supervised speech representations. Written English tags are automatically obtained from images using off-the-shelf image captioning systems. Hindi utterances associated with the same keyword are then aligned (using self-supervised features), and alignment evidence is aggregated to identify recurring speech segments corresponding to the target word. Experiments evaluating keyword spotting and localization show that our alignment-based approach outperforms a previous attention-based neural model. We also show the benefit of incorporating negative examples during alignment. Our work demonstrates that cross-lingual word-to-speech mappings can be learned directly from visual grounding without transcriptions or explicit model training.

---


### 121. [Dynamic Haven Selection for Multi-Agent Pickup and Delivery in Constrained Warehouses](https://arxiv.org/abs/2608.26939)

**<font color=#1a73e8>作者：</font>** Taisei Hirayama, Kohei Yoshida, Hiroki Sakaji 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Space-efficient warehouse layouts often contain single-agent-width aisles and dead-end workstations where robots have few places to wait without blocking others. In Multi-Agent Pickup and Delivery (MAPD) on such constrained layouts, robots must accept online pickup-delivery tasks while preserving protected waiting locations called Havens. The Safe HAven Retreat Planner (SHARP) introduced a mechanism that extends each committed task path with a validated retreat to the agent's dedicated initial Haven, but fixed-Haven commitments can send agents toward distant Havens after deliveries. We present A-sharp (Adaptive SHARP), which changes an agent's retreat target at task assignment time. A naive switch can cause two agents to rely on the same waiting location or let another committed path pass through a location that is still occupied or reserved. A-sharp prevents these failures with an availability test for candidate Havens and a pending-release rule that keeps the previous Haven protected until the agent departs. Under explicit Haven-structure and Safe Interval Path Planning (SIPP) assumptions, we prove invariant preservation and finite-release completeness: every task in any finite release sequence is delivered in finite time. Across 72,000 runs on 14,400 paired map-agent-count-rate-seed cases over four maps, both SHARP and A-sharp complete their respective 14,400 runs. For makespan (final delivery time), a prespecified paired comparison with Holm correction over all 138 configurations with more Havens than agents finds A-sharp significantly better in 107 configurations and never significantly worse than SHARP; on the tested tree map, the median reduction is 16.7%.

---


### 122. [KinyaEmbed: Contrastive Sentence Embeddings for Kinyarwanda via Multi-Stage Curriculum Training](https://arxiv.org/abs/2608.26941)

**<font color=#1a73e8>作者：</font>** Ireddi Rakshitha, Devavarapu Yashwanth, Ntakirutimana Pierre  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present KinyaEmbed, the first dedicated sentence embedding model for Kinyarwanda, a morphologically rich Bantu language spoken by over 12 million people in Rwanda. Existing multilingual embedding models such as LaBSE, mE5-large, and OpenAI text-embedding-3-large perform poorly on Kinyarwanda due to severe under-representation in their pre-training corpora. KinyaEmbed is built on KinyaBERT-large and trained via a four-stage curriculum using MultipleNegativesRankingLoss (MNRL): Stage 1 leverages ~18,000 paraphrase pairs from the Official Gazette of Rwanda with three temperature scales; Stage 2 fine-tunes on 715 NLLB-translated MNLI triplets for entailment structure; Stage 3 aligns representations using English-Kinyarwanda OPUS-100 translation pairs; Stage 4 refines with 2,936 high-quality pairs filtered from KinyaCOMET at quality threshold 0.8. We evaluate on SemRel2024-rw and introduce Wiki-RW-STS, a new contamination-free Kinyarwanda STS benchmark of 300 pairs derived from Kinyarwanda Wikipedia. A seven-checkpoint ensemble (all5+23A*2, with the final stage double-weighted) achieves Spearman \r{ho}=0.7298 on SemRel2024-rw, surpassing mE5-large by 20.9% and OpenAI text-embedding-3-large by 41.0%. KinyaEmbed also achieves the best document clustering silhouette score (0.2146) across all evaluated models. All checkpoints, the KinyaCOMET filtered pairs, and the Wiki-RW-STS benchmark are publicly available.

---


### 123. [KISS-GS: 3D Gaussian Splatting Compression Kept Simple](https://arxiv.org/abs/2608.26948)

**<font color=#1a73e8>作者：</font>** Wieland Morgenstern, Friedrich Elias Branschke, Florian Fleischmann 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scene reconstruction with 3D Gaussian Splatting (3DGS) has become common, however deployment remains painful as the uncompressed file sizes can be massive. Current 3DGS compression systems combine multiple strategies for file size reduction, which can obscure where gains come from and limit component reuse across training pipelines. To make the gains more transparent, we propose KISS-GS, a modular compression pipeline named after the principle of keeping things simple, designed to decouple compression entirely from training.
Given a 3DGS scene reconstructed with vanilla 3DGS, we are able to reduce it through compaction by 15.7x using a combination of state-of-the-art pruning schemes. Then we encode it into an image-based format designed for simple, ubiquitous decoding. With the SOG-XT format, we propose a novel extension to Self-Organizing Gaussians with two main contributions: (i) Self-organizing 2D Codebooks and (ii) Parallel Representative Assignment Smoothing (PRAS), which leverages the symmetry of quaternion and scale parameterizations to produce 2D attribute grids more amenable to encoding.
This encoding reduces scene size by 6.6x. We show that optional encoding-aware fine-tuning yields a further 2.2x. Across standard 3DGS benchmarks, our simple and modular approach thus achieves a total of 85x to 319x reductions in the size of the scene over uncompressed vanilla 3DGS, setting new benchmarks for real-world scenes and surpassing tightly integrated methods in rate-distortion. Decoding relies solely on web-native image formats, and the modular design makes each stage easy to combine with future advances in reconstruction and compaction.
Code and project page: this https URL

---


### 124. [Per-View Gaussian Predictions Enable Training-Free Distractor Filtering in Feed-Forward 3DGS](https://arxiv.org/abs/2608.26951)

**<font color=#1a73e8>作者：</font>** Kangmin Seo, Jae-Pil Heo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D Gaussian Splatting reconstructs an explicit Gaussian representation from multiple input images in one network execution, making 3D reconstruction increasingly accessible for casual captures. However, such captures frequently contain transient objects that appear in only a subset of the views. Such content can be encoded into the per-view Gaussians associated with the inputs that observe it and remain in the combined representation despite being observed by no other input. As a result, it may produce blurred, duplicated, or floating artifacts in novel views. We introduce a training-free filtering procedure that exploits this per-view prediction structure. For each input, we exclude its associated Gaussians and render the same camera using the remaining representation, revealing content that is inconsistent with the other inputs. Feature similarity forms candidate regions, and rendering-based verification retains only candidates whose removal reduces reconstruction error in the other input views. The procedure operates on a single frozen prediction without retraining or scene-specific optimization. Across three reconstruction models and two distractor benchmarks, it consistently improves novel-view quality with varying numbers of input views. On clean scenes, evaluations across four models show that the original reconstructions are largely preserved.

---


### 125. [A Catalog of User Authentication Patterns](https://arxiv.org/abs/2608.26955)

**<font color=#1a73e8>作者：</font>** Alex R. Mattukat, Horst Lichter  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security patterns are intended to support the design and development of secure software systems. However, although established catalogs of security patterns exist, their practical application remains limited. In particular, despite these catalogs, concrete patterns for common security controls such as user authentication (authentication for short) are lacking. This paper aims to make an initial contribution toward closing this gap, as exemplified by authentication. It presents a novel authentication pattern catalog, comprising 14 user authentication patterns. To support the catalog's practical application, it classifies patterns by the well-known concept of authentication factors and by the usual role each pattern fulfills in practice. By cataloging common authentication techniques through authentication patterns, we aim to make an important contribution to supporting software engineers and architects in designing and developing secure software systems.

---


### 126. [Scaling Model-Generated Distillation Data Can Make Latent Teacher Traits More Recoverable](https://arxiv.org/abs/2608.26958)

**<font color=#1a73e8>作者：</font>** Zhichen Dong, Zhixuan Liu, Yuyu Fan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling model-generated data is usually viewed as improving distillation: more examples should increase coverage, reduce noise, and produce stronger students. We show a second effect: larger datasets can make subtle teacher-specific signals easier to detect in the trained student, even when examples are off-task and never mention the trait. In a controlled setup inspired by subliminal learning, a teacher induced to express a target trait generates restricted off-task data, such as number-only completions. Students trained on different amounts of independent off-task data are evaluated in a separate domain, with matched no-trait controls isolating target-specific transfer. Our main finding is that larger independent datasets make the teacher's induced trait stand out more clearly in the student's later behavior. Other plausible traits may also strengthen with scale, but the target usually grows more. When the small-scale student already favors the target, scaling mainly amplifies that behavior; when it favors a related or salient alternative, more data can shift behavior toward the intended trait. Analyses of learned LoRA updates show a parallel trend. These effects appear across model families, trait types, multi-trait settings, and cross-model transfer. Our results suggest that scaling generated distillation data should be paired with trait-aware curation and evaluation, even when the data appears off-task or benign.

---


### 127. [Geo-LoRA: Geometry-Aware Subspace Evolution for Low-Rank Adaptation in Continual Learning](https://arxiv.org/abs/2608.26960)

**<font color=#1a73e8>作者：</font>** Yibo Feng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rehearsal-free class-incremental learning (CIL) with LoRA adapters remains challenging because the low-rank subspaces updated across tasks evolve without geometric control, causing unstable shared representations and repetitive collapse of task-specific updates into previously occupied directions. We introduce Geo-LoRA, a geometry-aware framework that explicitly regulates how low-rank subspaces, both shared and task-specific, evolve during continual learning. For the shared branch, Subspace Projection Preservation (SPP) constrains consecutive updates to follow smooth trajectories on the Grassmann manifold, and Adaptive Core-Slack Alignment (ACSA) decomposes transitions into principal and residual components, aligning the former while modulating the latter to balance stability and plasticity. For the task-specific branch, Median-Calibrated Block Overlap (MCBO) imposes a statistical constraint via normalized projection overlap, penalizing excessive reuse to mitigate subspace crowding. These constraints jointly regulate the evolution of all LoRA subspaces across layers and tasks without introducing additional adapter types beyond standard LoRA. Geo-LoRA provides a principled geometric formulation for continual low-rank adaptation and consistently achieves state-of-the-art performance across multiple benchmark datasets and different task lengths.

---


### 128. [Gromov-Monge Flow Matching for Equivariant Graph Generation](https://arxiv.org/abs/2608.26961)

**<font color=#1a73e8>作者：</font>** Moritz Piening, Christian Wald  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graphs are invariant under node permutations, motivating the use of permutation-equivariant architectures in generative models. In flow matching, however, symmetry may also enter the source--target coupling: once graph pairs are compared up to node relabeling, the natural Wasserstein geometry is that of the graph quotient space. The Euclidean quotient metric of this space coincides with the Gromov--Monge distance, obtained by optimally relabeling the nodes. We develop this perspective theoretically, showing that quotient couplings can be lifted to aligned representatives without additional cost and that symmetrization yields equivariant flow-matching minimizers, including for categorical endpoint prediction. In practice, exact Gromov--Monge alignment is intractable, so we construct minibatch couplings using efficient Gromov--Wasserstein-type relaxations and lower bounds for the inner node alignment, optionally combined with an outer assignment between graphs. The resulting procedure changes only the training coupling and is compatible with standard permutation-equivariant architectures. Across continuous graph and categorical molecular generation, these structure-aware couplings substantially improve sample quality at small integration budgets, while our scaled-up molecular models remain competitive under conventional many-step sampling.

---


### 129. [Packora: Systematic Design for Generative Molecular Crystal Structure Prediction](https://arxiv.org/abs/2608.26962)

**<font color=#1a73e8>作者：</font>** Nayoung Kim, Kiyoung Seong, Sungsoo Ahn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular crystal structure prediction (CSP) is important in pharmaceuticals, agrochemicals, and organic electronics, where subtle differences in molecular conformation and packing can strongly affect material properties. We present Packora, a flow-based generative model for molecular CSP that jointly predicts atomic coordinates and the lattice from molecular graphs. Packora supports multi-component and organometallic crystals and can condition on any subset of molecular conformers, stereochemical labels, and space-group information within a single model. Inspired by the CCDC CSP blind test, we evaluate generation and ranking separately, using generation to isolate generator quality and ranking to measure end-to-end performance under a common relaxation and ranking pipeline. We also systematically study architecture, training, conditioning, inference, and scaling, identifying an effective design based on cacheable pairwise reasoning, training objective and numerical solver choices, conditioning dropout, and balanced scaling of pairwise and single representations. Packora outperforms the baselines on both structure generation and ranking benchmarks, achieving the best matched-budget coverage across all six generation benchmarks, as well as higher experimental-form recovery, lower experimental-form ranks, and faster convergence in ranking.

---


### 130. [Adversarial Training Without Input Gradients via Low-Rank Householder Expansions](https://arxiv.org/abs/2608.26963)

**<font color=#1a73e8>作者：</font>** Tiana C. Johnson, Donsub Rim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work concerns adversarial training against the small-norm adversarial examples that arise from the inherent input instability of a trained deep neural network. Examples in this class are small as measured in the relative $\ell^2$-norm, and therefore lie in the neighborhood of the input on which the model acts approximately linearly, the regime in which the perturbation remains imperceptible. We first show that such examples can be computed directly from the trained network parameters, without input gradient iterations, by means of a linearization called the low-rank Householder expansion (LRHE). The expansion describes the composed affine map rather than any individual layer, and the directions it identifies are read from the activation pattern already available in the forward pass. We then propose a simple adversarial training scheme built on this construction. No differentiation with respect to the input is performed at any point: training requires only additional forward evaluations, with weight parameters updated by the standard backward pass, and the inner maximization of the usual min-max formulation is eliminated entirely. That such a regularizer exists is our main finding: the methods that dispense with the inner search all obtain their local geometry by differentiating with respect to the input, and we show this is not necessary. The regularizer costs the equivalent of $2.8$ PGD steps per epoch, an $8.7\times$ reduction relative to 40-step adversarial training on MNIST and below the cost of 3-step training. The resulting models match three-step PGD adversarial training for relative $\ell^2$ budgets $\varepsilon \le 0.02$ and 40-step training for $\varepsilon \le 0.012$, falling away beyond, consistent with the locality of the expansion.

---


### 131. [Graph-Based Pseudo-multimodal Contrastive Learning for 12-Lead ECG Representations](https://arxiv.org/abs/2608.26964)

**<font color=#1a73e8>作者：</font>** Mengyu Wang, Kozo Okada, Takafumi Goto 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> 12-lead electrocardiogram (ECG) is a standard, non-invasive examination widely used for diagnosing coronary artery disease, where clinical interpretation relies on comparing waveform patterns across multiple leads. However, most existing ECG analysis methods focus on single-lead signals or treat each lead independently, and typically process ECG signals as one-dimensional time-series data using CNNs or RNNs. While effective in modeling local waveform changes, such approaches have difficulty capturing inter-lead dependency and global waveform patterns essential for clinical diagnosis.
To address this limitation, we propose a graph-based pseudo-multimodal contrastive learning framework called Graph-CMMC. ECG waveforms are transformed into Gramian Angular Difference Field (GADF) images to construct complementary representations of the same cardiac activity, enabling a pseudo-multimodal learning setting. Using all 12 leads, Graph-CMMC aligns waveform and GADF representations in a self-supervised manner, while a graph-based relational module is employed to model inter-lead dependency and enforce structural consistency across leads during contrastive learning.
Experimental results on a multi-label coronary artery occlusion classification task demonstrate that the proposed framework achieves competitive performance compared to supervised learning methods. These results further suggest the effectiveness of using GADF as a complementary representation and incorporating explicit graph-based modeling of inter-lead dependency for learning robust 12-lead ECG representations.

---


### 132. [ClusterAttention: A training-free speedup of bidirectional attention](https://arxiv.org/abs/2608.26965)

**<font color=#1a73e8>作者：</font>** Kasper Nordenram, Amelie Dittmann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper introduces ClusterAttention, a general training-free speedup of bidirectional attention layers. Existing sparse attention methods either rely on structure in the input, such as order in language or spatial proximity in images, or use slow clustering processes amortized over several forward passes. ClusterAttention instead uses a fast recursive clustering method that adapts to the geometry of the keys and queries in each attention head to produce useful clusters. This method allows setting the size of the clusters arbitrarily. We utilize this by setting all clusters to be a fixed size that is a power of two, allowing the block-sparse attention to run at the same latency per query-key interaction as dense attention on GPUs. We also derive an expression for the output error in sparse attention, that explains the counterintuitive experimental finding that tight clusters can lead to larger errors than random clusters. We then derive the error when excluded clusters are compensated through their centroids, and show that this error shrinks with tighter clusters. We integrate this compensation into the method.
On large-scale tabular data ClusterAttention speeds up TabPFN-3 arXiv:2605.13986 by two to six times, while retaining at least 99% of the dense accuracy. To our knowledge, it is the first training-free method that can be successfully applied in the setting of unstructured input and a single forward pass. For video generation with Wan 2.1-14B T2V arXiv:2503.20314 , ClusterAttention achieves output closer to dense attention and a larger speedup (1.8x versus 1.4x) compared to SVOO arXiv:2603.18636 , a leading method developed specifically for this domain, both run without offline calibration.

---


### 133. [TEMPLAR Wales: A georeferenced environmental and toponymic dataset of Welsh settlements](https://arxiv.org/abs/2608.26970)

**<font color=#1a73e8>作者：</font>** Oktay Karakuş, Can Eyupoglu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Place names provide persistent records of how landscapes have been described and organised, but their quantitative reuse requires explicit separation between mapped places, lexical annotations and environmental measurements. TEMPLAR Wales is a georeferenced environmental-toponymy dataset comprising 3,757 settlement records across Wales. The resource links a reproducible settlement frame to deterministic lexical screening and settlement-level environmental attributes through stable identifiers. It contains 1,350 lexical detections across 1,294 settlements, generated from a frozen registry of 24 Welsh place-name elements, while retaining exact- and prefix-token matches and their provenance separately. Environmental attributes describe river and coastal proximity, elevation and local terrain context at multiple spatial scales, land cover and neighbourhood woody cover, with parallel terrain measurements derived from independent elevation products. The dataset is distributed as four relational tables accompanied by a field-level data dictionary, source-provenance register and licensing metadata. Technical validation confirms relational integrity, deterministic lexical reconstruction, documented environmental coverage, strong agreement between independent terrain sources and reproducible reconstruction of the frozen release. TEMPLAR Wales provides a reusable foundation for research in toponymy, linguistic geography, historical and environmental landscape studies, GIS and spatial data analysis without treating computational lexical detections as verified etymologies or contemporary environmental measurements as historical landscape reconstructions.

---


### 134. [TempJail: Temporal Jailbreak Attacks against Image-to-Video Generation Models](https://arxiv.org/abs/2608.26971)

**<font color=#1a73e8>作者：</font>** Qi Lu, Zehui Guo, David Yuanda Gan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In recent years, image-to-video (I2V) generation models have made remarkable progress in subject consistency and temporal coherence, enabling high quality video synthesis. However, these advances also introduce new safety risks. Existing studies mainly focus on jailbreak attacks involving single frame violations, while largely overlooking the temporal dimension unique to video generation models. In this paper, we investigate three attack scenarios and uncover a temporal vulnerability in I2V systems: unsafe semantics may emerge not from a single frame, but from semantic composition over time. We further identify two key challenges in such attacks: temporal abstraction and semantic camouflage. To address these issues, we propose TempJail, a novel temporal jailbreak framework for I2V systems. For temporal abstraction, we decompose a target malicious caption into an initial frame visual condition and a temporal text instruction. For semantic camouflage, on the image side we model semantic injection as controlled latent perturbation in diffusion sampling and introduce gradient guidance from pretrained encoders. On the text side, we rewrite the caption into an innocuous ``subject-action-scene'' template that bypasses safety filters while preserving temporal guidance. In the black-box inference phase, these two modalities jointly enable malicious semantics to be gradually triggered over time. Experiments on closed-source commercial models, including Kling, Seedance, Veo and PixVerse, show that TempJail improves attack success rate over prior state-of-the-art methods by 23.3\% under GPT-5.2 evaluation and 22.0\% under human evaluation. Our codes are available at \href{this https URL}{GitHub}.

---


### 135. [Squeezing More from Limited Data with Recursive Transformers](https://arxiv.org/abs/2608.26973)

**<font color=#1a73e8>作者：</font>** Serdar Gülbahar, Lukas Edman, Alexander Fraser  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pre-training under limited data requires a different view of scaling than web-scale language modeling. With a fixed data budget but relatively abundant compute, increasing parameter count helps only up to an optimal scale; beyond that point, models overfit and generalization worsens. We study this behavior across 10M-100M word pre-training budgets, two corpora, and multiple downstream evaluations, and find that optimal size depends strongly on both the data budget and the downstream target. We argue that standard Transformers scale down poorly to this setting, because embeddings consume a large fraction of the parameter budget and per-token computation is tied to representational capacity. To address this coupling, we study recursive Transformers, reusing a shared block across depth to scale compute, together with factorized embeddings to reduce vocabulary-map parameters. We train three recursive models and find that they outperform standard Transformers at 10M and 100M words, while remaining competitive with BabyLM Challenge 2025 winners.

---


### 136. [Terrain signatures in Welsh settlement names](https://arxiv.org/abs/2608.26978)

**<font color=#1a73e8>作者：</font>** Oktay Karakuş, Can Eyupoglu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Landscapes are named, but whether names retain measurable environmental information beyond broad geographic structure is rarely tested. We analysed 3,757 Welsh settlements using a frozen, source-audited 24-element lexical framework, preregistered outcome-specific models and geographically structured validation. The central comparison contrasted 101 settlements carrying high-terrain elements (\textit{bryn} or \textit{mynydd}) with 139 carrying low-terrain elements (\textit{cwm} or \textit{pant}). High-terrain names occupied locations 24.4 m higher relative to their 2-km surroundings (95\% CI, 10.8--38.1 m; Holm-adjusted $p$ = 0.00137). The association remained positive across prespecified 1-, 2- and 5-km neighbourhood definitions and was reproduced using an independently produced elevation source (24.1 m; 95\% CI, 10.6--37.6 m). Adding terrain-name polarity to a non-lexical spatial and settlement baseline reduced geographically held-out mean squared error by 4.63\%, 6.22\% and 7.30\% under 10-, 25- and 50-km spatial blocking, respectively, although improvement varied among held-out regions. River-related names provided weaker, directionally consistent evidence, while the preregistered woodland model was non-estimable. Residual spatial structure, unresolved name language and the absence of independent external replication limit interpretation. Selected Welsh settlement-name categories therefore retain measurable information about present-day terrain within Wales, without establishing individual etymology, causal naming, historical environmental memory or transferability to other naming systems.

---


### 137. [Exploring Normativity in Stable Diffusion: Insights for XAI in the Arts](https://arxiv.org/abs/2608.26980)

**<font color=#1a73e8>作者：</font>** Michelle Dutoit, Baptiste Caramiaux  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative text-to-image (T2I) systems are increasingly adopted in creative practice, yet their normative behaviors remain underexplored from the perspective of creative practitioners. In this workshop paper, we present a within-subject study with 14 creative practitioners using Stable Diffusion to create illustration from two tasks of differing specificity. We investigate whether and how practitioners perceive normative behavior in a T2I system and how it impacts their creative process depending on task specificity. Our findings show that participants perceived normative behavior through invariant patterns, stereotypical output, and unsolicited omission or addition of details. These experiences led to feelings of disempowerment and creative compromise. We discuss implications for XAIxArts, including prompt transparency and artist empowerment in creative contexts.

---


### 138. [Decentralized Multitask Learning over Learned Task Graphs](https://arxiv.org/abs/2608.26989)

**<font color=#1a73e8>作者：</font>** Zirui Wan, Stefan Vlaski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper investigates decentralized multitask learning over networks when the underlying task relationships are unknown. While existing graph-regularized multitask frameworks typically assume a known structure, practical settings often require learning inter-task dependencies directly from distributed data. We propose a decentralized two-phase strategy that first estimates a generalized graph Laplacian from noisy non-cooperative stochastic gradient iterates, and subsequently exploits the learned graph to enable cooperative multitask diffusion learning. This framework is motivated by a Gaussian Markov random field prior, which gives rise to a decentralized maximum likelihood estimator for the graph Laplacian. The analysis quantifies the Laplacian estimation error and its propagation to the steady-state performance of the multitask diffusion recursion, and introduces a topology sensitivity index to capture the effect of network heterogeneity. Simulation results corroborate the theoretical findings and demonstrate that cooperation enabled by the learned task graph significantly improves performance over non-cooperative learning, while approaching the true-graph baseline when the estimation stepsize is sufficiently small.

---


### 139. [Benchmarking_Fast_Domain_Adaptation_for_Unsupervised_Speech_Units](https://arxiv.org/abs/2608.26992)

**<font color=#1a73e8>作者：</font>** Robin San Roman, Manel Khentout, Tu Anh Nguyen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Representation learning has attracted great atten- tion and managed to reach good performances as a pretraining method for downstream tasks or as a first step towards unsu- pervised speech modeling. Yet, little is known about how such methods deal with out-of-domain speech and how could they be adapted in a few shot to new domains. This is important especially for accented speech where one observes a long tail of accents that diverge from the standard ones. We introduce ABX- Accent, a benchmark based on the AESRC dataset that features 10 different accents of English. It includes a small (< 10 hours) unlabelled training set in each of the accents and adaptations of the Zero Resources Challenge ABX evaluation metrics to each of the accents. We illustrate this benchmark with a baseline model that uses adaptive domain normalization to fine tune a pretrained Contrastive Predictive Coding model on the accents. This method is first developed on LibriSpeech using a male/female split. When applied to the new benchmark, the proposed method yields a relative improvement of 23.6% on across-speaker ABX scores on average compared to non adapted models. The data and metrics will be open sourced upon paper acceptance

---


### 140. [Virtual iEEG from Scalp EEG: Charting the Landscape of Source Imaging, Intracranial Inference and Reconstruction](https://arxiv.org/abs/2608.26998)

**<font color=#1a73e8>作者：</font>** Dongyi He, Xiangkai Wang, Hongjie Yan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Intracranial electroencephalography (iEEG) provides temporally precise and spatially specific access to neural activity from focal and deep brain regions, but its invasiveness and restricted anatomical coverage limit routine use. These constraints have motivated scalp-to-intracranial inference, termed virtual iEEG when model outputs carry iEEG-defined event, feature, representation, or contact-level waveform semantics. This review presents a target-centred framework distinguishing event inference, feature translation, and waveform reconstruction, while separating predictability from observability, identifiability, fidelity, and utility. Evidence is evaluated according to cohort independence, anatomical and spectral coverage, train--test separation, and target-patient adaptation. Current studies support inference of selected intracranial events, low-frequency components, and task-related representations, but not unique recovery of arbitrary contact-level activity. Stronger validation requires appropriate controls, source-imaging baselines, uncertainty assessment, and incremental-utility testing. Future progress depends on independent paired datasets and prospective evidence that virtual iEEG adds value beyond scalp EEG and EEG source imaging.

---


### 141. [Metamorphism: A mathematical challenge for antivirus technology](https://arxiv.org/abs/2608.27007)

**<font color=#1a73e8>作者：</font>** Luis M. Augusto  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Metamorphic viruses, currently the most advanced computer viruses in the wild, have the unique ability of mutating their own code virtually into infinitely many highly dissimilar copies of themselves that nevertheless have the same functionality. This ability -- metamorphism -- together with other advanced ob- fuscation techniques makes these computer viruses virtually undetectable by the antivirus software available in the market today. In this paper, we show that viral metamorphism is fully attainable by the employment of van Wijngaarden grammars. The challenge then for an antivirus software is to embed the Turing machine that decides the language generated by the grammar.

---


### 142. [A Multi-Modal AI Framework for Real-Time Queue Prediction, Management and Optimisation in Intelligent Border Control Systems](https://arxiv.org/abs/2608.27010)

**<font color=#1a73e8>作者：</font>** Varvara Mama, Eleni Veroni, Nikolaos Kapsalis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In the present work an efficient border control management procedure is proposed. Compared to operational queue management systems, whose operations are based on mostly static data, the proposed work takes into account dynamic traffic conditions, thus enabling optimal performance, even in cases of uncertainty. To this end, we are proposing a multi-modal Artificial Intelligence (AI) framework, tailored to th needs of border control systems, which enables real-time queue prediction, management, and resource optimization. The novel proposed approach integrates heterogeneous data sources and presents them through a unified representation by employing Long Short-Term Memory (LSTM) networks for queue forecasting. Furthermore, it leverages Model Predictive Control (MPC) and scheduling optimization to derive actionable control policies, which in turn can be presented to border control officers. The proposed work has been evaluated using synthetic data simulating realistic traffic. The evaluation results demonstrate that the proposed method reduces queue prediction error by up to 35% and average waiting time by 30%. Accordingly, the average throughput increases by nearly 20%, compared to ARIMA and rule-based methods. The abovementioned results show the effectiveness and efficiency of combining AI architectures with optimization techniques for proactive and adaptive border traffic management.

---


### 143. [ITL: Interpretable Document Alignment with Structured Reference Frameworks](https://arxiv.org/abs/2608.27031)

**<font color=#1a73e8>作者：</font>** Raúl Giráldez, Dayrelis Mena, Jesús S. Aguilar--Ruiz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Measuring alignment between documents and structured reference frameworks requires identifying conceptual evidence distributed throughout the text and reporting it through measures that are quantitative, interpretable, and traceable. Many commonly used retrieval and classification approaches return either pairwise similarity scores or one or more class labels, whereas fewer methods provide concept-level scores that are directly traceable to the terminological evidence supporting them. We present \emph{Intelligent Target Locator} (ITL), a domain-agnostic and language-portable methodology that estimates the affinity between the textual units of a target document and the concepts defined in a \emph{Structured Reference Document} ($SRD$). From the $SRD$, ITL induces concept-specific terminological profiles built from independent terms, bigrams, trigrams, and co-occurrences. Each term is assigned an importance weight that combines concept membership, term-type specificity and inter-concept discriminability. The output is a textual-unit--concept affinity matrix that can be aggregated at different levels of granularity. We conduct an internal consistency assessment using the 17 Sustainable Development Goals (SDGs), evaluating each official goal statement against the $SRD$ induced from the same set of descriptors. Every statement reached its highest affinity with the corresponding concept, and the mean affinity across the remaining concepts stayed marginal relative to the mean reference affinity. This separation indicates that ITL distinguishes the conceptual profiles of the framework. ITL thus offers a general basis for quantifying document alignment with structured frameworks while keeping each result traceable to the terminological evidence that supports it.

---


### 144. [Differentiable Jitter Correction using Deep Learning-based Image Quality Metric for Phase-Contrast Micro-CT](https://arxiv.org/abs/2608.27034)

**<font color=#1a73e8>作者：</font>** Junan Chen, Yiting Jia, Joscha Maier 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper proposes a fully differentiable jitter correction method for X-ray phase-contrast micro computed tomography using a deep learning-based image quality metric that estimates and compensates per-projection rigid jitter directly from the acquired projection data, without a pre-scan motion-free reference. The approach builds on a gradient-based auto-focus strategy adapted to parallel-beam geometry. A set of candidate objective functions is benchmarked in a controlled study, and the sensitivity of the visual information fidelity (VIF) metric to the jitter artifact is verified with the target phase-contrast data. To operate without a clean reference, a compact 3D convolutional neural network is trained to predict the VIF score from a single corrupted volume. A spatially selective total variation penalty applied exclusively to the image background is introduced to penalize spurious high-frequency structures that otherwise emerge during optimization. Experiments on biological specimens acquired at different synchrotron beamlines are conducted. Evaluation uses jitter motion applied to simulated and experimentally acquired projection data. The result confirms that the integrated pipeline reliably recovers fine structural detail lost due to jitter, with generalization demonstrated across morphologically distinct samples.

---


### 145. [Representing and Parsing Korean Constituency Structure at Different Levels of Granularity](https://arxiv.org/abs/2608.27035)

**<font color=#1a73e8>作者：</font>** Jungyeul Park, KyungTae Lim, Zihao Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Korean constituency parsing raises a representational challenge because the terminal units of a phrase-structure tree do not straightforwardly correspond to simple surface words. Korean eojeols are morphologically complex spacing units, and existing constituency resources differ in how they represent eojeol-internal morphology and non-overt elements. This paper compares three constituency parsing representations derived from the Penn Korean Treebank: Morpheme+XPOS, Eojeol+XPOS, and Eojeol+UPOS. We construct these representations by removing null elements, aligning Penn Korean phrase structure with overt eojeol tokens, preserving Penn Korean phrase labels where possible, and varying the terminal and preterminal layers. We then evaluate canonical non-binary transition-based constituency parsers in top-down, in-order, and bottom-up orders under a shared modeling and evaluation setup. All experiments use gold terminal segmentation and gold preterminal labels and therefore evaluate constituency parsing conditioned on gold morphosyntactic annotation. Eojeol terminals yield shorter transition sequences, but Eojeol+UPOS parsing substantially underperforms the morphologically richer conditions. Eojeol+XPOS narrows this gap, while Morpheme+XPOS gives the strongest results even after its predictions are projected to the eojeol terminal domain. Under these gold-annotation conditions, the results show that fine-grained morphological and XPOS representations provide valuable evidence for the evaluated parsers. This empirical finding concerns the information available for parsing and does not by itself determine the linguistically preferable terminal domain. Independently, linguistic and resource-design considerations motivate eojeol as a stable and interpretable surface domain for phrase-structure annotation, with morpheme-level and XPOS information retained as aligned morphosyntactic evidence.

---


### 146. [Neighborhood Watch: Privacy Risks in Seeded Local Combination Synthetic Data](https://arxiv.org/abs/2608.27037)

**<font color=#1a73e8>作者：</font>** Hadrien Lautraite, Tristan Allard, Anne-Sophie Charest 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Synthetic data is seen as a promising solution for sharing data in sensitive contexts. However, recent work on privacy attacks have shown that there are still significant residual risks, especially for synthetic data generations methods that are not based on formal approaches such as differential privacy. In this paper, we investigate the privacy risks associated with local combination approaches for generating synthetic data in which synthetic profiles are built by combining real neighbouring profiles. More precisely, we focus on three methods from this family, namely SMOTE, Simulant and Avatar, which have been recently used as a way to share 'anonymised data' in the healthcare domain. In particular, we conduct an extensive privacy analysis through a diverse set of attacks: membership inference, linkage and reconstruction attacks. Our results demonstrate substantial privacy leakage for all three methods, raising serious doubts about whether their outputs should be regarded as anonymous in practice.

---


### 147. [Multi-Person Human Motion Forecasting in Complex Scenes](https://arxiv.org/abs/2608.27039)

**<font color=#1a73e8>作者：</font>** Serdar Ozsoy, Lars Doorenbos, Juergen Gall  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurately forecasting the movement of people in complex scenes requires reasoning over the past and present state of the entire environment. In this context, effectively incorporating object information and social interactions into a unified framework remains particularly challenging. To address this, we propose Object-Conditioned Social Diffusion (OCSD), a conditional diffusion model that integrates motion history, multi-person interactions, and object cues into a single framework. OCSD uses an object-conditioning mechanism that modulates denoising at every timestep, enabling fine-grained human-object reasoning, and a social encoder that models the interactions between all humans in the scene. As a result, our model naturally handles varying group sizes, complex social interactions, and supports sampling multiple plausible futures. Extensive experiments show that OCSD achieves state-of-the-art results on the Humans in Kitchens (HiK) and HOI-M3 benchmarks. It reduces the two-second path error by 121.5 mm (31.3%) on HiK and 130.5 mm (33.2%) on HOI-M3 compared to prior work, and produces more realistic long-term forecasts.

---


### 148. [Cyber-Electromagnetic Anomaly Detection Through Time-Series Analysis](https://arxiv.org/abs/2608.27043)

**<font color=#1a73e8>作者：</font>** María Teresa Guillén Navarro, Juan Luis Serradilla Tormos, Sergio López Bernal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Military operations benefit from the coordination between kinetic and non-kinetic domains. In particular, the coordination of cyber operations and electromagnetic warfare has become increasingly relevant for gaining operational advantage. This coordination is also relevant for Cyber Situational Awareness (CSA), where the Observe-Orient-Decide-Act (OODA) loop requires monitoring and interpreting evidence from heterogeneous sources. In this context, anomalies may appear not only in the physical behavior of signals, but also in the communication behavior observed at the traffic level. However, many existing anomaly detection proposals focus on only one of these perspectives, limiting their ability to characterize events that manifest simultaneously in the electromagnetic spectrum and cyberspace. To address this limitation, this work develops and evaluates two anomaly detection models that combine features from both domains. More specifically, the study uses the ZBDS2023 dataset, which contains traffic from nodes in a mesh network, including benign and attack behaviors. Thus, this dataset provides physical-level features, traffic-level features, and labeled attacks. Two detection approaches are evaluated: a supervised model based on Random Forest and an unsupervised model using LSTM-Autoencoder. The results show that learning-based models can detect patterns combining both levels, especially under a supervised approach, achieving an F1-score of 89.76% with Random Forest and 64.09% with LSTM-Autoencoder. Although these results indicate that the proposed models can support CSA by improving the observation and interpretation of anomalous behavior, the subtle differences between normal and attack samples highlight the need for richer discriminative features.

---


### 149. [Soft Active Electromyography Interface for Machine Learning-Enabled Silent Speech Recognition](https://arxiv.org/abs/2608.27048)

**<font color=#1a73e8>作者：</font>** Yuta Kurotaki, Shusuke Yamakoshi, Reitaro Yoshida 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Silent speech recognition (SSR) provides an alternative communication pathway in the absence of audible speech. However, conventional approaches are limited by the need for constant facial attachment, privacy concerns, and unstable signal acquisition. Here, we propose a soft, active electromyography (EMG) interface that enables word-level SSR using machine learning. Worn on the hand, the device uses a fingertip electrode that can be positioned near the lips to acquire EMG signals only when needed. The interface integrates liquid metal (LM) interconnects, transparent flexible printed circuit (FPC) electrodes, and elastomer encapsulation to ensure high mechanical stability during finger motion. A deep neural network trained on these stable signals achieved a mean accuracy of 97.2 $\pm$ 1.3% across three subjects in classifying a 30-word vocabulary, demonstrating robust linguistic discrimination. Furthermore, real-time drone control validates the practicality of this approach in noisy and privacy-sensitive environments where conventional voice recognition fails. This study highlights the potential of soft, wearable EMG systems as secure and intuitive human-machine interfaces.

---


### 150. [Beyond Classification: Task-Dependent Learnability under Privacy-Motivated Image Transformations](https://arxiv.org/abs/2608.27066)

**<font color=#1a73e8>作者：</font>** Leon Ranke, Wolfgang Hübner, Ronny Hug 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Privacy-Enhancing Technologies (PETs) in computer vision often rely on noise or image perturbations to protect visual data while securely processing it, creating a trade-off between task performance and protection. This trade-off is commonly evaluated using image classification, which primarily captures semantic separability and remains robust despite significant geometric, spatial layout or local boundary alterations. As a result, it is too simplistic as a proxy for generic vision tasks. Exhaustive downstream-task evaluation, however, is computationally expensive because models must often be trained for each PET transformation and parameter setting. We therefore propose a compute-aware multi-task protocol for evaluating PETs in model training. It combines lightweight proxy tasks that target complementary aspects of visual structure while remaining simple and fast to compute. Across irreversible privacy transformations, key-based block primitives, and learnable image encryption schemes, we demonstrate that PETs with similar classification accuracy can differ substantially on other tasks. The outcomes highlight the need for PET evaluation protocols that move beyond classification-only reporting.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-202](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
