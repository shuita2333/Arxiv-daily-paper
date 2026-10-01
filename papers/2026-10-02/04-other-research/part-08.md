# 📦 其他研究 | 2026年10月02日

> 本类共 **382** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-382**（第 8/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-382**

---

### 351. [PTNO: Training Neural Operators with Noisy Monte Carlo Estimates for Particle Transport Problems](https://arxiv.org/abs/2609.40090)

**<font color=#1a73e8>作者：</font>** Yubo Cao, Xi Deng, Mengqi Xia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Particle transport under multiple scattering is central to radiative transfer and plasma physics, yet high-fidelity Monte Carlo (MC) simulations must trace prohibitively many particles. Learning-based surrogates can amortize this cost, but typically train on expensive, well-converged MC solutions. We propose the Particle Transport Neural Operator (PTNO), a neural operator that learns particle transport surrogates directly from noisy, low-cost MC labels. Such labels pose two challenges: (1) high variance, which destabilizes standard supervised learning, and (2) a high dynamic range (HDR) spanning many orders of magnitude. For the first, we learn the solution operator from noisy labels of many configurations, amortizing MC cost and generalizing to unseen configurations. Because MC labels are unbiased, we show that the squared loss on them shares its minimizer with the loss on converged solutions, and our budget-allocation study over training scenes $M$, MC samples per render $N$, and independent renders per scene $K$ shows that many noisy scenes beat fewer converged ones. For the second, a nonlinear transform such as the logarithm biases noisy supervision. Instead, PTNO keeps labels in physical space and enforces positivity with a softplus output layer that represents small values effectively. We further train with a pointwise relative $L_2$ loss (PRelL2), the stop-gradient relative loss of HDR denoising and neural rendering, which normalizes each residual by the stop-gradient prediction instead of the noisy label. We demonstrate PTNO on neutron transport in fusion reactors and radiative transfer in participating media. On the two neutronics tasks, PTNO is $10^4$-$10^5\times$ faster than converged MC on the same CPU and $10^3$-$10^5\times$ cheaper than MC at matched accuracy; on the two radiative-transfer tasks, MC at matched accuracy costs $0.8$-$11\times$ as much as PTNO.

---


### 352. [GateSPINE: Gated Cross-View Fusion for Lumbar Spine MRI Report Generation](https://arxiv.org/abs/2609.40091)

**<font color=#1a73e8>作者：</font>** Hoang Nguyen Van, Cuong Vuong Tuan, Trang Mai Xuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated report generation can ease the burden radiolo gists face when interpreting multi-sequence MRI studies. Unlike CT, MRI examinations comprise multiple sequences and imaging planes, each con tributing complementary diagnostic information. Existing methods en code a study as a single volume and combine multiple acquisitions by fixed rules. Findings visible in only one plane are thus diluted and of ten missed, lowering recall on clinical efficacy metrics, where a missed abnormality is most costly. We propose GateSPINE, a vision-language framework that fuses sagittal T1 and T2 volumes with a training-free operator, encodes the fused sagittal and axial volumes with two parallel 3D encoders, and decodes their combined representation into a report. Its core mechanism is a gated cross view fusion module that predicts, per feature channel and token, how much of each view to admit, so the more informative view dominates at each spatial location. We evaluate GateSPINE on three lumbar MRI datasets, comprising two public bench marks and a private cohort collected from Phenikaa University Hospital, using both natural language generation (NLG) and clinical efficacy (CE) metrics. GateSPINE achieves the highest CE F1 through improved re call on all three datasets; on SPIDER, which lacks an axial sequence, this reflects the sagittal fusion component rather than the gated cross-view mechanism, which is validated on the two cohorts with both imaging planes. GateSPINE also remains competitive on standard NLG metrics.

---


### 353. [Unlearnable, or Unmeasured? On the Reliability of Difficulty Labels in RLVR](https://arxiv.org/abs/2609.40115)

**<font color=#1a73e8>作者：</font>** Chandak Chakma, Syed Nazmus Sakib, Nafiul Haque 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has become an important approach for improving reasoning during post-training. Recent work suggests that some difficult prompts remain resistant to learning even when they occasionally produce correct solutions. We revisit this unlearnability phenomenon and find that the affected prompts do improve, at roughly one third of the learnable rate, while the difficulty-defined set used to study them is much less reproducible than expected. These difficulty labels are estimated from a limited number of sampled responses. Combining them across seeds can further change which prompts are selected instead of simply reducing measurement noise. We develop a sampling-based framework for quantifying this instability and determining how much evaluation is required for difficulty assignments to reproduce reliably. We also revisit the gradient-similarity evidence proposed to explain unlearnability and show that part of the observed separation arises because difficult prompts provide fewer correct rollouts from which their gradients can be estimated. Matching this sample count weakens the gradient difference but does not remove it. Overall, the slow-learning phenomenon survives our reanalysis, while both the prompts used to define it and the evidence used to explain it require more careful measurement.

---


### 354. [Beyond Model Ranking: Regime Diagnosis for Distributional-Statistical Misspecification in Industrial Time-Series Forecasting](https://arxiv.org/abs/2609.40117)

**<font color=#1a73e8>作者：</font>** Pengyu Nie, Chenglang Xu, Yaoshi Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series forecasting models achieve strong benchmark performance but exhibit severe systematic bias in industrial deployments. This train--deploy gap is conventionally attributed to temporal-structural errors or distribution shifts. We characterize a complementary source that these explanations overlook: canonical losses embed fixed statistical priors, while industrial demand mixes benign and pathological regimes---zero-inflation, skewness, high variability---in which these priors are systematically violated. The induced bias persists even under perfect temporal modeling, remains in a distributional-shape component that normalization cannot remove, and creates an aggregation trade-off invisible to aggregate metrics. We turn these observations into an evaluation toolkit centered on the Regime-wise Relative Bias Vector (RBV): a metric-agnostic, regime-decomposed diagnostic that audits how pooled training allocates systematic mismatch across pathological subpopulations. A controlled attribution analysis decomposes RBV into a model-independent intrinsic floor, set by each loss's estimand, and an excess component attributable to training, tracing observed bias to the loss rather than the model. A large-scale study---13 loss objectives, 3 seeds, 60,000+ series spanning RetailShiftBench and M5, with random-split controls---shows that regime-aware diagnosis separates optimization-type from bias-type failure, and that regime-aware training resolves the pooling-induced bias that capacity scaling cannot, for mean-type losses. A formal structural observation, that risk under evaluation-distribution contamination is affine in the pathology mixture weight, grounds these findings. Our work complements model ranking with mechanism-grounded, regime-oriented evaluation.

---


### 355. [Scalable Cox Regression via Grouped Risk Sets and Sharper LogSumExp Rates](https://arxiv.org/abs/2609.40120)

**<font color=#1a73e8>作者：</font>** Elizaveta Iashchinskaia, Egor Gladin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Motivated by the computational challenges of large-scale Cox regression, we study stochastic minimization of LogSumExp objectives over large sets. Mini-batch normalizer estimates generally yield biased gradients. We instead use a softplus surrogate that introduces one auxiliary scalar per normalizer and admits unbiased single-sample gradients. For smooth convex LogSumExp objectives, we prove an $O(T^{-1/2})$ averaged objective bound, improving the previous $T^{-1/4}$ analysis. With a strongly convex regularizer on the original variable, we also obtain a last-iterate squared-error rate of $\widetilde{O}(T^{-1})$ without strong convexity in the auxiliary variables. For Cox regression, the normalizers are defined over nested risk sets. We exploit this structure by grouping neighboring failures and sharing one auxiliary variable per group. The resulting compressed objective admits uniform score and curvature bounds that control the errors from grouping and softplus approximation. Together with the general optimization result, these bounds give a mean-square rate of $T^{-4/5}$, up to logarithmic factors, relative to the full Cox solution. The compressed estimator also matches the full estimator's asymptotic distribution. Experiments on synthetic and real survival datasets with slowly decreasing risk sets show a favorable performance relative to stochastic baselines.

---


### 356. [Who Asked for This? Inline Annotations as Authoring Transactions for Provenance in Agentic Authoring](https://arxiv.org/abs/2609.40126)

**<font color=#1a73e8>作者：</font>** Chang Xiao  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Writing with AI agents turns a paragraph into the outcome of many requests, yet the finished document rarely explains which request produced which change. We introduce Reactant, an interaction paradigm in which authors place typed inline annotations in their original documents. A verified transaction protocol records each request, skill identity, and the correspondences that identify additions, deletions, and transformations. The kernel validates the witness against the recorded states to establish word-level longitudinal lineage. We demonstrate Reactant through this paper's revision history, and report four months of three colleagues' self-directed use. Their uses include conversational inquiry into history and deriving reusable skills from recurring requests, illustrating how the transaction record serves as an extensible substrate for agentic authoring.

---


### 357. [VR-JEPA: Learning Contrastive-State Latent Guidance for Generation-based Video Reasoning](https://arxiv.org/abs/2609.40129)

**<font color=#1a73e8>作者：</font>** Zehua Ma, Kun Xiang, Yunshuang Nie 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning through video generation offers a promising path toward visual intelligence by modeling latent visual states and their dynamics. However, current video generation models often lack explicit guidance on how these states should evolve, leaving generated trajectories prone to physical and structural inconsistencies that undermine reasoning reliability. While the Video Joint-Embedding Predictive Architecture (V-JEPA) provides rich spatiotemporal priors learned through latent prediction, these general priors do not naturally adapt to the logical reasoning capabilities required for complex visual tasks. To bridge this gap, we propose VR-JEPA, a framework that aligns the V-JEPA predictor with task-specific reasoning logic through localized contrastive-state learning and uses its predicted latent trajectories to guide video generation for visual reasoning. Specifically, (i) we pair successful trajectories with generated alternatives under the same input conditions and use discrepancies in their V-JEPA representations to identify informative states and tokens for localized contrastive supervision. (ii) We further equip the V-JEPA predictor with skill-specific experts trained on anchor-task data, allowing the model to adaptively specialize its shared spatiotemporal priors across diverse cognitive domains. Together with skill-specific experts, this contrastive supervision enables VR-JEPA to predict latent trajectories that provide task-specific logical guidance for video generation. Comprehensive experiments on the large-scale VBVR-Pro-Bench dataset demonstrate that VR-JEPA achieves an $11.33\%$ relative improvement over the cutting-edge generation-based reasoning baseline, significantly mitigating physical artifacts and enhancing logical consistency.

---


### 358. [Prototype-Rule Neurosymbolic Regularization for Rank-Constrained Tensor Neural Networks under Label Scarcity](https://arxiv.org/abs/2609.40131)

**<font color=#1a73e8>作者：</font>** Eftychios Protopapadakis, Konstantinos Makantasis, Konstantinos M. Giannoutakis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rank-constrained tensor neural networks reduce the parameterization of high-order inputs, but they do not explicitly constrain class geometry in the learned representation. This study investigates whether a differentiable prototype-rule can provide a complementary inductive bias for Rank-R tensor learning under limited supervision. The proposed framework augments the Rank-R objective with prototype-based regularization and optionally fuses prototype evidence with neural logits at inference. Four hyperspectral benchmarks are evaluated with four Rank-R configurations under both seven-fold stratification and spatially separated folds that mitigate leakage; a separate spatial study varies the class support budget from 2 to 20 samples. Under spatial evaluation, full neurosymbolic inference changes Macro-F1 score by +8.82 percentage points on Botswana, +5.49 on Indian Pines, +1.59 on Pavia University, and -0.62 on Salinas. Most of the benefit arises from training-time regularization, whereas inference fusion is small and dataset dependent.

---


### 359. [Game-Guided Skill Discovery through Self-Play for Playable Agent Control](https://arxiv.org/abs/2609.40137)

**<font color=#1a73e8>作者：</font>** Seungeun Rho, Jeonghwan Kim, Xue Bin Peng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present Game-Guided Skill Discovery (GGSD), a framework that uses self-play in games to discover motor skills that are directly playable by humans. Playable skills provide a compact abstraction for controlling embodied agents through a small set of learned behaviors rather than low-level actions. To be effective, these skills should be semantically distinct, interpretable, and expressive; properties that existing unsupervised skill-discovery methods often fail to achieve simultaneously. GGSD achieves these desiderata by grounding skill discovery in competitive gameplay. A hierarchical agent competes against its past selves, with a high-level policy selecting from a small discrete skill set and a skill-conditioned low-level policy learning the corresponding behaviors. After training, a human can replace the high-level policy and directly control the agent through the same discrete skills. Despite the small number of high-level actions, skill transitions give rise to emergent combo behaviors, expanding expressivity beyond individual primitives. Across Ant, Franka-arm, and Unitree G1 environments, we show that GGSD produces human-playable skills that humans can compose to solve unseen tasks, such as Maze and CubePush, without additional training. An interactive demo is available at this https URL.

---


### 360. [Policy Iteration Is Not Strongly Polynomial for Deterministic Markov Decision Processes: The Price of Algorithmic Anarchy](https://arxiv.org/abs/2609.40147)

**<font color=#1a73e8>作者：</font>** Han Zhong, Yinyu Ye  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We establish an exponential iteration lower bound in the number of states for Howard's policy iteration on deterministic discounted Markov decision processes, with at most two actions per state. This rules out strong polynomiality of Howard's policy iteration when the discount factor is part of the input and yields an exponential separation from the simplex method with Dantzig's pivoting rule, which is proved to be strongly polynomial on this class. Even when each reward is restricted to logarithmic bit length, we obtain a stretched-exponential iteration lower bound. The gap between Howard's decentralized and simultaneous selfish improvements and Dantzig's coordinated selection of a single action with the largest gain across all states reveals a ``price'' of algorithmic anarchy.

---


### 361. [Role-Adaptive Policy Optimization for Offline Reinforcement Learning](https://arxiv.org/abs/2609.40149)

**<font color=#1a73e8>作者：</font>** Seonvin Cho, Soohyun Choi, Songnam Hong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Policy regularization in offline reinforcement learning balances policy improvement against reliance on uncertain value estimates. This balance can differ between selecting actions for execution and supplying actions for critic bootstrapping, yet methods such as TD3+BC couple these roles through a shared policy. We propose Role-Adaptive Policy Optimization (RAPO), which adapts policy-update coefficients according to their roles in value learning and execution. RAPO learns these coefficients by differentiating through candidate policy updates formed using the base algorithm's actor objective. For TD3+BC, RAPO separates bootstrap and execution actors and adapts their coefficients independently: the bootstrap objective penalizes policy-induced changes in target values, while the execution objective evaluates a local policy-improvement surrogate. For IQL, whose value learning is already independent of the execution actor, RAPO preserves the original value updates and adapts only the inverse temperature in advantage-weighted policy extraction. Experiments on D4RL locomotion and AntMaze tasks show improvements over both base algorithms, with larger gains for TD3+BC, whose RAPO instantiation outperforms baselines on average.

---


### 362. [MANET-GNN: Learned Decentralized Optimization of Power Allocation in Multi-Channel MANETs](https://arxiv.org/abs/2609.40170)

**<font color=#1a73e8>作者：</font>** Tomer Alter, Nir Shlezinger, Michael Segal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> MANETs enable flexible infrastructure-less wireless connectivity in dynamic and resource-constrained environments. As modern MANETs exploit multiple frequency channels and support heterogeneous traffic patterns, decentralized transmit-power allocation becomes increasingly challenging. We develop a unified learned optimization framework for decentralized power allocation in dynamic multi-hop, multi-channel MANETs. We formulate a constrained end-to-end throughput maximization problem covering unicast, multicast, multicommodity, convergecast, and many-to-many communication. Although centralized and non-convex, this problem serves as an unsupervised training objective for MANET-GNN, a message-passing GNN that operates as a distributed learned optimizer. MANET-GNN uses only local, possibly noisy, CSI and a prescribed number of neighbor message exchanges, enabling low-latency decentralized inference while generalizing across topologies and network sizes. Numerical results show that MANET-GNN achieves centralized-competitive performance across communication frameworks, remains robust to channel uncertainty, and scales effectively across MANET configurations.

---


### 363. [Index-Translate: A Multilingual Translation Model Family -- Text, Speech, Controlled Dubbing, and Long-Document Translation](https://arxiv.org/abs/2609.40181)

**<font color=#1a73e8>作者：</font>** Tianjiao Li, Mengran Yu, Chenyu Shi 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Index-Translate, a multilingual translation model family that combines a shared multilingual foundation with specialized training for general translation, instruction following, speech translation, controlled dubbing, and long-document translation. It includes three model sizes, 2B, 9B, and 35B-A3B, and supports translation in 150 languages, with multilingual instruction following. Evaluations on general translation and complex translation instructions show that Index-Translate outperforms translation models of comparable size and achieves performance comparable to 100B-scale translation models and frontier models. Index-Echo provides end-to-end speech-to-text and speech-to-speech translation, outperforming existing end-to-end models and achieving performance comparable to frontier omni models. Index-Homura extends the family to syllable-controlled dubbing. Index-NativeLong introduces native long-document translation with a dedicated task formulation and benchmark. These capabilities support diverse translation tasks, including multilingual content production.

---


### 364. [Near-Linear Accuracy Bounds for Moreau--Yosida Unadjusted Langevin Sampling](https://arxiv.org/abs/2609.40193)

**<font color=#1a73e8>作者：</font>** Yuchen Xin, Zhihua Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We establish near-linear accuracy bounds for the classical Moreau--Yosida unadjusted Langevin algorithm (MYULA). The target is $\pi\propto e^{-f-g}$, where $f\in C^2(\mathbb{R}^d)$ is $m$-strongly convex with Lipschitz gradient and $g$ is convex and globally Lipschitz. Under an explicit parameter-dependent step-size condition, we bound the invariant-measure bias relative to the Moreau-smoothed target by $\widetilde O(h)$, with only logarithmic dependence on the inverse smoothing parameter in the error coefficient. Combining this estimate with the Moreau approximation bias and Wasserstein contraction gives $\widetilde O(\varepsilon^{-1})$ iterations to make the $N$th-iterate law $\mu_N$ satisfy $\sqrt m\,W_2(\mu_N,\pi)\le\varepsilon$, for fixed model parameters and initialization. We bound the stationary error directly, without assuming third derivatives or a Lipschitz Hessian. Each iteration uses one gradient evaluation and one exact proximal evaluation. The key idea in our analysis is to convert a second-order stationary residual into a Wasserstein bound using a Poisson-based estimate.

---


### 365. [MemLife: Curating and Reasoning over Long-Term Egocentric Video Memories](https://arxiv.org/abs/2609.40195)

**<font color=#1a73e8>作者：</font>** Guangzhi Xiong, Xinyuan Zhang, Xiao Yang 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-term egocentric video enables personalized AI assistants to reason about daily life. However, as video histories grow to hundreds of hours spanning months or years, reprocessing raw clips for every query becomes computationally prohibitive. Memory systems offer a scalable alternative by compacting videos into text representations, but often fail on practical benchmarks: either the memory does not preserve key evidence, or the retriever fails to locate relevant entries due to retrieval competition in growing search spaces. To address these challenges, we introduce MemLife, a multimodal memory system that constructs entity-grounded, first-person text episodes and retrieves them via a time-indexed agentic reader. Without training or query-time video access, MemLife improves over the strongest training-free baseline by 4.6--12.0% across four long-horizon benchmarks. To further improve memory quality, we propose MemOpt, a reinforcement learning framework that optimizes the memory writer to produce faithful, informative, and retrievable memories. MemOpt consistently improves MemLife by 2.7--5.0% across different video and question distributions, with gains that generalize across writer and reader backbones and memory systems.

---


### 366. [Recognition of Urbanized Areas in UAV-Derived Very-High-Resolution Visible-Light Imagery](https://arxiv.org/abs/2609.40212)

**<font color=#1a73e8>作者：</font>** Edyta Puniach, Wojciech Gruszczyński, Paweł Ćwiąkała 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This study compared classifiers that differentiate between urbanized and non-urbanized areas based on unmanned aerial vehicle (UAV)-acquired RGB imagery. The tested solutions in-cluded numerous vegetation indices (VIs) thresholding and neural networks (NNs). The analysis was conducted for two study areas for which surveys were carried out using different UAVs and cameras. The ground sampling distances for the study areas were 10 mm and 15 mm, respectively. Reference classification was performed manually, obtaining approximately 24 million classified pix-els for the first area and approximately 3.8 million for the second. This research study included an analysis of the impact of the season on the threshold values for the tested VIs and the impact of image patch size provided as inputs for the NNs on classification accuracy. The results of the con-ducted research study indicate a higher classification accuracy using NNs (about 96%) compared with the best of the tested VIs, i.e., Excess Blue (about 87%). Due to the highly imbalanced nature of the used datasets (non-urbanized areas constitute approximately 87% of the total datasets), the Mat-thews correlation coefficient was also used to assess the correctness of the classification. The analysis based on statistical measures was supplemented with a qualitative assessment of the classification results, which allowed the identification of the most important sources of differences in classification between VIs thresholding and NNs.

---


### 367. [Learning Skills from Historical Action Trajectories: Action Experience Dictionary for World Action Models](https://arxiv.org/abs/2609.40219)

**<font color=#1a73e8>作者：</font>** Qi Lyu, Jiahua Dong, Hao Shen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World Action Models (WAMs) couple visual dynamics prediction with action generation, yet they do not explicitly support the reuse of action experience across manipulation tasks. Furthermore, existing WAMs struggle to capture underlying cross-task semantic relationships that could guide target action prediction, as redundant background elements interfere with the extraction of key visual information. To address these challenges, we develop a novel Action Experience Dictionary (AED) that encodes historical physical action trajectories into shared action embeddings to support skill reuse and model cross-task relationships. Specifically, we first aggregate historical actions to align with visual observations and retrieve action embeddings from the AED using a pretrained action tokenizer. Subsequently, we visually condition the pooled embeddings through cross-attention and prepend them to noisy action tokens, providing interaction context and action intent for prediction. To model action-related motion and reduce reliance on irrelevant background cues, we introduce a motion-aware transition loss that supervises visual feature change prediction over random temporal intervals. Experiments on simulation benchmarks and in real-world cross-embodiment settings verify the effectiveness of our AED. The anonymous project website is available at \href{this https URL}{AED}.

---


### 368. [LOCI: Spatial Linear Memory for Streaming World Models](https://arxiv.org/abs/2609.40222)

**<font color=#1a73e8>作者：</font>** Ji Xia, Tingting Liao, Xuezhi Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When a camera revisits a previously observed region, a video world model should reproduce what was there before. This requires both remembering past observations and retrieving the right one for the current viewpoint. Key-value caches preserve visual detail but grow with video length; recurrent memory is compact but compresses history into a fixed-size state, so individual past observations are no longer directly accessible. We introduce LOCI, a hybrid spatial-memory architecture that keeps both representations. In half of the transformer blocks, main attention keeps a key-value cache of past observations; in the other half, it is restricted to the current chunk and complemented by a recurrent linear-attention memory whose reads and writes are conditioned on projective camera geometry, so viewpoint enters both memory addressing and stored content. Recurrent readouts flow into subsequent cache-backed blocks and supply their queries with accumulated scene context. On the public MIND memory benchmark and on held-out recorded trajectories, LOCI reproduces revisited content more faithfully than representative world models and a same-recipe full-softmax model; with full history, it lowers peak memory at equal length by about 30% relative to full softmax. With a bounded bank of retained observations, it streams long videos at constant memory and remains more faithful than full softmax under the same budget.

---


### 369. [StreamRig: Exploiting Intra-Rig Geometry for Streaming Multi-Camera Odometry](https://arxiv.org/abs/2609.40244)

**<font color=#1a73e8>作者：</font>** Yufei Wei, Shuhao Ye, Qi Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mobile robots and vehicles carry synchronized multi-camera rigs, yet many streaming 3D foundation models are designed for monocular input, leaving efficient use of rig geometry a challenge. We present StreamRig, a freeze-and-stream framework that builds causal streaming odometry for calibrated rigs on a frozen multi-view 3D foundation model. The frozen front-end jointly perceives the synchronized views using rig calibration. A Rig-Resampler compresses their features, a CausalBridge applies causal attention with a key-value cache, and a lightweight head regresses rig poses. A periodic re-anchoring protocol supports stable pose estimation over long sequences. Only these modules are trained, 74.6M parameters in total, with relative poses as the sole supervision. Our two-stage training strategy combines group relocalization pretraining with causal rig training to transfer the geometric priors of the frozen front-end and the alignment ability of the pretrained modules to streaming odometry. We evaluate on NCLT, TartanGround, KITTI-360, and our self-collected humanoid-robot dataset ZJH, where training uses only simulation and real-world evaluation is zero-shot. Across all four datasets, StreamRig achieves lower translation and rotation drift than the evaluated non-oracle monocular streaming and rig-aware offline models, while maintaining low inference cost. Ablations and controlled camera-count experiments identify the sources of these gains. We further examine how longer training windows affect inference over longer horizons. Code has been released at this https URL.

---


### 370. [Belief-Aware Multi-Agent Path Finding under Map Uncertainty](https://arxiv.org/abs/2609.40269)

**<font color=#1a73e8>作者：</font>** Viraj Parimi, Shao-Hung Chan, Han Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-Agent Path Finding (MAPF) aims to find collision-free paths for multiple agents in a shared environment. Classical MAPF assumes that all static obstacles are known in advance, but real-world environments can change unexpectedly due to fallen objects, spills, or other local disturbances. When such changes are spatially correlated, an observation can inform traversability estimates beyond the observed location. Prior approaches address uncertainty in traversability through contingent plans or replanning based on direct observations, but do not leverage this spatial dependence to infer the traversability of nearby unobserved locations. As a result, they cannot use one observation to anticipate nearby unobserved obstacles that may cause costly rerouting later. We focus on Belief-Aware MAPF, where map discrepancies are fixed during execution but initially unknown, and observations can be informative beyond the observed location. We propose Multi-Agent Gaussian belief Inference for Coordination (MAGIC), a framework that updates a shared belief about traversability online based on agents' observations. MAGIC uses a Gaussian Markov Random Field and Gaussian Belief Propagation to approximately infer traversability and construct detour-aware costs for standard MAPF planners. Our experiments on MAPF benchmarks show that MAGIC reduces the executed sum of costs compared to existing approaches on 96.3% of instances, across several planner families and teams of up to 800 agents, demonstrating its applicability to large-scale MAPF problems.

---


### 371. [PMosFM: Preconditioned Manifold Matching for One-Step Physics-Constrained Generation](https://arxiv.org/abs/2609.40287)

**<font color=#1a73e8>作者：</font>** Zhangyong Liang, Haibin Ling  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-constrained generative models aim to generate physical fields that match a target distribution and satisfy prescribed constraints. However, enforcing these constraints often increases sampling costs through iterative corrections or training costs through residual optimization and trajectory unrolling. To address this issue, we introduce \textbf{P}reconditioned \textbf{M}anifold \textbf{o}ne-\textbf{s}tep \textbf{F}low \textbf{M}atching (\textbf{PMosFM}), a preconditioned manifold matching framework for one-step physics-constrained generation. By encoding constraints in a manifold decoder, PMosFM learns transport in intrinsic coordinates without separate residual losses or terminal residual unrolling. A geometric preconditioner rescales coordinates using the decoder-induced metric, while a regularized covariance transform approximately whitens the interpolation-state inputs. A finite-interval objective couples velocity supervision with consistency between decoded endpoints in physical space. We show that exact parameterization removes residual-induced Gauss--Newton curvature, that geometric and covariance effects separate in a local conditioning bound, and that physical flow-map error bounds endpoint distributional error. Controlled ablations examine conditioning, and experiments evaluate optimizer-update time and memory footprint. At inference, PMosFM uses one neural transport evaluation followed by physical decoding. Experiments across benchmarks show lower training and sampling time than the multi-step baselines at comparable physical and distributional fidelity. Code and datasets will be released publicly.

---


### 372. [Disentangling Computation in Multi-Task Neural Networks with the Green's Operator](https://arxiv.org/abs/2609.40292)

**<font color=#1a73e8>作者：</font>** James Hazelden  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How is computation organized and reused across tasks and time in a trained recurrent network? Most analyses emphasize the geometry of neural activity, dynamical motifs, or local perturbation growth. We instead study the network's global first-order perturbation response. The finite-horizon Green's operator maps perturbations at each source along a trajectory to their downstream state-space responses and therefore directly represents perturbation routing. Simple reductions of this operator provide task-to-task and time-to-time views of the same computation, while matrix-free products make these views accessible without constructing the full operator. In a flexible multitask recurrent network, task reductions reveal structured reuse of known computational motifs, while temporal reductions reveal causal pathways and how they emerge during training. Our main point is simple: the Green's operator provides a global response geometry for mapping the organization of learned dynamical computation.

---


### 373. [Looped Diffusion Transformer](https://arxiv.org/abs/2609.40305)

**<font color=#1a73e8>作者：</font>** Yong Xien Chng, Tianyi Chen, Wenwen Tong 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Improving text-to-image models has traditionally relied on increasing model size or the number of denoising steps. In this work, we explore an alternative way to scale computation by repeatedly running shared Transformer blocks within each denoising step, effectively increasing computational depth while keeping the parameter count fixed. This looped computation enables iterative refinement of internal representations without explicit reasoning tokens. However, naive looping fails to consistently improve image quality. We trace this problem to weak supervision across intermediate loops and unregulated attention updates that progressively erode local information. To overcome these challenges, we propose Looped Diffusion Transformer (Looped-DiT), which combines deep supervision across intermediate loops with self-modulating attention to stabilize looped feature updates. Under matched-parameter and matched-compute settings, Looped-DiT consistently outperforms non-looped baselines. Notably, a 260M-parameter looped model can surpass a model 6.5x larger across multiple text-to-image benchmarks while requiring 4.9x lower inference compute. Beyond this performance gain, we find that looped computation can offer a more effective form of iterative computation for diffusion models, with increasing loop depth yielding larger gains than adding more denoising steps under a fixed inference budget. Furthermore, deeper loops can progressively correct mistakes made in earlier loops, exhibiting behaviors suggestive of latent reasoning. Together, these results show that looped computation offers a promising way to scale visual generation models.

---


### 374. [Compression Footprints as Security Signals for Model-Poisoning Defense in Federated Learning](https://arxiv.org/abs/2609.40312)

**<font color=#1a73e8>作者：</font>** Sachi Shome, William Eiers  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lossy compression is widely used in Federated Learning (FL) but is generally treated as an error source, while conventional poisoning defenses inspect update geometry. In this work, we instead treat the compressor's response as a security signal: the input-dependent distortion and payload behavior induced by lossy compression can expose differences between honest and attack-generated updates. We introduce the concept of a \emph{compression footprint}: the low-dimensional collection of reconstruction, directional, sparsity, and payload statistics induced by a lossy compressor. We characterize sufficient conditions under which compression footprints separate honest and malicious updates, and operationalize our findings in the CRAFT (\emph{Compression-guided Robust Aggregation via Footprint Trust}) server-side robust aggregation method. Crucially, under a strict honest-majority assumption, CRAFT uses server-verifiable footprints, requires no client-side metadata nor knowledge of the number of malicious clients, and adds no communication beyond the compressed FL pipeline. Moreover, while CRAFT assumes a strict honest majority, it does not require the number of malicious clients to be known in advance. We observe that error-bounded lossy compressor (EBLC) footprints provide stronger separation than Top-K footprints and that footprint trust suppresses malicious influence. We evaluate CRAFT under IID client data with 36\% malicious participation across six standard model-poisoning attacks, three datasets, and six robust aggregation baselines, finding that CRAFT consistently achieves the best accuracy in 7 out of 18 settings and within 1.7 percentage points of the best in the others. Our results show that lossy compression can serve as both a communication mechanism and a security signal for robust aggregation in FL.

---


### 375. [Atomizer-IO: Beyond Pixels, Patches and Grids](https://arxiv.org/abs/2609.40320)

**<font color=#1a73e8>作者：</font>** Hugo Riffaud de Turckheim, Sylvain Lobry, Nicolas Houdré 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most vision architectures assume that observations lie on a regular grid, an effective abstraction for natural images but a restrictive one for sensing data whose channels, temporal sampling, spatial resolution, and geometry can vary. Generic set-based architectures remove the grid, but also remove useful spatial inductive biases. We introduce Atomizer-IO, an architecture that places observations first and derives structure from their physical relationships. Building on top of an atomic representation of the data, each observation is described by its measurement and acquisition metadata, while local cross-attention maps observations to anchor points that can be arbitrarily placed. We evaluate this design by progressively relaxing the grid assumption, from varying input raster configurations and incomplete channel sets to flexible output density and, ultimately, inputs without a raster grid. Atomizer-IO is competitive with flexible EO-specific architectures on most tasks, while offering post-training control over inference cost and competitive compute--performance trade-offs. The same formulation extends without architectural redesign to unordered 3D point clouds, showing that the atomic interface generalizes beyond regular raster inputs. These results suggest that pixels, patches, and grids do not need to define the interface of a sensing architecture.

---


### 376. [Turbo Harness: Instance-Adaptive Harness Optimization](https://arxiv.org/abs/2609.40330)

**<font color=#1a73e8>作者：</font>** Tunyu Zhang, Hao Wang, Kai Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automating the search for effective harnesses is an important step toward enabling agents to recursively self-improve. Existing harness optimizations typically produce a single global harness that is applied uniformly across task instances. However, a harness that works well on average may not be optimal for every instance. We introduce Turbo Harness, a framework that can adapt a globally optimized harness to each instance by reusing information generated during the original optimization process. Specifically, Turbo Harness recycles artifacts produced during a completed global harness optimization run, and summarizes them into a structured playbook. We train a harness editor to leverage this prior optimization experience to generate instance-specific patches to the global harness. At inference time, the editor uses the instance and the playbook to construct a tailored harness in which the execution model operates. Through numerical experiments, we show that Turbo Harness consistently outperforms existing harness optimization baselines across seven benchmarks spanning interactive agent tasks, software engineering, and long-horizon terminal tasks.

---


### 377. [I Have a Stream: Making Self-Supervised Learning Work on Continuous Video](https://arxiv.org/abs/2609.40333)

**<font color=#1a73e8>作者：</font>** Ivan Martinović, Lukas Knobel, Yuki M. Asano  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning draws inspiration from infant visual development, yet standard training pipelines bear little resemblance to it: images are independently sampled and globally shuffled across epochs. We study self-supervised learning from continuous video streams, where frames are consumed in temporal order using strict sliding-window batches, without global reshuffling or multi-epoch replay. To this end, we construct WT++, a 95-hour urban walking-tour video dataset for streaming pretraining. Combined with a comprehensive evaluation suite we find that contrastive and distillation-based methods struggle in this setting, while MAE is more robust but still falls short of standard i.i.d. pretraining. We find that high inter-batch similarity, caused by sliding-window consumption across consecutive batches, does not explain this gap. The main challenge is high intra-batch similarity, where frames within each batch are near-duplicates. To mitigate this, we propose StreamMAE, which preserves the core MAE reconstruction objective while adapting the input pipeline with stream-aware regularization and motion-biased crop selection. StreamMAE outperforms streaming baselines, matches i.i.d. MAE trained on the same video data, remains competitive with ImageNet-pretrained MAE, and scales positively as the pretraining stream grows from 12 to 95 hours.

---


### 378. [Image Classifiers are Efficient Self-Supervised Video Representation Learners](https://arxiv.org/abs/2609.40347)

**<font color=#1a73e8>作者：</font>** Owais Iqbal, Sudipta Sarkar, Shyam Marjit 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce VideoMSN, a Masked Siamese Network framework for efficient self-supervised spatio-temporal representation learning in videos. Instead of relying on heavy 3D architectures or reconstruction-based autoencoders for learning with unlabeled data, we repurpose standard image Vision Transformers by representing videos as super images which are grids composed of frames sampled from videos. From each super image, we construct two views: one with spatial patch masking and the other with temporal frame masking, ensuring no information leakage across frames. A shared Vision Transformer (ViT) encoder aligns their embeddings using a masked Siamese loss, capturing both motion and appearance cues without reconstruction. Our decoder-free formulation leverages an image foundation model towards efficient video representation learning. Starting from pretrained DINO-v3 and DeiT-v3 image encoders, VideoMSN achieves state-of-the-art performance on Kinetics-400, UCF101, and HMDB51 while requiring up to $32\times$ fewer and $160\times$ fewer video pretraining epochs compared to prior video self-supervised learning methods. Our proposed approach also shows strong performance in low-shot classification, confirming the transferability of the learned representations in a label-scarce scenario. Project Page: this https URL.

---


### 379. [AssemblyWorld: Rethinking 3D Assembly with General-Purpose Agents](https://arxiv.org/abs/2609.40353)

**<font color=#1a73e8>作者：</font>** Jiahao Zhang, Yeying Fan, Moitreya Chatterjee 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The task of 3D assembly requires translating an understanding of parts and their relationships into precise spatial arrangements. Can pretrained general-purpose agents assemble objects through visual interaction without additional assembly-specific fine-tuning? To investigate this question, we introduce AssemblyWorld, an interactive 3D environment in which agents inspect rendered views and manipulate supplied rigid parts, guided by images or assembly manuals when available. Agents perceive part geometry through 2D views rather than direct access to mesh vertices or faces, while their resulting assemblies are evaluated geometrically. Building on this environment, we construct AssemblyWorldBench, comprising 100 assembly tasks across 80 objects spanning furniture, industrial assembly, and fracture reassembly. Evaluating eight agent systems reveals substantial differences in their capabilities. The strongest system achieves 80.9% part accuracy but 59.4% complete-assembly success. The evaluated open-source systems lag substantially behind their stronger closed-source peers in both execution reliability and assembly accuracy. Analyses of visual references, interaction trajectories, and failures show how agents revise assemblies while leaving residual positioning errors. AssemblyWorld provides a common setting for both assessing the capabilities of interactive assembly agents and characterizing the gap between approximate structure recovery and precise reconstruction.

---


### 380. [ViTeX-Bench: Benchmarking High-Fidelity Video Scene Text Editing](https://arxiv.org/abs/2609.40356)

**<font color=#1a73e8>作者：</font>** Xinghao Chen, Xiangbo Gao, Jiongze Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent video generation is increasingly realistic and controllable, yet video editing remains less developed, particularly for precise local edits that must preserve the original scene dynamics. Video scene text editing replaces text on scene surfaces, such as storefront signs, whiteboards, and product labels, while preserving the surrounding content, motion, and camera dynamics. Although scene text editing is well studied for images, video scene text editing that achieves high visual quality, temporal consistency, and edit locality remains underexplored. Existing resources offer limited paired real-video data, and general video-editing metrics do not directly measure whether the requested text remains correct over time. We introduce ViTeX-Bench, a benchmark suite comprising ViTeX-Dataset and a three-axis evaluation protocol. The dataset contains 387 real-world 720p videos with text-region masks and editing instructions: 230 provide reviewed, pipeline-generated paired edits for training, and 157 form a frozen evaluation split. The protocol evaluates text correctness, visual and temporal quality, and edit locality through 13 metrics, with one primary metric per axis and a Pareto comparison of their trade-offs. OCR calibration, human evaluation, and annotation-sensitivity analyses support the interpretation of these scores. Across eight baselines from four editing families, accurate text, temporal stability, and scene preservation remain difficult to achieve together. We also release ViTeX-Edit-14B, an open-source reference editor fine-tuned on the paired training split with motion-aligned glyph-video conditioning. It achieves CharAcc 0.688, the highest mean among the evaluated video-native editors, and the lowest comparable text-crop Warp among raw editor outputs. ViTeX-Bench provides a reproducible foundation for studying these trade-offs in video scene text editing.

---


### 381. [Physis-Lang: Self-Evolving Language as a Physical Representation for Video World Model](https://arxiv.org/abs/2609.40358)

**<font color=#1a73e8>作者：</font>** Liming Lu, Xianzheng Ma, Wenkun He 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models are expected to predict how the physical world evolves, yet they often produce visually plausible videos that violate basic physical principles. Existing approaches commonly assume that natural language is insufficient to represent the physical knowledge required for reliable generation, and therefore introduce additional visual, latent, numerical, or planning-based signals. We revisit this assumption and introduce Physis-Lang, a self-evolving framework that treats physical language as a shared and optimizable representation across data curation, model training, and video generation. Physis-Lang represents physical processes through language that describes their relevant entities, causes, interactions, governing principles, temporal evolution, and effects. To improve this representation, we construct PhysCapBench, which decomposes physical processes into atomic assertions and evaluates captions using recall and precision. An agentic loop iteratively analyzes assertion-level errors and refines the instruction used to produce physical captions. Physis-Lang further converts model deficiencies into textual descriptions and uses language-guided retrieval to identify visually diverse videos that cover missing physical processes. Experiments on four widely used physical video benchmarks with Wan and Cosmos backbones demonstrate consistent improvements in physical plausibility. Notably, starting from open-source Cosmos3-Nano backbones, our Physis-Lang-enhanced models surpass the leading proprietary Veo 3.1 model.

---


### 382. [Multimodal Flow: Unified Flow Modeling of Language and Vision in Embedding Spaces](https://arxiv.org/abs/2609.40362)

**<font color=#1a73e8>作者：</font>** Hongyuan Tao, Xinggang Wang, Lianghui Zhu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Multimodal Flow, a fully continuous generative model of language and vision. Most unified multimodal models either model both language and quantized images as discrete tokens or combine discrete language prediction with continuous image generation. The former introduces a visual quantization bottleneck. The latter requires modality-dependent objectives and sampling procedures. Fully continuous modeling avoids these trade-offs and enables a shared generative process, but remains underexplored for multimodal pretraining. Multimodal Flow introduces a unified continuous architecture that integrates multimodal continuous representations with a shared chunk-causal flow backbone. It organizes text blocks and images as ordered continuous hyperchunks, preserving textual token order and visual spatial structure. The backbone learns a single vector field over these hyperchunks through Flow Matching. Joint attention enables cross-modal interaction, while modality-specific feed-forward networks process each modality. The model predicts multiple target chunks in parallel during training and generates hyperchunks sequentially at inference. We instantiate MF-1 and pretrain it on multimodal data. Across 0.6B, 1.2B, and 1.6B scales, continued pretraining consistently improves multimodal modeling. With only 150B pretraining tokens, MF-1 achieves an average score of 82.8 across GenEval and DPG-Bench and 75.3 across VQAv2, MMBench, and POPE, remaining competitive with unified models trained on substantially more data. Under matched data, optimization, and parameter budgets, Multimodal Flow further outperforms representative hybrid and discrete models. These results establish continuous chunk-based embedding flow modeling as a new fully continuous paradigm for unified multimodal modeling. The related code and model are publicly released at this https URL.

---


> [!TIP]
> 当前位于：**351-382**（第 8/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-382**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
