# 📦 其他研究 | 2026年11月02日

> 本类共 **432** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-432](./part-09.md)

---

### 301. [Smartphone Indoor Localization Enhanced by Hierarchical Multi-Sensor Context Recognition](https://arxiv.org/abs/2610.39691)

**<font color=#1a73e8>作者：</font>** Wenhui Feng, Muhan Weng, Jianyu Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Smartphone indoor localization requires low-cost, robust positioning across scene transitions and phone-use variations. Pedestrian dead reckoning (PDR) enables infrastructure-free deployment but accumulates errors from heading drift, structural transitions, and carrying-mode changes. Existing methods often treat contextual cues as a single event stream or local correction signal, limiting their ability to address distinct localization errors. This paper presents a framework enhanced by hierarchical multi-sensor context recognition. A jointly data- and model-driven recognition model predicts environment, scene, and activity probabilities, which are converted into scene-event and action-context segments. Scene-event segments guide scene-constrained PDR correction through corridor heading constraints, landmark attraction, fixed-lag backtracking, and vertical-transition handling. Action-context segments drive action-aware RoNIN-based position compensation for carrying-mode-dependent drift. Experiments on cross-floor and multi-action trajectories against LiDAR-SLAM references show that the proposed framework outperforms PDR and representative learned inertial odometry baselines, demonstrating that hierarchical semantics provide reliable, localization-specific correction cues.

---


### 302. [DEQ-Stereo: Deep Euilibrium Video Stereo Matching via Adaptive Convergence](https://arxiv.org/abs/2610.39701)

**<font color=#1a73e8>作者：</font>** Kiljoon Han, Kyumin Hwang, Wonheok Choi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Iterative refinement models have significantly improved stereo matching accuracy, but their rigid, fixed update schedules incur heavy computational costs and a strict trade-off between speed and accuracy. This challenge is magnified in video streams, where traditional online methods resort to reducing feature channels or relying on expensive temporal warping. To address this, we propose \textbf{DEQ-Stereo}, a novel video stereo matching framework based on the Deep Equilibrium (DEQ) paradigm. Instead of unrolling a fixed number of iterations, DEQ-Stereo reformulates the refinement as an implicit fixed-point problem, adaptively terminating once convergence is met. To ensure fast and stable intra-frame convergence, we introduce the \textbf{Convolutional Simplified Gated Unit (ConvSGU)}, which eliminates unnecessary non-linearities by modeling the latent state as a gated, element-wise sum of inputs. Furthermore, to exploit cross-frame temporal coherence, we propose \textbf{Temporal State Transfer (TST)}, a warm-start strategy that propagates the converged hidden state to the next frame without requiring explicit pose or warping priors. Extensive evaluations demonstrate that DEQ-Stereo delivers state-of-the-art performance with a superior accuracy-to-latency trade-off.

---


### 303. [Confidence Filtering in Video-Based Gait Assessment: Measurement Error versus Selection Shift](https://arxiv.org/abs/2610.39704)

**<font color=#1a73e8>作者：</font>** David Regev, Eran Beeri Bamani  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video-based gait assessment often keeps only high-confidence pose observations, which can lower measurement error but change the movement assessed. We compared confidence selection with budget-matched random selection in a Parkinson-related cohort (n = 96) and an NF2-related replication cohort (n = 18). In the Parkinson-related cohort, confidence selection produced a small but consistent shift in the observed movement summary (+0.05 SD, 95% CI 0.03 to 0.07), while held-out Mini-BESTest error stayed flat (-0.04 points, -0.13 to 0.05); a policy preserving motion-group proportions reduced the shift, while NF2 showed no shift and its predictor did not beat a constant baseline. Because this shift mixes measurement error with selection shift, we decompose and simulate both on the cohort's window structure. Filtering lowers local error when error depends on confidence, but biases the endpoint once confidence tracks movement more than error. In the Parkinson-related data, confidence was only weakly tied to movement (rho = 0.14). There, filtering is harmless if well-tracked windows are unbiased. If instead systematic error only redistributes within participants, filtering can add up to 0.58 degrees. Unchanged clinical error from such small-cohort predictors therefore cannot show that quality filtering preserves the assessed movement.

---


### 304. [NIF: Normal-Intersection Fields for Geometrically Consistent Oriented Box Refinement](https://arxiv.org/abs/2610.39715)

**<font color=#1a73e8>作者：</font>** Shaokai Zheng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate oriented detection requires a box to follow object boundaries, yet a standard regression head predicts its center, size, and angle from a pooled region representation. Small errors in these coupled parameters can displace long boundaries even when the object is correctly classified. We propose NIF, a refinement module that replaces an additional box regressor with normal-intersection fields. Given a coarse oriented box, the module observes local features at 20 boundary anchors and predicts signed distances along their outward normals. These observations admit an exact affine representation in five geometric variables. A differentiable, reliability-weighted least-squares fit projects the predicted field onto this representation and analytically recovers a refined rectangle. Tangential pooling preserves the normal position profile, while shared projection limits the added network to 0.132M parameters. On DOTA-v1.0, NIF reaches 78.00%, 79.11%, and 79.02% mAP with Oriented R-CNN, LSKNet-S, and Strip R-CNN, respectively, achieving the highest single-scale SOTA result in Table 1. It reaches 68.19% on DIOR-R, improves matched FAIR1M/DIOR-R baselines by 0.30/0.68%, and raises HRSC mean IoU from 0.867 to 0.888 while reducing field error by 24.5%. Across four different detector frameworks with the detectors frozen, relative AP75 improves by 1.57-4.18% and COCO-style mAP by 0.42-3.74%, without detector retraining. Code is available at this https URL.

---


### 305. [Implicit Bias of (Stochastic) Gradient Descent on Deep Linear Diagonal Networks](https://arxiv.org/abs/2610.39717)

**<font color=#1a73e8>作者：</font>** Wiebke Bartolomaeus, Holger Rauhut  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern machine learning models are often overparameterized, i.e., have more parameters than training data. This typically implies that the loss function admits multiple minimizers so that training methods (and their hyperparameter choices) have significant influence on the computed solution. We study this so-called implicit bias phenomenon in the context of training deep linear diagonal networks. Previous work has shown that the gradient flow for learning such networks converges to (almost) sparse solutions when initialized small. For an arbitrary number of layers, we extend this analysis to the practically more realistic (stochastic) gradient descent iterations. Our approach identifies (stochastic) gradient descent as a perturbed (stochastic) mirror gradient descent. This allows us to establish convergence and characterize the limiting solution, relating it to weighted $\ell_1$-minimization. Moreover, we provide sufficient conditions on the step sizes and quantify the influence of the step sizes on the implicit bias.

---


### 306. [WorldProbe: When Video World Models Fall Apart under Long-Horizon Spatial Exploration](https://arxiv.org/abs/2610.39721)

**<font color=#1a73e8>作者：</font>** Minqi Wang, Jie Peng, Hejun Dong 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models generate future visual observations from camera or action inputs, with the goal of synthesizing persistent 3D worlds that can be explored across time and space. Existing benchmarks typically evaluate short interactions or rely on camera trajectories fixed before generation. The performance of video world models under long-horizon exploration with extensive camera motion remains under-explored. We introduce WorldProbe, a diagnostic benchmark that uses a goal-conditioned multimodal agent to adapt camera actions online during generation. WorldProbe comprises 164 test cases across four probing families. Across 10 state-of-the-art models, we generate more than 1,600 rollouts totaling approximately 800 minutes, with horizons up to 180 seconds. Our evaluation across four dimensions reveals both the degradation of local measures and the emergence of long-range inconsistencies. We find that recent models sustain visual and content quality for longer, while long-range memory and evolution remain weak. These results expose a gap between locally stable generation and persistent world consistency that is largely missed by existing benchmarks. Code and benchmark resources are available at this https URL.

---


### 307. [Cross-Encoder Anchor Refinement for Zero-Shot Anomaly Detection](https://arxiv.org/abs/2610.39727)

**<font color=#1a73e8>作者：</font>** Kaisong Ji, Ziyang Xu, Chang Bian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot anomaly detection aims to transfer anomaly discrimination from auxiliary training domains to unseen categories while localizing subtle defects. A key challenge is to construct discriminative references that combine contextual representations with complementary local evidence. We present Cross-Encoder Anchor Refinement (CEAR), which connects two visual encoding paths for the same image at the anchor stage, before normal and anomalous prototypes are constructed. An independent convolutional encoder pretrained for industrial product recognition builds an image-specific memory shared across selected vision transformer (ViT) layers. Spatial anchors read from ViT patch features query this memory through cross-attention and undergo residual refinement. Image-conditioned normal and anomalous queries then gate anchor aggregation to construct prototypes for anomaly scoring. Across 13 industrial and medical datasets, CEAR achieves the best performance in 57 of 68 evaluations spanning image-level detection and pixel-level localization. Notably, CEAR surpasses all other state-of-the-art methods in 41 of 44 pixel-level comparisons. Across 11 localization datasets, mean gains in pixel-level maximum F1 score and average precision are 4.45 and 3.79 percentage points, respectively. This study shows how cross-encoder interaction at the anchor stage can integrate complementary visual representations for fine-grained anomaly localization across domains.

---


### 308. [Grounding Predictive Reliability through Masked Observability](https://arxiv.org/abs/2610.39728)

**<font color=#1a73e8>作者：</font>** Shang Gao, Bernhard Sick, Franz Götz-Hahn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An uncertainty estimate is meaningful only if its semantics can be tied to observable predictive behavior. Normal-Inverse-Gamma (NIG) evidential regression provides a structured decomposition of predictive variability into data-scale and predictive-mean components, but marginal likelihood does not identify their allocation. We address this semantic ambiguity in masked representation learning. MORSE (Masked Observability for Reliable Structured Encoding) predicts the same hidden target under controlled changes in visible context and uses normalized cross-context variation to ground predictive-mean uncertainty, while a Gaussian objective learns the conditional mean and data scale. The normalized variation plays the role of the NIG factor $1/\nu$, which the marginal leaves unidentified; this yields a policy-relative observability variance that measures dependence on visible evidence, distinct from variation induced by resampling the training set. On a Gaussian-process benchmark with a contextual reference built from analytic Bayes conditional means, MORSE has the lowest log-variance error among compared evidential, ensemble, and dropout estimators in all nine tested settings, while the estimator closest to training-set variation perturbs the model rather than its context in every setting, so the two references separate the estimators empirically. MORSE amortizes observability estimation into one forward pass per observation state. On a heteroscedastic pulse benchmark, its predictor's cross-context variance approaches a large-sample reference as training data increase. MORSE also improves low-label transfer on PTB-XL and in-distribution trajectory prediction on IMPTC.

---


### 309. [Investigating Data Flows from Android Games](https://arxiv.org/abs/2610.39730)

**<font color=#1a73e8>作者：</font>** Judit Borcsiczky, Lukas Moog, Boel Nelson  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Online applications can share data with arbitrary parties, without users noticing. In practice, these data flows could constitute privacy violations to individual users, with the lack of transparency leaving users unaware of the unwanted data flows. To understand the spread and scale of this privacy threat, we investigate what data is collected and where it is sent in popular free-to-play Android games. As part of our investigation, we conduct a measurement study where we collect and analyze over 16 GB of network traffic from 50 puzzle games. Additionally, we explore the effectiveness of user-side countermeasures for a selection of the apps. We find that while most countermeasures, such as ad-blocking DNS services, decrease data flows, withholding consent and opting out of data collection can produce inconsistent behavior including increased outgoing traffic. To encourage further analysis, we release our measurements as an open dataset.

---


### 310. [Going deep, reaching further: What can Boltzmann machines efficiently represent?](https://arxiv.org/abs/2610.39731)

**<font color=#1a73e8>作者：</font>** Tobias Reinhart, Gemma De les Coves  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While universal approximation theorems theoretically underpin the representation capabilities of machine learning models, they have two shortcomings: They do not focus on efficient representations and they tend to be insensitive to depth and other heuristically important properties. In this work we show that these two shortcomings are intertwined. We prove that machine learning models which are deeper or have higher-order interactions can efficiently represent a larger set of functions, i.e. have larger efficient reach. It follows that deep Boltzmann machines (DBMs) have maximal efficient reach, restricted Boltzmann machines (RBMs) sub-maximal, and k-body generalizations of RBMs form a hierarchy between the two, even though all are universal. More generally, (i) we provide a full characterization of machine learning models with maximal efficient reach; (ii) we derive separations between deep and shallow models for three representation tasks; and (iii) we prove that the efficient reach of shallow models constitutes an infinite hierarchy indexed by the interaction order. The proofs draw on different methodologies, namely on (i) a recent characterization of universal spin models; (ii) computational complexity bounds for spin models; and (iii) communication complexity bounds applied to shallow models. This work shows that universal machine learning models can strongly differ in their efficient representation capabilities, and provides a theoretical foundation for heuristic observations.

---


### 311. [Bank-World: A Benchmark for Evaluating Agents on Banking Workflows](https://arxiv.org/abs/2610.39733)

**<font color=#1a73e8>作者：</font>** Daniel Rupawalla  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Bank-World is a benchmark of 50 banking tasks across two simulated institutions. Completing banking work requires more than producing the right calculation: agents must reconcile records, obtain permission, execute transactions, and keep instructions and status reports consistent as circumstances change. Bank-World tests these requirements through single-turn assignments and multi-turn interactions with simulated employees who supply information, approve actions, and revise instructions. Grading combines executable checks of recorded actions and state with model judgments of task requirements, including whether valid alternative solutions satisfy them. Across 1,600 attempts by four models, we find that correct decisions often fail to become completed work. Agents charge fees twice, distribute the correct total in incorrect amounts among the recipients, and execute payments while approval is pending. Their strengths also differ: Sol leads single-turn completion, Opus has the highest observed multi-turn completion rate, and Grok succeeds across more multi-turn tasks but less consistently. Bank-World makes these differences inspectable through task-level results and worked examples connecting source evidence, agent decisions, and simulated consequences. We retain the task environments, executable graders, and full trajectories privately to reduce contamination and preserve the benchmark for future evaluations.

---


### 312. [From the Transformer to a Formal Semantics of Coordinated Transformations](https://arxiv.org/abs/2610.39735)

**<font color=#1a73e8>作者：</font>** Marco Giunti, Fabrizia Giulia Garavaglia  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We develop a formal semantics for a general class of coordinated systems of parameterized transformations, taking the Transformer as a paradigmatic starting point but abstracting from its particular mathematical instantiation. Representational vectors receive both extensional reference and ordered intensional interpretations, while parameter structures acquire relative, second-level interpretations that determine how argument properties are preserved, replaced, or combined. This yields the notion of a transforming concept: a parameterized transformation whose numerical action is coordinated with a corresponding property-level map. We then distinguish the common algebraic-semantic core of these systems from their architecture-specific functional organization, allowing different mathematical instantiations and mechanical realizations of the same abstract system type. The framework is applied to attention heads and residual connections, providing semantic explanations that depend only on the shared algebraic-semantic core and their local functional organization and therefore generalize beyond the standard Transformer. These analyses also reveal the modularity of the framework: complex architectures can be decomposed into simpler semantically coordinated subsystems whose organization may recur across different abstract system types.

---


### 313. [PAPERBENCHX: Can AI Reproduce Science Across Disciplines?](https://arxiv.org/abs/2610.39744)

**<font color=#1a73e8>作者：</font>** Ruoyu Wu, Zengji Tu, Aolong Sun 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Before AI can be trusted to discover new science, it should be able to reproduce what science already knows. Reproduction provides a rigorous checkpoint for an AI scientist: the target claim is known, yet recovering it still requires translating an incomplete scientific description into an executable experiment and producing evidence that can be independently verified. Existing research-reproduction benchmarks largely focus on AI and machine learning, where experiments share relatively homogeneous software stacks. Extending this capability across scientific disciplines introduces a different challenge: agents must operate domain-specific scientific software, make physical and numerical choices, diagnose long-running computations, and distinguish valid evidence from merely plausible outputs. We introduce PAPERBENCHX, a benchmark of 93 expert-constructed paper-reproduction tasks spanning 12 research areas across electromagnetics, photonics, chemistry, materials science, biology, and robotics. Each task provides the source paper, a public task specification, and a domain-native scientific environment involving specialized scientific software. Agents must reconstruct a key experiment, execute and diagnose it, and deliver a runnable workflow that supports the target scientific claim. To evaluate scientific validity rather than surface-level agreement, we replay every submission from scratch and score only regenerated evidence against expert-validated criteria. Across 10 frontier agent configurations, the best configuration fully reproduces only 14% tasks under the 90% threshold. Meanwhile, mean rubric scores range from 27.53% to 59.08%, indicating that substantial partial progress rarely translates into complete scientific reproduction. These results reveal a large gap between paper understanding and reliably producing reproducible scientific evidence.

---


### 314. [From Artifacts to Coordination: Exploring How Shared Canvases Drive Collaboration during Group Ideation](https://arxiv.org/abs/2610.39765)

**<font color=#1a73e8>作者：</font>** Saramsh Gautam, Andrew M. Webb, Mahmood Jasim  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent years have seen a surge in tools that support collaborative ideation through shared canvases. While these canvases offer flexible workspaces, how collaborators leverage them to iteratively develop ideas by externalizing thoughts, organizing artifacts, and coordinating tasks remains underexplored. To address this gap, we conducted an exploratory study with seven triads planning a travel itinerary using an infinite-canvas technology probe. Drawing on participant interviews and video analysis of their canvas interactions, we observed that collaborators contributed in parallel and arranged artifacts freely without a predefined structure. This spatial organization allowed collaborators to coordinate implicitly, made less vocal participants' contributions visible, helped distinguish private exploratory regions from shared working areas, and supported the emergence of distinct roles through repeated patterns of contribution. We discuss design implications for canvas-based ideation tools, including surfacing unnoticed contributions, supporting emergent roles without formalizing assignments, and keeping spatial cues legible for AI integration in collaborative canvases.

---


### 315. [Multi-output LSTM soft sensors for industrial anaerobic co-digestion using LSTM-beta-VAE generative data augmentation](https://arxiv.org/abs/2610.39768)

**<font color=#1a73e8>作者：</font>** Rohit Murali, Benaissa Dekhici, Tao Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anaerobic digestion (AD) requires close monitoring of key process variables, including pH, the ratio of volatile organic acids to alkaline buffer capacity and biogas production, to maintain biological stability and prevent process failure. While mechanistic frameworks such as the Anaerobic Digestion Model No. 1 are highly parameterised, computationally expensive, and difficult to calibrate for real-time applications, data-driven Long Short-Term Memory (LSTM) networks offer a potentially more adaptable alternative. However, current data-driven approaches in AD are predominantly limited to single-output architectures that focus solely on production yields, as opposed to simultaneous prediction of vital stability indicators. Furthermore, industrial AD datasets are typically sparse and skewed toward steady-state operations. Baseline evaluations demonstrated this scarcity prevents standard algorithms (Random Forest, XGBoost) and unaugmented LSTMs from recognising the transition to unstable operations, resulting in poor estimation of stability indicators. To overcome these challenges, this study proposes a novel generative data augmentation framework using an LSTM-beta-Variational Autoencoder coupled with a multi-output LSTM (MO-LSTM) soft sensor. By synthesising physically valid sequences of these transitions to unstable operations from one year of full-scale plant data, the method safely populates sparse regions of the feature space. Trained on this augmented dataset, the MO-LSTM achieved robust simultaneous estimation across all targets. This approach mitigates data sparsity, providing a basis for hybrid mechanistic-data-driven modelling and early-warning soft sensors in industrial bioprocesses.

---


### 316. [Quantum-Inspired Convolutional Networks for High-Resolution Pseudo-Label Generation from Multimodal Earth Observation Data](https://arxiv.org/abs/2610.39773)

**<font color=#1a73e8>作者：</font>** Abhishek Singh, Giovanni Cuozzo, Alexander Jacob 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate land-cover mapping from multimodal Earth observation (EO) data remains a challenge in regions where high-resolution annotations are scarce or costly to obtain. This work introduces a quantum convolutional encoder-decoder network for pseudo-label generation using Sentinel-1 SAR and Sentinel-2 multispectral imagery, guided only by coarse MODIS-derived land-cover maps. The proposed framework uses quantum-inspired convolutional blocks to enhance feature extraction and cross-sensor fusion, enabling the model to infer a fine-scale semantic structure from heterogeneous inputs. Experiments were conducted on the DFC2020 dataset, which provides a quadruple of Sentinel-1 SAR, Sentinel-2 multispectral, low-resolution MODIS labels and high-resolution reference land-cover maps. The proposed training framework first learns a robust representation of multimodal inputs through the reconstruction branch before any supervision from low-resolution labels is applied. This self-supervised stage enables the model to capture a fine-scale spectral-spatial structure, which is then used to generate high-resolution pseudo-labels. These pseudo-labels are subsequently evaluated through classification metrics on the test data, demonstrating that the proposed approach produces more spatially coherent and class-consistent compared to classical baselines. The results highlight the potential of quantum-inspired deep learning to improve label generation in low-annotation remote sensing scenarios, offering a scalable path towards high-quality land-cover products for EO applications.

---


### 317. [Surface Conditioning for Zero-Shot Multivariate Correction in a Marine Biogeochemistry Emulator](https://arxiv.org/abs/2610.39777)

**<font color=#1a73e8>作者：</font>** Gabriela Martínez Balbontín, Anastase Charantonis, Dominique Béréziat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bias correction in process-based models usually means iterative data assimilation with explicit covariance modelling. We propose a lightweight alternative based on a neural emulator of marine biogeochemistry (BGC), showing that the conditioning pathway of its autoencoder can serve as an observation injection point. The decoder is conditioned on surface variables via Feature-wise Linear Modulation (FiLM), originally designed to incorporate physical boundary forcings. We extend these inputs to include surface chlorophyll-a and replace the simulated field with satellite observations at inference time. The surface substitution propagates through the water column, improving agreement with depth-resolved observations at all depths, and spreads to other output variables in a pattern consistent with expected trophic relationships.

---


### 318. [SCOPE: Semantic COdec Pre-Editing for Object-Preserving Compression](https://arxiv.org/abs/2610.39778)

**<font color=#1a73e8>作者：</font>** Silvia Dani, Leonardo Galteri, Marco Bertini  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image compression is increasingly used before machine vision systems, yet standard codecs are mainly optimized for human perception rather than downstream task accuracy. We propose SCOPE (Semantic COdec Pre-Editing), a conditional image pre-editor that modifies images before compression to improve the bitrate and detection accuracy trade-off. The model is conditioned on the codec family and compression severity, allowing a single trained network to adapt to multiple compression settings without retraining or loading codec-specific weights. Instead of uniformly preserving the whole image, the pre-editor learns to protect task-relevant regions while simplifying less important background content to improve compressibility. The resulting rate-accuracy curves show consistent gains across different codec families and detector architectures, together with strong transferability to unseen learned and wavelet-based compression families.

---


### 319. [Optimal Contextual Pricing in Non-Stationary Environments](https://arxiv.org/abs/2610.39803)

**<font color=#1a73e8>作者：</font>** Yiding Feng, Alireza Rezaeimoghadam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study contextual dynamic pricing in a non-stationary environment. In each round, a seller observes a buyer's context, posts a price, and receives only binary purchase feedback. The buyer's value is linear in the context and an unobserved feature vector that may change over time, subject to a known total variation budget $V$. We measure dynamic regret against the first-best benchmark that extracts each buyer's full value.
For identical contexts, we develop a deterministic algorithm that combines binary-search exploration, lower-envelope pricing, and periodic and inconsistency-triggered restarts. It achieves regret $O((\sqrt{TV}+1)\log T)$. With heterogeneous contexts, a new geometric difficulty arises: small feature changes can leave a relaxed feasible set narrow but far from the current feature vector. We address this difficulty through a multiscale shallow-pricing algorithm that maintains relaxed feasible sets and enclosing ellipsoids at several variation scales. Larger scales provide reliable localization certificates, while the smallest active scale determines the exploitation price. The algorithm achieves dynamic regret $O((d^2+d^{3/2}\sqrt{TV})\log^2 T)$, where $d$ is the context dimension. For fixed $d$, both guarantees match the lower bound $\Omega(\sqrt{TV}+\log\log T)$ up to logarithmic factors in $T$, establishing near-optimality among deterministic algorithms for every $V\in[0,T]$, including the stationary case.

---


### 320. [GROME: GROunding Factorized MEmory into Video World Models](https://arxiv.org/abs/2610.39812)

**<font color=#1a73e8>作者：</font>** Fang Yu, Xiaoxue Wu, Haiyu Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-horizon consistency is essential for video world models, yet it becomes difficult to maintain once observed content falls outside the context window. Existing memory mechanisms either retrieve history as implicit context, which remains constrained by context capacity and entangles static and dynamic information or consolidate history into explicit global representations, which struggle to model evolving dynamics and accumulate geometric errors. To overcome these limitations, we introduce \textbf{GROME}, a novel factorized memory framework that augments video world models for long-horizon coherence across both static scenes and dynamic entities. GROME operates via three synergistic components: 1)~\emph{Static-Dynamic Factorization} decouples historical evidence into static and dynamic components, preserving static scene geometry and dynamic entity states separately; 2)~\emph{Local Memory Retrieval} selects spatially aligned static history to eliminate geometric drift alongside the latest dynamic entity states to ensure temporal continuity; 3)~\emph{Training-Free Memory Injection} seamlessly grounds the factorized memory into video world models via their native conditioning pathways. Experiments on long-horizon revisit scenarios demonstrate that GROME substantially enhances scene persistence and dynamic entity fidelity over existing methods, all while preserving the visual quality and controllability of the frozen backbone without additional training. Beyond self-rollouts, GROME readily accommodates external observations as plug-and-play memory, unlocking flexible and controllable video continuation and scene exploration.

---


### 321. [Possibility-based Inference: A Deterministic Framework for Robust and Reliable Uncertainty Quantification in Decision-Making](https://arxiv.org/abs/2610.39821)

**<font color=#1a73e8>作者：</font>** Seyedfakhredin Musavishavazi, Maryam Alipour  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision-making under uncertainty remains a key issue in Machine Learning (ML), particularly in the deployment of safety-critical systems, where reliable quantification of system behavior is essential for evaluating behavioral impacts and strengthening confidence in ML models. This contribution, influenced by fuzzy set theory and grounded in Bayesian statistics, addresses challenges related to data precision and the performance-accuracy trade-off in Bayesian inference (BI). To this end, we introduce a possibility-based contrastive grade of prediction as an alternative quantification method to existing latent posterior-based approaches for parameter estimation (approximation) and model selection. Unlike conventional Bayesian inference, which represents uncertainty within the probabilistic framework, the proposed model adopts a possibility-based representation that allows uncertain and potentially conflicting information to be characterized more flexibly. Rather than focusing on isolated aspects of a problem, the resulting mathematical framework provides a systematic approach to data mining while mitigating overly confident, yet implausible predictions generated by highly specialized deep learning architectures.

---


### 322. [AegisFlow: Training-Free Non-Myopic Path-Safe Guided Flow Matching](https://arxiv.org/abs/2610.39825)

**<font color=#1a73e8>作者：</font>** Kunpeng Liu, Boshi Zhang, Keyou You  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pretrained generative models, such as diffusion and flow matching models, have demonstrated exceptional capabilities in synthesizing high-quality data. However, steering their generative trajectories to satisfy strict constraints--such as identity preservation in image editing or obstacle avoidance in robotics--remains fundamentally challenging. While recent training-free guidance methods enforce path-safety, they rely heavily on min-norm controllers that only account for immediate constraint satisfaction. These myopic approaches often yield suboptimal trajectories that hover dangerously close to the boundary, severely restricting the model's ability to optimize toward its target. In this paper, we propose AegisFlow, a training-free, non-myopic path-safe guidance framework that recasts guided generation as a safety-critical optimal control problem with global scope. By integrating a time-varying barrier function directly into the global cost functional, AegisFlow naturally enforces constraints along the entire generative path. To compute the global optimal control, we derive a tractable, mathematically grounded approximation of the Hamilton-Jacobi-Bellman (HJB) equation. Comprehensive experiments demonstrate that AegisFlow outperforms state-of-the-art methods across text-guided image manipulation and robotic planning, establishing a significantly better trade-off between target alignment and constraint satisfaction. Code is available at this https URL.

---


### 323. [SHPRR: An Algorithm for Pure Exploration under Constrained Regret](https://arxiv.org/abs/2610.39837)

**<font color=#1a73e8>作者：</font>** Georgina Nouli, Flore Sentenac, Maximilian Schiffer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Best Arm Identification (BAI) conventionally measures the cost of experimentation by the number of samples collected. In many operational settings, however, the cost of exploration relative to a trusted baseline already in place is equally important. We study BAI under both a fixed sampling horizon and a regret budget. Unlike generic resources considered in constrained pure exploration, regret has a distinctive structure: sampling better arms is less costly relative to the baseline. We theoretically show that the regret cost of exploration decreases across the phases of Sequential Halving, a widely used pure-exploration algorithm. This observation yields improved guarantees on the probability of identifying the best arm and motivates a more effective allocation of the regret budget. We propose Sequential Halving with Proportional Regret Rationing (SHPRR), which front-loads the regret budget to allow more exploration when many arms remain. Experiments on synthetic and real-world instances show that SHPRR improves best-arm identification performance over uniform regret allocation and existing baselines.

---


### 324. [Exploring the Potential of Symbolic Regression in Precision Livestock Farming](https://arxiv.org/abs/2610.39839)

**<font color=#1a73e8>作者：</font>** Elisabeth Mayrhuber, Maciej Oczak, Michael Iwersen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The ability to predict farrowing time in pigs is crucial for optimal farm management and ensuring piglet survival. This study investigates the potential of explainable artificial intelligence for precision livestock farming, focusing on acceleration sensor data from sows around the time of farrowing. Accurately predicting farrowing allows farmers to balance both, piglet safety by avoiding piglet crushing events and the mother sow's welfare, by avoiding early crating. Traditional machine learning models often lack interpretability (``closed-box'' problem). Explainable artificial intelligence offers a solution by revealing the decision-making processes within the models. This work is split into two stages. First the detection of nest building behaviour and second the prediction of the remaining time to farrowing. The nest building detection was possible for 166 out of 180 sows and successful within 48 hours before farrowing for 149 sows. The nest building detection is purely based on the change of a sow's activity level and uses no machine learning techniques. Further, this study utilizes symbolic regression, an open-box modelling technique that generates interpretable mathematical formulas, to predict the remaining time until the onset of farrowing. The results are compared with closed-box models, like support vector regression and artificial neural networks, for both explainability and performance. Notably, symbolic regression achieved a mean absolute error of 9.28 hours for the time-to-farrowing prediction, outperforming the closed-box models in terms of performance and interpretability. This research demonstrates that explainable artificial intelligence, specifically symbolic regression, can offer both interpretable results and competitive performance in precision livestock farming.

---


### 325. [LiDAR-SHIELD: A Fully Dockerized Adversarial Robustness Assessment Framework for LiDAR-Based 3D Perception Models](https://arxiv.org/abs/2610.39848)

**<font color=#1a73e8>作者：</font>** Alexandros Gkillas, Ioulia Kapsali, Christos Anagnostopoulos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDAR-based 3D perception underpins autonomous driving and robotics, yet deploying these models safely requires stress-testing them against adversarial inputs before real-world use. Although state-of-the-art adversarial attacks exist, their implementations are often fragmented across individual repositories, each tied to a specific architecture or task and requiring manual environment reconstruction and model-specific integration code. We present LIDARSHIELD, a unified and fully Dockerized framework that reverses this workflow: rather than installing the target model inside the toolkit, LIDARSHIELD exposes any model through three lightweight HTTP endpoints, namely /info, /forward, and /gradient As a result, connecting a new model or dataset requires only a single loader function or adapter. The framework supports both 3D semantic segmentation and 3D object detection through the same engine-service protocol, integrating a task-aware suite of state-of-the-art attacks, including PGD and Square Attack for segmentation, and point perturbation, point removal, point injection, and LiDAttack for detection. This enables systematic exposure of corner cases and vulnerabilities across heterogeneous LiDAR backbones. The LiDAR-Shield codebase is publicly available at this https URL.

---


### 326. [Integrating Perception, Comprehension, and Projection for Alert Validation: A Unified Cyber Situational Awareness Framework](https://arxiv.org/abs/2610.39849)

**<font color=#1a73e8>作者：</font>** Navodika Karunasingha, Mohan Baruwal Chhetri, Surya Nepal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security Operation Centres (SOCs) must validate large volumes of alerts with limited analyst resources, yet alerts often lack sufficient context to determine whether suspicious activity is attack related. While provenance-based intrusion detection research has progressed from perception-level signals to comprehension- and projection-level cyber situational awareness (CSA), it remains unclear whether richer CSA consistently improves alert validation. This paper presents the first systematic evaluation of perception-, comprehension-,and projection-level CSA within a unified alert validation framework. Using Captain and Kairos, we generate multi-level CSA and formulate alert validation as a positive-unlabelled multi-instance learning (PU-MIL) task over CSA-derived behavioural hypotheses. Experimental evaluation on the DARPA TC dataset shows that comprehension-level CSA substantially improves validation by incorporating causal attack context. Relative to the Queue and Max. CSG baselines, PU-MIL achieves up to 28.6 and 75 percentage-point gains in Recall@5, and 24.6% and 86.8% reductions in mean positive rank on Cadets and Theia, respectively. Projection-level CSA can yield additional benefits, reducing the mean positive rank on Theia from 22.0 to 8.5 at a 40-minute projection horizon, although its effectiveness varies across projection horizons. Overall, richer CSA does not necessarily lead to better alert validation. Rather, its value depends on when and how it is introduced, motivating adaptive CSA progression that selectively enriches alerts according to validation requirements.

---


### 327. [Open-set multi-view seahorse re-identification from underwater photograph sequences](https://arxiv.org/abs/2610.39857)

**<font color=#1a73e8>作者：</font>** Tristan Fauvel, Sylvie Louisy, Patrick Louisy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated animal re-identification from photograph sequences can facilitate minimally invasive Capture-Mark-Recapture studies at scale. Yet, photographs taken during an observation session can vary greatly in quality, not always providing the necessary information for accurate re-identification. In this paper, we present new methods for taxonomic classification, sex determination, and open-set re-identification from image sequences. We train and evaluate our models on a dataset of 35,914 photographs of 474 individual seahorses observed in the wild. We demonstrate that our approach, by combining information from multiple photographs, yields state-of-the-art performance.

---


### 328. [Parametric Gaussian Noise Mixer (PGNM): Unified Synthesis of Camera Noise and Film Grain](https://arxiv.org/abs/2610.39868)

**<font color=#1a73e8>作者：</font>** Mingyang Song  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Noise synthesis is commonly approached through physical models of image formation or neural networks trained to generate noisy images. We explore a middle ground: an explicit statistical model fitted directly from paired clean and noisy images. A normalized convolution correlates a Gaussian field across pixels and color channels, and a lookup maps each Gaussian value to a residual given the clean intensity. Because the field stays standard Gaussian, the two components are fitted separately, without reproducing the physical process or training a neural generator. With one formulation for camera noise from SIDD and simulated film grain from Newson, the model has the lowest average distribution and correlation errors on SIDD among the evaluated methods and remains competitive on film grain. A denoiser trained on its noise comes closest to one trained on real noise, and a 1080p frame renders in 10 ms on GPU.

---


### 329. [Syndrome Trellis Decryption in Post-Quantum Cryptography](https://arxiv.org/abs/2610.39873)

**<font color=#1a73e8>作者：</font>** Meir Ariel  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present a novel post-quantum cryptographic framework based on masked high-memory convolutional codes in the Niederreiter paradigm. The public key is derived from a high-memory polynomial parity-check matrix augmented by dense random masking and additional invertible linear transformations. The resulting matrix exhibits strong random-like properties, effectively concealing its algebraic structure and resisting known structural and algebraic attacks. Legitimate recipients retain polynomial-time decoding capability, whereas adversaries appear to be limited to generic information-set decoding with exponential complexity. Under standard cryptanalytic estimates, the proposed construction achieves security margins exceeding those of classical McEliece- and Niederreiter-based systems by factors greater than 2^200. Beyond its enhanced security profile, the construction offers considerable design flexibility, supporting arbitrary plaintext lengths, linear-time decryption, and a uniform per-bit computational cost, enabling efficient scalability to very long messages. Practical implementation is facilitated by a parallel array of syndrome-trellis decoders, dynamically instantiated according to candidate syndrome values, enabling efficient hardware and software implementations with high throughput. Overall, the proposed scheme is a promising candidate for robust, scalable, quantum-resistant public-key cryptography.

---


### 330. [What Survives Label Downsampling? Exact Region Survival for Coarse Segmentation Targets](https://arxiv.org/abs/2610.39880)

**<font color=#1a73e8>作者：</font>** Zhiyuan Zhang, Yukun Ou, San Tek Choi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segmentation networks that predict at an output stride are trained against label maps downsampled by strided sampling, nearest-neighbor resampling or majority pooling. These methods label each coarse grid cell on its own, so a region that wins no cell is absent from the target and receives no positive label. We present MatchDown, which builds the coarse target from a minimum-cost matching between regions and the grid cells they occupy. It keeps as many regions as any one-region-per-cell target can, certifies how many losses are unavoidable, and with priority tiers (MatchDown-P) keeps every evaluated region (a region that a metric scores) of at least one cell's area. On COCO, Cityscapes and BBBC038 at factors 2 to 16, MatchDown-P loses exactly the minimum number of regions, whereas the downsampling used by StarDist, nnU-Net and connectomics pyramids loses four to five times as many on COCO at factor 8. Keeping a region in the target and reconstructing its shape are different problems: we show that no region lost by majority pooling can be reconstructed above IoU 0.5 by upsampling any coarse target, yet on BBBC038 a star-convex head trained on MatchDown targets segments 35% of the nuclei that majority pooling loses above IoU 0.5, against 15% when trained on majority targets and 24% on StarDist's strided target. On two nucleus datasets, with thresholds cross-validated for count error, this head has instance accuracy at IoU 0.5 (Acc50) 2.6 to 4.2 points above the strided target and at most 2.8 points below cell-center sampling, and a lower count error than the strided and cell-center targets on BBBC039. On BBBC039, an affinity head, which outputs one label per cell, lowers count error relative to majority targets by 9.3 nuclei per image at 7.2 points lower Acc50. MatchDown runs once, before training, in place of the label-downsampling step.

---


### 331. [Data-driven Random-feature Approximation of Koopman Generators of Nonlinear Continuous-time Systems](https://arxiv.org/abs/2610.39897)

**<font color=#1a73e8>作者：</font>** Ana Čukarska, Maximilian Gollwitzer, Viola Muning Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning continuous-time dynamical systems from data is an active area of research. The Koopman formalism is often used here, because it is a flexible approach that is informative about the system's fundamental properties. The formalism represents dynamical systems through linear operators acting on a suitable function space. A practical difficulty arising in the numerical approximation of Koopman operators is the choice of a ``dictionary'', meaning an effective finite-dimensional representation of the function space. In this paper, we focus on learning dynamical systems in continuous-time, and so we consider numerical approximations of the Koopman generator instead of the Koopman operator. Our main contribution is a data-driven random-feature method to obtain a parsimonious and effective function representation for Galerkin approximation methods such as gEDMD. The representation we construct is data-informed, which allows us to improve upon data-agnostic methods. We empirically demonstrate the suitability of our method for forecasting tasks and system analysis. The numerical experiments show that our approach is accurate, and faster than iterative optimization. Further, we prove convergence of our approximation of the vector field and the resulting trajectories. In addition to the numerical results, we also make theoretical contributions, including a general convergence criterion for the semigroup generated by the gEDMD approximation and a counterexample showing that gEDMD does not generally preserve exponential boundedness. With our contribution, we advance the frontier of efficiently learning continuous-time dynamics from data, towards interpretable and mathematically robust modelling based on the Koopman framework.

---


### 332. [CovFedAvg: Local Low-Loss Curves and Federated Model Selection](https://arxiv.org/abs/2610.39902)

**<font color=#1a73e8>作者：</font>** Federico Lucchetti, Marcus Völp  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clients observing different parts of a prediction task may learn locally equivalent models with incompatible behavior outside their observed support. We study whether redundant models permit local low-loss paths toward a compatible shared model. CovFedAvg retains local models and curve controls on clients, fits a common endpoint through aggregated gradient contributions, and selects an actual candidate model using distributed training losses. No centralized calibration examples or client-to-client sample exchange are required. Exact selection guarantees no higher evaluated training loss than the previous model and the current-round FedAvg candidate; this is not a global-optimality, stationarity, generalization, or differential-privacy guarantee. We state conditional client-compatibility and approximate-selection bounds and retain corrected transformation identities and a separate full-gradient safeguard theorem for reference algorithms. A complementary input-support example recovers the shared absolute-value regression, while matched direct fine-tuning also solves it. Across a synthetic support task, recorded activity-recognition subjects, and participating and future gas-sensor batches, we evaluate five methods, five seeds, two network widths, and 20 rounds without calibration data. At width 16, CovFedAvg raises participating-Gas macro balanced accuracy from FedAvg's 88.88% to 89.84%; matched distributed fine-tuning reaches 91.65%. Results support feasibility and modest gains over FedAvg, but do not establish a curve-specific advantage over equally costly optimization. Exact-sum numerical experiments establish data flow; end-to-end privacy requires additional mechanisms and analysis.

---


### 333. [Inkitiate: Initiating and Steering Agent Assistance through Ink in a Spatial Workspace](https://arxiv.org/abs/2610.39905)

**<font color=#1a73e8>作者：</font>** Liangwei Wang, Nan Chen, Luna K. Qiu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Handwriting and sketching help people develop ideas around information. As this work unfolds, users may seek assistance with finding, understanding, and organizing materials. We investigate how ink can initiate and steer agent assistance in this process. An eight-participant formative study explored desired assistance and interaction expectations, informing three connected activities: bringing materials in, thinking with materials, and shaping the space. We present Inkitiate, a spatial workspace for ink-based agent assistance in knowledge work. Through ink, users retrieve external materials, build on accumulated content and results, and reorganize the canvas, while inspecting and guiding agent actions. In a study with eighteen participants, users reported favorable usability and low perceived workload, and used retained ink and materials to develop further ink queries. An ink-query vocabulary and cases reveal how users combine linguistic and graphical expressions to direct agents. These findings inform ink-based agent interaction design for expressive requests and continued work with materials.

---


### 334. [From if to Oops: Turning a conditional into a key-recovery oracle](https://arxiv.org/abs/2610.39910)

**<font color=#1a73e8>作者：</font>** Gustavo Banegas, Nia Dimitrova, Monika Trimoska  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deterministic variants of CSIDH remove randomness from the group action, either through implementation techniques or, as in Houben's deterministic CSIDH and OSIDH-LD, by design. Since earlier fault attacks on CSIDH mostly target random point sampling, determinism seems to close that avenue. We show that it opens another: every secret-dependent step occurs at a fixed, public point of every execution, so an attacker can fault the same step repeatedly. Our attack forces the mask that selects which of two lanes computes the next isogeny to zero, for example by skipping one instruction. Whether the output changes reveals whether a secret exponent reaches a chosen threshold, and a binary search over these thresholds recovers the full key with one fault per execution: at most 297 oracle queries for OSIDH-LD and 222 for deterministic CSIDH with CSIDH-512-sized keys. We recover full OSIDH-LD keys in a software fault simulation of the reference implementation, and show on a ChipWhisperer-Lite that the targeted instruction is skipped with probability at least 0.94 at an isolated fault position. Finally, we argue that fault resistance requires giving up determinism, and propose countermeasures relying on randomization.

---


### 335. [TokenRepel: Generating Diverse Image Sets Without Compromising Quality](https://arxiv.org/abs/2610.39913)

**<font color=#1a73e8>作者：</font>** Qingtao Yu, Zhen Wang, Ning Lai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present an inference-time approach that enhances the visual diversity of image sets generated by text-to-image models, without compromising the average image quality. Our method leverages the intrinsic geometry of hidden representations in pretrained models to diversify images generated from the same prompt. First, we introduce a token repulsion mechanism that increases the angle between feature tokens across samples. It takes a negative Riemannian gradient step on a von Mises-Fisher mixture distribution of tokens on the unit hypersphere. Second, to preserve the quality of each output image, we propose a token density preservation mechanism that projects the repulsion-induced prediction change onto a half-space aligned with the model's score direction. This encourages the updates to remain within the high-density regions learned by the generative model. We further extend this mechanism to the output of each intermediate layer, enabling finer-grained iterative guidance. We evaluate our method on three types of pretrained text-to-image models. Experiments show substantial gains in visual diversity under identical prompts, while maintaining a comparable level of image fidelity.

---


### 336. [Tokenizer Tokens Tell Training Tales](https://arxiv.org/abs/2610.39919)

**<font color=#1a73e8>作者：</font>** Nishita Jain, Parth Upman, Shreyank N Gowda  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tokenizers are usually treated as fixed preprocessing tools, but they are trained on text and can retain traces of that text in their vocabularies. We ask whether a BPE tokenizer can reveal if a candidate dataset was part of its training corpus. The key observation is simple. Rare strings become tokens only when enough corpus frequency pushes them over the merge threshold. This suggests that membership signal should appear in rare tokens used by the candidate dataset, rather than in the order in which merges were made. We formalize this under a threshold model of BPE inclusion, showing that the likelihood-ratio test assigns its largest weights to tokens that are rare in the background but frequent in the candidate dataset. The same model suggests that merge rank and merge-graph position should not add a first-order membership signal once token existence and dataset frequency are known. We instantiate this view as RTAM-Fusion, which calibrates rare-token mass with shadow tokenizers and combines signals across rarity levels. On the tokenizer membership benchmark, RTAM-Fusion improves AUC and balanced accuracy over Vocabulary Overlap while using fewer shadow tokenizers. Existing defenses also continue to leak membership signal against adaptive attackers at production vocabulary sizes. Code: this https URL

---


### 337. [Spectral Invariant Fusion and Refinement for Domain Generalized Semantic Segmentation](https://arxiv.org/abs/2610.39926)

**<font color=#1a73e8>作者：</font>** Yansong Bai, Yunzhi Zhuge, Xinzhuo Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Domain generalized semantic segmentation is challenging because it requires accurate dense prediction on unseen domains without any access to target-domain data during training. Existing methods improve transferability through data diversification, invariant learning, or direct use of foundation models, but they often struggle to simultaneously suppress domain-sensitive interference and preserve fine-grained spatial cues. In this work, we propose SIFR, a frequency-aware dual-stream framework that tackles domain shift at both the fusion and decoding stages. SIFR uses spectral modeling as a unified principle to regulate both heterogeneous prior interaction and dense decoder refinement. Instead of directly fusing frozen CLIP and DINOv2 features, SIFR performs spectral-guided invariant fusion to filter out domain-sensitive responses while preserving complementary semantic and structural information. In addition, SIFR incorporates a spectral decoder refinement module that stabilizes multi-scale decoder features through low-frequency statistics-based normalization and adaptive frequency selection, thereby reducing the propagation of residual domain bias in dense prediction. This design enables SIFR to jointly improve domain robustness and segmentation precision under severe distribution shifts. Extensive experiments on multiple DGSS benchmarks, including synthetic-to-real, real-to-real, and adverse-weather settings, demonstrate consistent improvements over previous state-of-the-art methods.

---


### 338. [Learning Calibrated Confidence for Multi-Agent Collaboration](https://arxiv.org/abs/2610.39927)

**<font color=#1a73e8>作者：</font>** Chenxiao Fan, Chongming Gao, Gangyi Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Complex information seeking on the Web often requires collecting evidence from multiple documents and reasoning across them, as in multi-hop question answering. Multi-agent systems address such tasks by dividing work among specialized agents, where upstream agents produce intermediate answers and supporting evidence that downstream agents build upon. However, upstream answers vary in correctness, and most systems provide no quantitative signal about it, leaving the downstream agent to judge whether to trust or verify what it receives based solely on the textual evidence.
In this paper, we propose MASCAL. Each agent learns to produce a correctness probability for its answer by jointly optimizing task performance and confidence calibration in reinforcement learning; the upstream agent passes this probability at handoff, giving the downstream agent a quantitative basis for its decisions, and the final answer also carries a calibrated probability, quantifying the reliability of the system output. To guide the downstream agent in using this signal during training, we introduce confidence-aware weighting, which increases the learning weight at positions responsive to the upstream probability, so that the agent learns more from decisions where it actively uses the signal. Across three collaboration architectures spanning Web retrieval and reasoning tasks, MASCAL improves task accuracy and calibration quality for both agents, and generalizes to deeper collaboration chains and different model scales. Intervention analysis confirms that upstream confidence affects downstream decision behavior, and the learned final confidence supports selective answering and targeted rechecking.

---


### 339. [BiHashFormer: Hash-Driven Dual-Branch Transformer for Efficient Object Detection in HRW Shots](https://arxiv.org/abs/2610.39937)

**<font color=#1a73e8>作者：</font>** Jingchen Huang, Wenxi Li, Chenyang Lyu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in gigapixel-level imaging have brought High-Resolution Wide shots to the forefront of research. However, these images present significant challenges: extreme sparsity of foreground, gigapixel-level resolutions and interleaving of foreground and background. This causes traditional detectors and attention mechanisms to be hindered by background, resulting in inefficiency and inaccuracy. To tackle this problem, we propose BiHashFormer, a dual sparsified branch transformer built on hashing. RoI Selector will predict the foreground proportion for top-k selecting target-containing windows. The compression branch processes windows selected and refines attention into HashAttention by discarding half of the key-value pairs, reducing cost and improving efficiency. The compensation branch uses HashMiner to perform low-cost hash searches in the remaining regions, recovering features of missed objects. Experiments confirm that the selection relationship in HashAttention is one-way and reveal the preference of different queries for keys. In experiments on the gigapixel benchmark PANDA, BiHashFormer reduces 37.5% backbone FLOPs while improving AP50 to 81.0%. Moreover, this parallel dual-branch structure allows the model to avoid inference delays caused by inter-branch dependencies, while achieving much greater stability than single-branch models, specially with low rates of RoI selection.

---


### 340. [ElasticFormer: Detecting Objects in HRW Shots via Elastic Computing Vision Transformer](https://arxiv.org/abs/2610.39946)

**<font color=#1a73e8>作者：</font>** Wenxi Li, Jingchen Huang, Chenyang Lyu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in gigapixel-level imaging have brought High-Resolution Wide shots to the forefront of research. However, these images present significant challenges: extreme sparsity of foreground, gigapixel-level resolutions and diverse target counts. This makes traditional close-up detectors inaccurate and slow as they are overwhelmed by the background. Although previous research has explored sparse backbones, their fixed sparsity patterns lack the adaptability required to handle diverse target numbers. To address this, we introduce ElasticFormer, a sparse backbone that dynamically allocates computational resources based on foreground proportion. After scoring windows based on variance, proposed ElasticSelector module will predict the foreground proportion for top-k selection. The mechanism guides the model to select target-containing windows, scaling resources in areas where objects are clustered. We introduce a novel loss function combined with the 3-phase training strategy for ElasticSelector, allowing it to function properly when bounding box annotations are missing. A WSOD study is carried on PASCAL VOC 2007 to evaluate its extensibility. Further, ElasticNet is created to verify its backbone-agnostic nature. In experiments on the PANDA gigapixel benchmark, ElasticFormer reduces backbone FLOPs by 80% while achieving a significant improvement in AP50 when compared to fixed-ratio sparse methods.

---


### 341. [UniRA: Unified Representation Alignment and Auto-Encoding for Efficient Diffusion Generation](https://arxiv.org/abs/2610.39948)

**<font color=#1a73e8>作者：</font>** An Lanji, Dawei Liu, Jin Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion transformers (DiTs) have become the dominant architecture for high-fidelity image synthesis, yet they suffer from slow training convergence and high computational cost. Two recent lines of work address this from complementary angles: Representation Alignment (REPA) accelerates DiT training by aligning intermediate features with a pretrained external representation model (e.g., DINOv2), while Representation Auto-Encoders (RAE) replace the pixel-space VAE with a compact representation-space tokenizer learned from self-supervised features. However, these approaches are developed and applied in isolation: REPA still relies on a pixel-space VAE for latent diffusion, and RAE does not exploit the alignment signal that accelerates the diffusion backbone. We present \textbf{UniRA}, a unified framework that couples representation alignment and representation auto-encoding into a single objective. UniRA learns a representation-space tokenizer whose output serves simultaneously as the diffusion target and the alignment anchor, so the tokenizer, the diffusion backbone, and the external representation model are co-optimized. We give a theoretical result showing that this joint optimization preserves the representation quality of the external model while accelerating diffusion convergence, and we derive a principled weighting that balances the reconstruction, alignment, and generation objectives. On ImageNet class-conditional generation at 256*256 and 512*512, UniRA matches or surpasses state-of-the-art DiTs (SD3, REPA, RAE) in FID while reducing training steps by up to 5*. We further show that the unified representation space supports improved zero-shot classification and linear probing, confirming that generation and understanding benefit from a shared, aligned latent space.

---


### 342. [When to spend privacy: optimal allocation in private learning](https://arxiv.org/abs/2610.39954)

**<font color=#1a73e8>作者：</font>** Umberto Biccari, Yongcun Song  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Privacy accounting bounds the cumulative privacy cost of Differentially Private Stochastic Gradient Descent but does not determine how to allocate a fixed budget across iterations. We formulate the complete Gaussian noise-variance schedule as an open-loop control under a composed zero-Concentrated Differential Privacy constraint, explicitly accounting for schedule selection. For expected quadratic terminal tracking, we prove that every local minimizer exhausts the certified budget, yielding an exact-budget simplex formulation. We introduce Privacy-Budget Adjoint Mirror Descent (PB-AMD), combining pathwise adjoint gradients with entropic updates that preserve positivity, charge floors, and the prescribed budget. Under regularity and coercivity assumptions, we establish existence and budget stability of optimal schedules, design-to-training utility stability, and deterministic, stochastic, and sample-average stationarity guarantees. A linear-quadratic reduction yields an explicit square-root allocation law. Experiments demonstrate tracking improvements over several allocation rules and predictive improvements over uniform allocation in a learning-rate restart setting, where learning-rate allocation performs similarly. Comparisons at a common stationarity tolerance show lower schedule-optimization times than projected gradient descent on the tested problems. The framework connects certified privacy accounting with optimization through nonlinear training dynamics.

---


### 343. [Observability-Aligned Evidential Masked Pretraining for Reliable VRU Motion Prediction](https://arxiv.org/abs/2610.39958)

**<font color=#1a73e8>作者：</font>** Shang Gao, Franz Götz-Hahn, Konrad Doll 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vulnerable road user (VRU) prediction must operate under partial observability and distribution shift, so reliable uncertainty matters alongside accuracy. Masked pretraining is attractive in this setting because it naturally exposes the model to missing content during self-supervision, but existing time-series masked autoencoding methods are typically deterministic and do not constrain how confidence should change with observability. We introduce eCoMAE, an evidential masked pretraining method for multivariate time series that explicitly aligns predictive evidence with what is observed. eCoMAE combines block-wise time-step masking with a Normal-Inverse-Gamma decoder and three observability-aware mechanisms: uncertainty-weighted mean consistency on positions visible in both a masked view and a reference pass, evidence suppression on masked positions, and representation consistency across stochastic masks. On IMPTC benchmark for VRU intention prediction under leave-one-environment-out weather shift, eCoMAE improves the strongest baseline from 0.7971 to 0.8068 in OOD accuracy and from 0.0718 to 0.0648 in OOD AURC. Additional evaluation on pedestrian trajectory forecasting across IMPTC, Waymo, nuScenes, and inD further yields the best fine-tuning MSE on all four datasets. These results show that observability-aligned evidential pretraining improves reliability under shift and remains effective beyond the primary benchmark.

---


### 344. [A physics-informed uncertainty-aware surrogate for $p$-$n$ junction diodes](https://arxiv.org/abs/2610.39993)

**<font color=#1a73e8>作者：</font>** Suchita Kulkarni  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop an uncertainty-aware physics-informed surrogate for a one-dimensional $p$-$n$ junction diode, conditioned on device length, doping and bias. Using the internal state of the device as predicted by the surrogate we develop a test-suite of quantities of interest including the terminal current, depletion width, peak field and stored charge. The formalism and the quantities are can be extended to asymmetric junction and two-dimensional diodes as shown by means of benchmark analysis. For the one-dimensional symmetric junction surrogate, we obtain 0.11% median $L_1$ error on the electrostatic potential, and 1.5% and 0.61% on the electron and hole densities. Finally, we develop an uncertainty analysis which determines the validity of surrogate answer within the user-specified tolerance.

---


### 345. [Enhancing Atrial Fibrillation Detection Through Hyperparameter Optimization](https://arxiv.org/abs/2610.40001)

**<font color=#1a73e8>作者：</font>** Sara Gjorgjieva, Ilinka Ivanoska, Marjan Gusev  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study explores the role of hyperparameter optimization (HPO) in enhancing the detection of Atrial Fibrillation (AF) using both machine learning and deep learning models. We evaluated a range of standard classifiers - Decision Tree, Random Forest, and XGBoost classifiers, alongside deep learning architectures including Recurrent Neural Networks, Deep Neural Networks, and Siamese Neural Networks. To fine-tune these models, we applied four HPO methods: Genetic Algorithm, Hyperband, Optuna, and SMAC3. The experiments were conducted using inter-patient and intra- patient data splits to assess model generalization and robustness in the presence of class imbalance, which is reflective of real-world AF occurrence. Our results, based on PhysioNet electrocardiogram datasets, showed that the Hyperband-optimized XGBoost model outperformed all others, achieving a peak F1 score of 96.95%. These findings highlight the critical role of suitable HPO strategies in enhancing the accuracy and robustness of AF classification outcomes in clinical settings.

---


### 346. [Efficient Learning of Mechanism Designs and Compositionality](https://arxiv.org/abs/2610.40005)

**<font color=#1a73e8>作者：</font>** João Pedro Gandarela, Thiago Rios, Stefan Menzel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning mechanism behaviour requires a representation of how connected parts jointly constrain motion. We study whether exposing reusable constraint subassemblies improves prediction from limited data. Assur-KB represents planar mechanisms through irreducible modules, boundary interfaces, and solve dependencies while retaining source geometry. Our theoretical results characterize transfer through module interfaces and establish physical limits arising from missing interface information and accumulated sensitivity. To test the representation claim directly, the experimental design compares matched mechanism-curve pairs across training budgets within the same multilayer-perceptron family. This controlled comparison establishes the utility of the complete representation in the evaluated learning setting. Assur-derived features provide a geometric-mean $1.8\times$ advantage in sample efficiency over flattened adjacency and position inputs across budgets of 50-10,000 mechanisms. Separate experiments establish invariance under tested joint relabelings, higher valid-generation rates under dyadic composition, and a coarser structural index over 10.02 million mechanisms. In summary, the theory and experiments identify how physical constraint structure supports limited-data prediction and which interface conditions govern compositional reuse.

---


### 347. [Human--AI Interactions as First-Class Data: A Formal Interaction Model and Runtime for Explainable AI Collaboration](https://arxiv.org/abs/2610.40006)

**<font color=#1a73e8>作者：</font>** Michela Taufer, Kin Ng, Ian Lumsden 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI assistants are increasingly embedded in computational notebooks, scientific workflows, software engineering tools, and learning systems, yet human-AI interactions are often treated as transient prompt-response exchanges rather than durable data products, hindering reproducibility, explainability, replay, behavioral analysis, and adaptive AI support. We argue that these interactions form a new data class requiring formal representation and introduce the Human-AI Interaction Description Language (HAIDL), a formal interaction model with a Backus-Naur Form-inspired concrete syntax. HAIDL encodes each interaction as a structured object capturing computational context, user request, prompt payload, AI response, feedback, problem context, provenance, and model metadata. We integrate this vision into HAIDL-X, a middleware for JupyterLab that instantiates HAIDL by capturing user-bot state, building contextualized prompts, interfacing with AI providers, collecting feedback, and storing interactions in a repository. We add a learning layer over HAIDL that maps interaction objects and notebook execution traces into reproducible measures of user behavior, including engagement, performance, help-seeking, error-oriented use, and learning personas. HAIDL-X provides a foundation for treating human-AI collaboration as structured, queryable, replayable, analyzable data.

---


### 348. [FIDE: Fiber-Informed Differentiable Experimental Design for Reference-Relative Law Dynamics](https://arxiv.org/abs/2610.40009)

**<font color=#1a73e8>作者：</font>** Pietro Zanotta, Ján Drgoňa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Aggregate measurements generally leave an evolving population law underdetermined, so different measurement systems can be equally adequate for a scientific task while constraining different aspects of the law. We study how to resolve this residual design freedom in baseline-preserving settings, where an existing dynamical model remains the working baseline outside quantities explicitly valued by the task. \textbf{F}iber-\textbf{I}nformed \textbf{D}ifferentiable \textbf{E}xperimental Design (\textbf{FIDE}) completes each candidate's aggregate constraints by information projection relative to a common frozen reference, then ranks scientifically adequate designs by the dynamical revision required to realize the resulting completed paths. The resulting \emph{Full action} is the minimum mean-squared velocity correction needed to realize a completed path; equivalently, its square root is the sharp reference-relative expectation-rate discrepancy over a gradient-normalized Sobolev class. This defines a conditional minimum-revision principle for baseline-preserving design rather than a generic truth-recovery objective. Experiments show that this preference changes sensor selection, can help or harm withheld downstream predictions depending on baseline reliability, can be used prospectively from aggregate predictions, and remains computationally usable for a $32$-dimensional configuration law.

---


### 349. [DINOv2 for PET: A Pre-Training Domain Benchmark Across Classification, Segmentation, and Prognosis](https://arxiv.org/abs/2610.40018)

**<font color=#1a73e8>作者：</font>** Roxanne De Maeyer, Yannick Brackenier, Vicky De Ridder 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> DINO (self-DIstillation with NO labels) has become a stan- dard for self-supervised pre-training, producing features that generalise across datasets and downstream tasks. In medical imaging it has been adopted mainly for radiology (X-ray, CT and MRI), where even natural- image DINO features transfer well. In the literature, these features have been reported to transfer worse to functional imaging such as PET. Yet PET-specific DINO models have barely been introduced, and even less validated across multiple tasks and datasets. We present PET-DINOv2-2D, the first DINOv2 model pre-trained on 2D PET, and benchmark it against open-source encoders: the origi- nal DINOv2 (pre-trained on the LVD-142M natural-image dataset) and OmniRad (pre-trained on CT, MRI and ultrasound). Using the same lightweight heads for every backbone, and despite far less pre-training data, PET-DINOv2-2D matches or outperforms both on three down- stream PET tasks: normal/abnormal classification, lesion segmentation and recurrence-free survival prognosis. Its advantage is largest when few labels are available, suggesting that PET pre-training gives more transferable, label-efficient features. Code is made available at this https URL.

---


### 350. [Segment Anything Model Based Context Guided Mamba Unet for Medical Image Segmentation](https://arxiv.org/abs/2610.40029)

**<font color=#1a73e8>作者：</font>** Chenchen Wang, You Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image segmentation is crucial for clinical diagnosis and treatment planning, requiring both global contextual understanding and fine-grained structural precision. While the Segment Anything Model (SAM) demonstrates strong generalization capabilities, its direct application to medical images often lacks domain-specific adaptability. Meanwhile, State Space Models (SSMs)-based methods, such as Mamba, efficiently capture long-range dependencies but may struggle with preserving fine anatomical details. To address these challenges, we propose a segment anything model based context guided mamba unet, SAMBA-UNet, a novel framework that integrates SAM's context knowledge with Mamba's hierarchical feature learning to enhance both global representation and local detail refinement. Specifically, we introduce the Hierarchical Context Enhancement Module (HCEM), an attention-based fusion module that deeply incorporates the multi-level features of SAM and Mamba to improve detail perception and segmentation precision. Additionally, we employ LoRA and Adapter-based fine-tuning to adapt SAM to medical imaging tasks, further enhancing its domain-specific segmentation capability and robustness. We conducted a comprehensive study on several medical segmentation datasets, including Synapse, ISIC17, and ISIC18, evaluating our method across multiple metrics. Experimental results demonstrate that SAMBA-UNet achieves state-of-the-art performance, effectively balancing generalization, segmentation accuracy, and computational efficiency. Our code will be released upon acceptance.

---


> [!TIP]
> 当前位于：**301-350**（第 7/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-432](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
