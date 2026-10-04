# 📦 其他研究 | 2026年10月05日

> 本类共 **385** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-385](./part-08.md)

---

### 51. [Fault-Tolerant Budget Conservation in Distributed Multi-Agent Delegation](https://arxiv.org/abs/2610.00349)

**<font color=#1a73e8>作者：</font>** Genliang Zhu, Chu Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Resource limits are becoming an authorization boundary for AI agents that delegate work across concurrent and failure-prone workers. Parent-child allocation constraints, affine objects, and distributed escrow do not by themselves prevent overspend when replies are lost, effects complete after timeout, messages repeat, branches partition, or DAG joins alias one lineage. We formalize fault-tolerant budget conservation for distributed multi-agent delegation. Budgets are quantized resource vectors represented by exclusive escrow credits that move through a delegation DAG. Before dispatch, a branch converts credit into an operation reservation bound to lineage, epoch, normalized effect, maximum charge, receiver, and idempotency key. It persists a signed dispatch permit with quarantine; the gateway verifies that permit before first acceptance. Uncertain effects remain charged until authenticated settlement, a fenced authoritative no-effect proof, or permanent retirement. We prove ownership partition, ledger and effect conservation, descendant non-amplification, at-most-once settlement, late-completion safety, and partition confinement under explicit mediation, durability, authentication, normalization, and gateway assumptions. An indistinguishability result shows that partition-local availability requires exclusive preallocation. Bounded TLA+ checking, an independent JavaScript explorer, and crash-injected two-process SQLite experiments exercise the declared scope and detect timeout-refund and historical-certificate-validation mutants. The mechanism preserves the issued budget bound across the evaluated crash, retry, duplicate, partition, join, and late-completion schedules.

---


### 52. [Vmem-$φ$: Low-Compute Out-of-Distribution Detection in Spiking Neural Networks from Membrane-Potential Statistics](https://arxiv.org/abs/2610.00350)

**<font color=#1a73e8>作者：</font>** Arul Rana, Agrim Tripathi, Shoaib Ahmed Dipu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spiking Neural Networks (SNNs) offer an energy-efficient approach to processing event-camera data, yet out-of-distribution (OOD) detection remains challenging in this setting. Existing OOD detection methods often depend on model outputs or computational components that are unavailable in object detection SNNs or are poorly suited to low-compute deployment. To that effect, we show that the subthreshold membrane potential \(V_{\mathrm{mem}}(t)\) provides a useful internal signal for detecting distribution shifts. Simple per-channel statistics derived from these membrane dynamics enable OOD detection. To evaluate this approach, we introduce Gen1-C, an event-camera corruption benchmark developed upon the Prophesee Gen1 automotive detection dataset, containing six sensor-motivated histogram-level stress tests at five severity levels. We further propose the Multi-Descriptor Deviation (MDD), a corruption-blind method that operates on membrane-potential statistics. At the highest corruption severity, MDD achieves an AUROC of more than 0.88 on five of the six corruptions using only a bounded 64-frame observation window. Notably, the remaining corruption is also the one that has the smallest effect on the underlying detector. These results show that the temporal membrane-potential dynamics can provide an effective and low-cost signal for OOD detection in SNN-based event perception.

---


### 53. [JusticeAxis: Benchmarking Legal Judgment between Rigid Rule Application and Ungrounded Discretion](https://arxiv.org/abs/2610.00353)

**<font color=#1a73e8>作者：</font>** Zhengkai Tu, Mingda Zhang, Zijia Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A sound judgment applies the law to established facts and weighs the circumstances in which they arose. However, existing methods swing between rigid statute matching and ungrounded discretion, benchmarks score a label or a rubric, and the experience that would supply the balance stays unverified. We formalize legal judgment as a reference-anchored task, whose object is a single decision that stays tied to the statute and to the circumstances at once. We introduce JusticeAxis, 256 real-world criminal cases from 18 countries with audio, image, and text evidence, and three lawyer-written judgments for every case: the recorded one and one for each failure. We further propose JusticeAgent, a harness whose element agents establish the facts and whose judge agent applies the law under skills carrying experience of the circumstances. Skills are distilled from execution trajectories and admitted only under Bayesian credible bounds. Experiments show that failure turns direction with scale: open-weight backbones drift to unsupported grounds, frontier models to the statutory default. We further verify that JusticeAgent, as a simple yet effective plugin, carries a frozen open-weight backbone to commercial level. Project resources are available at this https URL.

---


### 54. [Deep Learning for Anomaly Detection in Railway Systems: A Structured Survey](https://arxiv.org/abs/2610.00363)

**<font color=#1a73e8>作者：</font>** Ammar Bouketta, Smail Niar, Hamza Ouarnoughi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ensuring safe and reliable operation of modern railway systems increasingly relies on data-driven monitoring and intelligent fault detection. Deep learning has emerged as an effective paradigm for railway anomaly detection, driven by the growing availability of heterogeneous sensor data from rolling stock and infrastructure. This paper presents a structured survey of deep learning-based anomaly detection approaches for railway systems. The surveyed methods are organized using a unified taxonomy covering anomaly location, data representation and manifestation, sensing modality, and temporal characteristics. Existing approaches, including convolutional, recurrent and attention-based architectures, autoencoders, generative adversarial networks, and transformers, are structured into classification-based, prediction-based, reconstruction-based, and hybrid learning paradigms. The survey also examines data-centric challenges, evaluation practices, performance metrics, and practical deployment aspects, including edge-cloud architectures, computational constraints, and hardware-aware optimization. Finally, a decision-oriented framework links anomaly characteristics, data properties, and operational constraints to suitable detection paradigms and deployment configurations. This work provides a structured reference for selecting and deploying deep learning solutions for railway anomaly detection and highlights open challenges toward reliable and scalable intelligent monitoring systems.

---


### 55. [Manifold-Constrained Initial Noise Optimization for Efficient Generative Model Alignment](https://arxiv.org/abs/2610.00365)

**<font color=#1a73e8>作者：</font>** Jinho Chang, Jong Chul Ye  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in distillation and flow-map models have enabled deterministic one- or few-step generation for high-quality data, facilitating a new branch of reward alignment approaches that directly optimize the initial noise from a Gaussian distribution. However, most existing initial-noise optimization methods rely on first-order gradient information, which is either inapplicable or suffers from instability and inefficiency in black-box reward scenarios. Here, we introduce ZeNOVA, a stable and efficient initial noise alignment method in a gradient-free manner. Specifically, we address existing algorithms' major challenge in black-box scenarios through annealed soft-value guidance, manifold-constrained hyperspherical Langevin dynamics, and Metropolis-Hastings jumping. Extensive experiments on image and video generative models show that ZeNOVA outperforms all evaluated zeroth-order baselines by optimizing the initial noise toward higher rewards substantially more stably while exploiting the geometry of the Gaussian prior, demonstrating its practical applicability to various black-box reward alignment.

---


### 56. [What Should an Agent Remember? Disentangling Retention from Retrieval in Bounded-Memory Evaluation](https://arxiv.org/abs/2610.00366)

**<font color=#1a73e8>作者：</font>** Juli Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A persistent agent must decide both what to retain as information arrives and what to surface once a query appears, yet memory evaluations can confound these decisions by comparing methods that differ in both retention and selection. We build a streaming-recall benchmark crossing retention and selection rules and evaluate every condition on the same 300 seeded episodes. Holding access fixed, query-aware selection improves required-fact recall by 15.5 percentage points (95% CI: 12.8 to 18.2), whereas a mixed comparison that also changes history access reports a 68.7-point advantage, of which 53.2 points are attributable to access. Under bounded retention, query-aware, dense, and oracle selection reach the retention ceiling, and all 319 observed failures in the bounded recency condition are caused by eviction rather than ranking errors. Recall falls to 0% as targets recede sufficiently far into the past. Repeating the evaluation on SQuAD preserves the retention ceiling while showing that dense retrieval can outperform lexical retrieval on natural text. These results show that bounded-memory evaluations should hold access fixed and report retention and selection separately.

---


### 57. [M$^2$Weather: A Benchmark for Joint Multi-Station and Multi-Variable Weather Forecasting](https://arxiv.org/abs/2610.00370)

**<font color=#1a73e8>作者：</font>** Rongwen Li, Xiao Wang, Mingyang Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Station weather forecasting is fundamentally shaped by both complex spatial dependencies across stations and strong physical coupling among weather variables. However, existing studies often consider these relationships separately and use different datasets and experimental settings, hindering systematic assessment of their individual and joint contributions. In this paper, we introduce $M^2$Weather, a benchmark for joint multi-station and multi-variable weather forecasting. Through multi-criteria quality control and station stratification, we collect 2,809 high-quality stations with 5 physically coupled weather variables across three spatial scales: France, Europe, and Global. This multi-scale design lets us examine whether conclusions persist from national to global station networks. We also introduce unified training and evaluation protocols to enable fair comparison of different station-variable modeling paradigms. To further examine the benefits of modeling station-variable relationships, we design a lightweight, plug-and-play adapter. With a trained weather forecasting model, this adapter can introduce missing station or variable relationships without retraining the model. This enables fair and efficient investigation of station-variable relationships. Systematic evaluation of 16 representative models shows the benefits of jointly modeling station and variable relationships. Completing missing relationships further reduces MSE for all adapted models on all three datasets. Together, these results identify the complementary information across stations and variables as an important resource for improving station weather forecasting. Our code can be obtained at this https URL.

---


### 58. [Deny Without Disabling: Authorization-Paired Evaluation and Control for Multi-Agent Systems](https://arxiv.org/abs/2610.00371)

**<font color=#1a73e8>作者：</font>** Yunbei Zhang, Saiyue Lyu, Janet Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems derive their capabilities from sharing evidence, delegating tasks, and combining information across agents. The same process creates a safety problem: contributions that are admissible in isolation can jointly enable a prohibited use. Blocking every sensitive action avoids disclosure but defeats the purpose of collaboration. We introduce authorization-paired evaluation, which makes blocking prohibited uses and completing required authorized uses a joint success criterion, and FlowReview, a framework connecting object resolution, permission ranking, and deterministic enforcement. In controlled composition experiments, reviewing combined artifacts reduces the denied-commit rate from 86.0% to zero with no loss of authorized supply. Our findings show that preserving information and lineage alone does not ensure correct permission attribution. Object identity and permission must remain connected to execution through components whose outputs can be verified. Together, these findings establish a system-level requirement for multi-agent safety: govern composed information flows while preserving the authorized capabilities that make collaboration useful.

---


### 59. [Faithful Chart Generation for Multimodal Deep Research: Frame-Evidence Co-Adaptation](https://arxiv.org/abs/2610.00374)

**<font color=#1a73e8>作者：</font>** Yuxin Yue, Yingchen Zhang, Ruqing Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Analytical charts in multimodal deep research encode quantitative claims, requiring every visualized value to be faithfully grounded in supporting evidence. Unlike retrieved images that mainly provide contextual information, charts require numerical fidelity: visualized values should not only match retrieved evidence quantitatively but also preserve its original meaning and scope. However, achieving such fidelity remains challenging because current systems usually construct visualization plans before knowing what quantitative evidence can actually be retrieved from the web. As a result, predefined plans may require entities, temporal ranges, or comparison dimensions that the retrieved evidence only partially supports. Existing approaches mainly address this issue through post-hoc verification after chart plans are fixed, enabling unsupported values to be identified but leaving the underlying visual frames unchanged. To address this challenge, we propose Frame-Evidence Co-Adaptation (FECA), an evidence-adaptive visual planning framework for multimodal deep research. Inspired by the bidirectional sensemaking process in Data-Frame Theory, FECA models chart generation as an iterative interaction between visual frames and retrieved evidence. Each visual frame is adaptive: the frame guides evidence acquisition, while retrieved evidence determines whether the frame should be accepted, revised, or dropped before rendering. By coupling visualization planning with evidence availability, FECA shifts chart generation from fixed-plan verification to adaptive evidence-grounded visual reasoning. Experiments on 100 real-world research topics show that FECA substantially improves numerical fidelity while preserving report quality and chart utility.

---


### 60. [STCFormer: Adaptive Spatio-Temporal Modeling with Dynamic Cluster Transformer for Station-based Weather Forecasting](https://arxiv.org/abs/2610.00377)

**<font color=#1a73e8>作者：</font>** Rongwen Li, Haixin Xie, Mingyang Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Station-based weather forecasting supports daily life and economic activity, yet accurate forecasts require modeling complex spatial dependencies among stations. Recent clustering-based selective modeling offers a promising alternative to dense inter-station interactions. However, a grouping shared across an observation window may obscure local changes in station relationships, while intra-cluster interactions alone may miss important global context. The theoretical advantages of selective interactions over dense connectivity also remain insufficiently understood. We therefore propose STCFormer, an adaptive spatio-temporal Transformer that dynamically groups stations according to their local evolution within each temporal patch. Its Cluster-Guided Attention Block combines fine-grained local attention within clusters and global attention over regional state summaries, allowing each station to access information beyond its own cluster. We further show that a derived Lipschitz upper bound for cluster-conditioned local attention is no larger than its fully connected counterpart, explaining a potential robustness benefit and motivating the design of InfoLoss. Experiments on three real-world weather datasets spanning eight temperature and wind forecasting tasks show that STCFormer achieves the lowest 24-hour mean squared error on all eight tasks and ranks first or second in 47 of 48 comparisons across metrics and forecasting horizons. Ablations and case studies further confirm the benefits of locally adaptive grouping and complementary local-global interactions. Our code can be obtained at this https URL.

---


### 61. [Fusion techniques of time frequency-based images to predict the outcome of rTMS depression therapy](https://arxiv.org/abs/2610.00380)

**<font color=#1a73e8>作者：</font>** Wael Korani, Md Fahimul Kabir Chowdhury, Mohammed Aledhari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Depression is a mental condition that can lead to suicide and self-harm. Predicting the outcome of depression treatment is one of the most difficult tasks for clinicians. Among various treatment options, repetitive Transcranial Magnetic Stimulation (rTMS) is a widely used non-invasive method. Predicting rTMS response using Electroencephalogram (EEG) data is difficult because of high inter-subject variability and limited features from single-domain analysis. We introduce two fusion techniques, montage and blending, to overcome these limitations and extract richer features from EEG-derived Time-Frequency (TF) images. We then propose a lightweight custom Convolutional Neural Network (CNN) trained on fused TF representations. \textcolor{black}{We use a primary dataset of 15 patients and a secondary dataset of 46 patients. We run two sets of experiments. The first set uses segment-level 10-fold cross-validation. In this setup segments from the same patient can appear in both training and testing. The Montage CWT\_ST fusion reaches 99.90\% accuracy on the primary dataset and 91.90\% on the secondary dataset. The second set uses strict subject-disjoint cross-validation. All segments of a patient stay in one fold and no patient appears in both training and testing. Performance collapses. We test four time-frequency methods, six fusion mechanisms, and fourteen model architectures. With one exception, every configuration on both cohorts falls between AUC 0.31 and 0.54 and every 95\% confidence interval contains 0.5. A patient-level permutation test on the best standalone method returns $p = 0.703$. The best subject-level result is Montage CWT\_ST on the primary cohort, which reaches AUC $0.874 \pm 0.183$ and 82.7\% accuracy.

---


### 62. [On the Relationship between Model Quantization and Model Inversion Attacks](https://arxiv.org/abs/2610.00382)

**<font color=#1a73e8>作者：</font>** Rongke Liu, Youwen Zhu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Model quantization reduces the numerical precision of neural network weights and activations to lower storage and computational costs. Model inversion attacks recover or reconstruct sensitive training data or inference inputs from model outputs or intermediate features, so quantization may also alter their effectiveness. However, two questions remain unresolved: How does model quantization affect model inversion? How do data characteristics influence this relationship? To address the first, we bound quantization-induced changes in mutual information between inputs and a categorical variable defined by prediction probabilities, distinguishing informational effects from attack optimization obstacles. To address the second, we identify data-dependent changes in feature distributions and inversion outcomes, with pronounced quantization sensitivity differences at 4 bits. These insights guide a privacy-aware post-training quantization method that improves inversion resistance while recovering utility. It uses a Fisher-type task-sensitivity proxy for budget-aware bit allocation, calibrates activation ranges, and jointly optimizes weight and activation scales and weight-rounding decisions with task-recovery and geometry-retention objectives and scale and rounding regularization. Experiments cover multiple metrics, neural network architectures, and face, palmprint, and iris recognition tasks. On ResNet-50, Palm at 4 bits reduces RL-MIA's strict success from 54% to 26%, while accuracy decreases from 99.01% to 96.55% relative to FP32. Our method also supports output-level defenses: adding Stealthy Shield Defense (SSD, epsilon = 0.1) to Iris at 4.5 bits reduces BREP-MI's strict success from 63.33% to 37.33%, while accuracy decreases from 92.8% to 87.6% relative to quantization alone.

---


### 63. [EvoGen-Harness: Learning Where and How to Evolve Image-Generation Harnesses](https://arxiv.org/abs/2610.00383)

**<font color=#1a73e8>作者：</font>** Jiabin Luo, Yinan Liu, Chunlei Meng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern text-to-image (T2I) systems can be improved without modifying generator parameters by adapting the external system around frozen generators. However, existing approaches typically optimize a predefined dimension, such as prompts, routing, or workflows, restricting the space in which generation failures can be corrected. Allowing multiple generator-external responsibilities to evolve provides a broader adaptation space, but introduces a new challenge: visual feedback reveals what failed, but not where persistent evolution should occur or how this space should be explored efficiently. We introduce EvoGen-Harness, a generator-agnostic framework for multi-responsibility image-generation harness evolution, together with Trace (Trajectory-Relative Attribution and Coordinated Evolution). Trace aggregates evidence across stochastic executions, uses failure attribution as a search prior to focus candidate updates, and progressively re-attributes residual failures to coordinate evolution across responsibilities, while No-Patch and held-out validation prevent unnecessary or harmful updates. Across GenEval2, T2I-CompBench++, and WISE, EvoGen-Harness improves over the strongest evaluated baselines by +0.2633, +0.0720, and +0.0752, respectively, while achieving 87.9-91.4% attribution recall, 94.8% No-Patch accuracy, and only 1.9% regression. These results demonstrate that attribution-guided multi-responsibility evolution can substantially enhance frozen T2I systems beyond single-dimension adaptation.

---


### 64. [Interpretable Synthetic Medical Tabular Data Generation for Clinical Decision Support Using Fuzzy Cognitive Maps](https://arxiv.org/abs/2610.00391)

**<font color=#1a73e8>作者：</font>** Michael Vasilakakis, Dimitris K. Iakovidis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic medical tabular data generation has become essential for developing and validating computer-based medical systems (CBMSs) when real clinical data is restricted due to privacy, ethical, or data availability limitations. Existing probabilistic and deep generative models often lack interpretability and fail to preserve clinically meaningful dependencies, limiting their suitability for safety-critical applications. This paper proposes a novel application of Fuzzy Cognitive Maps (FCMs) in a framework for synthetic medical tabular data generation with explicit causality and privacy preservation. Clinical features are described using linguistically interpretable fuzzy sets, and inter-feature dependencies are encoded as FCM edge weights computed from fuzzy set intersections. Synthetic patient records are generated by propagating randomly initialized linguistic activation vectors through the FCM until convergence, followed by defuzzification to produce clinically coherent numerical values. The approach natively handles mixed data types, and domain constraints common in health records. Experimental evaluation on UCI medical benchmark datasets demonstrates competitive performance under a Train-on-Synthetic-Test-on-Real (TSTR) protocol. The proposed method achieves accuracy of up to 0.81 and AUROC of up to 0.90 on the Heart Disease dataset, matching or exceeding TVAE and Gaussian Copula baselines while running exclusively on CPU. Fidelity metrics including KS Complement (up to 0.91) and Correlation Similarity (up to 0.95) confirm strong statistical coherence, and DCR Baseline Protection scores consistently exceed those of TVAE, confirming adequate privacy guarantees. These results demonstrate that causally grounded, interpretable fuzzy modeling offers a computationally efficient and transparent alternative to deep generative models for trustworthy synthetic data generation in CBMSs.

---


### 65. [Specificity-Aware Diffusion Steering via Variance-Reduced Sequential Monte Carlo](https://arxiv.org/abs/2610.00395)

**<font color=#1a73e8>作者：</font>** Luran Wang, Linrui Ma, Hannes Stärk 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inference-time steering enables pretrained diffusion models to satisfy new constraints without full retraining. However, specificity-aware generation is difficult: repelling samples from a negative reference distribution can also erode the positive distribution where the two overlap. The key challenge is to suppress negative mass while minimally distorting the positive distribution. We address this problem by formulating specificity-aware steering as a target-design problem and deriving a target distribution from an overlap-based objective. The resulting target keeps the desired reference distribution only in regions where it is sufficiently preferred over the undesired reference distribution, giving a likelihood-ratio interpretation of specificity. To sample from the corresponding time-dependent target path, we develop a Sequential Monte Carlo sampler with a variance-minimized local proposal. We further introduce a practical fixed-noise optimization procedure with the Jacobian--vector products with the desired and undesired score fields. Experiments on synthetic task, class-contrastive generation, text-to-image tasks and peptide-MHC (p-MHC) binder show that the proposed method suppresses undesired regions more effectively, reduces mode shift, and improves sampling stability by decreasing the SMC weight collapse compared with negative-guidance baselines. Code is available at: this https URL

---


### 66. [NEUROTOKEN: Joint Source and Directional AAD with Envelope Decoding via Conditional Flow Matching](https://arxiv.org/abs/2610.00397)

**<font color=#1a73e8>作者：</font>** Ali Alavi, Donald S. Williamson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Identifying which speaker a listener is attending to in a noisy room -- the cocktail-party problem -- is the missing ingredient for next-generation hearing aids and brain-computer interfaces: it tells the device whose voice to amplify. Auditory attention decoding (AAD) reads this answer from EEG, but the literature splits into disconnected pieces: directional-AAD classifies side but does not map side to stream; regression-based source-AAD ranks candidate streams by a single Pearson correlation that is intrinsically noisy at the 1-5 s windows real devices need; and envelope reconstruction has no native AAD rule. We argue the right object is not any single statistic but the conditional likelihood of the attended envelope given EEG, and we make this practical with NEUROTOKEN: a single network whose three heads share one EEG front-end, with a conditional flow-matching head (ATTUNEFLOW) that scores candidates by an integrated velocity-residual likelihood ratio. Two inference-time ensembles -- QUADTRACK (four complementary statistics) and ENV-FLOW (z-normalised QUADTRACK+ATTUNEFLOW) -- absorb per-statistic failure modes for free. On KU Leuven, DTU, and NJU at 5 s, ATTUNEFLOW lifts per-segment source-AAD by 9%-16% over the strongest non-generative baseline and shrinks across-subject variance by ~3x; trial-level fusion exceeds 93% on two of three datasets. In parallel reproductions we show that canonical 95-97% direction-AAD numbers collapse by 17%-45% under a strict trial-disjoint protocol, clarifying both the true ceiling and why a likelihood-based formulation is needed.

---


### 67. [WIPSNet: Deep Learning for Paediatric Wheeze Detection from Overnight Impedance Pneumography](https://arxiv.org/abs/2610.00398)

**<font color=#1a73e8>作者：</font>** Felix Oury, Harley Day, Karina Mayoral 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Overnight impedance pneumography (IP) is used to monitor paediatric respiratory health. Its current clinical readout, the Expiratory Variability Index (EVI), compresses each IP recording into a single scalar and achieves an AUC of 0.633 for night-level wheeze classification. We introduce Wheeze Impedance Pneumography Scalogram Network (WIPSNet), a 3D ResNet operating on stacked continuous wavelet transform scalograms of overnight IP signals. On a 15-patient cohort (60 nights, 281 hours), WIPSNet achieves an AUC of $0.783 \pm 0.026$, outperforming EVI, a state-space model (Mamba), and two modern sleep-staging architectures. Performance peaks at a volumetric depth corresponding to 32 minutes of temporal context, suggesting that multi-scale temporal aggregation is important for modelling nocturnal respiratory dynamics. Overall, these results indicate that structured time-frequency representations combined with 3D convolutional architectures provide an effective approach for learning from long, irregular physiological time series.

---


### 68. [Dissonant ballerinas and crafty carrots: a comparative multi-modal analysis of Italian brain rot](https://arxiv.org/abs/2610.00402)

**<font color=#1a73e8>作者：</font>** Anca Dinu, Andra-Maria Florescu, Marius Micluta-Campeanu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents a comparative multi-modal analysis of Italian and Romanian brain rot memes, investigating the factors that contribute to its appeal and the linguistic and cultural distinctions between the two versions. To conduct this analysis, we introduce a multi-modal brain rot dataset named CRIB (Collection of Romanian and Italian Brain rot), a manually curated collection of 240 TikTok videos stratified by language (Italian, Romanian) and popularity, on which we examine textual, acoustic, and visual features. Our findings indicate that popularity is not significantly correlated with textual elements like sentiment, absurdity, or rhyme, or acoustic elements such as vocal features or sentiment of the sound. Instead, in Romanian language, video-level dynamics, specifically faster cutting speeds and a more rapid overall pace, are strong predictors of a video's success. The cross-linguistic analysis reveals significant differences. Italian brain rot is textually more negative, exhibits higher perplexity, and uses more rhyme, while its sound is characterized by higher melodic range and loudness. Romanian audio is spectrally brighter with more erratic pitch variations.

---


### 69. [The Conflict Between Logic and Memory: Learning Higher-Order Interactions in Shallow MLPs](https://arxiv.org/abs/2610.00403)

**<font color=#1a73e8>作者：</font>** Gongyue Zhang, Honghai Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A network can fit its training examples while failing to recover the rule that generated their labels. We examine this separation in single-hidden-layer multilayer perceptrons (MLPs), using synthetic tasks that control interaction order and the presence of nuisance inputs. We establish elementary benchmark properties: pure parity contains no predictive lower-order marginals, admits an exact Bayes posterior, and can be represented on clean latent inputs by a width-$k$ ReLU network. Experiments then identify distinct optimization outcomes. In a matched order-2--4 sweep, SGD, Adam, and Muon all reach 100\% peak test accuracy at order two; at order three they reach 96.25\%, 50.87\%, and 76.82\%, respectively, while Muon reaches 99.21\% at order four. In a separate mixed-order task, freezing only the first-layer weights connected to independent nuisance inputs raises AdamW's epoch-10 accuracy from 44.73\% to 95.07\%. Removing the same inputs only at test time raises it to 48.38\%. Thus, nuisance-weight learning changes the training outcome beyond its immediate effect on prediction. Bias interventions expose a connection between target symmetry and shallow ReLU representations. In a compact signal-only regime, both SGD and Muon learn orders five through eight, with higher SGD peak accuracy at orders nine through eleven. Together, the results show how optimization and nuisance learning constrain the higher-order rules realized by a shallow network.

---


### 70. [UniBuc at SemEval-2024 Task 2: Tailored Prompting with Solar for Clinical NLI](https://arxiv.org/abs/2610.00408)

**<font color=#1a73e8>作者：</font>** Marius Micluta-Campeanu, Claudiu Creanga, Ana-Maria Bucur 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper describes the approach of the UniBuc team in tackling the SemEval 2024 Task 2: Safe Biomedical Natural Language Inference for Clinical Trials. We used SOLAR Instruct, without any fine-tuning, while focusing on input manipulation and tailored prompting. By customizing prompts for individual CTR sections, in both zero-shot and few-shots settings, we managed to achieve a consistency score of 0.72, ranking 14th in the leaderboard. Our thorough error analysis revealed that our model has a tendency to take shortcuts and rely on simple heuristics, especially when dealing with semantic-preserving changes.

---


### 71. [VANDAM: Viewing a nucleotide sequence with DNA molecular priors](https://arxiv.org/abs/2610.00411)

**<font color=#1a73e8>作者：</font>** Jeremy Levy, Ariel Larey, Yury Nahshan 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contemporary Genomic Foundation Models (GFMs) rely on a DNA-as-a-string paradigm that employs masked token prediction objectives for pretraining. However, this abstraction does not explicitly model the biochemical, structural, and physical properties essential to biological function. Many molecular properties can be estimated from sequence using established biophysical models, so their utility lies not in providing an independent modality, but in introducing priors that training objectives can explicitly exploit. We introduce VANDAM, a framework that extends the training of GFMs with DNA molecular priors. In self-supervised training, VANDAM predicts regional molecular properties from pooled representations. When functional labels are available and can reward retaining molecular priors, local features are additionally injected at the input. VANDAM consistently improves downstream performance across four architecture families and nine held-out genomic tasks by complementing token-based objectives. Probing experiments further demonstrate that the use of molecular priors generalizes to other unseen molecular properties.

---


### 72. [Do Better Scores Mean Better Physics? Physics-Grounded Explanations for Sim2Real Neural Operators](https://arxiv.org/abs/2610.00415)

**<font color=#1a73e8>作者：</font>** Somyajit Chakraborty, Xizhong Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine-learning surrogates accelerate physical simulation, but lower prediction error need not coincide with lower error in physically relevant flow statistics. We examine this question for flow around a NACA4418 airfoil using paired computational-fluid-dynamics simulations and experimental particle-image-velocimetry measurements. A mean-preserving input intervention removes velocity fluctuations from selected regions of observed flow histories. Across four neural operators, removing fluctuations from the most energetic 10% of valid observed cells changes forecasts more than equal-area random removal. Because the masks are not matched for removed fluctuation energy, this contrast measures sensitivity, not independent evidence of physical importance. Separately, a CNO has lower velocity-field error but substantially higher two-component fluctuation-energy error than the reference on both analysis subsets. An output attenuation stress test also demonstrates disagreement between benchmark errors and domain-summed fluctuation energy. These single-benchmark results motivate reporting complementary physical diagnostics alongside aggregate prediction scores; they do not establish counterfactual physical correctness.

---


### 73. [Source Identification Is Not Fitness Testing: Measuring the Limits of Synthetic-Data Attribution](https://arxiv.org/abs/2610.00417)

**<font color=#1a73e8>作者：</font>** Joss Armstrong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Repeated training on model-generated data can degrade later models. One possible response is to use provenance when deciding which generated examples to reuse. We test both how reliably that provenance can be recovered and whether it helps identify better training data. Using financial-risk text, we first identify the source of generated passages and then repeat the test after rewriting them. Generator attribution is 98.7% accurate on the original passages but falls to 53.1% after paraphrasing and 29.0% after style rewriting. Generated-versus-human detection remains close to perfect against the tested human comparison set. We then compare two ways of selecting generated examples over three rounds of generation and retraining. One uses source information. The other uses a score from a separate reference model. The two rules select different examples, but the planned comparison does not detect a stable difference in the degradation of the resulting models. The results show that identifying where data came from and identifying which data are useful for training are separate problems. The experiment therefore separates source identity, criterion-facing selection, and recursive training outcome: neither the provenance score nor the tested criterion-facing proxy is established as sufficient for future recursive behaviour.

---


### 74. [Scores That Hold, Benchmarks That Leak: Measuring Dataset Contamination in Public Brain-Tumor MRI Classification](https://arxiv.org/abs/2610.00421)

**<font color=#1a73e8>作者：</font>** Bhanu Prakash Vangala, Sowmya Guda, Latha Peddi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated classification of brain tumors from MRI is a heavily published application of deep learning in medical imaging, with reported accuracies on public benchmarks routinely exceeding 98%. However, accuracy does not capture a critical dimension of benchmark quality: dataset integrity, defined as the independence of test from training data at the image, patient, and acquisition-source levels. We introduce a three-layer contamination framework comprising duplicate, patient, and source-label leakage to assess the public corpora on which this literature rests. We audit the three most widely used corpora against a chest-radiograph negative control and quantify each layer's effect on measured performance across nine architectures and three evaluation conditions. Contamination is severe at every layer: 28.8% of the dominant corpus's official test split has a near-twin in its own training split, a second corpus leaks 22.3% of its test images byte-identically, 95.5% of traceable test images share a patient with training, and file-header features containing no anatomy separate tumor from no-tumor at 0.959 balanced accuracy, at parity with fine-tuned ResNet backbones. The unexpected result is that removing every identified leaked test image leaves balanced accuracy essentially unchanged: stable performance after deduplication does not establish benchmark integrity. Our findings establish dataset integrity as a distinct, measurable axis of benchmark quality that a stable leaderboard cannot certify. For biomedical research, reported accuracy on these corpora alone does not establish that a model has learned to recognize tumors rather than exploit dataset-specific cues. We release the contaminated-file lists, recovered patient identifiers, and deduplicated splits.

---


### 75. [The Life Cycle of a Massive Activation: Stochastic Birth, Weight-Decay-Driven Growth, and Competitive Consolidation](https://arxiv.org/abs/2610.00423)

**<font color=#1a73e8>作者：</font>** S. Aaron McClendon, Jorge Gallego-Feliciano, Antonios Saravanos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Massive activations, residual-stream coordinates with magnitudes far larger than typical activations, are associated with attention sinks in transformers, but how their scale is regulated during training remains incompletely understood. Combining training-trajectory analyses and controlled interventions, we trace their emergence, growth, and consolidation. Sink-carrying channels vary across random seeds but stabilize early within each run. Over longer training, surrounding channels erode and the sink concentrates onto a few redundant carriers. Across ablations, gradient attenuation follows the sink token's collective root-mean-square magnitude rather than any single channel, making collective scale central to understanding their effects. Our central result is that weight decay causally controls the turnover of global activation scale. In controlled continuations, removing decay near the peak allows this scale to keep rising, whereas retaining it produces decline even at constant learning rate. We develop a balance model for the rise and peak of massive-activation magnitude, in which AdamW-preconditioned growth opposes weight decay. Sweeping the decay coefficient $\lambda$ shifts peak timing approximately log-linearly and yields peak magnitudes scaling approximately as $\lambda^{-1/2}$, consistent with this balance. Optimizer measurements further show that preconditioning sustains the large-channel cohort against decay even when raw maintaining forces are too small to do so. Together, these findings connect the observed life cycle to scale-regulating training dynamics and establish weight decay as a training-time lever on activation magnitude.

---


### 76. [One pool, many targets: a conservation layer and what archival data can identify](https://arxiv.org/abs/2610.00445)

**<font color=#1a73e8>作者：</font>** Zahra Khodagholi, Niloofar Yousefi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pairwise guide--transcript scores do not enforce conservation of a finite guide-loaded RISC pool when they are interpreted independently as occupancies. We formulate a differentiable scalar equilibrium layer: one conservation equation with a unique positive root and exact implicit gradients. It yields a redistribution theorem, a qualified high-resource limit, an analysis of the retrieval approximation, and a conditional rank-invariance result: within one construct at one dose, rankings by fractional occupancy cannot distinguish equilibrium from independent scoring. We therefore audit the two experiments that proposition leaves open, dose and cross-context, on archival off-target data. Corrected thermodynamic affinities associate weakly with measured repression in the direction a working predictor requires, but a paired permutation test and a construct-cluster bootstrap do not establish added predictive value from the coupling: what survives their differing permutation-null baselines is \GapNet{}, a descriptive \GapNetOverSE{} of the equilibrium association's cluster standard error. The dose fits are heterogeneous and frequently violate the model-implied exponent constraint, which is superlinear rather than sublinear, so these data do not identify the competition parameter. A saturable compression of the competitor set holds both accuracy targets on held-out guide families but is not faster at the size measured. The contribution is a reusable conservation operator and the experimental information needed to test it. The code for this study is available at this https URL.

---


### 77. [Exact information accounting for SGD methods](https://arxiv.org/abs/2610.00446)

**<font color=#1a73e8>作者：</font>** Akshay Balsubramani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As an alternative to the standard geometric analyses, we give an exact, information-theoretic analysis of stochastic gradient descent (SGD) and its variants. We show that a preconditioned SGD step is the posterior-mean update of a Gaussian Bayes model, and that its one-step regret splits into an intrinsic-time cost and a change in comparator information. The split extends to an identity for the objective itself. Convex convergence, strict-saddle-point escape, the link between flatness and generalization, the standard learning-rate schedules, adaptive optimizers, and the noisy, momentum, heavy-tailed, and gradient-free variants of SGD each correspond to a term or a special case of this identity. We measure its terms on synthetic and real training runs. On real networks it attributes the slack of classical convergence bounds to the terms their derivations drop and separates optimizers that reach the same training loss. That separation follows the number and consistency of their steps. Its relation to which of them generalizes better differs between networks. For gradient-free SGD the identity determines how a curvature preconditioner should enter the update. The sharpness-based generalization certificate it yields, with a data-independent isotropic prior, is vacuous at network scale unless the curvature spectrum is nearly flat across all parameters.

---


### 78. [Frozen Scenes, Shifting Winners: Configuration Fragility in Text-to-3D Evaluation](https://arxiv.org/abs/2610.00447)

**<font color=#1a73e8>作者：</font>** Anson Y. Lam, Shuqing Li, Michael R. Lyu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can a text-to-3D leaderboard change when every generated scene stays fixed? We audit this question for rendered-image evaluation, where camera settings and caption wording become part of the measurement protocol. Across 300 frozen scenes from six generators, we vary eight render and caption factors for 19 alignment evaluators plus one perceptual-quality control, then test four targeted scene degradations. Peak configuration variance exceeds between-generator variance for 17/19 alignment evaluators, with prompt-bootstrap lower bounds above 1 for 11/19. Rankings are more stable than scores, yet 18/19 evaluators change their point-estimate winner under some configuration. Pairwise protocol margin envelopes show which comparisons keep their direction across the tested settings. Selected pairs have opposite pointwise intervals, but no reversal survives simultaneous inference over the full search. Thus the observed winner changes are descriptive, not confirmed changes in generator superiority. Sensitivity remains separate: no evaluator, even the prompt-free control, exceeds 67% tie-adjusted directional discrimination on layout scrambling, which is diagnostic rather than human-validated ground truth. The audit separates score stability, decision uncertainty, and targeted sensitivity, and recommends reporting (generator, score, card ID) with protocol-dependent comparisons and selection-aware uncertainty.

---


### 79. [PACT: End-to-End Learning of Human Pose, Contacts, and Forces from Video](https://arxiv.org/abs/2610.00451)

**<font color=#1a73e8>作者：</font>** Rikhat Akizhanov, Yangsong Zhang, Nikolai Kaliazin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human motion, environmental contacts, and interaction forces are governed by common physical laws, yet existing approaches typically separate visual pose reconstruction from contact and force estimation. This separation limits joint reasoning and can propagate errors between stages. We introduce PACT, an end-to-end model that jointly learns to estimate human pose, contacts and contact forces from monocular video. Our approach augments a human reconstruction foundation model with learnable contact-force tokens and a temporal transformer that integrates visual features with world-space motion. Joint prediction heads refine human poses and estimate contacts and forces, while physics-based supervision encourages consistency between the reconstructed motion and interaction forces. To address the scarcity of force annotations, we develop a data annotation pipeline that combines contact labeling with physics-based motion and force optimization, producing training supervision from synthetic and real-world videos. We also introduce a real-world climbing benchmark ForceWall with climbing videos and corresponding ground-truth contact forces obtained from the force sensors. Experiments demonstrate state-of-the-art contact and force estimation, outperforming staged reconstruction approaches and generalizing to interactions beyond the training distribution. These results support end-to-end joint learning as an effective approach to recovering human motion and physical interactions from video.

---


### 80. [PixelDense: Dense Prediction as Representation Alignment for Pixel Diffusion](https://arxiv.org/abs/2610.00483)

**<font color=#1a73e8>作者：</font>** Lehan Yang, Daiqing Qi, Wenhao Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Representation alignment (REPA) accelerates diffusion transformer training, but its alignment targets are almost exclusively semantic encoders such as DINOv2 and CLIP. Recent analysis points to spatial structure, not global semantics, as the carrier of the alignment effect, yet dense-prediction foundation models trained to predict that structure remain overlooked as REPA targets. In pixel-space diffusion, SAM2, Depth Anything v2, and Metric3D v2 each outperform the DINOv2-only GenEval baseline, with the two geometric teachers leading the segmentation teacher. A flat sum of all four teachers, however, lands below the best single geometric teacher, as semantic and geometric gradients compete for one denoiser projection. We introduce PixelDense, which routes DINOv2 and SAM2 through a semantic projection stream, routes Depth Anything v2 and Metric3D v2 through a geometric projection stream, and adds a weight-space orthogonality penalty that keeps the two streams in disjoint subspaces. All four teachers are frozen during training and dropped at inference. Applied to PixelGen and DeCo with a single recipe, PixelDense improves GenEval, DPG-Bench, and HPS v2.1, raises PixelGen-XXL's GenEval Overall from 0.7927 to 0.8093, and beats every single-teacher and unfactored multi-teacher variant. In partial-noise reconstruction, independent panoptic, depth, and surface-normal probes show up to 53.1% PQ gain and 36.0% depth AbsRel reduction at $\tau=0.5$ across COCO and Flickr30K. From random initialization, PixelDense also reaches the baseline's peak GenEval 1.23x faster. In SDEdit editing on PIE-Bench, PixelDense keeps more of the source background and layout at every edit strength, raising background PSNR by up to 2.2 dB.

---


### 81. [EurekaBench: Measuring Agentic Ability to Discover New Scientific Insights](https://arxiv.org/abs/2610.00492)

**<font color=#1a73e8>作者：</font>** Jiayi Geng, Zhengxuan Wu, Kevin S. Chen 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When Isaac Newton discovered the law of gravitation, he did so through an iterative process of analyzing observed data such as planetary patterns, finding the underlying mechanisms by describing patterns in mathematical equations, and refining his theory against the Moon's orbit, revealing the startling insight that the same force governs both falling apples and orbiting planets. Would it be possible for AI agents to make similar discoveries? To measure this ability, we introduce EurekaBench, a cross-domain benchmark that tests AI agents' ability to conduct long-horizon experiments and discover mechanisms that explain observations. We evaluate these mechanisms by the scientific insights that can be derived from them. EurekaBench contains an expert-verified set of 26 long-horizon tasks across neuroscience, computer science, chemistry, astrophysics, geophysics, and plasma physics, with a total of 306 scientific insights that the discovered mechanisms are expected to support. Our evaluation framework tests three axes of scientific discovery: agents' ability to follow known scientific constraints, the predictive accuracy of the discovered mechanisms, and whether these mechanisms yield scientific insights or inform future research. Our results show that current AI agents often overly fixate on predictive accuracy optimization, surpassing human scientists, while falling substantially short in deriving scientific insights.

---


### 82. [One-Step Generative Modeling via Training Dynamics Action](https://arxiv.org/abs/2610.00518)

**<font color=#1a73e8>作者：</font>** Zhangyong Liang, Ying Huang, Haibin Ling  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> One-step generative models construct a static generator through iterative training-time transport. Existing transport objectives primarily assess distributional motion, although a neural generator needs to realize the requested sample displacements jointly through shared parameter updates. The training-time construction raises the question: \emph{once training becomes the iterative process that constructs the final one-step map, what to optimize: the next distributional move, or the route by which the finite generator learns the final map?} To address the question, we introduce \textbf{T}raining \textbf{D}ynamics \textbf{A}ction (\textbf{TDAction}), which selects transport targets according to local shared-parameter realization cost while retaining a prescribed level of distributional progress. We formulate the cost as a soft-terminal control problem and derive a closed-form Batch Tangent Action-to-Go value that accounts for parameter effort and terminal mismatch. The criterion captures cross-sample interactions omitted by independent pairwise costs; under isotropic mobility, the criterion agrees with quadratic Euclidean assignment for deterministic balanced couplings. Randomized tangent probes provide a low-rank implementation that constructs shared detached targets without adding an inference-time trajectory. Controlled studies examine the relationship between generator geometry, transport selection, and realized local action. On ImageNet $256\times256$, TDAction attains an FID below $1.1$ without distillation.

---


### 83. [Harbormaster: Evidence-Gated, Replay-Safe Maritime Anomaly Detection on AWS](https://arxiv.org/abs/2610.00519)

**<font color=#1a73e8>作者：</font>** Arun Sharma  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Ships broadcast their positions through the Automatic Identification System (AIS), and those reports can be false or missing. An operator who acts on an anomaly alert needs that alert to be attributable, reviewable, and recoverable after a failure. This paper describes Harbormaster, a production-shaped system on AWS that follows three rules. Physics checks run on every report before any learned model runs. The DynamoDB read store is an idempotent projection of PostgreSQL, and a guard on the log sequence number (LSN) of each change protects every write to it. A candidate model must pass a holdout gate and a shadow comparison before a canary gives it traffic, and a burn-rate check guards each canary step. The paper proves that replaying any prefix or suffix of the change log leaves each projected key at the value of its highest applied LSN. It also notes effects this result does not cover, such as repeated cache invalidations and repeated audit rows. In a bounded AWS window, a one-hour soak returned 35,999 HTTP 200 responses to 36,000 requests, with a 95th-percentile (p95) client latency of 142.751 ms. In a separate bounded AWS run of 900 s, the stream path received a burst of 400 records/s, and its consumer lag later drained to zero. Every number in the paper carries a label that says where it was measured, and the paper lists the parts of the design that were never built.

---


### 84. [SimplexUQ: An Evaluation Framework and Benchmark for Conformal Uncertainty on Simplex-Valued Predictions](https://arxiv.org/abs/2610.00523)

**<font color=#1a73e8>作者：</font>** Liang You, Hengyu Shi, Dongwen Ou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conformal prediction guarantees marginal coverage, but a single calibration threshold can still spread that coverage unevenly, over-covering easy regions and under-covering hard ones. SimplexUQ is, to our knowledge, the first benchmark and reproducible protocol for measuring this allocation problem on simplex-valued predictions; it compares existing conformal wrappers rather than proposing a new one. Its task suite, SimplexTasks-12, combines six controlled synthetic regimes with six frozen-predictor real tasks spanning class probabilities, topic mixtures, spectral abundances, cell-type fractions, age distributions, and emotion mixtures. Each comparison fixes the predictor, score, and response-free stratification map, varies only the wrapper, and reports marginal coverage, worst-stratum coverage, max disparity, and within-task radius and compute. Global calibration can look valid while failing badly: on CIFAR-10 it attains 0.900 marginal coverage but only 0.542 in the worst entropy stratum, and Mondrian calibration raises that stratum to 0.886 while reducing max disparity from 0.358 to 0.022. No wrapper dominates, however. Under smooth synthetic heterogeneity, several repairs are competitive; fixed-map analyses show that rankings depend on the evaluation groups and protocol; and in a 12-task comparison, Mondrian has lower disparity on its single target partition for all 12 tasks, whereas BatchMVP has lower disparity over overlapping groups on five. These are empirical comparisons, not new coverage guarantees. A controlled predictor-bias sweep shows that removing predictor bias only partly reduces global-threshold disparity. We release task cards, result provenance, permitted derived arrays, and rebuild instructions, and treat wrapper selection as a diagnostic comparison rather than a universal ranking.

---


### 85. [Ontology-Based Contextual AI Evaluations (OB-CAIE) Methodology](https://arxiv.org/abs/2610.00529)

**<font color=#1a73e8>作者：</font>** Julie Krugler Hollek, Michael Zargham, Mala Kumar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The ontology-based contextual AI evaluation (OB-CAIE) methodology was developed to address a lack of scientific rigor that arises from unclear testing coverage, to balance human expertise and automations, and to address a lack of reproducibility of AI evaluation testing environments. OB-CAIE strengthens the current state of AI evaluations by addressing the first step in the scientific method by clearly defining what will be tested. Two ontologies represent the tractable problem space in the OB-CAIE methodology: the Domain-Specific Ontology (DSO) and the Evaluation Process Ontology (EPO). The DSO is the what; the EPO is the how. An OB-CAIE problem space can be used for one or multiple AI evaluations. The OB-CAIE methodology allows for human judgment at specific points, in scientifically grounded ways, and in complex subject areas where human feedback is genuinely irreducible or machine irreplaceable. A key advantage of the OB-CAIE methodology is that failure points can be traced, visualized and analyzed within the canonical OB-CAIE methodology problem space.

---


### 86. [Memorizon: Training World Models Beyond Their Context Window](https://arxiv.org/abs/2610.00544)

**<font color=#1a73e8>作者：</font>** Tingting Liao, Xuezhi Liang, Hao Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming world models should render a place consistently across repeated visits. Directly supervising such revisits requires training samples that capture both visits, often spanning minutes. Yet dense attention over the full span incurs quadratic costs, making long-span supervision expensive. Memorizon breaks this coupling: long spans are needed for supervision, but not for attention, since the two visits can share a forward pass without including every intervening frame. A training sample covers a span of any length but is scored only on its last $k$ chunks. Instead of tokenizing the history before them, each scored chunk retrieves its own top-$K$ latents by camera co-visibility, and the union of these requests forms a shared bank. The bank is bounded by $kK$, so the sequence stays bounded however long the span; at the shortest span the recipe is exactly conventional training. Adding the bank raises the cost of a step once; beyond that, a longer span costs little, and going from 100 to 400 s adds 12% to the step time. Against a sliding-window baseline, retrieval raises revisit consistency on every split, and a span long enough to reach the first visit of each return adds a further 24% to 30%, at some cost in image quality; beyond that span, more length no longer helps. Filling the bank from another episode lowers revisit correlation by 83%, so the model uses what it retrieves. Project page: this https URL

---


### 87. [Geometry-Dependent Bounds for Online Non-Monotone DR-Submodular Maximization](https://arxiv.org/abs/2610.00545)

**<font color=#1a73e8>作者：</font>** Vaneet Aggarwal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study adversarial online maximization of nonnegative, non-monotone DR-submodular functions over compact convex down-closed sets. A learner commits each action before observing its objective and competes with the best fixed action in hindsight. We prove a comparator-uniform first-order inequality that gives coefficient $4/9$, improving the online $0.401$ benchmark, with one gradient query and one projection per round and $O(\sqrt T)$ expected approximate regret. If $\zeta {\bf 1} \in K\subseteq[0,1]^d$, the coefficient improves to $\underline\alpha(\zeta)=\tfrac12-(1-2\zeta)_+^2/[2(3-2\zeta)^2]$. The proof is a direct ordered-coordinate argument with an objective-independent rational action. Conversely, a three-group symmetry-gap construction yields an offline oracle upper bound $\beta_*=0.470438681380894\ldots$ at $\zeta=0$, even with exact value and full-gradient responses. A parameterized extension and exact finite-instance bounds define an upper function for every $\zeta$. The lower and upper bounds match at $1/2$ for $\zeta\ge1/2$, and show that the optimal deficit from $1/2$ is $\Theta((1/2-\zeta)^2)$ as $\zeta\uparrow1/2$. For coefficient-revealed polynomials we obtain $1/2$ for quadratics and a geometry-dependent cubic coefficient starting at $8/17$, including $0.49$ at $\zeta=1/5$. A constant objective sequence yields an offline $(4/9-\varepsilon)$ approximation with polynomially many first-order queries on the cube and projections, without requiring a supplied positive lower bound on the optimum. We also give nonanticipating adaptive-adversary and value-feedback guarantees, including $O(T^{3/4})$ regret with one noisy value per round.

---


### 88. [Evaluating Hybrid Quantum-Classical Models for Reduced-Order Brain Deformation Dynamics](https://arxiv.org/abs/2610.00554)

**<font color=#1a73e8>作者：</font>** Tao Liu, Ge He, Dongyu Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We evaluate hybrid quantum-classical machine learning for the reduced-order prediction of spatiotemporal brain deformation fields. To mitigate the computational intractability of high-dimensional displacement fields, we employ Proper Orthogonal Decomposition (POD) to project the data into a compact latent space. Within this framework, we formulate two distinct learning objectives: static temporal-to-latent regression and autoregressive latent state forecasting. We systematically benchmark compact classical baselines against both minimal and enhanced hybrid quantum architectures. Our results demonstrate that classical networks provide the strongest baselines in the present setting. For static regression, a classical POD-MLP outperforms all evaluated quantum variants, although an enhanced Variational Quantum Circuit (VQC) substantially improves upon a minimal VQC baseline. For temporal forecasting, a classical POD-LSTM delivers superior predictive accuracy and statistical robustness compared to an enhanced Quantum LSTM (QLSTM) across varying history windows and random initializations. Overall, this study establishes reduced-order physical field learning as a rigorous testbed for near-term QML, highlighting that while hybrid enhancements successfully recover expressivity in weak quantum circuits, classical architectures retain a definitive advantage in both fidelity and stability.

---


### 89. [Beyond Affine Transformations: A Soft Dominance Layer for Coordinate-Wise Neural Computation](https://arxiv.org/abs/2610.00563)

**<font color=#1a73e8>作者：</font>** Mariano Rivera  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents a preliminary study of an alternative to the affine transformation underlying conventional neural-network layers. In the proposed Soft Dominance Layer, each output unit compares input coordinates with a learnable reference vector and aggregates smooth inequality responses. A sigmoid relaxation makes the comparisons differentiable, while a sharpness parameter $\alpha$ controls their transition toward hard threshold decisions. The aim is to examine the trainability and direct threshold interpretation of this primitive, not to claim a replacement for affine layers. In single-run MNIST experiments, the highest observed Soft Dominance accuracy is $0.9061$ without annealing and $0.9173$ with annealing, compared with $0.9827$ for the MLP baseline. These descriptive results do not establish reliable configuration rankings or a statistically supported annealing benefit. Learned reference vectors exhibit spatial structure, providing qualitative evidence of structured learning. Repeated-seed experiments and broader datasets are required to assess robustness and practical relevance beyond this proof of concept.

---


### 90. [Attention Kernels for Learning Maps Between Heavy-Tailed Measures](https://arxiv.org/abs/2610.00564)

**<font color=#1a73e8>作者：</font>** Kailen Hargenrader, Edoardo Calvello, Bohan Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Operator learning on probability measures can be accomplished with transformers. For measures with polynomial tails, the exponential weighting in softmax can make the corresponding measure-level attention integrals diverge. This motivates replacing the exponential with slower-growing functions. We construct two benchmarks for operator learning on measures with closed-form targets. We use these benchmarks to study attention kernel growth and data transformation in post-norm transformers. Without data transformation, the softmax models exhibit ensemble collapse on both heavy-tailed benchmarks, while the three slower-growing kernels avoid collapse. Symlog preprocessing allows softmax to avoid collapse on the matrix inverse task but not on the sheared swap task. On the Gaussian control, all four kernels perform similarly. We also examine how sample size affects the sensitivity of empirical energy and Wasserstein distances to tail differences. These results support slower-growing attention kernels as an effective design choice for post-norm transformers learning from heavy-tailed ensembles.

---


### 91. [From Task Mixtures to Specialized Experts](https://arxiv.org/abs/2610.00580)

**<font color=#1a73e8>作者：</font>** Hojat Allah Salehi, Mehrdad Mahdavi, Andrew Arash Mahyari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In collaborative foundation model fine-tuning, client data is rarely homogeneous. Instead, clients typically possess unknown mixtures of distinct data distributions, or tasks. Conventional federated learning primarily addresses heterogeneity across clients without explicitly resolving latent task mixtures within each client. We study this setting as compound heterogeneity, where data is heterogeneous both across and within clients. We study adaptation over a common frozen representation and show that, when tasks share the same feature geometry, the optimal model for a client's task mixture under squared loss is a convex combination of the optimal models for its underlying tasks. Thus, a single locally trained model represents the client's overall task mixture, while individual inputs may be drawn from different underlying task distributions. This motivates routing inputs to specialized experts, and we show that, when the task optima form a simplex, task-aligned routing achieves lower risk than any single adapted model for genuinely mixed clients. With access to a small set of task-labeled public samples, we derive a convex program to recover task experts and match them to their corresponding tasks. Our routing analysis shows that effective specialization requires input-dependent expert selection aligned with each client's task mixture. Motivated by this analysis, we propose FedSEE. Across our experiments, FedSEE avoids the negative transfer observed in the evaluated baselines and improves performance by 2.9 points overall and 3.7 points for the worst-served quartile.

---


### 92. [Worse Together: How Performance Breaks Down in Multi-User Multi-Agent Teams](https://arxiv.org/abs/2610.00583)

**<font color=#1a73e8>作者：</font>** Sahan Paliskara, Nattaput Namchittai, Andrew Lampinen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> People are increasingly delegating tasks to AI agents, and those agents are increasingly encountering other people's agents over shared resources such as a codebase, a calendar, or a budget. When each agent acts for a different user with different goals, coordination often fails, and the group ends up worse off than if a single agent had acted for everyone. We study this multi-user, multi-agent setting across five frontier models and 77 scenarios in four environments: an API key environment in which agents share a compute budget, a clinic in which they share a calendar, a personal assistant environment in which they share a group order or booking, and a merge queue in which they share a release cutoff. In each scenario, we compare a single agent that serves every user (a coordinator) to a team in which each agent serves one user, with and without a communication channel between the agents. Teams deliver worse group outcomes than the coordinator in every environment: without a channel, they completely collapse in two environments, and even with one, coordination overhead creates substantial gaps. For example, in the personal assistant environment, the coordinator fulfills a targeted user request about twice as often as teams. We identify distinct behaviors associated with this poor group-level performance, including stalling as teams grow, overriding each other's actions, and fabricating claims. We find effective but environment-specific mitigations, such as a team lead, explicit procedural instructions, and a platform check that makes an agent read its peers' messages before committing. We will release the API key, clinic, and personal assistant environments as MAMUBench, comprising 74 scenarios for evaluating multi-user, multi-agent coordination.

---


### 93. [Right In-Place (RiP) Convolution: A Simple, General, and Near-Optimal Strategy for Memory-Efficient CNN Inference](https://arxiv.org/abs/2610.00586)

**<font color=#1a73e8>作者：</font>** Opegbemi Matthias Busoye, Tolulope Matthew Busoye, Eghonghon-aye Eigbe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation memory, not compute, limits CNN inference on constrained hardware such as microcontrollers. Direct in-place convolution removes the dual-buffer cost, but the memory-optimal formulation of Gural and Murmann assumes valid padding, unit stride, unit dilation, and odd square kernels, and needs a non-sequential traversal costing $2\times$ inference time in transposes. We identify two regimes in which their published closed form does not hold: (1) an under-allocation of exactly $(k-1)C_{in} \bmod (C_{out}-C_{in})$ scalars, active on every convolutional layer of their own deployed network and manifesting as a silent corruption of still-live input; (2) an unbounded overestimate, up to $2{,}432\times$, once the critical leg leaves the output grid. We correct both and generalize to arbitrary stride, dilation, padding, and rectangular kernels. We then propose Right In-Place (RiP) convolution, a bit-identical operation in which every layer reads its input right-aligned in a shared workspace and writes its output left-aligned from index zero. The debt is piecewise affine in the output pixel index, so evaluating its breakpoints in $O(1)$ yields the minimum safe gap without enumerating the output grid, with row-major access preserved. Across $10{,}000$ random layers RiP produced no corruption, and across 84 convolutional layers from 25 architectures it matches the herringbone workspace exactly on 58 and within 5% on 81, using 24.8% less memory than dual buffering on average. Written into TinyEngine's kernels and deployed to a Raspberry Pi Pico 1 and Pico 2, it cuts peak activation memory across eleven MCUNet models by 12.5 to 33.3% at unchanged cycle counts and bit-identical outputs, raising the number of models that fit the Pico 1's 256 KB SRAM from six to nine.

---


### 94. [ALER: Adaptive Learnable Experience Rewriting for Reinforcement Learning](https://arxiv.org/abs/2610.00592)

**<font color=#1a73e8>作者：</font>** Oleg Shchendrigin, Egor Cherepanov, Aleksandr I. Panov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In partially observable reinforcement learning (RL), a later observation can make stored information obsolete or change what it implies for the next decision. Memory architectures and benchmarks for RL mostly test retention, the ability to keep information unchanged until it is needed. We formalize two further requirements. Rewriting sets the decision-relevant content to a value independent of the old one, and experience fusion transforms the old content by a rule that a later observation specifies. For tasks built from such updates, we count the memory states that a solution needs, and several baselines reach their lowest success rates on compositions that need more states. We introduce ALER (Adaptive Learnable Experience Rewriting), an agent that pairs an LSTM with a slot memory. An independently addressed Gumbel-Softmax write that concentrates its weight on one slot overwrites that slot, and a learned gate fuses the retrieved content with the recurrent state before the policy and value heads. We also introduce Rune-Mazes, three environments in which rune observations invert, cancel, reset, or repeat updates of a hidden cue under vector and pixel observations. Against seven baselines, ALER reaches a success rate of at least $0.82$ in all sixteen Endless T-Maze configurations and at least $0.99$ on all five Rune T-Maze compositions, and it has the highest mean success rate on four-branch Rune Multi-Corridor with an Invert rune. On pixel-based Rune MiniGrid Memory, it has a higher mean success rate than PPO-LSTM in eight of ten configurations. Project page: this https URL.

---


### 95. [Just Align $\bm{x}$: Aligning Predictions, Not Representations](https://arxiv.org/abs/2610.00600)

**<font color=#1a73e8>作者：</font>** Yuyao Zhang, Yuwei Hu, Ziyang Mai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Representation alignment has become an effective way to accelerate diffusion training, but its benefits do not transfer reliably to pixel-space clean-image prediction. In JiT, we find that auxiliary feature alignment can improve access to semantic features while reducing access to image variation needed for clean-image prediction, creating a mismatch between the auxiliary objective and the denoising task. This suggests a different principle: auxiliary supervision should improve the prediction target itself rather than impose a separate representation target. We introduce JAx (Just Align x), a prediction-supervision method that aligns clean-image predictions across noise levels. JAx couples a noisier student observation with a cleaner observation through a Markov degradation that preserves the original JiT input distribution. Under this coupling, the oracle prediction from the cleaner state has the same conditional mean as the optimal JiT target, while its conditional target covariance is no greater. Thus, oracle prediction alignment preserves the population JiT objective up to a constant while providing a lower-variance training target. To make this construction practical with an imperfect EMA teacher, JAx combines ground-truth supervision with a reliability-gated coupling band that selects nearby teacher states based on prediction risk. On ImageNet 256x256, JAx consistently improves FID and accelerates convergence across JiT-B/16, L/16, and H/16, without an external encoder or changes to the architecture or sampling procedure. Gradient diagnostics further show reduced minibatch gradient variance, while ablations demonstrate that the gains cannot be explained by time reweighting alone. These results show that prediction-space supervision provides a simple and principled alternative to representation alignment for pixel-space generative models.

---


### 96. [Learning the identity: a case study of how SGD selects among functional decompositions](https://arxiv.org/abs/2610.00615)

**<font color=#1a73e8>作者：</font>** Andy Arditi, Weian Xie, David Bau 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> One might think that learning the identity function with a deep linear residual network is trivial - the path along residual connections already implements the identity, and so the network need only drive its weights to zero. However, this zero-weight solution is just one point on an entire manifold of population-loss minimizers, each corresponding to a different decomposition of the identity across the network's layers. Although the population loss does not distinguish among these solutions, stochastic gradient descent (SGD) reproducibly favors particular ones. For instance, under anisotropic label noise, the learned layers exhibit a noise-dependent spectrum; even with weight decay, SGD does not generally recover the zero-weight solution. Changing only the parametrization, while leaving the set of realizable functions unchanged, yields different behavior: factoring each weight matrix as a product of two matrices causes the weights to collapse to zero, even without explicit weight decay.
While perhaps mysterious and unintuitive at first, these phenomena can be understood through the lens of entropic loss, which augments the population loss with a term proportional to the expected squared norm of the minibatch gradient (Ziyin et al., 2025). On the identity manifold, the population loss is constant, while the entropic term distinguishes among these decompositions. We characterize its minimizers analytically and use them to derive predictions for the structure of solutions favored by SGD. Networks trained with SGD closely match these predictions.
Overall, the identity learning task studied here serves as a clean and simple case study of how the lens of entropic loss can clarify why SGD favors particular decompositions of the same input-output function.

---


### 97. [Misalignment of Low-Loss Regions Causes Grokking](https://arxiv.org/abs/2610.00620)

**<font color=#1a73e8>作者：</font>** Yongding Tian, Zaid Al-Ars, Maksim Kitsak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Grokking refers to the delayed emergence of validation-set generalization after a model has already overfit the training set. Although first observed in small algorithmic tasks trained with transformers, its underlying mechanism remains unsettled. In this work, we develop an analysis framework based on mode connectivity and the geometry of low-loss regions. The framework predicts that the standard modular-arithmetic setting does not always produce grokking: under a symmetry-preserving train/validation split, we observe a stable anti-grokking case in which validation performance does not recover. This counterexample challenges several existing correlational explanations of grokking. More broadly, our analysis framework and results further suggest that grokking arises when the low-loss regions induced by the training and validation partitions are misaligned. Once these regions become well aligned, training hyperparameters alone cannot produce grokking and the observed dynamics collapse to either trainable or non-trainable behavior.

---


### 98. [Mixture of Decoders for Diverse Dialog Response Generation](https://arxiv.org/abs/2610.00621)

**<font color=#1a73e8>作者：</font>** Wenchao Du  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mixture modeling is a long established machine learning technique for learning large sets of multi-modal data. While it is known that sequence-to-sequence models for dialog response generation suffer from the problem of low diversity, we hypothesize that it is because sequence-to-sequence models tend to learn a degenerate uni-modal distribution of responses. We then propose to incorporate a mixture of decoders into sequence-to-sequence models and try to make each decoder learn specialized topics in order to improve the diversity of generated responses. Our model is developed under the framework of conditional variational autoencoder (CVAE). We evaluate our approach on an open domain chat corpus and show improvement over strong baselines in quantitative measures and human evaluation.

---


### 99. [Preliminary Evaluation of Transition-Aware Controller Locomotion Adaptations for Supporting Postural Stability in VR](https://arxiv.org/abs/2610.00628)

**<font color=#1a73e8>作者：</font>** Ramisa Fariha Joyee, M. Rasel Mahmud  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present three locomotion adaptation approaches: Motion Acceleration, Turn Acceleration, and Motion Deceleration to improve postural stability during body-state transitions in virtual reality (VR). The system detects standing-to-walking, turning, and walking-to-stopping transitions and applies adaptive locomotion smoothing. Motion Acceleration gradually increases locomotion speed when users begin walking, Turn Acceleration smooths rotation while turning, and Motion Deceleration gradually reduces movement speed before stopping. We evaluated these techniques in a virtual navigation task using objective and subjective balance measures. Preliminary results show reduced center of pressure (COP) velocity and improved balance confidence. These findings suggest that locomotion adaptations can improve balance and navigation experience.

---


### 100. [Learning Linear Systems under Heavy-Tailed Noise: A Non-Asymptotic Analysis from A Single Trajectory](https://arxiv.org/abs/2610.00637)

**<font color=#1a73e8>作者：</font>** Xiaomian Yang, Sungho Shin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We establish non-asymptotic sample complexity bounds for the least-squares estimation of vector autoregressive models for exponentially stable systems with heavy-tailed noise based on a single observed trajectory. By assuming i.i.d. noise, bounded noise covariance, and persistent excitation, we show that the estimation error is $\widetilde{\mathcal{O}}(r^{1/2}T^{-1/2+1/p})$ under bounded $p$th moment for $p > 2$, where $T$ is the number of samples, $r$ is the noise dimension, and $\widetilde{\mathcal{O}}(\cdot)$ hides logarithmic terms. We also introduce a unifying approach to sample complexity analysis applicable to broad classes of noise distributions and showcase this by deriving error bounds for sub-exponential and sub-Gaussian noise distributions. Finally, we specialize our analysis to autoregressive models with exogenous inputs and show that the dimension factor of the error bound is independent of the model order.

---


> [!TIP]
> 当前位于：**51-100**（第 2/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-385](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
