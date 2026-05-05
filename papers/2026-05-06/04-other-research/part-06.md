# 📦 其他研究 | 2026年05月06日

> 本类共 **511** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-511](./part-11.md)

---

### 251. [Adversarial Imitation Learning with General Function Approximation: Theoretical Analysis and Practical Algorithms](https://arxiv.org/abs/2605.01778)

**<font color=#1a73e8>作者：</font>** Tian Xu, Zhilong Zhang, Zexuan Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial imitation learning (AIL), a prominent approach in imitation learning, has achieved significant practical success powered by neural network approximation. However, existing theoretical analyses of AIL are primarily confined to simplified settings, such as tabular and linear function approximation, and involve complex algorithmic designs that impede practical implementation. This creates a substantial gap between theory and practice. This paper bridges this gap by exploring the theoretical underpinnings of online AIL with general function approximation. We introduce a novel framework called optimization-based AIL (OPT-AIL), which performs online optimization for reward learning coupled with optimism-regularized optimization for policy learning. Within this framework, we develop two concrete methods: model-free OPT-AIL and model-based OPT-AIL. Our theoretical analysis demonstrates that both variants achieve polynomial expert sample complexity and interaction complexity for learning near-expert policies. To the best of our knowledge, they represent the first provably efficient AIL methods under general function approximation. From a practical standpoint, OPT-AIL requires only the approximate optimization of two objectives, thereby facilitating practical implementation. Empirical studies demonstrate that OPT-AIL outperforms previous state-of-the-art deep AIL methods across several challenging tasks.

---


### 252. [Runtime Evaluation of Procedural Content Generation in an Endless Runner Game Using Autonomous Agents](https://arxiv.org/abs/2605.01783)

**<font color=#1a73e8>作者：</font>** Rishabh Kar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Procedural Content Generation (PCG) enables game content to be created algorithmically without direct manual level-design effort, but it introduces a serious evaluation problem: generated content may become unbalanced, blocked, repetitive, or technically unsolvable. This paper presents Momentum, an endless-runner game that integrates runtime terrain generation, environment object spawning, and autonomous agent-based evaluation into a single gameplay loop. Ground tiles and environmental objects are generated dynamically as the player advances, object placement follows a constraint-driven mechanism inspired by Wave Function Collapse (WFC), and the runtime navigation surface is rebuilt asynchronously to remain consistent with the streamed environment. Two autonomous evaluation agents move ahead of the player and inspect the generated path: an aerial scanner that examines the corridor geometrically, and a ground-traversal agent that validates the same region from a navigational perspective. The evaluation pipeline combines ray casting, volumetric physics sweeps, obstacle-layer filtering, and structured crash reporting to identify problematic generated scenarios before they reach the player. The work demonstrates how generation and validation can be unified within the same runtime loop, rather than treating evaluation as a separate offline pass. Around this implementation, the paper formulates a measurable evaluation framework along the canonical PCG axes of playability, diversity, controllability, and runtime performance, derives a structural saturation bound on the spawner from its own placement constraints, and quantifies the per-segment scanning cost of the agents from first principles.

---


### 253. [DataEvolver: Let Your Data Build and Improve Itself via Goal-Driven Loop Agents](https://arxiv.org/abs/2605.01789)

**<font color=#1a73e8>作者：</font>** Qisong Zhang, Wenzhuo Wu, Zhuangzhuang Jia 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Constructing controllable visual data is a major bottleneck for image editing and multimodal understanding. Useful supervision is rarely produced by a single rendering pass; instead it emerges through iterative generation, inspection, correction, filtering, and export. We present DataEvolver, a closed-loop visual data engine that organizes this process around explicit goals, persistent artifacts, bounded corrective actions, and acceptance decisions. DataEvolver supports multiple artifact types, including RGB images, masks, depth maps, normal maps, meshes, poses, trajectories, and review traces. In the current release, the system operates through two coupled loops: generation-time self-correction within each sample and validation-time self-expansion across dataset rounds. We validate the framework on an image-level object-rotation setting. With a fixed Qwen-Edit LoRA probe, our final Ours+DualGate model outperforms both the unadapted base model and a public multi-angle LoRA on SpatialEdit and a held-out evaluation set. Ablations show a consistent improvement path from scene-aware generation to feedback-driven correction and dual-gated validation. Beyond the released rotation data, our main contribution is a reusable framework for building visual datasets through explicit goal tracking, review, correction, and acceptance loops.

---


### 254. [Beyond ECE: Calibrated Size Ratio, Risk Assessment, and Confidence-Weighted Metrics](https://arxiv.org/abs/2605.01796)

**<font color=#1a73e8>作者：</font>** Fernando Martin-Maroto, Nabil Abderrahaman, Gonzalo G. de Polavieja  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Confidence calibration has been dominated by the Expected Calibration Error (ECE), a linear metric that counts calibration offset equally regardless of the confidence level at which it occurs. We show that ECE can remain small even under arbitrarily large overconfidence risk, so we propose Calibrated Size Ratio (CSR) instead, an interpretable metric that equals 1 under perfect calibration, from which we derive the risk probability $P_{\mathrm{risk}}$ that quantifies the statistical evidence for overconfidence. We further argue that overconfidence risk assessment must be complemented by a measure of discriminative value: whether the assigned confidences actively distinguish correct from incorrect predictions. We show that confidence-weighted accuracy $\mathrm{cwA}$ is the natural such complement, and that confidence-weighting extends to all standard classification metrics. In particular, we prove that the confidence-weighted AUC (cwAUC) captures the information about calibration while the classical AUC cannot. We validate the proposed indicators on several synthetic confidence distributions under multiple controlled calibration profiles and on fifteen real datasets with and without post-hoc calibration. Experiments demonstrate that CSR achieves near-perfect sensitivity and specificity across all tested conditions.

---


### 255. [Neural Decision-Propagation for Answer Set Programming](https://arxiv.org/abs/2605.01797)

**<font color=#1a73e8>作者：</font>** Thomas Eiter, Katsumi Inoue, Sota Moriyama  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Integration of Answer Set Programming (ASP) with neural networks has emerged as a promising tool in Neuro-symbolic AI. While existing approaches extend the capabilities of ASP to real world domains, their reasoning pipelines depend on classical solvers, which is a bottleneck for scalability. To tackle this problem, we propose a new method to compute stable models, called decision-propagation (DProp), which alternates falsity decisions and truth propagations. Successful DProp computations are shown to capture the stable model semantics. We then develop Neural DProp (NDProp), a differentiable extension of DProp with neural computation for decisions and fuzzy evaluation for propagations. We evaluate the capabilities of NDProp for learning decision heuristics as well as neuro-symbolic integration, and compare it with existing neuro-symbolic approaches. The results show that NDProp can learn to efficiently compute stable models, and it improves accuracy and scalability on neuro-symbolic benchmarks.

---


### 256. [Koopman Representations for Early Outbreak Warning and Minimal Counterfactual Intervention in Multi-Agent Epidemic Simulations](https://arxiv.org/abs/2605.01803)

**<font color=#1a73e8>作者：</font>** Florin Leon  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> This paper presents a Koopman-based framework for early outbreak detection and intervention selection in a multi-agent epidemic simulation. Agents exhibit mobility patterns, heterogeneous susceptibility, immunity-dependent viral load progression, and local transmission through co-location. The goal of the simulation is to study near-critical epidemic regimes in which small changes in exposure or timing can alter the final outcome. Aggregate daily observables from early trajectory windows are encoded into a low-dimensional Koopman latent space whose approximately linear evolution supports short-horizon forecasting and outbreak risk estimation. These representations are combined with a random forest classifier trained to predict whether the final attack rate exceeds a major outbreak threshold. Experiments near the system tipping points show strong early warning performance, with Koopman-derived features contributing to class separation. Counterfactual analysis further shows that minimal interventions, such as keeping a single selected agent at home for one day, can reduce attack rates and, often, shift the trajectory below the outbreak threshold.

---


### 257. [MAGIC: Multi-Step Advantage-Gated Causal Influence for Multi-agent Reinforcement Learning](https://arxiv.org/abs/2605.01805)

**<font color=#1a73e8>作者：</font>** Haohan Yu, Jinmiao Cong, Shengzhi Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> A key challenge in multi-agent reinforcement learning (MARL) lies in designing learning signals that effectively promote coordination among agents. Designing such signals necessitates the ability to quantify the true, long-term causal influence between agents. To address this, we introduce Multi-step Advantage-Gated Interventional Causal MARL (MAGIC), a framework that extracts multi-step causal influences between agents and selectively converts them into intrinsic rewards. MAGIC uses causal intervention with conditional mutual information to quantify long-horizon agent influence, and introduces an advantage-based gating mechanism to ensure exploration is directed toward beneficial, goal-aligned behaviors. Experiments across multiple standard MARL benchmarks and task families, including MPE and SMAC/SMACv2, demonstrate that MAGIC outperforms state-of-the-art methods by a significant margin, achieving an improvement of at least 10.1% in the main evaluation metric.

---


### 258. [Federated Semi-Supervised Graph Neural Networks with Prototype-Guided Pseudo-Labeling for Privacy-Preserving Gestational Diabetes Mellitus Prediction](https://arxiv.org/abs/2605.01810)

**<font color=#1a73e8>作者：</font>** G. Victor Daniela, A. Mallikarjuna Reddya, Uday Kumar Addankia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gestational Diabetes Mellitus (GDM) is a high-prevalence pregnancy complication that requires accurate early risk stratification to reduce maternal and fetal morbidity. However, real-world clinical deployment of machine learning is hindered by two coupled constraints: (i) label scarcity, where a large fraction of electronic health records (EHR) lack confirmed diagnostic labels, and (ii) data privacy, which prevents sharing patient-level data across hospitals. This paper proposes FedTGNN-SS, a privacy-preserving federated semi-supervised framework for clinical tabular EHR. Each hospital builds a local k-nearest-neighbor patient similarity graph and trains a topology-adaptive GNN encoder. To robustly exploit unlabeled records, FedTGNN-SS combines (1) prototype-guided pseudo-labeling with neighborhood agreement, (2) adaptive graph refinement that periodically updates the k-NN graph using learned embeddings, (3) clinical-aware consistency augmentation applied only to continuous variables, and (4) privacy-safe prototype sharing that exchanges only class-level centroids. Across three diabetes-related datasets (GDM: N = 3,525; Pima: N = 768; Early Stage: N = 520) under 10\%-80\% missing labels per silo, FedTGNN-SS achieves 56 significant wins ($p < 0.05$) against 11 federated baselines and attains strong AUROC under extreme scarcity (Pima: 0.8037 at 80\% missing, Early Stage: 0.9634 at 80\% missing).

---


### 259. [Cross-Domain Adversarial Augmentation: Stabilizing GANs for Medical and Handwriting Data Scarcity](https://arxiv.org/abs/2605.01815)

**<font color=#1a73e8>作者：</font>** Md. Sohanuzzaman Soad, Mahady Al Hady, S M Rafiuddin Rifat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative Adversarial Networks (GANs) offer a pragmatic route to mitigate data scarcity in vision tasks. We study generative augmentation across two low-resource domains: Bangla handwritten characters and chest X-ray imaging using DCGAN-style models trained at 64x64 resolution. We evaluate fidelity and diversity via Inception Score (IS), Fr'echet Inception Distance (FID), and embedding visualizations (t-SNE/UMAP), and assess downstream utility by training classifiers on real versus real synthetic data. Our experiments show that generative augmentation improves sample diversity and yields consistent gains in classifier performance under limited-data regimes. We analyze stability enhancements (e.g., gradient-penalized objectives and spectral normalization) and report ablations on synthetic-to-real ratios and sample filtering. We discuss evaluation caveats for medical images, dataset licensing, and privacy risks associated with synthetic data. The resulting protocol is simple to reproduce and provides a strong baseline for applying generative augmentation to resource-constrained imaging tasks.

---


### 260. [Skipping the Zeros in Diffusion Models for Sparse Data Generation](https://arxiv.org/abs/2605.01817)

**<font color=#1a73e8>作者：</font>** Phil Sidney Ostheimer, Mayank Nagda, Andriy Balinskyy 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models (DMs) excel on dense continuous data, but are not designed for sparse continuous data. They do not model exact zeros that represent the deliberate absence of a signal. As a result, they erase sparsity patterns and perform unnecessary computation on mostly zero entries. With Sparsity-Exploiting Diffusion (SED), we model only non-zero values, preserving sparsity. SED delivers computational savings while maintaining or improving generation quality by skipping zeros during training and inference. Across physics and biology benchmarks, SED matches or surpasses conventional DMs and domain-specific baselines, while vision experiments provide intuitive insights into the limitations of dense DMs and the benefits of SED.

---


### 261. [Hybrid Visual Telemetry for Bandwidth-Constrained Robotic Vision: A Pilot Study with HEVC Base Video and JPEG ROI Stills](https://arxiv.org/abs/2605.01826)

**<font color=#1a73e8>作者：</font>** Natalia Trukhina, Vadim Vashkelis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bandwidth-constrained robotic and surveillance systems often rely on a single compressed video stream to support both continuous scene awareness and downstream machine perception. In practice, this creates a mismatch: low-bitrate video can preserve motion and coarse context, but often loses the fine local detail needed for reliable object recognition and decision-making. Motivated by a hybrid architecture in which low-resolution video supports dynamic scene understanding while eventdriven high-detail regions of interest (ROIs) support close-up identification and analytics, this paper formalizes a two-channel visual telemetry scheme in which a continuous low-bitrate video stream is augmented by selectively transmitted high-detail still ROIs. This first paper does not attempt to prove the superiority of a new still-image codec. Instead, it establishes the hybrid transmission paradigm itself using a practical and reproducible codec stack: x265/HEVC for the base video stream and JPEG stills for ROI refinement. We formulate the problem as bitrate-constrained information selection for robotic vision and define an experimental protocol in which video-only and hybrid schemes are compared under matched total communication budgets. The study is designed around UAV-oriented datasets, two practical bitrate regimes, several ROI triggering policies, and object-level classification refinement on selectively transmitted ROI stills. The resulting paper lays the methodological foundation for a second-stage investigation of JPEG AI as the semantic still-image channel within the same hybrid architecture.

---


### 262. [RMGAP: Benchmarking the Generalization of Reward Models across Diverse Preferences](https://arxiv.org/abs/2605.01831)

**<font color=#1a73e8>作者：</font>** Yangyang Zhou, Yi-Chen Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning from Human Feedback has become the standard paradigm for language model alignment, where reward models directly determine alignment effectiveness. In this work, we focus on how to evaluate the generalizability of reward models. By "generalizability", we mean the ability of RMs to correctly rank responses to align with diverse user preferences. However, existing reward model benchmarks are typically designed around a universal preference, failing to assess this generalization. To address this critical gap, we introduce RMGAP, a benchmark comprising 1,097 instances across Chat, Writing, Reasoning, and Safety domains. Since different users exhibit diverse preferences for the same task, we first generate four distinct responses with different linguistic profiles for each collected prompt. However, the original prompt set lacks the specificity to convey different preferences. We therefore construct tailored prompts by contrasting these candidates and designing scenarios in which one response becomes the uniquely appropriate choice. Moreover, we observe that users often express the same preference using different phrasings, and thus extend each prompt with two paraphrased variants. Our evaluation of 24 state-of-the-art RMs reveals their substantial limitations: even the best RM achieves only 49.27% Best-of-N accuracy, highlighting considerable room for improvement in reward model generalization. Related data and code are available at this https URL.

---


### 263. [Repurposing and Evaluating the (In)Feasibility of Dataset Poisoning enabled Watermarking for Contrastive Learning](https://arxiv.org/abs/2605.01834)

**<font color=#1a73e8>作者：</font>** Zhiyang Dai, Yansong Gao, Boyu Kuang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Contrastive learning (CL) reduces annotation cost via auto-derived supervisory signals. Since large-scale in-house CL datasets are infeasible, reliance on third-party or internet data is common. Recent studies show CL models are vulnerable to data-poisoning backdoor attacks, but their generalization and robustness are underexplored. We systematically evaluate existing data-poisoning backdoor attacks on CL, revealing limitations: poor dataset adaptability, low success rates, limited portability, and restrictive assumptions (e.g., downstream task knowledge). Interestingly, trigger samples exhibit distinguishable statistical divergence from clean samples, which inspires repurposing it as a watermark for dataset IP protection. Direct repurposing is challenging due to low success rates; we overcome this by statistical verification using a unified density metric. We further propose a multi-level watermarking scheme adapting to feature-level, soft-label, or hard-label outputs in CL. Experiments show some backdoor attacks can be repurposed as effective watermarks with trade-offs among fidelity, verifiability, and robustness. This work demonstrates weak backdoor effects become reliable signals for dataset IP protection in challenging CL settings.

---


### 264. [Learning Koopman operators for coupled systems via information on governing equations of subsystems](https://arxiv.org/abs/2605.01835)

**<font color=#1a73e8>作者：</font>** Tatsuya Naoi, Jun Ohkubo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nonlinear coupled systems are ubiquitous in science and engineering. The analysis and modeling of such systems is challenging due to their high dimensionality and complex interactions among subsystems. In recent years, operator-theoretic methods based on the Koopman operator have attracted attention as a powerful tool for analyzing and modeling nonlinear dynamical systems. Extended dynamic mode decomposition (EDMD) is one of the most popular methods to approximate the Koopman operator. However, EDMD is a purely data-driven method, and it could be unstable and inaccurate for coupled systems under limited data availability. In this paper, we propose a method to learn the Koopman operator for coupled systems using the differential equations governing each subsystem. We also demonstrate its effectiveness through numerical experiments on coupled oscillator systems.

---


### 265. [Disentangled Anatomy-Disease Diffusion (DADD) for Controllable Ulcerative Colitis Progression Synthesis](https://arxiv.org/abs/2605.01848)

**<font color=#1a73e8>作者：</font>** Umut Dundar, Alptekin Temizel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthesizing longitudinal medical images at controllable disease stages while preserving patient-specific anatomy is hindered by the entanglement of pathological textures and structural features. We address this challenge for ulcerative colitis (UC) endoscopy, where severity follows a continuous ordinal progression along the Mayo Endoscopic Score (MES). Our framework, Disentangled Anatomy-Disease Diffusion (DADD), conditions a latent diffusion model on two complementary embeddings: a pretrained image encoder for patient anatomy and a separately trained ordinal embedder for cumulative disease severity. Since image embeddings inevitably capture disease information, we introduce a Feature Purifier, a cross-attention-based erasure mechanism that identifies and suppresses disease-correlated channels, yielding purified anatomical representations. These cleaned anatomy tokens and target disease tokens are injected into the denoising network via a Triple-Pathway Cross-Attention mechanism with resolution-dependent routing gates. This architecture leverages the U-Net hierarchy, in which different network depths encode global structure versus fine-grained pathological texture. Furthermore, we introduce Delta Steering, a training-free directional signal derived from the ordinal embeddings that enables explicit, single-pass control over disease transitions at inference without requiring additional forward passes. Validated on the LIMUC dataset, our approach produces high-fidelity images across all severity levels and effectively rebalances skewed class distributions, enhancing performance for downstream classification tasks. The dataset is available at this http URL and the code base at this http URL

---


### 266. [DP-SfM: Dual-Pixel Structure-from-Motion without Scale Ambiguity](https://arxiv.org/abs/2605.01852)

**<font color=#1a73e8>作者：</font>** Lilika Makabe, Kohei Ashida, Hiroaki Santo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-view 3D reconstruction, namely, structure-from-motion followed by multi-view stereo, is a fundamental component of 3D computer vision. In general, multi-view 3D reconstruction suffers from an unknown scale ambiguity unless a reference object of known size is present in the scene. In this article, we show that multi-view images captured using a dual-pixel (DP) sensor can automatically resolve the scale ambiguity, without requiring a reference object or prior calibration. Specifically, the defocus blur observed in DP images provides sufficient information to determine the absolute scale when paired with depth maps (up to scale) recovered from multi-view 3D reconstruction. Based on this observation, we develop a simple yet effective linear method to estimate the absolute scale, followed by the intensity-based optimization stage that aligns the left and right DP images by shifting them back toward each other using cross-view blur kernels. Experiments demonstrate the effectiveness of the proposed approach across diverse scenes captured with different cameras and lenses. Code and data are available at this https URL

---


### 267. [High-Fidelity Mobile Avatars with Pruned Local Blendshapes](https://arxiv.org/abs/2605.01854)

**<font color=#1a73e8>作者：</font>** Youyi Zhan, He Wang, Tianjia Shao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a method to reconstruct high-fidelity human avatars from multi-view video that can run on mobile devices. Many works can model high-quality Gaussian-based full-body avatars from multi-view video. However, these methods require heavy computation to obtain pose-dependent appearance, making deployment on mobile devices very difficult. Recent methods distill from pretrained models and model pose-dependent nonlinear Gaussian attributes by linearly combining global pose features with blendshapes. Although they can run on mobile devices, they suffer some loss of detail. We observe that nearby Gaussians are often highly correlated within a local region of the body, and can be linearly modeled with less error. Therefore, we use local linear blendshapes in small body parts to capture global nonlinear changes of Gaussian attributes. To further reduce computation and model size, we propose to remove blendshapes for Gaussians whose attributes change little, yielding a minimal blendshape representation. Our method is an end-to-end training method without a pretrained model. To make it run on multiple devices, we implement our method using WebGPU. Experiments show that our method can render high-quality human avatars with better details, and can reach 120 FPS at 2K resolution on mobile devices.

---


### 268. [Decouple and Cache: KV Cache Construction for Streaming Video Understanding](https://arxiv.org/abs/2605.01858)

**<font color=#1a73e8>作者：</font>** Zhanzhong Pang, Dibyadip Chatterjee, Fadime Sener 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video understanding requires processing unbounded video streams with limited memory and computation, posing two key challenges. First, continuously constructing new and evicting old key-value(KV) caches is required for unbounded streams. Secondly, due to the high cost of collecting and training on unbounded streams, models must learn from short sequences while generalizing to long streams. Existing streaming VideoVLLMs fail to scale to unbounded video streams or focus on cache reuse strategies, leaving the impact of cache construction underexplored. In this paper, we propose Decoupled Streaming Cache(DSCache), a training-free cache construction mechanism that adapts pretrained offline models to streaming settings. DSCache maintains a cumulative past KV cache while constructing a separate instant cache on-demand, decoupled from past caches to preserve the informativeness of recent inputs. To enable position extrapolation beyond the training length, DSCache further incorporates a position-agnostic encoding strategy, ensuring KV caches to support unseen positions and preventing position overflow. Experiments on Streaming Video QA benchmarks demonstrate DSCache's state-of-the-art performance, with an average 2.5% accuracy gains over prior methods.

---


### 269. [QHyer: Q-conditioned Hybrid Attention-mamba Transformer for Offline Goal-conditioned RL](https://arxiv.org/abs/2605.01862)

**<font color=#1a73e8>作者：</font>** Xing Lei, Jincheng Wang, Xuetao Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline goal-conditioned RL (GCRL) learns goal-reaching policies from static datasets, but real-world datasets are often partially observable and history-dependent, exhibiting a mix of Markovian and non-Markovian that violate standard RL assumptions. History-aware sequence models such as Decision Transformer (DT) are a natural fit for long-term dependency modeling, yet pure attention is inefficient and brittle when handling local Markovian structure and long-range context simultaneously. Although recent hybrid architectures (e.g., LSDT) introduce local extractors to improve local dependencies modeling, the fixed-window extraction cannot adapt its effective memory to varying dependency lengths in temporally heterogeneous settings, often truncating long-range context rather than compressing its content adaptively. Moreover, sequential offline GCRL faces a key bottleneck: under sparse rewards, return-to-go (RTG) becomes non-discriminative across sub-trajectories, providing little guidance signal for stitching goal-reaching behaviors from diverse demonstrations. To address these, we propose \textbf{QHyer}, which replaces RTG with a flow-parameterized, state-conditioned goal-reaching Q-estimator to support stitching across demonstrations, and introduces a gated Hybrid Attention-Mamba backbone that performs content-adaptive history compression while preserving local dynamics. Extensive experiments demonstrate that \textbf{QHyer} achieves state-of-the-art performance on both non-Markovian and Markovian datasets, validating its effectiveness for diverse scenarios.

---


### 270. [Quality-Aware Exploration Budget Allocation for Cooperative Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2605.01865)

**<font color=#1a73e8>作者：</font>** Dahyun Oh, Minhyuk Yoon, H.Jin Kim  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Cooperative multi-agent reinforcement learning (MARL) requires agents to discover joint strategies in a combinatorially large state-action space, yet effective coordination configurations are exceedingly rare. Intrinsic motivation, which augments task rewards with novelty bonuses, is a popular approach for driving exploration, but its effectiveness hinges on the exploration intensity $\beta$, where too large a value overwhelms the task signal and causes coordination collapse, while too small a value prevents discovery of rare strategies. We address two complementary challenges: adapting $\beta$ globally over training, and allocating the exploration budget across agents whose intrinsic reward signals vary in reliability. Our framework combines a return-conditioned sigmoid schedule (RCB) for global intensity control with a per-agent Reward Signal Quality (RSQ) metric that concentrates the exploration budget on agents with reliable signals. The core insight is that agents receiving noisy intrinsic rewards should explore less aggressively, and this allocation can be determined automatically from signal-to-noise statistics. Successor Distance (SD), a quasimetric intrinsic reward, naturally produces distinguishable per-agent signal quality, completing the framework with convergence and ordering preservation guarantees. On seven cooperative benchmarks (MPE, SMAX, MABrax), our method achieves top-tier returns across all environments.

---


### 271. [Robust Conditional Conformal Prediction via Branched Normalizing Flow](https://arxiv.org/abs/2605.01868)

**<font color=#1a73e8>作者：</font>** Rui Xu, Xingyuan Chen, Wenxing Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conformal prediction (CP) constructs prediction sets with marginal coverage guarantees under the assumption that the calibration and test distributions are identical. However, under distribution shift, existing approaches primarily align marginal conformal score distributions, which is sufficient to preserve marginal coverage but does not control the conditional coverage error at individual test inputs. As a consequence, CP can remain unreliable in regions where the conditional score distributions are mismatched. In this work, we bound the conditional invalidity of CP under distribution shift in terms of the Wasserstein distance between the calibration and test distributions. This result highlights the role of invertible transport in mitigating conditional coverage degradation. Motivated by this insight, we introduce Branched Normalizing Flow (BNF), a two-branch architecture that normalizes a test input to the calibration distribution and transforms the prediction set of the normalized input back to the test distribution while preserving conditional guarantees. Empirically, BNF consistently improves conditional coverage robustness on nine datasets across a wide range of confidence levels.

---


### 272. [Sheaf-Theoretic Planning: A Categorical Foundation for Resilient Multi-Agent Autonomous Systems](https://arxiv.org/abs/2605.01879)

**<font color=#1a73e8>作者：</font>** Manuel Hernández, Eduardo Sánchez-Soto  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The challenge of engineering autonomous agents capable of navigating the stochastic and adversarial nature of the physical world has historically resided at the intersection of symbolic logic and control theory. Traditional multi-agent system (MAS) frameworks have relied heavily on monolithic logical models -- primarily variations of the event calculus and situation calculus -- to represent action, change, and temporal persistence. While these classical systems provide robust solutions to the frame problem through mechanisms like circumscription and successor state axioms, they are inherently limited by a closed-world assumption that fails in the face of unobserved agent interventions, plan interruptions, and divergent belief-reality states. The paradigm of Sheaf-Theoretic Planning (STP) emerges as a transformative alternative, grounding the problem of multi-agent coordination under the mathematical structures of topos theory and sheaf semantics. This report provides an exhaustive analysis, justification, and extension of the STP framework, exploring its categorical foundations, implementation feasibility, and role in the future of resilient autonomous systems.

---


### 273. [AFFormer: Adaptive Feature Fusion Transformer for V2X Cooperative Perception under Channel Impairments](https://arxiv.org/abs/2605.01888)

**<font color=#1a73e8>作者：</font>** Xi Zhou, Tao Huang, Qing-Long Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate 3D object detection is essential for ensuring the safety of autonomous vehicles. Cooperative perception, which leverages vehicle-to-everything (V2X) communication to share perceptual data, enhances detection but is vulnerable to channel impairments, such as noise, fading, and interference. To strengthen the reliability of intelligent transportation systems, this work improves the robustness of V2X cooperative perception under communication conditions that reflect common channel impairments. This paper proposes an Adaptive Feature Fusion Transformer (AFFormer), a Transformer-based framework that mitigates the adverse effects of corrupted features by modeling temporal, inter-agent, and spatial correlations. AFFormer introduces three key modules: Multi-Agent and Temporal Aggregation for context-aware fusion across agents and over time, Dual Spatial Attention for efficient modeling of spatial dependencies, and Uncertainty-Guided Fusion for entropy-driven refinement of fused features. A teacher-student knowledge distillation strategy further enhances robustness by aligning fused features with reliable early-collaboration supervision. AFFormer is validated on the V2XSet and DAIR-V2X datasets, where it consistently outperforms existing methods under both ideal and impaired communication conditions, demonstrating improved robustness to communication-induced feature degradation while maintaining a competitive efficiency-accuracy trade-off.

---


### 274. [CyberAId: AI-Driven Cybersecurity for Financial Service Providers](https://arxiv.org/abs/2605.01892)

**<font color=#1a73e8>作者：</font>** George Fatouros, Georgios Makridis, John Soldatos 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> European financial institutions face mounting regulatory pressure while their security operations centres remain constrained not by data or staffing but by reasoning capacity: enterprise SIEMs cover only a fraction of MITRE ATT&CK techniques, two thirds of SOC teams cannot keep pace with alert volumes, and the majority of breaches are preceded by alerts that are generated but never investigated. Frontier large language models now achieve state-of-the-art results on isolated cybersecurity tasks (one-day vulnerability exploitation, code-level patching, intrusion detection) yet no narrow win constitutes a platform that can compose across functions, persist multi-tenant state, map findings to regulatory regimes and survive an audit. This position paper argues that the right unit of construction is a hybrid multi-agent system in which specialised LLM subagents reason over classical SIEM/XDR telemetry rather than replacing it, share accumulated agent state across institutions through privacy-preserving federation, and can connect to complementary capability packs such as quantum-based authentication, digital twins for adversarial validation, and eBPF-based kernel telemetry. We present CyberAId, a model-agnostic, on-premise-deployable platform in which a Main Agent coordination layer, a Reporting capability, and specialist subagents operate within a shared runtime under bounded human-in-the-loop autonomy, organised around four falsifiable design principles, and aligned with relevant regulations. CyberAId will be validated at four representative financial use cases (client impersonation, anti-money-laundering for payment service providers, retail-banking incident response, and high-frequency-trading resilience) and propose skill-based agent adaptation as the most promising research direction for turning each deployment into a contribution to a continuously refined collective defence.

---


### 275. [How Label Imbalance Shapes Geometry: A General Spectral Analysis of Multi-Label Neural Collapse](https://arxiv.org/abs/2605.01897)

**<font color=#1a73e8>作者：</font>** Xiaoxuan Ma, Yixuan Yang, Song Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work investigates the phenomenon of Neural Collapse (NC) in multi-label classification, extending its conceptual framework from multi-class learning to general correlated and imbalanced multi-label settings. Although recent studies have identified a ''tag-wise averaging'' structure for multi-label features, this view relies on implicit assumptions of label balance and combinatorial symmetry. Consequently, it fails to account for the geometrical distortions caused by intrinsic label correlations and data imbalance, which are common in practice. We resolve the multiplicity-one imbalance conjecture raised by Li et al. (2024), showing that higher-multiplicity prototypes obey a class-frequency-weighted synthesis rule rather than uniform averaging. To address this, we propose a rigorous spectral-control framework to analyze the terminal phase of multi-label learning under general imbalanced conditions. We introduce the label covariance spectrum $\kappa_m$, a scalar controlling the distribution-dependent lower-bound geometry, derived from the second-order moment matrix of the label distribution. Contrary to the averaging perspective, our analysis reveals that the centered label covariance spectrum controls the stability of terminal geometry by quantifying the weakest centered inter-class contrast directions. We prove that the classical Tag-wise Averaging emerges only as a special case under perfect orthogonality. Numerical experiments on synthetic distributions validate our theoretical bounds. This work resolves the scaled-average aspect of the imbalance conjecture and establishes a unifying theoretical framework that extends Neural Collapse to complex, imbalanced multi-label settings.

---


### 276. [Behavior-Grounded Lane Representation Learning for Multi-Task Traffic Digital Twins](https://arxiv.org/abs/2605.01901)

**<font color=#1a73e8>作者：</font>** Rei Tamaru, Pei Li, Bin Ran  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traffic digital twins are powerful tools for advanced traffic management, and most systems are built on static geometric representations. However, these representations fail to capture the dynamic functional semantics required for behavior-aware reasoning, such as how a lane operates under complex traffic conditions. To address this gap, we introduce GeoLaneRep, a behavior-grounded lane representation learning framework for traffic digital twins. GeoLaneRep jointly encodes static lane geometry, observed vehicle trajectories, and operational descriptors into a shared, cross-camera semantic embedding. The encoder is trained with a joint objective combining contrastive cross-camera alignment, auxiliary role supervision, and temporal anomaly detection. Across 16 roadside cameras and 132 lanes, the learned embeddings achieve a $0.004$ lateral-rank error and an edge-role F1 of $1.000$ in zero-shot cross-camera matching, and an AUROC of $0.991$ for window-level anomaly detection. We further show that the same behavioral embeddings can condition a diffusion-based generator to synthesize lane geometries that satisfy targeted operational specifications, with $87.9\%$ overall specification accuracy across 38 lane groups. GeoLaneRep thus provides a semantic interface between roadside observations and downstream digital twin tasks, supporting cross-camera transfer, behavior-aware monitoring, and goal-directed lane synthesis. The framework is openly available at this https URL.

---


### 277. [Stochastic Sparse Attention for Memory-Bound Inference](https://arxiv.org/abs/2605.01910)

**<font color=#1a73e8>作者：</font>** Kyle Lee, Corentin Delacour, Kevin Callahan-Coray 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive decoding becomes bandwidth-limited at long contexts, as generating each token requires reading all $n_k$ key and value vectors from KV cache. We present Stochastic Additive No-mulT Attention (SANTA), a method that sparsifies value-cache access by sampling $S \ll n_k$ indices from the post-softmax distribution and aggregates only those value rows. This yields an unbiased estimator of the post-softmax value aggregation while replacing value-stage multiply-accumulates with gather-and-add. We introduce stratified sampling to design variance-reduced, GPU-friendly variants, demonstrating $1.5\times$ decode-step attention kernel speedup over FlashInfer and FlashDecoding on an NVIDIA RTX 6000 Ada while matching baseline accuracy at 32k-token contexts. Finally, we propose Bernoulli $qK^\mathsf{T}$ sampling as a complementary technique to sparsify the score stage, reducing key-feature access through stochastic ternary queries. Both methods are orthogonal to upstream techniques such as ternary quantization, low-rank projections, and KV-cache compression. Together, they point toward sparse, multiplier-free, and energy-efficient inference. We open-source our kernels at: this https URL

---


### 278. [Deep learning-based pavement performance modeling using multiple distress indicators and road work history](https://arxiv.org/abs/2605.01914)

**<font color=#1a73e8>作者：</font>** Lu Gao, Zhe Han, Yunshen Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The deterioration of pavement is a complex and dynamic process determined by different factors including material, environment, design, and some other unobserved variables. Accurate predictions of pavement condition can help maximize the use of available resources for pavement management agencies through better coordinated preservation and maintenance activities. This paper uses deep neural networks such as the convolutional neural network (CNN) and the long short-term memory (LSTM) to model the pavement deterioration process. In this paper, pavement condition data and maintenance and rehabilitation history collected by the Texas Department of Transportation over the past 18 years were used. Twenty-one flexible pavement condition indicators, including cracking, rutting, raveling, and roughness, collected from more than 100,000 pavement sections were included in the proposed models. Promising preliminary results were obtained. Case study results show that the proposed CNN model outperforms standard machine learning models in predicting pavement condition values.

---


### 279. [EAPFusion: Intrinsic Evolving Auxiliary Prior Guidance for Infrared and Visible Image Fusion](https://arxiv.org/abs/2605.01916)

**<font color=#1a73e8>作者：</font>** Zhenyu Sun, Luobin Zhang, Axi Niu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared-visible image fusion aims to create an information-rich fused image by integrating the complementary thermal saliency from infrared sensing and fine textures from visible imaging. Such accurate fusion is essential for real-world perception applications in complex scenes, including nighttime autonomous driving, search and rescue, and surveillance, and can further benefit downstream tasks such as semantic segmentation. However, most existing fusion methods rely upon static trained weights that cannot adapt to scene-specific content at inference time, and often suffer from a granularity mismatch when coarse auxiliary semantics are injected, which makes it difficult to simultaneously highlight targets and preserve details. In this work, we propose EAPFusion to address these issues by using self-evolving intrinsic priors instead of relying on external auxiliary models. Concretely, EAPFusion maintains a compact set of intrinsic priors and progressively updates them across scales. These evolved priors are utilized to dynamically generate convolutional kernels, shifting the paradigm from fixed, pre-trained filters to instance-adaptive parameters via prior-conditioned dynamic convolution. Furthermore, we design a channel-level fusion module that shuffles and interleaves infrared and visible channels, applying local channel mixing to boost cross-modal complementarity. Experiments on different datasets, including cross-dataset evaluation and semantic segmentation, show that the proposed method achieves state-of-the-art quantitative and qualitative fusion results, and consistently boosts downstream performance. Code is coming soon.

---


### 280. [SimPB++: Simultaneously Detecting 2D and 3D Objects from Multiple Cameras](https://arxiv.org/abs/2605.01924)

**<font color=#1a73e8>作者：</font>** Yingqi Tang, Zhaotie Meng, Erkang Cheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Simultaneous perception of 2D objects in perspective view and 3D objects in Bird's Eye View (BEV) is challenging for multi-camera autonomous driving. Existing two-stage pipelines use 2D results only as a one-time cue for 3D detection. We propose SimPB++, which simultaneously detects 2D objects in perspective and 3D objects in BEV from multiple cameras. It unifies both tasks into an end-to-end model with a hybrid decoder architecture, coupling multi-view 2D and 3D decoders interactively. Two novel modules enable deep interaction: Dynamic Query Allocation adaptively assigns 2D queries to 3D candidates, and Adaptive Query Aggregation refines 3D representations using multi-view 2D features, forming a cyclic 3D-2D-3D refinement. For multi-view 2D detection, we use Query-group Attention for intra-group communication. We also design a Crop-and-Scale strategy for long-range perception and a Propagating Denoising strategy with an auxiliary RoI detector. SimPB++ supports mixed supervision with 2D-only and fully annotated data, reducing reliance on expensive 3D labels. Experiments show state-of-the-art performance on nuScenes for both tasks and strong long-range detection (up to 150m) on Argoverse2.

---


### 281. [Training Non-Differentiable Networks via Optimal Transport](https://arxiv.org/abs/2605.01928)

**<font color=#1a73e8>作者：</font>** An T. Le  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks increasingly embed non-differentiable components (spiking neurons, quantized layers, discrete routing, blackbox simulators, etc.) where backpropagation is inapplicable and surrogate gradients introduce bias. We present PolyStep, a gradient-free optimizer that updates parameters using only forward passes. Each step evaluates the loss at structured polytope vertices in a compressed subspace, computes softmax-weighted assignments over the resulting cost matrix, and displaces particles toward low-cost vertices via barycentric projection. This update corresponds to the one-sided limit of a regularized optimal-transport problem, inheriting its geometric structure without Sinkhorn iterations.
PolyStep trains genuinely non-differentiable models where existing gradient-free methods collapse to near-random accuracy. On hard-LIF spiking networks we reach 93.4% test accuracy, outperforming all gradient-free baselines by over 60~pp and closing to within 4.4~pp of a surrogate-gradient Adam ceiling. Across four additional non-differentiable architectures (int8 quantization, argmax attention, staircase activations, hard MoE routing) we lead every gradient-free competitor. On MAX-SAT scaling from 100 to 1M variables, we sustain above 92% clause satisfaction while evolution strategies drop 8--12~pp. On RL policy search, we match OpenAI-ES on classical control and retain performance under integer and binary quantization that collapses gradient-based methods. We prove convergence to conservative-stationary points at rate $O(\log T/\sqrt{T})$ on piecewise-smooth losses, upgraded to Clarke-stationary on the headline architectures and extended to the piecewise-constant regime via a hitting-time bound. These rates match the known zeroth-order query-complexity lower bounds that all forward-only methods inherit. Code is available at this https URL.

---


### 282. [Exploring Data-Free LoRA Transferability for Video Diffusion Models](https://arxiv.org/abs/2605.01929)

**<font color=#1a73e8>作者：</font>** Yuchen Wang, Wenliang Zhong, Lichen Bai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video diffusion models leveraging step distillation or causal distillation have achieved remarkable performance. However, adapting existing LoRAs to these variants remains a critical challenge due to weight space mismatches. We observe that direct application leads to style degradation and structural collapse, yet the underlying mechanisms remain poorly understood. To fill this gap, we delve into the weight space and identify that the incompatibility stems from spectral interference within shared functional clusters defined over singular subspaces. Specifically, our analysis reveals that while both paradigms respect spectral rigidity, they establish conflicting routing pathways that clash through constructive overload or destructive cancellation. To address this issue, we propose Cluster-Aware Spectral Arbitration (CASA), a data-free framework that dynamically arbitrates between safeguarding the target's manifold and restoring LoRA alignment based on spectral density. Extensive experiments demonstrate that CASA effectively mitigates artifacts and revives LoRA functionality. Our code is available at this https URL

---


### 283. [GPU Fingerprinting for Location Verification](https://arxiv.org/abs/2605.01930)

**<font color=#1a73e8>作者：</font>** Wayne Tee, Jonathan Happel  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Robust governance of GPU chips is important for mitigating risks from unauthorized development of advanced AI models. Current methods for monitoring chip location rely on ping-based protocols backed by cryptographic keys stored on-chip. However, these keys can potentially be extracted by adversaries with physical access, compromising the location verification protocol. We address this vulnerability by proposing the use of hardware fingerprints rather than keys to identify GPUs during location verification. In addition, we develop a proof-of-concept GPU fingerprinting methodology that achieves up to 100% re-identification accuracy in small-scale tests.

---


### 284. [Pandora's Regret: A Proper Scoring Rule for Evaluating Sequential Search](https://arxiv.org/abs/2605.01936)

**<font color=#1a73e8>作者：</font>** Gerardo A. Flores, Yash Deshpande, Jannis R. Brea 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In sequential search, alternatives are tested until the true class is found. Standard proper scoring rules like log loss are local, ignoring the ranking of competitors and misaligning model evaluation with search utility. We show that sequential search induces a pairwise structure that overcomes this. By analyzing the expected cost of optimal search under varying testing costs, we derive Pandora's Regret: a closed-form, pairwise-additive, and strictly proper scoring rule. Pandora's Regret both elicits true probabilities and penalizes rank-reversing miscalibrations where distractors outrank the true class. Our construction yields a one-parameter Beta family that balances penalties for rank-swapping versus probability magnitude, while retaining a grounded interpretation as expected search cost. We prove that log loss, accuracy, and macro-F1 rely on implicit decision models misaligned with sequential search. Across 597 MedMNIST models, Pandora-based metrics better predict clinical diagnostic costs than standard alternatives, extending decision-theoretic scoring rule construction to the multiclass setting.

---


### 285. [PepSpecBench: A Unified Evaluation Benchmark for Peptide Tandem Mass Spectrometry Prediction](https://arxiv.org/abs/2605.01945)

**<font color=#1a73e8>作者：</font>** Zhiwen Yang, Pan Liu, Yifan Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tandem mass spectrometry provides a high-throughput framework for identifying and quantifying proteins in complex biological samples. In computational proteomics, predicting peptide MS/MS spectra is a critical task, enabling downstream applications such as large-scale peptide identification and quantification. While deep learning architectures have substantially improved prediction accuracy, three evaluation challenges obscure the true progress of the field. First, inconsistent data preprocessing and incompatible model output spaces hinder fair model comparison. Second, flawed data splitting strategies can permit hidden sequence leakage and inflate reported performance. Third, existing evaluations typically lack comprehensive cross-species benchmarking and systematic assessment of model robustness to influential experimental conditions. To address these challenges, we propose PepSpecBench, a unified benchmark for peptide MS/MS spectrum prediction. PepSpecBench standardizes data preprocessing across complementary public datasets, enforces a strict backbone-disjoint splitting strategy to eliminate sequence leakage, and evaluates diverse architectures within a shared fragment-ion representation space. It further introduces a comprehensive multi-species evaluation suite and physically grounded metadata perturbation probes to assess model robustness and instrument awareness. We uncover previously unrecognized performance discrepancies and robustness limitations across six representative models, providing actionable insights for future model design, evaluation and practical deployment.

---


### 286. [TRAP: Tail-aware Ranking Attack for World-Model Planning](https://arxiv.org/abs/2605.01950)

**<font color=#1a73e8>作者：</font>** Siyuan Duan, Ke Zhang, Xizhao Luo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models enable long-horizon planning by internally generating and evaluating imagined trajectories, making them a promising foundation for generalist agents. However, this imagination-driven decision process also introduces new security risks. Existing backdoor attacks typically aim to manipulate local features, one-step predictions, or instantaneous policy outputs. While such objectives may suffice for weaker reactive models, they are often ineffective against world models, where the learned dynamics prior and planning process can absorb or wash out the effects of shallow perturbations. More importantly, we find that world models exhibit a distinct backdoor vulnerability rooted in the long-tailed ranking structure of imagined trajectories, where disrupting the ordering of a few decision-critical trajectories can systematically hijack planning.
To exploit this vulnerability, we propose TRAP, a backdoor attack framework for world models that targets imagined trajectory ranking. TRAP combines a tail-aware ranking loss to focus optimization on decision-critical trajectories with dual gating mechanisms that stabilize optimization and regulate when and where the attack penalty is applied. Under trigger conditions, TRAP alters the relative ranking of imagined trajectories to redirect planning outcomes, while largely maintaining the normal ranking structure on clean inputs. Experiments on DreamerV3 and TD-MPC2 across diverse tasks show that TRAP consistently induces sustained behavioral deviations and significant performance degradation, highlighting the need for dedicated security evaluation of world-model-based agents.

---


### 287. [Flexi-LoRA with Input-Adaptive Ranks: Efficient Finetuning for Speech and Reasoning Tasks](https://arxiv.org/abs/2605.01959)

**<font color=#1a73e8>作者：</font>** Zongqian Li, Yixuan Su, Han Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning methods like Low-Rank Adaptation (LoRA) have become essential for deploying large language models, yet their static parameter allocation remains suboptimal for inputs of varying complexity. We present Flexi-LoRA, a novel framework that dynamically adjusts LoRA ranks based on input complexity during both training and inference. Through empirical analysis across question answering, mathematical reasoning, and speech tasks, we demonstrate that maintaining consistency between training and inference dynamics is important for effective adaptation, particularly for sequential reasoning tasks. Our findings reveal that input-dependent parameter allocation achieves higher performance with fewer parameters by optimally matching rank configurations to question complexity. Furthermore, task-specific dependency on rank dynamics varies, with mathematical reasoning tasks exhibiting higher dependency than QA tasks. Successful adaptation manifests not only in correctness but also in reasoning quality and instruction adherence. Flexi-LoRA consistently outperforms static LoRA while using fewer parameters, with performance gains more pronounced on tasks requiring strict reasoning chains. Our approach realizes key benefits of mixture-of-experts frameworks through a more streamlined implementation, reducing parameter redundancy while improving model capabilities. We provide comprehensive empirical studies across diverse tasks, establishing a basis for future work in input-adaptive and efficient fine-tuning approaches.

---


### 288. [LAPRAS : Learning-Augmented PRivate Answering for linear query Streams](https://arxiv.org/abs/2605.01960)

**<font color=#1a73e8>作者：</font>** Pranay Mundra, Adam Sealfon, Ziteng Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern database workloads are highly predictable: query streams are dominated by recurring jobs and templates, even when their arrival order is not known in advance. This motivates a learning-augmented view of online differentially private (DP) analytics: can algorithms utilize predictions about which queries will occur to improve utility under a single global privacy budget, while remaining robust when predictions are wrong? We study online DP query answering, where a curator must answer a stream $Q$ of $S$ linear queries arriving in uniformly random order under privacy budget $(\epsilon,\delta)$. We present LAPRAS, which assumes access to an oracle that outputs a prediction set of queries likely to appear in the stream and uses it to guide privacy spending. LAPRAS answers predicted queries using the offline-optimal Matrix Mechanism and answers the remaining queries online from a residual budget. To pace spending across an unknown number of unpredicted queries, we introduce Smooth Allocation, which forms an unbiased stopping-time estimate $\widehat{B}$ from the first $T=\Theta(\log^2 S)$ unpredicted queries and continuously recalibrates per-query expenditure. Empirically, over two real datasets, we validate the intended consistency--robustness trade-off: LAPRAS achieves near-offline utility under high overlap and degrades gracefully to baseline-level performance when overlap is low.

---


### 289. [FIRCE: A Framework for Intrusion Response and Conformal Evaluation](https://arxiv.org/abs/2605.01962)

**<font color=#1a73e8>作者：</font>** Seth Barrett, Lin Li, Gokila Dorai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine learning-based intrusion detection systems deployed in real-world environments frequently suffer from model degradation due to concept drift, where changes in traffic patterns invalidate training assumptions. To address this, we present FIRCE, a Framework for Intrusion Response and Conformal Evaluation that augments supervised IDS classifiers with conformal evaluation-based uncertainty quantification and drift detection. FIRCE supports four conformal evaluation strategies: Inductive, Cross, Approximate Transductive, and our proposed Approximate Cross-Conformal Evaluator, which achieves robust performance with minimal calibration overhead. FIRCE also introduces an adaptive chunking mechanism that dynamically adjusts evaluation granularity in response to stream volatility, improving drift responsiveness while preserving computational efficiency. Using a custom IoT testbed of 10 commercial devices and time-series network captures under simulated attack and drift conditions, we demonstrate FIRCE's ability to detect distributional shifts and trigger model retraining. We additionally benchmark FIRCE on the CICIDS2018 and UNSW-NB15 datasets to validate its generalizability. Experimental results show that conformal evaluation-based drift detection, combined with adaptive chunking, enables an efficient and robust response to evolving threats.

---


### 290. [Retrieval with Multiple Query Vectors through Anomalous Pattern Detection](https://arxiv.org/abs/2605.01965)

**<font color=#1a73e8>作者：</font>** Allassan Tchangmena A Nken, Baimam Boukar Jean Jacques, Miriam Rateike 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A classical vector retrieval problem typically considers a \emph{single} query embedding vector as input and retrieves the most similar embedding vectors from a vector database. However, complex reasoning and retrieval tasks frequently require \emph{multiple query vectors}, rather than a single one. In this work, we propose a retrieval method that considers multiple query vectors simultaneously and retrieves the most relevant vectors from the database using concepts from anomalous pattern detection. Specifically, our approach leverages a set of query vectors $Q$ (with $|Q|\geq 1$), and identifies the subset of vector dimensions within $Q$ that standout (anomalous) from the rest of dimensions. Next, we scan the vector database to retrieve the set of vectors that are also anomalous across the previously identified vector dimensions and return them as our retrieved set of vectors. We validate our approach on two image datasets, a text dataset, and a tabular dataset. Overall, we observe that, across most datasets, larger query sets lead to improved retrieval performance. The improvement is most pronounced when increasing the query sets from 1 to 8, while the gains become smaller beyond that.

---


### 291. [AdamO: A Collapse-Suppressed Optimizer for Offline RL](https://arxiv.org/abs/2605.01968)

**<font color=#1a73e8>作者：</font>** Nan Qiao, Sheng Yue, Shuning Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline reinforcement learning (RL) can fail spectacularly when bootstrapped temporal-difference (TD) updates amplify their own errors, driving the critic toward extreme and unusable Q-values. A key counterintuitive insight of this work is that collapse is not only a property of the backup rule or network architecture: optimizer dynamics themselves can directly trigger or suppress instability. From a control-theoretic viewpoint, we model offline TD learning as a feedback system and analyze Adam-based critic updates. This yields a necessary and sufficient condition for stability of the induced local update dynamics: within the regime we analyze, these dynamics are stable if and only if the spectral radius of the corresponding update operator is strictly below one. Further analysis suggests that standard Adam updates can inadvertently distort the parameter geometry, motivating explicit orthogonality constraints to prevent TD error amplification. To this end, we propose AdamO, an Adam-based optimizer with a decoupled orthogonality correction regulated by a strict task-alignment budget. We prove that this design theoretically guarantees worst-case task safety and preserves Adam's continuous-time dissipative dynamics. Empirically, AdamO is broadly compatible with diverse offline RL baselines, improving stability and returns across a broad suite of benchmarks.

---


### 292. [ProtoFair: Fair Self-Supervised Contrastive Learning via Pseudo-Counterfactual Pairs](https://arxiv.org/abs/2605.01971)

**<font color=#1a73e8>作者：</font>** Marah Halawa, Olaf Hellwich  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning methods learn high-quality visual representations, yet recent studies show that these representations often capture demographic biases present in the training data. Existing fairness-aware methods address this by redesigning the self-supervised objective itself, limiting portability across the rapidly evolving landscape of self-supervised learning (SSL) frameworks. We propose ProtoFair, a fairness-aware contrastive loss designed to work alongside existing SSL objectives without modifying them. ProtoFair leverages unsupervised prototype clustering to identify pseudo-counterfactual pairs: samples sharing the same cluster assignment but belonging to different sensitive groups. By pulling these content-matched, cross-group samples together in the embedding space, ProtoFair encourages the encoder to learn representations that are invariant to the sensitive attribute. The method requires only sensitive attribute annotations, no target labels, and integrates seamlessly with both SimCLR and SupCon. Experiments on CelebA and UTKFace demonstrate consistent fairness improvements while maintaining competitive accuracy.

---


### 293. [Plausible Deniability in Fully Homomorphic Computation](https://arxiv.org/abs/2605.01985)

**<font color=#1a73e8>作者：</font>** Shahzad Ahmad, Stefan Rass, Zahra Seyedi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We introduce \emph{Plausible Deniability in Fully Homomorphic Computation} (PD-FHC), a framework enabling users to outsource Boolean computations to an untrusted cloud while maintaining both computational privacy against honest-but-curious providers and plausible deniability against coercive adversaries. We define the notion of a \emph{Deniable Computation Medium} (DCM) and a \emph{Deniable Computation Scheme} (DCS) as medium-independent abstractions, then instantiate them using RGB images with Fredkin-gate circuits. Multiple computation scenarios (one real, several decoys) are embedded at secret positions within cover images; the cloud applies identical operations to every pixel, processing all scenarios uniformly. Under coercion, the user reveals a decoy computation with verifiable results while the real computation remains hidden. We formalize multi-round coercion games with existence and intent distinguishing advantages, proving computational privacy with advantage $\Theta(1/(n-1)!)$ and negligible existence-hiding advantage for the image instantiation. Our Python implementation, benchmarked across circuit sizes (5--289 gates) and image dimensions ($128^2$ to $512^2$), demonstrates competitive performance with TFHE for Boolean circuits while providing deniability that FHE fundamentally cannot offer.

---


### 294. [Misclassification Rate and Privacy-Utility Trade-offs in Graph Convolutional Networks via Subsampling Stability](https://arxiv.org/abs/2605.01987)

**<font color=#1a73e8>作者：</font>** Yexin Zhang, Zhongtian Ma, Qiaosheng Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study differential privacy (DP) in Graph Convolutional Networks (GCNs) through the framework of \textit{subsampling stability}. We derive upper bounds on the misclassification rate that depend explicitly on the subsampling probability $p_s$. Furthermore, we characterize the \textit{privacy--utility trade-off} by identifying feasible ranges of $p_s$; if $p_s$ is too large, the stability-based privacy condition becomes difficult to satisfy, yielding vacuous guarantees, whereas if it is too small, accuracy deteriorates. Our results provide the first rigorous theoretical framework for understanding subsampling stability in GCNs under DP.

---


### 295. [DBLP: Phase-Aware Bounded-Loss Transport for Burst-Resilient Distributed ML Training](https://arxiv.org/abs/2605.01989)

**<font color=#1a73e8>作者：</font>** Zechen Ma, Zixi Qu, Jinyan Yi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distributed machine learning (ML) training has become a necessity with the prevalence of billion to trillion-parameter-scale models. While prior work has improved training efficiency from the ML perspective at the application layer, it often fails to address transient congestion events at the network layer that introduce severe tail latency and training-time variability, thereby undermining the quality of service (QoS) of distributed ML training systems. Existing network optimizations treat all gradients equally and thus fail to integrate sufficient model-training insights into communication protocol design.
In this paper, we present Dynamic Bounded-Loss Protocol (DBLP), a burst-resilient, training-phase-aware, and hardware-agnostic transport protocol that incorporates model-level tolerance properties into gradient communication. By dynamically adjusting gradient loss tolerance across training phases, DBLP reduces overall training time and mitigates tail-latency collapse during transient high-loss events (i.e., microbursts).
Compared to the current state-of-the-art solution (baseline), DBLP tolerates significantly higher loss while achieving comparable test accuracy, and reduces end-to-end training time by an average of 24.4% and a maximum of 33.9%. At microburst events, DBLP achieves up to 5.88x single-round communication latency speedups over the baseline, preventing burst-induced tail-latency spikes and maintaining stable training performance.

---


### 296. [From Concept to Capability: Evaluating 3D Gaussian Splatting for Synthetic Scene Editing in Autonomous Driving](https://arxiv.org/abs/2605.01995)

**<font color=#1a73e8>作者：</font>** Ali Nouri, Yifei Zhang, Yifan Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The perception of an Autonomous Driving System (ADS) critically depends on relevant, comprehensive, and diverse datasets to ensure its safety while operating in the environment. Field data collection lacks completeness with respect to the list of rare but still possible safety-related scenarios needed for the development, verification, and validation of the ADS. 3D Gaussian Splatting (3DGS) has shown promising capabilities for the reconstruction and editing of scenes based on data collected by cameras and LiDAR sensors. However, the industrial fidelity evaluation of reconstructions is underexplored, which is crucial when employing such methods in safety-related systems, especially for ADS. This becomes more challenging as ADS operates in a dynamic, uncontrolled environment with limited viewpoints and often partially occluded objects. This paper addresses this gap by proposing and implementing a framework (Fig. 1) to systematically analyze the capabilities and limitations of 3DGS for use in the reconstruction of safety-related scenes. It focuses on the quality of reconstruction for vehicles and pedestrians, which are the two most critical object classes for ADS. Our findings provide industry insights into the fidelity degradation of reconstructions from multiple novel viewpoints, both lateral and longitudinal, enabling the integration of these methods into real-world industrial AD software development and testing pipelines.

---


### 297. [TumorXAI: Self-Supervised Deep Learning Framework for Explainable Brain MRI Tumor Classification](https://arxiv.org/abs/2605.01999)

**<font color=#1a73e8>作者：</font>** Abrar Hossain Zahin, Amit Kumar Saha, Tanvir Mridha 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Classifying brain tumors using magnetic resonance imaging (MRI) is crucial for early diagnosis and treatment; however, tumor heterogeneity and a dearth of annotated datasets restrict the use of supervised deep learning approaches. In this work, we use self-supervised learning (SSL) to study multi-class brain tumor classification. Using a ResNet-50 backbone, we evaluate four SSL frameworks including SimCLR, BYOL, DINO, and Moco v3 on a publicly available dataset of 4,448 MRIs with 17 distinct tumor types. On the dataset, SimCLR achieved 99.64% accuracy, 99.64% precision, 99.64% recall, and 99.64% F1-score. The workflow includes preprocessing, fine-tuning, linear evaluation, and SSL pretraining with data augmentations. Results show that, when labels are limited, SSL-pretrained models outperform supervised baselines in terms of F1-score, recall, accuracy, and precision. Additionally, by providing visual insights into model decisions, Explainable AI techniques (Grad-CAM, Grad-CAM++, EigenCAM) enhance interpretability. These results demonstrate SSL's scalability and dependability in diagnosing brain tumors from unlabeled medical data.

---


### 298. [RamanBench: A Large-Scale Benchmark for Machine Learning on Raman Spectroscopy](https://arxiv.org/abs/2605.02003)

**<font color=#1a73e8>作者：</font>** Mario Koddenbrock, Christoph Lange, Robin Legner 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine Learning (ML) has transformed many scientific fields, yet key applications still lack standardized benchmarks. Raman spectroscopy, a widely used technique for non-invasive molecular analysis, is one such field where progress is limited by fragmented datasets, inconsistent evaluation, and models that fail to capture the structure of spectral data. We introduce RamanBench, the first large-scale, fully reproducible benchmark for ML on Raman spectroscopy, consisting of streamlined data access, evaluation protocols and code, as well as a live leaderboard. It unifies 74 datasets (including 16 first released with this benchmark) across four domains, comprising 325,668 spectra and spanning classification and regression tasks under diverse experimental conditions. We benchmark 28 models under a standardized protocol, including classical methods (e.g., PLS), Raman-specific (e.g., RamanNet), Tabular Foundation Model (TFM) (e.g., TabPFN), and time-series approaches (e.g., ROCKET). TFM consistently outperform domain-specific and gradient boosting baselines, while time-series models remain competitive. However, no method generalizes across datasets, revealing a fundamental gap. Therefore, we invite the community to contribute new approaches to our living benchmark, with the potential to accelerate advances in critical applications such as medical diagnostics, biological research, and materials science.

---


### 299. [Personalized Digital Health Modeling with Adaptive Support Users](https://arxiv.org/abs/2605.02004)

**<font color=#1a73e8>作者：</font>** Zhongqi Yang, Mahkameh Rasouli, Neda Mohseni 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalized models are essential in digital health because individuals exhibit substantial physiological and behavioral heterogeneity. Yet personalization is limited by scarce and noisy user-specific data. Most existing methods rely on population pretraining or data from similar users only, which can lead to biased transfer and weak generalization. We propose a unified personalization framework that trains a personal model using adaptively weighted support users, including both similar and dissimilar individuals. The objective integrates personal loss, similarity-weighted transfer from similar users, and contrastive regularization from dissimilar users to suppress misleading correlations. An iterative optimization algorithm jointly updates model parameters and user similarity weights. Experiments on six tasks across four real-world digital health datasets show consistent improvements over population and personalized baselines. The method achieves up to 10% lower RMSE on large-scale datasets and approximately 25% lower RMSE in low-data settings. The learned adaptive weights improve data efficiency and provide interpretable guidance for targeted data selection.

---


### 300. [Privy: From Fine Print to Fair Practice in Privacy Rights Exercise](https://arxiv.org/abs/2605.02005)

**<font color=#1a73e8>作者：</font>** Qi Sun, Ziyang Li, Yinzhi Cao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Privacy regulations such as the CCPA and GDPR grant individuals rights over their personal data, yet it remains challenging for most users to exercise them in practice due to vague policy interpretation and unapproachable settings on web interfaces. We introduce Privy, an LLM-powered browser assistant that guides users through exercising their privacy rights on websites. Privy automatically analyzes a website's privacy policy and surfaces the specific rights available as action labels in a side panel. When a user selects a right, Privy provides step-by-step guidance and navigation, presenting direct links, generating email templates, or guiding form completion. Users can also request on-demand policy evidence and rights education to enhance their literacy. A technical evaluation across 14 websites shows that Privy extracts rights with high precision (0.979) and completes 96.3\% of privacy tasks in an average of 3.2 steps. A user study (N=15) also demonstrates the overall high-level of perceived helpfulness among users. Our findings suggest that comprehension and usability are not two separate challenges but a single interaction problem, and that effective privacy support requires integration of policy understanding and privacy actions. We offer design suggestions for future privacy assistants.

---


> [!TIP]
> 当前位于：**251-300**（第 6/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-511](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
