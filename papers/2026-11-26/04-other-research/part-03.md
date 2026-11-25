# 📦 其他研究 | 2026年11月26日

> 本类共 **342** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-342](./part-07.md)

---

### 101. [Multi Agent Reinforcement Learning enhanced Federated Learning for Predicting Remaining Useful Lifetime](https://arxiv.org/abs/2611.31880)

**<font color=#1a73e8>作者：</font>** Rajarshi Chattopadhyay, Chen-Khong Tham  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Remaining useful life (RUL) prediction is central to Prognostics and Health Management (PHM). The growth of industrial IoT has unlocked large multivariate sensor streams and enabled deep models - especially Transformers - for long-horizon sequence learning. However, transformers are parameter-heavy and data-hungry, while operational datasets are often siloed and privacy-sensitive. Federated Learning (FL) addresses this by training across clients without raw data sharing, but in practice many clients connect over lossy wireless links where UDP is preferred for low latency, making model exchange vulnerable to packet drops. We present a cooperative multi-agent reinforcement learning (MARL) framework that adapts FL to lossy channels by selecting per-client layer subsets to transmit and capping retransmissions. This framework is trained with QMIX value-function factorization for scalability. We instantiate the approach with a Graph Convolution Position-Aware Transformer (GCPATr) for RUL forecasting. On the CMAPSS dataset, our MARL-enhanced FL (RL-FL) consistently improves mean square error over standard FL, with the largest gains at high packet loss (e.g., up to 18% improvement on FD003 at 50% loss). These results show that MARL is an effective countermeasure to wireless degradation in FL-based RUL prediction.

---


### 102. [Rethinking Video Agents: When and Why Video Harnesses Work](https://arxiv.org/abs/2611.31883)

**<font color=#1a73e8>作者：</font>** Luoyuan Zhang, Xuanyu Zheng, Yancheng Long 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video understanding depends not only on how models reason about visual evidence, but also on which evidence they observe. Fixed observation policies determine this evidence in advance; agentic harnesses allow models to seek further observations as their understanding develops. This shift creates an opportunity to realize capabilities that fixed inputs leave untapped, yet the ability to request observations does not ensure their effective use. We investigate when and why video harnesses improve understanding, examining how task demands and models' capacity for interaction jointly shape their benefits. Using Video-Relook as an experimental framework, we let models adapt their temporal and spatial observations from a common default configuration, and analyze performance and interaction trajectories across models and tasks. Adaptive observation yields substantial gains on fine-grained action understanding, with benefits also extending to Video-MME-v2. Even under the same observation interface, gains differ substantially across models; interaction traces reveal corresponding differences in evidence seeking and the reliability of answer revision. The benefits also vary across tasks for the same model, ranging from substantial improvements to limited gains and regressions. Together, these findings support an account in which harness effectiveness depends on the alignment between opportunities for informative observation and the model's ability to turn interaction into reliable revisions. They motivate video harnesses that coordinate perception and reasoning, matching observational autonomy to task demands and model capabilities.

---


### 103. [HEAR, SEE, SPIKE ONCE: Highly Efficient NeuroAI Temporal Neural Networks for Low-Precision Multimodal Audio-Visual Classification and Online Learning](https://arxiv.org/abs/2611.31884)

**<font color=#1a73e8>作者：</font>** Shanmuga Venkatachalam, Quinn Jacobson, John Paul Shen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spiking neural networks for multimodal audio-visual classification reach high accuracy by adopting deep-learning machinery: multi-stage convolutional or transformer encoders trained end-to-end with surrogate-gradient backpropagation through time. These prior works typically rely on full-precision (32-bit) parameters and do not treat hardware efficiency as a primary design objective. In this paper, we propose NeuTNN-AV, a much simpler hardware-amenable multimodal substrate built on the recently proposed NeuroAI Temporal Neural Network (NeuTNN) and demonstrate that it can match or outperform state-of-the-art SNN baselines with a fraction of their synapse counts. NeuTNN neurons carry multiple active dendritic segments. Each input line spikes at most once (temporal coding) and every weight is learned via a local reward-modulated spike-timing dependent plasticity (STDP) rule. All weights are 4-bit integers and inference uses only comparisons and additions. On CREMA-D, it reaches 78.6% with 2.34M synapses establishing a new state-of-the-art SNN accuracy, against 77.14% for MISNet-XL (31M parameters). On UrbanSound8K-AV, NeuTNN reaches 98.82% with 1.38M synapses, against 96.85% for SMMT (9.99M parameters) and 98.96% for MISNet-XL (31M parameters). Weight memory is 23-106x smaller than the spiking baselines, and the measured synaptic energy per inference is two to three orders of magnitude lower. Furthermore, the proposed NeuTNN learns CREMA-D in a single pass with 73.8% accuracy and demonstrates rapid online continual learning by adapting to unseen actors from a few dozen clips.

---


### 104. [Cheap Memory Costs Future Compute: Co-Designing Persistent KV and GPU Execution for Efficient Streaming Video Diffusion](https://arxiv.org/abs/2611.31892)

**<font color=#1a73e8>作者：</font>** Jian Yang, Zhizhuo Kou, Qiyuan Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Block-causal video diffusion generates long videos block by block, conditioned on a persistent key-value (KV) cache. After each block is denoised, an extra noise-free ($t=0$) forward pass writes its clean KV into the cache; once distillation and speculative early exit make denoising cheap, this clean KV update dominates the runtime. Reusing stale KV shortens the update, but stale memory corrupts the conditioning of later blocks and inflates their denoising steps, so the saved compute reappears downstream. We present SAMR (Step-Aware Memory Reconstruction), a training-free method for frozen causal video DiTs that refreshes only part of the cache and reconstructs the rest without DiT forwards. Our key observation is that, once rotary position phases are removed, motion-aligned historical KV and the in-flight KV a token holds at its exit step are complementary estimates of its clean KV. SAMR debiases in-flight KV with offline-calibrated per-head affine maps in Pre-RoPE space, fuses the two estimates, and reserves true $t=0$ refreshes for tokens flagged by an attention-readout error proxy, all executed by tile-aligned, synchronization-free Triton kernels. On 48-second LongLive-1.3B videos, SAMR reduces DiT latency by 20.9% and principal FLOPs by 30.7% relative to dense KV updates, lowers downstream denoising steps, and improves final-quarter PSNR over token reuse by 1.61 dB (1.14 dB on held-out VidProM-16). The reconstruction also transfers to frozen Self-Forcing-DMD-1.3B: zero-shot, it reduces reuse-induced step inflation ($2.47 \to 2.30$ steps/token) and improves late PSNR by $+0.33$ dB, and a one-time training-free calibration recovers the diagnostic score that zero-shot transfer lowers ($89.62 \to 91.10$).

---


### 105. [Beyond Average Gains: Probing the Equity--Vulnerability Tension in Structured Visual AI for Learning](https://arxiv.org/abs/2611.31899)

**<font color=#1a73e8>作者：</font>** Mingyuan Li, Duan Wang, Erick Purwanto 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Open-ended conversational AI requires learners to formulate questions, organize learning paths, and track changing problem states. Structured visual interfaces may ease these demands, but higher average ratings do not establish that support is experienced consistently across learner backgrounds and devices. We conducted a randomized study of graph-algorithm learning, comparing VisualCodeChat (VCC), which combines predefined learning stages, conversational explanations, and dynamic algorithm visualizations, with a standard text-based chatbot. We analyzed 282 post-task questionnaires from university students. In unadjusted comparisons, VCC received significantly higher usability and perceived effectiveness ratings. We detected no significant between-condition differences in efficiency, satisfaction, or post-use emotion. Exploratory within-condition analyses identified differences associated with prior chatbot experience: infrequent users reported lower adoption and learning-management ratings in the standard AI condition, while uncomfortable prior chatbot experiences were associated with lower interaction and layout ratings in the VCC condition. These findings suggest that improving the average interaction experience is only part of making AI-supported learning inclusive. Future evaluations should examine whether learners with different prior experiences can obtain guidance, recover from difficulties, and demonstrate understanding independently across devices.

---


### 106. [MIFLOW: Dynamic Recent-Behavior Priors for Reference-Calibrated Online Flow-Policy Reinforcement Learning](https://arxiv.org/abs/2611.31902)

**<font color=#1a73e8>作者：</font>** Chenhao Wang, Haonan Ma, Wenjie Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow-based policies provide expressive action distributions for continuous-control reinforcement learning. In online actor-critic learning, off-policy value estimates can be unreliable in poorly covered action regions, where expressive policies may shift probability mass toward critic-favored actions. We propose MIFLOW, which calibrates online flow-policy learning with a recency-adaptive flow-matching prior fitted to recently executed actions. Inspired by canalization as a qualitative analogy for path-dependent stabilization, we use the prior as a moving density reference for value-guided policy improvement. MIFLOW uses the approximate recent-action log-density in a dimension-normalized correction to both actor updates and critic targets. This correction increases the cost of low-density actions while keeping them available. Across six MuJoCo continuous-control tasks and five random seeds, MIFLOW achieves competitive mean return curves and higher late-training mean returns than the evaluated baselines on several tasks. In a Walker2d-v4 case study, MIFLOW shows a lower proportion of actions assigned low density by the learned reference, both overall and among high-Q actions. Prior-family and prior-buffer comparisons show task-dependent differences in returns and prior-defined diagnostics. These results support dynamic recent-behavior priors for reference calibration in the evaluated settings. The diagnostics measure how sampled actions align with the learned reference. True action support and critic extrapolation error remain unmeasured in these experiments.

---


### 107. [OrangeTree: A Linear and Tree-based Time Series Forecasting Model Supporting Multiple Input and Output Lengths](https://arxiv.org/abs/2611.31905)

**<font color=#1a73e8>作者：</font>** Yiqi Tang, Zhichen Lai, Yuxuan Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series forecasting (TSF) models suffer from a critical rigidity: the inability to handle Multiple Input and Output Lengths (MIOL) within a single architecture. Current workarounds, such as padding or autoregression, often incur computational redundancy or suffer from error accumulation. We propose OrangeTree, a linear and tree-based architecture that decouples model parameters from sequence lengths. It employs a Segment Tree Encoder and an Inverse Tree Decoder to translate multi-length input history into multi-length output predictions within a unified framework. Crucially, a Range Weighter and a Feature Fuser bridge these components, dynamically selecting and fusing relevant ranges into optimal contexts for forecasting. Experiments on six benchmarks confirm OrangeTree achieves the SOTA performance. In MIOL settings, it matches the accuracy of length-fixed models without substantial accuracy degradation or a substantial increase in inference latency typical of heuristic methods. Code is available at this https URL.

---


### 108. [TQ-HQNet: A Trainability-Aware and Qubit-Efficient Hybrid Quantum Neural Network for Cross-Domain Learning on Heterogeneous Data](https://arxiv.org/abs/2611.31908)

**<font color=#1a73e8>作者：</font>** Abdur Rasool, Saba Aslam, Hui Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid quantum neural networks are a promising direction for noisy intermediate-scale quantum computing, but their practical effectiveness is often limited by poor trainability, rigid circuit design, and weak robustness across heterogeneous real-world tasks. This paper proposes TQ-HQNet, a Trainability-Aware and Qubit-Efficient Hybrid Quantum Neural Network for cross-domain learning on heterogeneous data. The proposed framework combines three mechanisms: 1) adaptive latent compression to map domain-specific features into qubit-compatible representations, 2) trainability-aware search over compact variational circuit candidates, and 3) hybrid fusion of multiple shallow quantum experts to improve robustness without increasing qubit cost excessively. TQ-HQNet is evaluated on four public datasets spanning neurological screening, phishing detection, financial direction prediction, and DNA sequence classification. Across all domains, the proposed model consistently improves over a fixed hybrid quantum baseline, with balanced-accuracy gains of +0.280, +0.170, +0.071, and +0.060, respectively. Ablation and sensitivity studies confirm that gains arise from trainability-aware compact circuit selection and expert fusion, not circuit scaling. Although classical baselines outperform on some tasks, fixed-split results show consistent improvements over the fixed hybrid reference. These analyses support the practical role of compact selection and fusion, with repeated-split and hardware-aware studies left for future work.

---


### 109. [ReJEPA: Bounded Predictive Regulation for Latent World Models](https://arxiv.org/abs/2611.31910)

**<font color=#1a73e8>作者：</font>** Fangzhou Lin, Yuping Wang, Shuo Xing 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent world models learn representations by predicting future states in an abstract embedding space rather than reconstructing raw pixels. When training across multi-frame sequences, however, not all frames and spatial regions are equally informative or predictable. We argue that forcing a world model to minimize every prediction error may be unnecessary and harmful. Under standard $L_2$ loss, unbounded gradients force the encoder and predictor to overfit noisy or transient frames at the expense of core physical structure, while amplifying gradient conflict with representation regularizers. Conversely, $L_1$ loss bounds large gradients, but its constant gradient magnitude near zero disrupts the local smoothness required for planning. We resolve this tension with \textbf{ReJEPA}, a bounded predictive regulation principle that combines bounded gradients for large errors with smooth quadratic behavior near zero, instantiated simply via the element-wise $\log\cosh$ loss.
As a drop-in training replacement across Temporal Straightening, LeWorldModel, and V-JEPA~2.1, $\log\cosh$ consistently outperforms $L_2$, a curvature-matched quadratic control, $L_1$, and Smooth-$L_1$ baselines without altering architectures or inference procedures. Notably, the gains grow with environmental complexity, scaling from simple navigation to contact-rich manipulation and real-world autonomous driving on NAVSIM. Probing and geometric analyses confirm that relaxing the penalty on extreme errors yields representations that better capture physical states and align with the true planning cost landscape.

---


### 110. [Meta-Amortized Cognitive Modeling](https://arxiv.org/abs/2611.31914)

**<font color=#1a73e8>作者：</font>** Jerry M. Huang, Lukas Schumacher, Niek Stevenson 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cognitive modeling is highly iterative. Researchers repeatedly revise model structures, parameterizations, covariates, and experimental designs as theories evolve and data accumulates. Amortized Bayesian inference with neural networks provides rapid estimation for individual models, but every revision requires new simulations and training. Here, we introduce CogFormerV2, a meta-amortized framework that enables researchers to specify, revise, and fit cognitive models with a single network, carrying amortization across an entire space of models all at once. Trained once in about a day on a single GPU, it delivers accurate, well-calibrated posteriors across more than 14.6 billion model configurations spanning binary, multi-alternative, and continuous decisions, with varying parameter sets, covariate structures, trial counts, and contamination levels. It can fit empirical data from distinct behavioral tasks and extends to new models through continual learning and representation transfer. Released as an open-source interactive application, CogFormerV2 provides a reusable infrastructure for meta-amortized inference in cognitive modeling, while carrying the potential to accelerate computational modeling workflows at large.

---


### 111. [HiGS: A Hierarchical Architecture for Fast Differentiable 3D Gaussian Splatting](https://arxiv.org/abs/2611.31918)

**<font color=#1a73e8>作者：</font>** Dawid Pająk, Martin Bisson, Rodolfo Lima 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) makes one screen tile the cell of partitioning, the cell of rasterization, and the unit of parallel work. Partitioning favors large tiles and rasterization small ones, and with one unit per tile the densest tiles set the frame time. We present Hierarchically Tiled Gaussian Splatting (HiGS), a unified architecture for rendering and reconstruction that gives each role its own granularity: Gaussians are partitioned over coarse macro-tiles, rasterized over the fine render tiles within them, and processed in bounded depth-sorted batches. A dense region issues more batches instead of one longer unit, so frame time follows the work in a view rather than its densest tile. The same batches carry reconstruction: compositing supplies the transmittance and color needed to differentiate each one independently, leaving optimizer memory traffic as the dominant training cost. We fuse the optimizer into the backward pass, halve the parameters and moments it stores and updates directly, and defer appearance updates outside the view. HiGS renders scenes faster than every published method we evaluate, by the widest margin on views with uneven load, and reconstructs them faster and in less memory, at equal image quality and with exact front-to-back alpha compositing.

---


### 112. [TANDEM: Temporal Anchor Densification With Reliability-Aware Memory for Lightweight Sparse Depth Completion in Endoscopic Robotic Navigation](https://arxiv.org/abs/2611.31922)

**<font color=#1a73e8>作者：</font>** Weikuan Qiu, Jiale Hou, Chongzhao Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> For endoscopic robotic surgery, accurate dense depth perception serves as a foundational capability, which enables navigation, instrument localization, and tissue interaction. However, endoscopic video lacks reliable metric depth, while metric measurements obtained via tracking, time-of-flight sensing, or instrument contact only cover a small fraction of pixels in each frame, rendering sparse depth completion an urgent and unsolved challenge. In this work, we propose Temporal Anchor Densification with Reliability-Aware Memory (TANDEM), a causal sparse depth completion framework for endoscopic video. It adopts a lightweight design and leverages the video stream: past measurements re-projected into the current view recover the metric evidence unavailable within a single sparse frame. To keep this evidence interpretable, accurate, and efficient, an explicit memory scores each re-projected measurement with analytic re-observation, age, and motion-parallax factors without overriding current measurements. A compact network then reconstructs depth via reliability-weighted gradient integration and a frequency-gated reference prior. We evaluate TANDEM on the C3VD colonoscopy and StereoMIS laparoscopy datasets. With only 5.58 M parameters, TANDEM reduces the root mean square error by 11.7% and 32.0%, respectively, compared with the strongest baseline, and achieves state-of-the-art accuracy. It also remains accurate under pose errors of the magnitude reported for endoscopic pose estimation. Code will be released at this https URL upon acceptance.

---


### 113. [MALET & Katalina: A Large-Scale Dataset and Static Analysis of macOS Malware](https://arxiv.org/abs/2611.31949)

**<font color=#1a73e8>作者：</font>** Godwin Attigah, Obinna Igbe  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> While malware on platforms such as Windows and Android has been extensively studied, the macOS ecosystem remains comparatively understudied. To address this gap, we present MALET, a large-scale public dataset for macOS malware analysis. MALET contains 44{,}804 malicious Mach-O binaries and 44{,}457 samples with zero antivirus detections on VirusTotal. From the undetected set, we further identify 25{,}835 high-confidence benign samples using conservative, heuristic-based filtering. We also introduce Katalina, an open-source static analysis framework that extracts macOS-specific structural features and indicators of potential behavior at scale.
Using MALET, we perform, to the best of our knowledge, the first large-scale static characterization of macOS malware. Our analysis reveals macOS-specific traits, including widespread misuse of security entitlements, abuse of native scripting interfaces, and irregularities in code-signing infrastructure. We find that 93.0\% of malicious samples are unsigned, demonstrating that unsigned code continues to execute in practice through user-mediated approval mechanisms. Among CA-signed malware, 28.4\% (816 samples) were associated with certificates that were later revoked, including samples publicly attributed to DPRK-linked threat actors, as reflected in antivirus labels and threat intelligence reports. Finally, we identify significant detection instability: in 185 structurally identical malicious samples, antivirus engines failed to provide consistent detections for 77.2\% (143 samples). Together, these results highlight persistent blind spots in macOS malware detection and motivate improved approaches to certificate abuse analysis, similarity-based clustering, and platform-specific defense mechanisms. Based on these insights, we outline concrete steps to advance the state of macOS malware analysis and defense.

---


### 114. [Beyond Rigid Hands: Deforming Skin into Contact-Consistent Hand Meshes](https://arxiv.org/abs/2611.31950)

**<font color=#1a73e8>作者：</font>** Seonghwan Park, Min-Gyu Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hands grasp objects with soft skin. A fingertip flattens against a mug, and a palm curves around a bottle. Yet hand-object datasets and estimators represent the hand as a rigid articulated mesh, which hovers above or penetrates the object where skin would press against it. Existing refiners keep the mesh rigid and adjust only the pose, trading pose accuracy for physical plausibility. We ask whether a rigid hand can instead touch the object as skin does while staying close to its original pose. We lift annotated or estimated rigid hands to contact-consistent meshes through an optimization that (i) slightly adjusts the joints and wrist to bring the fingers onto the object, (ii) deforms the skin so that penetrating regions settle onto the surface, and (iii) keeps this deformation consistent over time. Since deformation reaches only skin already near the object, we further train a lightweight head on the lifted annotations to predict where an estimated hand should touch and steer the deformation there. Unlike existing refiners, the lift more than doubles the skin lying on the object surface for three published estimators while barely changing the pose. Guidance from the learned head further improves grasp stability by closing contact gaps that the estimate leaves open. Existing hand-object datasets and estimators can thus adopt contact-consistent hands without changing the hand model or retraining the estimators.

---


### 115. [TACTUS: Unifying Surgical Action Understanding in Time and Space](https://arxiv.org/abs/2611.31956)

**<font color=#1a73e8>作者：</font>** Lurui Wang, Hao Ding, Chenhao Yu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Advancing surgical automation requires a comprehensive spatio-temporal understanding of how instruments act on tissue throughout an action. Existing surgical benchmarks, however, largely define supervision through task-specific targets, leaving the relationships between action semantics, instrument motion, and tissue interaction incompletely specified. To address this limitation, we introduce TACTUS (Tool, Action, Contact and Trajectory Understanding in Surgery), a new dataset and benchmark that establishes a unified annotation framework for complete surgical actions. The framework jointly specifies tool and action identities, nested action and interaction windows, instrument-specific landmark trajectories, and tissue-region tracks. To construct these annotations at scale, we develop a two-tier pipeline combining human annotation, point tracking, and model-generated spatial prompts. Using this pipeline, we re-annotate 141 videos from five public sources, producing 22,995 action clips spanning 2.9 million frames. The dataset comprises 15,668 Gold clips with human spatial prompts followed by review and re-checking, and 7,327 Silver clips combining human semantic and temporal annotations with model-generated spatial prompts. We further introduce TactusNet, the companion reference network, to benchmark semantic, temporal, and spatial prediction from shared video features. Across TactusNet and 13 published baselines, tool-action accuracy reaches 95.8% with per-head encoder fine-tuning, while the best temporal recall and contact Dice reach 46.6% at temporal IoU 0.7 and 0.351, respectively. Moreover, adding Silver improves the default TactusNet's pair accuracy from 93.8% to 95.5%. Together, these contributions establish a foundation for learning and evaluating the instrument-tissue interactions underlying future surgical automation.

---


### 116. [SPAR: Self-Referenced World-Model Rewards for Physical Alignment in Video Generation](https://arxiv.org/abs/2611.31958)

**<font color=#1a73e8>作者：</font>** Junyi Zhang, Qichao Wang, Wenzhe Qian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating videos with physically plausible dynamics remains challenging despite advances in visual quality. Latent world models offer predictive signals for evaluating physical plausibility, but higher agreement between predicted and observed features may reflect easier-to-predict scene content rather than more plausible dynamics. We propose \textbf{S}elf-Referenced \textbf{P}hysical \textbf{A}lignment \textbf{R}ewards (\textbf{SPAR}), a framework that uses world-model predictions for inference-time physical alignment. SPAR compares each video's prediction error with that of static clips constructed by repeating its own frames, providing a content-matched reference for evaluating generated dynamics. To account for the uneven spatial and temporal distribution of physical interactions, we introduce a unified \textbf{spatiotemporal reward refinement} strategy. \textbf{Spatial refinement} emphasizes localized prediction discrepancies, while \textbf{temporal refinement} moderates brief error peaks and supplements prediction errors with agreement between predicted and observed feature changes. Evaluations across multiple benchmarks demonstrate that SPAR improves the physical plausibility of both \textbf{text-to-video generation} and \textbf{image-to-video continuation}, bringing generated dynamics into closer alignment with the physical regularities governing real-world events. Additional results and resources are available at this https URL

---


### 117. [Are Web Agents Still Detectable? Stress-Testing Bot Defenses with Coordinated Evasion](https://arxiv.org/abs/2611.31962)

**<font color=#1a73e8>作者：</font>** Parsa Nilforushan, Gemmin Sugiura, Kourosh Hashemi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI web agents can autonomously navigate websites and complete various tasks. As their capabilities and adoption expand, evaluating bot defenses requires adversarial stress tests. Although prior work demonstrates that existing agents can remain detectable, it remains unclear how effective bot defenses are against adversaries that coordinate evasion across browser fingerprints, automation controls, and interaction behavior. To investigate this threat, we introduce DarkAgent, an autonomous web agent that combines a forked Chromium browser that conceals automation artifacts and generative models that produce human-like mouse and keyboard traces. To address the limitations of existing keyboard mimickers, our keyboard model jointly generates realistic key events and their timings while reliably reproducing the target text. Released agent detectors accept our generated behavior as human, and trained classifiers find it substantially harder to distinguish from human traces than existing mimickers. DarkAgent achieves an 89% page-access bypass rate across a third-party stealth benchmark, exceeding the strongest published baseline by 12 percentage points. To further enhance the measurement of agents, we introduce a benchmark that measures browser fingerprints, interaction behavior, and network activity to assess each channel's contribution to detecting adversarial agents such as DarkAgent. On this benchmark, browser and behavioral modifications are complementary: either alone remains detectable, and only their combination evades all tested checks. Together, our findings expose the gap between passing existing bot defenses and reproducing human behavior, and point to timing between actions as a remaining signal for defenders.

---


### 118. [Sounding the Black Box: Online Training of Embedded Neural Networks in Forward-Only Physical Simulators](https://arxiv.org/abs/2611.31964)

**<font color=#1a73e8>作者：</font>** Ruiqi Shu, Tianrun Gao, Haomin Wen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid physics-neural simulators embed neural networks in partial differential equation (PDE) solvers to model unresolved subgrid dynamics while preserving resolved physics and conservation laws. Because closure outputs feed back across time steps, single-step offline regression does not directly minimize multi-step rollout error, motivating online trajectory optimization. Solver backpropagation through time (BPTT) is the standard online solution when solver derivatives are available, yet many operational Fortran and C/C++ simulators expose only non-differentiable, forward-only interfaces. We introduce FORGE (Forward-Only Response and Gauss-Newton Estimation), an online framework that trains embedded networks from forward runs alone by decoupling exact network derivatives from black-box simulator dynamics. Stage I warms up the rollout via a low-dimensional Gauss-Newton step along output-orthonormal weight directions, canceling multi-layer feature drift via a final-layer correction. Stage II perturbs spatial output fields to fit a gain-bounded causal linear response operator across rollout steps, solves for regularized target outputs, and updates all weights via network backpropagation. Across five 2D and 3D benchmarks spanning phase separation, reaction-diffusion, fluid and MHD turbulence, and ocean circulation, FORGE outperforms gradient-free, reinforcement-learning, and emulator-based baselines, cutting coarse-solver test mean squared error (MSE) by 50%-96% in 2D and 70% in 3D, outperforming the strongest forward-only baseline by 16%-69%, and recovering 88%-98% of Solver BPTT's gains. Code is available at this https URL.

---


### 119. [On the Information Loss of Multi-Token Prediction: Origin and Solution](https://arxiv.org/abs/2611.31966)

**<font color=#1a73e8>作者：</font>** Tangyu Jiang, Zhanke Zhou, Haodi Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-token prediction (MTP) accelerates autoregressive decoding through block-wise prediction, but remains vulnerable to error accumulation across sequentially generated blocks. To investigate this limitation, we analyze the distinction between block-wise and sequence-level cumulative information loss (CIL). Specifically, when the model generates using its own previous outputs without access to reference answers, the input-conditional gap equals the cross-block dependence of the reference targets. To improve prediction when these generated prefixes are imperfect, we propose Dual-MTP, which supervises shared prediction heads under full and randomly masked contexts. Together, complete-prefix supervision and context perturbations provide complementary training signals while retaining the MTP architecture. To characterize this training objective, we use the normalized dual loss to bound the divergence between the model's predictive distributions under full and masked contexts. Experiments across five backbones and six tasks spanning mathematical reasoning and GLUE understanding show that Dual-MTP achieves the highest average task score on four of five backbones, with gains of up to 2.46 points over MTP. On mathematical reasoning tasks, Dual-MTP also achieves 1.4 to 1.9 times the decoding throughput of the NTP reference. Together, these results show that dual-context supervision can improve prediction accuracy while retaining efficient multi-token decoding.

---


### 120. [Predict Backbone, Graft Dynamics: A Decoupled Paradigm for Time Series Forecasting](https://arxiv.org/abs/2611.31970)

**<font color=#1a73e8>作者：</font>** Lin Zhang, Zilin Li, Jingmei Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern long-term forecasters are typically optimized for point-wise accuracy, which rewards dominant low-frequency backbones but often suppresses high-utility local dynamics such as abrupt variations, transient surges, and turning points. We propose Predict Backbone, Graft Dynamics, a decoupled forecasting paradigm that separates stable structural prediction from grounded dynamic restoration. We instantiate it as GRAFT, where a base forecaster predicts the reliable trajectory backbone, and a dedicated grafting path restores historically recurrent dynamics through retrieval-based evidence, phase-aware release, channel-wise control, and restoration-cooperative optimization. Unlike generic post-hoc revision methods that correct residual errors, GRAFT formulates the second stage as grounded dynamic grafting, where historical response evidence is calibrated into transferable dynamics and selectively grafted onto the backbone under phase-, channel-, and confidence-aware constraints. Across the full evaluation grid of seven benchmarks, two metrics, four horizons, and six backbones, GRAFT improves over the corresponding backbone in 87% of all comparisons, with average MSE/MAE reductions of 4.6%/3.9%. Dynamic-window analyses show that GRAFT restores local dynamics while preserving the stable backbone structure. These results suggest a new principle for high-utility forecasting: predict the backbone, then graft the dynamics.

---


### 121. [Localizing Cross-Lingual Generalization in Parameter Space](https://arxiv.org/abs/2611.31975)

**<font color=#1a73e8>作者：</font>** Yeoreum Lee, Jaeseong Lee, Seung-won Hwang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-lingual transfer is uneven across tasks, succeeding for natural language understanding but often failing for mathematical reasoning. We argue that this asymmetry is governed by the geometry of parameter space. Specifically, cross-lingual generalization is determined by whether English and target-language LoRA adapters share a low-error basin. To test this, we use linear mode connectivity (LMC) between English and target-language adapters, evaluating on three tasks. We find that NLI and QA model-language pairs are mostly linearly connected, whereas mathematical reasoning (Math) pairs are not, indicating that basin geometry is task-dependent. Such disconnection in Math is ``local'' rather than global. A small target-language task sample, applied only to the English adapter's language encoding or semantic composition layers, is enough to repair it. Cross-lingual generalization is also factorizable into language-specific encoding and language-agnostic composition, each supplied separately from a cheaper signal. English task data routed to the composition layers and an unlabeled target-language corpus routed to the language encoding layers each alleviate it on their own for nearly every pair. Composition is the more influential of these, and it needs no target-language data. Together, these results suggest that cross-lingual generalization decomposes into language-specific and language-agnostic components in parameter space. This decomposition offers a practical route for low-resource cross-lingual adaptation.

---


### 122. [Distill to Loop: Turning Pretrained Diffusion Transformers into Looped Models with Adjustable Depth](https://arxiv.org/abs/2611.31977)

**<font color=#1a73e8>作者：</font>** Chenru Wang, Shengwei An  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Looped transformers reuse one block of shared weights along the depth of the network. Recent looped diffusion transformers are trained from scratch, which repeats the full pretraining cost although strong pretrained non-looped diffusion transformers exist. We propose Distill to Loop (Dooop), which distills a pretrained non-looped diffusion transformer into a looped student whose blocks are initialized from the teacher's. We cast distillation as a fixed-point iteration toward the teacher, in which the output after every loop is trained toward the teacher, and each loop is one step of an ordinary differential equation in depth. As a result, one model runs any number of loops at test time without retraining, and the higher-order ODE solvers of diffusion model sampling can be applied along the depth dimension for better results. Meanwhile, because a looped model produces an output after every loop, we also construct loop guidance between the outputs of different loop counts, which improves the generated samples at little extra compute. On SD3-medium, a looped student with about 37% of the teacher's parameters matches the teacher on average over GenEval, ImageReward, PickScore and HPSv2.1 with two to four loops, and with two loops it uses about 58% of the teacher's compute. And on a four-step SD3-medium, loop guidance raises the average of the four metrics from 88.2 to 99.2.

---


### 123. [WaveSR: Physics-Inspired Wave Evolution Attention for Efficient Image Super-Resolution](https://arxiv.org/abs/2611.31984)

**<font color=#1a73e8>作者：</font>** Xiaoyan Lei, Biao Luo, Wenlong Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, physics-inspired neural networks have gained widespread attention due to their interpretability. The closed-form, frequency-time decoupled solution of the wave equation offers linear complexity and allows different frequency components to evolve independently, making it a potential alternative solution for efficient image super-resolution. Therefore, a physics-inspired wave evolution attention framework is proposed, namely WaveSR. The WaveSR framework involves two key modules, i.e., wave evolution attention (WEA) and Frequency-Adaptive Feed-Forward Network (FA-FFN). The WEA module achieves feature interactions through the analytical solution of the 2D wave equation in the Fast Fourier Transform (FFT) domain, enabling independent evolution of different frequency components with learnable wave speed \(c\) and damping coefficient \(\alpha\). The FA-FFN module realizes adaptive frequency feature selection through learnable spectral modulation, effectively enhancing feature representation capability. Subsequently, we employ a two-stage training strategy with a hybrid objective that combines a spatial-domain pixel loss and a frequency-domain loss to improve reconstruction quality. Our method provides a preliminary exploration of physics-inspired neural networks for efficient image super-resolution.

---


### 124. [Reconstructing Natural Images from Brain Activity during Natural Vision](https://arxiv.org/abs/2611.31989)

**<font color=#1a73e8>作者：</font>** Tejasvi Kothapalli, Ryan Ressmeyer, Declan Rowley 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing images from brain activity has two broad goals. The first is to build brain-computer interfaces. The second is to understand how the brain sees. The eyes deliver incomplete, noisy input, so the brain must fill in the gaps with its expectations of what natural scenes look like. This filling-in relies on the brain's prior over natural images. Image reconstruction lets us test which natural image prior best matches the brain's natural image prior. However, most previous work on image reconstruction relies on an unnatural condition: subjects must hold their eyes still. In reality, primates constantly move their eyes to see the world. We introduce a framework for reconstructing images from neural activity while a primate freely views a static natural scene. We record from five monkeys with high-density electrode arrays in the lateral geniculate nucleus (LGN) and primary visual cortex (V1). The recorded receptive fields cover only a small part of the image. Thus, we combine neural activity across eye movements, trials, and sessions to reconstruct the full image. We first present a simple linear method with a 1/f prior. We then scale this approach up with modern deep learning. We train a decoder by tokenizing spiking activity and measured gaze; these tokens are fed into a transformer and diffusion model to reconstruct the full scene. Three factors determine reconstruction quality: the amount of neural evidence combined over viewing time, the accuracy of eye tracking, and the choice of image prior. Our method sets a new state-of-the-art performance in reconstructing natural images from brain activity, across brain recording modalities: fMRI, EEG, MEG and electrophysiology.

---


### 125. [Metric-Dependent Scaling Laws for Sketched Multiclass Softmax Regression](https://arxiv.org/abs/2611.31995)

**<font color=#1a73e8>作者：</font>** Ziyan Chen, Linhe Zheng, Peilin Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study scaling laws for full-batch gradient descent with general stable deterministic learning rates in sketched multiclass softmax regression. In a Gaussian teacher student model with power law feature and teacher spectra, the student observes a random feature sketch and reuses a finite labeled sample throughout optimization. Sketching generally makes the student misspecified, so the analysis must jointly account for approximation, nonlinear finite time learning, and the fixed empirical perturbation induced by data reuse. On an exponentially likely sketch event, we show that cross entropy excess and excess zero one risk share a common spectral scale, consisting of a resolution term and an effective learned dimension divided by sample size; teacher student decision disagreement follows the square root of that scale. The resulting balance gives rate optimal sketch and cumulative horizon choices, and synthetic experiments support the predicted regimes and metric dependent exponents.

---


### 126. [ADE: A Zero-Training Unlearning Method for Latent World Models](https://arxiv.org/abs/2611.31998)

**<font color=#1a73e8>作者：</font>** Sirui He, Chi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent world models learn compact recurrent dynamics from offline trajectories, yet deployed simulators can retain backdoor triggers or stale transitions from outdated physical regimes. Existing unlearning methods fail in autoregressive physics: gradient updates distort latent manifolds and compound rollout drift, naive output zeroing suppresses valid control responses on trigger onset, and single-step deletion leaves corruption inside recurrent hidden states. We propose Analytical Dynamics Excision (ADE), a deterministic, zero-training closed-form unlearning algorithm for latent world models. Using only cached pretraining moments, ADE recovers retain covariances via single-pass matrix downdating without raw retain data and cascades closed-form edits across the input bottleneck, hidden states, and downstream heads. Pairing orthogonal excision with whitened recurrent damping and mean-preserving affine calibration neutralizes out-of-manifold backdoors and realigns in-manifold shifts without variance collapse. Across four regimes on three MuJoCo benchmarks, ADE outperforms seven tuned baselines on DreamerV1, eliminating HalfCheetah and Hopper velocity-flip triggers $4.4\times$ faster than fine-tuning, and transfers zero-shot to DreamerV3.

---


### 127. [Change the Base, Change the Game: Rethinking Pan-sharpening](https://arxiv.org/abs/2611.32002)

**<font color=#1a73e8>作者：</font>** Jeonghyeok Do, Geunhyuk Youk, Munchurl Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many pan-sharpening (PS) networks reconstruct high-resolution multispectral (HRMS) images by adding learned residuals to 4$\times$-interpolated low-resolution multispectral (LRMS) inputs, incorporating panchromatic (PAN) detail only through these residual corrections. This raises a simple question: Why start with a blurry base when sharp spatial detail is already available? We propose PanBase, a sharper multispectral starting point designed for more effective residual learning. Guided by physical sensor characteristics, PanBase combines PAN spatial detail with LRMS spectral information while enforcing consistency with the LRMS observations under sensor-specific blur. We construct this base without neural network training, estimating only nine coefficients per spectral band through closed-form calibration. Our PanBase can be easily integrated into existing backbones with a global residual skip through two simple changes: (i) replacing the skip base with PanBase and (ii) concatenating it as an additional input. Using each backbone's original training recipe and matched training budgets, PanBase improves most reduced- and full-resolution metrics on WorldView-3, QuickBird, and GaoFen-2, while achieving 4.4$\times$ faster training convergence on average. In zero-shot evaluation on WorldView-2, standalone PanBase achieves competitive reconstruction without target-sensor fitting or neural refinement.

---


### 128. [Calm Agent: Reframing Agent Interaction around Intermittent Human Attention](https://arxiv.org/abs/2611.32009)

**<font color=#1a73e8>作者：</font>** Dian Jin, Zixun Fu, Guan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI agents can carry out auxiliary tasks while users focus on other work. Yet users still need to understand task state, make changes, and respond when help is required. We argue that agents for ongoing auxiliary tasks should be designed around intermittent human attention: tasks should continue between interactions, and users should be able to return with little effort to understand and control them. We develop this position as Calm Agent. It connects three on-demand interaction modes: Delegate, Adjust, and Check, through a persistent task representation. Generative interaction provides controls and feedback suited to open-ended goals, while existing controls support routine actions. We illustrate these principles with Orvlet, a desktop prototype for background execution and compact task interfaces. We identify challenges in adapting interfaces while preserving continuity, coordinating attention across tasks, providing responsive interaction, and learning user habits over time. The aim is to support continuing task control while protecting attention for primary work.

---


### 129. [Distractors are the Real Enemy: Visual Distraction Adversarial Perturbations on SAM2-Based Video Tracking and Segmentation](https://arxiv.org/abs/2611.32011)

**<font color=#1a73e8>作者：</font>** Adonay Demewez Gebremedhin, Mohamad Alansari, Wessam Shehieb 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Promptable video trackers such as SAM2 achieve accurate and robust performance through strong temporal consistency, making them important foundations for downstream video understanding and tracking applications. As their use continues to expand, understanding their robustness to adversarial perturbations becomes increasingly important. Existing attacks on SAM2 largely focus on local mask degradation and short-term temporal feature disruption, leaving its longer-term dynamics and competing object interferences (Distractors) insufficiently explored. We observe that SAM2 itself exposes useful distractor cues when tracking becomes uncertain. Based on these observations, we propose DistractAttack, a white-box attack that uses background distractors to disrupt target tracking persistently. Its core procedure, Counterfactual Distractor Search (CDS), propagates clean and attacked trajectories in parallel to discover plausible competing regions and identify those that become increasingly effective under perturbation. The discovered evidence is accumulated over time to weaken target support and promote recurrent alternatives or disappearance predictions. Extensive experiments under video-level and one-shot perturbations across Visual Object Tracking and Video Object Segmentation demonstrate strong attack effectiveness, raising DRE to $4.4\times$ and NRE to $7.3\times$ their nearest baselines under video perturbation, while transferring effectively across model scales and tracker variants in black-box settings. Project page: this https URL

---


### 130. [DynaCue: Comparing Motion and Timing Between Groups of Videos](https://arxiv.org/abs/2611.32014)

**<font color=#1a73e8>作者：</font>** Hao Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A score that distinguishes videos with different temporal-consistency ratings can miss differences associated with motion preference. VideoScore's temporal consistency score distinguished higher- from lower-rated Pika videos in 95% of comparisons with 15 videos per group, yet could not detect the difference between preferred videos and their same-prompt alternatives in any of the 200 comparisons of 41 VideoGen-RewardBench pairs. We introduce DynaCue, a two-sample permutation test that combines complementary measurements of motion, frame continuity, and appearance to compare groups of videos without choosing a single cue in advance. DynaCue measures local changes in optical flow both before and after accounting for each clip's usual activity, captures interruptions through frame differences and freeze counts, and incorporates scores for motion and appearance. In controlled experiments, DynaCue detected group differences across five interventions affecting playback continuity, displacement, or rhythm. In real-world evaluations of generated videos where viewers rated temporal consistency or chose which of two videos they preferred for its motion, DynaCue detected group differences in at least 80% of resampled comparisons on each of the three datasets at the smaller sample sizes studied. Every other method evaluated on all three had a detection rate of 60% or less on at least one dataset.

---


### 131. [When Online Adaptation of Resilience Policies Hurts: Safe Exploration and Measurement Pitfalls in Resilience4j](https://arxiv.org/abs/2611.32015)

**<font color=#1a73e8>作者：</font>** Rajat M. Barot, Arjun S. Borkhatariya  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Circuit breaker, retry, and bulkhead settings in Java microservices are tuned once and frozen, although the best setting depends on the fault a dependency is currently showing. We study whether an online learner can pick these settings at runtime. AdaptR4j swaps Resilience4j policies atomically in Spring Boot 3 and lets a contextual bandit choose among complete CircuitBreaker/Retry/Bulkhead configurations from Prometheus signals. Our first, naive design scored worse than keeping the default policy in three of four winnable fault scenarios under the reward it optimised: exploring a menu that contained aggressive circuit breakers rejected most traffic while the learner was still learning. Two safeguards fix this: a safe policy menu (no breaker stricter than the latency SLO) and safe exploration with a bounded reward. With them, AdaptR4j beats the production default in every winnable scenario (p < 0.001, three runs each, run-to-run SD <= 0.03), beats the best fixed policy when the fault changes over time, and cuts user-visible failures up to 3.7x compared with the naive design. A context-free bandit on the same safe menu performs statistically indistinguishably, so the safeguards - not the learner - carry most of the benefit. We also report how an earlier version of our harness produced convincing but wrong results: a unit mismatch made every circuit breaker 100x too strict and rejected calls were invisible to the metrics, so 94% of user requests failed while latency and error metrics looked excellent.

---


### 132. [Learning Agent States for Latent Action Modeling](https://arxiv.org/abs/2611.32017)

**<font color=#1a73e8>作者：</font>** Shaoan Xie, Fan Feng, Peiyuan Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent action models (LAMs) learn action-like latents from unlabeled video by coupling frame-pair inference with latent-conditioned prediction, enabling policy and world-model pretraining. However, what the latent must explain depends on the representation space used for action inference and transition prediction. When this space entangles the agent's evolving physical state with visual context, such as background and persistent agent appearance, inferred latents can encode information unrelated to the agent's actions. To address this challenge, we propose Agent-State LAM, which jointly learns a compact agent-state representation and latent actions modeling its transitions. The compact state aggregates dense visual features into a shared space for both action inference and forward prediction. To guide what this state retains, we introduce spatially matched temporal discrimination (SMTD), which trains the state to distinguish its source frame from nearby frames through spatially flexible matching with frozen local visual features. Rather than comparing global frame representations, SMTD scores each frame by emphasizing its strongest local feature matches across spatial locations. This scoring allows background and persistent agent appearance to remain matched across frames despite displacement, making these shared cues less informative for identifying the source frame and encouraging the representation to capture the agent's evolving physical state. Extensive experiments on distracting control tasks and six real robot video datasets demonstrate improved action recovery, downstream control, and world-model prediction. Code and checkpoints are available at this https URL.

---


### 133. [Structure-Aware Transformers for Hierarchical Authorization in Personal AI Agents](https://arxiv.org/abs/2611.32018)

**<font color=#1a73e8>作者：</font>** Dongyu Cui, Jie Ding, Xuan Bi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personal AI agents can carry out complex, multi-step tasks on users' behalf, but doing so often involves numerous permission requests. Manually reviewing each request is time-consuming, while indiscriminate approval poses privacy and security risks. Predicting users' authorization preferences offers a way to reduce this burden while preserving user control. However, authorization prediction is challenging because permission requests are often hierarchical and observed user decisions are sparse and potentially correlated. To address these challenges, We propose the Parent-gated Authorization Transformer for Hierarchies (PATH) to predict users' authorization preferences for personal AI agents. PATH is a novel neural network architecture that combines hierarchy-aware attention masks with a parent-gated probability formulation to ensure hierarchy-consistent predictions. Hierarchy-level embeddings further support learning from sparse observations and patterns shared within each authorization level. We establish finite-sample risk bounds and provide sufficient conditions for consistent authorization probability estimation and algorithmic convergence. Experiments on simulated data, AI-generated user profiles, and real user authorization data demonstrate strong predictive performance with zero hierarchy violations.

---


### 134. [PFedHASNet: A Personalized Federated Hybrid Analog-Spike Network for Multi-Subject Motor Imagery EEG Decoding](https://arxiv.org/abs/2611.32019)

**<font color=#1a73e8>作者：</font>** Peijia Li, Ruidong Ma, Xianghong Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Motor imagery electroencephalography (MI-EEG) data are often collected and stored separately across subjects or institutions, and EEG acquisition and annotation remain costly. Training models solely on individual subject data limits the use of information from other subjects, whereas centralizing raw EEG recordings raises privacy and data governance concerns. Federated learning (FL) enables collaborative model training across distributed clients without sharing raw EEG data, providing a practical approach to leveraging information from multiple subjects. Accordingly, we propose PFedHASNet, a personalized federated hybrid analog-spike network for MI-EEG decoding. The shared encoder integrates continuous-valued temporal features, leaky integrate-and-fire (LIF) spike responses, and channel-wise log-variance statistics through learnable fusion weights. Client-private residual adapters and classifiers perform subject-specific feature refinement and personalized prediction, respectively. Experiments on held-out trials from participating subjects across four public MI-EEG datasets show that PFedHASNet achieves the highest mean client macro-F1 among 18 model configurations in cross-model comparisons, while maintaining competitive decoding performance with a compact client-side model in comparisons using the same backbone. Ablation studies further examine the contributions of hybrid representations and personalization components to decoding performance.

---


### 135. [APQKE-DR: Entropy-Failure Analysis of a Post-Quantum-Initialized Ratcheted Channel](https://arxiv.org/abs/2611.32024)

**<font color=#1a73e8>作者：</font>** Muhammad Asfand Hafeez, Zain Ul Abideen, Amna Zafar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Long-lived secure channels for embedded and cyber-physical systems (CPSs) must resist quantum attacks and failures in endpoint randomness. While several post-quantum key exchange protocols exist, their security assumes reliable randomness at the endpoint, but this assumption is not always true in embedded devices. In this paper, we introduce the Entropy Attack Suite (EAS) to evaluate secure channels facing endpoint randomness failures, such as low-entropy boot and Random Number Generation (RNG) path subversion. As a case study, we design and implement APQKE-DR, a post-quantum secure channel. Its handshake uses ML-KEM [1] and ML-DSA [2], producing a root key for an X25519 Double Ratchet. We assess the performance of APQKE-DR and security for smart grid communication, and integrate it beneath ANSI C12.22 and DNP3 without altering payload formats.
On a Raspberry Pi Compute Module 5, the APQKE handshake exchanges 9,610 bytes with median latencies of 1.99 ms (node) and 0.82 ms (server). The ratcheted channel adds 31 bytes per message. With fresh randomness and ideal cryptographic primitives, ProVerif verifies the modeled secrecy and authentication properties. If randomness fails, EAS can recover the RNG stream and root key from public transcripts. Under RNG-path subversion, a weak generator exposes the root key across sessions. If subversion also affects X25519 keys, attackers may access ratchet keys and plaintexts. TPM seeding prevents early-boot attacks but not later subversion, while measured boot can block modified firmware. Secure deployment thus requires integrity along the entire entropy path, not just strong cryptographic primitives.

---


### 136. [View Management with Gaussian Placement and Opacity Regularization for Online 3DGS](https://arxiv.org/abs/2611.32025)

**<font color=#1a73e8>作者：</font>** Dong Hwi Kim, Park Sangwon, Chaehyeon Song 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The realistic rendering of 3D Gaussian Splatting (3DGS) has drawn interest from real-time applications that require maps to be built online. This led to coupling 3DGS with SLAM, providing camera poses and initial Gaussians for the map. However, the map is still optimized with designs inherited from conventional SLAM, which train only on keyframes selected for localization and regularize geometry with uncertain frontend depth. These designs overlook the model complexity of a 3DGS map: with millions of parameters but few views of each region, the map overfits to sparse inputs. Resolving this is challenging, as every view and Gaussian added to the map competes for the same real-time budget. We close this gap from both sides. To add views while keyframes preserve the structure of the map, we progressively admit non-keyframe images as mapping updates complete and allocate the limited updates across different groups of frames according to the supervision each group provides. To control the model complexity of the map, edge-guided initialization places new Gaussians where image detail requires them. To complement the uncertain frontend depth, Self-Referenced Opacity Regularization (SOR) uses accumulated rendering evidence, at no extra rendering cost, to suppress the opacity of Gaussians that persistently contribute in front of a map-derived surface reference. Together, these designs improve both the appearance and the geometry of online maps within the real-time budget.

---


### 137. [Do Occupancy World Models Really Follow Actions?](https://arxiv.org/abs/2611.32029)

**<font color=#1a73e8>作者：</font>** Jongseong Bae, Ha Young Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Occupancy world models predict future 3D scenes conditioned on ego actions, yet their predictions may not faithfully follow the specified trajectory under counterfactual actions. Because driving datasets provide sparse coverage of alternative trajectories for each scene, existing models learn the spatial effect of ego motion implicitly from observed scene--trajectory combinations, which may entangle action effects with scene--trajectory correlations. We propose ReCast, an ego-trajectory-guided transformer that grounds future prediction in action-induced geometric correspondence across ego-centric frames. ReCast decouples historical encoding from future decoding and aligns deformable interactions using relative ego transformations, while retaining flexibility for non-rigid scene evolution. We also introduce a counterfactual action-faithfulness benchmark covering in-distribution, tail, and out-of-distribution trajectories. On Occ3D-nuScenes, ReCast achieves competitive standard forecasting performance while improving counterfactual forecasting, with particularly clear gains under out-of-distribution trajectories.

---


### 138. [Unifying Partner and Environment Diversity to Improve Human-AI Coordination](https://arxiv.org/abs/2611.32031)

**<font color=#1a73e8>作者：</font>** Patrick Q. Zhang, Yancheng Liang, Adrienne Fairhall 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Real-world applications of modern AI systems require generalization to both unseen environments and novel human users. The field of zero-shot coordination (ZSC) has focused primarily on deploying AI to cooperate with novel partners in otherwise familiar environments. Popular population-based methods achieve this by partnering the agent with a diversity of simulated human users during training in a fixed environment, but does not consider the more realistic scenario where both the users and the environment are unseen during training. Recently, training across environments has been explored in training a single self-play agent, which shows better generalization on both novel human users and unseen environments. In this work, we ask whether jointly modeling partner diversity and environment diversity yields stronger coordination with novel partners in novel environments. We introduce Cross Environment Co-Play (CECP), a two-stage framework that first trains a population of self-play agents across a distribution of procedurally generated environments, and then trains a cooperator policy against this partner population. To further couple social and environmental reasoning, we add a next-state prediction module that encourages representations to encode both partner behavior and task structure. We evaluate CECP on both a neuroscience-inspired cooperative foraging task, and the popular ZSC benchmark Overcooked, under held-out partner and held-out environment conditions. CECP achieves the strongest performance among the compared baselines and attains state-of-the-art results under our evaluation protocol for human-AI collaboration. We analyze the model's latent representation encoded by the next-state prediction module, showing it can not only improve the performance of the cooperative AI, but also provide more interpretable latents, demonstrated by the inference of partner skill levels.

---


### 139. [Scale-Robust and Global-Aware Representation Learning for Multivariate Time Series Anomaly Detection](https://arxiv.org/abs/2611.32033)

**<font color=#1a73e8>作者：</font>** Gyuwon Lee, Saejoon Park, Won-Seok Hwang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate time series anomaly detection (MTSAD) is an essential task for identifying abnormal system behaviors and supporting reliable operations across diverse real-world applications. Despite substantial advances in MTSAD, two key challenges in representation learning remain underexplored: (C1) how to learn scale-robust temporal representations that capture anomalies across different temporal scales and (C2) how to learn global-aware relational representations that capture inter-series dependencies by incorporating series-level global characteristics beyond local windows. To address these challenges, we propose STAGER, a novel method that jointly learns two complementary representations: scale-robust temporal and global-aware relational representations. Specifically, STAGER employs (1) a scale-robust temporal encoder that constructs a multi-scale temporal directed acyclic graph (DAG) to learn scale-robust temporal representations and (2) a global-aware relational encoder that incorporates learnable series-level global embeddings into the temporal representations and models inter-series relationships through graph neural networks. Two complementary auxiliary objectives further enhance the distinctiveness of the global embeddings. Extensive experiments on three real-world benchmark datasets demonstrate that STAGER achieves the best average rank among ten evaluated MTSAD methods across three evaluation metrics. Ablation and sensitivity analyses validate the effectiveness of the proposed components and auxiliary objectives, while efficiency evaluations demonstrate that STAGER achieves a favorable trade-off between detection performance and inference time compared with existing methods.

---


### 140. [BodyWeave: Native Body-Conditioned 3D Garment Generation](https://arxiv.org/abs/2611.32034)

**<font color=#1a73e8>作者：</font>** Junyi Zhang, Yuanchuan Wang, Qichao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating 3D garments for digital characters requires preserving a reference design while adapting the garment to the target body's shape and pose. Sewing-pattern methods can struggle to reproduce unfamiliar designs and fine details, while image-to-3D generators offer rich shape priors but typically lack explicit 3D body context. We present \textbf{BodyWeave}, a framework that unifies garment generation and fitting through native 3D body conditioning. Building on 3D generative priors, BodyWeave uses the body as a spatial reference throughout geometry generation: a \textbf{Global Body Adapter} guides garment placement and extent in the shared coordinate frame, while \textbf{Local Body Attention} guides surface refinement using nearby body geometry. A \textbf{Surface Penetration Loss} supervises decoded surfaces to reduce body intersections, and the resulting geometry conditions material synthesis to produce garments with physically based rendering attributes. To support learning across designs and wearers, we construct \textbf{GarmentWeave3D} with 293K aligned garment--body observations, including 114K same-design cross-body pairs. Evaluations on out-of-domain \textbf{Artist-Created Garments} demonstrate high geometric fidelity and low body penetration. Cross-body evaluations demonstrate accurate adaptation to new wearers with consistent garment--body spacing, while appearance comparisons show faithful fabric reproduction. Additional results and resources are available at this https URL

---


### 141. [DeCo-Attention: Decompose to Compensate for Low-Precision Attention](https://arxiv.org/abs/2611.32035)

**<font color=#1a73e8>作者：</font>** Yuhang He, Harrison Zhang, Fanrong Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-attention over tens of thousands of tokens dominates the generation time of video diffusion transformers, because its cost grows quadratically with sequence length. The FP4 matrix products of modern GPUs can speed up attention, but the 4-bit rounding of the queries Q and the keys K introduces large errors. We show that the exponential in softmax amplifies the error of their product QK, which therefore dominates the attention error. We propose DeCo-Attention, a co-design of algorithm and system for low-precision attention. DeCo-Attention is training-free and compensates the rounding error of Q and K along a few principal directions found by a per-head eigendecomposition. The lightweight compensation terms are appended to Q and K as extra channels, so the FP4 matrix product corrects its own rounding error while it computes the attention scores. Once the products run in FP4, the softmax bounds the kernel, and we optimize the softmax so that the gain of FP4 computation translates into realized speedup. With QK in FP4, we implement DeCo-Attention with the rest of attention in FP8 on GB300 and VR200 and in FP4 on RTX PRO 6000. On Wan2.2, these kernels run 2.13x, 2.49x, and 2.82x faster than BF16 attention, and the whole generation runs 1.55x, 1.68x, and 1.80x faster. On four video generation models, the FP8 configuration achieves LPIPS comparable to prior 8-bit QK methods, and the fully FP4 configuration lower LPIPS than prior fully 4-bit kernels.

---


### 142. [Instant LiDAR: Feed-Forward Gaussian Reconstruction for LiDAR Simulation](https://arxiv.org/abs/2611.32042)

**<font color=#1a73e8>作者：</font>** Xin Kang, Jiahui Huang, Jiawei Ren 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDAR reconstruction supports closed-loop autonomous driving simulation, but hours of per-scene optimization make large asset libraries costly to build and maintain. We present Instant LiDAR, a feed-forward pipeline that reconstructs multiple LiDAR scans as reusable Gaussian assets in minutes without per-scene optimization. LiDAR measurements provide strong geometric priors, but directly initializing Gaussians from them yields poor reconstruction due to nonuniform sampling and a limited field of view. Sparse returns leave surface gaps, while combining scans expands coverage but introduces redundant primitives. To address these challenges, Instant LiDAR combines measurement-anchored Gaussian prediction, sampling-aware Gaussian scales, and multi-frame consolidation. The predictor refines attributes anchored to recorded returns, while the scales adapt spatial support to LiDAR sampling. Multi-frame consolidation merges overlapping predictions into a compact asset spanning the driving log. Compared with NuRec, Instant LiDAR reconstructs scenes approximately 46 times faster on Physical AI (PAI) and 70 times faster on Waymo. It also achieves comparable downstream 3D detection accuracy on Waymo.

---


### 143. [CHORAL: A Multi-Agent Scaffold for Longitudinal Prognostic Reasoning from Patient-Generated Health Data](https://arxiv.org/abs/2611.32044)

**<font color=#1a73e8>作者：</font>** Youngji Koh, Esther Kang, Gyuna Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Longitudinal patient-generated health data can inform prognostic reasoning about how patients' conditions may evolve between follow-up visits. Existing approaches summarize trajectories or predict symptom states, but provide limited support for examining how heterogeneous evidence informs prognosis. We present CHORAL, a multi-agent scaffold that forms domain-specific appraisals before cross-domain synthesis and review, preserving evidence and revisions. Informed by a formative study with 12 psychiatrists, we evaluated CHORAL quantitatively and with 22 clinicians. CHORAL achieved balanced accuracy comparable to persistence (0.673 vs. 0.672), while detecting 40% of LOW-to-HIGH deterioration cases missed by persistence. Versus a single-agent baseline, it improved balanced accuracy from 0.639 to 0.673 and evidence coverage from 70.1% to 89.2%. Clinicians rated CHORAL significantly higher for evidence appraisal, alternative interpretations, grounds for challenge, and distinguishing what to rely on from what required verification. These findings show how multi-agent deliberation can support review by exposing alternative interpretations and grounds for verification.

---


### 144. [SegPFN: Training-Free In-Context Segmentation with Tabular Prior-Data Fitted Networks](https://arxiv.org/abs/2611.32045)

**<font color=#1a73e8>作者：</font>** Jiajian Ma, Yihao Qiao, Ke Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In-context segmentation (ICS) uses one or a few annotated reference images to specify what to segment in a target image. Existing training-free ICS approaches typically rely on manually designed inference procedures, which may limit how flexibly reference information is combined. Learned in-context inference offers an adaptive alternative, but acquiring this capability through segmentation-specific training can compromise generalization to unseen domains. We therefore ask: can a pretrained in-context learner infer what to segment from annotated references without segmentation-specific training? We introduce SegPFN, a training-free framework that reformulates ICS as tabular classification over frozen visual features. A frozen tabular prior-data fitted network (PFN) uses labeled reference patches as context to classify patches in the target image. We comprehensively benchmark SegPFN against major existing ICS methods across 11 datasets spanning semantic, part, and personalized segmentation. SegPFN improves overall mean intersection-over-union (mIoU) by 4.7 points over the strongest overall baseline and achieves the highest average mIoU in four of five task-shot settings. Further analyses show that hard-negative reference patches improve fine-grained target discrimination, while joint conditioning enables SegPFN to use multiple references effectively. These results show that SegPFN offers a simple and effective paradigm for training-free in-context segmentation.

---


### 145. [SurgGenesis: A Generative Surgical World Model for Future-Aware Surgical Understanding](https://arxiv.org/abs/2611.32054)

**<font color=#1a73e8>作者：</font>** Qirui Zhong, Quande Liu, Yang Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical scene understanding is constrained by data scarcity and long-tail class imbalance, as annotating surgical videos demands scarce clinical expertise while rare procedural events remain underrepresented. We tackle this through data generation and propose SurgGenesis, a generative surgical world model that learns future surgical state transitions in a latent space from visual observations and textual procedural descriptions, serving as a scalable surgical data engine. To adapt a large-scale video diffusion model to the data-scarce surgical domain without catastrophic forgetting, we introduce a three-stage progressive LoRA strategy that incrementally injects endoscopic visual priors, procedural semantics, and spatial motion cues. Rather than judging generation by visual fidelity alone, we validate SurgGenesis along two axes that separate a world model from a generic generator: (i) future-awareness, by comparing predicted futures against the real future through a GT-latent prediction gap and temporal-horizon analysis, and (ii) action-faithful usefulness, by checking that generated clips contain the commanded surgical triplet and that using them to rebalance long-tail events and drive downstream understanding (segmentation, triplet recognition, 3D reconstruction) yields action-specific gains. Conditioned futures therefore complement conventional long-tail sampling. Code: this https URL

---


### 146. [LoopDVR: Looped Transformer for Efficient Dense Visual Recognition](https://arxiv.org/abs/2611.32067)

**<font color=#1a73e8>作者：</font>** Sirui Liang, Xuanlong Yu, Longfei Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose LoopDVR, a framework for converting pretrained Transformer-based dense visual recognition models into parameter-efficient looped networks. Rather than reducing the network width or depth directly, LoopDVR reuses Transformer blocks across layers in both the ViT backbone and Transformer decoder, reducing the number of parameters while retaining the original computational structure. However, naively sharing parameters can disrupt the distinct transformations learned at different depths. To address this challenge, we identify suitable sharing groups based on inter-layer representation dissimilarity and keep the final backbone block independent for multi-scale feature construction. We then initialize each shared backbone block with the pretrained weights of its group's terminal layer to better preserve the learned representations. An independent Loop Adapter at each layer further helps retain depth-specific transformations within shared blocks. Subsequently, we distill visual representations into the looped backbone and integrate it with a looped decoder for task-specific training. Experiments demonstrate that LoopDVR achieves the best accuracy--parameter trade-offs across dense recognition tasks. Compared with the reference models, it reduces parameters by approximately 28% while maintaining competitive accuracy. Notably, LoopDet-S achieves 50.9 box AP with only 7.0M parameters, highlighting its effectiveness in compact models.

---


### 147. [Not the Scalar, but Its Evolution: Robust Source Attribution for Generated Images](https://arxiv.org/abs/2611.32074)

**<font color=#1a73e8>作者：</font>** Chao Wang, Zijin Yang, Yaofei Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The widespread deployment of latent generative models (LGMs) makes generated image source attribution essential for copyright auditing and data governance, yet practical attribution should remain reliable under common post-processing and platform-induced processing. Existing reconstruction-based attribution methods summarize an image's reconstruction response to a single global scalar, such as the reconstruction error or the ratio of two consecutive errors. These summaries discard channel-frequency structure, allowing image content and post-processing variation to obscure source evidence and making attribution after spreading difficult. We instead uncover a more stable source-discriminative cue under post-processing: the frequency-resolved evolution of residual energy across repeated applications of the same reconstruction operator. Motivated by this insight, we characterize a phenomenon we term Spectral Contraction and use it to build SpCon, a source-attribution framework that accesses only the target model's VAE. SpCon obtains adjacent residuals through two deterministic reconstructions, builds a spectral-contraction representation from their frequency-resolved relative energy change, and aggregates Student-t response densities for each source-condition pair over a finite set of fitted reference components. The same representation supports three settings according to non-belonging reference availability: none (Target-Only, TO; belonging references only), external out-of-domain sources (External-Reference, ER), or known in-domain competitors (Known-Reference, KR). Across seven LGMs, TO, ER, and KR attain average AUROC/AP of 0.8786/0.6344, 0.9404/0.7886, and 0.9652/0.8626 over the 35 conditions, all outperforming the strongest baseline (0.8154/0.5277), and achieve 0.8581/0.5507, 0.9369/0.7549, and 0.9734/0.8773 on the three social platforms.

---


### 148. [A Fused Gaussian Process Bandit Framework for Multi-Fidelity Bayesian Optimization](https://arxiv.org/abs/2611.32092)

**<font color=#1a73e8>作者：</font>** Muyun Lu, Jose E Aguilar Escamilla, Huazheng Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian optimization (BO) is widely used to maximize expensive black-box functions when direct evaluation is costly. In many real-world applications, the high-fidelity objective can be approximated by a series of lower-fidelity models that provide partial but informative signals at substantially reduced cost. Multi-fidelity BO (MFBO) algorithms aim to strategically combine these information sources to achieve an optimal trade-off between accuracy and evaluation cost. However, existing MFBO methods often oversimplify the complex dependencies between fidelity levels or rely on heuristic acquisition functions that lack theoretical performance guarantees. To address these limitations, we introduce a new formulation of the MFBO problem as a fused Gaussian Process bandit and develop a corresponding Fused Gaussian Process Upper Confidence Bound (FGP-UCB) algorithm. Our approach accurately predicts the high-fidelity function by fusing multi-fidelity observations through an autoregressive Gaussian Process model and explicitly quantifies the uncertainty arising from parameter estimation across fidelity levels. The proposed method also provides theoretical simple-regret guarantees, overcoming a key limitation of existing MFBO algorithms that lack provable performance bounds. Effectiveness of the proposed method is demonstrated via both theoretical analysis and empirical studies.

---


### 149. [RISE: Reasoning with Implicit State Embeddings for GUI Agents](https://arxiv.org/abs/2611.32102)

**<font color=#1a73e8>作者：</font>** Enqi Liu, Zhi Gao, Liu Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Graphical user interface (GUI) agents translate user instructions and screenshots into executable actions. To learn executable actions, existing approaches often rely on explicit reasoning during training, which encourage over-reliance on specific reasoning patterns rather than generalizable action-relevant information. In this paper, we propose an implicit framework, RISE, which integrates action-relevant reasoning into implicit state representations to guide GUI action prediction. To this end, action-relevant reasoning is captured through three complementary supervision objectives: full-CoT state alignment preserves information across the reasoning process, action-distribution alignment encodes action preferences, and reasoning-to-action boundary alignment captures the representation immediately before action generation. In this case, our RISE effectively learns informative implicit representations, thereby improving the accuracy of next-action token prediction. RISE achieves 70.6\% accuracy on OSWorld-G, establishing state-of-the-art performance among compared 8B models with a 4.3-point gain over its backbone. Results across two distinct backbones and six diverse benchmarks further demonstrate its effectiveness in GUI grounding and action prediction. Our code is available on our project page.

---


### 150. [An Automated Framework Integrating Deep Learning and Anatomical Reasoning for Cardiac Phenotyping From CCTA](https://arxiv.org/abs/2611.32114)

**<font color=#1a73e8>作者：</font>** Hien Minh Tran, Thi-Thu-Hien Pham, Le Duy Tan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Coronary computed tomography angiography (CCTA) depicts coronary anatomy and cardiac fat, but segmentation alone does not ensure anatomically consistent measurements. We propose an automated framework that combines deep learning with anatomical reasoning for quantitative cardiac phenotyping. Its anatomical measurement module uses graph geometry, branch identity, and surrounding structures to define vessel-specific pericoronary adipose tissue (PCAT) sampling and a surrogate epicardial adipose tissue (EAT) compartment. The latter also generates training targets without requiring expert pericardium contours. A companion module quantifies coronary calcium on non-contrast CT. Component-wise benchmarking was conducted on five public datasets: ImageCAS, ImageCAS-X, COCA, Visual Lab, and MultiD4CAD. On ImageCAS-X Test-160, lumen segmentation with validation-selected post-processing achieved a Dice score of 0.9133 and a clDice score of 0.940, exceeding the corresponding published CAS-Net point estimates. In the four-split ImageCAS evaluation, the four-member ensemble outperformed the single ResEnc-L model. Analysis of 800 paired scans showed that PCAT attenuation measurements differed between whole-vessel and lumen references. External EAT evaluation showed strong volume correlation and good spatial overlap. Explicit anatomical rules make the resulting measurements interpretable and inspectable. In practice, the framework provides a standardized pipeline for processing cardiac CT cohorts and quantifying coronary calcium, PCAT, and EAT for population-level analysis and comparison across studies. The source code is publicly available at this https URL

---


> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-342](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
