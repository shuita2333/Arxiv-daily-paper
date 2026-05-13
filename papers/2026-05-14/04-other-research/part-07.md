# 📦 其他研究 | 2026年05月14日

> 本类共 **396** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-396](./part-08.md)

---

### 301. [MoCam: Unified Novel View Synthesis via Structured Denoising Dynamics](https://arxiv.org/abs/2605.12119)

**<font color=#1a73e8>作者：</font>** Haofeng Liu, Yang Zhou, Ziheng Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative novel view synthesis faces a fundamental dilemma: geometric priors provide spatial alignment but become sparse and inaccurate under view changes, while appearance priors offer visual fidelity but lack geometric correspondence. Existing methods either propagate geometric errors throughout generation or suffer from signal conflicts when fusing both statically. We introduce MoCam, which employs structured denoising dynamics to orchestrate a coordinated progression from geometry to appearance within the diffusion this http URL first leverages geometric priors in early stages to anchor coarse structures and tolerate their incompleteness, then switches to appearance priors in later stages to actively correct geometric errors and refine details. This design naturally unifies static and dynamic view synthesis by temporally decoupling geometric alignment and appearance refinement within the diffusion this http URL demonstrate that MoCam significantly outperforms prior methods, particularly when point clouds contain severe holes or distortions, achieving robust geometry-appearance disentanglement.

---


### 302. [Disentangled Sparse Representations for Concept-Separated Diffusion Unlearning](https://arxiv.org/abs/2605.12122)

**<font color=#1a73e8>作者：</font>** Hyeonjin Kim, Hangyeol Jung, Heechan Yun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unlearning specific concepts in text-to-image diffusion models has become increasingly important for preventing undesirable content generation. Among prior approaches, sparse autoencoder (SAE)-based methods have attracted attention due to their ability to suppress target concepts through lightweight manipulation of latent features, without modifying model parameters. However, SAEs trained with sparse reconstruction objectives do not explicitly enforce concept-wise separation, resulting in shared latent features across concepts. To address this, we propose SAEParate, which organizes latent representations into concept-specific clusters via a concept-aware contrastive objective, enabling more precise concept suppression while reducing unintended interference during unlearning. In addition, we enhance the encoder with a GeLU-based nonlinear transformation to increase its expressive capacity under this separation objective, enabling a more discriminative and disentangled latent space. Experiments on UnlearnCanvas demonstrate state-of-the-art performance, with particularly strong gains in joint style-object unlearning, a challenging setting where existing methods suffer from severe interference between target and non-target concepts.

---


### 303. [Rollout Cards: A Reproducibility Standard for Agent Research](https://arxiv.org/abs/2605.12131)

**<font color=#1a73e8>作者：</font>** Charlie Masters, Ziyuan Liu, Stefano V. Albrecht  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reproducibility problems that have long affected machine learning and reinforcement learning are now surfacing in agent research: papers compare systems by reported scores while leaving the rollout records behind those scores difficult to inspect. For agentic tasks, this matters because the same behaviour can receive different reported scores when evaluations select different parts of a rollout or apply different reporting rules. In a structured audit of 50 popular training and evaluation repositories, we find that none report how many runs failed, errored, or were skipped alongside headline scores. We also document 37 cases where reporting rules can change task-success rates, cost/token accounting, or timing measurements for fixed evidence, sometimes dramatically. We treat rollout records, not reported scores, as the unit of reproducibility for agent research. We introduce rollout cards: publication bundles that preserve the rollout record and declare the views, reporting rules, and drops manifests behind reported scores. We validate rollout cards in two settings. First, four partial public releases in tool safety, multi-agent systems, theorem proving, and search let us compute analyses their original reports did not include. Second, re-grading preserved benchmark outputs across short-answer, code-generation, and tool-use tasks shows that changing only the reporting rule can change reported scores by 20.9 absolute percentage points and, in some cases, invert rankings of frontier models. We release a reference implementation integrated into Ergon, an open-source reinforcement learning gym, and publicly publish Ergon-produced rollout-card exports for benchmarks spanning tool use, software engineering, web interaction, multi-agent coordination, safety, and search to support future research.

---


### 304. [MULTI: Disentangling Camera Lens, Sensor, View, and Domain for Novel Image Generation](https://arxiv.org/abs/2605.12134)

**<font color=#1a73e8>作者：</font>** Sonali Godavarthy, Matthias Neuwirth-Trapp, Tim-Felix Faasch 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent text-to-image models produce high-quality images, yet text ambiguity hinders precise control when specific styles or objects are required. There have been a number of recent works dealing with learning and composing multiple objects and patterns. However, current work focuses almost entirely on image content, overlooking imaging factors such as camera lens, sensor types, imaging viewpoints, and scenes' domain characteristics. We introduce this new challenge as Imaging Factor Disentanglement and show limitations of current approaches in the regime. We, therefore, propose the new method Multi-factor disentanglement through Textual Inversion (MULTI). It consists of two stages: in the first stage, we learn general factors, and in the second stage, we extract dataset-specific ones. This setup enables the extension of existing datasets and novel factor combinations, thereby reducing distribution gaps. It further supports modifications of specific factors and image-to-image generation via ControlNets. The evaluation on our new DF-RICO benchmark demonstrates the effectiveness of MULTI and highlights the importance of Factor Disentanglement as a new direction of research.

---


### 305. [Design Your Ad: Personalized Advertising Image and Text Generation with Unified Autoregressive Models](https://arxiv.org/abs/2605.12138)

**<font color=#1a73e8>作者：</font>** Yexing Xu, Wei Feng, Shen Zhang 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating realistic and user-preferred advertisements is a key challenge in e-commerce. Existing approaches utilize multiple independent models driven by click-through-rate (CTR) to controllably create attractive image or text advertisements. However, their pipelines lack cross-modal perception and rely on CTR that only reflects average preferences. Therefore, we explore jointly generating personalized image-text advertisements from historical click behaviors. We first design a Unified Advertisement Generative model (Uni-AdGen) that employs a single autoregressive framework to produce both advertising images and texts. By incorporating a foreground perception module and instruction tuning, Uni-AdGen enhances the realism of the generated content. To further personalize advertisements, we equip Uni-AdGen with a coarse-to-fine preference understanding module that effectively captures user interests from noisy multimodal historical behaviors to drive personalized generation. Additionally, we construct the first large-scale Personalized Advertising image-text dataset (PAd1M) and introduce a Product Background Similarity (PBS) metric to facilitate training and evaluation. Extensive experiments show that our method outperforms baselines in general and personalized advertisement generation. Our project is available at this https URL.

---


### 306. [EchoTracker2: Enhancing Myocardial Point Tracking by Modeling Local Motion](https://arxiv.org/abs/2605.12140)

**<font color=#1a73e8>作者：</font>** Md Abulkalam Azad, Vegard Holmstrøm, John Nyberg 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Myocardial point tracking (MPT) has recently emerged as a promising direction for motion estimation in echocardiography, driven by advances in general-purpose point tracking methods. However, myocardial motion fundamentally differs from motion encountered in natural videos, as it arises from physiologically constrained deformation that is spatially and temporally continuous throughout the cardiac cycle. Consequently, motion trajectories typically remain locally confined despite substantial tissue deformation. Motivated by these properties, we revisit the architectural design for MPT and find that coarse initialization in commonly used two-stage coarse-to-fine architectures may be unnecessary in this domain. In this work, we propose a fine-stage-only architecture, \textbf{EchoTracker2}, which enriches pixel-precise features with local spatiotemporal context and integrates them with long-range joint temporal reasoning for robust tracking. Experimental results across in-distribution, out-of-distribution (OOD), and public synthetic datasets show that our model improves position accuracy by $6.5\%$ and reduces median trajectory error by $12.2\%$ relative to a domain-specific state-of-the-art (SOTA) model. Compared to the best general-purpose point tracking method, the improvements are $2.0\%$ and $5.3\%$, respectively. Moreover, EchoTracker2 shows better agreement with expert-derived global longitudinal strain (GLS) and enhances test-rest reproducibility. Source code will be available at: this https URL.

---


### 307. [PoseCompass: Intelligent Synthetic Pose Selection for Visual Localization](https://arxiv.org/abs/2605.12144)

**<font color=#1a73e8>作者：</font>** Yanan Zhou, Zhaoyan Qian, Yanli Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In visual localization, Absolute Pose Regression (APR) enables real-time 6-DoF camera pose inference from single images, yet critically depends on fine-tuning data quality and coverage. While recent methods leverage 3D Gaussian Splatting (3DGS) for novel view synthesis-based data augmentation, random sampling generates redundant views and noisy samples from poorly reconstructed regions. To mitigate this research gap, we propose PoseCompass, an intelligent pose selection pipeline for 3DGS-based APR. PoseCompass formulates synthetic pose selection and derives a value-based pose ranking mechanism to identify informative poses. The ranking integrates three dimensions: Localization Difficulty, favoring challenging regions; Coverage Novelty, exploring under-sampled areas; and Rendering Observability, filtering artifacts and noise. PoseCompass then generates trajectory-constrained candidates, selects the top-K ranked poses, and synthesizes views using 3DGS with lightweight diffusion-based alignment. Finally, the pose regressor is fine-tuned on mixed real and synthetic data. We evaluate PoseCompass on 7-Scenes, where it reduces adaptation time from 15.2 to 5.1 minutes, a 3x speedup, while cutting median pose errors by 53.8 percent and significantly outperforming random baselines.

---


### 308. [Cross-Modal-Domain Generalization Through Semantically Aligned Discrete Representations](https://arxiv.org/abs/2605.12145)

**<font color=#1a73e8>作者：</font>** Souptik Sen, Raneen Younis, Zahra Ahmadi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal learning seeks to integrate information across diverse sensory sources, yet current approaches struggle to balance cross-modal generalizability with modality-specific structure. Continuous (implicit) methods preserve fine-grained priors but render generalization challenging, while discrete (explicit) approaches enforce shared prototypes at the expense of modality specificity. We introduce CoDAAR (Cross-modal Discrete Alignment And Reconstruction), a novel framework that resolves this long-standing trade-off by establishing semantic consensus across modality-specific codebooks through index-level alignment. This design uniquely allows CoDAAR to preserve modality-unique structures while achieving generalizable cross-modal representations within a unified discrete space. CoDAAR combines two complementary mechanisms: Discrete Temporal Alignment (DTA), which enables fine-grained temporal quantization, and Cascading Semantic Alignment (CSA), which promotes progressive cross-modal semantic agreement. Together, they establish a competition-free unified representation space. Trained with self-supervised reconstruction objectives on paired multimodal sequences, CoDAAR demonstrates robust cross-modal and cross-domain generalization. Across Cross-Modal Generalization benchmarks, including event classification, localization, video segmentation, and cross-dataset transfer, CoDAAR achieves state-of-the-art performance, establishing a new paradigm for discrete and generalizable multimodal representation learning.

---


### 309. [Latent Causal Void: Explicit Missing-Context Reconstruction for Misinformation Detection](https://arxiv.org/abs/2605.12156)

**<font color=#1a73e8>作者：</font>** Hui Li, Zhongquan Jian, Jinsong Su 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic misinformation detection performs well when deception is visible in what an article explicitly states. However, some misinformation articles remain locally coherent and only become misleading once compared with contemporaneous reports that supply background facts the article omits. We study this omission-relevant setting and observe that current omission-aware approaches typically either attach retrieved context as auxiliary evidence or infer a categorical omission signal, leaving the specific missing fact implicit. We propose \emph{Latent Causal Void} (LCV), a retrieval-guided detector that explicitly reconstructs the missing fact for each target sentence and uses it as a textual cross-source relation in graph reasoning. Concretely, LCV retrieves temporally aligned context articles, asks a frozen instruction-tuned large language model to generate a short missing-context description for each sentence--article pair, and feeds the resulting relation text into a heterograph over target sentences and context articles. On the bilingual benchmark of Sheng et al., LCV improves over the strongest omission-aware baseline by $2.56$ and $2.84$ macro-F1 points on the English and Chinese splits, respectively. The results indicate that modeling the missing cross-source fact itself, rather than only attaching retrieved evidence or predicting an omission signal, is a useful representation for omission-aware misinformation detection.

---


### 310. [ALGOGEN: Tool-Generated Verifiable Traces for Reliable Algorithm Visualization](https://arxiv.org/abs/2605.12159)

**<font color=#1a73e8>作者：</font>** Kunpeng Liao, Yuexiao Ma, Yisheng Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Algorithm Visualization (AV) helps students build mental models by animating algorithm execution states. Recent LLM-based systems such as CODE2VIDEO generate AV videos in an end-to-end manner. However, this paradigm requires the system to simultaneously simulate algorithm flow and satisfy video rendering constraints, such as element layout and color schemes. This complex task induces LLM hallucinations, resulting in reduced execution success rates, element overlap, and inter-frame inconsistencies.
To address these challenges, we propose ALGOGEN, a novel paradigm that decouples algorithm execution from rendering. We first introduce Visualization Trace Algebra (VTA), a monoid over algorithm visual states and operations. The LLM then generates a Python tracker that simulates algorithm flow and outputs VTA-JSON traces, a JSON encoding of VTA. For rendering, we define a Rendering Style Language (RSL) to templatize algorithm layouts. A deterministic renderer then compiles algorithm traces with RSL into Manim, LaTeX/TikZ, or this http URL outputs.
Evaluated on a LeetCode AV benchmark of 200 tasks, ALGOGEN achieves an average success rate improvement of 17.3% compared to end-to-end methods, with 99.8% versus 82.5%. These results demonstrate that our decoupling paradigm effectively mitigates LLM hallucinations in complex AV tasks, providing a more reliable solution for automated generation of high-quality algorithm visualizations. Demo videos and code are available in the project repository.

---


### 311. [Fused Gromov-Wasserstein Distance with Feature Selection](https://arxiv.org/abs/2605.12161)

**<font color=#1a73e8>作者：</font>** Harlin Lee, Ying Yu, Mingxin Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fused Gromov-Wasserstein (FGW) distances provide a principled framework for comparing objects by jointly aligning structure and node features. However, existing FGW formulations treat all features uniformly, which limits interpretability and robustness in high-dimensional settings where many features may be irrelevant or noisy. We introduce FGW distances with feature selection, which incorporate adaptive feature suppression weights into the FGW objective to selectively downweight or suppress differentiating features during alignment. We propose two approaches: (1) regularized FGW with Lasso and Ridge penalties, and (2) FGW with simplex-constrained weights, including groupwise extensions. We analyze the resulting models and establish their key theoretical properties, including bounds relative to classical FGW and Gromov-Wasserstein distances, and metric behavior. An efficient alternating minimization algorithm is developed. Experiments illustrate how feature suppression enhances interpretability and reveals task-relevant structure, with a special application to computational redistricting.

---


### 312. [On What We Can Learn from Low-Resolution Data](https://arxiv.org/abs/2605.12168)

**<font color=#1a73e8>作者：</font>** Theresa Dahl Frehr, Niels Henrik Pontoppidan, Hiba Nassar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence systems typically rely on large, centrally collected datasets, a premise that does not hold in many real-world domains such as healthcare and public institutions. In these settings, data sharing is often constrained by storage, privacy, or resource limitations. For example, small wearable devices may lack the bandwidth or energy capacity needed to store and transmit high-resolution data, leading to aggregation during data collection and thus a loss of information. As a result, datasets collected from different sources may consist of a mixture of high- and low-resolution samples. Despite the prevalence of this setting, it remains unclear how informative low-resolution data is when models are ultimately evaluated on high-resolution inputs. We provide a theoretical analysis based on the Kullback-Leibler divergence that characterises how the influence of a datapoint changes with resolution, and derive bounds that relate the relative contribution of high- and low-resolution observations to the information lost under downsampling. To support this analysis, we empirically demonstrate, using both a vision transformer and a convolutional neural network, that adding low-resolution data to the training set consistently improves performance when high-resolution data is scarce.

---


### 313. [UniFixer: A Universal Reference-Guided Fixer for Diffusion-Based View Synthesis](https://arxiv.org/abs/2605.12169)

**<font color=#1a73e8>作者：</font>** Sihan Chen, Xiang Zhang, Yang Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the recent surge of generative models, diffusion-based approaches have become mainstream for view synthesis tasks, either in an explicit depth-warp-inpaint or in an implicit end-to-end manner. Despite their success, both paradigms often suffer from noticeable quality degradation, e.g., blurred details and distorted structures, caused by pixel-to-latent compression and diffusion hallucination. In this paper, we investigate diffusion degradation from three key dimensions (i.e., spatial, temporal, and backbone-related) and propose UniFixer, a universal reference-guided framework that fixes diverse degradation artifacts via a coarse-to-fine strategy. Specifically, a reference pre-alignment module is first designed to perform coarse alignment between the reference view and the degraded novel view. A global structure anchoring mechanism then rectifies geometric distortions to ensure structural fidelity, followed by a local detail injection module that recovers fine-grained texture details for high-quality view synthesis. Our UniFixer serves as a plug-and-play refiner that achieves zero-shot fixing across different types of diffusion degradation, and extensive experiments verify our state-of-the-art performance on novel view synthesis and stereo conversion.

---


### 314. [ACTING: A Platform for Cyber Ranges Federation](https://arxiv.org/abs/2605.12170)

**<font color=#1a73e8>作者：</font>** Kyriakos Christou, Maria Michalopoulou, Stefano Taggi 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyber Defence (CD) training requires interoperable cyber-range environments capable of supporting complex, multidomain exercises across distributed infrastructures. This paper presents three main contributions addressing this challenge. First, we introduce the Exercise Description Language - First Generation (EDL-FG), a structured language for formally describing cyber-range training services and exercises. EDL-FG captures both the technical infrastructure required to emulate ICT/OT environments and the scenario logic governing cyber events, injects, and participant interactions, enabling interoperable and automated scenario deployment across federated Cyber Ranges (CRs). Second, the ACTING platform introduces automated PE and scoring mechanisms that assess trainee actions during exercises through coordinated data collection and analysis across participating CRs. Third, the platform enables multi-domain cyber training scenarios that combine civilian and military operational contexts. Building upon federation capabilities established under the H2020 ECHO project, ACTING demonstrates how interoperable scenario description and automated evaluation support scalable and realistic CD training.

---


### 315. [Lower bounds for one-layer transformers that compute parity](https://arxiv.org/abs/2605.12171)

**<font color=#1a73e8>作者：</font>** Daniel Hsu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This note shows that no self-attention layer post-processed by a rational function can sign-represent the parity function unless the product of the number of heads and the degree of the post-processing function grows linearly with the input length. Combining this lower bound with rational approximation of ReLU networks yields a margin-dependent extension for self-attention layers post-processed by ReLU networks.

---


### 316. [Expected Batch Optimal Transport Plans and Consequences for Flow Matching](https://arxiv.org/abs/2605.12174)

**<font color=#1a73e8>作者：</font>** Samuel Boïté, Julie Delon, Kimia Nadjahi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Solving optimal transport (OT) on random minibatches is a common surrogate for exact OT in large-scale learning. In flow matching (FM), this surrogate is used to obtain OT-like couplings that can straighten probability paths and reduce numerical integration cost. Yet, the population-level coupling induced by repeated minibatch OT remains only partially understood. We formalize this coupling as the expected batch OT plan $\overline{\pi}_{k}$, obtained by averaging empirical OT plans over independent minibatches of size $k$. We then establish its large-batch consistency and, in the semidiscrete case relevant to generative modeling, derive rates for both the transport-cost bias and the convergence of $\overline{\pi}_{k}$ to the OT plan. For FM, this yields a population coupling whose induced velocity field is regular enough to define a unique flow from the source to the discrete target. We finally quantify how OT batch size interacts with numerical integration in a tractable two-atom model and in synthetic and image experiments.

---


### 317. [Multi-Task Representation Learning for Conservative Linear Bandits](https://arxiv.org/abs/2605.12176)

**<font color=#1a73e8>作者：</font>** Jiabin Lin, Shana Moothedath  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents the Constrained Multi-Task Representation Learning (CMTRL) framework for linear bandits. We consider T linear bandit tasks in a d dimensional space, which share a common low-dimensional representation of dimension r, where r is much smaller than the minimum of d and T. Furthermore, tasks are constrained so that only actions meeting specific safety or performance requirements are allowed, referred to as conservative (safe) bandits. We introduce a novel algorithm, Safe-Alternating projected Gradient Descent and minimization (Safe-AltGDmin), to recover a low-rank feature matrix while satisfying the given constraints. Building on this algorithm, we propose a multi-task representation learning framework for conservative linear bandits and establish theoretical guarantees for its regret and sample complexity bounds. We presented experiments and compared the performance of our algorithm with benchmark algorithms.

---


### 318. [DriftXpress: Faster Drifting Models via Projected RKHS Fields](https://arxiv.org/abs/2605.12183)

**<font color=#1a73e8>作者：</font>** Ali Falahati, Elliot Creager, Gautam Kamath 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Drifting Models have emerged as a new paradigm for one-step generative modeling, achieving strong image quality without iterative inference. The premise is to replace the iterative denoising process in diffusion models with a single evaluation of a generator. However, this creates a different trade-off: drifting reduces inference cost by moving much of the computation into training. We introduce DriftXpress, an accelerated formulation of drifting models based on projected RKHS fields. DriftXpress approximates the drifting kernel in a low-rank feature space. This preserves the attraction-repulsion structure of the original drifting field while reducing the cost of field evaluation. Across image-generation benchmarks, DriftXpress achieves comparable FID to standard drifting while reducing wall-clock training cost. These results show that the training-inference trade-off of drifting models can be pushed further without giving up their one-step inference advantage.

---


### 319. [Fair Conformal Classification via Learning Representation-Based Groups](https://arxiv.org/abs/2605.12195)

**<font color=#1a73e8>作者：</font>** Senrong Xu, Yanke Zhou, Yuhao Tan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conformal prediction methods provide statistically rigorous marginal coverage guarantees for machine learning models, but such guarantees fail to account for algorithmic biases, thereby undermining fairness and trust. This paper introduces a fair conformal inference framework for classification tasks. The proposed method constructs prediction sets that guarantee conditional coverage on adaptively identified subgroups, which can be implicitly defined through nonlinear feature combinations. By balancing effectiveness and efficiency in producing compact, informative prediction sets and ensuring adaptive equalized coverage across unfairly treated subgroups, our approach paves a practical pathway toward trustworthy machine learning. Extensive experiments on both synthetic and real-world datasets demonstrate the effectiveness of the framework.

---


### 320. [ECTO: Exogenous-Conditioned Temporal Operator for Ultra-Short-Term Wind Power Forecasting](https://arxiv.org/abs/2605.12196)

**<font color=#1a73e8>作者：</font>** Cao Yuan, Junjun Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate ultra-short-term wind power forecasting is critical for grid dispatch and reserve management, yet remains challenging due to the non-stationary, condition-dependent nature of wind generation. Meteorological exogenous variables carry substantial predictive information, but the most informative variable combination varies across sites, operating conditions, and prediction horizons. Existing deep learning approaches either treat exogenous inputs as generic auxiliary channels through uniform mixing or soft gating, or rely on fixed preprocessing steps such as PCA, without exploiting the physical structure of meteorological variables. We propose ECTO (Exogenous-Conditioned Temporal Operator), a unified framework that decomposes exogenous variable modeling into two complementary modules. Physically-Grounded Variable Selection (PGVS) performs hierarchical, group-aware sparse selection over exogenous variables using a domain-informed physical prior and sparsemax activations, producing a compact, condition-adaptive exogenous context. Exogenous-Conditioned Regime Refinement (ECRR) routes the forecast through learned regime experts that apply gain--bias calibration and horizon-specific corrections via a mixture-of-experts paradigm. Experiments on three wind farms spanning different climates, capacities (66--200 MW), and exogenous dimensions (11--13 variables) demonstrate that ECTO achieves the lowest MSE across all sites, with relative improvements over the strongest baseline ranging from 2.2% to 5.2%, widening to 8.6% at the longer prediction horizon ($H=32$). Ablation analysis confirms that each exogenous-related component contributes positively (PGVS +1.84%, ECRR +2.86%), and interpretability analysis reveals that PGVS learns physically meaningful, site-specific variable selection patterns, while ECRR converges to well-separated calibration strategies consistent across sites.

---


### 321. [Enhancing Domain Generalization in 3D Human Pose Estimation through Controllable Generative Augmentation](https://arxiv.org/abs/2605.12198)

**<font color=#1a73e8>作者：</font>** Xinhao Hu, Yiyi Zhang, Liqing Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pedestrian motion, due to its causal nature, is strongly influenced by domain gaps arising from discrepancies between training and testing data distributions. Focusing on 3D human pose estimation, this work presents a controllable human pose generation framework that synthesizes diverse video data by systematically varying poses, backgrounds, and camera viewpoints. This generative augmentation enriches training datasets, enhances model generalization, and alleviates the limitations of existing methods in handling domain discrepancies. By leveraging both indoor/real-world and outdoor/virtual datasets, we perform cross-domain data fusion and controllable video generation to construct enriched training data, tailored to realistic deployment settings. Extensive experiments show that the augmented datasets significantly improve model performance on unseen scenarios and datasets, validating the effectiveness of the proposed approach.

---


### 322. [Investigating simple target-covariate relationships for Chronos-2 and TabPFN-TS](https://arxiv.org/abs/2605.12200)

**<font color=#1a73e8>作者：</font>** Gaspard Berthelier, Mariia Baranova, Andrei-Tiberiu Pantea 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time Series Foundation Models (TSFMs) have recently achieved state-of-the-art performance, often outperforming supervised models in zero-shot settings. Recent TSFM architectures, such as Chronos-2 and TabPFN-TS, aim to integrate covariates. In this paper, we design controlled experiments based on simple target-covariate relationships to assess this integration capability. Our results show that TabPFN-TS captures these relationships more effectively than Chronos-2, especially for short horizons, suggesting that the strong benchmark performance of Chronos-2 does not automatically translate into optimal modeling of simple covariate-target dependencies.

---


### 323. [On the Importance of Multistability for Horizon Generalization in Reinforcement Learning](https://arxiv.org/abs/2605.12206)

**<font color=#1a73e8>作者：</font>** Asad Bakija, Florent De Geeter, Julien Brandoit 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In reinforcement learning (RL), agents acting in partially observable Markov decision processes (POMDPs) must rely on memory, typically encoded in a recurrent neural network (RNN), to integrate information from past observations. Long-horizon POMDPs, in which the relevant observation and the optimal action are separated by many time steps (called the horizon), are particularly challenging: training suffers from poor generalization, severe sample inefficiency, and prohibitive exploration costs. Ideally, an agent trained on short horizons would retain optimal behavior at arbitrarily longer ones, but no formal framework currently characterizes when this is achievable. To fill this gap, we formalized temporal horizon generalization, the property that a policy remains optimal for all horizons, derived a necessary and sufficient condition for it, and experimentally evaluated the ability of nonlinear and parallelizable RNN variants to achieve it. This paper presents the resulting theoretical framework, the empirical evaluation, and the dynamical interpretation linking RNN behavior to temporal horizon generalization. Our analyses reveal that multistability is necessary for temporal horizon generalization and, in simple tasks, sufficient; more complex tasks further require transient dynamics. In contrast, modern parallelizable architectures, namely state space models and gated linear RNNs, are monostable by construction and consequently fail to generalize across temporal horizons. We conclude that multistability and transient dynamics are two essential and complementary dynamical regimes for horizon generalization, and that no current parallelizable RNN exhibits both. Designing parallelizable architectures that combine these regimes thus emerges as a key direction for scalable long-horizon RL.

---


### 324. [Not How Many, But Which: Parameter Placement in Low-Rank Adaptation](https://arxiv.org/abs/2605.12207)

**<font color=#1a73e8>作者：</font>** Arijit Sehanobish, Charles Lovering  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the \textit{parameter placement problem}: given a fixed budget of $k$ trainable entries within the B matrix of a LoRA adapter (A frozen), does the choice of which $k$ matter? Under supervised fine-tuning, random and informed subsets achieve comparable performance. Under GRPO on base models, random placement fails to improve over the base model, while gradient-informed placement recovers standard LoRA accuracy. This regime dependence traces to gradient structure: SFT gradients are low-rank and directionally stable, so any subset accumulates coherent updates; GRPO gradients are high-rank and near-orthogonal across steps, so only elements with consistently signed gradients retain the learning signal. Our scoring procedure identifies these critical parameters in under 10 seconds at less than 0.5% of training cost. Selected parameters concentrate on residual-stream-writing projections (V, O, Down), stable across model families and scales (1.5B - 8B).

---


### 325. [ORCHID: Orchestrated Reduction Consensus for Hash-based Integrity in Distributed Ledgers](https://arxiv.org/abs/2605.12211)

**<font color=#1a73e8>作者：</font>** Abraham Itzhak Weinberg  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present \textbf{ORCHID} (\textit{Orchestrated Reduction Consensus for Hash-based Integrity in Distributed Ledgers}), a novel bio-inspired consensus protocol that maps the neuroscientific \emph{binding problem} -- how the brain integrates distributed neural oscillations into a unified conscious percept -- onto the distributed systems \emph{consensus problem}, how blockchain nodes agree on a single ledger state under Byzantine faults. Grounded in the Penrose--Hameroff Orchestrated Objective Reduction (Orch~OR) hypothesis and the Kuramoto synchronisation model, ORCHID equips each node with a quantum-noisy phase oscillator; consensus is triggered when the network's order parameter $r(t)$ crosses a \emph{binding threshold} $\theta_b$, mirroring the gamma-band binding event in conscious perception. ORCHID is further strengthened by a coherence-weighted Quantum Secret Sharing (QSS) layer, extending the survey framework of Weinberg to a concrete consensus application. Simulation results on Watts--Strogatz small-world networks ($n=10$--$150$) demonstrate: (i)~the Kuramoto order parameter reaches $r_{\max}=0.988$ under coupling $K=3.0$, well above the theoretical critical coupling $K_c \approx 1.41$; (ii)~a sharp QSS fidelity phase transition at coherence $c^*\approx 0.82$, confirming Theorem~2; (iii)100\% consensus rate at all tested Byzantine fractions (0\%--40\%), with median convergence under 4~s for $n=30$; and (iv)~ORCHID achieves $O(n{\cdot}k)$ message complexity, outperforming PBFT's $O(n^2)$ at $n\geq150$. These results establish ORCHID as a scalable, biologically plausible, and quantum-augmented consensus mechanism for post-quantum distributed ledgers.

---


### 326. [Learning Ego-Centric BEV Representations from a Perspective-Privileged View: Cross-View Supervision for Online HD Map Construction](https://arxiv.org/abs/2605.12218)

**<font color=#1a73e8>作者：</font>** Daniel Lengerer, Mathias Pechinger, Klaus Bogenberger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bird's-eye-view (BEV) representations derived from multi-camera input have become a central interface for online high-definition (HD) map construction. However, most approaches rely solely on ego-centric supervision, requiring large-scale scene structure to be inferred from incomplete observations, occlusions, and diminishing information density at long range, where perspective effects and spatial sparsity hinder consistent structural reasoning. We introduce Cross-View Supervision (CVS), a representation learning paradigm that transfers geometric and topological priors from an ego-aligned overhead perspective into camera-based BEV encoders. Rather than adding auxiliary semantic losses, CVS aligns representations in a shared BEV feature space and distills globally consistent structural knowledge from a perspective-privileged teacher into the ego-centric backbone. This supervision enhances structural coherence without modifying the inference architecture or requiring overhead input at test time. Experiments on nuScenes using ego-aligned aerial imagery from the AID4AD cross-view extension demonstrate consistent improvements over StreamMapNet while maintaining identical camera-only inference. CVS yields +3.9\,mAP in the standard $60\times30\,\mathrm{m}$ region and +9.9\,mAP in the extended $100\times50\,\mathrm{m}$ setting, corresponding to a 44\% relative gain at long range. These results highlight perspective-privileged structural supervision as a promising training principle for improving BEV representation learning in HD map construction.

---


### 327. [TriBand-BEV: Real-Time LiDAR-Only 3D Pedestrian Detection via Height-Aware BEV and High-Resolution Feature Fusion](https://arxiv.org/abs/2605.12220)

**<font color=#1a73e8>作者：</font>** Mohammad Khoshkdahan, Alexey Vinel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Safe autonomous agents and mobile robots need fast real time 3D perception, especially for vulnerable road users (VRUs) such as pedestrians. We introduce a new bird's eye view (BEV) encoding, which maps the full 3D LiDAR point cloud into a light-weight 2D BEV tensor with three height bands. We explicitly reformulate 3D detection as a 2D detection problem and then reconstruct 3D boxes from the BEV outputs. A single network detects cars, pedestrians, and cyclists in one pass. The backbone uses area attention at deep stages, a hierarchical bidirectional neck over P1 to P4 fuses context and detail, and the head predicts oriented boxes with distribution focal learning for side offsets and a rotated IoU loss. Training applies a small vertical re bin and a mild reflectance jitter in channel space to resist memorization. We use an interquartile range (IQR) filter to remove noisy and outlier LiDAR points during 3D reconstruction. On KITTI dataset, TriBand-BEV attains 58.7/52.6/47.2 pedestrian BEV AP(%) for easy, moderate, and hard at 49 FPS on a single consumer GPU, surpassing Complex-YOLO, with gains of +12.6%, +7.5%, and +3.1%. Qualitative scenes show stable detection under occlusion. The pipeline is compact and ready for real time robotic deployment. Our source code is publicly available on GitHub.

---


### 328. [Intrinsic Vicarious Conditioning for Deep Reinforcement Learning](https://arxiv.org/abs/2605.12224)

**<font color=#1a73e8>作者：</font>** Rodney A Sanchez, Ferat Sahin, Alex Ororbia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Advancements in reinforcement learning have produced a variety of complex and useful intrinsic driving forces; crucially, these drivers operate under a direct conditioning paradigm. This form of conditioning limits our agents' capacity by restricting how they learn from the environment as well as from others. Off-policy or learn-by-example methods can learn from demonstrators' representations, but they require access to the demonstrating agent's policies or their reward functions. Our work overcomes this direct sampling limitation by introducing vicarious conditioning as an intrinsic reward mechanism. We draw from psychological and biological literature to provide a foundation for vicarious conditioning and use memory-based methods to implement its four steps: attention, retention, reproduction, and reinforcement. Crucially, our vicarious conditioning paradigms support low-shot learning and do not require the demonstrator agent's policy nor its reward functions. We evaluate our approach in the MiniWorld Sidewalk environment, one of the few public environments that features a non-descriptive terminal condition (no reward provided upon agent death), and extend it to Box2D's CarRacing environment. Our results across both environments demonstrate that vicarious conditioning enables longer episode lengths by discouraging the agent from non-descriptive terminal conditions and guiding the agent toward desirable states. Overall, this work emulates a cognitively-plausible learning paradigm better suited to problems such as single-life learning or continual learning.

---


### 329. [Mechanistic Interpretability of ASR models using Sparse Autoencoders](https://arxiv.org/abs/2605.12225)

**<font color=#1a73e8>作者：</font>** Dan Pluth, Zachary Nicholas Houghton, Yu Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding the internal machinations of deep Transformer-based NLP models is more crucial than ever as these models see widespread use in various domains that affect the public at large, such as industry, academia, finance, health. While these models have advanced rapidly, their internal mechanisms remain largely a mystery. Techniques such as Sparse Autoencoders (SAE) have emerged to understand these mechanisms by projecting dense representations into a sparse vector. While existing research has demonstrated the viability of the SAE in interpreting text-based Large Language Models (LLMs), there are no equivalent studies that demonstrate the application of a SAE to audio processing models like Automatic Speech Recognizers (ASRs). In this work, a SAE is applied to Whisper, a Transformer-based ASR, training a high-dimensional sparse latent space on frame-level embeddings extracted from the Whisper encoder. Our work uncovers diverse monosemantic features across linguistic and non-linguistic boundaries, and demonstrates cross-lingual feature steering. This work establishes the viability of a SAE model and demonstrates that Whisper encodes a rich amount of linguistic information.

---


### 330. [UHR-Micro: Diagnosing and Mitigating the Resolution Illusion in Earth Observation VLMs](https://arxiv.org/abs/2605.12237)

**<font color=#1a73e8>作者：</font>** Shuo Ni, Tong Wang, Jing Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) increasingly operate on ultra-high-resolution (UHR) Earth observation imagery, yet they remain vulnerable to a severe scale mismatch between large-scale scene context and micro-scale targets. We refer to this empirical gap as a "resolution illusion": higher input resolution provides the appearance of richer visual detail, but does not necessarily yield reliable perception of spatially small, task-relevant evidence. To benchmark this challenge, we introduce UHR-Micro, a benchmark comprising 11,253 instructions grounded in 1,212 UHR images, designed to evaluate VLMs at the spatial limits of native Earth observation imagery. UHR-Micro spans diverse micro-target scales, context requirements, task families, and visual conditions, and provides diagnostic annotations that support controlled evaluation and fine-grained error attribution. Experiments with representative high-resolution VLMs show substantial failures in spatial grounding and evidence parsing, despite access to high-resolution inputs. Further analysis suggests that these failures are not fully resolved by increasing model capacity, but are closely tied to insufficient guidance in locating and using task-relevant micro-evidence. Motivated by this finding, we propose Micro-evidence Active Perception (MAP), a reference agent that decomposes queries into evidence-seeking steps, actively inspects candidate regions, and grounds its answers in localized observations. MAP-Agent improves micro-level perception by making high-resolution reasoning evidence-centered rather than image-centered. Together, UHR-Micro and MAP-Agent provide a diagnostic platform for evaluating, understanding, and advancing high-resolution reasoning in Earth observation VLMs. Datasets and source code were released at this https URL.

---


### 331. [PreScam: A Benchmark for Predicting Scam Progression from Early Conversations](https://arxiv.org/abs/2605.12243)

**<font color=#1a73e8>作者：</font>** Weixiang Sun, Shang Ma, Yiyang Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational scams, such as romance and investment scams, are emerging as a major form of online fraud. Unlike one-shot scam lures such as fake lottery or unpaid toll messages, they unfold through multi-turn conversations in which scammers gradually manipulate victims using evolving psychological techniques. However, existing research mainly focuses on static scam detection or synthetic scams, leaving open whether language models can understand how real-world scams progress over time. We introduce PreScam, a benchmark for modeling scam progression from early conversations. Built from user-submitted scam reports, PreScam filters and structures 177,989 raw reports into 11,573 conversational scam instances spanning 20 scam categories. Each instance is hierarchically structured according to the scam lifecycle defined by the proposed scam kill chain, and further annotated at the turn level with scammer psychological actions and victim responses. We benchmark models on two tasks: real-time termination prediction, which estimates whether a conversation is approaching the termination stage, and scammer action prediction, which forecasts the scammer's subsequent actions. Results show a clear gap between surface-level fluency and progression modeling: supervised encoders substantially outperform zero-shot LLMs on real-time termination prediction, while next-action prediction remains only moderately successful even for strong LLMs. Taken together, these results show that current models can capture some scam-related cues, yet still struggle to track how risk escalates and how manipulation unfolds across turns.

---


### 332. [H3D-MarNet: Wavelet-Guided Dual-Path Learning for Metal Artifact Suppression and CT Modality Transformation for Radiotherapy Workflows](https://arxiv.org/abs/2605.12252)

**<font color=#1a73e8>作者：</font>** Mubashara Rehman, Niki Martinel, Michele Avanzo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Metal artifacts in computed tomography (CT) severely degrade image quality, compromising diagnostic accuracy and radiotherapy planning, especially in cancer patients with high-density implants. We propose H3D-MarNet, a two-stage framework for artifact-aware CT domain transformation from kilo-voltage CT (kVCT) to mega-voltage CT (MVCT). In the first stage, a wavelet-based preprocessing module suppresses metal-induced artifacts through frequency-aware denoising while preserving anatomical structures. In second stage, Domain-TransNet performs kVCT-to-MVCT domain transformation using a hybrid volumetric learning architecture. Domain-TransNet integrates a CNN-based encoder to capture fine-grained local anatomical details and a transformer-based encoder to model long-range volumetric dependencies. The complementary representations are fused through an attention-based feature fusion mechanism to ensure spatial and contextual coherence across slices. A multi-stage, attention-guided decoder, supported by deep supervision, progressively reconstructs artifact-suppressed MVCT volumes.
Extensive experiments demonstrate that H3D-MarNet achieves 28.14 dB PSNR and 0.717 SSIM on artifact-affected slices from full dataset, indicating effective metal artifact suppression and anatomical preservation, highlighting its potential for reliable CT modality transformation in clinical radiotherapy workflows.

---


### 333. [Why Conclusions Diverge from the Same Observations: Formalizing World-Model Non-Identifiability via an Inference](https://arxiv.org/abs/2605.12255)

**<font color=#1a73e8>作者：</font>** Toru Takahashi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When people share the same documents and observations yet reach different conclusions, the disagreement often shifts into a judgment that the other party is cognitively defective, irrational, or acting in bad faith. This paper argues that such divergence is better described as a form of non-identifiability inherent in inference and learning, rather than as a defect of the other party. We organize the phenomenon into two levels: (i) $\theta$-level non-identifiability, where conclusions diverge under the same world model $W$ because inference settings differ; and (ii) $W$-level non-identifiability, where repeated use of an inference setting $\theta$ biases data exposure and update rules, causing the learned world model $W$ itself to diverge. We introduce an inference profile $\theta = (R, E, S, D)$, consisting of Reference, Exploration, Stabilization, and Horizon, and show how outputs can split even for the same observation $o$ and the same $W$. We further explain why disagreements tend to project onto a small number of bases -- abstract versus concrete, externalizability, and order versus freedom -- as a consequence of general constraints on learning systems: computational, observational, and coordination constraints. Finally, we relate the framework to deep representation learning, including representation hierarchy, latent-state estimation, and regularization-exploration trade-offs, and illustrate the framework through a case study on AI regulation debates.

---


### 334. [From Image Hashing to Scene Change Detection](https://arxiv.org/abs/2605.12259)

**<font color=#1a73e8>作者：</font>** Anh-Kiet Duong, Marie-Claire Iatrides, Petra Gomez-Krämer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image hashing provides compact representations for efficient storage and retrieval but is inherently limited to global comparison and cannot reason about where changes occur. This limitation prevents hashing from being directly applicable to scene change detection, where spatial localization is essential. In this work, we revisit hashing from a scene change detection perspective and propose HashSCD, a patch-wise hashing framework that enables both efficient global change detection and localized change identification. HashSCD encodes spatially aligned patches into compact hash codes and aggregates them through an XOR-like operation, allowing change detection and localization to be performed directly in the Hamming space without repeated inference on previous images. The model is trained in an unsupervised manner using contrastive learning at both patch and global levels. Experiments demonstrate that HashSCD achieves competitive performance compared to state-of-the-art unsupervised hashing and scene change detection methods, while significantly reducing computational cost and storage requirements.

---


### 335. [PRISM: Pareto-Efficient Retrieval over Intent-Aware Structured Memory for Long-Horizon Agents](https://arxiv.org/abs/2605.12260)

**<font color=#1a73e8>作者：</font>** Jingyi Peng, Zhongwei Wan, Weiting Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon language agents accumulate conversation history far faster than any fixed context window can hold, making memory management critical to both answer accuracy and serving cost. Existing approaches either expand the context window without addressing what is retrieved, perform heavy ingestion-time fact extraction at substantial token cost, or rely on heuristic graph traversal that leaves both accuracy and efficiency on the table. We present PRISM, a training-free retrieval-side framework that treats long-horizon memory as a joint retrieval-and-compression problem over a graph-structured memory. PRISM combines four orthogonal inference-time components: Hierarchical Bundle Search over typed relation paths, Query-Sensitive Edge Costing that aligns traversal with detected query intent, Evidence Compression that compresses the candidate bundle into a compact answer-side context, and Adaptive Intent Routing that routes most queries through zero-LLM tiers. By formulating retrieval as min-cost selection over typed path templates and pairing it with an LLM-side compression step, PRISM surfaces the right evidence under a strict context budget without any fine-tuning or modification to the upstream ingestion pipeline. Experiments on the LoCoMo benchmark show that PRISM delivers substantially higher LLM-judge accuracy than every same-protocol baseline at an order-of-magnitude smaller context budget, occupying a previously empty corner of the accuracy-context-cost frontier and demonstrating a superior balance between answer quality and retrieval efficiency.

---


### 336. [Delay-Empowered Causal Hierarchical Reinforcement Learning](https://arxiv.org/abs/2605.12261)

**<font color=#1a73e8>作者：</font>** Chenran Zhao, Dianxi Shi, Haotian Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many real-world tasks involve delayed effects, where the outcomes of actions emerge after varying time lags. Existing delay-aware reinforcement learning methods often rely on state augmentation, prior knowledge of delay distributions, or access to non-delayed data, limiting their generalization. Hierarchical reinforcement learning, by contrast, inherently offers advantages in handling delays due to its hierarchical structure, yet existing methods are restricted to fixed delays. To address these limitations, we propose Delay-Empowered Causal Hierarchical Reinforcement Learning (DECHRL). DECHRL explicitly models both the causal structure of state transitions and their associated stochastic delay distributions. These are then incorporated into a delay-aware empowerment objective that drives proactive exploration toward highly controllable states, thereby improving performance under temporal uncertainty. We evaluate DECHRL in modified 2D-Minecraft and MiniGrid environments featuring stochastic delays. Experimental results show that DECHRL effectively models temporal delays and significantly outperforms baselines in decision-making under temporal uncertainty.

---


### 337. [Missingness-MDPs: Bridging the Theory of Missing Data and POMDPs](https://arxiv.org/abs/2605.12262)

**<font color=#1a73e8>作者：</font>** Joshua Wendland, Markel Zubia, Roman Andriushchenko 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce missingness-MDPs (miss-MDPs), a novel subclass of partially observable Markov decision processes (POMDPs) that incorporates the theory of missing data. A miss-MDP is a POMDP whose observation function is a missingness function, specifying the probability that individual state features are missing (i.e., unobserved) at a time step. The literature distinguishes three canonical missingness types: missing (1) completely at random (MCAR), (2) at random (MAR), and (3) not at random (MNAR). Our planning problem is to compute near-optimal policies for a miss-MDP with an unknown missingness function, given a dataset of action-observation trajectories. Achieving such optimality guarantees for policies requires learning the missingness function from data, which is infeasible for general POMDPs. To overcome this challenge, we exploit the structural properties of different missingness types to derive probably approximately correct (PAC) algorithms for learning the missingness function. These algorithms yield an approximate but fully specified miss-MDP that we solve using off-the-shelf planning methods. We prove that, with high probability, the resulting policies are epsilon-optimal in the true miss-MDP. Empirical results confirm the theory and demonstrate superior performance of our approach over two model-free POMDP methods.

---


### 338. [CAD-feature enhanced machine learning for manufacturing effort estimation on sheet metal bending parts](https://arxiv.org/abs/2605.12266)

**<font color=#1a73e8>作者：</font>** Matteo Ballegeer, Toon Van Camp, Willem Jaspers 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Graph-based machine learning has emerged as a promising approach for manufacturability analysis by learning directly from CAD models represented as Boundary Representations (B-reps), exploiting both surface geometry and topological connectivity. However, purely geometric representations often lack the process-specific semantics required for accurate manufacturability prediction: many manufacturing factors, such as surface roles or bend intent, are not explicitly encoded in shape alone and are difficult for data-driven models to infer reliably. We propose a hybrid approach that addresses this challenge by enriching B-rep attributed adjacency graphs with manufacturing features recognized through a rule-based module. Applied to sheet metal bending, recognized features, such as bend characteristics, flange lengths, and surface roles are integrated as node attributes, concentrating the learning signal on process-relevant geometric patterns. Experiments on both a large-scale synthetic manufacturability benchmark and a real-world industrial dataset with measured bending times, one of the first such validations on genuine production data, demonstrate that combining domain knowledge with graph-based learning improves prediction accuracy across both tasks. The results demonstrate that hybrid modeling offers a feasible and effective path toward deployable tools for manufacturability assessment and effort estimation in industrial CAD environments.

---


### 339. [NARA: Anchor-Conditioned Relation-Aware Contextualization of Heterogeneous Geoentities](https://arxiv.org/abs/2605.12276)

**<font color=#1a73e8>作者：</font>** Jina Kim, Gengchen Mai, Lingyi Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Geospatial foundation models have primarily focused on raster data such as satellite imagery, where self-supervised learning has been widely studied. Vector geospatial data instead represent the world as discrete geoentities with explicit geometry, semantics, and structured spatial relations, including metric proximity and topological relationships. These relations jointly determine how entities interact within space, yet existing representation learning methods remain fragmented, often restricted to specific geometry types or partial spatial relations, limiting their ability to capture unified spatial context across heterogeneous geoentities. We propose NARA (Neural Anchor-conditioned Relation-Aware representation learning), a self-supervised framework for vector geoentities. NARA learns context-dependent representations by jointly modeling semantics, geometry, and spatial relations within a unified framework and captures relational spatial structure beyond proximity alone, enabling rich contextualized representations across heterogeneous geoentities of points, polylines, and polygons. Evaluation on building function classification, traffic speed prediction, and next point-of-interest recommendation shows consistent improvements over prior methods, highlighting the benefit of unified relational modeling for vector geospatial data.

---


### 340. [Hypernetworks for Dynamic Feature Selection](https://arxiv.org/abs/2605.12278)

**<font color=#1a73e8>作者：</font>** Javier Fumanal-Idocin, Raquel Fernandez-Peralta, Javier Andreu-Perez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic feature selection (DFS) is a machine learning framework in which features are acquired sequentially for individual samples under budget constraints. The exponential growth in the number of possible feature acquisition paths forces a DFS model to balance fitting specific scenarios against maintaining general performance, even when the feature space is moderate in size. In this paper, we study the structural limitations of existing DFS approaches to achieve an optimal solution. Then, we propose \textsc{Hyper-DFS}, a hypernetwork-based DFS approach that generates feature subset-specific classifier parameters on demand. We show that the use of hypernetworks compared to mask-embedding methods results in a smaller structural complexity bound. We also use a Set Transformer encoding to create a smooth conditioning space for the hypernetwork, so that functionally similar tasks are also geometrically close. In our benchmarks, \textsc{Hyper-DFS} outperforms all state-of-the-art approaches on synthetic and real-life tabular data. It is also competitive or superior across all image datasets tested, and shows substantially stronger zero-shot generalisation to feature subsets never seen during training than existing DFS approaches.

---


### 341. [What makes a word hard to learn? Modeling L1 influence on English vocabulary difficulty](https://arxiv.org/abs/2605.12281)

**<font color=#1a73e8>作者：</font>** Jonas Mayer Martins, Zhuojing Huang, Aaricia Herygers 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> What makes a word difficult to learn, and how does the difficulty depend on the learner's native language? We computationally model vocabulary difficulty for English learners whose first language is Spanish, German, or Chinese with gradient-boosted models trained on features related to a word's familiarity (e.g., frequency), meaning, surface form, and cross-linguistic transfer. Using Shapley values, we determine the importance of each feature group. Word familiarity is the dominant feature group shared by all three languages. However, predictions for Spanish- and German-speaking learners rely additionally on orthographic transfer. This transfer mechanism is unavailable to Chinese learners, whose difficulty is shaped by a combination of familiarity and surface features alone. Our models provide interpretable, L1-tailored difficulty estimates that can be used to design vocabulary curricula.

---


### 342. [TokenRatio: Principled Token-Level Preference Optimization via Ratio Matching](https://arxiv.org/abs/2605.12288)

**<font color=#1a73e8>作者：</font>** Truong Nguyen, Tien-Phat Nguyen, Linh Ngo Van 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Direct Preference Optimization (DPO) is a widely used RL-free method for aligning language models from pairwise preferences, but it models preferences over full sequences even though generation is driven by per-token decisions. Existing token-level extensions typically decompose a sequence-level Bradley-Terry objective across timesteps, leaving per-prefix (state-wise) optimality implicit. We study how to recover token-level preference optimality using only standard sequence-level pairwise comparisons. We introduce Token-level Bregman Preference Optimization (TBPO), which posits a token-level Bradley-Terry preference model over next-token actions conditioned on the prefix, and derive a Bregman-divergence density-ratio matching objective that generalizes the logistic/DPO loss while preserving the optimal policy induced by the token-level model and maintaining DPO-like simplicity. We introduce two instantiations: TBPO-Q, which explicitly learns a lightweight state baseline, and TBPO-A, which removes the baseline through advantage normalization. Across instruction following, helpfulness/harmlessness, and summarization benchmarks, TBPO improves alignment quality and training stability and increases output diversity relative to strong sequence-level and token-level baselines.

---


### 343. [STRABLE: Benchmarking Tabular Machine Learning with Strings](https://arxiv.org/abs/2605.12292)

**<font color=#1a73e8>作者：</font>** Gioia Blayer, Myung Jun Kim, Félix Lefebvre 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Benchmarking tabular learning has revealed the benefit of dedicated architectures, pushing the state of the art. But real-world tables often contain string entries, beyond numbers, and these settings have been understudied due to a lack of a solid benchmarking suite. They lead to new research questions: Are dedicated learners needed, with end-to-end modeling of strings and numbers? Or does it suffice to encode strings as numbers, as with a categorical encoding? And if so, do the resulting tables resemble numerical tabular data, calling for the same learners? To enable these studies, we contribute STRABLE, a benchmarking corpus of 108 tables, all real-world learning problems with strings and numbers across diverse application fields. We run the first large-scale empirical study of tabular learning with strings, evaluating 445 pipelines. These pipelines span end-to-end architectures and modular pipelines, where strings are first encoded, then post-processed, and finally passed to a tabular learner. We find that, because most tables in the wild are categorical-dominant, advanced tabular learners paired with simple string embeddings achieve good predictions at low computational cost. On free-text-dominant tables, large LLM encoders become competitive. Their performance also appears sensitive to post-processing, with differences across LLM families. Finally, we show that STRABLE is a good set of tables to study "string tabular" learning as it leads to generalizable pipeline rankings that are close to the oracle rankings. We thus establish STRABLE as a foundation for research on tabular learning with strings, an important yet understudied area.

---


### 344. [EgoEV-HandPose: Egocentric 3D Hand Pose Estimation and Gesture Recognition with Stereo Event Cameras](https://arxiv.org/abs/2605.12297)

**<font color=#1a73e8>作者：</font>** Luming Wang, Hao Shi, Jiajun Zhai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric 3D hand pose estimation and gesture recognition are essential for immersive augmented/virtual reality, human-computer interaction, and robotics. However, conventional frame-based cameras suffer from motion blur and limited dynamic range, while existing event-based methods are hindered by ego-motion interference, monocular depth ambiguity, and the lack of large-scale real-world stereo datasets. To overcome these limitations, we propose EgoEV-HandPose, an end-to-end framework for joint 3D bimanual pose estimation and gesture recognition from stereo event streams. Central to our approach is KeypointBEV, a flexible stereo fusion module that lifts features into a canonical bird's-eye-view space and employs an iterative reprojection-guided refinement loop to progressively resolve depth uncertainty and enforce kinematic consistency. In addition, we introduce EgoEVHands, the first large-scale real-world stereo event-camera dataset for egocentric hand perception, containing 5,419 annotated sequences with dense 3D/2D keypoints across 38 gesture classes under varying illumination. Extensive experiments demonstrate that EgoEV-HandPose achieves state-of-the-art performance with an MPJPE of 30.54mm and 86.87% Top-1 gesture recognition accuracy, significantly outperforming RGB-based stereo and prior event-camera methods, particularly in low-light and bimanual occlusion scenarios, thereby setting a new benchmark for event-based egocentric perception. The established dataset and source code will be publicly released at this https URL.

---


### 345. [GKnow: Measuring the Entanglement of Gender Bias and Factual Gender](https://arxiv.org/abs/2605.12299)

**<font color=#1a73e8>作者：</font>** Leonor Veloso, Hinrich Schütze  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent works have analyzed the impact of individual components of neural networks on gendered predictions, often with a focus on mitigating gender bias. However, mechanistic interpretations of gender tend to (i) focus on a very specific gender-related task, such as gendered pronoun prediction, or (ii) fail to distinguish between the production of factually gendered outputs (the correct assumption of gender given a word that carries gender as a semantic property) and gender biased outputs (based on a stereotype). To address these issues, we curate \gknow, a benchmark to assess gender knowledge and gender bias in language models across different types of gender-related predictions. \gknow allows us to identify and analyze circuits and individual neurons responsible for gendered predictions. We test the impact of neuron ablation on benchmarks for disentangling stereotypical and factual gender (DiFair and the test set of GKnow), as well as StereoSet. Results show that gender bias and factual gender are severely entangled on the level of both circuits and neurons, entailing that ablation is an unreliable debiasing method. Furthermore, we show that benchmarks for evaluating gender bias can hide the decrease in factual gender knowledge that accompanies neuron ablation. We curate GKnow as a contribution to the continuous development of robust gender bias benchmarks.

---


### 346. [Approximation of Maximally Monotone Operators : A Graph Convergence Perspective](https://arxiv.org/abs/2605.12301)

**<font color=#1a73e8>作者：</font>** Takashi Furuya, Yury Korolev, Takaharu Yaguchi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Operator learning has been highly successful for continuous mappings between infinite-dimensional spaces, such as PDE solution operators. However, many operators of interest-including differential operators-are discontinuous or set-valued, and lie outside classical approximation frameworks. We propose a paradigm shift by formulating approximation via graph convergence (Painlevé-Kuratowski convergence), which is well-suited for closed operators. We show that uniform and $L^p$ approximation are fundamentally inadequate in this setting. Focusing on maximally monotone operators, we prove that any such operator can be approximated in the sense of local graph convergence by continuous encoder-decoder architectures, and further construct structure-preserving approximations that retain maximal monotonicity via resolvent-based parameterizations.

---


### 347. [From Model Uncertainty to Human Attention: Localization-Aware Visual Cues for Scalable Annotation Review](https://arxiv.org/abs/2605.12303)

**<font color=#1a73e8>作者：</font>** Moussa Kassem Sbeyti, Joshua Holstein, Philipp Spitzer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> High-quality labeled data is essential for training robust machine learning models, yet obtaining annotations at scale remains expensive. AI-assisted annotation has therefore become standard in large-scale labeling workflows. However, in tasks where model predictions carry two independent components, a class label and spatial boundaries, a model may classify an object with high confidence while mislocalizing it. Existing AI-assisted workflows offer annotators no signal about where spatial errors are most likely. Without such guidance, humans may systematically underinspect subtly misplaced boxes. We address this by studying the effect of visualizing spatial uncertainty via a purpose-built interface. In a controlled study with 120 participants, those receiving uncertainty cues achieve higher label quality while being faster overall. A box-level analysis confirms that the cues redirect annotator effort toward high-uncertainty predictions and away from well-localized boxes. These findings establish localization uncertainty as a lever to improve human-in-the-loop annotation. Code is available at this https URL.

---


### 348. [KAN-CL: Per-Knot Importance Regularization for Continual Learning with Kolmogorov-Arnold Networks](https://arxiv.org/abs/2605.12306)

**<font color=#1a73e8>作者：</font>** Minjong Cheon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Catastrophic forgetting remains the central obstacle in continual learning (CL): parameters shared across tasks interfere with one another, and existing regularization methods such as EWC and SI apply uniform penalties without awareness of which input region a parameter serves. We propose KAN-CL, a continual learning framework that exploits the compact-support spline parameterization of Kolmogorov-Arnold Networks (KANs) to perform importance-weighted anchoring at per-knot granularity. Deployed as a classification head on a convolutional backbone with standard EWC regularization on the backbone (bbEWC) KAN-CL achieves forgetting reductions of 88% and 93% over a head-only KAN baseline on Split-CIFAR-10/5T and Split-CIFAR-100/10T respectively, while matching or exceeding the accuracy of all baselines on both benchmarks. We further provide a Neural Tangent Kernel (NTK) analysis showing that KAN's spline locality induces a structural rank deficit in the cross-task NTK, yielding a forgetting bound that holds even in the feature-learning regime. These results establish that combining an architecture with natural parameter locality (KAN head) with a complementary backbone regularizer (bbEWC) yields a compositional and principled approach to catastrophic forgetting.

---


### 349. [Transferable Delay-Aware Reinforcement Learning via Implicit Causal Graph Modeling](https://arxiv.org/abs/2605.12312)

**<font color=#1a73e8>作者：</font>** Chenran Zhao, Dianxi Shi, Yaowen Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Random delays weaken the temporal correspondence between actions and subsequent state feedback, making it difficult for agents to identify the true propagation process of action effects. In cross-task scenarios, changes in task objectives and reward formulations further reduce the reusability of previously acquired task knowledge. To address this problem, this paper proposes a transferable delay-aware reinforcement learning method based on implicit causal graph modeling. The proposed method uses a field-node encoder to represent high-dimensional observations as latent states with node-level semantics, and employs a message-passing mechanism to characterize dynamic causal dependencies among nodes, thereby learning transferable structured representations and environment dynamics knowledge. On this basis, imagination-driven behavior learning and planning are incorporated to optimize policies in the latent space, enabling cross-task knowledge transfer and rapid adaptation. Experimental results show that the proposed method outperforms baseline methods on DMC continuous control tasks with random delays. Cross-task transfer experiments further demonstrate that the learned structured representations and dynamics knowledge can be effectively transferred to new tasks and significantly accelerate policy adaptation.

---


### 350. [Autoregressive Learning in Joint KL: Sharp Oracle Bounds and Lower Bounds](https://arxiv.org/abs/2605.12316)

**<font color=#1a73e8>作者：</font>** Yunbei Xu, Yuzhe Yuan, Ruohan Zhan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the fundamental and timely problem of learning long sequences in autoregressive modeling and next-token prediction under model misspecification, measured by the joint Kullback--Leibler (KL) divergence. Our goal is to characterize how the sequence horizon \(H\) affects both approximation and estimation errors in this joint-distribution, sequence-level regime. By establishing matching upper and lower bounds, we provide, to our knowledge, the first complete characterization of long-horizon error behavior under the natural joint KL objective, with improved rates and optimality justification relative to existing work. On the approximation side, we show that joint KL admits a horizon-free approximation factor, in sharp contrast to Hellinger-based analyses that exhibit an \(\Omega(H)\) dependence for computationally efficient methods; this isolates the choice of divergence as the source of approximation amplification. On the estimation side, we prove a fundamental information-theoretic lower bound of order \(\Omega(H)\) that holds for both decomposable policy classes and fully shared policies, matching the \(\widetilde O(H)\) upper bounds achieved by computationally efficient algorithms. Our analysis clarifies the landscape of recent autoregressive learning results by aligning the log-loss training objective, the sequence-level evaluation metric, and the approximation metric {\color{black}through a sharp joint-KL oracle theory}. We further show that these joint-KL guarantees imply policy learning regret bounds at rates matching prior imitation learning literature.

---


> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-396](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
