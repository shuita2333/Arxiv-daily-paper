# 📦 其他研究 | 2026年09月29日

> 本类共 **225** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-225](./part-05.md)

---

### 51. [Action Forcing: Training World Models on Unsupervised Video by Recovering Underlying Egomotion Bases](https://arxiv.org/abs/2609.30595)

**<font color=#1a73e8>作者：</font>** Ashish Sundar, Tiankuo Hou, Zhong Fan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synchronised action annotations are needed to train controllable world models and these datasets remain elusive. Existing approaches make use of instrumented platforms with calibrated sensors, costly manual annotation, or latent-action models which lack grounding. We instead turn ordinary unlabelled video into action-supervised training data by recovering (without training) a data-derived egomotion basis. We track pixel displacements across frames and exploit the recurring coherent structure induced by egomotion to obtain grounded control signals directly. Using a method as simple as principal components analysis perform this, we find that the leading components provide signed, scalable, and composable throttle--yaw controls, although the method can recover only motion axes represented in the data. To prevent a high-capacity video DiT from exploiting pixel-level supervision, an online latent critic distils a frozen decoder--tracker--PCA (Principal Components Analysis) teacher without backpropagating through the decoder or tracker. Finally we critique the use of video generation metrics to evaluate WMs and introduce an example of an alternative, reference-free evaluation method. We measure \textit{controllability}, \textit{plausibility}, \textit{conjuring} (creating objects out of thin air) and \textit{geometric integrity}, revealing failures that conventional video metrics miss. We show that most baselines follow familiar action directions but struggle to reverse or remain stationary. Our model handles both while retaining compositional control and generation quality. Despite backwards actions being less than $1\%$ of our training data, we find that the model learns to reverse, scale its response linearly, and compose throttle with steering, all simply by learning through a grounded action space.

---


### 52. [Probabilistic Robustness-driven Universal Adversarial Perturbations with Explainability against Deep Reinforcement Learning-based Intrusion Detection System](https://arxiv.org/abs/2609.30605)

**<font color=#1a73e8>作者：</font>** Hongsen Zhang, Lu Zhang, Mingjing Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep reinforcement learning (DRL) enables adaptive intrusion detection in dynamic network environments but also exposes intrusion detection systems (IDS) to adversarial threats such as universal adversarial perturbations (UAPs), which apply a single input-agnostic perturbation to degrade detection performance across traffic. Probabilistic Robustness (PR), as a post-hoc evaluation metric, provides a principled, population-level measure of adversarial impact that conceptually aligns with the universality objective of UAPs, i.e., PR quantifies the prevalence of misclassification in the input space, making it a natural signal for guiding UAP generation. Hence, we propose PR-based UAP, which represents the first integration of an explicit PR-driven objective into generating UAPs against DRL-based IDS. Building on this formulation, we introduce PX-UAP, which leverages explainable artificial intelligence (XAI) to guide perturbation shaping under realistic domain constraints, and provides a rigorous theoretical analysis of its design. Extensive experiments demonstrate that PX-UAP consistently outperforms state-of-the-art UAP methods in attack effectiveness.

---


### 53. [MedTokenBudget: Lesion-Preserving Token Routing for Dermoscopic Image Classification](https://arxiv.org/abs/2609.30613)

**<font color=#1a73e8>作者：</font>** Zhexiang Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dermoscopy classifiers built on Vision Transformers process all image patches uniformly, although diagnostic evidence is concentrated in the lesion region. Existing token pruning methods reduce tokens using generic saliency or similarity signals, but rarely ask whether the retained subset still contains the lesion. This paper introduces MedTokenBudget, a supervised post-backbone token routing framework that learns to construct compact lesion-enriched representations when auxiliary lesion masks are available. Its Lesion-Aware Token Scoring (LATS) module fuses attention entropy, feature norm, and local feature contrast through a learned scorer, then routes the top-$K$ patches under a target budget. LATS is trained with budget curriculum learning, diversity regularization, attention distillation, and lesion-mask supervision. The trained router is evaluated with a lesion retention rate that directly measures how much ground-truth lesion evidence survives the token budget. On ISIC 2019, mask-supervised LATS consistently outperforms Random and ToMe at headline budgets while retaining substantially more lesion patches. Code is provided for reproducibility, and complete tabulated results are included in the supplementary material.

---


### 54. [Steering Versus Teleporting in Mobile Virtual Reality](https://arxiv.org/abs/2609.30620)

**<font color=#1a73e8>作者：</font>** Kristen Grinyer, Daniel Zielasko, Robert J. Teather  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Mobile virtual reality (MVR) provides low-cost access to extended reality (XR), but its limited input restricts use of common locomotion techniques such as head-decoupled and velocity-controlled steering. Using a low-cost controller with an audio-based button, we compared gaze- and controller-directed steering and teleportation in MVR. We included a controller pitch-based speed-control technique enabling continuous head-decoupled steering. Performance and participant feedback indicate that gaze was better suited to teleportation, whereas controller pointing better supports steering in primed search. We compare with similar techniques in standard VR and derive design considerations for low-cost, narrow-FOV hardware, demonstrating the potential to support varied travel techniques and velocity control in low-fidelity XR.

---


### 55. [CraftTrace: Unflattening Videos into Malleable, Creation-Inspired Structures for Generative Editing](https://arxiv.org/abs/2609.30623)

**<font color=#1a73e8>作者：</font>** Boyu Li, Yuqian Zhou, Duotun Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent generative video editing models enable video content modification (e.g., changing a character) but target short clips. Extending them to full multi-shot videos requires tedious work to locate relevant content across shots, segment it into clips, craft context-aware editing prompts for each clip, and repeatedly articulate complex editing intent. To address this, we explore an interaction paradigm for editing through underlying video structures (e.g., scripts, scenes, characters, shots, and their relationships). We present CraftTrace, an interactive prototype that transforms a video into a malleable, multilevel structure for generative editing. Users work in task-centric workspaces to modify elements or reshape relationships, while an AI agent translates and propagates changes across the video. A user study and expert review show that this structure helps users understand videos, formulate and refine editing intent, and explore alternatives, supporting rapid prototyping during early-stage exploration and full video post-production.

---


### 56. [OpenHail: An Event-Driven Gymnasium Environment for Electric Ride-Hailing Fleet Control](https://arxiv.org/abs/2609.30628)

**<font color=#1a73e8>作者：</font>** Tommaso Schettini, Nicholas D. Kullman, Jorge E. Mendoza  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine-learning policies have attracted increasing interest for ride-hailing fleet control in recent years. Reinforcement learning, in particular, requires a structured simulation environment that specifies observations, actions, rewards, and decision epochs for training and evaluation. For electric fleets, this environment must also capture the interaction among stochastic demand, vehicle operations, and capacitated charging infrastructure. We present OpenHail, an open-source Gymnasium environment for joint control of electric ride-hailing fleets. Its fixed-size observation--action interface exposes request assignment, repositioning, and charging to a single policy. The event-driven simulator represents requests with pickup deadlines, vehicle job queues, battery dynamics, and finite-capacity charging facilities with first-in--first-out queues. A configurable decision-epoch mechanism separates internal simulator events from policy interactions, supporting event-driven, periodic, hybrid, and policy-requested control within the same operational model. The software provides seeded instances, feasible-action utilities, evaluation tools, operational metrics, and baseline policies. The source code is available at this https URL.

---


### 57. [Stable initialization without the CLT](https://arxiv.org/abs/2609.30633)

**<font color=#1a73e8>作者：</font>** Simon Kuang, Kyle Chickering, Xinfan Lin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Successful training of deep neural networks is highly dependent on the distribution of the initial weights. If the weights are too large, network training blows up; if they are too small, the model fails to learn features. Stable initialization is the optimal moderation between these two extremes. The conventional theory of random networks uses the Central Limit Theorem to control inter-neuron dependencies, which introduces distributional approximation error and coupling between layers. For networks with sine activations, we derive the uniform-phase initialization, which obviates distributional approximation and fully decouples the layers. Ours is the first work to use the sine function's periodic symmetry. Models trained with the uniform-phase initialization outperform the state of the art in neural representation tasks like image and audio fitting. We find that our untuned models are competitive with the best-tuned baselines from previous work and support $\mu$P width scaling.

---


### 58. [Conditional Predictive Sufficient Statistics for Visual Representation Learning](https://arxiv.org/abs/2609.30647)

**<font color=#1a73e8>作者：</font>** Yuzhou Hong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A useful visual representation is a statistic of the observed past that retains the latent factors shared with the future and discards patch-private noise. We formalize this requirement as a conditional predictive sufficient statistic (CPSS). Under a shared-factor model of image patches, the mutual information between the past and the next patch equals the information the past carries about the shared factor, up to a remainder that the next patch itself fails to reveal. Predicting the next patch embedding with a cosine loss is maximum likelihood for a von Mises-Fisher model of that embedding's direction, and is therefore a tractable surrogate for the predictive information. The same population loss is also minimized by a constant embedding, so stop-gradient does not by itself select the sufficient statistic; it only blocks the symmetric gradient that implements the constant solution in one step. The regression target is a shallow embedding, which forces the network output back into that shallow range and leaves the sufficient statistic in intermediate blocks. Small causal Transformers on MNIST and CIFAR-10 are used as diagnostics, not as a leaderboard. On MNIST the future shift and the stop-gradient move probe accuracy by tens of points, and the CPSS readout peaks before the output. On CIFAR-10, with the same short budget and no augmentation, every objective lands near a linear classifier on pixels. What still matches the derivation is the geometry: the CPSS output is a worse readout than its best intermediate block, next-pixel regression does not pay that penalty, and removing the stop-gradient collapses the effective rank of the embedding even when the pretext loss looks perfect.

---


### 59. [Population loss in shallow ReLU networks: Bias & families of critical points](https://arxiv.org/abs/2609.30661)

**<font color=#1a73e8>作者：</font>** Michael Field  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The main result presented is a formula for the population loss in the student-teacher kernel model that is applicable to shallow ReLU networks with bias. This extends previous work of Choo and Saul (2009) and Brutzkus and Globerson (2017). The formula makes essential use of Owen's T-function. The necessary theory of the T-function is given and a high precision coding using MPFR for the T-function, based on an algorithm of Komelj (2023), is available on request. It is shown that various families of spurious minima described in past papers of Arjevani and the author extend to biased networks and that the loss is always strictly decreased when bias is added. The change in landscape geometry caused by adding bias appears to be relatively mild. Only the simplest examples are described in this paper where it is assumed that the number of inputs is equal to the number of neurons (this restriction is for reasons of length). A review of relevant previous results on unbiased networks is included. Aside from Gaussian statistics, the main mathematical tools and ideas come from analytic geometry (analytic and subanalytic sets, the Curve Selection Lemma).

---


### 60. [StarWM: Self-Supervised Trained Attention Routing for Robust World Models](https://arxiv.org/abs/2609.30667)

**<font color=#1a73e8>作者：</font>** Zeqiang Zhang, Fabian Wurzberger, Maximilian Otte 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A robust world model must strike the balance between faithfully capturing environmental dynamics and abstracting away from irrelevant content. While reconstruction-based world models ensure faithful supervision, they misallocate representational capacity by pixel area rather than dynamics relevance for visual tasks, which can cause task-irrelevant content to dominate the learned representation. Alternatively, reconstruction-free methods avoid this bias but risk discarding possibly relevant information. We propose StarWM, which uses a cross-attention module trained on self-supervised dynamics to decide where reconstruction applies. A dual-stream decoder then restricts reconstruction to the attended regions, with stop-gradient barriers preventing interference between the two objectives. These components allows reconstruction to supervise the visual content of attended regions without contaminating the latent with non-predictive information. On DeepMind Control with dynamic video backgrounds, default (reward-free) StarWM achieves the strongest performance under random-frame distractors and substantially outperforms reconstruction-based baselines under sequential video. In addition, its reward-augmented variant matches or exceeds reconstruction-free methods on sequential video, achieving the highest overall return across all distractor regimes. Mechanistic probing confirms StarWM preserves state attributes with near-perfect fidelity through long-horizon imagination while systematically discarding distractors.

---


### 61. [TRACE: Temporal Audit and Condition-aware Evaluation of Streaming Video Understanding](https://arxiv.org/abs/2609.30670)

**<font color=#1a73e8>作者：</font>** Yibo Ma, Qianqian Zhang, Peng Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Streaming video understanding requires models to interpret evidence as it arrives, yet current evaluations often report task scores without specifying when evidence becomes valid, how visual history is maintained, or how responses are triggered. As a result, similar scores may correspond to different workloads, failure modes, and operational behavior. We introduce TRACE (Temporal Audit and Condition-aware Evaluation), a condition-aware benchmark and evaluation framework that makes these factors explicit. TRACE combines temporally audited visual tasks with evidence timing and instruction-dependent trigger annotations, a unified causal Core--Adapter protocol that controls information availability while recording actual history processing and response events, and multidimensional reporting of answer quality, timeliness, response-selection behavior, workload, completion, and reliability. On 1,240 records from 517 videos, we evaluate eight publicly available models or systems in eight configurations. We find that nearly identical QA accuracy can mask substantial differences in completion, answer validity, and generation workload, while proactive performance separates into response quality, response delay, false alarms (responses emitted while no target window is currently valid and a later one remains), and missed target windows. These results show that streaming-video performance should be interpreted as execution-conditioned system behavior rather than a single score. Our benchmark and code can be accessed at \href{this https URL}{this https URL}.

---


### 62. [Structure-Guided Masked Autoencoders for Ultra-High Resolution Scientific Image Understanding](https://arxiv.org/abs/2609.30682)

**<font color=#1a73e8>作者：</font>** Enzhi Zhang, Du Wu, Rui Zhong 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised pre-training with Vision Transformers, including Masked Autoencoders (MAE), is difficult to apply to gigapixel scientific images. Random masking is poorly matched to the structured, multi-scale morphology of scientific data, while uniform tokenization produces prohibitively long sequences that make $O(N^2)$ attention impractical. We propose SGMA, a structure-guided masked autoencoding framework for ultra-high-resolution scientific images. SGMA couples two components: a content-adaptive quadtree tokenizer that compresses gigapixel images into a fixed-length sequence, and a structure-conditioned masking process that biases reconstruction toward spatially informative regions. To stabilize this process across scales, we introduce Damped Accumulation (DA), which aggregates signal-dependent responses across the tree into a structure canvas used to guide masking. The resulting pre-training task preserves fine microstructure while remaining compatible with standard ViT encoders and MAE-style reconstruction. Across electron microscopy, whole-slide optical microscopy, and X-ray CT datasets, SGMA consistently outperforms MAE baselines. It achieves 95.68% Dice on the 8K x 8K x 28K SpringXCT dataset, improving over the same-architecture MAE baseline by +13.00 points, and 83.21% Dice on the 32K^2 WSI PAIP dataset, improving by +16.84 points, while providing up to a 24.8x inference speedup.

---


### 63. [PixSim: a calibrated open-source simulator of instant-payment fraud, recovery and interdiction under analyst capacity constraints](https://arxiv.org/abs/2609.30684)

**<font color=#1a73e8>作者：</font>** Bashir Zeimarani, Alireza Khatib, Somayeh Mousavinasr 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Brazil's Pix settles about 5.9 billion instant, irreversible transfers a month. A fraudulent transfer can be recovered only while the funds remain in a traceable account, and in 2025 the Central Bank's recovery mechanism (MED) returned 9% of accepted contested value. Interdiction therefore has to happen before settlement, by routing each transaction to pass, human review or block, under a finite analyst team and a regulatory hold window. To our knowledge no public simulator jointly models irreversible settlement, a regulated recovery mechanism, downstream fund dispersal and capacity-constrained review. We present PixSim, an open-source simulator of the Pix rail with these elements, calibrated to Banco Central do Brasil open data, with every parameter sourced, calibrated to one published observable, or registered as an assumption. With the model frozen, full-scale runs reproduce the 2025 recovery rate within 0.006 and its decomposition within 0.02; the February-April 2026 window is reported as a misfit and the May 2026 tracing regime as a projection. On a benchmark with a payer-side scorer, four reference policies and ten scenarios, within the simulated mule model: recovery after settlement is constrained by dispersal speed; staffing by the arrival profile cuts a fixed rule's alert expiry from 52% to 2% at constant hours; halving the team removes a fixed threshold-and-block rule's advantage over a queue-aware rule, on loss and on loss plus false-block harm (+0.106 of victim value, positive on all twenty paired seeds), while a reversal at two thirds of the team was not confirmed on independent seeds; and a synthetic scorer of held-out AUC 0.82 cuts lost value by about a quarter. Code and data: this https URL

---


### 64. [SAGE: Source-Anchored Guidance via Frequency Equalization for Hierarchical RGB-T Alignment and Fusion](https://arxiv.org/abs/2609.30703)

**<font color=#1a73e8>作者：</font>** Timing Li, Yiming Sun, Boan Tao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial misregistration and cross-modal discrepancies often cause ghosting, structural blurring, and content imbalance in RGB-T fusion. Existing methods typically decouple appearance adaptation, geometric alignment, and information fusion, limiting dependency propagation across stages. We propose Source-Anchored Guidance via Frequency Equalization for Hierarchical RGB-T Alignment and Fusion (SAGE), a unified framework integrating frequency equalization, hierarchical alignment, and subband fusion. SAGE employs invertible joint encoding and source-specific low-frequency modulation to derive structural and gain guidance while preserving source information. Hierarchical frequency collaborative alignment estimates global affine geometry from low-frequency approximations and transfers geometric and contextual cues to high-frequency correlation reasoning for reliability-aware residual refinement. Guided subband fusion jointly aggregates the aligned frequency coefficients under propagated source and alignment guidance, coordinates complementary low- and high-frequency information, and reconstructs the fused image through the inverse wavelet transform. Extensive experiments on RGB-T datasets with real-world and synthetic misalignments demonstrate consistently competitive performance in alignment and fusion, validating the effectiveness of source-anchored guidance for weakly registered RGB-T images.

---


### 65. [Combining General and Domain-Specific Pretext Tasks for Brain MR Image Segmentation](https://arxiv.org/abs/2609.30708)

**<font color=#1a73e8>作者：</font>** Tasneem Nasser, Susanne Schmid, Roberto Souza 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A key challenge in medical image analysis is the scarcity of large annotated datasets for specific populations and diseases. As deep learning models rely heavily on labeled data, effective transfer learning strategies are needed to reduce the dependence on manual annotations. Self-supervised learning has emerged as a promising approach for developing foundation models by enabling the learning of transferable feature representations from large-scale unlabeled medical imaging datasets. In this study, we investigate voxel-level brain age prediction as a domain-specific self-supervised pretext task and compare it with image inpainting, a widely used non-domain-specific alternative. We further propose a multitask self-supervised pretraining framework that jointly optimizes both objectives to learn complementary neuroimaging representations. The pretrained models are evaluated on three downstream magnetic resonance image segmentation tasks: multiple sclerosis lesion segmentation, ischemic stroke lesion segmentation, and cortical brain structure segmentation. Overall, the proposed multitask pretraining framework consistently outperformed the single-task pretrained models and training from scratch across most experimental settings, demonstrating the benefit of combining domain-specific and general self-supervised learning pretext tasks for the development of generalizable neuroimaging foundation models.\ Code Availability: The source code used in this study is publicly available at this https URL

---


### 66. [CRC-Router: Risk-Constrained Routing for Medical Agentic AI Systems](https://arxiv.org/abs/2609.30714)

**<font color=#1a73e8>作者：</font>** Xueyang Li, Mingze Jiang, Gelei Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems are increasingly being explored in medical imaging to improve throughput and reduce clinician workload; however, safe deployment remains challenging because autonomous errors may propagate into downstream clinical decisions. A central requirement is therefore not only strong predictive performance, but also a reliable routing mechanism that determines when the system should proceed autonomously and when a case should be escalated for further review. To address this gap, we propose CRC-Router, a risk-constrained, uncertainty-aware routing module that is applicable to both conventional medical prediction models and agentic medical AI systems. CRC-Router combines multiple complementary uncertainty signals with the predictive score to construct a per-finding routing feature vector, maps this vector to an estimated wrong-accept risk using a lightweight per-finding risk model, and then applies Conformal Risk Control (CRC) to calibrate acceptance thresholds under a user-specified risk target. Instantiated on chest X-ray multi-finding triage using the NIH ChestX-ray14 dataset, CRC-Router achieves the strongest empirical risk--coverage trade-off among the evaluated baselines, both as a standalone routing layer and as a plug-in module integrated with the state-of-the-art MedRAX agent. These results demonstrate both the effectiveness of CRC-Router in selective medical automation and its modular, model-agnostic compatibility with existing predictive and agentic medical pipelines. Code is publicly available at this https URL

---


### 67. [NEMSim: Learning Control-Conditioned Multi-Event Physical Dynamics via Executable Event-Mechanism Priors](https://arxiv.org/abs/2609.30718)

**<font color=#1a73e8>作者：</font>** Junsong Yu, Junjie Xie, Pengwei Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-fidelity simulation of control-conditioned multi-event physical systems is computationally expensive, especially across broad control spaces and long trajectories. In these systems, macroscopic evolution emerges from localized discrete events whose intensities and effects depend on process controls and evolving local states, while the available system knowledge is typically expressed as event-attribute descriptions. Purely data-driven surrogates must infer these event effects from limited trajectory coverage, which can hinder generalization to unseen control regimes. Physics-guided methods instead primarily build on equation-level constraints or differentiable solvers rather than discrete event-rule priors. We therefore propose NEMSim (Neural Event-Mechanism Simulator), which compiles predefined event-attribute descriptions into an executable transition structure linking control-dependent event intensities, prior-guided mechanism attribution, and state-dependent responses. To enable evaluation of control-conditioned multi-event dynamics with explicit system knowledge, we construct a 3D KMC-based benchmark pairing high-fidelity trajectories with explicit event rules, standardized splits, and evaluation protocols. Across three settings, NEMSim reduces Avg. RMSE by 58.9%-81.3% relative to the strongest baseline in each setting. It also remains best in the data-efficiency study with training-data fractions down to 10%. Mechanism analyses further show that these gains arise from executable rule integration rather than prior access or architecture alone.

---


### 68. [Werracle: Sub-Cent Intra-Block AI Reflex Oracles and Flash-Loan Circuit Breakers for EVM Smart Contracts](https://arxiv.org/abs/2609.30719)

**<font color=#1a73e8>作者：</font>** Volkan Dağlı, Zerrin Dağlı, Dağhan Dağlı  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Contemporary on-chain artificial intelligence (AI) encounters an intractable Von Neumann memory and latency wall. Storing static floating-point neural weight matrices inside Ethereum Virtual Machine (EVM) storage costs millions of gas, rendering direct on-chain inference impossible. While Zero-Knowledge Machine Learning (ZK-ML) offloads matrix tensor multiplications to off-chain provers, it introduces fatal constraints: 10 to 300 seconds of SNARK proving latency and 250,000 to 500,000 gas per proof verification. Because decentralized finance (DeFi) exploits - such as uncollateralized flash-loan attacks, predatory sandwich MEV, and toxic loss-versus-rebalancing (LVR) flow - occur atomically inside a single block, ZK-ML oracles cannot react in time. Here, we present Werracle, a production-grade, zero-storage on-chain AI decision oracle fitting inside a single 32-byte EVM storage slot (bytes32). Leveraging foundational procedural Mandelbrot escape dynamics (z_{n+1} = z_n^2 + c) established by Dagli et al. (arXiv:2609.25498), Werracle derives continuous non-linear decision hyperplanes from a 24-byte coordinate triplet Theta = (c_x, c_y, zoom). Implemented in pure Solidity bytecode using fixed-point Q16.16 arithmetic (this http URL), Werracle evaluates a 16-point Pareto micro-grid in only 21,438 gas (under 0.0005 USD on Layer-2 rollups like Base and Arbitrum) with sub-millisecond execution latency. We demonstrate real-world DeFi efficacy via this http URL, a Uniswap v4 dynamic swap fee governor that measures orderbook turbulence on-the-fly and atomically adjusts liquidity provider fees between 0.05% and 0.50%. The protocol is formally verified against a 1,000-test cryptographically sealed deterministic verification suite (100.0% pass rate) with telemetry permanently disabled, operating live on a dedicated EVM devnet sandbox (Chain ID 4242).

---


### 69. [When 10,000 Windows Are Not 10,000 Tests: Auditing Statistical Confidence in Sliding-Window Time-Series Classification](https://arxiv.org/abs/2609.30721)

**<font color=#1a73e8>作者：</font>** Xinze Shi, Litian Zhang, Binrui Shi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sliding-window classifiers are often evaluated on thousands of overlapping test windows, even though neighboring predictions share observations and remain nested within recordings and subjects. Subject-disjoint evaluation prevents one form of leakage but does not make those test windows independent. We present a practical audit that maps three claims - performance on observed recordings, future recordings from observed subjects, and unseen subjects - to explicit aggregation rules and established dependence-robust inference. At 75% overlap, controlled simulations give 16.9% Type-I error for IID observed-record inference and 7.2% for session-centered Bartlett-HAC: a substantial improvement with residual miscalibration. Audits of frozen WISDM and HARTH predictions show that nearly fourfold growth in test rows yields only 1.75-1.94-fold variance-equivalent information growth. At that overlap, fixed-record paired Accuracy-difference intervals are 1.22-1.66 times the IID widths; this inflation is not universal at zero overlap. On HARTH, paired Accuracy-difference intervals include zero across three overlap settings, whereas Macro-F1 favors MiniROCKET. Independent recomputation, common-session checks, class-level results, and separately seeded calibration make the audit's scope and limitations inspectable. The resulting workflow distinguishes additional predictions from additional independent evidence.

---


### 70. [TrafficImag: A Benchmark for Counterfactual Roadside Traffic Video Generation](https://arxiv.org/abs/2609.30722)

**<font color=#1a73e8>作者：</font>** Xiangyu Li, Tianyi Wang, Zhihao Dou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing roadside traffic datasets support perception, forecasting, and visual question answering, but they do not evaluate counterfactual video generation, in which a selected actor is modified and the generated future should remain consistent with road topology and unrelated traffic. We introduce TrafficImag, the first benchmark for counterfactual roadside traffic video generation. TrafficImag combines a large-scale roadside dataset (9,022 annotated images, 7,043 deduplicated video clips, and 31,145 actor-centered history-future samples) with an executable protocol that supports behavior reasoning, intervention-aware image editing, and conditional video generation. Each intervention is represented as an actor-level program describing the target actor, intended behavior, legal route, interaction order, and temporal constraints, enabling a unified evaluation interface across heterogeneous foundation models. TrafficImag evaluates four complementary validity dimensions: initial-state correctness, route and behavior validity, interaction consistency, and non-target preservation, and considers an end-to-end counterfactual successful only when all four are satisfied. Across state-of-the-art foundation models, the strongest reasoner reaches 80.4% macro F1, the complete condition interface raises end-to-end success from 23.3% to 55.0% for the best generator. Oracle studies further show that conditional video execution is the primary remaining bottleneck. TrafficImag provides a reproducible benchmark for evaluating and diagnosing counterfactual traffic video generation beyond perceptual video quality.

---


### 71. [Input-Layer Starvation: Why Per-Layer Pruning Breaks IoT Intrusion Detectors](https://arxiv.org/abs/2609.30729)

**<font color=#1a73e8>作者：</font>** Md Anas Biswas  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Intrusion detectors for small Internet-of-Things (IoT) devices are usually compressed by pruning and judged by overall accuracy. We show that this hides a severe class-level failure, find its cause, and give low-overhead prevention and repair. On CICIoT2023, a two-layer convolutional detector pruned with uniform layer-wise magnitude pruning at 80% sparsity loses 16 points of accuracy but half of its macro-F1, the mean per-class F1 (0.542 to 0.271 over five independently trained models); 17 of 34 classes are materially damaged. Remaining weight count does not explain it: a perceptron and a transformer pruned to the same or fewer weights lose at most 0.096. The first layer does. It has 192 weights; uniform pruning leaves 38, 46% of its 64 filters lose every input weight, and fine-tuning under that starvation leaves the running means of the first normalisation layer displaced by up to 0.8 standard deviations in a few surviving channels, on which the deployed model collapses. Protecting those 192 weights, or pruning globally at the same sparsity, prevents the collapse (loss 0.013); recomputing the normalisation statistics on unlabelled training data, with no weight changed, repairs it (loss 0.039) and returns the false-alert rate to 33% (dense 29%). Damage shows a strong increasing dose-response in first-layer sparsity, starving a perceptron's input layer reproduces the collapse, and the pattern holds on TON_IoT. The failure is misattribution and false alerts, not silent evasion: on validation-selected blind spots, uniformly pruned detectors misattribute 72% of the traffic, against 50% with the first layer protected and 47% for the dense model.

---


### 72. [Amplify What You Gaze At: Target Saliency Boosting in Text-to-Image Generation](https://arxiv.org/abs/2609.30733)

**<font color=#1a73e8>作者：</font>** Shengqi Dang, Zhengxi Yu, Feilin Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image generation has advanced in controlling what, where, and how objects appear, yet how visual attention is distributed among objects remains largely unexplored. In this paper, we introduce Target Saliency Boosting, a new task aimed at boosting the visual saliency of a specific object during text-to-image generation without requiring any visual priors. Our key insight is that visual saliency is inherently relative: boosting the saliency of a target object also depends on the global saliency distribution across all objects in the scene. Based on this insight, we propose GazeME, a lightweight framework that uses saliency-marked prompts, inserting learnable marker tokens around object descriptions to indicate which objects to visually emphasize or suppress. To learn these markers, we construct a saliency-semantics dataset that associates objects in image--prompt pairs with object-level saliency scores, and propose Saliency Prior Marker Activation (SPMA), a saliency-aware stochastic marker activation strategy that exploits relative saliency relationships for robust training. During inference, GazeME automatically inserts appropriate markers into the prompt, thereby directly enhancing the visual saliency of the target object. Extensive experiments demonstrate that GazeME effectively boosts target saliency while preserving both semantic alignment and image quality.

---


### 73. [SEA-CLIP-Tiny: Efficient Multilingual Text-Vision Embedding for Southeast Asian Languages](https://arxiv.org/abs/2609.30739)

**<font color=#1a73e8>作者：</font>** Puja Ahmad Habibi, Faiz Assabil Firdaus, Ashvanth S 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual text-vision embedding models are essential for cross-lingual image-text retrieval, but Southeast Asian languages remain poorly supported due to the region's linguistic diversity and limited data and computing resources. In this paper, we introduce SEA-CLIP-Tiny, a compact multilingual text-vision embedding model for Southeast Asia with fewer than 50M parameters. Our model adapts a CLIP-KD-style framework to Southeast Asian multilingual settings through regional data curation and multilingual teacher guidance. Experiments across seven Southeast Asian languages show that SEA-CLIP-Tiny achieves the strongest average retrieval performance among the evaluated student models, reaching 12.9%, 31.5%, and 42.2% at R@1, R@5, and R@10, respectively. Compared with MobileCLIP2, it improves average R@10 by 12.1 points while using 38.4% fewer parameters and lower measured CPU latency. These results highlight the importance of region-aware training for efficient multilingual text-vision models in Southeast Asia.

---


### 74. [From Mono to Stereo: Accelerating Binocular Gaussian Splatting via Reprojection and Selective Patching](https://arxiv.org/abs/2609.30741)

**<font color=#1a73e8>作者：</font>** Hongfei Zhu, Ling Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Binocular rendering requires two nearby views of the same scene and therefore repeats substantial visibility and shading work. We present a 2D Gaussian Splatting (2DGS) pipeline that fully renders a dominant-eye RGB image and an alpha-weighted depth proxy, reprojects that image to the affiliated eye, and repairs uncovered pixels. Small interior gaps are interpolated, whereas larger disoccluded regions are identified as regions of interest (ROIs) and selectively re-rendered. The depth proxy reuses the alpha-blending weights computed during dominant-eye rasterization, avoiding a separate depth-rendering pass. An adaptive ROI generator localizes the required updates using reprojected image boundaries and optional connected center-hole detection. On DTU, Tanks and Temples, and MipNeRF-360, the method reduces the measured time of a sequential two-pass binocular reference by 15.5\% to 28.8\% and peak GPU memory by 6\% to 11\%. The corresponding affiliated-eye quality degradation is at most 1.3 dB PSNR, 0.02 SSIM, and 0.02 LPIPS, representing a measurable trade-off that requires application-specific perceptual validation. These results establish a practical efficiency-quality trade-off for controlled static-scene stereo rendering and motivate future evaluation under continuous motion and on physical VR hardware.

---


### 75. [From S3Q Theory to Implementation: Towards an Architecture for Machine Qualia](https://arxiv.org/abs/2609.30743)

**<font color=#1a73e8>作者：</font>** Tetiana Grinberg, Katrina Schleisman, Patryk Laurent 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A key challenge in machine consciousness research is translating theoretical models into computational-level implementations. In this paper, we address this challenge by proposing a five-layer implementation architecture for the S3Q (Simulated, Situated, Structurally Coherent) theory of consciousness. Rather than introducing novel formalisms, the architecture composes published computational primitives into a single pipeline. S3Q identifies three jointly necessary conditions for qualia: (1) grounded sensorimotor situatedness, (2) internal simulation via a world model, and (3) structural coherence between predictions and observations. No existing computational system implements all three simultaneously. We map each S3Q tenet to specific, compatible computational machinery and specify how these components interface within a single representation pipeline that operates on continuous, differentiable, per-object slot vectors, along with a developmental bootstrap sequence and falsifiable predictions for the composed system that no subset of the architecture produces in isolation. The model suggests that a basic sense of "self" develops by linking actions to their outcomes, and that behavior falls into three patterns (hesitation, curiosity, or avoidance) depending on how unexpected an outcome is and whether it is experienced as positive or negative. Each prediction is individually falsifiable, providing the field with a testable framework to advance our understanding of machine consciousness.

---


### 76. [Mechanism-Aware Ensemble Conditioning for Data-Limited Emulation of Extreme Events](https://arxiv.org/abs/2609.30746)

**<font color=#1a73e8>作者：</font>** Isabella S. Thiel, Juan Bello-Rivas, Yannis G. Kevrekidis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Extreme events in chaotic systems are difficult to learn from short trajectories because they are controlled by transient finite-time instability rather than by frequently observed bulk dynamics. We propose a mechanism-aware conditioning plug-in framework that turns a nudged coarse ensemble into a non-intrusive sensor of local instability geometry. In the small-noise regime, the ensemble covariance aggregates the same finite-time deformation kernels that govern local instability, providing a Jacobian-free proxy for the local amplification structure around a synchronized coarse trajectory. A small FiLM module injects statistics of this ensemble geometry into an otherwise unchanged backbone while leaving the coarse simulator unchanged. We demonstrate this interface in two distinct pipelines: a Transformer-style residual-attention corrector for a controlled low-dimensional chaotic system and a probabilistic recurrent STORN corrector for topographic two-layer quasi-geostrophic (QG) flow. In the low-dimensional benchmark, ensemble covariance directions co-activate with OTD modes and FiLM conditioning improves 99th-percentile exceedance-frequency errors over an identical no-context Transformer baseline. In QG, a fixed ensemble-conditioned FiLM-STORN model trained on only \(50\) time units substantially improves long-horizon rare-event statistics in the data-limited regime, including density-tail errors, exceedance frequencies, and spatial exceedance-area distributions relative to an unconditioned STORN trained on the same data; on averaged high-threshold exceedance diagnostics, it also outperforms the baseline STORN trained with $20$ times more high-resolution data. These results show that local instability geometry is not merely interpretable post hoc, but an actionable conditioning signal for data-efficient rare-event emulation.

---


### 77. [Differentiable RNA Secondary Structure Extraction for Deep Learning](https://arxiv.org/abs/2609.30752)

**<font color=#1a73e8>作者：</font>** Tyler Illman, Max Ward, Marcell Szikszai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many deep learning approaches to RNA secondary structure prediction have recently been proposed. They typically output a weight matrix $W$ where $W_{ij}$ is an arbitrary weight for base $i$ pairing with base $j$. Converting this matrix to a predicted secondary structure or base-pairing probability matrix typically involves ad hoc and problematic downstream algorithms. Despite the importance of this conversion step, which we refer to as structure extraction, it has received relatively little attention in the literature. In this work, we analyze how the congruence between training and extraction methods affects prediction performance. To do this, we compare four extraction algorithms: a Nussinov-like dynamic programming method, maximum-weight graph matching and the greedy extraction algorithms used by SPOT-RNA and RiNALMo. These are evaluated on outputs from the pretrained RiNALMo model and three toy models trained in this paper: a differentiable Nussinov-like model, a binary cross-entropy (BCE) baseline, and a model that incorporates a novel symmetric doubly stochastic matrix (SDSM) normalization algorithm during training which allows it to output base-pairing probability matrices directly, without a separate extraction step. This SDSM normalization algorithm is differentiable and can be added inline to any deep learning model during training and evaluation. We find that the performance of each extraction method depends strongly on how the corresponding model was trained. Considering the toy models themselves, the SDSM model showed the strongest overall performance: it outperformed the BCE baseline under all four extraction algorithms and produced pre-extraction outputs closest to the ground truth. These results suggest that SDSM normalization is a tractable alternative to traditional structure extraction.

---


### 78. [Skill Profiling with Attributable Reasoning (SPAR): A Wearable Analysis System for Boxing](https://arxiv.org/abs/2609.30753)

**<font color=#1a73e8>作者：</font>** Nibraas Khan, Hanchen David Wang, Enya Bullard 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> A punch is a ballistic, full-body action driven by a kinetic chain running from the legs through the trunk to the arm, where a small sequencing error separates a scoring strike from a miss. Wearable sensors can capture this movement in the gym, but most deployable systems only classify which punch was thrown rather than assess how well it was thrown. We present Skill Profiling with Attributable Reasoning (SPAR), an eight-IMU garment and pressure-insole system that classifies each punch as expert or novice and treats an explanation of that prediction as feedback. Feedback is only useful if the person receiving it can act on it, so SPAR explains the prediction at three tiers, a per-joint attribution for the analyst, a counterfactual over kinetic-chain layers for the coach, and a plain-language narrative of the two for the athlete. Across 17 participants and 4,713 punches, SPAR reaches a leave-one-participant-out AUC of 0.842 (95% CI [0.769, 0.907] over participants). A frozen time-series foundation model encodes the joint-angle and plantar-force series, and a small transformer trained on the cohort classifies the encoding. We audit the two quantitative tiers and report six themes from a thematic analysis of interviews with six practicing boxing coaches.

---


### 79. [Training-Free Bottleneck Width Planning for Convolutional Autoencoders](https://arxiv.org/abs/2609.30755)

**<font color=#1a73e8>作者：</font>** Guannan Guo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multiscale Spectral Rate-Distortion (MS-SRD) estimates the bottleneck channels required at user-supplied spatial cuts from training images and a normalized mean-squared error (NMSE) bound, without fitting a neural network. Its covariance-tail rule is exact for shared linear block-convolutional autoencoders under squared error. A nested-scale dominance result motivates reporting the activation-parameter Pareto frontier alongside the minimum-latent candidate. At NMSE <= 0.01 on thirteen grayscale datasets, its latent-size prediction has 0.84% mean absolute percentage error against nonlinear patch-autoencoder boundaries; ten predictions are exact and the remaining three differ by one channel. In a four-dataset deployable comparison, MS-SRD matches all retrospective external widths and all four selected models pass, without training a selector; a 46-fit validation grid and four Least-Volume fits each pass on two datasets. In a skip-closed U-shaped autoencoder at the same bound, five predictions are exact, nine are within one channel, and every failing prediction is one channel short. Experiments at looser bounds show progressively larger nonlinear savings.

---


### 80. [Selective Amortization of Full-Budget Counterfactual Reasoning for Visual Token Communication](https://arxiv.org/abs/2609.30756)

**<font color=#1a73e8>作者：</font>** Qinglei Qi, Zhihe Liang, Fengzhan Jing 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative image communication transmits compact semantic tokens under a limited packet budget, where token selection directly affects the final reconstruction quality after the complete packet is decoded. However, accurately estimating the terminal value of every candidate token requires repeated receiver-side reconstruction, resulting in substantial encoder-side computation. To address this problem, we propose ACV-Gate, an adaptive candidate evaluation framework that learns to approximate full-budget counterfactual evaluation and selectively assigns exact evaluations to the most informative candidates. Specifically, a set-aware student is trained using terminal advantages and regrets to predict candidate rankings directly, while a selective refinement mechanism evaluates only a bounded candidate set containing both Local-MDL and direct actions; cost-based thresholds further enable explicit control of the average evaluation workload. Experiments on CIFAR-10 show that ACV-Gate consistently improves reconstruction quality while substantially reducing candidate evaluations; at 0.20 bpp, the primary adaptive configuration improves PSNR over LocalMDL by 0.636 dB with only 2.13 candidate evaluations per image, corresponding to 27.60% of the calls required by the Exact-Full expert. Matched-candidate comparisons, synchronized GPU measurements, and evaluations on STL-10 and 384 *384 scale transfer further demonstrate consistent quality computation trade-offs, with particularly pronounced gains at low bit rates. These results show that combining terminal-value learning with selective candidate evaluation provides an effective and controllable mechanism for allocating encoder computation in packet-constrained generative image communication.

---


### 81. [LLPR: Location-aware learning and physics-based reconstruction for raindrop removal from a single image](https://arxiv.org/abs/2609.30758)

**<font color=#1a73e8>作者：</font>** Zewei He, Xingyu Liu, Xing Luo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Raindrops can cause occlusion and distortion in the background scenes due to their adherence to windows or camera lenses. Existing raindrop removal methods concentrate on designing sophisticated CNN or Transformer architectures to recover distorted and missing texture. In this paper, we try to integrate location information and physical model into off-the-shelf CNN or Transformer architectures to help improve their performance. Specifically, we notice that existing methods deploy a preprocessing sub-network to generate a binary or soft mask to indicate the raindrop location, which will increase the network parameters and computational complexity. In contrast, a location-aware learning branch is embedded to teach the encoder in the training phase with the capability of perceiving the position of the raindrops. Note that this location-aware learning branch can be removed during the inference process (achieving performance improvements at no cost). Furthermore, instead of directly reconstructing the raindrop-free image (i.e., background scene), we devise a physics-based reconstruction scheme to first learn the transparency matrix and the raindrop layer. The latent background layer is then reversely derived based on the physical model. By combining the above-mentioned components, we propose our location-aware learning and physics-based reconstruction (LLPR) framework for this challenging ill-posed problem. We also collect a real-world raindrop-degraded image dataset, which is challenging for single-image raindrop removal (SIRR) methods. Extensive experimental results demonstrate the effectiveness and generality of our LLPR framework, achieving superior performance against state-of-the-art SIRR methods. The code will be made available upon acceptance.

---


### 82. [Timo: $\textbf{T}$aming Mult$\textbf{i}$modal Diffusion Transformer for Human $\textbf{Mo}$tion Generation](https://arxiv.org/abs/2609.30761)

**<font color=#1a73e8>作者：</font>** Zhao Wang, Jiangtao Hu, Jack Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most existing human motion generation (HMG) methods use cross-attention modules to inject text semantics, but ignore the importance of bidirectional modeling between motion and text tokens, which limits text comprehension. A straightforward idea is introducing multimodal diffusion transformers (MMDiT), which have shown effective joint text--visual modeling in vision generation, into HMG. However, we find that articulated motion is temporally coherent but weakly correlated across joints, in which directly applying an MMDiT with flow matching produces poorly coordinated and jerky motion. In this work, we propose Timo, a novel kinematics-aware MMDiT framework tailored for HMG. Timo combines fully shared multimodal attention for bidirectional text--motion modeling with flow matching, geometric and rotational-kinematics supervision that compares actual rotations and their changes over time, and a two-stage curriculum progressing from broad motion learning to detailed caption alignment. Further, we construct a benchmark of $40{,}025$ held-out clips from six public datasets spanning diverse actions, assessing six complementary dimensions under a common evaluator and scoring protocol. Our model substantially outperforms state-of-the-art methods in both quantitative and qualitative evaluations. Remarkably, Timo surpasses Kimodo on five of six dimensions, achieving a $40.8$% relative improvement in the average benchmark score. Project page: this https URL. Demo page: this https URL.

---


### 83. [Insurance Reserve Intelligence Platform](https://arxiv.org/abs/2609.30765)

**<font color=#1a73e8>作者：</font>** Anugya A, Saket Mohanty, Abhilash Timmapur 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Insurance reserve estimation is a fundamental actuarial task supporting premium pricing, solvency assessment, financial reporting, capital planning, and risk management. Classical reserve methods based on Thiele's differential equation provide a rigorous and interpretable foundation for life insurance valuation, but repeated reserve calculations become computationally expensive in sensitivity analysis, optimization, and large-scale scenario evaluation.
This paper presents an Insurance Reserve Intelligence Platform for term-life reserve modelling that combines a classical Thiele-equation solver with a Physics-Informed Neural Network (PINN) enhanced by Knowledge-Informed Neural Network (KINN) losses. The framework includes synthetic policy generation, risk-adjusted premium calculation, classical reserve trajectory generation, reserve-ratio dataset construction, configurable neural training, validation diagnostics, sensitivity and elasticity analysis, prototype optimization workflows, and interest-rate scenario testing. A key refinement is the use of premium ratio and the explicit separation of pricing-time and scenario-time interest-rate semantics.
The final model uses seven features: elapsed time, issue age, pricing interest rate, scenario interest rate, premium ratio, sum assured, and mortality intensity. It predicts a standardized reserve ratio instead of raw reserve values, improving numerical stability across policies with different sums assured. The model achieved an R2 of 0.9887, MAE of 785.48, and RMSE of 1212.76 on the test set. On 200 policies, PINN/KINN inference was approximately 119.53 times faster than the classical solver. Results show strong predictive accuracy, physics consistency, and boundary performance, while highlighting remaining limitations in monotonicity and out-of-distribution generalization.

---


### 84. [Query-Conditioned Prototype Adaptation for Cross-Domain Few-Shot Learning: Single-Query Inference, Controlled Comparisons, and Failure Modes](https://arxiv.org/abs/2609.30769)

**<font color=#1a73e8>作者：</font>** Rushab Rasik Karania, Tomas Maul  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-domain few-shot learning requires adapting a classifier to a new visual domain from very few labelled examples without target-time parameter updates. We isolate one question: under a fixed global representation, what does joint query-support adaptation contribute to prototype construction? The Within-Instance Prototypical Transformer (WIPT) implements single-query test-time prototype adaptation by jointly transforming one unlabelled query and the labelled support embeddings, then forming query-specific class means. Using a shared frozen ViT-S/16 encoder, miniImageNet source training, and CUB, EuroSAT and ISIC targets, we replicate the key comparisons across five independent training seeds. In 1-shot evaluation, WIPT improves frozen ProtoNet in every run on CUB (+0.21 percentage points) and EuroSAT (+2.07), but decreases ISIC (-0.22). In 5-shot evaluation, ProtoNet remains strongest overall, while WIPT consistently improves a capacity-matched support-only Transformer on ISIC (+0.99). Joint processing of up to five queries yields no reliable accuracy gain; in a head-only 5-shot benchmark, g = 5 reduces analytical attention-token pairs by 73% and peak allocated memory by 29% relative to g = 1, although latency is non-monotonic. Across all target/shot conditions, WIPT changes uncertain ProtoNet decisions far more than confident ones, and rescue/break decomposition accounts for the observed gains and losses. Source-shift and scorer controls further show that the benefit is not universal. Overall, WIPT provides a streaming-compatible form of test-time prototype adaptation that can improve difficult low-shot cross-domain decisions without target-time optimization.

---


### 85. [Sampling Safe Futures: Multimodal Trajectory Planning for Personalized Safety in Anthropomorphic AI](https://arxiv.org/abs/2609.30780)

**<font color=#1a73e8>作者：</font>** Benedetta Picano, Dusit Niyato  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Anthropomorphic artificial intelligence systems increasingly remember personal details, display empathy, and are engaged with as social counterparts, creating forms of risk that emerge from the evolution of the user-system relationship over time. Existing safeguards largely operate at the level of individual conversational turns and cannot determine whether a sequence of seemingly acceptable interactions is cumulatively moving a particular user toward harm. This paper introduces personalized trajectory-level safety, a framework that treats relational safety as a sequential decision problem over a latent escalation state inferred from the user's messages and influenced by the system's responses. At each turn, a screening step first discards any response strategy that does not preserve at least one safe continuation of the interaction under every plausible model of the user. Among the remaining strategies, we formulate action selection as multimodal trajectory sampling, and use a Generative Flow Network to generate diverse future evolutions in proportion to their plausibility, safety, and utility. The system then selects the strategy that preserves the largest fraction of safe and useful continuations. We evaluate the framework in simulation, calibrated on statistics reported for real human-chatbot interactions, and using response strategies derived from public benchmarks. Results show that trajectory-aware decision making substantially reduces the frequency of harmful states while keeping helpful interaction. This work reframes safety for anthropomorphic AI from response-level filtering to personalized control over the future evolution of human-AI relationships. The source code is available at this https URL.

---


### 86. [Missingness-Aware Conformal Prediction Under Cross-Hospital Distribution Shift](https://arxiv.org/abs/2609.30781)

**<font color=#1a73e8>作者：</font>** Liang You, Dongwen Ou, Hengyu Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical measurements are recorded for some patients but not others, at rates that differ across hospitals, and marginal conformal coverage does not ensure coverage within groups defined by missingness. We propose a missingness-aware conformal calibration procedure for mortality prediction under cross-hospital distribution shift. It selects a measurement on an independent sample, groups patients by whether that measurement is recorded, and applies Mondrian calibration within each group, so no calibration outcome is reused. We evaluate the procedure across hospitals in eICU and across care units within one MIMIC-IV hospital, using three predictors. Relative to pooled calibration, it reduces the average worst-group coverage gap on its selected groups in all six settings, with a median reduction of 1.9 percentage points; paired site-bootstrap intervals exclude zero in five. These gains do not extend uniformly. Calibration by predicted risk achieves smaller gaps on a broader panel of missingness groups, and when eICU hospitals are evaluated separately, the gain shrinks for all three predictors and reverses in sign for one. We explain this discrepancy with a hospital-level decomposition. Pooling reweights hospitals through a covariance between group shares and coverage errors, and lets errors of opposite sign cancel: weighting explains the reversal, and cancellation accounts for most of the attenuation for the other two predictors. Constructed population distributions show that pooled and within-hospital evaluations can rank calibration methods oppositely even without sampling noise. Pooled improvement alone therefore cannot establish better coverage within hospitals, even when the calibration groups are fixed.

---


### 87. [Interpretable-by-Design Descriptor Portfolios Match a 2048-Dimensional Foundation Embedding on Low-Data Molecular Assays](https://arxiv.org/abs/2609.30789)

**<font color=#1a73e8>作者：</font>** Yiqi Yao, Miquel Duran-Frigola  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In low-data structure-activity prediction, the choice of molecular representation can matter more than the choice of predictor, and tabular foundation models sharpen that effect. We ask whether a portfolio of compact, semantically named descriptor blocks can reach the accuracy of a 2048-dimensional CheMeleon embedding while staying auditable at the feature level, meaning that every input dimension carries a model name and a recorded training provenance. Starting from a fixed 11-dimensional physicochemical base, we greedily concatenate provenance-screened blocks using the labelled context alone. Across nine ADME/Tox assays and 50 evaluation cells, scored on common-coverage subsets restricted to the molecules that every representation covers, the portfolio reaches a mean test AUC of 0.762, against 0.764 for CheMeleon and 0.756 for Mordred. The pooled gap to CheMeleon is +0.003 AUC (task-bootstrap 95% CI [-0.020, +0.030]), which satisfies our predeclared pooled parity gate but not the per-assay gate. At 25 context labels the headline rule again satisfies the pooled gate; at 10 labels it does not. We also report four predeclared candidate-selection rules that we falsified. Post-freeze checks over ten seeds and three previously unseen assays support pooled competitiveness for compact, auditable representations; a same-width random-bundle control does not establish that greedy membership itself adds accuracy. Assay-level differences remain unresolved.

---


### 88. [Towards Universal Representation-Based Process Control](https://arxiv.org/abs/2609.30790)

**<font color=#1a73e8>作者：</font>** Jinmyeong Choi, Taesup Kim, Artur Dubrawski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many temporal process learning and monitoring pipelines operate in local windows, making window-level decisions unavoidable in practice. In such settings, classical statistical tests can be applied to individual windows, but they typically evaluate predefined parametric hypotheses-such as unit-root or moment-based conditions-thereby limiting flexibility when reference behavior is defined empirically from task- or domain-specific data. In this work, we view window-level monitoring as a process control problem and reformulate it as reference-based hypothesis testing, where the null hypothesis is specified by an empirical reference distribution rather than a fixed parametric model. We operationalize this perspective through a representation-based, nonparametric framework that combines pretrained time series encoders, kernel density estimation, and conformal calibration, yielding finite-sample valid inference in learned representation space. Classical notions such as stationarity and cyclostationarity arise as natural instantiations of empirical reference sets within this framework. Through experiments, we demonstrate sensitivity to window-level distributional deviations while maintaining well-calibrated inference under stable reference regimes, highlighting the applicability of the proposed approach to a broad class of time series process control and monitoring tasks.

---


### 89. [Motion Style Slider: Endpoint-Supervised Continuous Style Control for Human Motion Diffusion](https://arxiv.org/abs/2609.30795)

**<font color=#1a73e8>作者：</font>** Chen-Chieh Liao, Yichen Peng, Yiyi Cai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing human motion diffusion methods provide strong motion generation quality, and recent style transfer models can inject target style cues, but fine-grained continuous control of style intensity remains underexplored. In production, style intensity is subjective across artists and directors, so the practical requirement is not a universal absolute unit, but a reliable monotonic control axis. We propose Motion Style Slider, a motion-to-motion style transfer framework for endpoint-supervised continuous control. Given a content motion and a style motion, we construct a style direction in a learned motion-style embedding space and condition diffusion generation with a scalar intensity. The training objective combines diffusion denoising with latent intensity regularization to encourage smooth and monotonic style scaling without requiring intermediate-intensity ground-truth motions. Our framework is compatible with pretrained motion diffusion backbones and supports heterogeneous style datasets, including the multi-actor style motion dataset. To test out-of-range usability, we additionally introduce a small real-capture over-reaction extension and evaluate large-intensity behavior against these unseen targets. Experiments measure controllability, interpolation/extrapolation behavior, content preservation, and motion realism, with ablations on direction construction and loss design.

---


### 90. [Evaluating Real-Time Voice Agents: From Component Quality to Grounded Outcomes](https://arxiv.org/abs/2609.30798)

**<font color=#1a73e8>作者：</font>** Shivam Negi, Arpit Rawat, Rashi Jain  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-time voice agents have moved from research prototypes to production deployments, yet the literature describing them is fragmented across three communities that rarely cite one another: speech foundation modelling, turn-taking psycholinguistics, and agentic evaluation. Architecture papers report latency, turn-taking papers report prediction accuracy, and agentic benchmarks report task success, so no single number describes whether a deployed agent is actually good. We address that gap with three evidence-based claims, each traceable to a corpus of 38 primary sources organised into an application-centric taxonomy of six categories. First, architecture choice is a deployment constraint rather than a settled verdict: a 2026 enterprise tutorial reports that no fully self-hostable end-to-end system yet meets production constraints, while a chunked cascade independently reaches state-of-the-art duplex behaviour, showing duplex behaviour is separable from duplex architecture. Second, evaluation has shifted decisively from component quality toward grounded outcomes, with recent benchmarks verifying backend state rather than trusting what the agent claims to have done. Third, the dyadic assumption in most models and benchmarks is breaking down: multiparty turn-taking and multi-speaker reasoning benchmarks show that deciding when not to speak, and reasoning about who may be told what, are first-class capabilities two-participant framings cannot measure. For each source we state the problem it targets, its mechanism, and its reported evidence, alongside the search strategy, inclusion criteria, and a verification step that caught a misattributed arXiv identifier in circulation. We propose TRG (Timing-Recovery-Grounded), a reporting standard characterising an agent by timing, post-disruption recovery, and state-verified outcome together, with a conditional fourth axis for multiparty deployments.

---


### 91. [XPhysICS: Cross-Physical-Domain Threat Grounding for Industrial Control Systems Security](https://arxiv.org/abs/2609.30805)

**<font color=#1a73e8>作者：</font>** Sangshin Park, Jainta Paul, Lawrence Ponce 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Industrial control system (ICS) threats documented for one plant can express cyber-physical effects relevant to another, but semantic similarity alone does not establish whether those effects are structurally admissible or evaluable on a target. We present XPhysICS, a provenance-aware, target-conditioned method that separates analyst-guided source abstraction from deterministic grounding into target-specific validation slices. Given a fixed source abstraction, vocabulary and schema, and machine-validated target contract, XPhysICS evaluates candidate mappings using five eligibility criteria: role compatibility, implemented type compatibility, stage coherence, slice viability, and rule-surface applicability. Grounding acceptance, slice adequacy, dynamic realizability, consumer applicability, and consumer outcome remain distinct evidence layers. We evaluate 83 structured source-threat abstractions across water treatment, water distribution, hydro/water-energy, and chemical-process targets. Controlled target-side studies of SWaT-to-water-treatment and WADI-to-water-distribution groundings produce clean, nominal-confounded, and near-threshold consumer outcomes; nine Hydro/GRFICS cases extend bounded validation-slice execution. We also evaluate bounded predictive, state-aware, and phase-aware consumer lanes, the unmodified upstream GeCo implementation, and a paper-derived reproduction of a physics-guided search method over three frozen groundings. Results show that cross-domain ICS threat reuse requires traceable source semantics, explicit target-conditioned grounding criteria, and careful separation of subsequent target-side evidence.

---


### 92. [Counterfactual Online Conformal Prediction Under Adaptive Logging](https://arxiv.org/abs/2609.30811)

**<font color=#1a73e8>作者：</font>** Xinyu Qiao, Yichen Lin, Kaihong Ji 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online conformal prediction can fail when predictions shape actions and actions determine which outcomes enter calibration. Standard adaptive methods may retain marginal coverage while systematically miscovering the counterfactual outcomes of rarely selected actions. This paper formalizes the failure through counterfactual coverage and introduces Propensity-Weighted Online Conformal Prediction, an inverse-propensity-weighted recursion that debiases calibration. A doubly robust variant further reduces nuisance bias to the product of outcome-model and propensity errors. Under positivity, the resulting coverage rate matches an information-theoretic lower bound up to logarithmic factors. Experiments on synthetic decision tasks, open bandit data, and financial rebalancing show that PW-OCP and DR-OCP improve counterfactual coverage and downstream regret without sacrificing prediction-set sharpness.

---


### 93. [Learning Provable Neural Network Observer for Uncertain Dynamical Systems](https://arxiv.org/abs/2609.30819)

**<font color=#1a73e8>作者：</font>** Zhangyi Wang, Jiaxu Liu, Chen Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many safety-critical applications, control of uncertain dynamical systems relies on observers that estimate states and external disturbances. Neural network observers can improve estimation accuracy, but certifying their Lyapunov stability via Linear Matrix Inequality (LMI) constraints leads to large-scale semidefinite programs (SDPs) that are difficult to solve for large networks. To overcome this scalability bottleneck, we propose a novel two-stage training framework for provably stable neural network observers. Our approach decouples the optimization into a point-guided Lyapunov pre-training phase, which rapidly achieves high estimation accuracy and local stability over sampled states, followed by an LMI fine-tuning phase that efficiently satisfies a strict global Lyapunov stability certificate. We provide formal theoretical guarantees for local stability radii and probabilistic coverage over a prescribed compact error-state domain under specified regularity and sampling assumptions. Experiments on nonlinear control benchmarks and X-29 aircraft ablations show that our LMI-certified neural network observers train significantly faster than direct LMI-based methods and generalize robustly across diverse systems, achieving improved tracking accuracy over a range of observer baselines. The code is available at this https URL.

---


### 94. [Adaptive Interaction Graphs for Particle Simulation](https://arxiv.org/abs/2609.30822)

**<font color=#1a73e8>作者：</font>** Aiden Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learned particle simulators based on graph neural networks achieve strong one-step accuracy, but errors compound over long horizons. An underexplored variable is the interaction graph: existing methods fix its topology via k-nearest neighbors or a static radius rule, regardless of local model confidence. We propose making this graph adaptive: a per-particle variance head, trained jointly with the acceleration head under a heteroscedastic Gaussian NLL loss, drives a trajectory in which high-uncertainty particles receive an expanded neighborhood. This is done at little extra inference cost by using the previous step's uncertainty estimate. A key discovery is that the variance head learns a meaningful notion of uncertainty: high-variance particles concentrate near complex regions, such as splash zones or free surfaces. When this signal drives graph topology, the resulting AdaptGNS simulator achieves a strict Pareto improvement on WaterDrop and a modest gain on Sand. Given the model's stronger performance on WaterDrop, we hypothesize that adaptive graphs are most useful when complexity is concentrated in space. Our code can be found at this https URL.

---


### 95. [CDBG: Causally Motivated Dual-Invariance Learning against Topological and Predictive Shifts in EEG Workload Recognition](https://arxiv.org/abs/2609.30831)

**<font color=#1a73e8>作者：</font>** Yuzhe Zhang, Wenmin Zhou, Chengxi Xie 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generalizing Electroencephalography (EEG)-based mental workload recognition to unseen subjects remains a formidable challenge due to severe inter-subject variability. While functional brain graphs effectively model distributed cognitive dynamics, their inherent subject-specificity induces two coupled distribution shifts: a class-conditional topological shift in the underlying functional connectivity, and a predictive mechanism shift in the learned representation-to-label mapping. Motivated by the subject-induced distribution shifts, we propose CDBG, a Causally motivated Dual-invariance learning framework for Brain Graphs. CDBG disentangles and mitigates these shifts via a two-stage rationale learning pipeline. First, it employs stochastic edge masking to extract sparse, workload-predictive graph rationales, regularized by workload-conditional Laplacian spectral alignment to enforce topological invariance across subjects. Second, it applies subject-wise Invariant Risk Minimization (IRM) to the graph representations, ensuring environment-wise risk stationarity. Extensive experiments on a self-built air traffic controller EEG cognitive workload dataset and multiple public datasets under a strict leave-one-subject-out protocol demonstrate that CDBG significantly outperforms state-of-the-art cross-subject and graph-based baselines, improving the Macro-F1 score by up to 4.23%, while simultaneously providing neurophysiologically interpretable functional rationales.

---


### 96. [Peer-Grounded Counterfactual Path Planning for Chronic Health Management](https://arxiv.org/abs/2609.30838)

**<font color=#1a73e8>作者：</font>** Saman Khamesian, Hassan Ghasemzadeh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Effective behavioral intervention in chronic disease management requires not a single prescription but a sequence of incremental steps, each grounded in what real, similar individuals have demonstrably achieved. Counterfactual explanation offers a natural computational route to such guidance, answering what change in behavior would have produced a better outcome. But existing methods return a target state without a route to it, guarantee no monotone health improvement along the way, and draw no evidence from peer behavior -- asking a patient to close a wide gap in one move, which is precisely the recommendation structure least likely to be attempted. We propose POROS (Peer-Grounded Optimal Routes Over States), a domain-agnostic framework rooted in Bandura's self-efficacy theory and Festinger's social comparison theory that constructs a Behavioral Progression Graph -- a directed acyclic graph over observed patient states in which every edge requires both peer-grounded behavioral proximity and strict health outcome improvement. Every edge is therefore a behavioral change that individuals in the cohort have demonstrated is achievable within a single period. Minimum-cost paths through this graph decompose otherwise inactionable behavioral gaps into incremental, peer-grounded steps. We evaluate POROS on two independent longitudinal cohorts of patients with diabetes. For patients below the 70% clinical threshold for time in range (TIR, blood glucose within 70-180 mg/dL), it reduces the mean gain required per step from 26.3 percentage points (pp) to 5.5 pp on one cohort and from 31.1 pp to 5.7 pp on the other, decomposing large behavioral jumps into the incremental steps that self-efficacy requires. Across both cohorts, 97-98% of multi-hop paths cross patient boundaries, embedding social comparison by construction.

---


### 97. [Attention-Based Adaptive Policies for Simultaneous Speech-to-Text Translation](https://arxiv.org/abs/2609.30839)

**<font color=#1a73e8>作者：</font>** Filip Tăşădan, Ema Tomanová, Ondrej Lopuch 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Simultaneous speech-to-text translation (Simul-S2TT) consists of generating partial translations while the incoming audio frames are processed by the system. However, the streaming nature of this setup creates the challenge of deciding the best moment to perform an accurate translation while minimizing the delay. To address this challenge, we utilize the cross-attention mechanism of the encoder-decoder architecture to find the right alignment between the input speech frames and the target text tokens. In this paper, we propose the Recent Frame Attention Policy (RFAP) and the Dual-Condition Attention Policy (DCAP) that allow offline trained speech-to-text translation models to be used in streaming scenarios without requiring additional training. Results on three different language translation pairs over the CVSS-C corpus show that the RFAP is able to surpass other policies with gains of up to 4.0 BLEU while reducing the translation delay by almost 1 second. Moreover, the DCAP is able to preserve a high translation quality when the latency is very low.

---


### 98. [Aligning One-Step Generative Models with Reward-Weighted Transport Distillation](https://arxiv.org/abs/2609.30840)

**<font color=#1a73e8>作者：</font>** Austin Wang, Ziheng Cheng, Lexing Ying  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> One-step generators enable high-quality visual generation with a single network evaluation, but their post-training is difficult: general implicit generators provide neither tractable likelihoods nor denoising trajectories, and many rewards are non-differentiable. We introduce Reward-Weighted Transport Distillation (RWTD), a post-training method that requires only generated samples and scalar reward evaluations. Rather than aligning solely to the conventional reward-tilted reference distribution, RWTD constructs an adaptive target that mixes separately tilted current and reference distributions. The current component incorporates improvements discovered during training, while the reference component anchors the target to the pretrained generator. RWTD realizes this target through feature-space optimal transport and fixed-point regression. Theoretical analysis shows that the fixed-point distributions of RWTD interpolate between off-policy reward tilting of the reference and on-policy tilting of the current model, providing a principled approach to balancing reward adaptation with retention of prior knowledge. Empirically, RWTD substantially improves the GenEval score of the one-step SANA Sprint 1.6B backbone from 0.73 to 0.80, while separate preference alignment experiments demonstrate strong cross-reward generalization that yields balanced improvements and preservation of compositional capabilities.

---


### 99. [I-Parakeet: Integer-Only Conformer ASR on Mobile NPU](https://arxiv.org/abs/2609.30846)

**<font color=#1a73e8>作者：</font>** Taichi Nishimura  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose I-Parakeet, an integer-only implementation of NVIDIA's Parakeet-CTC (0.6B parameters) that runs on a smartphone NPU without any floating-point operator or CPU fallback. Modern Conformer ASR models are hard to deploy on edge devices because of their size, and quantized models still fall back to floating point for numerically sensitive operations. This prevents them from fully exploiting integer accelerators such as mobile NPUs. To achieve this, our contributions are threefold. First, we derive an integer formulation of the relative-positional self-attention at the core of the Conformer. We fuse its two score branches with different quantization scales and the relative shift into integer-only operations. Second, we introduce a minimax-optimized Swish approximation that minimizes the maximum error of the Swish output. Third, a layer-wise range analysis of activations yields two targeted remedies: an INT16 grid for the BatchNorm output and percentile calibration for the heavy-tailed pre-encoder activations. I-Parakeet achieves 4.97% WER on LibriSpeech test-other, running on a Qualcomm NPU at a real-time factor of 0.048, 7.5x faster than a CPU baseline.

---


### 100. [MDSkin-Net: Multi-Task Skin Lesion Analysis Driven by Pattern Analysis Priors and Spatial Alignment Regularization](https://arxiv.org/abs/2609.30855)

**<font color=#1a73e8>作者：</font>** Yijian Li, Saad Bedros, Paul Bigliardi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable skin lesion segmentation and classification are central to dermoscopic computer-aided diagnosis. Existing multi-task frameworks couple the two tasks architecturally without clinical knowledge, while knowledge-injecting approaches rely on the macroscopic ABCD rule, which was not designed for dermoscopy. Dermoscopic diagnosis is grounded in Pattern Analysis, a microscopic framework structured around dermoscopic features. We propose MDSkin-Net, which incorporates cue-level Pattern Analysis priors into a hybrid CNN-Transformer architecture. At its core is a Pattern Analysis-Guided Attention Module (PAGAM) comprising three priors motivated by distinct dermoscopic cues: an improved Efficient Channel Attention (iECA), a Multi-Scale Spatial Attention (MSSA), and a Biased Asymmetry Attention (BAA). We further introduce a multi-scale spatial alignment regularization (MSAR) that uses the segmentation ground-truth mask as hierarchical soft supervision, confining the classification head to lesion-localized evidence and coupling both task pathways through a shared spatial prior. Trained exclusively on the ISIC 2017 training split without external dermoscopy data, the MDSkin-Net ensemble transfers robustly under zero-shot evaluation, reaching a Dice Similarity Coefficient (DSC) of 92.38% and a melanoma AUC of 97.84%on PH2, and a DSC of 88.92% on the ISIC 2018 Task 1 test set. On the in-domain ISIC 2017 benchmark, the ensemble attains a mean Area Under the Curve (AUC) of 91.60% across the two classification tasks (melanoma and seborrheic keratosis vs. rest), and a DSC of 84.72% for segmentation. Classification remains competitive with baselines; in-domain segmentation trails single-task specialists, yet the proposed priors and alignment regularization yield representations that generalize consistently across cohorts of different scales.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-225](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
