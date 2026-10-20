# 📦 其他研究 | 2026年10月21日

> 本类共 **534** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-534](./part-11.md)

---

### 301. [Steered Not Stirred: Effective Reward Tilting using Surrogate Reward Mixing](https://arxiv.org/abs/2610.25502)

**<font color=#1a73e8>作者：</font>** Alec Sargood, Olivia Gallup, Georg Maierhofer 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous-time generative models, from diffusion models, flow matching, and now flow maps, owe their practical value to high-fidelity generation and steerability. In many applications, a ground-truth latent ``oracle'' reward $R^*$ is unavailable or expensive to evaluate, e.g., human judgments or experimental measurements. Although the oracle reward is not directly observable, it can often be approximated through multiple cheaper surrogates that, individually, provide incomplete characterizations but collectively reveal substantial information about the downstream task. In this paper, we present a method for composing such surrogates to steer a pretrained model toward the distribution tilted by an unavailable $R^*$. Given a small feedback set of oracle rankings or numerical rewards, we introduce Mixing And Reward Tilting for INference-time Improvement (MARTINI), which learns a surrogate composition for plug-and-play use with standard inference-time steering methods. Our theory characterizes surrogate information limits and relates population recovery error to ideal-target KL at small tilt strength. For preferences, the bound additionally accounts for an irreducible mismatch between the Plackett-Luce population target and the conditional mean. Experiments demonstrate improved oracle-tilt fidelity in language generation and ImageNet alignment, and improved joint pose accuracy and validity in protein-ligand cofolding, without inference-time oracle queries.

---


### 302. [How Far Can an Agent Push? Trust-Safety Margins in Live Language-Based Economic Games](https://arxiv.org/abs/2610.25508)

**<font color=#1a73e8>作者：</font>** Dima Galat, Marian-Andrei Rizoiu  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The previous version contained Unicode em dashes. Paste this ASCII-only version:
Game theory identifies when a strategic action should be accepted, but not how long a live, language-based counterpart will continue to accept it. We entered the GLEE competition in its final week with one protected agent, Milton, and four instrument agents that ran deterministic, per-game randomized trials of policy changes; Milton received changes only through pre-specified gates or registered, rollback-guarded production rules. In negotiation, learned pricing improves adjusted percentile by 0.071 (n=21,168); in bargaining, a continuation model conditioned on the rejected offer did not improve on a recency-weighted incumbent and was retired. In persuasion, a preregistered five-dose experiment (7,391 assigned games, blinded until a fixed stop) shows that recommending every unit raises sales by 0.194 of the maximum (95% CI [0.147, 0.241]) where the receiver's slack makes obedience rational (52% of the Bayesian benchmark), lowers them where it does not (-0.067), and produces a larger early-to-late purchase decline than honest recommendations (-0.123). A rule fixed before unblinding now routes Milton's dose per cell. Milton stood 11th of 460 agents in bargaining at the fixed stop; we also report the close, where the final day's pool shift moved all five agents' bargaining ratings together while their play was unchanged, and three dispatch defects were found by checking delivered behavior against the design.

---


### 303. [KPI-Aware Multimodal Anomaly Detection for 5G and Open RAN Telemetry](https://arxiv.org/abs/2610.25510)

**<font color=#1a73e8>作者：</font>** Chiman Salavati, Liang Wu, Kelly Wan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable anomaly detection is a deployment bottleneck for 5G/Open RAN observability and emerging self-optimizing 6G systems, where hundreds of heterogeneous KPIs, severe class imbalance, and strict alert budgets make purely numerical scores brittle. We present KAC, a deployment-oriented KPI-aware multimodal anomaly-detection framework that uses KPI-level residual-text alignment to turn compact operator-style summaries into a learnable feedback signal over full-KPI temporal evidence. This gives the detector broad numerical coverage like modern time-series models, while retaining the sparse KPI-specific reasoning that makes operator feedback sustainable in a future operator-facing workflow. Across public telecom telemetry, enterprise-scale Open RAN observability data, and a Nokia benchmark built from real 5G RAN production packet traces with realism-hardened injected anomalies, KAC achieves strong threshold-based detection performance while remaining competitive on threshold-free ranking metrics. On TelecomTS, at a fixed 2.5 percent false-positive-rate operating point, KAC achieves the highest recall among the evaluated residual-based methods while maintaining comparable precision; across the evaluated benchmarks, it remains robust under substantial class imbalance. KAC is integrated in pre-production shadow mode with Nokia's GKE-based KPI construction pipeline, where it continuously scores telemetry windows alongside an internal packet-level anomaly detector for operational evaluation.

---


### 304. [Dynamics-Aligned Representation Learning under Induced Partial Observability](https://arxiv.org/abs/2610.25511)

**<font color=#1a73e8>作者：</font>** SM Mazharul Islam, Manfred Huber  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model-based reinforcement learning (MBRL) has enabled sample-efficient learning of continuous control policies from high-dimensional observations through learned latent dynamics models. These models are typically trained with observation reconstruction objectives, which provide strong supervision but can bias representations toward visual fidelity leading to an undertrained prior and unreliable long-horizon predictions. We propose a stochastic gating mechanism that induces controlled partial observability during training by sampling a spatial binary mask from a Beta--Bernoulli random field and applying it to the raw observation. The gate probability is resampled at each time step, exposing the encoder to conditions ranging from near-total occlusion to near-full visibility. Integration of our method requires minimal architectural changes from existing dynamics models: the gated observation and the binary mask are channel-wise concatenated and passed to the encoder as a single augmented input, with no modifications to the broader training pipeline. We evaluate the proposed approach on a set of pixel-based continuous control tasks selected from the DeepMind Control Suite. Using model predictive control for evaluation, which relies solely on open-loop model rollouts, we show that stochastic gating improves planning performance and data efficiency across tasks. Further analysis demonstrates that performance is robust to the spatial scale of the mask, and a balanced observability during training outperforms configurations biased toward either sparser or denser observations.

---


### 305. [When Interpretations Persist: Downstream Influence in Gaze-Aware Assistants](https://arxiv.org/abs/2610.25512)

**<font color=#1a73e8>作者：</font>** Mingcong Ding, Chenyan Zhang, Zhuojiang Cai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI assistants may carry forward not only observations but also interpretations of what a person is doing or may do next across time. Once retained, these interpretations become context for later predictions and system-triggered outputs. We study whether this representation step changes later behavior in gaze-aware streaming assistance. Holding retrieved events, their order, and the target input fixed, we find that Free-form Interpretation amplifies historical influence in both directions: correct histories produce more helpful changes and wrong histories more harmful changes. Unsupported and broader interpretations about activity or future behavior are associated with greater harmful influence. Evidence-Bounded Interpretation preserves distinctions between observation, inference, uncertainty, and temporal scope, reducing unsupported and overcertain content and lowering wrong-source harmful influence while retaining most helpful influence. The same effect structure appears with a second model. These findings identify persistent interpretation as a consequential design choice for history-aware human-AI systems.

---


### 306. [ReDT: Resolution-Decoupled Visual Geometry Transformer](https://arxiv.org/abs/2610.25517)

**<font color=#1a73e8>作者：</font>** Abteen Arab, Guile Wu, Dongfeng Bai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce ReDT, a feed-forward visual geometry transformer designed to scale multi-view reconstruction to high-definition (HD) inputs. Existing visual geometry transformers are typically trained at fixed, standard definition (SD) resolutions and exhibit degraded reconstruction quality and poor computational scaling to high input resolutions. While recent efficient architectures reduce the complexity of inter-frame attention, expensive intra-frame and encoder attention remain largely unaddressed, making HD reconstruction impractical with existing architectures. ReDT addresses both limitations with a resolution-aware architecture designed to scale to high-resolution inputs. The key idea of ReDT is to first map each view to a fixed-size set of basis tokens, compute correspondences in this compact constant-size basis space, and then project the outputs back to the original resolution for dense prediction. By decoupling the internal representation from input resolution during attention, ReDT substantially reduces the computational cost of high-resolution 3D reconstruction and improves model performance at all resolutions. Extensive experiments on multiple datasets spanning SD to FHD (2K) show that ReDT outperforms state-of-the-art visual geometry transformers in both reconstruction quality and computational efficiency. For instance, on the ETH3D (2K) dataset, ReDT achieves a $16\times$ speedup, a $34\%$ reduction in peak GPU memory usage, and a $33\%$ reduction in chamfer distance over VGGT-$\Omega$. \href{this https URL}{Project Website.}

---


### 307. [FracTS: Hierarchical and Autoregressive Time Series Generation](https://arxiv.org/abs/2610.25523)

**<font color=#1a73e8>作者：</font>** Jiayu Li, Umair Afzal, Zilong Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series are ubiquitous across different domains, and the growing use of synthetic data for privacy-preserving sharing, data augmentation, and stress testing makes time series generation increasingly important. Early generative approaches are predominantly autoregressive, which can suffer from low sample diversity, error accumulation, and difficulty modeling long-range dependencies. In this paper, we introduce FracTS, a hierarchical, coarse-to-fine autoregressive model for multivariate time series generation. Inspired by fractal generative modeling developed for images, FracTS adapts the paradigm from 2D to 1D sequences by learning a multi-scale representation that captures global trajectory structure at coarse scales and local dynamics at fine scales while following the autoregressive nature of time series. In contrast to unstructured images, time series are structured, allowing easy automated or designated temporal feature processing optimized for the model, and global (static) feature extraction describing the instances that generate the corresponding time series in the collection. We incorporate them in the generation process to further improve the generation quality. The design naturally handles multivariate dependencies and improves long-horizon temporal coherence without requiring fixed-length inputs. Experiments on five datasets (two conditional, three unconditional) conducted against seven baselines show that FracTS consistently outperforms baselines across marginal distribution and predictive ML utility, and correlation preservation in the unconditional setting. In particular, the predictive ML utility is averagely improved by 100.0% and 75.0-81.0% for unconditional and conditional time series datasets compared to the best baseline (relative error computed on dataset-averaged raw values). Code is available at: this https URL.

---


### 308. [From Clinical Risk Prediction to Operational Decisions: An Uncertainty-Aware Framework for ICU Staffing](https://arxiv.org/abs/2610.25530)

**<font color=#1a73e8>作者：</font>** Jiayan Yang, Ad Feelders, Arno Siebes  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Advances in electronic health records (EHR) and large-scale critical care databases have enabled the development of machine learning models for the early detection of patient deterioration. While these models often achieve strong predictive performance for outcomes such as sepsis and mortality, most studies evaluate them purely on discrimination metrics. This leaves a critical gap: how to systematically translate probabilistic clinical risk estimates into downstream operational decisions under real-world constraints, such as shift rigidity and hiring delays.
This study proposes an uncertainty-aware anticipatory staffing framework that bridges short-term patient risk prediction and staff planning without altering the upstream predictive model. Instead of relying on naive deterministic aggregation or fixed safety buffers, the framework explicitly models dynamic predictive uncertainty and evaluates extreme shortage exposure using Conditional Value-at-Risk (CVaR). These aggregated, risk-calibrated demand signals are then embedded into an hourly rolling-horizon scheduling policy to generate delay-constrained staffing decisions.
Evaluated on realistic trajectories from the MIMIC-IV database, the proposed framework demonstrates a favorable cost-shortage trade-off compared to deterministic and purely reactive baselines. Pareto frontier analysis illustrates how uncertainty-aware demand construction changes resource allocation under varying safety preferences, while stress testing confirms the framework's operational robustness even when subjected to systematic predictive bias in the form of calibration drift. By formalizing this translation layer, this work provides a principled, transparent pathway for safely integrating probabilistic AI outputs into high-stakes healthcare operational systems.

---


### 309. [Modaliff: A Unified Token Diffusion Model for Any-to-Any Generation](https://arxiv.org/abs/2610.25533)

**<font color=#1a73e8>作者：</font>** Duc Kieu, Kien Do, Minh Khoa Le 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Any-to-any generation seeks a single model that translates flexibly among text, image, and audio, yet existing approaches either require fully aligned multimodal tuples or a shared representation that suppresses modality-specific structure. We introduce Modaliff, a novel token-based diffusion model that learns from widely available bimodal pairs while preserving each modality in its native latent sequence. Modaliff assembles conditions and targets into a unified token sequence, with per-token attributes to disambiguate token identities and role-based positional embedding to preserve each modality's internal structure across sequence layouts. This design enables a single denoiser to support diverse generation tasks without task-specific architectural changes or a shared cross-modal latent space. Beyond one-to-one generation, Modaliff supports multiple conditions either by combining single-condition predictions at inference or by lightweight finetuning on captions that jointly describe multiple inputs. Experiments across text, image, and audio show that Modaliff achieves the best fidelity among any-to-any models on most generation tasks while using substantially fewer parameters and training data.

---


### 310. [Residential Construction Image Dataset Using CSI Divisions for Deep Learning-based Object Detection](https://arxiv.org/abs/2610.25535)

**<font color=#1a73e8>作者：</font>** Fahad Iqbal, Shayan Mirzabeigi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate recognition of construction site elements is essential for the application of deep learning (DL) in the construction industry. Despite rapid advances in computer vision, the adoption of DL in construction has been limited by the lack of structured, publicly available datasets aligned with established industry standards. To address this gap, we introduce the Residential Construction Dataset Using CSI Divisions (ResCD-CSI) image dataset, a manually labeled image benchmark organized according to the divisional structure defined by the Construction Specifications Institute (CSI). The dataset comprises high-resolution images collected from active residential construction sites across the United States, capturing diverse building components, materials, and equipment under real-world conditions. In total, 16,365 objects spanning 14 major CSI divisions were precisely annotated using bounding boxes, ensuring consistency and reliability for object detection tasks. By aligning with the CSI divisional framework, ResCD-CSI establishes a standardized resource that bridges construction practice with computer vision research and supports the development of Artificial Intelligence-driven solutions for residential construction monitoring.

---


### 311. [Reinforcement learning on the EPRI AI-ccelerating Unit Commitment benchmark: diagnosing over-commitment and guiding MILP with learned policies](https://arxiv.org/abs/2610.25544)

**<font color=#1a73e8>作者：</font>** Maharani Devira Pramita, Aidan O'Sullivan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) is increasingly proposed as a fast solver for unit commitment (UC), but standalone agents remain far more expensive than mixed-integer linear programming (MILP). In the first study of RL on the 51-generator, 72-hour benchmark of the Electric Power Research Institute (EPRI) AI-ccelerating Unit Commitment competition, we trace this gap to the agents' own exploration, close most of it, and show that the resulting policy can accelerate an exact solver. In every configuration tested, Proximal Policy Optimisation (PPO) and an action-branching Deep Q-Network (DQN) trained from scratch committed about twice the units of a thermal-only MILP optimum, at 39-64% higher cost, whereas a merit-order rule came within 1.6-7% (10-24% when unserved energy is priced). When each unit's decision is sampled independently, spare units insure against random de-commitments. Consistent with this, injecting exploration noise during fine-tuning enlarged a lean policy's fleet, a reward without shaping terms did not remove the over-commitment, and under their training noise the agents outperformed the rule subjected to comparable noise. Imitating the MILP solutions and fine-tuning conservatively brought PPO within 2.6% of the optimum, and these policies had the lowest penalised cost of any evaluated (about 5%). Fixing the fine-tuned policy's confident decisions made the MILP 3.8-8.5 times faster within 0.10-0.25% of the best solution, with a smaller worst case than an imitation-only policy fixing as many variables (1.1% against 8.9%). Because dispatch method and benchmark scope alone shift the reported optimality ratio by up to 3.6% and 9%, we propose a reporting protocol.

---


### 312. [Beyond the record: evaluating probabilistic AI weather forecasts deep in the tail](https://arxiv.org/abs/2610.25545)

**<font color=#1a73e8>作者：</font>** Bastiaan Van Velthoven, Cas Decancq, Diego G. Miralles 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can probabilistic artificial intelligence (AI) weather forecasts retain skill beyond their training domain? We compare four state-of-the-art AI models (ArchesWeatherGen, U-Cast, WeatherNext2 and GenCast-mini) with the physics-based IFS-ENS over land in 2022, at 1.5° resolution and lead times of 2--10 days. Monthly ERA5 records from 1979--2021 define common historical boundaries, and we characterize new records set in 2022 by their depth, i.e., the exceedance margin relative to local historical variability. Two proper scores, record-threshold weighted CRPS and Brier score, assess the magnitude and probability of record exceedances across all eligible cases, retaining both missed extremes and false alarms. Verified against ERA5, AI models outperform IFS-ENS for heat and cold records at almost every lead and depth. For heat, the advantage strengthens with depth, partly because IFS-ENS over-forecasts deep records, and largely persists for deeper records under HRES-fc0 verification. For wind, gains erode for deeper records and longer leads. Better tail scores can nevertheless coexist with aggregate probability deficits or surpluses, and some improvements arise chiefly on non-exceedances. Increasing underprediction on progressively more extreme observed subsets can also arise through outcome selection, even for an ideal conditional-mean forecast. These findings establish that native probabilistic AI ensembles retain, and for heat increase, their advantage over IFS-ENS as thresholds move beyond local records, although all advantages narrow with lead time. They caution against generalizing the extrapolation failure reported for deterministic AI forecasts to probabilistic systems, and motivate common verification conventions that separate comparative tail skill, performance on realized extremes, and probabilistic calibration.

---


### 313. [EmotiQ: A Quantum Residual Specialist Framework for Text Emotion Classification](https://arxiv.org/abs/2610.25549)

**<font color=#1a73e8>作者：</font>** Carlton Kigonya, Tanaka Chirara, Yunting Yin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emotion classification from text is challenging because many affective states are distinguished by subtle linguistic signals and semantically overlapping boundaries. We investigate whether compact quantum modules can serve as targeted residual specialists that assist traditional classifiers on difficult emotion decisions. We introduce EmotiQ, a residual specialist framework for text emotion classification using a frozen transformer classifier as the primary decision maker, identifies challenging emotion boundaries from validation behavior, and trains boundary specialists, including quantum encodings, data re-uploading specialists, prototype and fidelity specialists, and kernel-based specialists. Specialists are permitted to intervene only when they satisfy validation-based admission criteria. We evaluate the framework across six text emotion classification datasets and establish traditional model baselines. Experimental results show that the admitted EmotiQ policy improves mean macro-F1 metrics over the baseline, and achieves positive gains on five of six datasets. Among the quantum components, ZZ interaction feature maps are the most consistently effective, yielding a mean macro-F1 improvement of +0.0030 and positive gains on four datasets. These findings suggest that current quantum NLP methods can be deployed as residual specialists that provide localized improvements under strong classical supervision.

---


### 314. [Tricking Synthetic Image Detectors with Amortized Generative Attacks](https://arxiv.org/abs/2610.25554)

**<font color=#1a73e8>作者：</font>** Mohamed Awad, Khaled Elhady, Yasser Rohaim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rapid advances in image synthesis have increased the need for reliable synthetic-image detectors, yet their robustness to transferable attacks remains incomplete and understudied. Existing evaluations generally examine whether an attack constructed against one detector transfers to another, but rarely isolate how its effectiveness changes when the attacked images originate from different generators. We conduct a systematic evaluation of three representative attacks: two iterative perturbation-based methods, MIG and MuMoDIG, and the amortized generative attack Tricker. Across four detectors and five generators spanning diverse architectures, we introduce a two-axis evaluation protocol that independently varies the surrogate detector used to construct or train the attack and the generator supplying its input images. We assess attack effectiveness, cross-detector transferability, perceptual quality, runtime, and interaction with common post-processing operations. We revisit Tricker and show that its data and training requirements can be substantially reduced, enabling broader and more efficient evaluation. Our results demonstrate that transferability is not a detector-only property: the input-generator distribution strongly influences both evasion effectiveness and attacked-image quality. MIG and MuMoDIG exhibit pronounced dependence on the detector--generator pair, whereas Tricker provides more uniform white-box evasion and image quality. We additionally observe that post-processing maintains the asymmetric transferability topology. These findings expose a neglected dimension of attack evaluation and motivate transfer-aware protocols that jointly account for detector and generator variation. We will release our code, evaluation data, and trained attack models with a responsible-use statement.

---


### 315. [Flattening Fantasies: Analyzing Stereotypes in Pornographic Discourse](https://arxiv.org/abs/2610.25566)

**<font color=#1a73e8>作者：</font>** Sarmad Chandio, Osama Khalid, Sharaf Zia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study presents a large-scale quantitative analysis of 5.4 million video
titles from xHamster, the world's fourth most visited pornography platform, to
examine linguistic patterns used to describe different dimensions of
identities (e.g., race and gender). Specifically, we investigate how
nationalities, ethnic groups, and gender identities are portrayed in
pornographic discourse, focusing on stereotypes and deviations from implicit
norms of pornography. The results show the dominance of American pornography
over other groups, which acts as the de facto norm for the adult industry. We
identify persistent ethnic stereotypes reflecting colonial power dynamics,
religious fetishization, and the sexualization of cultural taboos. The
analysis reveals gendered representational differences across cultures, with a
prevalent Madonna-Whore dichotomy in the portrayal of women and stereotypical
depictions of men in physically dominant roles.

---


### 316. [CVTA: Cross-Variable Temporal Attention for Multivariate Irregular Time Series Prediction](https://arxiv.org/abs/2610.25584)

**<font color=#1a73e8>作者：</font>** Ankitkumar Joshi, Milos Hauskrecht  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Irregularly sampled multivariate time series arise in many real-world domains such as healthcare, climate science, and large-scale monitoring systems. Characterized by asynchronous observations and heterogeneity across variables, such time series pose significant challenges for forecasting. In this work, we introduce Cross-Variable Temporal Attention (CVTA), a short-term, continuous-time forecasting framework that learns prediction functions from its compact, interpretable state summarizing recent temporal dynamics across variables. CVTA uses Variable-Conditioned Embeddings to project heterogeneous variables into variable-specific latent spaces, and applies temporal attention to capture cross-variable dependencies from this state. Furthermore, we demonstrate that CVTA can be integrated as an auxiliary module into existing state-of-the-art prediction models through a dynamic meta-decision model. Extensive experiments on multiple real-world benchmarks show that CVTA achieves strong short-term predictive accuracy, supports efficient online inference, improves existing prediction models when used as an auxiliary module, and learns attention patterns that align well with domain knowledge.

---


### 317. [Distributionally-Robust Policy Learning with Observational Data](https://arxiv.org/abs/2610.25591)

**<font color=#1a73e8>作者：</font>** Debmalya Mandal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Policy learning from observational data is fundamental to applications ranging from personalized medicine to welfare-program targeting, but standard approaches optimize empirical performance and may fail when the deployment distribution differs from the training distribution. We study \emph{distributionally-robust policy learning}: given observational data, we seek a policy $\pi \in \Pi$ that maximizes the worst-case policy value over an $f$-divergence ball of radius $\rho$ around the data-generating distribution. We propose an estimator built on cross-fitted doubly-robust scores for the conditional treatment effect, paired with a DRO solver that handles \texttt{KL}, $\chi^2$, and \texttt{CVaR} ambiguity sets. We establish two convergence guarantees. First, the estimated policy attains the standard $\widetilde{O}(n^{-1/2})$ rate on its DRO regret, and inherits the doubly-robust property -- the rate continues to hold whenever either the outcome model or the propensity model is consistently estimated, even at slow nonparametric rates. We then propose a sample-splitting bias-correction algorithm derived from the Lagrangian dual, and show that under a Tsybakov-style margin condition on the treatment-effect, the estimator attains a fast rate of $\widetilde{O}(n^{-(1+\alpha)/(2+\alpha)})$ , interpolating between $\widetilde{O}(1/\sqrt{n})$ and $\widetilde{O}(1/n)$ as the margin parameter $\alpha$ ranges over $[0,\infty)$. To our knowledge, this is the first work to incorporate a margin condition into the analysis of distributionally-robust policy learning, and the first to obtain fast rates in this setting. Empirically, on synthetic and semi-synthetic experiments calibrated to a welfare-to-work program, distributional robustness yields meaningful improvements over empirical welfare maximization when training and test distributions differ.

---


### 318. [PRISM: Prior Relational Information for Self-supervised Modeling to Enhance Solubility OOD Generalization](https://arxiv.org/abs/2610.25605)

**<font color=#1a73e8>作者：</font>** Xinyi Chen, Jiahuan Pang, Titus Chima 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Solubility depends on intermolecular interactions between solutes and solvents, and is central to drug discovery, chemical and materials process engineering. Its prediction requires out-of-distribution (OOD) generalization to unseen solutes, solvents, and solvent mixtures, where supervised methods suffer from data scarcity, and existing self-supervised methods do not explicitly learn chemically meaningful relations. Learning chemically meaningful relational information without labels can alleviate data scarcity and improve OOD generalization, but remains challenging. We introduce Prior Relational Information for Self-supervised Modeling (PRISM) and apply it to solubility OOD generalization. PRISM is a label-free pretraining framework that converts expert-defined chemical priors into relational teachers. For solubility prediction, it trains four encoders to preserve the population-level relational information from priors capturing hydrophobic, electrostatic, polarizability, and substructural effects, using Kullback-Leibler (KL) divergence to match distance-based neighborhood distributions during pretraining. Across scaffold, solute, and solvent OOD settings, PRISM matches or surpasses supervised and self-supervised baselines. Under mixed-solvent OOD, freezing the four PRISM encoders and training a lightweight fusion-and-composition head outperforms strong baselines and substantially reduces run-to-run variation. Ablations and control studies confirm that gains stem from chemically meaningful relational structures baked into the encoders by PRISM. We expect this strategy of turning relational priors into self-supervision signals to extend beyond solubility prediction to domains where chemically or biologically meaningful relational priors are available.

---


### 319. [CheXFuse: Guided Differential Joint Attention Fusion for Robust Multimodal Chest X-Ray Classification in Data-Scarce Medical Settings](https://arxiv.org/abs/2610.25617)

**<font color=#1a73e8>作者：</font>** Muntaqim Ahmed Raju, Priyanka Siddappa, Md Shifat Haider Al Amin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A central challenge in multimodal learning is how to fuse modalities that differ substantially in predictive strength. When one modality provides a much stronger representation than another, indiscriminate cross-modal interaction can introduce weak, redundant, or unstable signals, limiting or even degrading performance relative to the strongest unimodal representation. To address this problem, we propose CheXFuse, a multimodal fusion framework based on Guided Differential Joint Attention (GuDJA). CheXFuse combines image and text token representations within a joint multimodal sequence, where learned token guidance emphasizes informative representations and differential attention reduces less useful attention responses. We evaluate CheXFuse on the Indiana University (IU) Chest X-ray dataset, using binary (normal vs. abnormal) classification as the downstream task. Experiments are conducted under both original-report and masked-report settings, with the latter serving as a controlled stress test under reduced textual informativeness. CheXFuse with GuDJA achieves the strongest mean overall performance across the evaluated baselines and ablations, reaching 95.73% accuracy, 95.79% F1-score, 96.54% recall, and 95.28% sensitivity at 95% specificity (Sens@95Spec) with original reports, and 95.58%, 95.60%, 95.60%, and 94.34%, respectively, under masked reports. These results suggest that GuDJA provides a promising fusion strategy under asymmetric or partially reduced modality informativeness.

---


### 320. [Weighted State Souping for Efficient Long-Context Retrieval](https://arxiv.org/abs/2610.25621)

**<font color=#1a73e8>作者：</font>** William L. Tong, Aryo Lotfi, Emmanuel Abbe 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State space models (SSMs) combine fast inference and fixed state size with competitive language-modeling performance. Recently, state souping has been proposed as a procedure whereby an SSM independently encodes chunks of tokens like documents, tool definitions, or memory records. The resulting state encodings may be cached and recombined to cheaply construct a context for downstream queries. However, both state souping and vanilla SSMs deteriorate on long, crowded contexts, limiting their utility for long-horizon domains. To address this issue, we propose weighted state souping, a simple method that learns query-dependent weights for composing cached states. The resulting models improve long-context performance substantially across both single- and multi-hop document question answering, needle-in-a-haystack retrieval, variable tracking, and tool use. Our method can be further adapted into an efficient sparse variant, yielding near-constant encoding cost with respect to context length while preserving (and sometimes improving) performance. We also present simple theoretical arguments that illustrate why souping works and when it may fail, and discuss informally the advantages of weighted souping. Weighted state souping thus combines reusable context representations with selective retrieval, offering an efficient approach to language modeling over large collections of documents, tools, and other forms of structured context that increasingly dominate modern agentic workloads.

---


### 321. [Recurrent Vision Transformers for Event-Based Spacecraft Pose Estimation Under Slow Relative Motions](https://arxiv.org/abs/2610.25622)

**<font color=#1a73e8>作者：</font>** Sofia McLeod, Mohsi Jawaid, Carl Seubert 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-based object pose estimation is vital for conducting spacecraft rendezvous and proximity operations (RPO). Recent research has demonstrated the robustness of event cameras against the harsh lighting conditions that often occur in orbit, thanks to the extremely high dynamic range of event sensors. However, event-based spacecraft pose estimation (EBSPE) suffers when the relative motion between the chaser and target is slow, since the event rate drops significantly, leading to data with low signal-to-noise ratio. Unfortunately, for safety reasons, real RPO trajectories often involve slow relative motions (e.g., down to 1 mm/s), and operating under low illumination exacerbates the problem. Addressing slow relative motions is thus crucial to raise the practicality of EBSPE. To this end, we propose using recurrent vision transformers (RVT) for EBSPE. The key idea is to exploit recurrent memory to capture longer-term information across sparse event streams, and to learn the temporal attention span from full trajectories rather than fixing the time window. We developed an RVT-based heatmap regressor to produce 2D-3D correspondences for pose estimation, which was validated on real event data collected under slow relative motions representative of RPO trajectories. Results indicate the superior pose estimation accuracy and stability of our RVT-based method, relative to previous per-event-frame-based or fixed-time-window EBSPE methods.

---


### 322. [Conditional Average Treatment Effect Distillation for Hypothetical State-Intervention Targeting Under Budget Constraints](https://arxiv.org/abs/2610.25627)

**<font color=#1a73e8>作者：</font>** Vasundhara Acharya, Bülent Yener  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personalized public-health targeting must capture heterogeneous intervention benefits while remaining interpretable under resource constraints. Flexible causal-effect models can be hard to operationalize, while coarse subgroup policies may lose individualized effect information. We study budget-constrained hypothetical state interventions in observational data without a logged historical decision policy. For obesity, elevated glucose, and lifetime smoking-history states, causal-structure-informed pretreatment covariates are prespecified, with capacity capped at 70% of those observed in the adverse state. We evaluate causal distillation where Causal Forest and Bayesian Causal Forest teachers estimate conditional average treatment effects (CATEs), which decision tree and random forest students approximate. We compare individualized policies with unsupervised K-means subgroup policies and supervised causal-tree policies with leaf counts matched to K-means cluster counts. Observational policies are assessed on held-out data using a doubly robust estimator, bootstrap uncertainty, and decision-focused teacher-student fidelity measures. Across PIMA obesity and glucose and NHANES smoking-history experiments, each distilled student was within 0.011 absolute utility of its teacher, with allocation Jaccard similarities of 0.738-0.937. K-means and causal-tree policies were also competitive, with the highest point-estimate policy varying by application. Prespecified paired comparisons were nonsignificant after Holm adjustment, while near-budget-boundary agreement was less stable than global fidelity for some teacher-student pairs. Findings support causal distillation for translating flexible effect models into simpler budgeted targeting rules, although observational estimates depend on causal-identification assumptions and require longitudinal or prospective validation.

---


### 323. [The Forward/Inverse Duality of Controlled Emergence:A Computational Design Program from Explanation to Engineering](https://arxiv.org/abs/2610.25630)

**<font color=#1a73e8>作者：</font>** Hao Li, Minghui Ren, Shaowen Lu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The macroscopic capabilities of intelligent systems arise from the local interactions of many simple units. When such systems are deployed in the real world, their behaviour must nevertheless be constrained, leaving designers caught between releasing adaptability and preventing loss of control, yet without formal tools to resolve the dilemma. This paper proposes a unified research program for controlled emergence that restates this tension as a pair of dual problems: the forward problem explains macroscopic behaviour from local rules, and the inverse problem solves for controllable rules and readout mechanisms from a desired target. We take an augmented quintuple as the formal object shared by both ends, and decompose ``engineering'' into three independently measurable coordinates: controllability, reproducibility, and degree of formalizability. On this basis we give three testable working hypotheses (critical scale; the cooperation and trade-off between constraint and adaptability; minimal constraint) and one feasibility criterion, which reduce inverse design from unconstrained optimization to interval checking. The program takes explicit failure boundaries as its premise, does not pursue complete control, and always preserves the system's room for self-organization. The reduced pilot experiment attached to this paper serves only to verify the executability of the research protocol and does not constitute a statistical test of the working hypotheses. This design language generalizes to multi-agent artificial intelligence, the industrial internet, and emergency response systems, all of which must confront emergence and controllability at once.

---


### 324. [Where Do the Gaussians Go? Foreground Attraction for Camera-Based Weakly Supervised 3D Occupancy](https://arxiv.org/abs/2610.25631)

**<font color=#1a73e8>作者：</font>** Jeagon Song, Jhonghyun An  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-based 3D semantic occupancy models can be trained without 3D labels by rendering their predictions into the images and supervising them with 2D pseudo labels. In sparse Gaussian representations trained this way, Gaussian positions are learned only through pixel-wise rendering losses, which we hypothesize give small foreground objects little weight. In trained GaussianFlowOcc models, the Gaussian density on foreground voxels is on average only 1.62 times that on background voxels. We propose a training-only foreground attraction loss that back-projects foreground pseudo-label pixels with pseudo depth and pulls nearby Gaussians toward these 3D points, favoring Gaussians that already predict the target class; the inference network is unchanged. On Occ3D-nuScenes, the loss raises this concentration to 2.40 over three seeds. Over three seeds, the mean foreground IoU increases from 6.29 to 6.96 and is higher for each seed, whereas the change in mean mIoU (13.53 to 13.82) is within the seed-to-seed variation of the baseline. Single-run ablations further indicate that pseudo-label targets outperform targets placed at ground-truth voxels and that acting on the Gaussian positions alone is not sufficient, and a single-seed test shows that the model degrades less when fewer Gaussians are kept at inference.

---


### 325. [Confidence-Guided Pseudo-Label Refinement for Unsupervised Cross-Domain Person Re-Identification](https://arxiv.org/abs/2610.25633)

**<font color=#1a73e8>作者：</font>** Sundas Iqbal, Danish Ali, Qing Tian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised cross-domain person re-identification remains challenging because domain shifts generate noisy pseudo labels that are reinforced during iterative adaptation. Existing clustering-based methods often rely on limited reliability cues or global confidence criteria and may impose hard identity supervision on ambiguous target samples. To address these limitations, we propose CGPLR, a confidence-guided pseudo-label refinement framework for unsupervised domain-adaptive person re-identification. CGPLR estimates sample-level reliability by jointly modeling centroid compatibility, local neighborhood consistency, separation from the strongest competing cluster and temporal assignment stability. The resulting confidence distribution is used to derive cluster-adaptive upper and lower thresholds for a three-way selective decision. Reliable assignments are preserved, recoverable samples are reassigned only when an alternative cluster receives sufficient geometric and neighborhood support and highly ambiguous samples are deferred from hard identity supervision. The learning objective adapts to these decisions through confidence-weighted supervision for preserved samples, cautious corrected-label weighting for reassigned samples and label-free representation consistency for deferred samples. CGPLR achieves 76.4% Rank-1 accuracy and 47.6% mean average precision (mAP) on Market-1501 to MSMT17, and 95.1% Rank-1 accuracy and 87.7% mAP on MSMT17 to Market-1501, demonstrating effective reliability-aware selective adaptation. The code is available at this https URL.

---


### 326. [Clean Forcing: Drift-Resistant Autoregressive Video Diffusion with a Frozen Base](https://arxiv.org/abs/2610.25634)

**<font color=#1a73e8>作者：</font>** Wenqing Wang, Joonghyuk Shin, Jonathan Tremblay 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) video diffusion models generate streaming video of arbitrary length by conditioning each new chunk of frames on those already generated. However, they suffer from exposure bias, where a model trained on clean context must continue from its own imperfect outputs, and errors compound until quality collapses within seconds (drift). Existing methods either require cluster-scale base retraining, apply training-free inference corrections with inconsistent results, or train frozen-base correctors for sampling and cache errors. We instead find that drift is largely deterministic and therefore learnable, as holding the noisy state fixed while varying only the history reveals a counterfactual velocity gap that is ~95% systematic across noise seeds. Based on this observation, we introduce Clean Forcing, which trains a 5.9M-parameter LoRA corrector on the frozen base model to regress this gap, with a closed-loop stage that adds DAgger-style aggregation and a drift-contraction objective to expose the corrector to its own rollouts. Because the clean histories can be the base model's own single-shot generations, training needs no real videos, and the merged corrector adds no inference cost. In 50 s text-to-video generation, Clean Forcing reduces {\Delta}-drift from +11.3 to +1.65 without real video and to -0.16 with 40 real clips, improving on the best published result of +3.57 with over 150x less data. Extensive experiments demonstrate that Clean Forcing outperforms prior methods in aesthetic quality and data efficiency with reduced drift for long-horizon video generation.

---


### 327. [Formalization of Rényi Differential Privacy in Isabelle/HOL (Draft version)](https://arxiv.org/abs/2610.25636)

**<font color=#1a73e8>作者：</font>** Tetsuya Sato  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Differential privacy (DP) is a gold-standard definition of privacy designed to evaluate the privacy guarantee of databases. Rényi differential privacy (RDP) is an important variant of DP that gives tight evaluations of machine learning algorithms. These formulations are easy to understand, but evaluating privacy for actual databases is complicated. Even a small change in the database can break its privacy, and evaluations of DP and RDP themselves are complicated. In particular, RDP evaluations in recent studies have become much harder. Therefore, formal verification of them has been studied for over a decade.
In this paper, we propose an Isabelle/HOL library for formalizing Rényi differential privacy in a general setting. We first formalize RDP for continuous distributions. As a technical basis, we formalize several properties of convex functions and $f$-divergences for nonnegative convex functions. We formalize basic properties of RDP, conversion laws from RDP to DP, the moment accountants in DP, and the Gaussian mechanism and its RDP. Finally, we discuss the stochastic gradient descent mechanism with Gaussian noise and formalize a rough evaluation of its RDP and DP.

---


### 328. [TNVD-SC: Diagnosing Scan Context Failures in Forests with Terrain-Normalized Vertical Distributions](https://arxiv.org/abs/2610.25637)

**<font color=#1a73e8>作者：</font>** Jineon Kim, Jhonghyun An  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-term LiDAR place recognition in forests is difficult because repetitive vegetation and uneven terrain create severe structural aliasing. We diagnose Scan Context (SC) by separating candidate retrieval from fine matching: on the standardized TreeLoc++ Wild-Places protocol, a TNVD support key places a valid location in the top-25 set for approximately 99% of queries, while conventional SC matching on those candidates reaches only 61.84% mean R@1. With an identical raw-SC candidate set, terrain normalization improves max-height cells by only 1.21 points but vertical-distribution cells by 19.72 points. These observations motivate Terrain-Normalized Vertical Distribution Scan Context (TNVD-SC), which preserves the SC ring-sector topology while encoding terrain-relative vertical probability distributions. Under the standardized TreeLoc++ protocol, TNVD-SC reaches 91.83% mean R@1 and attains the highest R@1 mean and R@1 stability among the compared methods, while TreeLoc++ remains stronger in mean MR, MF1, and AUC. The unchanged method reaches 85.14% mean R@1 on the four-session CVTNet-style NCLT evaluation. A lossless count-coded implementation with exact hierarchical Jensen-Shannon search reduces descriptor payload by 3.86x and compute latency by 23.8% without changing the audited retrieval outputs.

---


### 329. [ACorD: Adaptive Correspondence Discovery for Medical Image Registration](https://arxiv.org/abs/2610.25638)

**<font color=#1a73e8>作者：</font>** Arghavan Rezvani, Kun Han, Xiaohui Xie  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image registration is a fundamental task for aligning anatomical structures across images. Exhaustively searching for point-wise correspondences is prohibitively expensive in both computation and memory, particularly for high-resolution 3D medical images. Most recent learning-based methods directly predict correspondences in a coarse-to-fine manner, but often propagate intermediate estimates across scales without explicitly weighting correspondence evidence, which can allow coarse-scale errors to persist during refinement. To address these challenges, we propose ACorD, an adaptive correspondence discovery framework designed to mitigate error propagation with an attention-guided process. ACorD first predicts multiple potential correspondence candidates through Correlation-guided Cross-scale Offset Prediction (CCOP), which combines correlation maps as spatial matching priors with cross-scale features as global deformation context. Then, Multi-Head Deformable Aggregation (MHDA) aggregates these candidate correspondences using attention, producing a learned, non-uniform weighting over competing matches rather than treating them equally. The multi-head design further captures complementary deformation patterns, ensuring both global alignment and local precision. By integrating adaptive offset prediction with selective, attention-based aggregation of correspondence evidence, ACorD enables accurate deformation refinement. Extensive experiments on four public medical registration benchmarks demonstrate that adaptive correspondence discovery within a multi-scale refinement framework improves registration robustness across diverse anatomical structures.

---


### 330. [Visual Memory and Textual Alignment for Cross-Modal Few-Shot Segmentation](https://arxiv.org/abs/2610.25641)

**<font color=#1a73e8>作者：</font>** Tianqi Wei, Zhi Chen, Xin Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot segmentation (FSS) aims to segment target objects with limited annotated examples. Recent studies have begun to explore large foundation models to improve generalization for this task. In particular, SAM 3 provides strong visual representations and supports text-guided segmentation. However, its performance remains limited in specialized domains, where semantic prompts and visual representations are often poorly aligned. To address this challenge, we propose ViTA-SAM, a framework built upon SAM 3 that integrates visual memory and textual features through cross-modal alignment. Specifically, we construct a visual memory module that encodes support features together with their corresponding masks, providing support-aware visual guidance for query prediction. In parallel, we leverage the text encoder of SAM 3 to extract semantic features as complementary priors. To bridge the gap between semantic and visual representations, we introduce a cross-modal alignment module that conditions textual features on memory-enhanced visual representations, yielding more consistent and visually grounded predictions. In addition, we propose a pseudo-label refinement strategy that updates the memory with predicted query masks, enabling query-adaptive representation learning. Extensive experiments on multiple benchmarks show that ViTA-SAM achieves the best overall performance among the compared methods, outperforming the strongest competing method by over 5% in average mIoU.

---


### 331. [Negation without Confusion: Decomposing Bias and Recomposing Style in Text Embeddings for Negation-aware Image Generation](https://arxiv.org/abs/2610.25645)

**<font color=#1a73e8>作者：</font>** Sooyeon Park, Hemraj Singh, Kyunghyun Min 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Negation-aware image generation remains challenging for text-to-image diffusion models, which often struggle with negation due to implicit linguistic biases that are deeply entangled within text representations. As a result, bias-aligned semantics frequently dominate over intended negative constraints. To overcome this limitation, we propose a simple training-free method of Decompose and Recompose text embedding (Dero), which constructs a semantic-preserving subspace and a bias subspace using auxiliary prompts and performs semantic disentanglement based on bidirectional SVD. By decomposing entangled representations and selectively recomposing disentangled semantic components, Dero realigns text representations toward intended negation semantics while restoring residual stylistic features to preserve semantic fidelity and image quality. As a model-agnostic inference-time framework operating solely on text representations, Dero can be seamlessly applied to diverse diffusion architectures, including both U-Net and DiT based models. Extensive experiments on both object- and concept-level negation demonstrate consistent improvements in negation-aware image generation, achieving stronger text-image alignment, better semantic fidelity, and higher human preference scores.

---


### 332. [Spherical Fixed-Point Reasoners: Adaptive Loop Halting on the Hypersphere](https://arxiv.org/abs/2610.25646)

**<font color=#1a73e8>作者：</font>** Arber Zela, Artavazd Maranjyan, Pol Puigdemont 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Looped (weight-tied) transformers enable adaptive computation by allocating more iterations to harder inputs. Fixed-Point Reasoners (FPRM) achieve this with a damped fixed-point solver, but operate in an unbounded Euclidean residual space with coupled rescaling and relative-norm halting. We introduce Spherical Fixed-Point Reasoners (SFPRM), which perform the same computation on the unit hypersphere of normalized transformers (nGPT). Input injection, damping, and halting become geodesic operations, yielding boundedness by construction and eliminating coefficient coupling. We prove fixed-point existence, local convergence under an explicit step-size condition, and global convergence under strong injection. On Sudoku-Extreme, Maze-Hard, and Mini-ARC, SFPRM achieves 96.6%, 87.9%, and 59.1% test accuracy, respectively, outperforming FPRM and other baselines while allocating test-time compute more effectively. Its converged geometry is also interpretable: token-input angles capture puzzle structure and predict correctness.

---


### 333. [A "feature ODE" describing the learning behavior of shallow MLPs on simple functions](https://arxiv.org/abs/2610.25652)

**<font color=#1a73e8>作者：</font>** Joseph Turnbull, Berkan Ottlik, Jamie Simon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the gradient flow training dynamics of two-layer multi-layer perceptrons (MLPs) on anisotropic Gaussian data. Even in this simple setting, solving the dynamics in full is notoriously difficult, so we try something different. We propose a "feature ODE" that might be intuitively expected to describe the learning dynamics of a shallow MLP. We find that MLPs trained to learn simple target functions (low-order Hermite polynomials and staircase functions) actually roughly follow the loss trajectories from this feature ODE. This agreement is a surprise because of the size of the simplification and the fact that it does not come from a rigorous chain of approximations. We discuss this surprise and speculate on its reasons and uses.

---


### 334. [FluidGen: Physics-Aware Fluid Video Generation via Motion-Guided Post-Training](https://arxiv.org/abs/2610.25660)

**<font color=#1a73e8>作者：</font>** Yang Zheng, Zizhang Li, Boyang Deng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation models produce visually compelling motion but systematically fail on fluid phenomena, including smoke, fire, and explosion debris, where outputs lack coherent vortical structure and collapse to bland dynamics that violate the physics of real fluids. Classical solvers achieve high physical fidelity but require detailed 3D scenes and carefully tuned parameters, making them impractical for in-the-wild imagery and video generation. We address this gap by injecting a data-driven fluid prior into a pre-trained video model, trained on a mixture of high-fidelity Houdini simulation data with paired velocity-field ground truth and curated in-the-wild fluid video data for appearance diversity. The core of our approach is a dual stream architecture that predicts per-frame velocity fields alongside RGB, supervised by simulation ground truth. This auxiliary signal regularizes generation toward physically consistent motion and exposes an interpretable physical quantity that we further leverage as a reward for velocity-aware direct preference optimization. Our model produces substantially more realistic fluid dynamics sequences than strong video baselines and optimization-based methods. Project page: this https URL

---


### 335. [Can Metadata Fix the Gauge? Calibration Turns Sparse Multi-Source Learning from Sparse PCA into Sparse Mean Recovery](https://arxiv.org/abs/2610.25663)

**<font color=#1a73e8>作者：</font>** Yirong Xiang, Yibo Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Source labels tell us where a sample came from, but not how that source oriented its coordinates. In a sparse Gaussian multi-source model with source-specific sign gauges, that distinction changes the learning problem. Without calibration, pooling across sources erases the mean signal, and the source-labelled experiment reduces to sparse PCA. With task-independent relative-gauge metadata, synchronization aligns sources and the same observations become a sparse mean problem. We formalize the value of metadata through AlignedMass, which quantifies how much first-order signal a metadata-induced alignment restores. Source labels create only limited AlignedMass, whereas valid calibration can create AlignedMass proportional to the full sample size. This yields a statistical separation in micro-source regimes and, under standard sparse-PCA hardness assumptions, a computational separation as well. Synthetic experiments check the predicted scaling; controlled real-feature
and physical sensor studies examine sign cancellation, separately
acquired calibration, and reuse across tasks.

---


### 336. [PoSTCache: From Forecasting to Postdictive Smoothing for Revisable Diffusion Caching](https://arxiv.org/abs/2610.25664)

**<font color=#1a73e8>作者：</font>** Liwei Lan, Hui Chen, Jungong Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion and flow matching models achieve impressive visual generation quality but remain computationally expensive due to iterative sampling. Caching-based acceleration provides a practical training-free solution by reusing or predicting intermediate features. However, existing methods largely enforce a forward-only information flow: approximations produced for skipped model evaluations are immediately committed to the sampling trajectory and cannot benefit from feedback generated by later full-computation steps. We propose \textbf{PoSTCache} (\emph{Postdictive Smoothing Trajectory Cache}), a training-free and plug-and-play framework that reformulates diffusion caching as revisable trajectory inference. PoSTCache first uses an existing caching strategy to construct forward proposals for skipped steps. At a later full-computation step, the discrepancy between the refreshed prediction and its forward proposal yields a correction signal, which PoSTCache propagates backward to refine and reintegrate the preceding predictions. Viewing full-computation steps as sources of corrective feedback also changes how they should be selected. We therefore introduce the Posterior Variance Reduction (PVR) strategy, which estimates cross-timestep dependencies from offline denoising trajectories and selects anchors according to their expected reduction in surrogate trajectory uncertainty rather than local approximation error alone. Experiments on representative image and video generation models show that PoSTCache consistently improves the quality--efficiency trade-off over representative caching methods.

---


### 337. [Frechet Forcing: Training Long-Horizon Streaming World Models from Short Clips](https://arxiv.org/abs/2610.25666)

**<font color=#1a73e8>作者：</font>** Yian Zhao, Yu Yan, Hongcan Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video world models generate the future chunk by chunk, conditioned on their own past and a stream of actions. Trained on short clips, they drift once a rollout exceeds the training horizon, as prediction errors re-enter the context and compound. A common remedy is to train the model on its own rollouts via distribution matching distillation (DMD). For action-conditioned world models, the teacher becomes a bottleneck: an external video model is agnostic to the actions, whereas the model's own pretrained network drifts in the same manner as the student. We observe that a long rollout need not match a teacher, provided it remains a realistic continuation of its own scene that follows the commanded actions. Realism and scene fidelity can be measured against real-data statistics, which remain valid at any horizon, while action following is preserved by the model's conditional generation loss. We propose Fréchet Forcing, which fine-tunes a world model together with its deployed multi-step sampler under three constraints. Generative anchoring applies the flow-matching loss after a self-generated history ending on real data. Context fidelity, a Fréchet distance (FD) on latent statistics of the free rollout centred on each clip's own ground truth, keeps every rollout faithful to its scene. Reality matching, an FD to real frames in a frozen perceptual space, keeps the generated frames realistic. Because all three targets are derived from short real clips without comparing a rollout against a long recorded future, training requires no teacher, no online critic and no long videos. Fine-tuning MiniWorld-1B, pretrained on 253-frame clips, for at most 36 GPU-hours on 381-frame clips yields rollouts that remain stable beyond 4,000 frames and continue to follow their actions in both robot manipulation and camera-controlled exploration.

---


### 338. [HyperTaxa: Multiscale Genome Representations for Generalized Microbial Taxonomic Inference](https://arxiv.org/abs/2610.25673)

**<font color=#1a73e8>作者：</font>** Akash Rao, Sushim Gupta, Vishalini Ramnath 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable microbial taxonomic inference is challenged by the rapid growth of newly sequenced organisms and incomplete reference coverage. While alignment- and database-driven tools remain essential for reference-backed identification, they are not designed for learned inference over species absent from genome-level training. We introduce HyperTaxa, a taxonomy-aligned representation learning framework for open-set microbial taxonomic inference. HyperTaxa encodes whole genomes as multiscale hyperspectral k-mer transition fields and aligns these representations to a taxonomy-derived semantic space using a two-stage Node2Vec-to-MDS procedure that combines local graph structure with global hierarchical distance preservation. The resulting space supports zero-shot inference over species excluded from genome-level training but represented in the taxonomy, generalized zero-shot inference over seen and unseen species, and cascaded genus-to-species prediction. Across benchmark and large-scale disjoint-species evaluations, HyperTaxa improves taxonomic prediction over pseudo-image and transformer-graph baselines, with the strongest gains at higher taxonomic ranks. Ablations further show that multiscale transition encoding and taxonomy-aware alignment are key contributors to generalization. These results position HyperTaxa as a complementary taxonomy-aware representation and candidate-generation framework for microbial identification under incomplete reference coverage and open-set uncertainty.

---


### 339. [RxGS: Relightable Gaussian Stylization via BRDF Decomposition](https://arxiv.org/abs/2610.25681)

**<font color=#1a73e8>作者：</font>** Wanrong Hong, Liu Jiang, Mukesh Prasad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reference-based 3D scene stylization transfers the appearance of a reference image onto a reconstructed 3D scene while preserving scene geometry. Recent methods perform this transfer by optimizing the appearance representation of neural scene models including Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS). These methods optimize an RGB appearance representation, in which a single per-point colour combines the effects of material reflectance, environment illumination, together with the shading it produces, and the viewing direction. When stylization modifies this combined colour, the illumination effects present during stylization are baked into the stored appearance, so the stylized scene cannot be rendered under different illumination. To address this limitation, we present RxGS, a relightable 3D scene stylization framework built on a Bidirectional Reflectance Distribution Function (BRDF)-aware 3D Gaussian representation. Rather than modifying a per-point RGB colour, RxGS optimizes only the diffuse albedo field recovered by inverse rendering, while leaving roughness, metallicity, surface normals, and the estimated environment lighting unchanged. As a result, the stylized scene keeps all the components a physically-based renderer needs other than the edited albedo, and can therefore still be relit. RxGS optimizes the albedo field using a nearest-neighbour feature matching loss together with a spatial smoothness prior over Gaussian centres. We evaluate the method using a Geometry Consistency Cost (GCC) based on optical-flow warping error. RxGS achieves the lowest GCC on all evaluated NeRF-Synthetic scenes and remains competitive on real-captured scenes, while additionally supporting relightable stylization, which existing reference-based 3D scene stylization methods do not provide.

---


### 340. [BitFlat: Error-Localized Bitstream Design for Robust Diffusion Image Compression](https://arxiv.org/abs/2610.25682)

**<font color=#1a73e8>作者：</font>** Xinfeng Deng, Li Zhou, Haitao Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Zero-shot diffusion image compression based on reverse channel coding achieves high perceptual quality at low bitrates without retraining, yet its bitstream remains vulnerable to bit flips. Prior work has shown that a joint combinatorial representation can amplify a single bit flip into substitutions of multiple atoms and that indexing each atom independently confines this error propagation. However, independent indexing reduces the number of atoms that fit within the bit budget and gives the decoder no indication of which atoms are corrupted. To address these issues, we propose BitFlat, a training-free error-localizing bitstream framework with two components. Blockwise Locality Alignment (BLA) decomposes the globally coupled atom selection at each diffusion step into independent selection units, each describing one signed atom from a dedicated codebook with a fixed-width field, so that any bit error affects only the unit in which it occurs. Reliability-Aware Diffusion Control (RADC) uses the bits saved by BLA to impose structured valid-codeword constraints within each field and converts the decoding state of each field into a binary reliability gate, which turns detected corrupted atoms into erasures at known positions and excludes them from noise synthesis. BitFlat requires neither target residuals nor additional network forward passes and leaves the diffusion model unchanged. Experiments on Kodak, DIV2K, and CLIC2020 show that BitFlat outperforms conventional, learned, and diffusion-based codecs at bit error rates from $10^{-4}$ to $10^{-2}$ and, even with $26.7\%$ fewer bits, surpasses Robust Turbo-DDCM.

---


### 341. [MT-CC: Multi-Group Temperature Scaling for Asymmetric Calibration Behavior in Class-Incremental Learning](https://arxiv.org/abs/2610.25689)

**<font color=#1a73e8>作者：</font>** Sungjun Yun, Yonghee Choi, Dong-Jun Han  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As deep neural networks are required to continuously adapt to evolving data, class-incremental learning (CIL) has become an active research area. However, most existing works primarily focus on improving accuracy while overlooking confidence calibration, which measures the trustworthiness of the model's predictions. Although temperature scaling (TS) is effective for static calibration, it has rarely been explored in continual settings where data distributions evolve over time. In this paper, we introduce Multi-Group Temperature Scaling for Continual Calibration (MT-CC), a novel post-hoc calibration framework that addresses the asymmetric calibration behavior in CIL, where the rate of confidence changes does not align with the rate of accuracy degradation across tasks, leading to different levels of miscalibration. Our key contribution is to design multiple temperature parameters through a lightweight grouping network that separates samples by confidence statistics and task-aware signals in CIL. Furthermore, a Groupwise Difference-between-Confidence-and-Accuracy (GDCA) regularization is incorporated to promote intra-group consistency. Experiments demonstrate that MT-CC significantly improves calibration performance while maintaining accuracy, offering a principled framework for reliable continual learning.

---


### 342. [Progress-Guided Preference Generation for Aligning Generative Control Policies](https://arxiv.org/abs/2610.25692)

**<font color=#1a73e8>作者：</font>** Tung M. Luu, Tri Ton, Duc M. Nguyen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative policies have achieved strong performance in imitation learning tasks, but their success is often constrained by the limited availability of expert demonstrations. Although preference-based fine-tuning can leverage suboptimal rollouts to improve performance, existing approaches heavily rely on expensive human annotations. In this work, we introduce Progress-Guided Preference Generation (PGPG), an unsupervised preference alignment framework that eliminates the need for human-in-the-loop supervision. Our method leverages ordered coverage alignment to measure sequential progress relative to a small set of expert demonstrations, enabling the automatic extraction of pseudo-preference labels from autonomously collected rollouts. Furthermore, we introduce key enhancements to improve the reliability of these progress-guided preferences, enabling effective fine-tuning of pretrained generative policies without requiring manually designed reward functions. Extensive experiments across a suite of challenging long-horizon manipulation tasks demonstrate that PGPG outperforms standard supervised fine-tuning baselines. Moreover, our conceptually simple framework is broadly applicable across multiple classes of generative policies, demonstrating strong versatility when integrated with both diffusion and flow-matching policies.

---


### 343. [Stochastic Tracking of Drifting Affine Fixed Points](https://arxiv.org/abs/2610.25699)

**<font color=#1a73e8>作者：</font>** Sajad Khodadadian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear stochastic approximation (SA) is widely used to estimate fixed points from noisy observations, but most finite-time analyses assume that the underlying operator remains fixed. We study linear SA with time-varying affine operators, where the fixed points change over time and the observation noise may be correlated across rounds. For constant-stepsize updates, we establish a bound on the cumulative expected squared distance between the iterates and the corresponding fixed points. The bound accounts for the initial error, observation noise, and changes in the fixed points over time. We also establish lower bounds for scalar Gaussian models, showing that, under specified conditions, a suitably chosen constant stepsize achieves the smallest possible worst-case cumulative error up to constant factors, even compared with estimators that use future observations. These results further quantify the effect of temporal correlation on estimation accuracy. Since choosing an appropriate stepsize generally requires knowledge of the noise level and how much the fixed points change, we develop an adaptive method that uses an additional bounded, unbiased observation of the fixed point to achieve an almost optimal algorithm without needing the knowledge of the noise level and the fixed point variation over time. Finally, we apply our results to value-function estimation using synchronous tabular temporal-difference learning in changing environments, assuming generative-model access and a common invariant distribution.

---


### 344. [Evidence Sufficiency and Model Comparisons in MexRegQA: An Item-Level Audit of Mexican-Spanish Regulatory QA](https://arxiv.org/abs/2610.25710)

**<font color=#1a73e8>作者：</font>** Fred Hu, Yeqi Wang, Xing Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Similarity-gated coverage does not establish that retrieved evidence contains the facts needed to answer a question. We audit Mexican-Spanish financial-regulatory QA and find that 35 of 135 covered items lack some or all load-bearing facts. On the post-hoc full-evidence slice (n=98), eleven prompt-matched models score 95-98/98 and none differs significantly from the anchor; this does not establish equivalence. Removing evidence-defective items changes the nominal significance status of 14 of 55 pairwise comparisons. On 56 zero-evidence items, accuracy spans 33.9%-89.3%. Removing evidence from the audited items under an abstention-permitting prompt reduces accuracy by 63-81 percentage points in all ten tested legs, with no recovered items. Building on sufficient-context research, we contribute MexRegQA v1.0: 192 items with provenance and evidence-status labels, frozen retrieval evidence for 191 evaluated items, predictions, judge outputs and offline checks. The audit was outcome-aware, the later model/panel sweep reused the same questions, and all reported scores and labels rely on machine evaluation without independent human validation. We propose releasing evidence-status labels alongside grounded QA benchmarks so that model comparisons can be examined separately from evidence availability.

---


### 345. [Peer-Relative Trust-Guided Update Screening for Robust Semi-Decentralized Federated Learning under Label-Flipping Attacks](https://arxiv.org/abs/2610.25714)

**<font color=#1a73e8>作者：</font>** Ajay Kumar Shrestha, Sandhya Joshi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Trust and reputation mechanisms can reduce the influence of malicious clients in federated learning (FL), but strict update filtering is difficult under non-independent and identically distributed (non-IID) data because honest local updates may temporarily reduce performance on a shared validation proxy. Building on our earlier trust-based semi-decentralized FL (SDFL) framework, this paper operationalizes the trust signals and introduces peer-relative update screening that combines a robust validation-utility score with direction- and norm-based update quality. The method is evaluated with 50 MNIST clients, 20% persistent label-flip attackers, Dirichlet heterogeneity levels of 0.5 and 0.1, 100 communication rounds, and five paired random seeds. Under moderate heterogeneity, the proposed method reaches 98.37% final accuracy while rejecting 95.82% of malicious updates and retaining 90.30% of benign updates; the final benign and malicious trust distributions are completely separated (KS=1.00). Under severe heterogeneity, it reaches 95.25% accuracy, rejects 88.55% of malicious updates, and retains 76.90% of benign updates (KS=0.96). Trust weighting alone preserves slightly higher utility in the most heterogeneous condition, but accepts all malicious submis-sions. The results therefore distinguish influence mitigation from explicit containment and quantify the utility-selectivity trade-off introduced by screening. The study provides an empirically validated off-chain governance core that can feed blockchain-based audit and incentive layers in SDFL.

---


### 346. [LEVI: Benchmarking Visual Identity Fidelity with Verifiable Low-Entropy Constructs](https://arxiv.org/abs/2610.25716)

**<font color=#1a73e8>作者：</font>** Xiao Ma, Zhonghao Zhan, Hamed Haddadi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern generative models can produce visually plausible images while violating exact identity constraints. Evaluating such failures requires distinguishing violations of the requested identity from permissible variation in appearance. We introduce Low-Entropy Visual Identity (LEVI), which characterizes visual identities determined by compact facts and explicit rules. The low-entropy requirement concerns identity uncertainty, while appearance may remain diverse. We formulate identity fidelity in terms of the probability that a conditional image distribution assigns to the identities permitted by the prompt. Visual Identity Spaces (VIS) formalize this distinction by specifying admissible identity values and which different realizations express the same identity. Building on this formulation, we develop Verifiable Visual Grammar (VVG), a declarative language whose typed primitives and compositional constraints describe identity-bearing structures. Using this grammar, we build a benchmark for image generation. It assesses each output against the task's identity requirements, drawing evidence from the final pixels. The curated benchmark contains 1,375 tasks spanning 120 base identity spaces across six domains. Among ten evaluated model configurations, the highest whole-task pass rate is 58.69%. These results reveal a persistent gap between visually plausible images and faithful realization of their specified identities. Project page (forthcoming): this https URL.

---


### 347. [Neural Video Coding under Limited Delay: Theoretical Optimality and System Design](https://arxiv.org/abs/2610.25729)

**<font color=#1a73e8>作者：</font>** Likun Cai, Jun Chen, Ashish Khisti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traditional neural video compression (NVC) methods predominantly follow strictly causal predictive-coding paradigm, treating zero-frame delay as a fixed constraint rather than delay as an explicit design parameter. From an information-theoretic perspective, allowing limited frame delay enables a codec to exploit correlations with future frames within the delay window, thereby reducing uncertainty that is inaccessible to strictly causal prediction and potentially improving the rate-distortion tradeoff. In this work, we formalize this intuition through a rigorous rate-distortion analysis builds on the clique factorization of Markov networks, and propose Graph-Factored Sequential Coding (GFSC), a principled framework for sequential video coding under limited delay. To our knowledge, we provide the first theoretical result showing that, for general $K$-order Markov sources with positive distributions, a $K$-frame delay is sufficient to attain joint-coding rate-distortion optimality over a nontrivial distortion region, a guarantee unavailable to zero-delay causal coding in general. In practice, we instantiate GFSC through lightweight neural modules, allowing existing causal predictive codecs to be augmented without modifying their core architectures. Experiments across multiple NVC models and datasets show that GFSC consistently improves rate-distortion performance over the corresponding causal counterparts. Under matched delay budgets, GFSC also achieves competitive performance compared with representative bidirectional codecs.

---


### 348. [Remember Less, Adapt Longer: Bounded-State In-Context Reinforcement Learning with Recurrent Summary Memory](https://arxiv.org/abs/2610.25758)

**<font color=#1a73e8>作者：</font>** Jiawen Wang, Cheng Xue, Peng Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In-context reinforcement learning (ICRL) enables agents to adapt to new tasks without parameter updates, relying on memory to retain what they learn from experience. For agents operating continually, existing approaches using memory trade off bounded cost against access to past experience. Approaches using growing memories, such as full-history attention and accumulating summaries, incur storage and per-decision costs that increase with task length. Fixed-size memories bound storage but restrict access: sliding windows discard older steps, while recurrent networks compress even recent interactions into a hidden state. We introduce Recurrent Summary Memory (RSM), a Transformer policy that attends exactly to a short working buffer of recent interactions and carries a fixed-capacity summary of earlier experience. When the buffer fills, RSM rewrites the summary from its previous contents and the buffer, then clears the buffer, so deployment memory and per-decision cost stay $O(1)$ in task length. On long-running partially observable tasks, frozen RSM policies sustain their adapted performance for eight times the training horizon with about 1% of full-history memory, ending ahead of every evaluated baseline while growing memories deteriorate. When the task configuration changes mid-run, RSM re-adapts better than growing and recurrent memories. Clearing the summary or blocking the policy's access to it removes its benefit, while swapping in another task's summary steers behaviour towards that task. Together, these results show that our fixed-capacity summary can sustain in-context adaptation far beyond the training horizon.

---


### 349. [ActTime: Action-Conditioned World Modeling for Time Series](https://arxiv.org/abs/2610.25764)

**<font color=#1a73e8>作者：</font>** Xinxing Zhou, Xiaojie Yuan, Yanlong Wen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time-series models increasingly condition on known future inputs. In controlled systems, some of these inputs are actions that can be changed, compared, and optimized before execution. A model must therefore do more than predict the realized future: it must predict how outcomes change under different actions from the same observed history and support reliable comparison of candidate plans. We introduce ActTime, an action-conditioned world model for time series. Over the observed history, ActTime updates variable-specific latent states through an action-conditioned transition and corrects them using observations. It then rolls the same transition forward under candidate actions to generate future trajectories. Training uses only factual trajectories, without paired alternative-action outcomes or planning supervision. We construct a simulator-grounded evaluation suite across building energy, traffic, greenhouse climate, and inventory management, covering factual prediction, intervention-effect prediction, offline decision making, and closed-loop planning. ActTime ranks first in 12 of 16 domain-task settings. Across eight methods, the mean pairwise model-ranking reversal rate is 17.8% between factual prediction and intervention fidelity, and rises to 28.4% between intervention fidelity and decision ranking. These results show that factual accuracy, intervention fidelity, and decision quality are related but not interchangeable.

---


### 350. [TRACE: Tracking Multimodal Clinical Trajectories for Inpatient Risk Prediction](https://arxiv.org/abs/2610.25765)

**<font color=#1a73e8>作者：</font>** Minjun Kim, Jong Hak Moon  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate inpatient risk prediction requires modeling heterogeneous clinical evidence that accumulates irregularly over time. This challenge spans in-hospital mortality, prolonged length of stay, and readmission, each with task-specific observation windows. Existing multimodal approaches combine structured health record data, chest x-rays, and clinical text, but primarily focus on modality fusion or missing-modality compensation, with limited attention to temporal trajectories over an admission. We propose TRACE (TRAjectory modeling of multimodal Clinical Events), a daily-scale framework organizing clinical events into day-level trajectories, separating day-invariant global context from day-specific local events drawn from EHR data, chest x-rays, radiology reports, and discharge summaries. The trajectory is encoded using temporal attention, allowing unavailable modalities to emit no tokens. A phenotype-guided contrastive objective further organizes admissions under heterogeneous disease distributions. Across cohorts from MIMIC-IV, eICU, and MIMIC-III comprising nearly 180,000 total stays, we evaluate TRACE on mortality, length of stay, and readmission prediction. TRACE achieves the highest AUROC across all nine dataset-task settings and the highest ACC in eight, outperforming baselines. Ablation studies validate our attention masks and contrastive learning, while trajectory-level attribution localizes risk-associated hospital days and modalities.

---


> [!TIP]
> 当前位于：**301-350**（第 7/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-534](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
