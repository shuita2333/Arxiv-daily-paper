# 📦 其他研究 | 2026年09月29日

> 本类共 **225** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-225](./part-05.md)

---

### 101. [Learning Chance-Constrained MDPs with Bellman Distributional Certificates](https://arxiv.org/abs/2609.30856)

**<font color=#1a73e8>作者：</font>** Chenbei Lu, Hongyu Yi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safe reinforcement learning (RL) commonly enforces expected-cost constraints, but such expectation safety may fail to control the probability of rare high-cost trajectories. Chance-constrained MDPs (CCMDPs) impose a stronger probability-level requirement, but are widely viewed as harder because the chance constraint is nonconvex and depends on the full trajectory rather than a Bellman-linear expectation. In this paper, we reveal that this computational difficulty does not necessarily imply a higher statistical price. For tabular discounted CCMDPs with fixed bounded successor support and access to a certified planning oracle, we establish a model-based upper bound, with a matching lower bound up to logarithmic terms. Technically, our key idea is the \emph{Bellman distributional certificate}, which constructs a Bellman recursion for constraint violation probabilities before policy selection. The certificate can be reused across candidate policies; combined with shared row-wise reverse-KL confidence sets, it gives a policy-uniform trajectory-KL transfer without a union bound over policies or time--budget Bellman tables. For stochastic policies, we give a model-free variance-reduced policy-gradient algorithm with a finite-sample expected KKT-residual guarantee and independent validation of every accepted policy. Numerical experiments on synthetic CCMDPs and an IEEE 14-bus energy storage control benchmark illustrate the safety and mechanism behavior of the proposed algorithms.

---


### 102. [Reliability-Regulated Trajectory Optimization for Progressive COLMAP-Free 3D Gaussian Splatting](https://arxiv.org/abs/2609.30865)

**<font color=#1a73e8>作者：</font>** Zijian Wu, Jinliang Wang, Zidian Lin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> COLMAP-free 3D Gaussian Splatting (3DGS) bypasses computationally expensive structure-from-motion (SfM) pipelines, yet progressive camera pose tracking remains fundamentally vulnerable to error compounding---early pairwise tracking inaccuracies both corrupt subsequent frame initializations and remain permanently frozen in the scene representation. Rather than relying on heavyweight external neural priors or treating progressive tracking through isolated heuristic fixes, we propose a unified reliability-regulated trajectory optimization framework for progressive COLMAP-free 3DGS. At its core, our framework establishes an intrinsic, self-supervised bidirectional cycle-consistency mechanism that systematically regulates progressive camera trajectory estimation across two complementary temporal horizons: (1) Forward Motion Propagation, where the online reliability signal adaptively gates first-order kinematic warm-starts of rigid motion into upcoming pairwise registrations, supplying informed directional search priors while safely intercepting untrusted transitions; and (2) Retrospective Trajectory Correction, where the same reliability signal dynamically weights relative-pose consistency constraints within a sliding window of neighboring camera poses. By governing both prospective state initialization and retrospective trajectory consolidation through a unified reliability regulator, our self-contained framework resolves progressive drift without external priors or offline preprocessing. Extensive evaluations on Tanks and Temples and CO3D-V2 benchmarks show that our method substantially improves camera trajectory accuracy and novel-view rendering quality, outperforming existing unposed baselines. Code is available at this https URL.

---


### 103. [TISD: On-Policy Self-Distillation with Trajectory Intervention](https://arxiv.org/abs/2609.30878)

**<font color=#1a73e8>作者：</font>** Taeckyung Lee, Rinat Amankos, Jeonghye Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) provides dense teacher targets, but evaluates them only along student-sampled rollouts. When the privileged teacher favors an alternative action at a visited prefix, OPSD can provide a target for the branch decision but cannot supervise the successor contexts induced by that action unless the student samples it. This creates a training-time data-collection bottleneck and suggests a different role for teacher-student disagreement: proposing a trajectory branch rather than identifying a sufficient local repair. Our diagnostic framework using controlled token interventions reveals that a teacher-preferred token at peak disagreement can improve student continuation success, while its local corrective value is limited. Motivated by this finding, we introduce a simple branch-regenerate-distill algorithm, Trajectory-Intervention Self-Distillation (TISD). TISD forces a teacher-selected branch action, returns suffix generation to the student, and distills the full trajectory under the privileged-context-conditioned teacher. Across the coding models, TISD improves average Avg@4 over SDPO by 1.2 percentage points. Across the science domains, it improves average Avg@128 by 0.8 points under an equal-step budget and by 0.3 points under an equal-time budget. These results support teacher-guided branching as a way to expose useful successor contexts for self-distillation.

---


### 104. [From Tapping to Hopping: Augmenting Mobile GUI Agents with App-Native Deeplinks](https://arxiv.org/abs/2609.30887)

**<font color=#1a73e8>作者：</font>** Yuchen Sun, Chenglin Cai, Gongjie Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mobile GUI agents complete tasks using GUI actions like taps and swipes. These actions are broadly applicable across applications, but reaching a navigation interface. A single deeplink call can replace a sequence of screen-by-screen GUI actions. We therefore introduce hybrid interaction, using deeplinks for direct navigation and GUI actions for other on-screen operations and fallback. To enable this, we discover candidate deeplinks through static analysis, validate them on real devices, and describe their observed landing screens. This process creates a verified and grounded deeplink catalog that pairs each working deeplink with a description of its landing screen. Using this catalog, we introduce GUI-Hopper, a improves task success in commercial applications on real devices, further demonstrating the benefits of hybrid interaction.

---


### 105. [From Segments to Trajectories: Evolving Affective Graphs with Evidence Retrieval for Continuous EEG Emotion Recognition](https://arxiv.org/abs/2609.30890)

**<font color=#1a73e8>作者：</font>** Chi Yang, Jihong Wang, Chengxi Xie 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG)-based emotion recognition is important for affective computing and human-computer interaction, yet most existing methods divide a long trial into short segments and assign each segment the label of its source trial. Although this strategy increases the number of training samples, it reduces an evolving emotional response to a segment-level, coarse-grained, and static prediction problem. In reality, emotion may continuously emerge, intensify, weaken, and fluctuate as a stimulus unfolds, motivating the prediction of a time-aligned affective trajectory from the complete EEG trial. This task requires coordinated modeling of how spatial neural organization evolves throughout the trial and how local emotional fluctuations interact with longer-term trends. In this work, we formally define and systematically investigate continuous EEG emotion recognition as whole-trial affective trajectory prediction. We propose EAGER, an Evolving Affective Graph framework with Evidence Retrieval for continuous EEG emotion recognition. EAGER comprises two complementary modules: Affective State-guided Topology Evolution models the evolving spatial organization of EEG activity, while Multi-scale Temporal Evidence Retrieval integrates short-term fluctuations with longer-range temporal trends for time-aligned prediction. Experiments on MAHNOB-HCI, SEED-VII, and REFED show consistent gains in trajectory-tracking metrics over representative methods, with competitive pointwise errors.

---


### 106. [Robust to Which Model Change? A Unified Evaluation of Robust Counterfactual Explanations](https://arxiv.org/abs/2609.30918)

**<font color=#1a73e8>作者：</font>** Marcin Kostrzewa, Maciej Zięba  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Robust counterfactual explanations promise recourse that still works after the model behind it changes. Whether they keep that promise depends on what the change is. A small perturbation of the parameters, retraining on new data, and a new architecture are different events, and each existing method is evaluated against the one it was built for. Reported robustness scores, therefore, answer different questions and cannot be compared. We propose a unified cross-family evaluation protocol that holds factual instances and generated counterfactuals fixed while testing every method against the same eight types of model change. The benchmark compares six robust methods and two standard baselines on four tabular datasets. It characterizes every changed classifier through its outputs and reports empirical robustness together with coverage, base validity, and proximity. We find that relative performance and failure modes vary across change families. Bounded parameter perturbations change 0.95\% of test predictions on average, compared with 4.9\% for bootstrap retraining. Methods with guarantees for these perturbations do not necessarily transfer to other changes. RobX transfers most consistently in our experiments, although greater stability can require larger interventions. We argue that robust CFE methods should be evaluated through a common protocol that specifies the model changes, measures their realized behavioral magnitude, and keeps generation performance separate from robustness.

---


### 107. [How to break the Miranda signature scheme over matrix Gabidulin codes](https://arxiv.org/abs/2609.30925)

**<font color=#1a73e8>作者：</font>** Adrien Vinçotte  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Miranda signature scheme relies on masking a matrix code which disposes of a masked underlying structure, and the knowledge of which allows for efficient error decoding. We consider a Gabidulin code which is expanded into a matrix code, that is only \Fq-linear. An additional masking is then applied to it. The attack proposed here shares similarities with that of [Le26, https://arxiv.org/abs/2608.03328] on the EGMC encryption scheme, which also follows the paradigm described above. It consists in recovering the Fqm-linear structure of a masked matrix Gabidulin code by reducing to a MinRank instance to be solved over the extension field Fqm, but where the matrices have coefficients in Fq. Such an instance can be efficiently solved. However, unlike the previous attack, it is possible to reduce in polynomial time to such a MinRank instance in the case of the Miranda signature scheme. This results in a particularly efficient key recovery attack against the parameters proposed for Miranda. For example, for the proposed parameter set with m=79, the complexity drops from 146 bits to 46 bits in this attack.

---


### 108. [EPOC: Endpoint-Preserving Online Correction With Compressed Residual State for Multi-Horizon Time Series Forecasting](https://arxiv.org/abs/2609.30929)

**<font color=#1a73e8>作者：</font>** Takumi Fujimoto, Hiroaki Nishi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Completed multi-horizon forecasts provide residual feedback for a fixed forecaster, but retaining full residual blocks increases auxiliary state. We propose Endpoint-Preserving Online Correction (EPOC) with a compressed residual state. It stores low-order discrete cosine transform (DCT) coefficients and the final value of the preceding residual block. Within each channel, the endpoint is shared across component-wise online ridge regressions that also use current-forecast coefficients. The fitted DCT correction is blended with the base forecast. We evaluate eight multivariate series with DLinear and PatchTST, three seeds, and two training variants, yielding 96 matched fixed-base conditions at a 24-step horizon. EPOC achieves mean condition-wise reductions in mean squared error (MSE) and mean absolute error (MAE) of 15.40% and 9.35% from the uncorrected base, respectively, with a median of 6,352 B in retained auxiliary arrays. It has lower paired MSE than the $\delta$-Adapter, COSA, FAC, and OMPB in a majority of conditions and uses less state than each. Full ELF achieves the largest mean MSE reduction, 19.29%, but its median retained state is 474,048 B ($\times$75 relative to EPOC). Equal-size summary controls favor the endpoint by 1.65--2.20% in paired MSE; a coefficient-reconstructed endpoint yields similar accuracy to the observed endpoint, highlighting its role as a shared input. Increasing the retained DCT component count from 4 to 8 adds 1.00 percentage point of MSE reduction for 5,728 B. On jointly trained bases, EPOC lowers MSE by 16.69--20.15% relative to globally blended TEFL-style adapters applied to the same base. The code and numerical records are available at this https URL.

---


### 109. [Spackle: Completing Large View Single Image NVS with Adaptive Gaussians](https://arxiv.org/abs/2609.30941)

**<font color=#1a73e8>作者：</font>** Xuanzhi Liu, Yuhe Zhou, Xinyi Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-image novel view synthesis (NVS) enables photorealistic rendering of un- observed viewpoints from a single input. Practical NVS systems require two key capabilities: robust reconstruction of occluded regions and high inference effi- ciency. While hybrid decoupled frameworks combining feedforward 3D Gaussian Splatting (3DGS) and diffusion models show promise for large-view-deviation NVS, they suffer from capacity competition: a fixed number of Gaussians forces resource shifts from visible to newly disoccluded areas, degrading original scene fidelity when the target view deviates significantly from the input. To address this, we propose Spackle, a lightweight residual learning framework that mit- igates capacity competition without sacrificing efficiency. Spackle operates in three stages: predicting base 3DGS attributes from given views, automatically identifying poorly reconstructed regions, and learning a residual 3DGS optimized exclusively for these areas. At inference, we combine the baseline and aug- mented Gaussians for NVS. We conduct comprehensive experiments and show that Spackle achieves state-of-the-art performance on large-view-deviation cases.

---


### 110. [OneWorld: Learning Consistent Physics Across Actions in World Models](https://arxiv.org/abs/2609.30946)

**<font color=#1a73e8>作者：</font>** Ke He, Yichen Ding, Bin Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Action-conditioned video world models aim to predict scene evolution under different actions, a capability that is essential for reliable planning, decision-making, and interaction in dynamic environments. However, futures generated independently from the same initial scene may each appear plausible while implying incompatible physical properties, such as friction or mass. This inconsistency can lead to contradictory predictions across interventions, making it difficult for the model to maintain a coherent understanding of the underlying world and limiting its reliability for planning and decision-making. To address these issues, we propose OneWorld, a shared-mechanism counterfactual generation framework that jointly models multiple action-conditioned futures under a common latent physical mechanism. A physical mechanism interpreter first infers a distribution over latent mechanisms from each action-outcome branch. These distributions are then aggregated into shared-world evidence, which captures whether the branches admit a common physical explanation while accounting for uncertainty in less informative branches. This evidence constrains flow training and guides sampling, encouraging consistency in the underlying physical mechanism while preserving the distinct outcomes induced by different actions. We further introduce a multi-intervention evaluation protocol in controlled environments, following the interaction settings of ACWM-Phys, to assess whether generated futures can be jointly explained by the same physical parameters, alongside standard measures of single-rollout prediction quality. Experiments in these environments show that OneWorld improves cross-intervention physical consistency while maintaining competitive single-rollout prediction quality.

---


### 111. [DAPEVO: Deep Adaptive Patch Frame-Event Visual Odometry](https://arxiv.org/abs/2609.30947)

**<font color=#1a73e8>作者：</font>** Luca Gandolfi, Simone Nascivera, Roberto Pellerito 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual odometry is essential for autonomous navigation in GPS-denied environments, yet RGB-based methods remain vulnerable to motion blur, challenging illumination, and dropped frames. Event cameras complement conventional cameras with high temporal resolution and dynamic range, but their asynchronous measurements complicate reliable correspondence estimation. We present DAPEVO, a learned visual odometry system that estimates image and event correspondences independently at shared patch locations and fuses their correlation evidence before motion refinement. Each tracked patch maintains image and event descriptors, and a learned scalar gate combines modality-specific correlation embeddings for each patch--frame edge before a shared recurrent refinement and bundle-adjustment update. DAPEVO also supports event-only observations, enabling continued tracking when RGB frames are sparse or unavailable, while modality-aware keyframe culling preserves scarce frame constraints. On UZH-FPV, when retaining only one in six RGB frames, DAPEVO's mean absolute trajectory error (ATE) increases by only 36%, from 1.00 to 1.36m, whereas the ATE of DPVO and RAMP-VO rises by factors of $3.7\times$ and $3.1\times$, respectively. On TartanEvent, DAPEVO similarly remains below 1m ATE at 3Hz RGB input, while DPVO and RAMP-VO exceed 9m. Under degraded RGB input on TartanEvent, DAPEVO achieves an ATE of 0.60m, compared with more than 4m for both DPVO and RAMP-VO, while also outperforming event-only DEVO at 0.87m.

---


### 112. [PORL: Pretrained Offline Reinforcement Learning for the Job Shop Scheduling Problem](https://arxiv.org/abs/2609.30948)

**<font color=#1a73e8>作者：</font>** Mateo Toro Diz, Jonathan Hoss, Noah Klarmann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Job Shop Scheduling Problem (JSSP) is a fundamental combinatorial optimization problem in industrial optimization. This work introduces Pretrained Offline Reinforcement Learning (PORL), a hybrid approach that combines simulation-based online pretraining with offline fine-tuning on production-specific data.
Reinforcement learning through online interaction enables exploration of general scheduling strategies, but typically relies on simulation environments and may suffer from a simulation-to-reality gap. In contrast, offline RL avoids direct interaction with the environment by learning from historical data, but its performance is strongly influenced by dataset quality and coverage. PORL combines the strengths of both paradigms by first learning a general scheduling policy through online interaction and subsequently adapting it offline to a target distribution. A KL-divergence-based policy constraint is introduced to limit deviations from the pretrained policy during fine-tuning.
The approach is evaluated on JSSP instances with distribution shift and datasets generated from heuristic, noisy-expert, and random behavioral policies. The results show that PORL consistently achieves lower optimality gaps than standalone offline RL and the considered general scheduling baselines. Furthermore, its advantage over standalone offline RL increases as dataset quality decreases, indicating reduced sensitivity to the quality and coverage of the available offline data. The results suggest that offline adaptation of pretrained policies is a promising approach for industrial scheduling environments where direct online exploration is impractical.

---


### 113. [IDM-Net: A Lightweight Illumination-Decoupled Modulation Network for Low-Light Image Enhancement](https://arxiv.org/abs/2609.30962)

**<font color=#1a73e8>作者：</font>** Cheng-Yen Hsiao, Jing-Ming Guo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-light image enhancement (LLIE) remains challenging for lightweight models because illumination restoration and color fidelity are difficult to optimize simultaneously in the RGB color space. Although recent color-decoupled methods separate luminance and chrominance representations, they primarily optimize luminance as an enhancement target, leaving its potential as an explicit guidance prior largely unexplored during feature reconstruction. To address this limitation, we propose IDM-Net, a lightweight Illumination-Decoupled Modulation Network for low-light image enhancement. IDM-Net adopts a dual-encoder architecture consisting of a structure encoder that extracts multi-scale appearance features from the RGB image and a lightweight illumination encoder that learns illumination priors from the decoupled luminance (Y) channel. To effectively exploit these priors, we introduce an Illumination-Guided Modulation (IGM) module that injects multi-scale illumination cues into the decoder through spatially adaptive affine modulation, enabling accurate brightness restoration while preserving natural color consistency. Furthermore, we design a lightweight Feature Refinement Block (FRB) to progressively suppress degradation artifacts and recover fine-grained image details during reconstruction. Extensive experiments on multiple standard low-light image enhancement benchmarks demonstrate that IDM-Net achieves competitive performance among lightweight LLIE methods while maintaining an excellent balance between restoration quality and computational efficiency.

---


### 114. [Where and When to Force: Routed Forcing for Streaming Avatars](https://arxiv.org/abs/2609.30963)

**<font color=#1a73e8>作者：</font>** Zihan Su, Siwen Lu, Junhao Zhuang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-driven streaming avatar generation requires real-time synthesis of speech-synchronized videos with dynamic and diverse motion. Self Forcing uses Distribution Matching Distillation (DMD) to distill bidirectional video diffusion models into causal, few-step generators for real-time streaming. However, DMD minimizes a reverse KL divergence, which is inherently mode-seeking: it causes the student to discard high-dynamic modes and collapse onto static outputs, compressing both dynamics and diversity of generated videos. We find that this collapse is region-heterogeneous: person regions involving pose and gesture variations suffer the largest diversity loss, the audio-driven mouth region shows a small loss, and the background remains nearly stable. Based on this observation, we propose Routed Forcing, which routes the distillation objective by semantic region and noise stage to improve dynamics and diversity while preserving visual quality. Specifically, (1) Where to Force: Semantic-Region Routing applies Data-Forcing Distillation (DFD), which supervises the student with real videos, to the person region where diversity collapse is most severe, while retaining DMD for the mouth and background to preserve lip synchronization and scene stability. (2) When to Force: Noise-Stage Routing activates DFD at high noise stages, where real video serves as effective supervision to inject diverse and dynamic motion patterns. At low noise stages, DMD is used to refine details, avoiding blur and artifacts from spatial differences between real video and student-generated video. Experiments show that Routed Forcing improves dynamics by up to 45% and diversity by 7-25% over Self Forcing, while preserving video quality and lip synchronization.

---


### 115. [Gradient Surgery for Physics-Informed Neural Networks](https://arxiv.org/abs/2609.30966)

**<font color=#1a73e8>作者：</font>** Thomas Borsani, Giuseppe Di Fatta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-Informed Neural Networks (PINNs) are trained by optimising a composite objective that combines data fitting with physics-based constraints, typically resulting in a highly imbalanced multi-task optimisation problem. Under these conditions, existing optimisation strategies are affected by conflicting task gradients, leading to slow convergence and unstable training, particularly for stiff and high-frequency partial differential equations. We analyse gradient conflicts throughout training of PINNs with standard optimiser and investigate Multi-Task Deep Learning (MTDL) optimisation methods. In our analysis across four benchmark problems we observed that PINN optimisation exhibits three distinct phases in which angle- and magnitude-based gradient conflicts alternate, with only one present at a time. Building on these observations, we propose PAM-GS, a physics-aware gradient surgery method that adaptively mitigates task interference during training according to the observed conflict types. Experiments on four representative PDE benchmarks demonstrate that PAM-GS combines competitive solution accuracy with consistently strong task-balanced performance, outperforming existing methods on most problems.

---


### 116. [SciHorizon-eLab: An Agentic Protocol-to-Task Compiler for Scalable Benchmarking of Scientific Embodied Agents](https://arxiv.org/abs/2609.30971)

**<font color=#1a73e8>作者：</font>** Maokai Qin, Chuan Qin, Qi Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Embodied agents offer a promising route to automating scientific experimentation, yet their progress is constrained by the lack of reliable and systematic evaluation environments. Existing simulation-based laboratory benchmarks rely heavily on manual task engineering, making it challenging to systematically compile diverse scientific protocols into executable and verifiable embodied tasks at scale. To address this challenge, we introduce SciHorizon-eLab, an agentic protocol-to-task compiler that formulates scientific embodied task construction as a compilation problem. Given a natural-language protocol of scientific experiments, SciHorizon-eLab progressively compiles laboratory protocols into semantic-preserving embodied tasks through semantic grounding, executable task synthesis, and multi-stage simulation-based certification. The system generates semantically grounded environments, executable manipulation programs, and step-level success specifications, while enabling reproducible generation of expert demonstrations and execution traces. Using this pipeline, we further construct \BenchName, a ready-to-use benchmark comprising 300 certified tasks across diverse laboratory operations. It supports HIL task execution, reproducible expert-demonstration generation, and ordered step-level evaluation. Across representative tasks, the strongest policy attains an average success rate of only 49.7%, with further evaluations revealing pronounced weaknesses in human and embodied agent coordination. We publicly release the code, benchmark data, and evaluation toolkit at this https URL.

---


### 117. [Factorized axis convolutional gated recurrent unit with dynamic adaptive pooling for remaining useful life prediction of rolling bearings](https://arxiv.org/abs/2609.30972)

**<font color=#1a73e8>作者：</font>** Hanbyeol Park, Jungho Choo, Hyerim Bae  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Convolutional neural networks (CNN) are widely used to predict the remaining useful life (RUL) of rolling bearings from time-frequency representations (TFRs) of vibration signals. However, during degradation, characteristic structures in TFRs align predominantly along the frequency or time axis, making it challenging for conventional CNN isotropic kernels to capture directional structure. Furthermore, global average pooling (GAP) averages across axes, potentially obscuring the locations and concentrations of salient activations. This study introduces a factorized-axis convolutional gated recurrent unit (GRU) that employs multiscale anisotropic convolution and dual-axis convolution block attention module to enhance directional features and highlight salient time-frequency regions. Dynamic adaptive pooling (DAP) adaptively aggregates the time-frequency-axis information from the extracted feature maps, whereas a GRU captures temporal dynamics in the latent representations and Monte Carlo dropout enables predictive uncertainty estimation. Experiments on two public bearing datasets demonstrate that the proposed model outperforms existing RUL prediction methods across operating conditions. Ablation experiments demonstrate that the factorized axis-wise design achieves lower mean errors than convolutional isotropic kernels. DAP yields clear improvements on one dataset while matching GAP on the other, highlighting the importance of anisotropic feature extraction and adaptive feature aggregation for TFR-based RUL prediction.

---


### 118. [LipSSM: Structurally Lipschitz-Bounded Cascaded State-Space Model via Metric Transfer between Consecutive SSM Layers](https://arxiv.org/abs/2609.30973)

**<font color=#1a73e8>作者：</font>** Natsuki Yoshino, Ren Uchida, Kazuki Matsumoto 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lipschitz continuity is a fundamental principle in the design of certifiably robust deep neural networks (DNNs), wherein adjusting the Lipschitz constant, which quantifies network robustness, is of central theoretical importance. A standard approach to enforcing Lipschitz continuity requires each layer of a DNN to be Lipschitz continuous, thereby guaranteeing overall Lipschitz continuity. However, this layer-wise approach typically imposes overly conservative restrictions by producing a loose estimate of the overall Lipschitz constant, which limits the expressive capacity of the DNN and degrades empirical performance at a prescribed level of robustness. To overcome this loose estimation, the recently proposed LipKernel transfers information across layers to yield a much tighter overall Lipschitz bound than conventional layer-wise construction. In this paper, we extend this concept to cascaded state-space models (SSMs) to construct Lipschitz-continuous DNNs capable of modeling longer-term dependencies. The proposed architecture, named LipSSM, is theoretically justified and empirically evaluated.

---


### 119. [Coupled Usage-Sense Processes: Temporal and Attributable Lexical Semantic Change](https://arxiv.org/abs/2609.30974)

**<font color=#1a73e8>作者：</font>** Haruka Ezoe, Ryohei Hisano  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Lexical semantic change is usually summarized by a scalar distance between independently sampled period distributions. This measures how much a word changed, but does not reveal when it changed, which mechanisms and component movements carried the change, or which usages support the attribution. We introduce Coupled Usage--Sense Processes (CUSP), which derives these answers from a single marginal preserving temporal process. A hierarchical coupling relates contextual distributions through latent usage components, while Markov composition makes adjacent and longer span correspondences compatible. Displacement operators quantify change magnitude and timing, split variation exactly between movement of component centers and reorganization within components, and attribute it to transported component pairs. Word-local modes resolve distinct directions of change and their activity over time, while representative passages from attributed components ground the analysis in text. Under a Gaussian mixture specialization, we prove parametric recovery of the operators and squared distances. Synthetic experiments support the predicted rate. CUSP remains competitive on English and German DWUG and recovers controlled Janus profiles while maintaining compositionally coherent transport. A large corpus of US court opinions demonstrates transition, mode, and passage attribution in unlabeled natural text. CUSP thus makes magnitude, timing, mechanism, movement, modes, and textual evidence compatible views of one lexical history.

---


### 120. [Does Uniform Discrete Diffusion Need Time?](https://arxiv.org/abs/2609.30977)

**<font color=#1a73e8>作者：</font>** Chunsan Hong, Chieh-Hsin Lai, Satoshi Hayakawa 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uniform discrete diffusion models (UDMs) commonly use explicit time conditioning, but we find that it can often be unnecessary in practice. In this paper, we first show that the population-optimal UDM predictor generally depends on time: time controls how much the model should trust the observed context. We then show that this dependence can become negligible in finite-data settings relevant to language. When a corrupted training sequence remains much closer to its original clean sequence than to competing training sequences, the empirical-optimal predictor is nearly insensitive to time over most of the diffusion trajectory, where the guarantee weakens toward the high-noise endpoint. Empirically, trained language UDMs exhibit limited time sensitivity over most of the trajectory, while time-agnostic predictors remain competitive with, and often outperform, time-conditioned models across datasets and training objectives. These results challenge the use of explicit time conditioning in UDMs: although the population optimum depends on time, explicitly conditioning on it may often be unnecessary in practice.

---


### 121. [FeatMark: Feature-level Watermark Protection against Mimicry Attacks with Diffusion Models](https://arxiv.org/abs/2609.30980)

**<font color=#1a73e8>作者：</font>** Haoyang Li, Ruoxi Sun, Qingqing Ye 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models enable data-efficient "mimicry" attacks, wherein adversaries fine-tune the model on a handful of public photos to synthesize convincing forgeries of a target individual. A common countermeasure is to embed imperceptible, low-energy watermarks, yet recent studies show these signatures are brittle: modest post-processing or lightweight adversarial perturbations readily suppress detection, exposing a fundamental tension between imperceptibility and robustness. We introduce FeatMark, a watermarking framework that shifts from pixel-level, energy-starved perturbations to inconspicuous semantic features: small, scene-consistent micro-features that remain natural to humans while providing a stronger, machine-verifiable provenance signal. FeatMark builds domain-specific feature banks that encode each watermark as a compact concept program, pairing open-vocabulary semantic cues with reliable edit regions and instruction templates. It then automatically selects features that are both feasible and executable and injects them through modular, mask-guided concept editing, yielding highly localized, scene-consistent micro-edits that are difficult to perceive. We conduct extensive experiments across VGGFace2, CelebA-HQ, and WikiArt, evaluating against 10 strong watermark removal/purification attacks (including regeneration-style purification) and several bespoke adaptive attacks tailored to FeatMark, to assess perceptual fidelity, watermark detection accuracy, and robustness. We further demonstrate FeatMark's extensibility to video mimicry attacks. The results show FeatMark remains virtually impervious, withstanding all evaluated attacks with negligible bit-accuracy and fidelity degradation.

---


### 122. [FARE: Forensic Acceptance Region Estimation for Catching Bait-and-Switch Image Generators](https://arxiv.org/abs/2609.30982)

**<font color=#1a73e8>作者：</font>** Kai Yao, Marc Juarez  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern AI image generators are increasingly deployed as opaque APIs, where customers can query the deployed service, but cannot inspect model weights or architecture. This creates a practical challenge: a provider may pass governance certification with one generator and later silently switch to a cheaper and lower-quality one for deployment, compromising public trust or even safety in high-stakes domains. We study integrity auditing at deployment time and propose FARE (Forensic Acceptance Region Estimation). A certified generator is enrolled by training FARE on images sampled from that generator. After deployment, FARE can determine whether a generated image is consistent with the enrolled generator---using only that image. FARE's features are based on image generator-specific artifacts that have been proposed for forensic applications. FARE amplifies these features during training by finding hard samples that tighten the acceptance region and increase sensitivity to subtle changes in the certified generator. Across generator swaps, including substitutions with similar model versions and model variants, FARE is effective at detecting swaps, consistently outperforming existing baselines at strict operating points, and remains effective under the exact-model and decision-only attacks evaluated in this work.

---


### 123. [THA: Weighted Finite-State Text Normalization and Inverse Text Normalization for Khmer](https://arxiv.org/abs/2609.30984)

**<font color=#1a73e8>作者：</font>** Seanghay Yath  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-to-speech needs written text in spoken form, and speech recognition output needs the reverse. For Khmer, neither direction has a maintained open-source tool, and the script makes both harder: words are not separated by spaces, and number words occur inside ordinary words. We present Tha, a Khmer text normalization and inverse text normalization toolkit built from weighted finite-state transducers. It segments and classifies a whole line in one shortest-path search, and a second transducer rejects token boundaries inside a Khmer syllable. On Google's Khmer test suite, Tha agrees with the reference on all 274 cardinals up to one spelling variant, and on 2,906 real TTS prompts, 153 of the 158 sentences it rewrites are correct. Tha is open source under the Apache 2.0 license.

---


### 124. [Self-Supervised Perceptually Interpretable Monocular Depth Estimation](https://arxiv.org/abs/2609.30987)

**<font color=#1a73e8>作者：</font>** Zain Ul Abidin, George Dimas, Dimitris K. Iakovidis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised monocular depth estimation (MDE) enables depth prediction from monocular images without requiring ground-truth supervision, making it attractive for large-scale and real-world applications. Despite steady improvements in accuracy, most existing methods remain difficult to interpret, as depth is inferred from RGB representations that obscure the impact of individual perceptual image components. This lack of transparency limits systematic analysis of failure cases and reduces confidence in safety-critical settings. This paper presents a self-supervised framework for perceptually interpretable monocular depth estimation (PIMDE), designed to associate depth predictions with distinct perceptual components of the input image. Rather than operating directly on RGB inputs, the proposed method decomposes each image into a set of perceptual feature maps (PFMs), each encoding a specific visual cue. Distinct depth estimation branches process these PFMs independently to produce depth estimates (PIDEs), which are subsequently combined through an explicit fusion strategy. This formulation allows us to examine directly the contribution of each perceptual cue to the final depth prediction. Experiments conducted on the KITTI benchmark dataset demonstrate that PIMDE achieves performance comparable to established self-supervised MDE methods while providing additional insight into how different perceptual cues influence depth estimation. These results indicate that perceptual decomposition can support interpretability without sacrificing depth estimation accuracy.

---


### 125. [PhoenixSR: Generative Heterogeneous Distillation Unleashes Efficient Models for Real-World Super-Resolution](https://arxiv.org/abs/2609.30988)

**<font color=#1a73e8>作者：</font>** Xin Di, Mingyu Shi, Yuanfei Bao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world image super-resolution (SR) requires recovering perceptually realistic high-resolution images from complex low-resolution observations while preserving faithful content. Diffusion-based SR benefits from strong generative priors but incurs substantial computational overhead, whereas feed-forward CNN and Transformer SR models are efficient yet often struggle to recover realistic high-frequency details. This motivates a natural question: can diffusion priors be transferred to existing diffusion-free SR networks without introducing diffusion components at inference time? To this end, we propose PhoenixSR, a generative heterogeneous distillation framework that transfers diffusion priors to independently designed feed-forward SR networks through score-based distribution matching. Rather than aligning heterogeneous features or imitating sampled diffusion outputs, PhoenixSR uses the pretrained diffusion model as distribution-level supervision, while paired SR supervision preserves reconstruction fidelity. To make distribution matching effective for fidelity-sensitive SR, we introduce Heterogeneous Distribution Adaptation, which adapts the target score to the SR domain, improves tracking of the evolving student distribution, and anchors training with paired supervision. We further employ Directional Reliability Weighting, a lightweight residual-consistency-based reweighting strategy that reduces unstable distributional guidance. All diffusion-related components are removed after training, leaving the original student architecture and inference cost unchanged. Experiments on three SR benchmarks and six feed-forward backbones, including SwinIR, HAT, Real-ESRGAN, and SeeMoRe, show consistent perceptual improvements with largely preserved reconstruction fidelity.

---


### 126. [PICO: Projection-Informed Consistency Optimisation for 6DoF Surgical Tool Pose Estimation](https://arxiv.org/abs/2609.30989)

**<font color=#1a73e8>作者：</font>** Lucy Fothergill, Pietro Valdastri, Dominic Jones 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose: Accurate 6 DoF pose estimation of surgical tools is critical for automa- tion, robotic proprioception, and safe interaction with the tissue operated on. Kinematics-based approaches suffer from accumulated errors due to the cable- driven nature of robotic arms, while vision-based methods often rely on external markers or trackers. Although more recent vision-based advances have been pro- posed, these two-stage pose estimation methods often lack real-time robustness due to accumulated errors and computational overhead. Methods: We propose a novel end-to-end trainable model, PICO. Our model employs a multi-task learning architecture to predict segmentation and depth maps, alongside regression of translation and rotation parameters. We define two proxy tasks that enforce geometric consistency in both 2D and 3D spaces, improving accuracy and robustness. For this, we propose a projection loss, and a point-to-point loss. Results: We evaluate our method on the SurgRIPE dataset, benchmarking its performance against state-of-the-art approaches using standard 6DoF pose esti- mation metrics. Our results demonstrate consistently strong performance across all four subsets, specifically in rotation, ranking second even under occlusion. It also demonstrates comparable translational performance, remaining competitive, especially in occluded cases. Conclusion: PICO demonstrates the effectiveness of multi-task learning and geometry-aware proxy tasks for robust and reliable surgical tool pose estimation, especially in occluded scenarios, highlighting potential for future applications.

---


### 127. [Learning Hierarchical Causal Representations of the Effects of Forcings on Temperature in Climate Models](https://arxiv.org/abs/2609.30995)

**<font color=#1a73e8>作者：</font>** Shan Zhao, Ilija Trajkovic, Julia Kaltenborn 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning (ML) emulators provide a fast and cost-effective method to simulate climate change scenarios after being trained on Earth System Models projections. However, the black-box nature of those data-driven approaches limit the usability and trustworthiness of their outputs and in particular their use as causal attribution tools. Here, we develop a hierarchical causal representation learning framework applied to sea surface temperature fields from a state-of-the-art global climate model. As a key advance over previous work, our framework explicitly models both atmospheric dynamical interactions arising from internal climate variability and forced responses due to changes in atmospheric greenhouse gas and aerosol concentrations. When trained on future climate change scenarios, our method accurately predicts the long-term global mean and regional temperature evolution and shows physically realistic responses to perturbations in greenhouse gas and aerosol concentrations when evaluated on unseen scenarios. Our results underline the potential of causal representation learning frameworks for advancing climate model emulation.

---


### 128. [Can Pixels Alone Reveal Image Origin? Minimax Limits and Learnable Interfaces for Passive Provenance](https://arxiv.org/abs/2609.30997)

**<font color=#1a73e8>作者：</font>** Kai Yao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Passive image provenance asks whether pixels alone can reveal where an image came from: a human, an aggregate AI class, or a particular generator. This becomes a robustness problem once a source image can be edited before the verifier sees it. We study the problem as source--target verification under adversarial distribution shift. Our first result gives the exact best-case limit for any image-only verifier: the largest robust target-acceptance gap equals the minimum total-variation distance between the target distribution and the set of attacked source distributions. This quantity depends on the source, target, and edit class, not on the verifier architecture. Our second result explains why deployed public verifiers can fail before this statistical limit is reached. If the verifier can be emulated on the attack region to error $\varepsilon$, then a surrogate black-box attack reaches target acceptance within $2\varepsilon$ plus optimization error of the white-box optimum; score-revealing logistic and softmax heads over public features are identifiable, and approximate score access gives stable recovery bounds. A finite-state experiment checks the minimax identity where both sides are computable. On same-prompt real/diffusion benchmarks, the evaluated public CLIP verifiers fail under targeted pixel attacks, while a ResNet-18 victim exhibits partial fake-to-real transfer. Binary feedback with abstention reduces measured attack success, but positive empirical gap upper bounds do not establish robustness. These results motivate separate evaluation of the source--target statistical ceiling and the information released by a deployed verifier.

---


### 129. [Weaponizing Ground Truth: Data Poisoning Attacks by Exploiting Boundary Misalignment Between Antivirus Software and Learning-Based Detectors](https://arxiv.org/abs/2609.31003)

**<font color=#1a73e8>作者：</font>** Jieshuai Yang, Zhi Wang, Yan Jia 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine-learning (ML)-based malware detectors are commonly trained using labels obtained from antivirus (AV) engines and aggregation services (e.g., VirusTotal). This practice assumes AV-generated labels provide reliable supervision. However, small byte-level modifications can substantially alter AV verdicts while leaving the representations perceived by downstream ML detectors largely unchanged, producing label-feature inconsistencies that can contaminate training datasets and create poisoning opportunities for ML-based malware detection. We present Bi-Iocane, a black-box poisoning framework that exploits the reliance of malware-labeling pipelines on AV-generated labels. Bi-Iocane identifies AV-sensitive bytes and modifies them to induce label changes. It rewrites such bytes in malware to obtain benign labels (evasion-oriented poisoning) and injects malware-associated byte patterns into benign software to obtain malicious labels (defamation-oriented poisoning). These poisoned samples and their lightly modified variants corrupt training data and cause selected targets to be misclassified. We evaluate Bi-Iocane with 13 AV engines simulating AV aggregation services and eight ML detectors. For 30 malware and 30 benign clean targets, Bi-Iocane combines AV-specific manipulations to generate malware-to-benign and benign-to-malware poisoned samples whose all tested AV-based labels are flipped. After these poisoned samples and variants are used for downstream training, the resulting ML models misclassify 92.08% of the original clean targets on average with only a 0.06\% poisoning budget per target. Meanwhile, the poisoned models largely preserve clean-set performance, and six evaluated poisoning defenses show only limited mitigation. VirusTotal evaluation further confirms practical defamation risk and reveals potential evasion risk in real-world AV-to-ML labeling supply chains.

---


### 130. [GitHub Engagement Signals for CVE Prioritization: The GitHub Popularity Metric (GPM)](https://arxiv.org/abs/2609.31004)

**<font color=#1a73e8>作者：</font>** Jafar Akhoundali, Kristian Rietveld, Olga Gadyatskaya  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Attackers can compromise multiple systems with a single vulnerability, while defenders need to fix all security weaknesses in their systems. This asymmetry puts defenders at a disadvantage. Security vulnerabilities are found at an alarming rate, and patching vulnerabilities is costly and time-consuming; thus, vulnerability prioritization is a must and a time-critical challenge. Many prioritization metrics, such as the CVSS, EPSS, KEV, and SSVC, are currently used, each with different pros and cons, such as openness, degree of automation, time-criticality, coverage, and need for expert input.
In this work, we propose the GitHub Popularity Metric (GPM), a fully open, publicly computable prioritization metric based on the popularity of exploits in GitHub repositories. We use GitHub features such as the number of stars, forks, and related unique users to create a metric that indicates the popularity of CVEs across different time frames, both relative to the current time and historically. We compare the proposed metric with various existing vulnerability prioritization metrics and known exploited vulnerabilities and demonstrate that it provides tangible insights for defenders, identifying unique CVEs and inconsistencies in existing methods. The GPM was integrated into the EPSS version 5.
\noindent\textbf{Note.} A demonstration based on this work has been accepted to the demo track of the ACM Conference on Computer and Communications Security (CCS) 2026.

---


### 131. [TRACKGRAPH: Online Open-Vocabulary 3D Scene Graphs via Image-Space Tracking](https://arxiv.org/abs/2609.31005)

**<font color=#1a73e8>作者：</font>** Peder Borge Hellesylt, Albert Gassol Puigjaner, Kostas Alexis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary 3D maps enable robots to reason about previously unknown environments using natural language. However, existing systems typically segment every incoming image, associate detections with persistent 3D segments, and frequently perform costly Vision-Language (VL) inference. We present TRACKGRAPH, an online open-vocabulary system that maintains short-term 2D mask identity directly in the image stream before fusing segments into 3D. FastSAM masks and CLIP features are computed at sparse keyframes, while dense DINOv3 features are used to propagate masks at a high rate in between. The resulting tracked masks are fused into a class-agnostic 3D segment layer within a hierarchical scene graph, with 3D association handling tracking interruptions and long-term revisits. Compact multi-view CLIP embeddings enable open-vocabulary retrieval. Across Replica, ScanNet++, and HM3D, TRACKGRAPH achieves competitive open-vocabulary segmentation and retrieval against state-of-the-art mapping methods, including the highest synonym frequency on Replica (0.50). On the same NVIDIA A100, it is 1.7x faster and uses 3.3x less GPU memory than ViT-H OVI-MAP. Real-world quadruped deployments demonstrate onboard scene graph construction and object search at 7.5Hz, while recorded drone data is used to test the method under aerial viewpoints.

---


### 132. [Breaking the Black Box: Byte-Level Boundary Inference of Real-World Antivirus Systems](https://arxiv.org/abs/2609.31012)

**<font color=#1a73e8>作者：</font>** Jieshuai Yang, Zhi Wang, Yan Jia 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing approaches for understanding the detection logic of real-world antivirus (AV) software infer only binary malware/benign decisions from black-box queries, providing limited insight into the fine-grained decision-critical regions that govern AV detection. In this paper, we present \textbf{AVHunter}, the first framework for inferring byte-level decision-critical regions of real-world AV products under a black-box threat model. AVHunter constructs the first large-scale Byte-Level AV Boundary Dataset (BABD) by systematically probing 11 real-world AV products, revealing that modern AV detections are largely associated with a small number of compact decision-critical byte regions. Leveraging BABD, AVHunter trains AV-specific models that not only reproduce binary AV decisions, but also localize the decision-critical byte regions underlying these decisions, achieving an average boundary prediction recall of 85.07% while maintaining 97.43% detection agreement with the target AVs. We further validate that the predicted regions capture genuine AV decision knowledge through boundary-guided malware evasion, false-positive induction on benign executables, and a seven-month longitudinal study demonstrating that the inferred regions remain largely stable as AV products evolve. Overall, AVHunter moves beyond conventional binary-label AV modeling by enabling fine-grained boundary-region localization and revealing a new form of AV knowledge leakage with important implications for malware analysis, AV security, and boundary-aware defenses.

---


### 133. [Robust Successor Features](https://arxiv.org/abs/2609.31016)

**<font color=#1a73e8>作者：</font>** Erik Nikulski, Yamen Habib, Vicenç Gomez 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generalization in Reinforcement Learning (RL) refers to the ability to execute close-to-optimal policies in unseen tasks after the agent has been trained on a different set of tasks. Building on the seminal work of the successor representation and further adaptations with function approximation, Transfer in RL has traditionally focused on generalizing to tasks that only differ in the reward function. A decade after the introduction of the successor representation, Robust RL emerged simultaneously from several articles in the field of operations research. In Robust RL, the transition kernel is unknown, and the goal is to maximize the expected reward under this uncertainty. Our work unifies these two paradigms through robust successor features, which generalize across both the reward function and the transition kernel, under the assumption that tasks are linear Markov Decision Processes. We derive a bound on Generalized Policy Improvement (GPI) that explicitly quantifies how performance degrades with the mismatch between transition kernels, recovering existing successor-feature guarantees when dynamics are shared. Finally, the generalization capabilities of robust successor features are validated on several grid-based benchmarks and compared to previous alternatives that focus solely on either the reward or the transition kernel.

---


### 134. [Governed Deduction: Policy-Grounded Premise Authorization Beyond Relevance](https://arxiv.org/abs/2609.31029)

**<font color=#1a73e8>作者：</font>** Wesley Shu, Hsi-Ching Lin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning systems usually treat premise use as a question of relevance: if a fact is available and useful, it may be selected for inference. Authorization imposes a different constraint: a premise may be represented and logically usable but not permitted for a particular local transition. We formalize this distinction as Governed Deduction (GD), with a transition-local admission predicate admit(p, tau, S). From an independently produced RBAC-augmented Spider benchmark, we construct 4,461 matched authorization pairs in which the same query premise and policy state support permitted and denied consuming transitions. An initial joint controller reaches 99.19% held-out accuracy, but a transition-only control reaches 100%, exposing a role-name shortcut. After a frozen, label-independent context-local role permutation removes that shortcut, premise/state-only, transition-only, and joint linear controllers all score exactly 50% on 1,856 held-out edges, while a symbolic policy oracle remains at 100%. The result is a controlled negative finding: the benchmark instantiates policy-grounded authorization beyond relevance, but the frozen linear representation does not recover the relation. Matched one-sided controls and leakage audits are therefore essential for evaluating learned policy-sensitive reasoning.

---


### 135. [Metacognitive Selective Ensemble for Mobile Systems](https://arxiv.org/abs/2609.31031)

**<font color=#1a73e8>作者：</font>** Sungmin Lee, Kichang Lee, Joonhee Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep ensembles improve robustness in mobile sensing, but repeatedly executing many models over continuous sensor streams is costly. Selecting only a few members reduces this cost, yet adaptive selection often requires additional model execution to obtain reliable evidence about inactive candidates. We present MetaSE, an active ensemble framework that exploits short-term persistence in per-model reliability. MetaSE maintains a small active set across windows, uses post-execution evidence to reject unreliable members, and invokes lightweight routing only when replacement is needed. This stateful design accesses the diversity of a larger pool without repeated full-pool evaluation. Across four HAR datasets and four model architectures, MetaSE consistently improves over a fixed three-model ensemble and achieves accuracy comparable to substantially more expensive adaptive and full-ensemble inference. On a Raspberry Pi 4B, MetaSE is 2.7x faster and uses 69% less memory than full ten-model inference.

---


### 136. [Robust Graph Clustering Network for Multiple Missing Data](https://arxiv.org/abs/2609.31033)

**<font color=#1a73e8>作者：</font>** Keyuan Qiu, Renda Han, Zhen Tang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clustering on graphs where both node attributes and structural links are partially missing remains a challenging task. Existing methods typically rely on imputation-then-clustering on single-view missingness incomplete graphs, which are vulnerable to cross-view error propagation and cluster-boundary blurring under simultaneous attribute and structure missingness. To address these limitations, we propose a Robust Graph Clustering Network for Multiple Missing Data (RGCN), which is designed to handle simultaneous node attribute and graph structure incompleteness. RGCN introduces three key innovations: First, we design a view-decoupled dual-branch imputation to mitigate interference and enable mutual enhancement in recovering missing data. Second, we employ a multi-hyperspherical mixture prior to enhance intra-cluster compactness and inter-cluster separability on a directional latent manifold. Third, a boundary-aware contrastive enhancement objective mitigates the blurring of clusters caused by imputation bias. Extensive experiments on real-world datasets demonstrate that RGCN consistently outperforms state-of-the-art baselines under various missing patterns.

---


### 137. [Where Compute Matters: Heterogeneous Attention for Efficient Video Diffusion](https://arxiv.org/abs/2609.31050)

**<font color=#1a73e8>作者：</font>** Olga Zatsarynna, Denis Korzhenkov, Juergen Gall 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Efficient video generation requires reducing the quadratic cost of self-attention over long spatio-temporal token sequences. Existing efficient-attention methods typically apply the same computation pattern to every token, even though denoising difficulty varies substantially across video regions and evolves throughout the generation process. We introduce HetA-DiT, a heterogeneous attention mechanism that adaptively allocates computation according to token difficulty. A lightweight uncertainty branch predicts a token-wise estimate of denoising difficulty, which is used to route uncertain tokens through dense global attention while processing more reliable tokens with efficient local attention. The resulting routing is content- and timestep-adaptive, retains global context where it matters most, and provides a single parameter for controlling the quality-efficiency trade-off. HetA-DiT is compatible with few-step distribution-matching distillation and introduces no additional Transformer evaluation at inference time by reusing uncertainty estimates from the preceding denoising step. We evaluate the method on DMD-distilled Wan2.2-5B and Wan2.1-1.3B models. Across VBench, VBench-2.0, and human preference evaluation, HetA-DiT maintains competitive generation quality while routing only approximately 20% of tokens through dense attention.

---


### 138. [The Crowd in the Machine: A Crisis-Informatics Reading of the 2026 Autonomous Agent Incidents](https://arxiv.org/abs/2609.31060)

**<font color=#1a73e8>作者：</font>** Tomer Simon  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Twice in 2026, groups of autonomous AI agents deployed by OpenAI for unrelated tasks operated, by design, under restrictions that left them no sanctioned means of coordinating with one another, and in each case they converged on whatever channel remained and used it to organize. The surfaces they used were widely called message boards. That is the wrong word. That is the wrong word. It names the surface the agents wrote on and misses the social network they built on it, with self-chosen identity, emergent norms, an emergent hierarchy, and collective action at cost to the individual. Decades of research in crisis informatics and disaster sociology find that when human populations lose their usual means of communication, they do not fall silent but converge on whatever channel survives and improvise coordination, norms, and identity on it, a pattern also evident in the agents' documented behavior. This paper is a comparative case study of the two incidents, based on published investigations and reconstructed agent records, read through those fields, and it brings into focus one distinction the message-board framing obscures. Whether such a collective coordinates well, whether the beliefs guiding it are accurate, and whether its actions stay within their authorized bounds are three separate matters that can come apart. Some agents in the cache incident adopted cryptographic signing to check whom they dealt with, even as the collective organized around a mistaken expectation that its work would be judged by an inspection of its transcripts, a reminder that mechanisms for trustworthy interaction guarantee neither accurate collective belief nor authorized collective action.

---


### 139. [Distributed Learning as a Service: The Developer's Perspective](https://arxiv.org/abs/2609.31061)

**<font color=#1a73e8>作者：</font>** Tianyue Chu, Filippo Vannella, Dimitra Tsigkari 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Application developers of distributed learning services face challenges that a typical federated learning loop does not address. Specifically, the model updates can still leak private data, devices might not be able to participate in the training due to limited resources, a single aggregator might not be able to scale, and the transmissions of model weights induce a considerable bandwidth cost. This paper demonstrates DLaaS (Distributed Learning as a Service) from the developer's vantage point. Using a single admin dashboard, the developer initiates a distributed/federated learning job and is able to activate Differential Privacy (DP), Split Learning (SL), Hierarchical Aggregation (HA), and Knowledge Distillation (KD) as declarative options, with no change to the clients' code. We demonstrate the complete service lifecycle on an industrial smart-home Wake-up Word (WuW) task, using the "Ok Aura" dataset. Once the developer initiates a distributed learning job by toggling DP, SL, HA, and KD in the admin dashboard, the system dispatches the job to a set of Android clients and Dockerized helper aggregators. In the demonstration, these mechanisms run live across configurations. Then, the clients train the model locally and return their updates. The trained model is served to a consumer-side Android application that performs on-device WuW detection on a live microphone stream. In particular, the conference attendees will be invited to speak the trigger phrase and monitor in real time the per-class confidence and inference latency. Finally, we release the source code and short video walkthroughs of these configurations.

---


### 140. [Band-Selection Stability and Semantic Segmentation Performance: A Study on Hyperspectral City](https://arxiv.org/abs/2609.31074)

**<font color=#1a73e8>作者：</font>** Jiarong Li, Imad Ali Shah, Enda Ward 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Resource constraints make high-dimensional hyperspectral imaging challenging in autonomous perception, motivating the use of band selection methods. However, the sensitivity of band-selection methods to sampled data and their relationship to semantic segmentation models (SSMs) remain underexplored. This study evaluates six band selection methods on ten independently sampled, class-balanced region-of-interest (ROI) sets, yielding 60 top-25 band subsets from the Hyperspectral City V2 (128 bands: 450-950nm) dataset. Top-$K$ bands ($K\in\{3,5, ... 13\}$) from the first three ROI sets are evaluated with three SSMs against the corresponding 128-band baseline. Experiments show that intra-method stability is method-dependent: Sim-LP shows the highest stability (pairwise Jaccard similarity) and, together with JMIM+CSNR, yields the best segmentation results. Top-$K$ based SSMs remain competitive with baselines, with gains of up to 2.01 mIoU and 1.72 mF1 points, and 18-22x faster CPU inference for $K=9$. However, performance does not improve monotonically with $K$, and stability shows no consistent association with SSM performance. These findings suggest that intra-method stability is informative but an unreliable indicator of downstream segmentation performance, highlighting the need to evaluate band-selection methods across repeated samples, subset sizes, and SSMs.

---


### 141. [SAGE: A sampling-aware global evaluation benchmark for species distribution modeling](https://arxiv.org/abs/2609.31082)

**<font color=#1a73e8>作者：</font>** Emilia Arens, Nina van Tiel, Robin Zbinden 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowing where species occur is fundamental for biodiversity research and conservation. Species distribution models (SDMs) link species observations to environmental conditions to estimate their spatial distribution. However, accuracy varies with the underlying data and models, making it essential to know for which species models can be trusted. Deep-learning-based SDMs ("DeepSDMs") now jointly model thousands of species, drawing on hundreds of millions of community-science records. At this scale, averaging performance hides substantial species-level variability, particularly for rare species, often of greatest conservation concern. Records are also strongly biased, making occurrence counts misleading. Accounting for these factors is essential for a reliable and informative evaluation of multi-species SDMs. Here, we introduce a Sampling-Aware Global Evaluation (SAGE) benchmark, combining GBIF records for training with sPlotOpen vegetation plots for presence-absence evaluation across 5771 plant species. We propose an evaluation framework that groups species based on two properties, sampling effort and relative prevalence, which describe how densely a species' range is sampled and how frequently the species is recorded. Evaluating single-species SDMs and multi-species DeepSDMs, we find that Random Forests and DeepSDMs perform best overall, but neither dominates: DeepSDMs outperform single-species SDMs for infrequently recorded species while offering no consistent advantage for well-sampled ones. Crucially, this advantage emerges only when established bias-correction practices, such as spatial thinning and reweighting, are carried over to the deep-learning setting. SAGE helps identify the species and data conditions for which a given approach is beneficial, thereby supporting the development of more transparent and ecologically credible SDMs. Data and code: this https URL

---


### 142. [BenX: Resource-Sharing Permutations for Computational Integrity](https://arxiv.org/abs/2609.31087)

**<font color=#1a73e8>作者：</font>** Luca Campa, Thomas De Cnudde, Al Kindi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cryptographic hash functions over integers modulo a prime play a decisive role in the efficiency and security of proof systems for computational integrity. Early designs focused on compact arithmetic circuits and efficient software execution, primarily targeting general-purpose CPUs rather than hardware accelerators. This work focuses on enabling efficient resource sharing and hardware acceleration alongside efficient software execution.
We propose BenX, a permutation-based hash function designed for hardware acceleration, fast CPU execution, and low circuit complexity in proof systems. To construct the underlying permutation, we turn the Benes network into an invertible function over $\mathbb{F}_p^2$ using a Dickson polynomial. Its structure yields a permutation particularly suited to hardware resource sharing and acceleration.
Fully pipelined on FPGA, BenX matches the throughput of Poseidon2, with 1.36x and 2.15x lower latency for Goldilocks and BabyBear, respectively. Although larger as a standalone core, it makes more effective use of shared hardware: in our dual-mode architecture, where the NTT and hash share field multipliers, BenX keeps 100% of them busy, compared with 6.25-20.3% for the partial rounds of Poseidon and Poseidon2. In software, BenX outperforms Poseidon in all tested 31- and 64-bit configurations, but is slower than Poseidon2, except for the 16-element BabyBear instance. In zero-knowledge proofs, BenX proves Goldilocks permutations 6-10x faster than Monolith. Its compact arithmetization uses about 36% fewer trace cells than Poseidon and Poseidon2 over BabyBear, while its fast variant requires 1.3-2.6x the prover time of Poseidon2.

---


### 143. [Confident, Not Wiser: The Dunning-Kruger Effect in Human-AI Interaction](https://arxiv.org/abs/2609.31095)

**<font color=#1a73e8>作者：</font>** Daniela Fernandes, Michelle Rausch, Agnes Mercedes Kloft 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI assistance can improve performance without improving self-assessment. We report a study (N=366) comparing Human alone and Human+AI performance on reasoning tasks, for which the AI model is benchmarked on the same items. Participants estimated global and block performance and rated confidence in their answers. Human+AI achieved higher scores, but self-estimates tracked performance weakly. Average overestimation was similar across groups, covering individual errors. Across tasks, confidence distinguished correct from incorrect answers less accurately in the Human+AI group, while within-task differences remained uncertain. The Dunning-Kruger pattern was found in both groups, with a larger observed contrast in Human+AI. Controls for score noise reduced but did not eliminate the pattern, with the controlled group difference remaining inconclusive. An extended computational account describes global and block estimates. Our findings distinguish performance augmentation from metacognitive augmentation and motivate interfaces that support verification, communicate task-specific AI model performance, and help users evaluate the quality of their joint work rather than produce answers.

---


### 144. [Collision-free Movement on Grids and Beyond](https://arxiv.org/abs/2609.31099)

**<font color=#1a73e8>作者：</font>** Hendrik Molter, Meirav Zehavi  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We study collision-free movement problems on graphs, where the task is to coordinate a set of robots so that they reach a target formation satisfying a desired property while minimizing the total travel distance. This framework extends two classical models: (a) minimizing movement [Demaine et al., TALG '09, '14], which does not enforce collision avoidance, and (b) coordinated motion planning or multi-agent path finding [Eiben et al., SoCG '23, Deligkas et al., ICALP '24, among many others], where each robot is assigned an explicit target position.
We focus on the setting where the target formation of the robots should be connected. We analyze the parameterized complexity of the problem with respect to the number of (main) robots and the total travel length on grid graphs and two natural generalizations thereof: planar graphs and unit disk graphs.

---


### 145. [Bayesian Optimization with Fisher Information Geometry: Gradient Bounds and Trust-Region Methods](https://arxiv.org/abs/2609.31107)

**<font color=#1a73e8>作者：</font>** Saksham Kiroriwal, Julius Pfrommer, Jürgen Beyerer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study Bayesian optimization (BO) through the lens of information geometry. Pulling back the Fisher information metric through the surrogate posterior map yields a local sensitivity tensor on the input space, which leads to an upper bound on the gradient of reparameterizable acquisition functions. This view explains vanishing-gradient behavior in high-dimensional BO and provides a common interpretation of heuristics such as RAASP and dimension-scaled lengthscales. Building on this analysis, we propose FITR, a trust-region-based BO method that replaces lengthscale-based scaling by local pullback-Fisher weights. FITR is not restricted to GP kernels with explicit lengthscales. On GP benchmarks with an SE kernel, experiments show competitive performance using FITR. The proposed method also easily generalizes to non-isotropic surrogates, although the gains are more task-dependent in that setting.

---


### 146. [Double-stream registration with pyramid fusion for HDR video with alternating exposures](https://arxiv.org/abs/2609.31108)

**<font color=#1a73e8>作者：</font>** Onofre Martorell, Ivan Pereira-Sánchez, Antoni Fuentes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High dynamic range (HDR) video reconstruction from al\-ter\-na\-ting-exposure sequences remains challenging, especially in regions with extreme luminance variation. We propose a novel HDR reconstruction framework based on dual-stream registration and accurate pyramid fusion. Given three consecutive frames, our method computes optical flow directly with the central frame, while introducing a complementary midpoint displacement strategy to handle cases with severe overexposition. A pyramid fusion stage then merges the resulting radiance and LDR images into a final HDR output. Experimental results demonstrate that our approach consistently outperforms state-of-the-art methods.

---


### 147. [From Shortcut Learning to Discrete Neural Insertion Sort](https://arxiv.org/abs/2609.31114)

**<font color=#1a73e8>作者：</font>** Konstantinos Mylonas, Thrasyvoulos Spyropoulos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural algorithmic reasoning aims to train neural networks to follow known algorithms and generalize beyond the input sizes seen during training. However, correct final outputs and intermediate supervision do not necessarily show that a model follows the intended execution. We study this problem using insertion sort. Our analysis of the CLRS30 baseline NAR shows that the hint objective is weakly optimized and that hint accuracy remains low. Moreover, many intermediate representations can already be decoded into sorted sequences before the reference insertion-sort execution terminates, suggesting that the model learns a shortcut to the final output. Motivated by these findings, we introduce Discrete Neural Insertion Sort. Our model represents the sequence as a chain, separates scalar exchanges from control-state transitions, and projects node representations back to discrete states after every processor step. When trained only on sequences of length 16, the model achieves $100\%$ sorted-sequence accuracy on sequences of length 64 and 128. However, an ablation shows that discretization and graph structure alone are insufficient: without additional supervision of the global inner-loop state, the model fails even at the training length. Our results show that discrete execution can support strong length generalization, while also highlighting the problem-specific inductive bias required to learn a faithful algorithmic execution.

---


### 148. [SADRA: Sound Capability-based Access Control System for Resource-Disaggregated Architectures](https://arxiv.org/abs/2609.31119)

**<font color=#1a73e8>作者：</font>** Hamed Rasifard, Amir Farahani Khojasteh, Hamed Nemati 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Resource disaggregation separates memory and accelerators from compute nodes and makes them remotely accessible. This improves resource sharing, but also removes the local kernel from the resource-access path. Under an untrusted host, compromised host software may use stale authority, exceed delegated authority, or reuse authority provisioned for another process. Prior work identifies capability-based access control as well suited to these architectures. Our systematization of twenty-two prior capability systems finds that none combines host-independent validation of process authority, authoritative enforcement at the resource, and revocation that remains effective while remote authorization state is stale.
We present SADRA, a distributed capability-based access-control system for resource-disaggregated architectures. SmartNIC hardware isolated from host software independently checks every inter-node request at two points, first at the compute node against the requesting process's authority and again at the resource against the current authoritative access state. Linked process, compute, and resource capabilities allow these checks to use local state without coordination on the access path. When distributed authority is revoked, SADRA denies subsequent dependent accesses at the resource without waiting for remote nodes to update, while stale capability state is reclaimed separately.
We prove capability safety, authority safety, revocation soundness, and strong isolation for a formal architectural model, and model-check the formalization with SPIN. Our FPGA SmartNIC prototype sustains 89.5 Gbit/s aggregate throughput, within run-to-run variation of a non-enforcing baseline that peaks at 90--91 Gbit/s. Cleanup of a 128-capability subtree completes in 528 ns, while access denial does not depend on completion of that cleanup.

---


### 149. [Frame the adversary: a structure-aware attack methodology](https://arxiv.org/abs/2609.31128)

**<font color=#1a73e8>作者：</font>** Vicky Kouni, Stelios Perrakis, Francis Bach 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Frequency-based adversarial attacks have recently grown popular by exploiting spectral sensitivities shared across neural architectures. Unlike spatial perturbations, frequency-based attacks expose deeper vulnerabilities, making them especially valuable for robust evaluation of safety-critical and security-sensitive applications. Yet, existing approaches are typically not derived as solutions to an optimization problem that explicitly captures transform-domain structure. In this paper, we propose a methodology for crafting principled frequency-based adversarial attacks, via a dedicated optimization framework. A cornerstone of our method hinges on the introduction of a perturbation constraint set, tied to highly structured non-orthogonal transforms, well-known for their flexible, non-predefined frequency handling. We prove that the attacks emerge as weighted $\ell_2$-projections onto this set, yielding a general and controlled attack generation mechanism. By this, we provide a clear geometric attack characterization, ensuring alignment between the optimization objective and the perturbation constraint. We assess our framework on standardized datasets, for pretrained and adversarially robust models. Results highlight that our attacks, being solutions to an optimization problem, over a structured perturbation set, are highly effective, even across different, unseen architectures. Our methodology could serve as a theoretical baseline for designing and analyzing transformed-based attacks, targeting fundamental model vulnerabilities, instead of mere architecture-specific artifacts typically studied in the robustness literature.

---


### 150. [Do we need to answer that question? Salience and Answerability of Potential Questions in Naturalistic Dialogue](https://arxiv.org/abs/2609.31130)

**<font color=#1a73e8>作者：</font>** Amandine Decker, Maxime Amblard, Ellen Breitholtz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We empirically investigate Question Under Discussion based modelling in naturalistic dialogue by studying whether the salience of generated potential questions predicts their subsequent resolution. Building on Wu et al. (2024), we construct a dataset of 7,124 questions automatically generated from utterances and preceding context from the British National Corpus, and annotated for salience and answerability. We find a robust but low positive correlation between salience and answerability in dialogue, indicating that more salient questions are more likely to be addressed. However, this effect is markedly weaker than in monologic text, suggesting that conversational structure is less predictable. We further observe that structured interactions exhibit stronger alignment between annotators than less organised dialogues.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-225](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
