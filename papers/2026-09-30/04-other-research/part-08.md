# 📦 其他研究 | 2026年09月30日

> 本类共 **908** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-400**（第 8/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

---

### 351. [Simulation-Free Learning of GP-SDEs from Irregular Observations](https://arxiv.org/abs/2609.33112)

**<font color=#1a73e8>作者：</font>** Zhidi Lin, Yuhao Liu, Ying Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gaussian process stochastic differential equations (GP-SDEs) provide a flexible Bayesian model for unknown continuous-time state dynamics with uncertainty quantification, but learning and inference from noisy and irregular observations remain computationally challenging. To address this issue, we propose GP-SDE Matching, a simulation-free variational framework for Bayesian GP drift learning and continuous-time state smoothing. We analytically marginalize the sparse GP posterior to derive a tractable drift-matching objective that accounts for both the posterior mean and uncertainty of the unknown drift. To handle irregular observations, we further introduce an irregular-time-aware variational state posterior that incorporates the actual observation times during both encoding and continuous-time marginal querying. Experiments on the stochastic Lorenz--63 system demonstrate substantially improved drift recovery and state reconstruction under irregular observations, while five system identification benchmarks show robust forecasting under increasing observation sparsity and competitive performance against existing latent-SDE and state-space methods.

---


### 352. [ParallelPilot: Supporting Coordination and Monitoring in Parallel AI Coding](https://arxiv.org/abs/2609.33113)

**<font color=#1a73e8>作者：</font>** Tao Long, Weili Shi, Hussein Mozannar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As coding assistants become increasingly autonomous, developers run multiple sessions in parallel, shifting the challenge from code generation alone to coordinating and monitoring concurrent agent work. Through a formative study (N=14), we identified PILOT: five supervisory practices for Planning, Isolating, Logging, Observing, and Triaging parallel sessions. We present ParallelPilot, a design probe that instantiates PILOT through a planning interface, a run-logger, and an ambient dashboard alongside existing coding tools. In a counterbalanced within-subjects study (N=16), participants using ParallelPilot increased ticket throughput by 63% in short coding tasks and supervised an average of one more concurrent agent at peak, while their tracking effort and context switching dropped. ParallelPilot also clarified execution plans, task dependencies, and intervention cues, and 14 of 16 participants preferred it over their current setup. These gains were not accompanied by significant improvements in perceived control or perceived success in redirecting the agents. Our findings demonstrate the value of explicit supervision support and position PILOT as a scaffold for designing tools that help people supervise concurrent work within and beyond coding. We suggest that future coding assistants should pair high-level awareness with low-cost paths back to the implementation evidence developers need to judge and steer agent work.

---


### 353. [Mycelium: A Generalizable Cross-Grid Multi-Task Model for Electrical Distribution Systems](https://arxiv.org/abs/2609.33120)

**<font color=#1a73e8>作者：</font>** Zhengyang Wei, Shourya Bose, Helgi Hilmarsson 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electrical distribution grid operations require inference across heterogeneous networks from sparse, noisy, and incomplete time series measurements. In this work, we identify challenges and explore solutions towards a unified model that can perform diverse tasks grounded in the physics of the electric grid and generalize to unseen distribution networks. We define a unified grid ontology that represents variable sized distribution networks as heterogeneous graphs while preserving native topology, asset types, and electrical relationships across networks. We develop a physics based data simulation pipeline that combines reference and procedurally generated distribution networks with network reconfigurations, fault scenarios, and configurable sensing conditions. We present Mycelium, a heterogeneous graph transformer with structure aware communication edges and electrical reference features that encode network position and nominal phase orientation, together with task specific temporal readouts which generate per task outputs. We train Mycelium on reference as well as synthetic grids, and study its generalization on benchmark networks completely excluded from training and validation. Mycelium is observed to outperform task specific neural baselines on most reported benchmark metrics. Architectural ablations and the aforementioned studies reveal Mycelium's capability to learn representations of the underlying physics which serves to enhance cross-task performance, thereby addressing a significant challenge in unified grid models.

---


### 354. [Policy Plasticity Matters in Offline-to-Online Reinforcement Learning: Refitting Offline Policies for Online Adaptation](https://arxiv.org/abs/2609.33127)

**<font color=#1a73e8>作者：</font>** Yuheng Huang, Yunpeng Qing, Yixiao Chi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline-to-Online Reinforcement Learning (O2O RL) has emerged as a practical paradigm that pre-trains the policy using static offline datasets and subsequently adapts the policy through online interactions. Existing O2O methods primarily address the transition through value calibration, while generally treating the offline-trained policy as a given initialization. We instead study O2O adaptation from the perspective of network plasticity, asking whether the offline-trained policy remains sufficiently adaptable for online learning. Controlled experiments show that prolonged optimization on static offline data progressively reduces network plasticity even after offline performance has largely saturated, and that lower plasticity is associated with weaker subsequent online improvement. Motivated by these observations, we propose REstoring plasticity via Fresh Initialization and policy Transfer (REFIT), a lightweight model-level method for the O2O transition. Before online fine-tuning, REFIT distills the offline policy into a freshly initialized student while temporarily freezing a random subset of student units, transferring the learned offline behavior to a more plastic policy initialization. Extensive experiments on D4RL and OGBench demonstrate that REFIT consistently achieves higher aggregate performance than existing O2O plug-in methods across both Cal-QL and IQL backbones, while plasticity diagnostics and ablations provide further evidence of restored network plasticity.

---


### 355. [Flow-Matching-Based Protein Structure Tokenizer Made Efficient and Easy](https://arxiv.org/abs/2609.33129)

**<font color=#1a73e8>作者：</font>** Zhe Zhang, Yikai Zhang, Jiangtao Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As the bridge between protein modality and discrete modeling, protein structure tokenization still largely relies on heavily engineered training objectives tailored to specific downstream tasks and large training datasets, which hinders its transfer to broader application scenarios. To address this issue, we propose ProFiT, a lightweight flow matching tokenizer. With simple training strategies that encourage healthy codebook utilization, ProFiT can be trained efficiently and naturally learns semantically meaningful representations without any manual semantic alignment, while achieving reconstruction quality and generalization that match or surpass those of substantially larger tokenizers. We conduct extensive evaluations across a wide range of settings and demonstrate that ProFiT is a plug-and-play tokenizer adaptable to diverse downstream tasks. This study further reveals the significant potential of the flow matching tokenizer paradigm. Our code is publicly available at this https URL.

---


### 356. [ILP-BO: Integer Linear Programming-Based Black-Box Optimization](https://arxiv.org/abs/2609.33131)

**<font color=#1a73e8>作者：</font>** Hyakka Nakada, Shu Tanaka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Black-box Optimization (BO) is a powerful framework for optimizing expensive objective functions or unknown functions with a limited number of evaluations. A central step of standard BO such as Bayesian optimization is the optimization of a surrogate-based acquisition criterion, which is commonly performed using nonlinear optimization or heuristic search. Therefore, conventional black-box optimization generally does not guarantee global optimality in candidate selection. In this study, we propose Integer Linear Programming-based Black-box Optimization (ILP-BO), a quasi-Bayesian optimization framework that transforms kernel-based surrogate optimization over discrete domains into an Integer Linear Programming (ILP) problem. The key idea is to represent nonlinear kernel functions exactly on finite discrete distance levels by introducing binary one-hot auxiliary variables. This transformation converts the nonlinear surrogate into a linear objective with linear constraints and binary variables. To incorporate exploration while preserving the linear structure, we further introduce a Hamming-distance margin that excludes neighborhoods around previously observed points. We derive the proposed formulation for several standard kernels and obtain an analytical upper bound on the Hamming-distance threshold based on the measure in the binary search space. The resulting candidate-selection problem can be solved by integer programming solvers with certificates of optimality. Thus, our methodology has the potential to serve as a highly transparent black-box optimization framework. Experiments on synthetic and discrete optimization benchmarks show that ILP-BO achieves competitive optimization performance compared with practical Bayesian optimization methods.

---


### 357. [Beyond the Training Horizon: Mechanisms and Limits of Length Generalization in Looped Transformers](https://arxiv.org/abs/2609.33144)

**<font color=#1a73e8>作者：</font>** Jia Liang, Xi Jin, Liangming Pan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped Transformers can generalize to reasoning chains longer than those encountered during training, but the computations enabling this behavior and limiting its extent remain unclear. We mechanistically compare two looped-Transformer configurations, which we call the Matched-Recurrence Looped Transformer (MR-Loop) and Decoupled-Recurrence Looped Transformer (DR-Loop), reflecting their respective recurrence-training schemes. We evaluate polynomial iteration, finite-state composition, and knowledge-graph traversal using detailed mechanistic analysis. Attention analysis, intermediate-state decoding, and causal interventions reveal distinct mechanisms learned under final-answer supervision. MR-Loop updates an intermediate state at a fixed readout while advancing relation selection through adjacent-token interactions and a transferable progress cue. DR-Loop instead propagates intermediate states across relation positions, forming an advancing computational frontier. However, both mechanisms become unreliable at greater depths: MR-Loop exhibits degradation of its readout state and progress cues, while DR-Loop exhibits declining reliability of state propagation. Limited self-correction allows local errors to persist and compound. Across both models, we uncover a common representational principle: recurrent states encode not only task-relevant content but also its computational status, whether that content remains in a form that can support subsequent computation. Transferable live-consumed and fresh-aged residual directions causally control whether represented information can participate in subsequent computation, including beyond the training horizon. We further show that length generalization need not rely on faithful step-by-step reasoning, as Looped Transformers can exploit task structure without explicitly representing every intermediate state.

---


### 358. [DroneWAM: Efficient World Action Model for Drone Visual Navigation](https://arxiv.org/abs/2609.33148)

**<font color=#1a73e8>作者：</font>** Liang Yao, Fan Liu, Hongbo Lu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World-action models give visual navigation agents a way to anticipate how candidate actions will change future observations and to act from the predicted consequences. For drones, this capability must operate under tight accuracy and efficiency constraints. We present DroneWAM, an efficient world-action model for drone visual navigation. DroneWAM adopts a JEPA-based architecture to model future states directly in representation space, avoiding the cost of explicit future image generation. A pretrained Resampler further compresses dense encoder features into fewer latent tokens, reducing the computation repeated at each imagined step. We also introduce adaptive rollout, where a preference-trained Gate adaptively allocates prediction depth according to the current scene. To support learning under richer aerial motion, we construct DroneNav-6D, a simulated visual navigation dataset with synchronized RGB observations, 6-DoF flight trajectories, control commands, and randomized wind disturbances. On DroneNav-6D, DroneWAM achieves the best trajectory accuracy among the compared methods. Adaptive rollout further reduces the average prediction depth from 8 to 4.58 while improving trajectory accuracy, demonstrating that predictive computation can be allocated more effectively across scenes. \href{this https URL}{Codes and data} will be released.

---


### 359. [Convergence of Practical Muon](https://arxiv.org/abs/2609.33152)

**<font color=#1a73e8>作者：</font>** Haonan Wang, Yu Wu, Minghui Liwang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon is emerging as a promising alternative to AdamW for large-scale neural network training, yet theoretical understanding of its practical implementation remains incomplete, as existing analyses often simplify or omit two key components: (i) practical Newton--Schulz iterations with empirically tuned polynomial coefficients $(3.4445,-4.7750,2.0315)$; and (ii) decoupled weight decay for regularization. In this paper, we provide an optimization interpretation and establish convergence for practical Muon, jointly accounting for both components. Specifically, we interpret practical Muon as right-preconditioned optimization of the original loss with a dynamic weighted $\ell_2$ regularizer that vanishes as stationarity is approached, so that the optimization target remains the original objective. We then establish, to our best knowledge, the first convergence guarantee for practical Muon in the stochastic nonconvex setting, with an $\mathcal{O}(T^{-1/4})$ convergence rate in terms of the expected Frobenius norm of the gradient, improving the dimension dependence of the best known AdamW's convergence rate by a factor of $\sqrt{d}$, where $T$ is the iteration horizon and $d$ is the parameter dimension. Experiments further support the theoretical convergence results.

---


### 360. [PDFa11yMut: Measuring Mutation-Specific Detection in PDF Accessibility Checkers](https://arxiv.org/abs/2609.33160)

**<font color=#1a73e8>作者：</font>** Gauri Jain  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Automated PDF accessibility checkers provide useful conformance evidence, but a clean report is not a complete accessibility oracle. PDFa11yMut measures mutation-specific checker behavior by applying paired structure-level transformations to reference-suite baselines, verifying intended deltas and non-target invariants, and recording hash-linked checker evidence. Across 30 conformance-oriented mutants, PAC and veraPDF each produced 30 and 30 direct target findings, respectively, while Acrobat produced 23 direct findings plus 3 prespecified consequence-proxy findings. The 39 semantic/assistive-representation mutants produced no automated target finding in the tested configurations, while Acrobat issued manual-review prompts for a subset; Class B is interpreted descriptively rather than as a universal checker obligation. A separate convenience-selected exploratory AT sample observed representation differences in 8 of 9 pairs under one fixed NVDA/Acrobat/Windows procedure. The artifact contributes reusable operators, structural and purity oracles, paired baseline/mutant evidence, and reproducible analysis for a scoped mutation-testing study rather than a general checker-accuracy benchmark.

---


### 361. [FloodDiffusion 2: Efficient and Path Controllable Streaming Motion Generation](https://arxiv.org/abs/2609.33167)

**<font color=#1a73e8>作者：</font>** Yiyi Cai, Yuhan Wu, Kunhang Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present FloodDiffusion 2 (FD2), an efficient and controllable framework that builds upon FloodDiffusion (FD1), a state-of-the-art streaming motion generation model. While FD1 produces plausible motion, it suffers from low efficiency and limited controllability, as its attention design requires repeated computation over the entire history, and it lacks precise trajectory control for real-world applications. To address these limitations and improve generation quality, FD2 introduces three advances. First, Partial Attention makes finalized history representations independent of the active window, enabling KV-cached inference and shared-history packing for efficient training. Second, we establish a necessary-and-sufficient Bregman criterion for regression losses to preserve diffusion's conditional-mean velocity field. This criterion guides an FK-induced quadratic loss that incorporates motion geometry without online FK evaluation. Third, FD2 introduces precise path conditioning to control the character's root trajectory while preserving natural body motion. Experiments show that FD2 reduces training computation by 4.6$\times$ and accelerates denoising by 11.29$\times$, reaching 2.303 ms per update on long sequences. Alongside these efficiency gains, FD2 improves motion quality over FD1 and achieves state-of-the-art FID scores among streaming methods, with 0.048 on SEED and 0.053 on HumanML3D.

---


### 362. [When Does Backpropagating Through Policy Memory Matter? Physical Credit, Optimizer Updates, and Observability](https://arxiv.org/abs/2609.33169)

**<font color=#1a73e8>作者：</font>** Xingjian Li, Yi Han, Jianhua Z. Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Policies with memory can learn along two backward paths: through the physical states their actions produce and through the representations they store. Transformer-XL and truncated backpropagation through time cut the second path at stored history while keeping its values. We ask when this cut matters. Holding the forward computation fixed and varying only derivative edges, we measure parameter gradients, the updates the optimizer applies, and continued training in a Transformer vessel-trajectory model and a quadrotor tracking policy. In the vessel model, detaching the key-value cache shrank the gradient to about a tenth of its norm, with little rotation, when gradients flowed through all earlier physical states, but barely changed it under one-step physical credit. In this strongly clipped regime the optimizer, not the gradient, set how far updates differed: global-norm clipping removed most of the gradient difference between memory-cut graphs, whereas AdamW turned a 2% gradient difference between two placements of the cut into update differences of up to 31% at the step where the placement was switched. In a quadrotor trained from initialization with 0.20 m/s velocity noise, removing memory raised tracking error by 43% and cutting memory gradients raised it by 32%; at low noise the cut's mean cost exceeded the value of memory. Two-step truncation segments gave no measurable gain, although with hidden velocity a two-step window captured most of the value of memory; eight-step segments removed half to three quarters of the cost. Switching the cut on only for the last fifth of training understated its cost about threefold at 0.20-0.30 m/s, but not at low noise or with hidden velocity. These results suggest measuring the cost of a memory cut by training with it from initialization, and comparing backward graphs by the updates the optimizer applies rather than by raw gradients.

---


### 363. [Perturb-and-Solve: Efficient Learned-Operator Conditioning for Latent Diffusion Inverse Problems](https://arxiv.org/abs/2609.33171)

**<font color=#1a73e8>作者：</font>** Abduragim Shtanchaev, Arip Asadulaev, Luiza Labazanova 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent diffusion models serve as powerful priors for solving inverse problems in image restoration, such as deblurring, inpainting, and super-resolution. Current methods have a trade-off between generality and efficiency. Solvers that are restricted to a fixed set of degradation operators are fast and efficient. Methods that support arbitrary degradation operators are slow and require gradients through the diffusion network. To break this bottleneck, we introduce PASEO (Perturb-And-Solve for Efficient Operator conditioning), a method that uses a small (1M parameters) learned network to degrade diffusion model predictions in latent space. PASEO supports learned degradation operators without back-propagating through the diffusion network. We efficiently sample reconstructions from an approximate posterior by combining the diffusion model's prediction with the observed image. We do this by adding noise and solving linear equations based on a local linear approximation of the learned network, without building or inverting large covariance matrices. Across super-resolution, deblurring, and inpainting on FFHQ and COCO, PASEO achieves strong perceptual quality while running up to 9x faster and using up to 34% less peak memory than the tested baselines, with the same or fewer model evaluations.

---


### 364. [ABO-Med: Accelerated Bilevel Optimization for Few-Shot Medical Image Classification](https://arxiv.org/abs/2609.33176)

**<font color=#1a73e8>作者：</font>** Ruoxuan Shi, Sheng Yang, Zhengxing Su 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In recent years, bilevel optimization has been widely used in a variety of machine learning tasks. However, prior bilevel optimization algorithms generally require the computation of second-order information, which limits their practical scalability. Only recently has a first-order paradigm for bilevel optimization been established, attaining near-optimal theoretical guarantees for solving bilevel optimization problems. In this paper, we propose ABO-Med, a scalable instantiation of this paradigm for few-shot learning, by incorporating it into the model-agnostic meta-learning (MAML) framework and tailoring it to medical image classification. We also introduce Medical Adaptive RandomAugment (MedRAug), a modality-aware augmentation strategy designed for medical images. Theoretically, ABO-Med establishes the optimality of MAML-type meta-learning approaches. Empirically, ABO-Med outperforms prior baselines on several public medical datasets, with gains of 1.99% to 18.76%, while MedRAug further improves the average accuracy by 2.20% to 6.34%. Additional cross-domain experiments, augmentation ablation studies, backbone ablation studies, and training efficiency analysis further validate the effectiveness and efficiency of the proposed method.

---


### 365. [When an Evaluation Rule Writes Training Labels: Measuring Human-Reference Forgiveness in NAVSIM](https://arxiv.org/abs/2609.33189)

**<font color=#1a73e8>作者：</font>** Jiaxuan Guo, Jingxin Yang, Jiaqi Ye 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When the human reference scores zero on a metric, the released GTRS-Dense label generator for NAVSIM marks every candidate trajectory in the scene as passing it. NAVSIM's authors introduced this human-reference forgiveness to avoid penalizing contextually justified maneuvers when scoring one trajectory, and warned that it could overlook important failures. In label generation it sets a whole column of 16,384 candidate targets to passing. To measure the consequences for supervision, we re-run the generator with the overwrite disabled and compare the pre-overwrite targets with the released labels on all 103,288 navtrain scenes. The rule erases a candidate distinction that the training loss reads on 11,237 of them (10.8793%). Firing usually changes most of a column: lane keeping carries 9,982 of the 13,042 forgiven loss columns, and its median forgiven column had 14,391 of 16,384 candidates failing before the overwrite. On held-out navtest scenes forgiven on lane keeping, the released lane-keeping head's median AUC against the pre-overwrite outcome is 0.7095; on unforgiven scenes matched on failing-candidate count it is 0.9807. For the Hydra-MDP checkpoint released with GTRS, whose configuration takes the same label file, the two values are 0.6627 and 0.9761. Continuing the released GTRS-Dense checkpoint for 300 optimizer steps with three paired seeds, we observe the forgiven-scene AUC 0.1086-0.1251 higher with pre-overwrite than with published targets, and a narrower gap between matched groups, still above zero. Scoring with forgiveness disabled, we observe lane keeping higher by 2.478-3.524 points on navtest scenes forgiven on any of five loss metrics, with lower adjacent-frame plan consistency. Both changes are larger there than on the rest. EPDMS, scored the same way, does not separate the two target sets.

---


### 366. [Apparent Compression, Real Stability: The Intrinsic Dimension of Learning a Quantum Wavefunction](https://arxiv.org/abs/2609.33193)

**<font color=#1a73e8>作者：</font>** Lu Wei, Yufeng Wang, Chenfeng Cao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How many directions in weight space does training need? The intrinsic dimension answers this with the smallest number of random directions in which training still reaches a target accuracy, and small values have motivated parameter-efficient methods such as LoRA. We measure it for variational Monte Carlo (VMC), which trains a neural network to represent the ground state of a quantum many-body system. VMC is a demanding test, because the network generates its own training samples and every gradient is noisy, and a revealing one, because the exact answer is known and every run can be scored. We train only a small latent vector that a frozen random map turns into the network's weights, with no change to the standard natural-gradient optimizer. We find that a small dimension can be misleading, while the stability it brings is real. On a magnet with a hard sign pattern, a network that cannot represent signs reaches its best energy in 8 of 28,642 directions, but only because no such network can go lower; once signs are learnable, neither the signs nor the magnitudes are cheap. The dimension rises across a quantum phase transition, so it tracks how difficult a state is at far less compute than fitting a scaling law, yet it never falls below a floor set by the random subspace itself, even where the ground state is nearly trivial. Training in the subspace, in contrast, never diverged in our experiments, whereas full-parameter training with the same settings did, and a control with matched solvers attributes the difference to the reduced dimension.

---


### 367. [ReAL: Accelerating Flow Matching through Segment Advancement with Shared Lookahead](https://arxiv.org/abs/2609.33202)

**<font color=#1a73e8>作者：</font>** Xuanhua Yin, Chuanzhi Xu, Haoxian Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow-matching models generate high-quality images and videos, but repeated neural network evaluations make sampling expensive. Skipping evaluations reduces this cost by extending an available velocity estimate over a longer span. However, local velocity agreement alone does not determine a suitable span, and checking each candidate endpoint adds costly model calls. We introduce ReAL, a training-free sampler that selects how far to advance using one shared lookahead. Our key insight is that the discrepancy between uncorrected and lookahead-corrected endpoint proposals can be computed directly from the observed velocity mismatch and the candidate span beyond the lookahead. This relation provides a span-dependent selection criterion without additional endpoint evaluations. The same lookahead selects the longest passing candidate span, corrects the accepted update, and supplies its velocity as the next starting estimate. After initialization, each regular iteration requires only one fresh evaluation. ReAL uses the pretrained velocity output and original noise schedule, with no additional training or access to internal features. Experiments cover four image-generation backbones, video generation, and image editing. ReAL achieves 4.91x measured speedup on FLUX.1-dev while retaining 97.0% of dense mean ImageReward. On HunyuanVideo, it achieves a 5.49x speedup while maintaining a VBench score close to that of dense sampling.

---


### 368. [Structured Residual Connectivity Matters for Diffusion Transformers](https://arxiv.org/abs/2609.33203)

**<font color=#1a73e8>作者：</font>** Yuhe Liu, Xinyin Ma, Gongfan Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers (DiTs) have established themselves as a scalable backbone for high-fidelity image synthesis. However, unlike U-Net based diffusion models that rely on rigid, hand-crafted skip connections, DiTs predominantly use a uniform residual stream that integrates all preceding layers as a monolithic state. In this work, we rethink residual connections in diffusion transformers and propose to transform them from passive summation into an active retrieval mechanism optimized for image denoising. First, we conduct a systematic analysis of DiT's internal representation, revealing a latent preference for early-layer feature reuse and symmetric layer guidance. Motivated by this, we introduce a structured connectivity design that explicitly integrates local residual connections with long-range pathways. Instead of static skip connections or dense all-layer routing, our method enables each transformer block to selectively ``attend'' to critical earlier representations, dynamically retrieving spatial and semantic cues through direct, differentiable cross-depth paths. Experiments show that our adaptive connectivity leads to faster convergence, with up to $1.73\times$ fewer training iterations, and significant gains in FID and visual quality with less than $0.1\%$ additional parameters, further improving a strong REPA-XL/2 model from $5.9$ to $4.34$ FID without guidance and reaching $1.39$ FID with classifier-free guidance. Our findings suggest that adaptive cross-layer connectivity is a critical yet underexplored factor in diffusion transformers, and that incorporating structured information pathways provides a simple and effective direction for improving scalable generative models.

---


### 369. [SMORE: Stability-Promoting Mesh-Agnostic Model Reduction for Time-Dependent PDEs](https://arxiv.org/abs/2609.33205)

**<font color=#1a73e8>作者：</font>** Yangyuan Li, Weichao Li, Shaowu Pan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-fidelity simulations of time-dependent partial differential equations (PDEs) are computationally expensive, motivating data-driven reduced-order surrogates for many-query tasks such as uncertainty quantification, design optimization, data assimilation, and optimal control. However, existing surrogate models often exhibit poor temporal stability, which can lead to unstable rollouts and exploding gradients during backpropagation, especially in multistep long-horizon forecasting. To address this, we propose SMORE, a mesh-agnostic framework for model order reduction of time-dependent PDEs. Its latent dynamics are trained with Lyapunov-guided stability regularization, which promotes stable long-horizon rollouts. We provide theoretical guarantees under the stated structural assumptions. Beyond forecasting PDE evolution, the learned latent dynamics, which are interpretable and linear or linear-quadratic, could bring benefits for downstream tasks such as data assimilation and optimal control. Moreover, our framework is capable of predicting continuous PDE solution fields from sparse measurements of the initial condition. We evaluate SMORE on a range of problems, including wave propagation, the Navier-Stokes equations, and the shallow water equations. Our results show that it improves long-horizon rollout generalization and empirical robustness, and achieves competitive accuracy at comparable parameter budgets relative to competitive baselines including DINo, FNO, CNO, and Transolver.

---


### 370. [WorldAgent: Verification-Guided Agentic Physical World Construction](https://arxiv.org/abs/2609.33208)

**<font color=#1a73e8>作者：</font>** Caoliwen Wang, Mengdi Wang, Yige Chen 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Constructing complex physical worlds from language requires coordinating extensive 3D environments, detailed structures and objects at different spatial scales, and interacting physical processes under both stated goals and implicit physical constraints. We present WorldAgent, an agentic framework for verification-guided physical world construction from a single natural-language prompt, without iterative user debugging. A world construction layer expands the prompt into a structured world specification and uses physical knowledge to build scenes and run numerical simulations. After every step, a verification layer inspects scene geometry and simulation states alongside rendered views. Failed checks guide automatic revisions to the specification and re-execution of the affected steps. Accepted worlds pass the required checks and remain editable for further inspection and resimulation. We introduce AgenticSimBench, on which WorldAgent achieves the best scores among the evaluated agent-based methods on five of seven metrics. In a 26-participant user study, it receives the highest mean ratings across all four criteria.

---


### 371. [Background Gradients Shape Memorization in Flow Matching](https://arxiv.org/abs/2609.33210)

**<font color=#1a73e8>作者：</font>** Xuanhua Yin, Boyu Wei, Shuyi Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Repetition is closely associated with memorization in generative models, but how other training images affect the retention and copying of targets remains unclear. We study this question in class-conditioned flow matching, where images outside the target set form the background. At fixed target repetition and same-class background row count, replacing repeated same-class images with distinct images reduces the target extraction rate from 80.7% to 18.0%. To explain this effect, we develop a paired-trajectory framework that isolates target-induced parameter displacement and the background gradient response to it. This response has an exact path-integrated curvature representation, connecting background loss geometry to target learning. Reciprocal response transfer between repeated and distinct backgrounds changes target retention and copying in both directions, establishing the response's causal role. After target removal, the response correction parallel to the target-induced displacement preserves approximately 90% of the copying effects of full response transfer. Directly scaling the displacement also changes copying without further training. The post-removal copying effects of reciprocal transfer are reproduced across datasets and architectures. Together, these results identify the background gradient response as a mechanism through which same-class training data shape the retention of target learning and the reproduction of target images.

---


### 372. [RepFlow: Reciprocal Supervision Improves Generation and Representation in Flow Models](https://arxiv.org/abs/2609.33217)

**<font color=#1a73e8>作者：</font>** Weili Zeng, Feng Tian, Shengqi Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative models learn visual structure through denoising, yet their internal states are entangled with both noise level and network depth, making it difficult to obtain a stable visual representation from the generator itself. We introduce RepFlow, which learns such a representation from the generator's evolving computation and uses it to guide generation. Specifically, a separate timestep-free encoder is trained, through a timestep-conditioned predictor, to recover generator states across depths and noise levels from masked clean images. By excluding the reference noise and masked-out content from the encoder's input, we encourage the encoder to distill visual information that is recoverable from the visible image context and predictive of generator states. The representation learned from the generator's evolving states is then fed back to guide and improve the generator, whose updated states provide supervision for further representation learning, forming a reciprocal learning process. This reciprocal process improves multi-step generation and representation quality, as measured by frozen linear probing on ImageNet with latent-space SiT and pixel-space JiT, without an externally pretrained representation teacher. Across the two unconditional settings, FID decreases by $19.2$--$40.8\%$ relative to native training, while linear-probe accuracy improves by 6.80--10.04 percentage points over the best searched raw generator features. The learned representation also serves as a distributional metric for one-step JiT post-training, extending its role from instance-level alignment to distribution-level supervision.

---


### 373. [Scope-WM: Scoped Computation for Efficient Visual World Models](https://arxiv.org/abs/2609.33218)

**<font color=#1a73e8>作者：</font>** Chunzheng Li, Zesheng Jia, Hongda Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual world models enable robotic planning by predicting future observations, but dense latent-state propagation and sample-intensive trajectory optimization incur high inference latency and peak memory usage, limiting real-time deployment on resource-constrained platforms. Existing sparse world-model acceleration methods either rely on unguided token sparsification, which may discard planning-relevant information and restrict achievable sparsity, or introduce heavy auxiliary modules and cumbersome multi-stage training pipelines. In this work, we present Scope-WM, an efficient visual world model that scopes computation to prediction-relevant latent regions and promising action sequences. Scope-WM distills prediction relevance into a lightweight action-conditioned selector and applies full dynamics prediction only to a compact subset of selected tokens. It updates the remaining tokens using a compact summary of foreground states and their changes, allowing the background to perceive foreground dynamics without costly token-to-token interactions. During planning, Scope-WM preserves and reuses high-quality action sequences discovered during the initial MPC search, focusing subsequent search under reduced rollout budgets. The resulting pipeline requires only a one-off selector distillation followed by a single joint training stage for the sparse world model. On the challenging Push-T task, Scope-WM reduces peak GPU memory usage and planning time to $18.1\%$ and $14.3\%$ of those of dense DINO-WM, respectively, corresponding to a $6.97\times$ planning speedup, while maintaining competitive task performance. Further evaluations across five diverse visual planning tasks demonstrate the general applicability of Scope-WM. Code is available at this https URL.

---


### 374. [AevaScenes: An FMCW LiDAR Dataset and Benchmark for Long-Range Perception](https://arxiv.org/abs/2609.33230)

**<font color=#1a73e8>作者：</font>** Gautham Narayan Narasimhan, Heethesh Vhavle, Kumar Bhargav Viswanatha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> FMCW LiDAR measures per-point radial Doppler velocity alongside range, providing a motion cue unavailable in conventional time-of-flight sensors. Exploiting this signal at long range remains understudied. We present an FMCW LiDAR dataset of 575 sequences (57.5K frames) with over 8 million annotated 3D boxes across 16 detection classes and per-point labels across 24 semantic classes, captured by six commercial FMCW LiDAR sensors and six paired 4K cameras across eight Bay Area cities, including 237 nighttime sequences, with annotations extending to 400m. We define a benchmark with three tasks: 3D object detection, scene flow estimation, and semantic segmentation. Detection and scene flow are evaluated across three range bins to 400m, with a public evaluation server. We explore the impact of Doppler measurements on flagship recognition tasks, and find significant improvements up to 2X in detection AP of far-away vehicles and pedestrians, particularly in low-latency single-frame settings. We similarly find scene flow accuracy is significantly improved with Doppler measurements across all ranges. Our dataset and benchmark have been publicly released at this https URL.

---


### 375. [MTLiquid: Enabling Efficient Multi-Task Learning using Liquid Neural Networks for Lightweight Healthcare Monitoring Systems](https://arxiv.org/abs/2609.33232)

**<font color=#1a73e8>作者：</font>** Rachmad Vidya Wicaksana Putra, Fahad Abdul Rauf, Muhammad Shafique  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous-time sensing and monitoring with timely and accurate decision-making are critical for many real-world applications. In healthcare monitoring systems, physiological signals are often available or sampled at irregular time intervals, hence requiring continuous-time processing to provide accurate prediction. Moreover, such systems often need to solve multiple detection/prediction tasks to provide a comprehensive patient review from different physiological aspects for more accurate decision-making. To solve this, continuous-time neural networks (CTNNs) can be employed. However, state-of-the-art works typically solve only one task at each network, thereby limiting their efficiency gains. To address this limitation, we propose MTLiquid, a novel methodology to enable efficient multi-task learning in continuous-time processing for healthcare monitoring systems through effective network design and training strategy. MTLiquid employs: (1) multiple input and output heads to accommodate different tasks, while sharing the same backbone network across tasks; as well as (2) an effective training strategy that leverages a loss-weighting technique to balance learning updates across different tasks and a proportional data presentation technique to address imbalanced dataset sizes. Experimental results for mortality prediction (P12) and sepsis early detection (P19) tasks for ICU patients show that, MTLiquid achieves strong performance (AUROC: 0.84 for P12 and 0.94 for P19) comparable to the state-of-the-art single-task learning in both continuous-time networks (AUROC: 0.84 for P12 and 0.95 for P19) and discrete-time networks (AUROC: 0.79-0.82 for P12 and 0.92-0.94 for P19), while incurring significantly smaller memory cost by 44%-94%. These results highlight the potential of our MTLiquid methodology to enable lightweight continuous-time healthcare monitoring systems for better decision-making.

---


### 376. [The Price of Locality: Why Forward-Forward Underperforms Backpropagation?](https://arxiv.org/abs/2609.33240)

**<font color=#1a73e8>作者：</font>** Zhaoxian Wu, Haichuan Liu, Tianyi Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Forward-Forward Algorithm (FFA) replaces backpropagation (BP) with layer-wise local contrastive objectives, eliminating the backward pass and the need to retain intermediate activations, yet suffers a persistent performance gap with BP that worsens with depth. This paper diagnoses two structural failure modes: an optimization floor arising from concurrent local updates; and a geometric collapse of layer representations driven by the local update mechanism. On the optimization side, we prove that the FFA loss satisfies the Polyak--Lojasiewicz inequality at each layer; however, simultaneous layer updates induce inter-layer representation-distribution drift, so each layer optimizes against a moving input distribution and incurs an error floor. On the representational side, the pairwise similarity kernel of layer representations contracts exponentially toward rank one as depth increases, collapsing the diversity of per-layer error signals. This collapse bounds FFA's effective learning capacity, which measures the diversity of gradient information across layers, independently of depth, whereas BP's chain-rule signal preserves per-layer diversity, yielding a capacity that scales with depth.

---


### 377. [Minimax-Optimality of Posterior Sampling for Reinforcement Learning](https://arxiv.org/abs/2609.33246)

**<font color=#1a73e8>作者：</font>** Taewon Goo, Kihyuk Hong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Posterior sampling for reinforcement learning (PSRL) is one of the simplest and most effective exploration methods, but a basic question has remained open: does unmodified PSRL achieve minimax regret without structural assumptions on the prior? We answer yes. Exact vanilla PSRL is minimax optimal in leading-order Bayesian regret under arbitrary correlated priors. The difficulty is that a posterior-sampled transition model is coupled with its own continuation value. We overcome this with a common empirical transition reference that isolates the resulting value mismatch and a Bellman-based variance argument that controls it without an extra leading-order state-space factor. For finite-horizon, time-inhomogeneous tabular MDPs with unknown stochastic rewards, this yields the minimax $\widetilde{O}(\sqrt{SAH^3K})$ regret rate under arbitrary joint priors over rewards and transitions. The same proof principle gives the minimax $\widetilde{O}(d\sqrt{H^3K})$ rate for linear-mixture MDPs under arbitrary joint parameter priors.

---


### 378. [Feedback-Robust AI for Patient Knowledge Graphs](https://arxiv.org/abs/2609.33248)

**<font color=#1a73e8>作者：</font>** Mohammed Sameer Syed  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Patient knowledge graphs from bedside monitoring should type their relations and state whether the data support their signs. In anesthesia and intensive care, clinicians titrate drugs and ventilation in response to the physiology, so temporal relations mix the patient's response with the clinician's policy. We introduce ClosedLoopBench: 29 relations with signs fixed by physics, pharmacology or clinical practice, on 3,442 VitalDB surgical cases (12,653 h) with negative-control action streams. When each patient's actions are replaced by another patient's, six of 12 estimators declare on average 11-18 of their 19-29 distinct relation estimates significant without calibration, and after calibration cross-correlation and Granger tests still assign ventilator rate -> end-tidal CO2 the sign of the clinician's policy. We propose feedback-robust patient graphs that combine concept nodes with evidence pointers, typed relations admitted against negative controls, and beat-level couplings. On VitalDB under null streams, our graphs contain 0.06-0.10 false concept-level relation instances per graph, versus 10-12 for correlational construction. Patient-specific estimates of 11 slow drug and ventilator responses predict later data no better than population estimates, whereas the pulse-arrival-time-systolic-pressure slope is negative in 94.3% of 2,884 cases and patient-specific (early-late correlation 0.67 [0.63, 0.70]).

---


### 379. [VGGT-Diff: Visual Geometry Meets Diffusion for Sparse-View Novel View Synthesis](https://arxiv.org/abs/2609.33253)

**<font color=#1a73e8>作者：</font>** Kangjie Chen, Xiangyu Li, Dongbin Zhang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present VGGT-Diff, a geometry-routed multi-view diffusion model for sparse-view novel view synthesis. Existing novel view synthesis (NVS) methods face a fundamental trade-off: reconstruction-based approaches preserve observed geometry but struggle to synthesize unseen regions, while diffusion-based methods provide strong generative priors yet rely on implicit source-to-query correspondence. VGGT-Diff bridges these regimes by routing visual geometry latents from VGGT-{\Omega} into a pretrained video diffusion model. Each visual token is associated with a 3D point and confidence, then transformed into query-aligned latent conditions through a confidence-aware Visual Geometry Router (VGR) that preserves front and back surface evidence. These conditions guide joint target-view denoising, while Point-Track Residual Consistency (PTRC) regularizes predicted-clean residuals along reliable 3D tracks, improving multi-view stability. We further introduce robust geometry conditioning, combining training-time regularization with inference-time guidance for improved robustness. Experiments show competitive or state-of-the-art performance across interpolation and extrapolation under different viewpoint difficulties. Our code is available at this https URL.

---


### 380. [BERT4DTI : BERT-based Model for Predicting Drug-Protein Interactions](https://arxiv.org/abs/2609.33254)

**<font color=#1a73e8>作者：</font>** Thanina Hamitouch, Khadidja Henni, Abdelkrim Arie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding how drugs interact with protein targets is fundamental to drug discovery, drug repurposing and the early identification of promising therapeutic candidates before costly experimental testing. Sequence-based DTI models face three practical limitations: labelled interactions are scarce and unevenly distributed, large pretrained chemical and protein encoders are expensive to fine-tune end-to-end, and independently encoded sequences do not capture pair-specific dependencies. We present BERT4DTI, which encodes SMILES strings with ChemBERTa and amino-acid sequences with ProtBERT, applies bidirectional mutual attention between token-level representations, and classifies the resulting interaction features using convolutional layers and a multilayer perceptron. To reduce trainable size, ProtBERT is truncated to 18 retained layers and only the last two layers of each encoder are fine-tuned. On BIOSNAP, DAVIS and BindingDB, BERT4DTI is competitive, achieving the best ROC-AUC and PR-AUC on BIOSNAP and the highest sensitivity on all three benchmarks. An ablation on DAVIS shows that mutual attention improves PR-AUC and specificity. With 125M trainable parameters compared with 353M for full BERT fine-tuning, BERT4DTI provides a favourable performance-parameter trade-off for sequence-based DTI screening, while leaving runtime profiling, calibration and leakage-audited validation for future work.

---


### 381. [GTRL: Grounding Divide-and-Conquer Value Learning with Temporal Differences](https://arxiv.org/abs/2609.33259)

**<font color=#1a73e8>作者：</font>** Abdul Monaf Chowdhury, MD Sameer Iqbal Chowdhury, Shifat E Arman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In offline goal-conditioned reinforcement learning (GCRL), divide-and-conquer scales to long horizons by joining two shorter segments at a subgoal. However, under stochastic dynamics, the base case of this rule values the luckiest trajectories through the data. The subgoal must also lie on a shared trajectory, so a state-goal pair that no trajectory connects gets no value update at all. To address both, we present Grounded Transitive RL (GTRL), an offline GCRL value learning algorithm that grounds the divide-and-conquer update with a one-step TD target. Over a single step, TD is correct, as its target averages over the successors and needs no subgoal. GTRL adds this target to the composition rather than replacing it, so every pair receives an update, and the composition still carries the long horizon. GTRL also corrects the bias from hindsight relabeling by reweighting each goal against how reachable it was from other successors. We evaluate our algorithm on nineteen OGBench tasks spanning stochastic, deterministic, and stitching environments, where it achieves the highest average success rate. Code will be released soon.

---


### 382. [CORTEX: A Verified Experience Layer for Generalist Agents](https://arxiv.org/abs/2609.33260)

**<font color=#1a73e8>作者：</font>** Garapati Keerthana, Manik Gupta  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An agent can solve a task today and face the same task under new facts, tools, or governing knowledge tomorrow. Most agent systems can retrieve relevant text or recall prior conversations, but they lack a principled way to decide when a previous solution is still valid, when it must be adapted, and when it should be discarded. We introduce CORTEX (Contextual Orchestration and Reuse of Task EXperience), a general AI systems framework that connects specialized agents through an external layer of verified experience. Each episode records its task conditions, source and tool state, decisive predicates, proof trace, verifier, and outcome. A meta-controller chooses exact replay, checked adaptation, fresh synthesis, or escalation. Accepted episodes can become task patterns and procedural strategies through a challenge-driven development loop. This gives the system an implicit competence layer that can grow without changing model weights. We formalize system contracts for exact replay and source-version separation, and derive when reuse saves computation. A controlled two-domain implementation tests the exact-replay core on 1,000 synthetic cases. Complete-family holdouts test procedural transfer on 1,000 new-family cases across eight clinical and policy splits, with complete fresh-evidence grounding and perfect invariance to irrelevant-field and insertion-order perturbations. The transfer trace exposes the work required for verified strategy execution. These results establish an initial path toward general intelligence through reusable procedures, typed experience, and developmental transfer.

---


### 383. [EngIntervene: Benchmarking Multimodal Engineering State Understanding and Design Intervention Reasoning](https://arxiv.org/abs/2609.33261)

**<font color=#1a73e8>作者：</font>** Jinchang Zhang, Yingda Tao, Jiakai Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal engineering benchmarks largely evaluate static understanding, such as recognizing components, interpreting diagrams, or answering technical questions. This leaves a missing middle between engineering perception and full design generation: whether a model can use an understood system state to reason about relations, constraints, and the consequences of design changes. We introduce \textsc{EngIntervene}, a benchmark for this capability. It contains 3,229 questions across seven engineering domains and organizes evaluation into four levels: state grounding (T1), relational and mechanistic reasoning (T2), constraint-aware diagnosis (T3), and intervention reasoning (T4), which asks whether a proposed modification achieves its target while preserving required constraints. The tasks instantiate a unified engineering state representation spanning objects, relations, constraints, and design objectives, and T2--T4 are scored against structured reference answers with atomic criteria. Across open- and closed-weight multimodal models, stronger grounding does not reliably translate into better diagnosis or intervention, and the best open-weight model trails the best closed model by 14.7 percentage points on the T2--T4 average. Removing or shuffling visual evidence consistently degrades performance, while benchmark-specific supervised fine-tuning improves T1 but not T2--T4. T4 further exposes a large gap between satisfying individual revision criteria and producing a fully valid intervention. Engineering reasoning thus requires not only recovering the current state, but also reliably using it to reason about constraints and post-intervention consequences. Code and benchmark artifacts are available at this https URL

---


### 384. [VehDyn: A Driving World Model Benchmark for Vehicle Dynamics](https://arxiv.org/abs/2609.33264)

**<font color=#1a73e8>作者：</font>** Tianyi Wang, Wangsheng Du, Jiazhou Chen 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models are emerging as data engines, action planners, and generative simulators for autonomous driving, but existing benchmarks primarily assess visual fidelity and coarse physical plausibility, providing limited evidence on whether generated driving futures obey realistic vehicle kinematics and dynamics. This limitation is further compounded by the lack of datasets in which vehicle, road, maneuver, and speed conditions are independently controlled, and ground-truth vehicle states are recorded in synchrony with videos. We introduce VehDyn, a driving world model benchmark for vehicle dynamics. VehDyn is built on a CARLA-CarSim co-simulation platform where photorealistic rendering is coupled with a validated multi-body dynamics model, and it contains 10,080 configurations from a full factorial design over five vehicle types, four tire-road friction coefficients, three maneuvers, four target speeds, 14 scenes, and three illuminations, each paired with synchronized position, velocity, and attitude sequences. Built on this dataset, VehDyn introduces a hierarchical evaluation framework that measures trajectory alignment, kinematic consistency, and dynamic consistency, and benchmarks 12 state-of-the-art video world models. We further assess the video quality using two established protocols and correlate it with the VehDyn score. Trajectory-level metrics are nearly saturated, with ten of twelve models within 20\% of ground truth, while no model reaches 92\% of ground truth on dynamic consistency, and visual-quality metrics are only weakly correlated with vehicle-dynamics fidelity. DrivingWorld achieves the highest VehDyn score, followed by Cosmos 3 Nano and LTX-Video 2.5, and the VehDyn score agrees closely with human judgment. VehDyn provides a systematic foundation for developing driving world models that are physically consistent and visually realistic.

---


### 385. [Structured Sparse Memory for Recurrent Reasoning](https://arxiv.org/abs/2609.33270)

**<font color=#1a73e8>作者：</font>** Zixuan Zhao, Samuel Wheeler, Neil Getty 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recurrent models trained from scratch have recently become competitive on ARC-style reasoning tasks, but the usual framing around small recurrent backbones overlooks two important parts of the system: task-conditioned memory and synthetic augmentation data. We study this regime through CHARM, a compact hybrid ARC model that combines recurrent reasoning with structured task memory, synthetic data, and inference-time aggregation. In existing approaches, task-conditioned memory supplies a large hidden source of capacity, reaching more than 30x the size of the recurrent backbone. We introduce a compositional sparse embedding (CoSE) for task conditioning that reduces learned task-memory parameters by over 90% while improving pass@2 in controlled ARC ablations. For the recurrent backbone, recurrent depth helps only when balanced with learning horizon. Combining these ingredients, our system reaches 84% pass@2 on ARC-AGI-1 and 46.7% pass@2 on ARC-AGI-2 public evaluation. The benefits of structured memory also generalize to unseen puzzles and other domains. Our code, dataset, and model checkpoints are available at this https URL.

---


### 386. [Next Thoughts Are Distributions: Generative Autoregressive Reasoning in the Latent Space](https://arxiv.org/abs/2609.33271)

**<font color=#1a73e8>作者：</font>** Yang Li, Yi Wang, Shiyuan Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning problems often admit multiple valid ways to proceed. Continuous reasoning promises to move computation beyond language tokens into a more compact latent space, but representing several plausible ways to think next remains difficult. We introduce Autoregressive Thought Flow (ATF), which models the next continuous thought as a multimodal distribution. A causal autoregressive model performs the reasoning computation, while a lightweight diffusion head generates a plausible next thought from the resulting condition. The sampled thought is fed back into the model, allowing continuous reasoning to unfold for a variable number of steps while preserving the pretrained backbone. Across mathematical reasoning tasks, ATF improves accuracy with compact latent traces and benefits from reinforcement learning and additional test-time thinking. Multi-sample evaluation shows broader solution coverage, indicating that its multimodal predictions capture useful diversity among reasoning paths. Our results suggest that continuous reasoning is more effective when multiple possible next thoughts remain available rather than being collapsed into a single prediction.

---


### 387. [Towards Identifiable Representations under Misspecified Structure](https://arxiv.org/abs/2609.33273)

**<font color=#1a73e8>作者：</font>** Yuke Li, Yujia Zheng, Ziyi Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The presence of noise that depends on the latent variables poses a fundamental challenge to identifiability. Existing results rely on conditional independence among the observations given the latent variables. We study a more general \emph{misspecified structure}, where this conditional factorization does not hold, and establish both precise and approximate identifiability guarantees. We characterize structural misspecification as a perturbed factor analysis problem. For precise identifiability, we establish subspace identifiability under spectral separation and controlled perturbation, followed by component-wise identifiability under structural sparsity. When the precise condition is not guaranteed, we derive an approximate subspace-identifiability theorem. Based on these results, we develop an unsupervised variational estimator for recovering latent variables. Experiments demonstrate the effectiveness of the proposed framework.

---


### 388. [ChronoFlow: Hierarchical Flow Matching for Irregular Time Series Generation](https://arxiv.org/abs/2609.33276)

**<font color=#1a73e8>作者：</font>** Changhun Kim, Sunguk Jang, Jeongjun Lee 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in generative modeling have substantially improved time series generation, yet most existing methods either assume a regular temporal grid or focus on feature dynamics under a given sampling structure. This makes them illsuited for generating irregular time series in their native form, where a model must capture not only feature values, but also how many observations occur, when they occur, and which features are observed together. To address this heterogeneous generation problem, we propose ChronoFlow, a unified hierarchical flow matching framework organized by statistical granularity. Following a coarse-to-fine hierarchy, ChronoFlow first generates observation counts and feature-wise frequencies, then jointly generates observation times and feature co-observation patterns, and finally generates values conditioned on the realized pattern. This turns a complex joint generation problem into structurally aligned subproblems while preserving their dependencies. To evaluate complete irregular time series generation, we introduce complementary metrics spanning sample realism, sampling structure, value fidelity, and temporal and cross-feature dependencies, and validate them through controlled corruptions. Across five benchmarks, ChronoFlow achieves strong improvements in generation fidelity over existing baselines, while factorization studies support the proposed hierarchy. Our code is available at this https URL.

---


### 389. [Domain Generalization under Sampling Pattern Shifts in Irregular Time Series](https://arxiv.org/abs/2609.33279)

**<font color=#1a73e8>作者：</font>** Changhun Kim, Joohyung Lee, Kwanhyung Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Irregularly sampled multivariate time series (ISMTS) are prevalent in real-world applications, where both observation times and available measurements can vary substantially across domains. While recent models increasingly exploit such sampling information for prediction, its robustness under sampling pattern shifts remains underexplored. We introduce HAR-C, to the best of our knowledge the first controlled benchmark for sampling pattern shifts in ISMTS, and show that sampling shifts alone can substantially degrade performance, induce sampling-specific shortcuts, and remain challenging for existing domain generalization (DG) methods. Motivated by these findings, we propose PRISM, a DG framework that first learns complementary feature-centric and sampling-centric representations without task labels, and subsequently performs robust supervised training across diverse sampling variations to discourage brittle shortcut reliance. Extensive experiments on controlled and real-world ISMTS benchmarks demonstrate that PRISM consistently improves robustness to unseen sampling shifts over existing methods. Our code is available at this https URL.

---


### 390. [The Text Beside the Image: Detection, Utility and Leakage for Trustworthy Multimodal Medical Data and Beyond](https://arxiv.org/abs/2609.33280)

**<font color=#1a73e8>作者：</font>** Andreas Maier, Monica Hinrichs-Mayer, Franziska Weber 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical images are released with the reports that describe them, and protecting the image does not protect the report. This paper measures the text component of such releases. We measure identifier detection, downstream utility and residual identity leakage on the same documents, with the pseudonymisation policy as the variable under test: 15 detectors, three release conditions and four corpora of medical reports, legal judgments, news and other genres, and e-mail, in German, English, Chinese and Arabic. A fixed 13-detector union reaches a person sensitivity of 0.9998 at specificity 0.8686 on the medical reports, 0.9958 at 0.8504 on the legal judgments, 0.9352 at 0.9318 on news and other genres, and 0.9906 at 0.6235 on e-mail. With this ensemble, frequency matching with a public name list recovers zero identities by alignment across the four corpora; the names it got right were ones the detector missed, left in clear text. Cross-document linkage ranks the correct person first for 0.93% of e-mail queries without training and 3.94% with it, against 1/3697 chance and 71.98% on unmodified text. On the medical reports it recovers nothing without training and 0.71% of 138 queries with it, against 1/207 chance and a 2.73% ceiling on unmodified text.

---


### 391. [Application Agnostic EM Side-Channel Emanations of the FPGA Clock Distribution Network](https://arxiv.org/abs/2609.33281)

**<font color=#1a73e8>作者：</font>** Ashish Sharma, Alia Long, Keith D. Mecham 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Electromagnetic side channels have been extensively utilized in non-invasive attacks or analyses to extract critical information from deployed systems. Most of the attacks or analyses are typically executed on cryptographic algorithms under the assumption that the underlying implementation remains fixed. The assumption is valid in the context of fixed hardware, where modifications to the circuit are not made after manufacturing. However, in the case of adaptive hardware, including field-programmable gate arrays (FPGAs), the assumption no longer holds as modifications to the configuration of the array are permitted post-manufacturing. Consequently, this study introduces a methodology for the analysis of electromagnetic side channels of an FPGA through the study of deterministic finite state machines (DFSMs), where the effects of placement, routing, and operating frequency on the EM emanations of the FPGA due to the utilized clocking resources are characterized. To analyze the impact of frequency, device placement, and resource allocation on the EM emanations from the FPGA, statistical analysis including mean difference and variance difference calculations of measured EM fields were utilized to identify points of high EM activity on a set grid of sampled points. A 1.32x increase in flagged grid points was observed in the analysis of the mean difference when the percentage of utilized clock resources was increased from 25% to 90%. Similarly, a 1.39x increase in flagged grid points was observed when the variance difference was calculated for the same increase in clock resources.

---


### 392. [RINI: Seeing the Prior Is Not Enough](https://arxiv.org/abs/2609.33284)

**<font color=#1a73e8>作者：</font>** Hongyi Du, Tianyi Zhang, Heng Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A research proposal can describe an established mechanism correctly while claiming to introduce it. We study whether providing the earlier paper corrects such contribution claims. Three controlled experiments compare proposals generated with a contribution-bearing prior and a same-topic control. Providing the prior yields no clear aggregate reduction in unsupported novelty. Human analysis of 175 interpretable exposed proposals finds that 137 recognize the prior's relevance, but 61 correctly attribute the established contribution. Of 71 proposed remaining distinctions, 37 are covered by the same prior. We introduce Research Idea Novelty Inspection (RINI), which audits contribution claims against evidence, checks the remaining distinction, and applies local revisions. Five human annotators evaluate 1,080 original-revision pairs across three methods. On the same 240 originals judged to require correction, successful repair is 11.7% for Self-Revision, 39.1% for Retrieve-and-Revise, and 72.2% for RINI, with research tasks weighted equally. The improvement over same-evidence direct revision is 33.0 percentage points. The revised proposals retain their research questions and technical methods. These results motivate explicit contribution attribution when using literature to generate and revise research proposals.

---


### 393. [BITS: Rethinking Fair and Comprehensive Evaluation for Irregular Time Series Forecasting](https://arxiv.org/abs/2609.33303)

**<font color=#1a73e8>作者：</font>** Kangjia Yan, Linfeng Wang, Tianen Shen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite recent progress in irregular time series forecasting, the field still lacks a unified benchmark for fair and comprehensive evaluation. Existing evaluations are often conducted on a limited set of datasets with inconsistent experimental protocols and predominantly error-based metrics, rendering it difficult to compare and assess methods fairly and comprehensively across diverse settings. To eliminate these limitations and accelerate progress, we propose BITS, a standardized, reproducible, and extensible benchmark for advancing research on irregular time series forecasting. BITS covers eleven datasets from nine domains with diverse irregularity characteristics, and it characterizes the datasets according to their missing rate, missing pattern complexity, sampling irregularity, and skewness. Further, it offers a unified pipeline for data preprocessing, model integration and evaluation, and reporting. It accommodates regular and irregular time series forecasting methods, including time series foundation models, under consistent settings, incorporating both error-based and non-error-based evaluation metrics. Findings include that method performance varies substantially across irregularity characteristics, with no single modeling strategy consistently dominating. We also find that using error-based or non-error-based metrics can yield different model rankings, highlighting the need for multi-dimensional evaluation. The code can be found at this https URL.

---


### 394. [Relevance Does Not Imply Applicability: Experience Activation for Personal GUI Agents](https://arxiv.org/abs/2609.33304)

**<font color=#1a73e8>作者：</font>** Fuyao Zhang, Xuan Wang, Zherui Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Personal Graphical User Interface (GUI) agents rely on interaction history to infer what a user wants from ambiguous instructions and to anticipate recurring routines. Existing approaches retrieve task-relevant history and append it to the policy's context, implicitly assuming that experience relevant to a task remains useful for each decision within it. We find that this help is largely spent at the first decision: retrieved history strongly improves the opening step of an episode, yet provides little sustained benefit over the remaining 90\% of steps, and offers weak guidance on whether a proactive suggestion is warranted. A relevant record may tell the agent where to begin, but not which past action applies to the current screen or whether a routine is due now. The underlying issue is that relevance does not imply applicability}: relevance is determined at the task level, whereas applicability depends on the situation at decision time. We therefore recast personalization as experience activation and introduce ExpActivator, a training-free framework that activates only the experience applicable to the current situation. During execution, ExpActivator matches each new screen to historical states in the frozen GUI backbone's latent space and supplies the corresponding action as a reference. Before execution, it activates a recurring intent only when the current time and scenario provide sufficient support, and otherwise abstains. Across four GUI backbones, ExpActivator improves within-trajectory step success by 28\% on average, achieves the best personalized execution on every backbone while using about one-fifth as many history tokens, and reaches approximately 2.3$\times$ the Matthews correlation coefficient of the strongest proactive baseline. Experience pays where it is activated, not where it is appended.

---


### 395. [LoopTrack: A Simple Baseline for Parameter-Efficient Transformer Tracking](https://arxiv.org/abs/2609.33306)

**<font color=#1a73e8>作者：</font>** Liang Peng, Chenxiao Li, Libo Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current Transformer-based tracking methods typically stack multiple Transformer blocks with separate parameters to model interactions between the target template and the search region for target localization. These trackers often incur substantial parameter overhead from stacked blocks, making their deployment on resource-limited devices difficult. To address this, we propose a parameter-efficient Transformer tracking framework, dubbed LoopTrack, which repeatedly applies a set of Transformer blocks with shared parameters to interact features in a looped architecture for tracking, significantly reducing the number of parameters. To further exploit target cues, we present two lightweight designs, including target-aware looping (TAL) and gated target memory (GTM). The former applies intermediate target information generated by one loop to guide feature interaction in the subsequent loop, enabling progressive feature refinement, while the latter maintains a compact memory across frames, which is incorporated into the loop process to provide long-term information to the tracker, mitigating temporal drift in tracking. Compared to existing Transformer trackers, LoopTrack enables multiple rounds of feature interaction with fewer model parameters, making it resource-friendly for deployment. In extensive experiments on multiple datasets, LoopTrack shows a favorable accuracy-parameter trade-off. In particular, our LoopTrack$_{\rm One}$, with a single shared Transformer block, achieves 66.2\% SUC score on LaSOT with only 3.4M parameters, while LoopTrack$_{\rm Three}$, using three shared blocks, achieves 69.3\% SUC score with 6.4M parameters, surpassing existing parameter-efficient tracking methods with comparable or larger model size. With LoopTrack, we aim to establish a simple yet strong baseline for parameter-efficient Transformer tracking. Our code and models will be released.

---


### 396. [Estimation is Not Enough: Carpet-Bombing Detection via Per-Packet Uniformity Testing](https://arxiv.org/abs/2609.33308)

**<font color=#1a73e8>作者：</font>** Yutong Yan, Sijia Du, Haowei Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Carpet-bombing attacks spread traffic uniformly across one or more destination IP prefixes, keeping every host in the prefix below alarm thresholds while exhausting prefix-level defenses. Existing carpet-bombing detectors run at seconds-to-minutes latency, too slow to respond within the attack window. Sketches support per-packet processing in fixed-width memory, a natural fit for cutting latency, yet no sketch-based detector exists for carpet bombing. Because source addresses can be spoofed, and attacks can be launched through reflection, source-side evidence is structurally unavailable and detection must anchor at the destination side. We present SweepSketch, the first sketch-based detection model for carpet bombing: it anchors at the destination, keeps no source state, and compresses a tagged self-cleaning T-HLL primitive, per-packet CUSUM decisions, and dual-EWMA change gates into 44-byte fixed-width buckets deployable on the Tofino2 programmable switch. Its design is supported by six theorems, including verifiable detection lower bounds. Under the same memory budget, SweepSketch leads all 10 baselines across the sketch, entropy, and sequential-testing classes in F1 (0.991). Its median alarm latency is 186--627 ms, and it has structural immunity to source spoofing. On 30 real/synthetic multi-prefix samples held out from parameter design, it detects all 140 victim prefixes.

---


### 397. [PIC-UIE: Predicting Image-Adaptive Corrections for Lightweight Underwater Image Enhancement](https://arxiv.org/abs/2609.33318)

**<font color=#1a73e8>作者：</font>** Cunhao Zhu, Dongliang Xu, Xiangtao Kong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Underwater image enhancement (UIE) aims to restore visibility, color fidelity, and structural detail from images degraded by wavelength-dependent attenuation and backscatter. State-of-the-art UIE methods often rely on large backbones and dense image-to-image prediction, limiting their practicality for edge deployment. Moreover, operating entirely in a single color space couples degradation estimation with luminance and chroma correction. To address these challenges, we propose PIC-UIE, a lightweight predictor--executor framework that predicts image-adaptive corrections from a fixed $256\times256$ RGB thumbnail and applies them to the native-resolution input in the YCbCr color space. The predictor produces seven outputs, organized into spatial correction, nonlinear luminance and coupled chroma mapping, and image-level color calibration. A depth map regularizes the transmission proxy during training, whereas inference uses only the RGB input. With 9,486 parameters and 0.094 GFLOPs at $256\times256$, PIC-UIE achieves 24.137 dB PSNR and 0.9216 SSIM on UIEB-90 and 21.320 dB PSNR on zero-shot LSUI. It further processes native 4K images at 55.0 FPS under the comparison protocol. These results show that structured correction prediction provides an effective and practical alternative to dense RGB reconstruction for underwater image enhancement.

---


### 398. [VisionHOPE: Visual Backbones as Self-Modifying Learning Systems](https://arxiv.org/abs/2609.33325)

**<font color=#1a73e8>作者：</font>** Siran Peng, Tianshuo Zhang, Tianyu Fu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual backbones have evolved from Convolutional Neural Networks (CNNs) with local aggregation to Vision Transformers (ViTs) with global interactions, State-Space Models (SSMs) with input-dependent state transitions, and Test-Time Training (TTT) layers that adapt an inner learner while processing an image. Across this progression, visual computation has become increasingly adaptive to each input, yet the rules governing that adaptation remain largely prescribed by the trained backbone. We introduce VisionHOPE, the first generic visual backbone formulated as a self-modifying learning system, in which what the model remembers and how it learns co-evolve within an image. Building on the self-referential construction of Nested Learning (NL), VisionHOPE realizes this co-evolution through five coupled memories that store content, generate key and value representations, and govern learning rate and retention. These memories evolve jointly as visual context accumulates along each scan. However, directly applying the unconstrained self-referential update to a visual backbone leads to instability. We therefore derive a stability-matched step-size control scheme that combines a soft cap on self-referential injection with a spectral clamp on the retained memory transition, and prove that the resulting memory dynamics are non-expansive along each scan. For two-dimensional feature maps, we adapt NL's chunk formulation by aligning chunks with image rows and columns across four directional scans. The proposed VisionHOPE achieves competitive results on ImageNet-1K, COCO, and ADE20K, establishing self-modifying learning systems as a practical foundation for general-purpose visual backbones. The code is available at this https URL.

---


### 399. [ANTMAN: Adaptive Need Tracking for Multi-Agent Navigation in Large Information Spaces](https://arxiv.org/abs/2609.33326)

**<font color=#1a73e8>作者：</font>** Jerry Wang, Haibo Jin, Xiaopeng Yuan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Information-seeking agents increasingly operate over information spaces that are too large to process exhaustively. Yet many multi-agent systems organize computation around static partitions of the available space, causing coordination to grow with how information is segmented rather than with what the query still requires. We introduce ANTMAN, an adaptive coordination framework that treats evolving unresolved information needs as the unit of runtime coordination. ANTMAN maintains a revisable Need Graph that tracks unresolved requirements, accumulated evidence, prior attempts, and search progress, and uses this state to control worker selection, routing, and task-local recovery as new evidence is discovered. By separating the coordination policy from substrate-specific search interfaces, the same need-conditioned mechanism can operate across different information spaces. Experiments across multi-document question answering, controlled long-context scaling, and realistic structured navigation show that ANTMAN remains effective across settings, including when execution is delegated to substantially smaller worker models. Under a 16x increase in searchable context, ANTMAN increases active coordination by only 1.23x, compared with more than 15x for partition-driven baselines, while preserving strong answer quality.

---


### 400. [FeCoSplat: Feedback-Guided Compression for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2609.33330)

**<font color=#1a73e8>作者：</font>** Yuxuan Li, Yihang Chen, Yufeng Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D Gaussian Splatting (3DGS) enables efficient novel-view synthesis from sparse multi-view images, yet its representations remain costly to store and transmit. Existing approaches compress either the input images, incurring heavy receiver-side reconstruction, or the reconstructed Gaussian primitives, which are difficult to compress due to their heterogeneous and irregular attributes. We instead compress compact intermediate features, providing a better balance between compression efficiency and receiver-side complexity. Based on this paradigm, we propose FeCoSplat, a feedback-guided compression framework for feed-forward 3DGS. FeCoSplat first compresses multi-view features to obtain an intermediate 3DGS, whose rendered views are used as feedback to guide a second-stage compression for further refinement. The resulting bitstreams are decoded into a compact implicit state, from which the final Gaussian primitives are reconstructed with a lightweight predictor. Experiments demonstrate that FeCoSplat achieves favorable rate--distortion performance, particularly at low bitrates, while requiring only 3.45M parameters for receiver-side Gaussian reconstruction. Code will be released soon.

---


> [!TIP]
> 当前位于：**351-400**（第 8/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
