# 📦 其他研究 | 2026年10月06日

> 本类共 **260** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-260](./part-06.md)

---

### 101. [Adaptive Spectral-Koopman Dynamics Modeling for Temporal Domain Generalization](https://arxiv.org/abs/2610.02822)

**<font color=#1a73e8>作者：</font>** Tengxue Zhang, Yu Ke, Yang Shu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal Domain Generalization (TDG) has emerged to address real-world streaming data with distribution shifts over time. However, existing methods are either prone to overfitting to domain-specific noise in the data space or become overly complex and less interpretable in the parameter space. To bridge these gaps, we propose \textbf{AdaSpecK}, a spectral-Koopman framework with adaptive context extraction for TDG. To mitigate noise fitting to irregularly sampled domains, we introduce spectral-regularized Koopman dynamics modeling, which applies spectral-aware filtering in the latent space to extract denoised low-frequency trajectories and learn a Koopman operator to model the system dynamics in a linearized space. To model complex historical environments under non-stationarity, we design a context-informed heterogeneous pattern extraction mechanism. Specifically, we employ a target-conditioned attention module to attend to distinct past windows, producing a dynamic, target-specific historical summary. By constructing an environmental signature from the current evolutionary pattern, our model adaptively perceives which aspects of the past context are most informative for future prediction via a learned router. Extensive experiments on eight diverse classification and regression benchmarks demonstrate that AdaSpecK achieves state-of-the-art performance. The code and datasets are available at \href{}{this https URL}.

---


### 102. [TerrainForge: Physics-Grounded road geometry Editing for Counterfactual Autonomous Driving](https://arxiv.org/abs/2610.02825)

**<font color=#1a73e8>作者：</font>** Yang Chen, Yicheng Zhu, zhenning Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Road geometry (e.g., crests, sags, and speed humps) and surface conditions (e.g., wet or icy pavement) affect how vehicles move, what drivers and onboard cameras observe, and how much clearance remains between vehicles. Editing these properties in a driving scene therefore requires corresponding changes in vehicle motion. Capturing these differences in a driving video requires a road edit to propagate to vehicle motion, camera viewpoint, and the clearance between vehicles. We present TerrainForge, a framework for generating road geometry-focused counterfactuals from reconstructed multi-vehicle driving episodes. A unified road model connects scene deformation with four-wheel vehicle dynamics, allowing crests, sags, speed humps, and friction changes to propagate through vehicle motion, camera viewpoint, and inter-vehicle clearance. Vehicle dynamics are evaluated against CarSim, and prescribed road geometry is verified in reconstructed Waymo scenes. Across 18 episodes, leaving surrounding vehicles on their recorded trajectories instead of recomputing their responses produces median peak differences in predicted ego-lead distance of 1.52 m for crests and 1.41 m for sags. We further simulate the ego response to 15,758 road edits across 983 braking episodes, pairing each edit with its safety outcomes relative to an unedited replay. These pairs train a first-stage screening surrogate that takes the original driving context and candidate road-edit parameters as input and predicts the resulting change in the ego's terminal gap. On held-out scenes, this prediction achieves 22-40% lower mean absolute error than predicting no change, so candidates can be screened cheaply before the full multi-vehicle rollout.

---


### 103. [Turnover-Orthogonal Credit Assignment for Open-Team Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2610.02847)

**<font color=#1a73e8>作者：</font>** Amit Thakur, Mukesh Singhal  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Open-team multi-agent reinforcement learning studies cooperative systems in which agents may join, leave, or be replaced during an episode. In such settings, the team return changes both because agents choose useful actions and because the active population itself changes. Standard centralized critics and shared advantages often mix these two effects into one scalar credit signal, allowing surviving agents to be rewarded or penalized for exogenous turnover events outside their control. We introduce turnover-orthogonal credit assignment (TOCA), a value decomposition for open teams that separates action effects, pure turnover effects, and action--turnover interactions. Under exogenous turnover, the event-conditioned value admits a centered decomposition whose event-conditioned baseline removes the pure turnover component while preserving credit for actions that make the team robust to future replacements. We instantiate this idea with a permutation-invariant centralized critic over variable-size agent sets and event tokens, and derive both a counterfactual per-agent credit signal and a softly weighted interaction variant, TOCA-$\beta$, for high-variance control environments. Controlled diagnostic experiments show that TOCA improves return over event-aware MAPPO-style critics and that removing interaction credit substantially hurts performance. In a replacement-only Dynamic Spread benchmark, TOCA-$\beta$ achieves the best mean return at high turnover rates and improves over its no-interaction ablation. These results suggest that explicitly separating turnover from action credit is a useful principle for robust learning in dynamic cooperative teams.

---


### 104. [Counterfactual Action Evaluation, Observation Bottlenecks, and Representation Geometry in Joint-Embedding Predictive World Models](https://arxiv.org/abs/2610.02860)

**<font color=#1a73e8>作者：</font>** Arjun Subramanian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low latent prediction error does not establish that a world model distinguishes the consequences of its actions. We introduce an evaluation protocol that traces the same intervention through simulator state, raster observations, target embeddings, and predictor outputs. Exact simulator-state forks in a controlled deformable-physics testbed reveal distinct bottlenecks. Changed commands alter particle motion, yet 41.5% of one-step raster pairs are identical. Observation loss is not the whole explanation: among 579 high-visibility counterfactuals, median predictor-to-target response is 0.0051 and 0.0217 across two seeds, falling to 0.0027 and 0.0116 after variance normalization. An isotropic state perturbation matched to the target counterfactual embedding shift produces 190x and 53x larger predictor changes on the same visible pairs, isolating action-path under-use rather than a dead or globally shrunk predictor. MSE-only training gives 8.36x lower 10-step latent error in matched seeds, but in spectrally concentrated spaces; one VICReg target encoder is also strongly concentrated, so neither error nor rank alone certifies physical state. Finally, stiffness remains near chance even from full-resolution rasters and mechanical state while privileged material parameters decode perfectly, indicating weak identifiability under this excitation rather than encoder discard. These results motivate auditing physical effect, observation visibility, representation geometry, and action dependence separately.

---


### 105. [NeuroLens: Learning Latent Embeddings of Neural Semantics from Chronic Recordings](https://arxiv.org/abs/2610.02864)

**<font color=#1a73e8>作者：</font>** Hanrui Lyu, Baiyuan Chen, Tianshu Tan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding how neural activity represents higher-order cognition and how these representations evolve over time has long been a central pursuit in neuroscience. However, current analytical tools cannot easily distinguish representational plasticity from recording instability in chronic neural recordings. Here, we introduce NeuroLens (Latent Embeddings of Neural Semantics), a self-supervised model based on the Joint-Embedding Predictive Architecture (JEPA) framework that learns denoised, semantically informative latents from chronic neural recordings. An adaptive encoder maps changing neural populations into a common latent space, while a temporal predictor learns structure that supports prediction of future latent states. By predicting in latent space, NeuroLens captures temporally predictable structure and reduces sensitivity to transient, recording-specific variability. Across chronic intracortical data in mice and humans, the learned representations improve decoding of decision-making and semantic task variables. Multi-day pretraining enables generalization to future sessions, rapid few-shot adaptation to unseen neural populations, and more stable decoding over time than state-of-the-art baselines. Together, these results establish NeuroLens as a new paradigm for studying how neural representations change during learning and over long timescales.

---


### 106. [On Unlearning for Time-series Forecasting](https://arxiv.org/abs/2610.02865)

**<font color=#1a73e8>作者：</font>** Zeyu Shi, Yanhui Luo, Ziming Hong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series forecasting is widely used in sensitive domains. Models in these settings are often trained on longitudinal user- or entity-level records, which may later require removal because they contain sensitive or proprietary information or have been corrupted by sensor failures. To address such deletion requests without costly retraining, machine unlearning has been widely studied as a practical mechanism for privacy protection and data governance. However, the application of machine unlearning to time series prediction has not yet been well realized; this is mainly due to the following unique challenges: Gradient-based unlearning can be unstable because a deleted observation participates in multiple causally connected forecasting windows, causing parameter updates to propagate beyond the requested interval and degrade retained forecasting utility. Label-guided updating offers a more controlled alternative, but continuous and context-dependent forecasts lack a suitable replacement target, while the exact-retrained output is unavailable during unlearning. Moreover, the remaining support for a deleted temporal pattern is highly non-uniform. Some affected windows retain structurally similar counterparts in the retained data, whereas others become underrepresented or isolated. We present RDTU, a Residual Diffusion framework for time-series unlearning. RDTU first uses a retained-set neural tangent kernel predictor to obtain a deletion-compatible base forecast. Then it quantifies the global and local structural support of each affected window using the volume contribution of the retained-reference data. Then a diffusion model generates a residual correction that estimates the counterfactual forecast, yielding a pseudo-label field that guides a lightweight model update. Experiments show that RDTU consistently produces unlearned models that most closely match exact retraining.

---


### 107. [DIVINE: Simple Cross-Market Stock Pretraining via Diverse Indicator Reconstruction](https://arxiv.org/abs/2610.02866)

**<font color=#1a73e8>作者：</font>** Kuan-Yu Chen, Shu-Cheng Zheng, Yu-Chen Den 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial time-series pretraining typically learns from masked observations, contrastive relations, or future outcomes---yet existing objectives struggle to simultaneously avoid future-supervision uncertainty and maintain return-prediction alignment. We propose DIVINE (DIVerse INdicator rEconstruction), a simple cross-market pretraining framework that reconstructs technical indicators from raw OHLCV history. Computed from observed price-volume history, technical indicators provide consistently defined supervision across markets while summarizing diverse market dynamics with established relevance to return prediction. Pretrained jointly on six-equity market datasets, DIVINE reconstructs 77 targets derived from 16 standard indicators and transfers only the learned encoder to downstream stock ranking. Across all six markets, DIVINE achieves the strongest average portfolio performance with a lightweight 0.05M-parameter encoder, outperforming pretraining baselines and matching or exceeding substantially larger financial foundation models, while remaining robust and data-efficient. Systematic analyses show that indicator diversity and market diversity provide complementary gains in transfer. Together, these results suggest that supervision design and cross-market diversity---rather than model scale---are the key drivers of strong, transferable financial representations.

---


### 108. [TACD: Distilling Efficient Text-to-Motion Models via Terminal Amplification Control](https://arxiv.org/abs/2610.02867)

**<font color=#1a73e8>作者：</font>** Wei-Jin Huang, Yuan-Ming Li, Kun-Yu Lin 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent text-to-motion models have improved motion quality and instruction following, yet many-step denoising and large model components make deployment slow and memory-intensive. We present Terminal-Amplification-Controlled Distillation (TACD), an on-policy approach for training efficient motion generators from text prompts and pretrained teachers, without real-motion training data. Building on segmented on-policy flow distillation, we supervise clean-motion predictions along student-generated trajectories. We identify a failure mode in which velocity matching on a fixed supervision grid repeatedly overweights errors near the denoising endpoint, degrading few-step generation. TACD ties the latest teacher query to the student's step size, bounding the effective loss weights in clean-motion space without changing inference. Experiments on HumanML3D and KIT-ML demonstrate improved few-step generation, including a 58% reduction in eight-step HY-Motion student FID relative to distillation without this bound. For diffusion teachers, the endpoint-matching form of TACD yields four-step students with lower FID and matched or improved text-motion retrieval relative to their 50-step teachers on HumanML3D. On HY-Motion and Kimodo, eight-step students with compact components achieve 7.7-11.9x end-to-end speedups and reduce peak GPU memory by 3.8-6.7x relative to their teachers. Project page: this https URL

---


### 109. [Distributionally Robust Survival Models under Subpopulation Shift and Outlier Contamination](https://arxiv.org/abs/2610.02868)

**<font color=#1a73e8>作者：</font>** Seonghwi Kim, Sung Ho Jo, Minwoo Chae  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning robust survival models under distribution shift is an important but challenging problem in many applications. In heterogeneous populations, a model that performs well on average may still perform poorly on certain subpopulations, and this issue becomes even more severe when the training data are contaminated by outliers. In this paper, we propose a novel distributionally robust framework for survival analysis that jointly addresses latent subpopulation shift and outlier contamination. The proposed method combines an outer minimization that selects a refined nominal distribution by reducing the influence of contaminated samples and an inner maximization that focuses on the most challenging subpopulation. This formulation directly accommodates non-decomposable survival losses while preserving interactions across samples, including the risk-set structure of the Cox negative partial log-likelihood. We develop an alternating gradient-based algorithm with outer updates derived from the KKT conditions of the inner maximization. Experiments on simulated data and two survival benchmarks demonstrate that the proposed method remains robust when subpopulation shift and outlier contamination occur simultaneously. It stabilizes training in contaminated settings and substantially improves worst-group performance across both linear and nonlinear survival models, while maintaining competitive and sometimes superior overall performance.

---


### 110. [AgentTrap: Stateful Feedback Deception against Autonomous Penetration Testing Agents](https://arxiv.org/abs/2610.02869)

**<font color=#1a73e8>作者：</font>** Yuelin Wang, Jiongchi Yu, Yanbang Sun  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous penetration testing agents conduct multi-step attacks by continuously adapting their plans and actions to target responses. As a common defense, honeypots can be deployed to divert these agents from real assets by presenting decoy services, while also supporting attack tracing and active counterattacks. However, conventional honeypots rely primarily on static artifacts and predefined responses, leaving them unable to adapt to the evolving attack strategies of autonomous penetration testing agents. To this end, we present AgentTrap, the first closed-loop honeypot tailored for autonomous penetration testing agents. AgentTrap uses sentinel endpoints to avoid benign interference, stateful deception grounded in the protected application, and behavior-guided escalation to sustain engagement and collect agent-side behavioral evidence with controlled disclosures.
We evaluate AgentTrap against eight autonomous penetration-testing agents in a deployed web application containing a real application endpoint and a separate honeypot endpoint configured under three defense strategies. Compared with no defense, AgentTrap reduces the aggregate real-target attack success rate from 95.8% to 79.2% and successfully elicits attacker API keys in 18.8% of the runs, outperforming static deception and fixed escalation. Furthermore, trace analysis shows that resistance to such counterattacks depends jointly on model-level recognition of deceptive requests and architecture-level isolation of sensitive resources.

---


### 111. [Peer Effects in Signed Networks: Separating Influence Through Positive and Negative Ties](https://arxiv.org/abs/2610.02872)

**<font color=#1a73e8>作者：</font>** Xiaojing Du, Jiuyong Li, Lin Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluating network interventions requires understanding how treatment affects people through their social relationships. Counting treated neighbors without distinguishing supportive and antagonistic ties can conceal opposing influences. We define effects through positive and negative ties, their interaction, and a sign-composition effect of reallocating treatment between the two types at a fixed total, and give their identification formulas. Under sign-blind assignment, we show how ignoring signs mixes the effects of the two tie types. We propose SiDE (Signed-exposure Doubly robust Estimator), which combines sign-specific outcome models with exposure probabilities induced by individual treatment assignment. We establish double robustness of its score and assess approximate intervals that account for overlapping neighborhoods. Semi-synthetic experiments on six real signed networks demonstrate accurate effect estimation and examine the limits of interval coverage. An exploratory reanalysis of published school-experiment data yields a positive estimate of the peer effect through spend-time ties on wristband wearing, but the intervals for all four effects include zero after adjustment for multiple comparisons. This framework can inform network intervention design by showing when influences through the two tie types reinforce or offset one another.

---


### 112. [When Can We Trust the Matching Principle? Robust Deployment Geometry Under Finite-Sample and Model Uncertainty](https://arxiv.org/abs/2610.02894)

**<font color=#1a73e8>作者：</font>** Vishal Rajput  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Match only geometry you can identify; otherwise spread the penalty. We quantify that decision by the trust ratio tau = epsilon / gamma (estimation uncertainty over spectral separation). Under the linear-quadratic Matching response, oracle-relative drift between estimated and oracle projector matching scales as tau^2 for probes in the chosen top-r deployment subspace -- O(tau^2) in the Davis-Kahan separation region tau < 1/2, with practical usefulness depending on constants. Confidence-Calibrated Matching (CCM) turns tau into a policy -- directional when tau is small, progressively isotropic when not -- with thresholds from calibration, not from the theorem (match sits in the separation region; soft is mostly heuristic). Experiments show both regimes, including UCI HAR embeddings where always-match is worse than abstain on every cell.

---


### 113. [ViTok: Improving Dense Semantics in AM-RADIO-Style Multi-Teacher Distillation with PHI-S and Masked Image Modelling](https://arxiv.org/abs/2610.02903)

**<font color=#1a73e8>作者：</font>** Hailun Xu, Kanchan Sarkar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study how to consolidate the current VITOK progress into a single multi-teacher distillation recipe that jointly preserves global recognition and dense semantics. Our starting point is an AM-RADIO-style student distilled from SigLIP2 and DINOv3-L, where SigLIP2 supplies strong global semantics and DINOv3-L supplies stronger dense features. The central empirical issue is that the same recipe does not optimize all objectives equally well: changes that improve ImageNet-1K kNN accuracy can still degrade ADE20K segmentation. We summarize a progression of modifications that make this trade-off more explicit and more manageable: split adaptor heads for CLS and patch tokens, asymmetric cosine/MSE losses, initialization from a DINOv3-L checkpoint, teacher reweighting, masked image modeling (MIM), and PHI-S feature balancing. The resulting model reaches 83.2 patch kNN and 85.2 CLS kNN, slightly surpassing the DINOv3-L teacher on ImageNet-1K kNN classification, while PHI-S restores ADE20K performance from 46.5/58.1 to 48.5/61.0 mIoU/mAcc, matching the teacher on this dense benchmark. We also summarize negative results: scaling distillation from ImageNet-1K to ImageNet22K does not consistently help, and naively adding extra teachers such as SAM3 or HOG features introduces interference. Rather than claiming a final recipe, this paper distills the current project state into a compact empirical story and a concrete set of lessons for future iterations.

---


### 114. [Tangent Schrödinger Bridge Matching: Learning Stochastic Transport with Mechanistic Sensitivities](https://arxiv.org/abs/2610.02906)

**<font color=#1a73e8>作者：</font>** Jowaria Khan, Elizabeth Bondi-Kelly  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting how stochastic systems respond to changes in viscosity, reaction rates, or external forces requires costly simulations, motivating reusable learned models. Yet matching observed outcome distributions does not ensure accurate intervention responses. We introduce Tangent Schrödinger Bridge Matching (Tangent-SBM), which learns stochastic transports from endpoint observations and mechanistic sensitivities. It propagates parameter derivatives alongside trajectories and supervises them against supplied targets. For average-response targets, single-rollout squared error also penalizes response variability; our objective uses two independent rollouts to match the mean without this additional penalty. We establish conditions under which sensitivity accuracy bounds finite-change prediction error and decision regret. Across Gaussian, stochastic double-well, PDEBench reaction--diffusion, and stochastic Navier--Stokes systems, Tangent-SBM improves sensitivity and finite-change prediction over matched conditional-bridge baselines while maintaining comparable endpoint and distributional accuracy. Controls examine target correctness, response objectives, and simulator-budget allocation. To test decision usefulness, we evaluate calibrated viscosity selection in Navier--Stokes: Tangent-SBM reduces tracking error relative to taking no action on every evaluated task.

---


### 115. [Do ResNets Route? Sparse Interaction Experts in Residual Networks](https://arxiv.org/abs/2610.02907)

**<font color=#1a73e8>作者：</font>** Liang Yan, Siying Chen, Kaijie Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Residual networks execute every block for every input, yet their functional contributions need not be input independent. We formulate a trained ResNet as a set function over binary residual-branch masks and apply Möbius inversion to decompose its output exactly into individual residual corrections and higher-order interactions. For smooth residual stacks, we show that each fixed $k$-way interaction scales as $\mathcal{O}(\lambda^k)$ under residual scaling. Exhaustive analysis of ImageNet-pretrained ResNet-18 and ResNet-34 reveals that interaction mass peaks at orders five and ten, respectively, rather than at low orders. Reducing the residual scale shifts both spectra toward lower orders, but also changes model predictions. The interaction coefficients are concentrated in magnitude but not hard sparse, and prediction-preserving sparsity weakens with depth. Crucially, the dominant interactions vary across inputs and predicted classes around a shared global core, while their overall complexity changes little with sample difficulty. These results show that dense ResNets implement an implicit form of soft routing: every block is executed, but different inputs rely on different residual interaction experts. Routing can therefore emerge at the level of functional contribution without an explicit router or sparse execution.

---


### 116. [Kinematics-Induced Multimodal 3D Human Pose Estimation with Subject-Level Privacy](https://arxiv.org/abs/2610.02943)

**<font color=#1a73e8>作者：</font>** Kaushik Bhargav Sivangi, Fani Deligianni  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal 3D Human Pose Estimation (3D HPE) combines complementary information from RGB, LiDAR, and mmWave radar, but models trained on correlated observations from the same individuals, raise privacy risks overlooked by record level analysis. We present a unified framework for multimodal 3D HPE that couples kinematics-induced sensor fusion with subject level privacy auditing and private training. First, our multimodal model aligns modality specific joint representation, injects skeletal structure and adaptively aggregates complementary sensor evidence for accurate pose prediction. Second, we formulate a black-box subject membership inference attack for 3D HPE, complemented by an empirical pointwise maximal leakage analysis, which characterizes how individual attack score outcomes change inference about the membership outcome. Third, we instantiate user-level differential privacy via Action Temporal Stratification, a population weighted within-subject sampling strategy that enforces action and temporal coverage. We evaluate our framework on the MM-Fi dataset across three diverse experimental protocols. Source-code will be released upon acceptance.

---


### 117. [When Predicting Nothing Beats SAM 3: Revisiting Evaluation in Video Object Segmentation](https://arxiv.org/abs/2610.02946)

**<font color=#1a73e8>作者：</font>** Jihwan Hong, Woohyeon Park, Jaeik Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Object Segmentation (VOS) in complex and long videos is increasingly important for real-world applications, where target objects often appear only intermittently within long temporal horizons. However, existing benchmarks largely focus on temporally salient objects that remain visible for most of the video. To address this gap, we introduce FaVOS (A Benchmark for Video Object Segmentation with Fractional Temporal Visibility), a benchmark designed to evaluate VOS methods under low temporal visibility. We show that, in this regime, the standard J&F metric can collapse VOS evaluation into absence classification, because empty predictions receive high rewards on target-absent frames. Consequently, even a trivial empty-mask predictor can outperform strong models such as SAM 3, revealing a fundamental mismatch between current metrics and practical VOS performance. To mitigate this issue, we propose Volumetric J&F, which evaluates mask sequences as spatio-temporal volumes and reduces the dominance of target-absence rewards while preserving sensitivity to segmentation quality and temporal structure. Project page: this https URL.

---


### 118. [Hyperparameter selection for equation learning with biologically-informed neural networks](https://arxiv.org/abs/2610.02954)

**<font color=#1a73e8>作者：</font>** William Lavery, Jodie A. Cochrane, John T. Nardini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Biologically-informed neural networks (BINNs) have emerged as a flexible subclass of physics-informed neural networks (PINNs) for learning terms in partial differential equations from data. BINNs are particularly suited for biological systems, where the governing equations are highly nonlinear and only partially known a priori, and where data observations are often sparse, noisy, and incomplete. However, applying BINNs effectively in practice depends critically on hyperparameter selection, which remains a central challenge in equation-learning frameworks. Hyperparameters are often chosen heuristically and only cursorily documented, which limits the reproducibility of results and the transferability of methods. We present a diagnostic workflow for hyperparameter selection that can be used when the ground-truth equations are not known. The workflow is guided by three main questions: (1) Are the benefits of greater network capacity worth the cost? (2) Do more training epochs keep reducing the validation loss? (3) Do the learned terms stop changing as network capacity and training increase? We apply our workflow to synthetic systems of varying complexity with known ground truth, spanning diffusion and growth right-hand side terms and data ranging from 1D+t to 2D+t. We demonstrate that the validation loss generally follows the true error in the learned terms and distil practical rules of thumb for selecting hyperparameters in the BINN architecture. By providing a structured workflow, practical guidelines, and suggested starting values for hyperparameter selection, this work lowers the barrier to BINN-based equation learning.

---


### 119. [Understanding Trajectory Heterogeneity in Federated World Model Learning](https://arxiv.org/abs/2610.02957)

**<font color=#1a73e8>作者：</font>** Yipan Wei, Zhaokun Yan, Ziming Hong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models learn state evolution from trajectories, making access to temporal context a central training requirement. Federated learning can use distributed records, while ownership boundaries within a trajectory restrict the examples each client can construct. Our study benchmarks this cross-time setting through hourly action-conditioned clinical prediction on eight MIMIC-IV disease cohorts, comprising 40.87 million transition memberships. We specify severity-based client ownership, patient-separated construction, local history and future-window rules, and paired rollout evaluation from one to 32 hours. A matrix of ten federated algorithms covers 32 disease--partition configurations under five rounds of ten-percent participation. Three findings emerge from existing results and training logs. First, client ownership and participation jointly restrict long-window coverage: only 7.55\%--21.36\% of pooled-available 32-step windows have a locally complete anchor visited during training, averaged across diseases. Second, finer severity partitions accompany higher FedAvg error in 15 of 16 paired comparisons, while algorithm gains are small and horizon-dependent: FedProx reduces mean error by 0.56\%, with no consistent improvement at 32 steps. Third, algorithm labels conceal distinct update behavior, including inactive extrapolation and orders-of-magnitude differences in update scale. Cached-update performance also varies strongly across trajectory partitions under the same benchmark protocol. These results establish temporal access, participation coverage, optimization behavior, and horizon-resolved prediction as complementary dimensions for evaluating federated clinical world models.

---


### 120. [Dirac-Interconnected Neural Elements: Discovering Modularity in Physical Systems Without Reduction](https://arxiv.org/abs/2610.02960)

**<font color=#1a73e8>作者：</font>** Reiho Li, Razmik Arman Khosrovian, Takaharu Yaguchi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning has shown remarkable success in the data-driven modeling of dynamical systems. Much of its success is attributed not to the flexibility of neural networks but to inductive biases based on physical prior knowledge, such as energy conservation and symplecticity. However, existing methods do not fully exploit the fact that real-world physical systems are interconnections of components. Some methods require the interconnection to be known a priori, while others assume the system to be reducible to an ordinary differential equation (ODE) and learn only the reduced ODE, discarding the algebraic constraints imposed by the interconnection. Here, we propose Dirac-interconnected neural elements (DINEs), a neural network model that represents a physical system as a differential-algebraic equation (DAE), whose algebraic constraints are given by a Dirac structure in kernel representation. With DINEs, we simultaneously identify from data the interconnection among the components as a Dirac structure and learn the characteristics of the components as neural networks. This allows us to keep the learned subsystems in unreduced form and isolate or compose them to make a new system without retraining. Moreover, DINEs can handle partially observable systems. Experimental results demonstrate these capabilities on physical systems beyond the reach of existing methods.

---


### 121. [Post-Training Frontier Text-to-Image Models by Composing Preference and Rubric Rewards](https://arxiv.org/abs/2610.02967)

**<font color=#1a73e8>作者：</font>** Yuanhao Ban, I-Hung Hsu, Anastasios Angelopoulos 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent text-to-image generation models have achieved remarkable visual quality, but improving them through post-training remains challenging because no single reward signal captures the full range of human preference. In this work, we develop a simple and effective post-training recipe for open-domain text-to-image generation based on the composition of complementary reward signals. Our reward system consists of two main components: a preference reward, trained on large-scale human preference data using a Bradley-Terry objective to capture overall human aesthetic and perceptual preferences, and rubric-based rewards, which explicitly evaluate prompt faithfulness and other desirable properties while providing safeguards against reward hacking. A key challenge is how to combine these heterogeneous reward signals. We show that a naive weighted average leads to suboptimal optimization behavior, and propose a simple reward composition strategy that more effectively balances preference optimization with rubric satisfaction. In the Arena text-to-image leaderboard (this https URL), our RL-trained Flux2dev achieves an Elo rating 69 points above the base model, and our post-trained Ideogram-4 surpasses every open-source model on the leaderboard, reaching an Elo of 1223.5. (Claims of state-of-the-art performance are based on the Arena leaderboard snapshot as of September 4, 2026.) Our results suggest that effective rewards for frontier generative-model training require broad coverage of user intent and robustness to exploitation under optimization. To support reproducible research, we release Arena-T2I-Training, a 1K subset of training data that recovers some gains of full-scale training, providing a resource that we hope will facilitate future work on post-training for text-to-image models.

---


### 122. [Tracking Human Daily Cognitive Activity from EEG and Biometric Data](https://arxiv.org/abs/2610.02971)

**<font color=#1a73e8>作者：</font>** Alina Gutoreva, Zhaniya Omar  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Understanding human cognitive activity in everyday life remains challenging due to the dynamic, context-dependent, and multimodal nature of cognition. Laboratory-based studies often fail to capture real-world cognitive processes, while single-modality approaches provide only partial insight into cognitive states. Advances in wearable sensing now enable the collection of heterogeneous data streams for a more comprehensive view of daily cognition. This paper presents a multimodal framework for tracking human cognitive activity using electroencephalography (EEG), wearable physiological signals, behavioral context, and self-reported measures. A preliminary pilot study was conducted with observational data from three participants (N = 3) over 280 annotated 10-minute intervals spanning nine activity domains across two weeks.
Results reveal consistent temporal patterns, including a discernible mid-day decrease in motivation and energy at 13:00, followed by afternoon recovery. Work and IADLs yielded the highest flow state rates (51% and 50%), while ADLs produced the lowest (15%). Motivation correlated strongly with arousal (r = 0.78) and attention (r = 0.74), whereas perceived stress showed a weaker negative relationship (r = -0.33). A linear regression model predicting motivation from arousal, attention, energy, and stress achieved R2 = 0.76 (MAE = 9.84, RMSE = 12.85). Lag-based analysis indicates that prior energy levels positively predict subsequent motivation, confirming temporal dependencies in cognitive dynamics.
These findings demonstrate the feasibility of multimodal cognitive activity analysis in real-world environments and highlight the importance of integrating physiological and behavioral indicators. The proposed framework provides a foundation for future large-scale multimodal systems and applied intelligent solutions.

---


### 123. [Safeguarding Mutual Correction in Source-Free Domain Adaptation via Cut Statistics](https://arxiv.org/abs/2610.02981)

**<font color=#1a73e8>作者：</font>** Seongjun Lee, Changhee Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Source-Free Domain Adaptation (SFDA) aims to adapt a source-pretrained model to an unlabeled target domain without access to the original source domain. While early single-model approaches rely on self-refinement, they are inherently susceptible to confirmation bias and struggle to correct their own systematic errors. To overcome this limitation, recent methods introduce Vision-Language (ViL) models as external knowledge sources. However, these approaches operate in a largely unidirectional paradigm, using the ViL model primarily to supervise the source-pretrained model. This overlooks a key structural property: the two models exhibit distinct failure modes -- where one produces an incorrect prediction, the other may produce a correct one, creating a natural opportunity for mutual correction within the target domain. Yet, without ground-truth labels, identifying which model is correct on any given sample is non-trivial, and naively exchanging predictions risks propagating errors across models. To address this challenge, we propose SafeCut, a novel approach that leverages the cut statistic as a label-free measure of prediction reliability to gate cross-model supervision. Our approach dynamically controls both the direction and strength of supervision based on relative reliability, selectively amplifying true corrections while suppressing miscorrections on a per-sample basis. We further provide theoretical justification showing that this reliability-gated mechanism guarantees a net-positive correction signal. Extensive experiments across diverse SFDA benchmarks demonstrate that SafeCut achieves state-of-the-art performance, highlighting the effectiveness of safeguarding mutual correction in SFDA via cut statistics.

---


### 124. [Differentiable Koopman Operator for Contrastive Learning on Dynamic Graphs](https://arxiv.org/abs/2610.02990)

**<font color=#1a73e8>作者：</font>** Md Abrar Jahin, Taufikur Rahman Fuad, Md Rizwan Parvez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world interaction networks are inherently dynamic: edges form and dissolve as node behavior shifts over time. Most snapshot-based contrastive methods encode temporal dependencies implicitly in encoder weights, without an explicit model of how node representations evolve, making them brittle under distribution shifts. We propose KAIROS (Koopman-Aligned Invariant Representations for Open Dynamic Systems), a self-supervised framework that embeds a differentiable Koopman operator within a dynamic graph contrastive learning loop to linearize temporal evolution in the learned embedding space. A dual-view encoder pairs raw node features with a graph-diffused structural view and is optimized with multi-granularity contrastive objectives across temporal windows. For anomaly detection, KAIROS uses the Koopman prediction residual together with temporal inconsistency and local neighborhood deviation to separate irregular behavior from predictable graph evolution. Evaluated on nine dynamic graph benchmarks, KAIROS achieves state-of-the-art anomaly detection results on all nine datasets, with gains of up to 23.15 ROC-AUC points over prior work, while remaining competitive for unsupervised node classification. These results show that explicit dynamics modeling provides a scalable and effective inductive bias for temporal graph representation learning.

---


### 125. [Temporal Geometry of Deep Networks: Hyperbolic Representations of Training Dynamics for Intrinsic Explainability](https://arxiv.org/abs/2610.03000)

**<font color=#1a73e8>作者：</font>** Ambarish Moharil  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Intrinsic explainability remains a challenging problem, particularly in contexts where multilayer perceptrons (MLPs) require dynamic re-training within an optimization environment. This paper investigates how MLPs and their training dynamics can be represented and studied in non-Euclidean spaces; our representation features the Poincaré model of hyperbolic geometry. We aim to capture the geometric evolution of their weighted topology and self-organization over time. Instead of restricting the analysis to single checkpoints---as per established measure-based explainability methods---we construct temporal \textit{parameter graphs}, i.e., snapshots over time $T$ steps of the optimization/training process for MLPs. This reflects the view that neural networks encode information not only in their weights but also in the trajectory traced during training. Drawing on the idea that many complex networks admit embeddings in hidden metric spaces where distances correspond to connection likelihood, we present a geometric and temporal graph-based metalearning framework for obtaining dynamic hyperbolic representations of the underlying neural parameter graphs. Our model embeds temporal parameter graphs in the Poincaré model ball, and learns from them while maintaining equivariance to within-snapshot neuron permutations and invariance to permutations of past snapshots. In doing so, the approach preserves functional equivalence over time and recovers the latent evolving geometry of the network. Experiments on regression and classification tasks with trained MLPs show strong meta-network performance, accompanied by hyperbolic temporal representations. This reveals how the network structure emerges over time under specific training environments, thus providing insights into the network's self-organization.

---


### 126. [Neural Data Needs Semantic Tokenization: Behavioral Events as Boundaries of Session-Transferable Tokens](https://arxiv.org/abs/2610.03001)

**<font color=#1a73e8>作者：</font>** Sangyoon Bae, Jiook Cha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Extracellular electrophysiology records a different set of neurons in every session. Neural foundation models embed each neuron and each session into their tokens, so every new session is an input they have never seen, and they fail to generalize to it. A tokenizer for new sessions needs a unit that every session shares and that carries behavior. Population activity offers such a unit. It evolves on a low-dimensional manifold that persists across neuronal turnover and across animals once sessions are aligned. This manifold changes regime at task events such as stimulus onset and movement onset. Within each regime the population occupies a state, the part of the manifold it spans between two events, and each state carries its own behavioral meaning. We propose Tokenization with States (TWS), which segments each trial, one repetition of the task, at these events and converts every state into tokens of population geometry, with no neuron or session embedding. On held-out International Brain Laboratory (IBL) sessions, TWS decodes movement even from regime boundaries that carry no information about the target, while a per-neuron foundation model pretrained on those sessions decodes at chance. Frozen after training on mice alone, TWS transfers to macaques and Utah arrays with only a linear probe. On reach direction, a target that its boundaries do not define, it achieves a Matthews correlation of 0.23, where the event time alone achieves $0.01$. For cross-session generalization, the token matters more than the model on top.

---


### 127. [Recursive Self-Improvement in Unified Multimodal Models](https://arxiv.org/abs/2610.03002)

**<font color=#1a73e8>作者：</font>** Huijuan Wang, Chufan Shi, Cheng Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models (UMMs) understand and generate both text and images, which lets a model produce its own training data. Existing self-improvement in UMMs keeps supervision on the visual side, where image understanding judges image generation. We propose recursive cross-capability self-improvement (RSI), a training loop in which the text and visual abilities of a UMM supply training data for one another. In each round, the model generates images and reads them to find where it falls short. It then writes programs aimed at these shortcomings, and execution verifies every result against its specification. Verified renders train image generation, while labeled renders and the model's own correct programs train visual understanding and program writing. Program execution thus acts as a source of truth outside the model, so errors do not accumulate across rounds. We study RSI on charts and build BasicChartBench to evaluate open models early in training. On requests worded differently from training, four rounds of RSI raise the score from 45.7% to 60.2%, while continued training stays at 46.3%. Verified construction carries most of the gain, and targeting the model's failures adds 3.5%. Along the way, the share of verified programs rises from 48.9% to 95.2%, and the reader's accuracy on edited renders rises from 55.6% to 87.4%.

---


### 128. [Rethinking Fixed Temporal Grids: Frequency-Disentangled Motion Generation](https://arxiv.org/abs/2610.03012)

**<font color=#1a73e8>作者：</font>** Yunjiao Zhou, Junlang Qian, Gen Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most human motion generation methods encode motion as tokens on a uniform temporal grid, where every token spans the same fixed time window. Human motion, however, is temporally heterogeneous: slowly evolving global trajectories coexist with rapid transient events such as foot contacts and joint impulses. Forcing such multi-scale dynamics onto tokens of identical temporal resolution entangles motion frequencies, leaving slow regions redundant while smoothing out the rapid details that distinguish realistic motion. We propose \textbf{FreqMo}, a scale-adaptive motion representation that decomposes motion into wavelet frequency bands, separating dynamics across temporal scales while preserving temporal localization and exact reconstruction. Unified Frequency Residual Quantization (UFRQ) then encodes all bands within a single shared codebook, compressing the token sequence threefold and enabling stable single-stage generation. Experiments show FreqMo attains SOTA fidelity with substantially improved high-frequency preservation, and the same decomposition transfers to continuous diffusion backbones.

---


### 129. [RYOPO: Bringing End-to-End Category-Level Object Pose Estimation into Real Time](https://arxiv.org/abs/2610.03013)

**<font color=#1a73e8>作者：</font>** Hakjin Lee, Junghoon Seo, Jaehoon Sim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Category-level object pose estimation predicts the rotation, translation, and metric size of unseen instances within known categories. Many accurate RGB-D methods rely on external instance segmentation and crop-based pose estimation, introducing separate stages and object-dependent processing costs that hinder real-time inference. To bring accurate pose estimation into real time, we present \ours{}, an end-to-end trainable query-based RGB-D set predictor. It jointly detects and segments objects and estimates their \mbox{9-DoF} poses without explicit CAD-derived shape priors or a separately trained instance segmentor. Shared image and scene encoding avoids repeated per-object crop encoding. A query-conditioned geometry pathway associates observed 3D points and RGB features with object queries and incorporates shared scene context. Object-centric refinement uses the resulting point descriptors to update an explicit pose state through pose-conditioned cross-attention and recurrent residual corrections. On NOCS, \ours{} substantially improves on published RGB-D joint detection and pose estimation results. It achieves competitive performance compared with two-stage methods under all-object evaluation on REAL275 and HouseCat6D, while enabling real-time full-frame pose estimation at $31.8$ FPS on an RTX~A6000. Project page: this https URL.

---


### 130. [OmniAct3D: Leveraging Foundation Geometry and Evidence-Grounded Reasoning for Panoramic 3D Detection](https://arxiv.org/abs/2610.03015)

**<font color=#1a73e8>作者：</font>** Runtong Wu, Fei Teng, Di Wen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate 3D detection is essential for mobile embodied agents, while Vision Foundation Models (VFMs) offer transferable visual and geometric priors. Yet existing VFM-based 3D detectors rely on narrow-view monocular images or discrete perspective views, limiting coherent surround perception; equirectangular projection (ERP) instead encodes a continuous 360 scene in a single image. Direct transfer remains difficult because ERP organizes geometry and visual information differently, making object-relevant cues hard to model, localize, and preserve. We propose OmniAct3D, a framework that adapts perspective-trained VFM detectors to ERP while preserving transferable VFM priors. To resolve geometric mismatch, the ERP-Ray Geometry Adapter (ERGA-Ray) models spherical viewing rays and periodic spatial structure. To localize evidence in scene-wide context, the Visual-Action Reasoning Chain (VARC) grounds each hypothesis in relevant panoramic evidence and converts it into a structured geometric action. To recover local cues lost under fixed token budgets, the Appearance-Guided Heading Expert (AGHE) re-encodes object regions at higher resolution for heading estimation. Experiments show that OmniAct3D improves over the previous best 3D detector by 2.96 NDS points on Spheriverse and over the unadapted VFM baseline by 24.87 mAP points on PanoMMOcc. With target-specific geometry adaptation, VARC retains 95--98% of the same-configuration mAP, indicating reusable object-level 3D reasoning across sensing configurations. The source code will be made publicly available at this https URL.

---


### 131. [Personalized Automatic Speech Recognition for a Dysarthric and Tracheostomic Speaker using Artificial Conversations](https://arxiv.org/abs/2610.03017)

**<font color=#1a73e8>作者：</font>** David Nadrchal, Monorama Swain, Florian Schmid 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This work presents an automatic speech recognition (ASR) system personalized for a Czech speaker with a permanent tracheal stoma and severe dysarthria rendering their speech unintelligible to untrained listeners. We release a public dataset containing 33 annotated hours of the speaker's speech, collected using a novel "artificial conversation" protocol designed for high engagement and dialogue realism. We propose a multi-stage training pipeline based on Whisper Base: fine-tuning on standard Czech speech, acoustically simulated tracheostomic speech, and the speaker's data. We evaluate the system across three near real-time scenarios: scripted conversations, question answering, and spontaneous dialogue, achieving a 50\% relative reduction in Character Error Rate compared to Whisper Base baseline and surpassing the average recognition accuracy of their assistants in acoustic recognition of isolated utterances. We demonstrate that even for severely impeded speech, a helpful ASR is achievable, as evidenced by the quantitative results and the feedback from the speaker.

---


### 132. [Signal Simplification Is Not Predictive Simplification: Diagnosing Residual Neural Forecasting in Short-Horizon Volatility](https://arxiv.org/abs/2610.03019)

**<font color=#1a73e8>作者：</font>** Bingqi Lian, Linfeng Cheng, Mei Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid statistical-neural pipelines often assume that a successful statistical first stage leaves a cleaner and more learnable residual target. We examine that assumption in short-horizon volatility forecasting through a signal-forecast-system diagnostic framework. Across five liquid U.S. assets, a volatility-aligned HAR-style model outperforms AR, MA, and ARIMA. Within expanding training windows, the pre-standardization fitted residual process used to construct residual-LSTM sequences has about 82% lower variance than the corresponding target and near-zero lag-1 autocorrelation; independently, rolling pseudo-out-of-sample HAR errors show about 74% variance reduction and similarly weak lag-1 dependence. Residual-only LSTM augmentation nevertheless raises mean squared error from 0.3049 to 0.3594 on average, with deterioration on every asset. Pure LSTM records the lowest selected pseudo-out-of-sample MSE, 0.2649, while the residual hybrid requires substantially more end-to-end runtime without improving accuracy. We describe this pattern as forecaster-preconditioner asymmetry: first-stage forecasting success and statistical residual simplification need not translate into useful downstream neural preconditioning.

---


### 133. [ReSCUE: Re-translation with Sentence Commitment for Unsegmented Long-Form Simultaneous Sign Language Translation](https://arxiv.org/abs/2610.03022)

**<font color=#1a73e8>作者：</font>** Sihan Ren, Gaozheng Li, Yuanshang Quan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Simultaneous Sign Language Translation (SLT) is critical for real-time communication, yet existing methods remain largely confined to sentence-level, offline settings that assume pre-segmented inputs. These assumptions hinder deployment in realistic scenarios involving continuous, unsegmented video streams. We present ReSCUE, a unified framework for simultaneous SLT on unsegmented long-form sign language videos that aligns training and inference with realistic streaming conditions. ReSCUE combines inference-aware training to handle partial inputs, non-signing pauses, and multi-sentence contexts, stabilized re-translation to enable low-latency yet revisable predictions with reduced output flicker, and a sentence commitment mechanism for online segmentation and memory management. Experiments on standard sentence-level benchmarks show that ReSCUE achieves lower latency and the best translation quality under low-latency settings. On long-form unsegmented datasets, ReSCUE approaches the translation quality of oracle offline systems that use ground-truth sentence boundaries, while operating at substantially lower latency, demonstrating its practicality for real-world streaming scenarios.

---


### 134. [Verifiable, Articulable, and Tacit Components of Preference](https://arxiv.org/abs/2610.03025)

**<font color=#1a73e8>作者：</font>** Alexander Spangher, Sheldon Huang, Andreas Haupt 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> What makes a short story gripping; a news article newsworthy; or a math proof elegant? These constructs resist articulation or verification; their meaning is at least partially tacit. However, modern AI models are improved primarily via articulated constitutions, rubrics and verifiers (i.e. in RLAIF and RLVR); tacit components of preferences are typically understudied. We introduce a large, labeled preference dataset CreativePreferences, containing 2.8M texts labeled by 317M human preference judgments across 7 creative domains, with 42 benchmark tasks. We model these labels with executable programs, rubric banks and densely trained models (V, A and VAT, respectively). We observe robust articulability gaps, VAT-VA; and verifiability gaps, VAT-V; we estimate upper and lower bounds for each gap with a novel measurement approach that discovers articulable and verifiable metrics, identifies spurious variables and estimates the value of undiscovered metrics using capture-recapture. These gaps occur across all domains, even in domains traditionally treated as fully verifiable: correctness-centered domains (i.e. mathematics and software engineering) and claim- and novelty-centric domains (i.e. news, patents, peer review). The size of the gap varies based on domain (e.g. peer review and creative writing have the largest articulability gaps) and widens as more people take part in the judgment, consistent with Collins' collective tacit knowledge. We show two consequences: (1) on human generations, the full model more closely matches human preferences, often in disagreement with articulated criteria, and (2) in an analogy to Goodhart's law, articulating preference shifts it away from the tacit dimension. Articulability and verifiability gaps are consequential; we give recommendations on when tasks can be prompted; how learning mechanisms might improve; and when to leave judgments with humans.

---


### 135. [CrowdOcc: Monocular Semantic Scene Completion for Quadruped Robots in Crowded Indoor Environments](https://arxiv.org/abs/2610.03031)

**<font color=#1a73e8>作者：</font>** Feiyang Chen, Jincheng Hu, Yiduo Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular semantic scene completion (SSC) for quadruped robots remains underexplored in real crowded indoor environments, where human-scene occlusion disrupts static geometry and human occupancy predictions are often incomplete or spatially misplaced. We present CrowdOcc, an RGB-D dataset and monocular SSC framework for this setting. CrowdOcc contains 25.1K frames from 11 indoor scenes, with semantic occupancy annotations constructed through static dynamic decoupling. Our framework combines: (i) Normal Guided Scene Geometry Fusion (NGSGF) to complement depth-aware lifting with surface-normal cues for occlusion robust geometry; and (ii) Human-Centric Sparse Interaction (HCSI) to selectively model human-human and local human scene relations in 3D. Our method achieves state-of-the-art SSC performance on CrowdOcc's scene-disjoint test set, reaching 15.80 IoU, 11.40 mIoU, and 46.23 Human IoU, demonstrating generalization to unseen indoor scenes.

---


### 136. [Adaptive Second-Order Solvers for Fast Stochastic Diffusion Sampling](https://arxiv.org/abs/2610.03034)

**<font color=#1a73e8>作者：</font>** Ella Kemperman, Luca Ambrogioni  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models rely on numerical solvers requiring time-discretization, which has a large influence on the tradeoff between sampling cost and quality. However, the computational difficulty of the reverse process varies along the sampling trajectory and across data distributions, making the choice of discretization important. We adapt proportional-integral (PI) step-size control to diffusion, using our diffusion noise-normalised error estimator. Unlike existing adaptive methods in diffusion that respond only to the current error, the PI solver also incorporates the previous error, yielding smoother step adaptation. We further show that these per-sample trajectories exhibit shared structure and can be aggregated into a fixed schedule that retains much of the benefit of adaptive sampling. We evaluate both approaches on natural-image and language datasets, in terms of quality, measured by FID at a matched number of neural network evaluations (NFE), comparing them with widely used stochastic solvers and schedules. For images, our fixed discretization outperforms the commonly used EDM schedule in terms of sample quality when used with the stochastic Heun sampler, and with the EDM-churn sampler at low NFE. Additionally, our PI adaptive solver obtains better FID than most stochastic and adaptive baselines, although it does not beat the EDM-churn sampler at low NFE. Moreover, we find our solver outperforms both the EDM and the entropy schedule on language diffusion at low-to-medium NFE in terms of perplexity, with the drawback of lower token entropy. Lastly, we find that the benefit of per-sample adaptivity is problem-dependent. It is highly beneficial in 1D toy examples, while only marginal for image and language data, where the average schedule sometimes even outperforms the PI-adaptive solver. Code is available at this https URL

---


### 137. [Balancing Multimodal Learning via Functional Progress](https://arxiv.org/abs/2610.03035)

**<font color=#1a73e8>作者：</font>** Zhongjing Gu, Fengqiang Wan, Yiming Cui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal learning often suffers from modality imbalance, where the joint optimization process is dominated by a single modality. Existing methods typically estimate modality imbalance from score disparities derived from prediction uncertainty or optimization statistics. However, due to distinct prediction uncertainty and learning dynamics across modalities, direct comparison of such scores may misinterpret intrinsic modality differences as progress gaps, leading to biased imbalance estimation. In this paper, we propose Function-Space Guided Multimodal Optimization (FGMO), which leverages a function-space progress signal to assess modality-wise optimization progress and coordinate optimization across modalities to alleviate modality imbalance. Specifically, we introduce Functional Progress Estimation (FPE) to measure each modality's update-induced function-space response and calibrate it against a loss-aligned unimodal reference, producing a comparable progress signal. Based on this signal, Functional Response Control (FRC) redistributes modality-level function-space budgets and realizes the target responses through tensor-wise learning-rate adjustment. Theoretical analysis establishes a one-step target-contraction property of FRC under bounded controller-state mismatch, and extensive experiments demonstrate the effectiveness of FGMO across multiple multimodal benchmarks.

---


### 138. [Parasitic Co-Denoising: Unlocking 3D Human Motion Generation in a Frozen Video Diffusion Model](https://arxiv.org/abs/2610.03047)

**<font color=#1a73e8>作者：</font>** Yunjiao Zhou, Junlang Qian, Lihua Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite never being supervised on explicit 3D motion, large-scale text-to-video diffusion models synthesize realistic human motion in their generated videos. We ask whether this implicit knowledge can be turned into explicit 3D motion generation, without training a separate motion model. Probing a frozen Wan2.1 reveals that a recoverable motion signal is present in its intermediate states across the entire denoising schedule, not confined to the clean output. Motivated by this, we introduce parasitic co-denoising, a paradigm in which motion is decoded from the host model along its denoising schedule rather than produced by an independent generator. We instantiate it as the Parasitic Motion Decoder (PMD), an efficient flow-matching decoder that shares the host's noise schedule and reads its intermediate features through a $\sigma$-adaptive multi-layer fusion, leaving the host unmodified. Drawing its coverage from the host rather than from motion data, PMD leads dedicated motion generators on text-motion alignment at a small fraction of their trainable parameters, while producing paired video and motion in a single pass that motion-only baselines cannot match.

---


### 139. [BeeWhere: Segmenting Bumble Bee Colonies to Quantify Behavioral Effects](https://arxiv.org/abs/2610.03051)

**<font color=#1a73e8>作者：</font>** Roberta Hunt, August Easton-Calabria, James Crall  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Social bees are important pollinators that support biodiversity and crop pollination globally and serve as important model systems for collective behavior, but scalable measurement of individual- and colony-level behavior remains difficult in dense, occluded nest environments. Existing monitoring workflows use fiducial tags (e.g., ArUco) to preserve individual identity, yet tag-based tracking can fail when markers are obscured and provide limited information about body extent, spatial context, and untagged individuals. We present BeeWhere, an AI-assisted annotation and analysis workflow that combines ArUco detections with deep-learnt instance segmentations to quantify bumble bee behavior from high-resolution colony images and videos. Using bumble bee (Bombus impatiens) microcolonies as a test case, we annotate 483 frames containing 8,443 bee instances. We additionally annotate pollen balls, nest structures, and chamber boundaries, and train YOLO instance segmentation models for downstream behavioral analysis. Instance segmentations enable quantification of important behavioral metrics based on body contours, including nearest-neighbor distance, proximity to nest structures, spatial occupancy within the nest, and detection counts over time. We apply the BeeWhere models to tag-based tracking in an exploratory validation study assessing the behavioral impacts of neonicotinoid pesticide exposure. BeeWhere increased detection rates compared to tag-based tracking, particularly when bees were partially obscured or under challenging imaging conditions, and also captured treatment-associated changes in bee spatial organization not captured using tag-based tracking alone. These results suggest that instance segmentation can complement fiducial-marker tracking by recovering behaviorally meaningful signals under challenging colony conditions.

---


### 140. [RIPPLE in Still Water: Zero-Shot Clustering in Federated Learning with Wavelet Scattering Transform](https://arxiv.org/abs/2610.03054)

**<font color=#1a73e8>作者：</font>** Alessandro Licciardi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clustered Federated Learning (FL) partitions a client population into groups of similar local distributions and trains one specialized model per cluster, mitigating client drift that degrades single-model methods under non-IID data. Prior methods discover cluster structure inside the training loop through gradient similarity, loss evaluation, or EM-style updates, thus increasing communication overhead, exposing gradients to inversion attacks, and providing no mechanism to assign clients absent from training. We propose RIPPLE, a clustered FL framework in which cluster assignment is computed entirely offline from a spectral characterization of each client's local data: a variance-weighted principal-component prototype embedded via the Wavelet Scattering Transform and decoded by a Gaussian Mixture VAE trained server-side on synthetic client populations before federation begins. Per-round communication cost matches FedAvg exactly, and a client absent from training obtains a personalized model from a single forward pass, without gradient computation, model evaluation, or extra communication round. We prove that the gap between RIPPLE's surrogate clustered objective and the oracle is bounded by a computable quantity decaying with client sample size and independent of federation duration; per-cluster convergence matches the minimax-optimal rate for non-convex smooth objectives. Across five benchmarks spanning controlled and realistic heterogeneity, RIPPLE consistently outperforms all baselines, with margins growing on the most realistic partitions.

---


### 141. [When Does Synthetic Relational Data Teach Models to Use Relations? Tracing Predictive Structure from Pretraining Data to Model Behavior](https://arxiv.org/abs/2610.03057)

**<font color=#1a73e8>作者：</font>** Shivam Dubey, Mohamed Bouadi, Nassim Bouarour 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Relational foundation models are increasingly pretrained on synthetic databases, yet downstream benchmarks reveal little about why one synthetic corpus produces a better model than another. In particular, strong performance may arise from realistic row-level statistics without the model ever learning to use relational structure. We study this as a data-attribution problem: which property of synthetic pretraining data induces relational computation? Using four Relational Transformer checkpoints trained with the same architecture, initialization, objective, and compute budget on corpora produced by four relational data generators, we trace a measurable property of the data to learned computation and downstream behavior. We hypothesize that relational mechanisms emerge when cross-table information is predictively necessary for the masked-cell pretraining objective. RelDiff exhibits by far the largest predictive gain from foreign-key-linked parents, and its corresponding model is uniquely sensitive to foreign-key interventions on unseen databases. This dependence survives a random-initialization control, grows monotonically with the fraction of corrupted links, and localizes to a serial cross-table pathway. Finally, disrupting the same mechanism during downstream inference removes RelDiff's advantage on relational tasks while leaving structure-insensitive models nearly unchanged. These results connect a property of synthetic training data to a learned mechanism and, through intervention, to downstream behavior.

---


### 142. [Learning Transferable Policies from Action-free Time Series Through Dynamical Embeddings](https://arxiv.org/abs/2610.03065)

**<font color=#1a73e8>作者：</font>** Niklas Emonds, Georgia Koppe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning control from action-free recordings is challenging because intervention effects are unobserved and policies may exploit errors in reconstructed dynamics. We present a hierarchical model-based reinforcement learning framework that uses shared structure across related systems to learn system-specific control policies from action-free recordings. A hierarchical dynamical system reconstruction model captures shared dynamics and individual variation through low-dimensional embeddings. These embeddings are then reused to parameterize shared policy and value networks, linking differences in reconstructed dynamics to differences in control. Policies are trained entirely via simulation under an explicit intervention model with additive latent perturbations. Piecewise-linear recurrent neural networks enable mechanistic analyses of the controlled dynamics, while decoder-based constraints make the immediate effects of interventions interpretable in observation space and permit interventions on one modality while protecting another from direct manipulation. On Lorenz-63 and double-pendulum systems, hierarchical policies improve transfer over independently trained policies. On Lorenz-63, they also achieve a higher mean reward than repeated planning with the same reconstructed models, perform comparably to methods trained with controlled interactions, and generalize to systems absent from policy training after embedding inference alone. Applications to neural-behavioral recordings demonstrate suppression of predicted movement under constrained neural perturbations. Together, these findings show how shared dynamical representations support transferable control and mechanistic hypothesis generation from action-free recordings.

---


### 143. [Where to Look Is Not How to Fix: Pre-Denoising Diagnostics and Modality-Dependent Control in Diffusion Composition](https://arxiv.org/abs/2610.03068)

**<font color=#1a73e8>作者：</font>** Fangzheng Wu, Brian Summa  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding compositional failures in text-to-image diffusion requires identifying both where stress is detectable and how intervention changes the output. We study these questions through a controlled anchor--stress protocol that jointly evaluates text-encoder diagnostics and denoiser interventions. We introduce a text-only Compositional Stress Index (CSI), which separates common from rare compositions across SD1.5, SDXL, and the SD3 text path and provides an upstream diagnostic coordinate. A matched six-prompt localization study links intervention location to distinct outcomes: residual-minimizing embedding adapters improve representation fit, while downstream cross-attention intervention increases color hit rate (CHR) by 0.0272. Across SD1.5 and SDXL denoiser blocks, the largest positive signed diagnostic-accessibility mean occurs at the deep encoder, whereas selective boost has its largest positive mean CHR response at decoder blocks. Selective subtraction and broad ablation reveal further modality- and architecture-dependent responses, including a substantial CHR decrease when SDXL decoder cross-attention is broadly ablated. We find a diagnosis-control dissociation under our controlled attribute-object composition setting: compositional defects are diagnosable before denoising, but the representation coordinate that exposes risk is not necessarily the coordinate or modality that improves generation.

---


### 144. [Learn Feasibility Once, Optimize All Objectives: Derivative-Free Diffusion Models for Chance-Constrained Programming](https://arxiv.org/abs/2610.03071)

**<font color=#1a73e8>作者：</font>** Ziwen Liu, Yan Liu, Congying Han 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chance-constrained programs (CCPs) optimize decisions under uncertainty by limiting the probability of constraint violation. Despite advances in traditional and learning-based approaches, optimizing non-convex or non-smooth objectives and adapting to different objectives under fixed chance constraints remain challenging. In this paper, we propose a \textbf{D}erivative-free \textbf{D}iffusion-based framework that \textbf{D}isentangles constraint modeling from objective optimization, termed \textbf{D$^3$Opt}. We learn the chance-feasible structure once, independently of any particular objective, by training a risk-conditioned diffusion model solely on constraint-filtered decisions and freezing it as a reusable prior for post-specified objectives. At inference time, we propose an annealed, particle-based Feynman--Kac correction along the frozen reverse diffusion process to optimize post-specified objectives using only function evaluations. This enables derivative-free optimization of non-convex and non-smooth objectives without objective-specific retraining. We prove that the correction preserves feasibility when this property holds for the frozen prior, and derive an optimization-error bound separating learned-prior coverage, finite-particle approximation, and finite-temperature effects. Experiments on linear Gaussian CCPs, objective-transfer tasks, and chance-constrained economic dispatch demonstrate effective optimization across smooth and non-smooth objectives, including non-convex cases, and objective generalization under fixed chance constraints without retraining.

---


### 145. [An automated pipeline for standardised speech-unit annotation in spontaneous dialogue](https://arxiv.org/abs/2610.03078)

**<font color=#1a73e8>作者：</font>** Hanlu He, Harald Vilhelm Skat-Rørdam, Ingvi Örnólfsson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Quantifying conversational dynamics requires reliable identification of interactional units and their temporal boundaries, but speech activity alone does not distinguish conversational turns from listener feedback or within-turn pauses. We present an automated pipeline for extracting turns and backchannels from separate-channel recordings of spontaneous dyadic conversation, designed to provide a consistent first-pass annotation for subsequent human review. The pipeline combines voice activity detection, channel-energy filtering, temporal merging, automatic speech recognition, and context-based post-processing. We evaluated the pipeline on 99 ten-minute Danish conversations from 33 dyads using segment-level detection reliability and temporal boundary error. Conversations were recorded under both normal and asymmetric listening conditions. In the latter, speech-shaped noise was delivered to one participant through bone-conduction headphones. Overall detection reliability was F1=0.621, with similar performance for turns F1=0.624 and backchannels F1=0.618. For successfully matched segments, median absolute onset and offset errors were 0.150 and 0.160s for turns and 0.130 and 0.180s for backchannels, respectively. Mean errors were substantially larger for turn boundaries, indicating a smaller number of large boundary mismatches. Performance did not differ significantly across the two experimental listening conditions. In a four-conversation case study, pipeline-human agreement was lower and more variable than human inter-annotator agreement and varied across parameter settings. These results support the pipeline as an automated first pass within a semi-automated annotation workflow, providing a consistent basis for more standardised and reproducible annotation of conversational dynamics.

---


### 146. [RIFAR: Reliability and Forgetting-Aware Replay for Continual Robot Learning](https://arxiv.org/abs/2610.03079)

**<font color=#1a73e8>作者：</font>** Zirong Song, Zheng Lu, Haoran Liao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Genuine embodied agency requires robots to turn continuous real-world experience into lasting, transferable skills. This demands continual learning that integrates new capabilities without eroding prior knowledge as tasks and environments evolve. Experience replay mitigates forgetting, but storing complete demonstrations becomes costly as tasks accumulate. World-action models offer a generative alternative, reconstructing past experience through joint predictions of actions and future observations. However, visually coherent rollouts may contain actions that cannot realize the predicted transitions, while new-task adaptation can disrupt previously learned behavior. RIFAR therefore combines reliability screening with drift-aware replay selection. It reconstructs trajectories from compact demonstration prefixes and uses a frozen inverse-dynamics model to assess action-visual consistency. Training first combines current demonstrations with the highest-quality screened trajectories. RIFAR then compares action predictions before and after this adaptation on identical historical inputs, reselecting trajectories with larger normalized drift from the same screened pool for continued training. Across three LIBERO suites and real-world experiments, RIFAR surpasses the previous state of the art in WAM-based generative replay. On LIBERO-Goal, it achieves 90.97 AUC while retaining only 320 historical time steps per task, approximately 4.9% of the steps retained using 50-demonstration replay.

---


### 147. [Smart Sensing for Safer Bridges: From Sensor Signals to AI-Driven Anomaly Detection](https://arxiv.org/abs/2610.03082)

**<font color=#1a73e8>作者：</font>** Rahul Jaiswal, Joakim Hellum, Halvor Heiberg  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bridges contribute significantly to transportation connectivity and urban development. Therefore, reliable bridge monitoring is crucial for protecting public safety and detecting anomalous behavior in bridge sensor data that may provide early indications of abnormal structural conditions. This paper investigates anomaly detection in real-world bridge sensor data using two different complementary approaches, namely signal processing and the data-driven machine learning model Isolation Forest. The real-time bridge sensor data is collected from an iBridge sensor device installed on a bridge in Norway. The methods are evaluated using anomaly counts, anomaly detection time, processing rate, anomaly rates, visualization, and temporal agreement. Moreover, a controlled anomaly-injection analysis is performed to evaluate the sensitivity of each method. Numerical results demonstrate distinct detection characteristics and computational requirements, highlighting the potential of machine learning, particularly the data-driven Isolation Forest, alongside signal processing for identifying anomalies in bridge sensor measurements.

---


### 148. [NegT2IBench: When Negation Changes the Picture. A Polarity Benchmark for Text-to-Image Models](https://arxiv.org/abs/2610.03084)

**<font color=#1a73e8>作者：</font>** Omar Elfatairy, Maria A. Bravo, Jessica Bader 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) models are judged by benchmarks that measure whether requested content appears, but these benchmarks largely overlook the complementary ability to satisfy negated constraints, for example, generating "a non-red cup." Measuring negation raises challenges not faced by affirmation-based benchmarks and requires careful prompt and evaluation design. We introduce NegT2IBench, a benchmark of 4,800 prompts covering two attribute types and four relation categories. Prompts are organized by polarity: the number of positive statements that must hold and negated statements that must not, each ranging from 0 to 2. Varying the two independently separates the effect of negation from the effect of prompt complexity. Our detector-based scoring is reproducible, auditable, and pinpoints which requirement failed. On 600 images with three-annotator labels, it agrees with humans as closely as vision-language judges up to 30x larger, while using only a fraction of their GPU memory. Across eleven T2I models and 211,200 images, nine score lower on a single negated statement than on a single positive one. Per-statement scoring reveals that the loss is largest for color and near zero for proximity, and that 41.5% of failed statements render exactly what the prompt forbids. Rendering what a prompt asks for and withholding what it forbids are distinct capabilities that an aggregate compositional score cannot distinguish. NegT2IBench measures the latter directly, providing a controlled testbed for diagnosing negation failures and developing methods to overcome them.

---


### 149. [Light Entropic Optimal Transport on Riemannian Manifolds](https://arxiv.org/abs/2610.03085)

**<font color=#1a73e8>作者：</font>** Xavier Aramayo-Carrasco, Petr Mokrov, Alexander Korotin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Entropic Optimal Transport (EOT) has become a practical framework for learning stochastic couplings between complex distributions, with applications in generative modeling and domain adaptation. However, most EOT solvers are designed for Euclidean spaces, while manifold extensions remain limited and often rely on costly iterative methods, simulated dynamics, or generic neural models that do not fully exploit the underlying geometry. We introduce ManifoldLightOT, a light approach for learning kernel-induced EOT couplings directly on common manifolds. Using the kernel form of the EOT solution, we construct geometry-specific Gibbs kernels together with compatible potential parameterizations for spheres, tori, $\mathrm{SO}(3)$, and $\mathrm{SE}(3)$. These choices yield closed-form normalization and directly sampleable conditional distributions. Our formulation naturally extends to products of manifolds, making it applicable to more complex geometries. The parameters of the potentials are optimized directly from samples using Monte Carlo estimates of the learning objective. Through synthetic and real-world experiments, we show that ManifoldLightOT often outperforms existing manifold OT methods while retaining direct sampling.

---


### 150. [ULTRADISCOVERY: Abductive Exploration in an Interconnected, Epistemically Open Universe](https://arxiv.org/abs/2610.03092)

**<font color=#1a73e8>作者：</font>** Weihan Li, Tianshi Zheng, Yangqiu Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific discovery often begins when scattered clues call for a new way of describing the world. Such abductive exploration can require constructing the representation in which an explanation is stated, when the world is epistemically open, and composing evidence scattered across contexts, when it is structurally interconnected. Existing benchmarks rarely separate these two demands or control them independently. We introduce ULTRADISCOVERY, an interactive world of five domains in which an agent revises an initially successful theory and predicts the outcome of an unseen cross-domain intervention. A $2 \times 2$ design leaves the representation open or discloses it, and leaves the evidence distributed or aligns it, with the latent dynamics fixed. With the representation open, agents across eleven models often retract the axiom they were taught, and none introduces the unobserved entity or rewrites the variables that a replacement requires. Disclosure triples intervention requests and adds about one of the eighteen findings the world affords, and alignment adds less. Two vendor-harness systems carry discovery into more domains, and one of them rewrites the variables in Open episodes. No system makes the exact prediction within 200 paid actions. At larger budgets one exact prediction appears with both aids, while every Open episode remains inexact. The results locate the difficulty in the step from accumulating evidence to composing it into a representation that transfers.

---


> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-260](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
