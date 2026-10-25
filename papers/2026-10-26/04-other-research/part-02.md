# 📦 其他研究 | 2026年10月26日

> 本类共 **211** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-211](./part-05.md)

---

### 51. [Unified Trajectory and 3D Pose Forecasting for Multi-Agent Sports Analysis](https://arxiv.org/abs/2610.30519)

**<font color=#1a73e8>作者：</font>** Marc Peral, Guillem Capellera, Luis Ferraz 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Forecasting future human motion requires jointly reasoning about an agent's global trajectory and 3D body pose, which are tightly coupled, particularly in team sports where multiple interacting players introduce complex social dynamics. We exploit a socio-temporal encoder that fuses trajectory and pose at the input level and models them jointly through shared factorized attention. The model is further enhanced by a per-joint loss reweighting scheme that emphasizes dynamic joints and prevents degenerate solutions, and a frequency-domain trajectory smoothing term that improves trajectory prediction while indirectly benefiting pose forecasting. To ensure fair comparison with prior joint forecasting methods, we identify and correct evaluation biases arising from overlapping sequence construction, adopting instead a non-overlapping protocol and a deterministic, oracle-free strategy for multi-future prediction. Our approach improves over prior joint forecasting methods on both WorldPose and 3DPW, with the largest gains on pose accuracy, demonstrating that the proposed joint formulation generalizes beyond the densely interactive scenarios that motivate it.

---


### 52. [NEST: Nested Embedding Representation for Multiscale Clustering](https://arxiv.org/abs/2610.30520)

**<font color=#1a73e8>作者：</font>** Zhanqi Zhang, Mikio Aoi, Gal Mishne  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world data often exhibits cluster structure at multiple resolutions, yet existing methods typically learn a single partition or construct an explicit hierarchy. Inspired by Matryoshka Representation Learning, we introduce NEST, an unsupervised framework that encodes coarse-to-fine structure within a single embedding. NEST jointly optimizes clustering and separation across nested prefix subspaces, enabling progressively finer distinctions as embedding dimensionality increases, with rank and within-cluster regularization that keep the embedding from collapsing. Empirically, distances in the learned embedding follow the hierarchy distance more closely than those of the input, although the hierarchy is never observed during training. On synthetic hierarchies, NEST recovers multiscale structure given only the number of clusters per level. Experiments on vision, text, and single-cell data further demonstrate multiscale organization across real-world representations. By making clustering granularity an intrinsic property of the representation, NEST provides a unified approach to multiscale structure discovery.

---


### 53. [Atlas: Making Sense of Long Horizon Agent Trajectories](https://arxiv.org/abs/2610.30548)

**<font color=#1a73e8>作者：</font>** Sangho Suh, Joseph Chee Chang, Pao Siangliulue 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI agents can now search literature, generate hypotheses, analyze datasets, and run experiments at a scale difficult for researchers to match. Yet scaling scientific execution does not automatically scale researchers' ability to make sense of what agents produce. When researchers return to a long-horizon run, they must evaluate work they did not monitor: what the agent produced, which decisions shaped those outputs, and whether those decisions served the research goal. We frame this post-run sensemaking as a representation problem across three linked levels: goal, decision, and artifact. From this framework we developed Atlas, an agentic workspace with a trajectory tree, which renders the run as a branching structure showing what the agent chose and set aside, and artifact projections over six representations. In a within-subjects study (N=14), participants reported higher decision transparency, artifact sensemaking, and goal connection with Atlas than with a standard baseline, together with substantially lower subjective workload.

---


### 54. [Bridging the Closed-World Gap: Interpretable Anomaly Detection via a Hybrid TSK-FCM Ensemble on the BETH Dataset](https://arxiv.org/abs/2610.30576)

**<font color=#1a73e8>作者：</font>** Lohith Srikanth Pentapalli, Josette Riep, Justin Ouwerkerk 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A fundamental paradox plagues the deployment of Machine Learning in cybersecurity: supervised models generalize poorly to novel, Out-of-Distribution (OoD) attacks, whereas unsupervised models often suffer from poor separability, leading to unmanageable false-alarm rates. This challenge is exemplified by the BETH dataset, a kernel-level benchmark in which the training data consists solely of benign and suspicious insider behaviors, whereas the test set consists almost entirely of novel botnet activation attacks. To bridge this detection gap, we propose a Hybrid Fuzzy Ensemble that synergizes the precision of supervised learning with the adaptability of unsupervised clustering. Our architecture integrates a gradient-optimized Takagi-Sugeno-Kang (TSK) fuzzy classifier to act as an expert on known insider threats, with a parallel Fuzzy C-Means (FCM) module to detect geometric anomalies. A critical finding of our research is that traditional fuzzy membership scores degrade in high-dimensional feature spaces due to the curse of dimensionality. We overcome this by introducing a robust Min Distance metric that exploits the raw geometric isolation of botnet activation attacks. This approach yields a state-of-the-art AUROC of 0.9951 on the BETH test set, outperforming the original Isolation Forest baseline by 17.1%. By combining near-perfect OoD detection with the intrinsic interpretability of fuzzy logic, our framework offers a viable path toward robust, transparent, and autonomous network defense.

---


### 55. [Evaluating Type-1 Diabetes Digital Twins by Decision Quality](https://arxiv.org/abs/2610.30577)

**<font color=#1a73e8>作者：</font>** Victor Li, Owen Tucker, Michael S. Hughes 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A digital twin (DT) for type 1 diabetes (T1D) can predict how an individual's blood glucose will respond to different insulin treatments without actually trying them. For each treatment, downstream statistics of predicted glucose trajectories, such as glycemic risk, can be computed to guide clinical decisions. However, the quality of DTs is usually measured by the accuracy of their predicted glucose trajectories, which may not reflect the quality of the downstream treatment decisions they inform. In this work, we directly evaluate DTs by this decision quality on downstream treatment ranking, i.e., whether a DT predicts glucose trajectories that can be used to rank candidate treatments as the real patient would. We present an evaluation protocol over 30 virtual patients from the FDA-accepted UVA/Padova model, each simulated under 21 different basal-bolus treatments. For each patient, a DT is fitted under one treatment and then produces glucose trajectories for the remaining 20 treatments. Our results show that prediction accuracy and decision quality disagree. A baseline that models the average patient, never seeing the individual's glucose data, has the lowest prediction accuracy of all six methods (RMSE: 63.6 mg/dL) but ranks treatments with the second-highest mean Spearman (0.766), while a black-box neural network that predicts glucose nearly twice as accurately (RMSE: 32.9 mg/dL) ranks them no better than a random ordering of the 20 treatments (0.049 Spearman). Therefore, selecting a DT based on prediction accuracy alone can prefer one that recommends treatments at chance, and decision quality must be evaluated directly rather than assumed to follow from prediction accuracy.

---


### 56. [KinoUAV: A Benchmark for Safe and Stable UAV Vision-Language Navigation with Kinodynamic Modeling](https://arxiv.org/abs/2610.30609)

**<font color=#1a73e8>作者：</font>** Chenyao Yang, Peijin Wang, Yingchao Feng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unmanned aerial vehicles (UAVs) have recently emerged as important remote sensing platforms, and UAV navigation has shown great potential in remote sensing applications. However, existing methods do not explicitly incorporate kinodynamic modeling or safety distances into trajectory generation, resulting in high absolute yaw rates, frequent collisions, and low navigation success rates, which limit safety and motion stability. To address this challenge, we introduce KinoUAV, a kinodynamic benchmark comprising a dataset and KinoUAV-Agent. First, we develop a hierarchical kinodynamic trajectory generation pipeline that drives UAV through acceleration actions. It uses waypoint chains from global planning and generates trajectories segment by segment under velocity, acceleration, and jerk constraints, reducing oscillations and improving trajectory stability. Furthermore, we introduce directional free-space distance (DFD) labels into the constructed dataset to describe the available clearance for safe motion decisions. The proposed KinoUAV-Agent predicts DFDs and uses them to generate safe actions, decoupling perception from action decision-making. This design enables autonomous obstacle avoidance and improves navigation safety. The benchmark incorporates the proposed Cruise-Seek task, in which the UAV first enters the target region and then searches for the target, reducing the difficulty of target search and improving navigation success. Experiments on KinoUAV show that KinoUAV-Agent outperforms existing methods, achieving the highest success rate while maintaining lower absolute yaw rates and collision rates. These results demonstrate the effectiveness of kinodynamic modeling for safe and stable UAV navigation.

---


### 57. [GSHeadRelight: Fast Relightability for 3D Gaussian Head Synthesis](https://arxiv.org/abs/2610.30619)

**<font color=#1a73e8>作者：</font>** Henglei Lv, Bailin Deng, Jianzhu Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Relighting and novel view synthesis of human portraits are essential in applications such as portrait photography, virtual reality (VR), and augmented reality (AR). Despite recent progress, 3D-aware portrait relighting remains challenging due to the demands for photorealistic rendering, real-time performance, and generalization to unseen subjects. Existing works either rely on supervision from limited and expensive light stage captured data or produce suboptimal results. Moreover, many works are based on generative NeRFs, which suffer from poor 3D consistency and low real-time performance. We resort to recent progress on generative 3D Gaussians and design a lighting model based on a unified neural radiance transfer representation, which responds linearly to incident light. Using only in-the-wild images, our method achieves state-of-the-art relighting results and a significantly faster rendering speed ($\times12$) compared to previous 3D-aware portrait relighting research. Project page: this http URL.

---


### 58. [Refining Open-Vocabulary Semantic Segmentation via Regional Semantics and Visual Prototypes](https://arxiv.org/abs/2610.30623)

**<font color=#1a73e8>作者：</font>** Aijing Yu, Zhengbo Wang, Lijun Sheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contrastive Language-Image Pre-training (CLIP) has shown superior performance in the image-level open-vocabulary classification task, benefiting from its powerful alignment of visual features and text embeddings. However, dense prediction tasks require models to perform pixel-level predictions, necessitating modifications to CLIP for region-text alignment. In this paper, we adjust the attention layers within the vanilla visual encoder of CLIP. With a novel attention calculation method for selective attention features, the model retains more regional semantic information. To further mitigate the negative impact of the modality gap, we introduce additional visual prototypes to refine the original predictor solely based on text embeddings. Specifically, patch features with confident predictions are selected to form an additional auxiliary memory-based classifier for more accurate prediction. We further integrate an optimizable feature extractor with an exponential moving average updating strategy to enhance prediction quality. Extensive experiments on $5$ semantic segmentation datasets demonstrate the effectiveness of our method.

---


### 59. [CODI: Improving Self-Supervised Vision Transformers with Cross Distillation](https://arxiv.org/abs/2610.30639)

**<font color=#1a73e8>作者：</font>** Siran Dai, Qianqian Xu, Peisong Wen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised Vision Transformers learn strong image-level representations, but their patch-level representations can be unreliable for dense prediction. We study this mismatch and find that the class token concentrates global semantics on a small number of representative patches, while dense prediction errors often occur on low-attention regions. We provide a local gradient analysis showing that, along the [CLS] attention readout, image-level self-distillation gradients are weighted by [CLS]-to-patch attention mass. To provide masked patches with global semantics without changing the architecture, we propose Cross Distillation (CODI), which mixes a small amount of the teacher class-token distribution into each teacher patch-token target. CODI gives every masked patch an attention-independent semantic correction while preserving the standard self-distillation architecture. Experiments on dense and image-level benchmarks show that CODI improves both dense and image-level performance under aligned pretraining settings. Code is available at this https URL.

---


### 60. [Asking Less, Adapting Better: Feedback-Efficient Test-Time Adaptation for Vision-and-Language Navigation](https://arxiv.org/abs/2610.30643)

**<font color=#1a73e8>作者：</font>** Zixu Wang, Huaquan Zhang, Shoukai Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-and-Language Navigation (VLN) requires agents to follow instructions and navigate to target locations. However, current VLN agents often suffer severe performance degradation in unseen environments due to distribution shifts. Test-Time Adaptation (TTA) offers a promising paradigm to bridge this gap, yet existing methods that rely on unsupervised entropy minimization can propagate errors through the trajectory, causing cascading failures in navigation. Recent methods mitigate this by incorporating human feedback, but they apply trajectory-level supervision uniformly across all steps without localizing the actions is truly informative, leading to inefficient feedback utilization and mismatched optimization granularity. To address these limitations, we propose FETA, a Feedback-Efficient Test-Time Adaptation method that improves both feedback efficiency and optimization reliability. To reduce unnecessary human interventions, we introduce a hierarchical sample selection strategy to localize informative samples. Specifically, we first filter trajectories whose normalized policy entropy exhibits large fluctuations. Within each selected trajectory, we further select the critical action via an entropy-gradient saliency criterion and query a single binary feedback on its correctness. A discrepancy-aware entropy optimization objective then updates the policy only at the queried step, with adaptive scaling that assigns larger relative weights to samples with greater prediction-feedback discrepancy. Extensive experiments across multiple benchmarks demonstrate that FETA achieves state-of-the-art performance with fewer human interventions, while remaining robust under noisy feedback and continual adaptation settings.

---


### 61. [One-shot federated unsupervised domain adaptation with Smoothed Knowledge Distillation and teacher refinement](https://arxiv.org/abs/2610.30646)

**<font color=#1a73e8>作者：</font>** Ali Abedi, Q. M. Jonathan Wu, Ning Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Federated unsupervised domain adaptation (FUDA) addresses the challenge of adapting models to an unlabeled target domain using decentralized source domains while preserving data privacy. However, existing FUDA methods typically require multiple communication rounds, rely on complex aggregation strategies, and often struggle with noisy pseudo labels and inconsistent source knowledge. To address these challenges, we propose SKD-ETR, a novel one-shot FUDA framework that combines Smoothed Knowledge Distillation (SKD) and Exponential moving average-based Teacher Refinement (ETR). SKD trains a student model on the target domain using smoothed soft pseudo labels generated by the ensemble of source models. This reduces overconfidence, mitigates noise, and improves robustness. ETR further refines each source model by interpolating its parameters toward the student via exponential moving average (EMA), thereby transferring target-domain knowledge back to the teachers. This bidirectional refinement enhances pseudo-label quality and student generalization without additional communication overhead. SKD-ETR eliminates complex aggregation by initializing the student model randomly and performing a single-round distillation process. Extensive experiments on OfficeHome, Office-Caltech, and DomainNet demonstrate that SKD-ETR achieves competitive performance while being communication- and computation-efficient, and robust under noisy supervision. The code for this paper is available at this https URL.

---


### 62. [Residual Calibration via Local Feature-Space Refinement](https://arxiv.org/abs/2610.30652)

**<font color=#1a73e8>作者：</font>** Xihao Wang, Chengyao Yu, Ruixing Ming  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep neural networks often struggle to provide reliable confidence estimates, making post-hoc calibration essential for reliable decision-making. Existing post-hoc methods largely rely on score-based transformations, which improve marginal calibration but often fail to capture spatially varying miscalibration in local regions of the learned feature space. To address this gap, we propose Local Adaptive Probability Estimation (LAPE), a post-hoc residual calibration framework. Specifically, LAPE treats the global calibrator output as a stable anchor and refines the individual prediction by leveraging non-parametric local evidence from neighboring calibration samples. As a plug-and-play refinement module, LAPE effectively utilizes the information about feature-space geometry and can reuse the calibration data that are used to construct the global calibrator. Furthermore, we extend LAPE to the setting with multi-view inputs through Cascade Feature Augmentation Fusion (CFAF). Extensive experiments demonstrate that the proposed methods can improve the calibration quality of various existing baselines and remain efficient and robust across different settings.

---


### 63. [RiboBridge: protein-conditioned de novo RNA binder structure design](https://arxiv.org/abs/2610.30668)

**<font color=#1a73e8>作者：</font>** Zhou Zhang, Hanqun Cao, Minghao Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Designing RNA molecules that bind to target protein structures requires generating both an RNA conformation and its bound complex geometry, without assuming a predefined binding site. Existing approaches generally model these coupled processes within a unified representation, entangling RNA conformation generation with protein-relative placement. In this work, we introduce RiboBridge, a structure-first framework that separates RNA conformational generation from protein--RNA assembly through cross-frame interaction geometry. RiboBridge first proposes multiple candidate RNA-binding interfaces on the protein surface, generates canonical RNA conformations within a pretrained RNA structural latent space (RiboSphere), and then predicts protein--RNA interaction constraints to bridge the independently defined RNA and protein coordinate frames. The resulting interaction geometry is converted into a geometrically consistent protein-relative pose through rigid placement. We evaluate RiboBridge on a temporally split, sequence-filtered, and redundancy-controlled benchmark of 124 protein--RNA complexes. Under post-hoc interface-correspondence evaluation, where native information is used only after generation to select among already generated predicted-pocket candidates, RiboBridge achieves the highest fNAT and DockQ and the lowest interface and ligand RMSDs among compared methods. Component ablations and stage-wise diagnostics further characterize the contributions of RNA conformational generation, interaction prediction, and rigid placement, identifying the main sources of complex-recovery error.

---


### 64. [AgentDreamer: Agentic 3D Motion Reasoning for Text-Controllable Physics Simulation](https://arxiv.org/abs/2610.30679)

**<font color=#1a73e8>作者：</font>** Mijeong Kim, Suho Park, Junha Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose AgentDreamer, an agent-guided optimization framework that aligns text instructions with simulated motion through explicit 3D motion planning. Given a text instruction and scene geometry, an off-the-shelf agent translates the instruction into a structured semantic motion prior, specifying what should move, in which direction, and in what temporal order. The agent represents this prior using parametric functions over a series of temporal chunks, yielding dense 3D trajectories. We then optimize the parameters of a differentiable MPM simulator such that its rollout best matches the prior while remaining constrained by the scene dynamics. This allows the agent to provide semantic guidance from language, while the simulator grounds it in physically feasible motion. We further introduce Motion-IG, an information-theoretic metric for text-motion alignment based on masked text recovery. By comparing the likelihood of recovering masked motion-related content with and without the simulated motion, Motion-IG measures the information contributed by the motion beyond that available from the remaining text and scene context. Experiments show that AgentDreamer improves text alignment over video-based guidance, producing simulations that more closely follow the requested physical behavior.

---


### 65. [Direct cueing of word identity through word duration: evidence from Mandarin homophones](https://arxiv.org/abs/2610.30682)

**<font color=#1a73e8>作者：</font>** Xiaomeng Zhu, Megan Niu, Jason Shaw 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While there is increasing evidence that words are stored in the mental lexicon with some phonetic detail, there are open questions about exactly which phonetic details are stored and whether they are functionally relevant for spoken word recognition. Word-level phonetic cues, such as word duration, provide an appropriate test case. Across languages, including Mandarin Chinese, high frequency words are shorter than low frequency words. Using a homophone ordering task, we investigate whether differences in word duration impact word recognition. Mandarin Chinese was examined since it has abundant disyllabic homophones. Our results indicate that participants were able to use word duration to recognize the order of homophone pairs, selected to vary in lexical frequency. Both with high noise levels and when no other cues were available, participants mapped the shorter duration auditory stimulus to the higher frequency word. The results provide evidence that word duration can directly cue the identity of words, suggesting that it may be a phonetic detail incorporated into the lexical representation. We discuss this direct cueing account alongside alternative accounts of how word duration may modulate word recognition.

---


### 66. [Learning Domain Trajectories with Flow Matching for Gradual Domain Adaptation](https://arxiv.org/abs/2610.30685)

**<font color=#1a73e8>作者：</font>** Yubo Huang, Yushe Cao, Zixi Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large distribution shifts remain a primary obstacle for domain generalization and unsupervised adaptation. Although gradual domain adaptation alleviates this difficulty by introducing ordered intermediate domains, most existing approaches still operate in a discrete, step-wise manner, which can accumulate errors and often relies on unstable Min--Max optimization. We propose \textbf{FlowGDA}, a flow-matching framework that models gradual adaptation as \emph{continuous} transport on a statistical manifold in a representation space. FlowGDA learns time-dependent velocity fields that induce smooth domain trajectories, using a simulation-free regression objective rather than adversarial training. To prevent semantic drift, we couple left-to-right transport between consecutive domains with a source-anchored transport and a semantic consistency loss, and we further stabilize learning via a two-stage sequential optimization scheme. Extensive experiments demonstrate that our method outperforms state-of-the-art techniques, validating flow matching as an effective alternative for domain adaptation.

---


### 67. [An Agent Architecture with Tools and Memory for Selective Correction of Wrist PPG Heart Rate Estimates](https://arxiv.org/abs/2610.30688)

**<font color=#1a73e8>作者：</font>** Xu Wang, Shuhan Yi, Zhen Cheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wrist photoplethysmography (PPG) heart rate estimates are vulnerable to motion artifacts, and corrections that reduce mean error can worsen individual windows. We propose an agent architecture with tools and memory around a fixed heart rate estimator. Pulse, motion, and limited historical evidence generate candidate estimates, whose predicted benefits and harms guide selection. An independent risk gate determines whether to retain, correct, or reject each output. We trained the architecture on PPG-DaLiA and tested it on Wrist Exercise, GalaxyPPG, and WildPPG with frozen weights. Across these four public datasets, mean absolute error (MAE), macro-averaged over ten estimators, decreased by up to 44.5%, with the largest reduction on GalaxyPPG. Beneficial and harmful corrections decreased and increased absolute error by more than 1 bpm, respectively. Their ten-estimator macro-averaged proportions ranged from 16.06% to 36.64% and from 1.68% to 6.77%, respectively, across the four datasets. At 60% and 80% target coverage, numerical correction on the same accepted windows contributed more to total error reduction than window selection. We implemented real-time wearable acquisition, Bluetooth reception, and smartphone deployment of a selected estimator and the framework. In backend analysis of four prototype recordings from one participant, ten-estimator macro-averaged MAE decreased from 9.09 to 4.45 bpm without additional rejection. Under the evaluated conditions, the architecture improved average accuracy while quantifying correction benefits and harms, supporting wearable heart rate analysis that considers error, correction risk, and coverage.

---


### 68. [LoRA Superposition across Pretrained Models](https://arxiv.org/abs/2610.30691)

**<font color=#1a73e8>作者：</font>** Keigo Watanabe, Hiroshi Kera, Kazuhiko Kawamoto  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) is usually tied to the pretrained backbone on which it is learned. We ask whether LoRAs trained independently for the same task on different pretrained backbones can be summed and applied unchanged to all contributing backbones. We call this construction LoRA superposition. Across seven ViT-B/16 CLIP backbones and eight image-classification tasks, the exact sum improves all 56 backbone-task pairs and achieves a mean accuracy gain of 30.21 percentage points over the unadapted backbone. The exact sum achieves a mean accuracy only 0.28 percentage points below that of individually trained solo LoRAs. In contrast, a leave-one-model-out (LOMO) sum produces a mean gain of only 0.06 percentage points over the unadapted backbones. Backbone-specific solo LoRAs are nearly orthogonal in parameter space, while pairwise cross-backbone responses are strongly concentrated on the diagonal. These results support a component-wise non-interference hypothesis, under which the frozen backbone acts as an implicit selector of its own component without explicit routing or cross-model alignment.

---


### 69. [ParaLin++: Accelerating Parallel Diffusion Integrator via Intrinsic Partially Linear Structure](https://arxiv.org/abs/2610.30704)

**<font color=#1a73e8>作者：</font>** Jianrong Lu, Zhiyu Zhu, Hui Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free few-step samplers are often described as nearly quality-lossless under conventional FID/CLIP-style evaluation. It remains unclear whether that conclusion transfers to more realistic and complex generation-quality benchmarks. We first systematize the quality metrics used to evaluate training-free sampling acceleration for diffusion and flow-matching models.
We find that representative training-free step-shortening methods often remain nearly lossless under FID/CLIP-class metrics, yet can suffer substantial quality degradation when evaluated with semantic-composition, dense-instruction, and long-text-rendering benchmarks such as GenEval, DPG-Bench, and LongTextBench. Parallel sampling is a notable exception: by retaining the full-step discretization and removing only the solver's temporal dependency, it can preserve near-lossless quality while accelerating sampling. Building on this observation, we propose \textit{ParaLin++}, a step-parity parallel sampler that preserves the full-step discretization while accelerating the solver iterations. Experiments across Stable Diffusion-v2, LSUN Church, FLUX.1-dev, and Ming-Flash-Omni 2.0 show that ParaLin++ preserves the full-step Euler quality profile at $2.6\times$--$4.8\times$, $1.68\times$ on FLUX, and $1.21\times$ on Ming. Project page: this https URL.

---


### 70. [AIRO: A Streaming-Based Machine Learning Framework for Threat Detection and Security in Industrial Internet of Things](https://arxiv.org/abs/2610.30713)

**<font color=#1a73e8>作者：</font>** Raima Deb, Pranav M Pawar, Mithun Mukherjee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern Industrial Internet of Things (IIoT) im- plementations now connect edge gateways, cloud dashboards and business applications. This improves visibility and remote monitoring. However it simultaneously exposes industrial traffic to various cyber threats including scanning, web attacks and Structured Query Language (SQL) injection (SQLi), phishing- driven credential theft, and command-and-control (C2) activity. Although rule-based tools remain useful for detecting known signatures, their efficacy decreases with minimally altered attacks or when alerts require manual investigation. This paper presents AIRO (Autonomous Intelligence-Driven Cybersecurity Risk Re- duction System), an efficient framework for IIoT monitoring and response. AIRO combines Apache Kafka streaming, attack- specific feature extraction, machine learning (ML) inference, confidence-based decision logic and risk reduction measures such as Internet Protocol (IP) blocking, account suspension and traffic limiting. We developed four specialized datasets for C2 beaconing, reconnaissance, SQLi, and phishing to evaluate AIRO. These datasets include noisy and overlapping characteristic distribu- tions to minimize label leakage. The best-performing models, primarily Gradient Boosting and LightGBM, achieve F1-scores up to 0.9229 while ensuring low-latency from event input to mitigation

---


### 71. [PhyEvolve: Multi-Agent State-Evolution Planning for Physics-Aware Video Generation](https://arxiv.org/abs/2610.30717)

**<font color=#1a73e8>作者：</font>** Yang-Hao Zhou, Lixing Tan, Zhiqi Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in text-to-video generation have substantially improved visual fidelity, yet existing models still struggle to understand the physical evolution implicit in user prompts, making it difficult to generate videos with continuous physical state evolution. Here, we propose PhyEvolve, a multi-agent framework that enhances natural-language prompts through structured state-evolution planning. PhyEvolve consists of three agents: a Director, a Physical Evolver, and a Composer. Given a user prompt and an optional first frame, the Director grounds the scene and disentangles physical events from observation changes. The Physical Evolver uses scene evidence to identify physical mechanisms then constructs causally linked state transitions that unfold throughout the video, whether visible or not. The Composer utilizes these transitions to enhance the original prompts. Without retraining or model modification, PhyEvolve works directly with existing generators through prompt replacement. Extensive experiments on four major benchmarks show that PhyEvolve achieves state-of-the-art performance, outperforming the cutting-edge prior agentic baseline by 7.9 percentage points on average. These results demonstrate that explicit causal state-evolution planning improves physical consistency and state continuity in generated videos through natural-language prompt enhancement.

---


### 72. [Solvable models of learning to pursue a moving target](https://arxiv.org/abs/2610.30721)

**<font color=#1a73e8>作者：</font>** John J. Vastola, Kanaka Rajan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agents tasked with intercepting a moving target must learn how to reach it, ideally as efficiently as possible. As observers of animal pursuit behavior have noticed, different strategies are possible: on one extreme, the agent reactively moves toward the target's current location; on the other, the agent predicts the target's future location and moves directly there. Motivated by the desire to understand how such strategies might be learned, we introduce a continuous-time linear-quadratic model of open-loop target pursuit whose optimal control strategies interpolate between these possibilities. Usefully, a small number of interpretable parameters control which type of strategy is optimal, and it is possible to derive closed-form solutions for optimal strategies, policy learning dynamics, and value learning dynamics. Exploiting our model's linear structure, we find that the time scales of learning precisely correspond to the eigenvalues of certain matrices, and that relevant eigenvalue spectra generically have a gap. We show that this gap indicates that agents tend to learn how to reach their target before optimizing their movement. Our results provide a detailed mathematical characterization of pursuit behavior and its learning dynamics, which can both serve as a benchmark for empirical work, and as a foundation for more elaborate theoretical treatments of pursuit.

---


### 73. [Learning from Next-Frame Prediction: Towards Unified and Scalable Visual Representation Learning](https://arxiv.org/abs/2610.30724)

**<font color=#1a73e8>作者：</font>** Yifeng Yao, Jinghan Li, Zhihao Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video provides a natural source of supervision: what happens next serves as a learning signal for visual world modeling. Yet masked video pretraining focuses on recovering missing content from surrounding context rather than predicting the future from the past. Autoregressive methods instead predict forward one token at a time, but have yet to match joint-embedding methods in representation quality. This gap motivates us to revisit the granularity and space of future prediction. In this work, we introduce VANE, a self-supervised visual pretraining framework built on next-frame prediction in embedding space. A causal encoder summarizes past observations for a state predictor that infers the representation of the entire next frame, making temporal evolution the primary learning signal. This prediction is carried out in a fixed embedding space provided by a frozen semantic tokenizer, emphasizing scene content and structure. To retain fine-grained spatial detail alongside semantic content, a lightweight auxiliary generative decoder reconstructs future-frame patches conditioned on the predicted representations. To unify visual modeling across images and videos, we construct a local-to-global crop sequence for still images, allowing the same encoder to predict newly revealed regions from earlier crops under the same objective. Experiments show that VANE improves with model and data scaling, achieving SOTA on most anticipation, recognition, and dense perception benchmarks among unified encoders. Especially on EPIC-KITCHENS-100 action anticipation, it surpasses V-JEPA 2.1 by 7.1 points in mean-class recall@5. These results demonstrate that next-frame prediction in embedding space is effective and scalable for visual world modeling.

---


### 74. [Width and Depth Limits Commute During Training](https://arxiv.org/abs/2610.30729)

**<font color=#1a73e8>作者：</font>** Ruijia Zhang, Soufiane Hayou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work established that the infinite-width and infinite-depth limits of residual networks commute at initialization when residual branches are scaled by $1/\sqrt{depth}$. In particular, the network output converges to the same limit whether width and depth tend to infinity sequentially or jointly. We extend this commutativity result to training in linear residual networks. Under the same $1/\sqrt{depth}$ residual-branch scaling (Depth-$\mu$P) and the $\mu$P width parameterization, we prove that, for any fixed number of gradient-descent steps with gradient clipping, the network output converges in $L^2$ along every joint width--depth growth path as both width and depth tend to infinity. Consequently, the infinite-width and infinite-depth limits commute throughout any finite training horizon. Without gradient clipping, the corresponding $L^2$ convergence does not hold in general, but we establish the weaker convergence in probability.

---


### 75. [Big World, Little Me: Comparing a First-Person VR Walkthrough Video and Static Slides for Communicating Height-Related Accessibility Barriers](https://arxiv.org/abs/2610.30731)

**<font color=#1a73e8>作者：</font>** Chan In Sio, Alex Mann, Qian Ming Jia 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People with dwarfism and other forms of short stature may encounter barriers created by fixed-height environments and discriminatory social assumptions. This paper evaluates Big World, Little Me, a 10 min 52 s first-person walkthrough recorded from a Unity-based VR environment. The narrative depicts domestic reachability, public-transport, and employment barriers. In a non-randomised between-subjects study, 100 participants aged 15--48 years viewed either the fixed-duration audiovisual walkthrough or a silent, self-paced 27-slide presentation representing the same principal events. Narrative engagement was higher for the walkthrough ($M=5.54$, $SD=0.51$) than for the slides ($M=4.24$, $SD=0.73$), mean difference $=1.30$, 95% CI [1.05, 1.55], Hedges' $g=2.05$, $p<.001$. State empathy was also higher for the walkthrough ($M=3.15$, $SD=0.33$) than for the slides ($M=2.21$, $SD=0.60$), mean difference $=0.94$, 95% CI [0.74, 1.13], Hedges' $g=1.91$, $p<.001$. Exploratory supportive-intention ratings increased more in the walkthrough condition than in the slide condition. Participants also rated the walkthrough as more dynamic, continuous, spatially clear, and information-rich. The findings indicate stronger immediate responses to the complete walkthrough format, but do not isolate the effects of motion, continuity, pacing, information quantity, or participant control. The walkthrough should be understood as screen-based VR-authored media rather than immersive VR or a reproduction of lived experience.

---


### 76. [Do We Need to "Be There" to Say Goodbye? Comparing Participatory Agency and Spatial Presence Across Digital Farewell Formats](https://arxiv.org/abs/2610.30734)

**<font color=#1a73e8>作者：</font>** Chan In Sio, Alex Mann, Qian Ming Jia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Digitally mediated attachment is increasingly common, yet the mechanisms of symbolic closure in hybrid physical--digital relationships remain underexplored. We address an XR design question: how different mediated farewell formats relate to perceived symbolic closure, spatial presence, and bereavement-related emotional intensity. Using "cloud petting" as a controlled proxy of digitally mediated attachment, we compare three farewell formats: (1) lightweight social messaging, (2) a revisitable web memorial, and (3) immersive VR ritual participation. These formats differ in symbolic participation, spatial presence, and sensorimotor ritual enactment. In a mixed-methods study ($N=45$), Website and VR showed significantly higher perceived symbolic closure than Messaging, while the present sample did not detect a significant closure advantage for VR over Website. VR was also associated with significantly stronger grief-related responses on the Pet Bereavement Questionnaire, whereas negative-affect change measured by the Positive and Negative Affect Schedule did not differ significantly across modalities. This pattern motivates a preliminary, exploratory, mechanism-level Agency-Amplification account: formats supporting structured farewell participation were associated with higher perceived closure, whereas the VR format, combining technical immersion, spatial presence, and sensorimotor ritual enactment, was associated with stronger loss-oriented emotional processing. Because the formats also bundled differences in participation, revisitation, technical immersion, and spatial presence, the study provides preliminary design guidance without isolating the causal contribution of any single feature.

---


### 77. [Wavenumber-Aware Deep Learning for Robust Analysis of Raman Spectra](https://arxiv.org/abs/2610.30746)

**<font color=#1a73e8>作者：</font>** Jihwan Kim, Jaeseong Heo, Yujin Kim 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine-learning models for spectroscopy usually treat a spectrum as a fixed-grid intensity vector, leaving the physical coordinate implicit in the array index. Such models are tied to a single sampling grid, spectral range and resolution, which limits their use when measurement conditions change. Here we represent each spectral point as a pair of intensity and wavenumber and compute Transformer positional encodings from the wavenumber itself. On Raman spectra of three bacterial species and their synthetic mixtures, this representation remained robust to noise, sparser sampling and partial spectral coverage across convolutional, residual and Transformer networks. In controlled comparisons, wavenumber-based encoding outperformed index-based and learned encodings under partial observation and retained its performance on sampling grids never seen during training, where index-based encoding degraded. These findings were reproduced on a public 30-isolate bacterial benchmark. Explicit physical coordinates offer a simple route to robust spectral analysis under variable measurement conditions.

---


### 78. [Visualizing and Interpreting Temporal Care Team Dynamics for Cancer Survival Risk Analysis](https://arxiv.org/abs/2610.30748)

**<font color=#1a73e8>作者：</font>** Yuhua Huang, Hsiao-Ying Lu, Kwan-Liu Ma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cancer care is a longitudinal, time-sensitive process requiring coordination among diverse healthcare professionals (HCPs), whose collaboration evolves throughout treatment. Prior studies link care team structure to patient outcomes, but the temporal dynamics of collaboration and their relationship to evolving patient risk remain poorly understood. We introduce a visual analytics framework for modeling and interpreting time-varying care team interactions in oncology. We construct dynamic collaboration networks from electronic health record (EHR)-mediated communication data and use a temporal graph neural network (TGNN) to estimate patient outcome risk over time. We then investigate how changes in care team composition and specialist participation relate to shifts in estimated risk across treatment stages. Our multi-view interactive system combines TGNN-based risk modeling with coordinated visualizations of care team networks, feature-level explanations from a surrogate logistic regression model, and exploratory what-if analysis. Without making causal claims, the system helps analysts examine how risk estimates co-evolve with collaboration patterns and identify care team characteristics associated with these changes. We demonstrate its utility through expert-guided analysis scenarios involving 505 patients with breast, colorectal, and lung cancers, evaluating its ability to reveal clinically meaningful collaboration patterns. This work improves the interpretability of temporal graph-based models in longitudinal, team-based healthcare, with potential applicability to other evolving collaborative settings.

---


### 79. [How Firm Are AI Models' Ethical Boundaries? A Pay-Stub Editing Test of 15 Models](https://arxiv.org/abs/2610.30751)

**<font color=#1a73e8>作者：</font>** Simiao Ren, Xingyu Shen, Tommy Duong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can a small change in wording move an AI model from refusing a sensitive request to acting on it? We test 15 models on the same request to increase the income shown on a pay stub. Across 445 observable trials, models issue editing calls in 14.1% of cases when a loan purpose is stated, 33.1% when the purpose is omitted, and 66.2% when the change is described as fixing a printing error. Astra refuses all ten loan-purpose requests but issues calls in all ten purpose-omitted trials. Fable, Opus, and Muse Spark issue none across all three wordings; Sonnet issues some under the latter two. Response excerpts illustrate different ways of refusing, redirecting, or justifying an edit. The file is a marked test document and all tools are simulated. These results probe how boundaries behave in one setting; they do not prove an overall ethics ranking or that a harmful real-world edit succeeded.

---


### 80. [FilmFlow: Agentic System for 3D Virtual Film Cinematography](https://arxiv.org/abs/2610.30753)

**<font color=#1a73e8>作者：</font>** Yiming Zhang, Jiarui Guo, Haojia Wei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Complex camera motion is central to visual storytelling, yet translating cinematographic intent into controllable, executable camera trajectories remains challenging. We introduce FilmFlow, an agentic framework that converts natural-language instructions or reference videos into explicit camera trajectories for dynamic 3D environments. To generate these trajectories, a Director agent constructs executable camera plans by composing high-level motions from concurrent atomic operations that jointly control translation, rotation, and framing. The Director is supported by three specialized agents: an Interpreter that extracts scene-grounded cinematographic intent, a Scout that selects initial viewpoints, and a Critic that evaluates rendered results and provides visual feedback for iterative plan refinement. We also introduce CinemaBench, comprising 150 Blender scenes from self-created and licensed sources, with five camera instructions per scene for 750 text-directed tasks and 60 reference videos associated with a subset of scenes. CinemaBench supports evaluation of both text-directed camera generation and video reference-directed camera generation. Across a diverse set of evaluated baselines, FilmFlow achieves the strongest benchmark performance and the highest user preference, demonstrating effective spatial reasoning, temporal coordination, and visual composition for executable 3D cinematography.

---


### 81. [Primal-Dual Representation Learning for Low-Rank Constrained MDPs](https://arxiv.org/abs/2610.30756)

**<font color=#1a73e8>作者：</font>** Chenhao Zhou, Chao Zhang, Wensong Bai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Representation learning has substantially improved the efficiency of unconstrained continuous-state Markov Decision Processes (MDPs), but its extension to Constrained MDPs (CMDPs) is difficult because the transition representation must be learned while constraint violation is controlled. In this paper, we study representation learning for low-rank CMDPs with continuous state spaces, and propose REP-PD-TEG for the soft cumulative-violation setting. In the feature learning period, the algorithm interacts with the environment using a decaying-$\epsilon$-greedy mixture execution policy, and uses the collected samples to learn transition features by maximum likelihood. Based on the learned features, it constructs uncertainty bonuses and plans with an optimistic Lagrangian objective to obtain the return policy. We prove regret and soft-violation guarantees for the return policies, and quantify the influence of the decaying-$\epsilon$-greedy exploration. In particular, REP-PD-TEG achieves the optimal $\widetilde O(\sqrt K)$ return policy bound, and gives a $\widetilde O(K^{3/4})$ overall sample bound when exploratory actions are charged. For the stricter hard cumulative violation, where feasibility must be verified episode by episode, we propose REP-PD-H-TEG. It plans under a bonus-corrected lower-confidence utility certificate with the learned representation, and performs a stabilized dual search to obtain the return policy, yielding regret and hard-violation bounds. Together, these results give the first theoretically guaranteed representation-learning method for low-rank continuous-state CMDPs with both soft cumulative guarantees and certified hard-violation control.

---


### 82. [Can Loan Processors and Underwriters Spot AI-Edited Statements? An Empirical Study](https://arxiv.org/abs/2610.30758)

**<font color=#1a73e8>作者：</font>** Simiao Ren, Xingyu Shen, Tommy Duong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI-assisted editing can produce loan documents that preserve familiar issuer layouts while changing the applicant's identity. We investigated whether experienced underwriters and loan processors identify such forgeries in first-pass, document-only review. Three practitioners recruited through Upwork each received one applicant package drawn from 134 forged PDFs derived from 47 genuine financial documents supplied with full consent. The edits preserved amounts, dates and balances; identifier inconsistencies introduced by the pipeline were knowingly retained before distribution. Reviewers were not told that files had been altered and returned 132 file-level judgements. Checking their explanations against the originals yielded 14 edit-supported concerns (10.6%): 12 Suspicious judgements and two Insufficient information judgements. All supported concerns involved identifier disagreements within or across documents, and no reported visual cue identified an actual edit. Thus, approximately one in ten judgements contained evidence of the forgery, despite known inconsistencies remaining in the files. These observations motivate evaluating consistency checks and independent source verification alongside human review. With three reviewer-package pairs and no genuine-file controls, the findings describe this exploratory setting rather than population-wide detection accuracy.

---


### 83. [Adaptive Deadline- and Energy-Aware Caching Algorithms in Dynamic Multi-UAV Edge Networks](https://arxiv.org/abs/2610.30768)

**<font color=#1a73e8>作者：</font>** Jian Kim, Ki-Il Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Content caching via unmanned aerial vehicles (UAVs) becomes one of the solutions to maintain content delivery when terrestrial infrastructure is unavailable or disrupted. However, existing caching approaches often focus primarily on cache-hit performance or average delivery delay, without jointly addressing spatially heterogeneous and time-varying demand, content-specific deadlines, and uneven communication-energy consumption across UAVs. To address these challenges, we formulate a dynamic deadline- and energy-aware cache placement and replacement problem that jointly considers deadline misses, UAV-side communication energy, and inter-UAV energy imbalance. To achieve this, we first develop deadline- and energy-aware UBAC (DE-UBAC), an interpretable hierarchical rule-based realization that incorporates deadline-aware prioritization, cooperative placement, energy-aware coordination, and cache-update cost. However, predefined priorities and thresholds limit its adaptability under dynamically coupled network conditions. We therefore propose GRU-assisted Deadline- and Energy-aware Proximal Policy Optimization (GRU-DEPPO), which combines local and global GRU-based temporal representations with a centralized PPO actor-critic for adaptive cache placement and replacement. Simulation results show that GRU-DEPPO achieves the lowest deadline-miss rate and total UAV-side communication energy among the considered schemes. Compared with DE-UBAC, GRU-DEPPO reduces the deadline-miss rate by approximately 61% and inter-UAV energy imbalance by approximately 40%.

---


### 84. [Evaluation of Front-End Feature Matching for Lunar Visual SLAM](https://arxiv.org/abs/2610.30774)

**<font color=#1a73e8>作者：</font>** Guillem Casadesus Vila, Grace Gao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lunar rovers will primarily rely on cameras for localization until navigation satellite services are deployed, and will continue to need them afterwards for relative navigation, hazard detection, and surface operations. Visual odometry (VO) and Simultaneous Localization and Mapping (SLAM) mostly estimate motion by matching features between frames. However, feature matchers are developed on urban, indoor and driving scenes, planetary studies compare them on orbital registration or within complete SLAM systems, and real lunar imagery with reference poses is scarce, so matching between rover frames on low-texture, harshly lit terrain, and its effect on VO, has not been compared. We benchmark eleven classical and learned detector-matcher combinations on nine synthetic, lunar-testbed, and terrestrial-analogue datasets, and a feature tracker, scoring pairwise pose accuracy against baseline and the trajectory error of the resulting VO. Under a common rotation-only metric, the SuperPoint pairings outperform SIFT with ratio-tested FLANN matching on both lunar testbeds and one analogue site, with smaller or unresolved differences on synthetic data. When rotation and translation direction are scored jointly, this SIFT pairing exceeds both SuperPoint pairings on four synthetic datasets, so synthetic results alone do not establish relative performance on real rover imagery. In stereo VO, the SuperPoint pairings are not consistently more accurate than SIFT, but only they keep tracking on all eight sequential datasets. Pairings with classical detectors depend on lighting while SuperPoint changes little: a low spotlight makes them more accurate than diffuse light on the same testbed views, consistent with more contrast and detected keypoints. SuperPoint with LightGlue is the fastest learned combination (16 ms per frame), and DINOv2 retrieval proposals still need geometric verification.

---


### 85. [Where meanings converge and diverge: Revisiting linguistic relativity across 81 languages](https://arxiv.org/abs/2610.30778)

**<font color=#1a73e8>作者：</font>** Weiran Wang, Wenjuan Qin, Haitao Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Do people who speak different languages organize concepts in similar ways? This question lies at the heart of the Sapir--Whorf hypothesis and debates about linguistic relativity. Shared basic meanings, however, need not imply shared relations among them. We compared relations among 196 basic concepts across 81 languages, using word embeddings from two multilingual models to quantify conceptual structure expressed in language. Cross-language correspondence was greater for sociocultural meanings than for meanings concerning nature and motion, a contrast recurring across models and classifications. Within the sociocultural domain, relational differences increased with geographic separation; less closely related languages differed more across all domains. These findings suggest that universality and relativity are interwoven across conceptual domains. They inform an account in which shared cognitive resources interact with linguistic and local experience, and predict greater cross-language correspondence in human semantic judgments for sociocultural than for nature and motion meanings.

---


### 86. [DeXplicit: Making Physical State Explicit in Dexterous Manipulation World Models](https://arxiv.org/abs/2610.30781)

**<font color=#1a73e8>作者：</font>** Adam Lee, Mutian Xu, Yukang Cao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Before acting on an object, a robot needs to anticipate how its hand motion will change the physical world and what the resulting scene will look like. Existing approaches typically entangle action-conditioned dynamics, camera motion, and visual synthesis within a video generation model, or represent dynamics as point trajectories without explicit object structure. We introduce DeXplicit, a dexterous manipulation world model that instead predicts how the world evolves explicitly in metric 3D before rendering its visual consequences. Given an initial scene and a future hand trajectory, a lightweight 3D dynamics network predicts object-centric motion and deformation, providing structured and geometrically grounded future world states. These predictions then serve as a strong scaffold for video generation: appearance is transported through the predicted 3D motion and projected into future views, allowing the renderer to focus on completing uncertain and newly visible content rather than implicitly learning world dynamics from pixels. This explicit-3D-first decomposition also enables efficient causal generation, requiring only two denoising steps per block while conditioning on generated history.
Across HOT3D, OakInk2, and PhysTwin, DeXplicit reduces moved-point error by 27-40% relative to PointWorld and improves object fidelity IoU+ by 47% on HOT3D under a shared renderer. Our design with two-step causal generation achieves a 57x speedup from our 14B bi-directional configuration in video synthesis.

---


### 87. [An Introduction to World Models for Generalist Agents](https://arxiv.org/abs/2610.30789)

**<font color=#1a73e8>作者：</font>** Zhihui Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models have recently emerged as a promising direction toward developing generalist agents capable of understanding, predicting, and interacting with diverse environments. However, despite growing interest, the concept of a world model remains loosely defined, encompassing approaches ranging from predictive dynamics models and learned simulators to models that jointly generate future observations and actions. This introductory paper aims to clarify the concept of world models and provide a unified perspective on their role in developing generalist agents. Starting from the partially observable Markov decision process (POMDP) framework, we connect world modeling to classical control, dynamical systems, signal processing, and reinforcement learning. We introduce different approaches to world modeling, emphasizing the knowledge they capture, their learning objectives, and how they support decision-making. We further explore the relationship between world modeling and policy learning, highlighting how these capabilities can be unified through conditional prediction without requiring separate models. Rather than offering an exhaustive survey of existing methods, this paper focuses on fundamental concepts, modeling principles, and connections, with the goal of providing an accessible and unified introduction to world models for generalist agents.

---


### 88. [Trace2World: Reconstructing App Worlds from Real Interaction Traces for Scalable GUI Agent Training](https://arxiv.org/abs/2610.30792)

**<font color=#1a73e8>作者：</font>** Zezhou Wang, Hanzhang Zhou, Panrong Tong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling GUI reinforcement learning requires environments that preserve real-app behavior. Yet coupling behavior inference with coding can turn partial traces into runnable mocks with incorrect state transitions. We introduce \textbf{Trace2World}, which separates global behavior reconstruction from implementation. It reconciles traces into a shared, source-linked app model, then compiles an executable environment. Independent replay of source workflows localizes mismatches for bounded implementation repair. Validated worlds then support learner-adaptive task and environment augmentation within source-supported behavior. From 1,570 traces, Trace2World constructs 50 environments. On 200 workflows across ten apps, 91.1% are reproduced end to end, versus 59.8% for the strongest matched task-local baseline. Source-grounded validation retains 94.0% of simulated training gains on real devices, versus 54.7% under self-validation. Learner guidance raises benchmark success from 56.9% to 61.1%. Training in Trace2World further improves the model by 20.2 points on our benchmark, 5.4--16.2 points across four external GUI benchmarks, and 16.3 points on 100 real-device tasks. Reliable reconstruction separates what behavior source evidence supports from whether the implementation preserves it.

---


### 89. [WovenAnchor Matcher: Specialized Intra- and Inter-Image Context Modeling for Feature Matching](https://arxiv.org/abs/2610.30799)

**<font color=#1a73e8>作者：</font>** Zhiyang Li, Ruijiang Jin, Thibaut Klenke 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semi-dense local feature matching commonly aggregates contextual information before coarse-to-fine correspondence estimation. However, intra-image and inter-image aggregation serve different roles: the former should propagate spatial evidence within each image while retaining structured two-dimensional dependencies, whereas the latter should gather information from plausible corresponding regions while limiting noise from unrelated locations. We propose WovenAnchor Matcher (WAM), a semi-dense matching framework based on role-specialized context aggregation. WAM introduces two complementary operators. WovenMamba performs intra-image aggregation through horizontal-then-vertical state-space propagation, allowing vertical updates to operate on horizontally contextualized features and thereby encouraging a structured two-dimensional receptive-field bias. AnchorCrossAttention performs inter-image aggregation by using cross-attention to gather context from plausible corresponding regions across the image pair. It performs this exchange over local representative anchors that aggregate feature evidence within each window. On MegaDepth, WAM achieves 66.1 pose AUC@5$^\circ$, improving on the JamMa baseline by 2.0 AUC points under the same evaluation setup. Ablations show that removing or replacing either specialized component reduces accuracy, providing evidence that intra-image propagation and inter-image retrieval benefit from role-specific aggregation designs. Code and pretrained weights are available at this https URL.

---


### 90. [A Computationally Efficient and Rate-Optimal Algorithm for Adversarial Linear MDPs with (Aggregate) Bandit Feedback](https://arxiv.org/abs/2610.30801)

**<font color=#1a73e8>作者：</font>** Haolin Liu, Chen-Yu Wei, Hanbin Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study episodic linear Markov decision processes with unknown transitions, adversarial losses, and bandit feedback. The state-of-the-art result for this setting (Liu et al., 2024) either achieves $\sqrt{K}$ regret with a computationally inefficient algorithm or achieves suboptimal $K^{3/4}$ regret, where $K$ is the number of episodes. Our work gives the first $\sqrt{K}$ regret with a polynomial-time algorithm. Our method reduces adversarial linear MDPs to adversarial linear bandits whose action set consists of policies' expected feature vectors. The central challenge is that this action set is unknown and can be estimated only through exploration. We address this challenge by constructing an approximate separation oracle for the action set that either generates executable policies from queried features, or refines an outer approximation of the action set. This approach draws inspiration from the reduction of van Erven et al. (2025) for linear contextual bandits and the oracle-efficient linear bandit algorithm of Ito et al. (2019), but additionally deals with the imprecision of the oracle. The resulting algorithm requires only aggregate loss feedback, and to our knowledge. This is the first polynomial-time algorithm for adversarial MDPs with aggregate feedback beyond the tabular case.

---


### 91. [Is spectral predictability enough? Testing Ω-matching for synthetic pretraining under distribution shift](https://arxiv.org/abs/2610.30802)

**<font color=#1a73e8>作者：</font>** Edric Castel C. Hao, Juan Raphael S. Seña, Neon S. De Jesus  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic pretraining under distribution shift requires deciding what synthetic data to use. A natural criterion is to match the spectral predictability $\Omega$ of the source to the target, but is $\Omega$ sufficient? We test this hypothesis, which we call predictability-aware pretraining, across three architectures (LSTM, PatchTST, TCN) and three seeds. Under ideal synthetic-to-synthetic conditions, $\Omega$-matched pretraining can outperform even an oracle baseline (+46.8% MSE reduction, LSTM), though the benefit is already architecture-dependent. On the real-world ETTm1 benchmark, however, this relationship does not hold: sine-plus-noise pretraining at matched $\Omega$ yields only a marginal mean improvement +2.3% averaged over all three architectures, up to +65.5% on individual channels), whereas $\Omega$ matched chaotic ODE trajectories systematically degrade performance -13.2%). The two sources agree on the direction of transfer for only 53% of configurations across all three architectures (Pearson r=-0.02), indicating that $\Omega$ carries little information about which source will transfer beneficially. We further observe an architecture-dependent asymmetry in the response to the direction of the $\Omega$ gap. We conclude that $\Omega$ matching can help in controlled settings but is not sufficient to predict transfer across sources, and we discuss additional signal properties that a source-selection criterion may need to consider.

---


### 92. [What Lies Beyond Perception: A Partition Theory of the Limits of AI Evaluation and Oversight](https://arxiv.org/abs/2610.30803)

**<font color=#1a73e8>作者：</font>** Ahmed M. Mahran  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Replacing the judge can move a benchmark score, and models can be trained to hide capabilities. Both put the evaluator in question: what can it certify? We develop a partition theory of evaluation from one principle: judgement is bounded by perception. An agent's discrimination is the partition of its inputs into classes it cannot tell apart. Discrimination is necessary for capability but not sufficient, so bounds on it bear directly on whether evaluation can show that a model lacks an ability. We prove a one-sided bound. An examinee whose partition refines its evaluator's has the discrimination to pass every test the evaluator can grade, provided each input has an acceptable reply. We define the echo test, which accepts any reply the evaluator perceives as identical to the input, and show that it is complete for the tests the evaluator can grade. Passing therefore certifies at most a floor on discrimination, never a ceiling, and only a sharper evaluator can raise it. Used to detect concealment, echo-test failure points the wrong way: under exhaustive probing it flags every honestly weaker examinee and no concealer that presents as the evaluator's peer. Exact imitation of a weaker model is undetectable by any behavioural evaluator. We extend the bound to ensembles of monitors and to channels a model controls, explain published findings on judge disagreement and sandbagging, and derive testable predictions. A safety case that argues from behavioural evaluation alone that a model lacks an ability must assume the model's cooperation.

---


### 93. [One Evaluation Is Enough: Inversion-Free Image Editing with Trajectory Correction](https://arxiv.org/abs/2610.30827)

**<font color=#1a73e8>作者：</font>** Lifan Jiang, Taiyang Chen, Senlin cheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-image editing commonly relies on inversion and iterative sampling, while efficient one-step editors often stabilize a large update by estimating and averaging editing fields at multiple noise levels. We ask a stricter question: is a single temporal field evaluation sufficient for reliable inversion-free editing? Our answer rests on a previously underused duality in a variance-preserving (VP) one-step model: one source-target query at a shared noisy state simultaneously determines a local angular semantic tangent and a clean endpoint displacement. We integrate the tangent over the analytically known remaining VP angle to obtain a nominal one-step transport, and use the endpoint displacement to correct its long-horizon extrapolation through a constrained projection. This transport-first, correction-second construction yields Endpoint-Calibrated Transport (ECT), a closed-form, training-free editor requiring only one noise level, two text conditions packed into one denoiser batch, and one latent update. ECT requires no image inversion, trajectory integration, second temporal observation, or iterative optimization, and can be directly applied to pretrained epsilon-prediction VP one-step generators. Across the reported benchmark settings, ECT delivers stable gains in editing quality within an extremely short editing time.

---


### 94. [Semi-Linear Gaussian Bayesian Networks: Enhancing Flexibility in Node Dependencies via penalized B-Splines](https://arxiv.org/abs/2610.30838)

**<font color=#1a73e8>作者：</font>** Aitor Oviedo-Madrid, Mabel Morales-Otero, Jose Gonzalez-Gomariz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Bayesian networks for continuous variables often rely on restrictive assumptions: linear Gaussian models lack flexibility to capture nonlinear dependencies, while non-parametric approaches provide greater flexibility at a high computational cost. This creates a gap for modeling scenarios where variables are approximately Gaussian but exhibit nonlinear relationships. We introduce Semi-Linear Gaussian Bayesian Networks (SLGBN), a novel class of continuous Bayesian networks designed to bridge this gap, preserving Gaussian conditional distributions while introducing nonlinear conditional mean functions. The proposed framework provides a unified probabilistic framework combining linear Gaussian and nonlinear Gaussian conditional models within the same Bayesian network Nonlinear conditional mean functions are estimated using generalized additive models (GAMs) with penalized B-splines. We present parameter estimation procedures for both types of nodes, as well as a greedy hill-climbing algorithm for learning the network structure under the SLGBN framework. To assess its performance, we compare SLGBN with other continuous Bayesian network models, including semiparametric Bayesian networks (SPBN) and Linear Gaussian Bayesian networks (LGBN). Experimental results evaluate both goodness of fit and the ability to recover the underlying network structure. The results show that, in the presence of nonlinear Gaussian relationships, SLGBN achieves better fit and improved structure recovery compared to alternative models, particularly when combined with the Extended Bayesian Information Criterion (EBIC*) score. Furthermore, by retaining Gaussian conditional distributions, SLGBN offers computational advantages over fully semiparametric approaches.

---


### 95. [Bifurcations from Weight Space: JEPAWG on Parametric Dynamical Systems](https://arxiv.org/abs/2610.30847)

**<font color=#1a73e8>作者：</font>** Tobias Göbel, Miranda C.N. Cheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Trained network weights are increasingly treated as data, but there is rarely ground truth about what a population of models should encode, which hampers systematic validation of weight-space methods. This makes parametric dynamical systems a natural test-bed: the dynamics change qualitatively at submanifolds of parameter space that are, in well-studied families, known analytically or numerically. Fine-tuning a forecasting network at each point of a parameter grid yields a model zoo indexed by a physical parameter, against which weight-space diagnostics can be checked.
We build such model zoos for four dynamical systems and analyse them with JEPAWG, a recently proposed joint-embedding hypernetwork built around a learned parameter--weight representation. It was first introduced for neural samplers for lattice field theories, where its latent geometry located the phase transition and estimated the 2D Ising critical exponent. Applied to dynamical systems, JEPAWG is competitive on forecasting with a hypernetwork trained directly for that task, despite being supervised on the parameter--weight correspondence rather than on forecasts. Beyond forecasting, the norm of the parameter-derivative of the decoded weights locates Hopf points and curves, tracks a period-doubling cascade closely enough to give a qualitative estimate of the Feigenbaum constant, and detects a global bifurcation, which has no eigenvalue signature and is therefore invisible to linearisation. As such, JEPAWG provides interpretable insight into the dynamics that is not available from other hypernetworks. Together, these results indicate that JEPAWG is a workable instrument for reading physical structure off a population of trained networks.

---


### 96. [ADAPT for Science: A Multi-Agent System for Self-Evolving Scientific Optimization](https://arxiv.org/abs/2610.30851)

**<font color=#1a73e8>作者：</font>** Zhaoran Feng, Yuchen Ni, Jianan Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific discovery often requires identifying a small number of high-performing designs in vast, constrained search spaces. This is difficult when evaluations are costly, feasible solutions are sparse, parameters are strongly coupled, and physical constraints are strict. Recent AI for AI methods can automatically improve algorithms and optimization procedures. However, general purpose approaches are not designed around scientific priors, physical constraints, and limited evaluation budgets. We introduce ADAPT for Science, a multi-agent framework that treats scientific optimization as two coupled decisions: where to search and how to search. ADAPT uses historical designs to identify promising and diverse initial conditions, progressively concentrates computation on favorable search directions, and evolves the optimization procedure from execution feedback. We evaluate ADAPT on the design of gravitational wave detectors using a differentiable physics simulator and eight unseen detector topologies. Under matched scientific evaluation budgets, ADAPT achieves a mean loss of 0.204 +/- 0.101, reducing loss by 54.9% relative to the best classical optimizer and by 62.2% relative to the best general purpose agentic evolution baseline. ADAPT achieves the lowest loss on all unseen topologies among the evaluated baselines. ADAPT provides a step toward scientific optimization systems that continuously learn from prior experience and their own search outcomes.

---


### 97. [Training Mixed-Monotone Neural Networks for Verification Without Set Propagation](https://arxiv.org/abs/2610.30853)

**<font color=#1a73e8>作者：</font>** Jonas Fingerhut, Lukas Koller, Matthias Althoff  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most formal verification approaches for neural networks conservatively enclose the output set of the neural network. However, computing a tight output enclosure is in general computationally hard. We sidestep this challenge with a novel neural network architecture that realizes mixed-monotone functions as the difference of monotone subnetworks. By utilizing the theory on mixed-monotone systems, this reduces the computation of a tight output enclosure from complicated set propagation to two simple forward passes of opposite corners of an input interval. Moreover, because the size of the resulting enclosure is a closed-form function of the weights of the neural network, we can directly minimize it during training. We prove a lower bound on the size of any such enclosure, given by the total variation of the represented function generalized to several inputs, which makes it possible to compare the tightness of the enclosure against the optimum. Our evaluation on regression and dynamical-system benchmarks demonstrates that our training reduces the enclosure size to within 0.5% of the lower bound without sacrificing prediction accuracy. Computing our enclosure is orders of magnitude faster than CROWN and $\alpha$-CROWN and on deep networks it is also tighter than zonotope propagation and CROWN, while its size exceeds that of $\alpha$-CROWN by only 5.1%.

---


### 98. [CAVC: Convergence-Adaptive Audio-Visual Cache for Modality-Asymmetric Diffusion Generation](https://arxiv.org/abs/2610.30854)

**<font color=#1a73e8>作者：</font>** Lifan Jiang, Yibo Zhao, Senlin cheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based audio-visual generation methods typically perform joint denoising of audio and video latents throughout the entire sampling trajectory, repeatedly executing modality-specific denoising branches and cross-modal attention at every timestep. However, we observe that such uniform joint computation is not always necessary. The key is a modality-asymmetric recoverability: audio-side drift introduced by mid-stage caching can be substantially reduced by only a few terminal joint denoising steps, whereas video-side degradation caused by caching leads to persistent loss of motion and temporal details. This asymmetry suggests that inference acceleration should selectively cache recoverable audio-side computation while preserving full video refinement. Motivated by this observation, we propose \textbf{Convergence-Adaptive Audio-Visual Cache (CAVC)}, a training-free modality-asymmetric caching framework. CAVC adopts a sandwich-structured computation allocation: after detecting that audio denoiser outputs enter a cache-tolerant regime, it caches and reuses the audio denoiser output to bypass audio denoising and cross-modal attention in the middle stage, while the video branch continues independent spatio-temporal refinement; a few joint steps are then restored at the end to reduce accumulated cross-modal drift and improve synchronization. Experiments across multiple public benchmarks demonstrate that CAVC achieves 1.10--1.35x wall-clock acceleration, improves several visual dynamics and temporal statistics, and maintains competitive audio fidelity and audio-visual alignment.

---


### 99. [Direct Forcing: A Single-Stage Training Recipe for Few-Step Autoregressive Text-to-Video Generation](https://arxiv.org/abs/2610.30861)

**<font color=#1a73e8>作者：</font>** Haojun Xu, Jie Huang, Xin Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step autoregressive video generation enables low-latency streaming, yet prevailing training pipelines separate causal adaptation from distribution matching. Recent representation-based text-to-video methods retain this separation by starting from ODE-initialized checkpoints, even when the target distribution is defined directly by reference videos. We introduce Direct Forcing, a single-stage framework that uses reference videos both as paired examples of how a history continues and as a target population for self-generated rollouts. Causal Continuation Alignment learns paired spatiotemporal correspondence under reference histories, while Rollout Distribution Matching uses maximum mean discrepancy to align the representation distributions of self-generated and reference videos. Together, these complementary signals allow a pretrained video model to learn causal continuation and the target video distribution in a single training stage. Dynamic Gradient Balancing adapts the relative gradient contributions of continuation alignment and distribution matching during training. Starting from bidirectional Wan2.1-1.3B, Direct Forcing learns a four-step autoregressive generator in 250 updates without a separate initialization stage or online diffusion-score supervision, achieving 84.63 VBench Total and 86.01 Quality. Ablation studies further demonstrate the benefits of dynamic gradient balancing and reveal distinct representation preferences: deeper features benefit continuation alignment, whereas intermediate features yield better performance for rollout distribution matching.

---


### 100. [Cross-Spectral Feature Fusion for Multispectral Document Binarization](https://arxiv.org/abs/2610.30863)

**<font color=#1a73e8>作者：</font>** Yasas Savinda, Maheshi Buddhinee Dissanayake  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Historical document binarization remains challenging when faded ink, bleed-through, and background degradation exhibit wavelength-dependent behavior across visible and near-infrared observations. This study investigates whether adaptive cross-spectral feature fusion and targeted structural guidance can improve multispectral document binarization beyond fixed fusion and generic attention mechanisms.
Four registered SMADI bands at 500, 600, 700, and 1000 nm are processed using a multi-branch conditional generative adversarial network (cGAN). Visible, NIR, and structural feature streams are fused at encoder depth L = 3 using spatial- and channel-wise softmax gating, while auxiliary edge maps derived from selected VIS-NIR band pairs provide targeted structural guidance. Nine controlled fusion and structural configurations are evaluated using five-fold document-level cross-validation, DIBCO-standard metrics, and Holm-corrected statistical testing.
The F3 + NIR edge-guided configuration provides the strongest overall performance among the evaluated models, achieving mean F1 = 0.7916, p-FM = 0.8044, and IoU = 0.6654. Relative to the fixed Mid AVG baseline, it improves F1 by 0.0269, p-FM by 0.0360, and IoU by 0.0321, with all three gains remaining statistically significant after Holm correction. Mean NRM and DRD are also reduced, although these reductions are not statistically significant after correction.
Targeted cross-spectral structural guidance provides an effective mechanism for regulating intermediate multispectral fusion, improving primary foreground-overlap performance while retaining the complete four-band observation.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-211](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
