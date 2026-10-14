# 📦 其他研究 | 2026年10月15日

> 本类共 **810** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 301. [Hyperbolic Time Series Forecasting with Learnable Decomposition and Manifold Dynamics](https://arxiv.org/abs/2610.15760)

**<font color=#1a73e8>作者：</font>** Sarang Rajendra Patil, Vishal Fenn, Mengjia Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multiscale structure is central to time series forecasting: temporal signals contain slowly varying trends, intermediate seasonal patterns, and high-frequency residuals. Traditional forecasters model this multiscale structure in Euclidean space, without representing the ordering it induces among components. We identify that cascaded decomposition orders components by their characteristic frequencies, forming a natural frequency hierarchy. This hierarchy aligns with the exponential volume growth of hyperbolic space, which provides increasing representational capacity with radius and naturally accommodates nested hierarchies. We propose HyperForecast, the first long-term time series forecasting (LTSF) framework operating in hyperbolic space. HyperForecast embeds decomposed temporal segments on the Poincaré ball where radial distance captures this nested structure, from low-frequency components near the origin to high-frequency components near the boundary. We model geodesic velocity through two manifold-dynamics variants: (a) autoregressive forecasting via Poincaré residual dynamics, and (b) non-autoregressive forecasting that predicts all future segments in parallel. HyperForecast consistently outperforms existing and state-of-the-art baselines on 9 of 11 long-term forecasting benchmarks, achieving up to 58% lower mean squared error at long horizons. Further analysis reveals that the learned radial embeddings recover the frequency hierarchy and that hyperbolic geometry contributes substantially to forecasting performance.

---


### 302. [SlotAVS: Object-Centric Audio-Visual Segmentation via Bi-Modal Slot Attention](https://arxiv.org/abs/2610.15764)

**<font color=#1a73e8>作者：</font>** Arnav Sharma, Anand Mishra, Renu Rameshan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-Visual Segmentation (AVS) requires predicting pixel-wise masks of sounding objects by grounding acoustic signals in visual space. In multi-source scenes, concurrent sound sources often remain entangled within shared visual representations, leading to merged masks or unstable specialization when using standard alignment-focused transformer architectures. To address this, we present SlotAVS, an object-centric framework driven by competitive bi-modal slot attention. While robust foundation models provide rich semantic priors, SlotAVS shifts the paradigm from global cross-modal fusion to explicit competitive binding. By initializing discrete object slots from temporal audio sequences and enforcing strict slot-wise competition over spatial visual tokens, our method structurally mitigates the blending of distinct acoustic entities. Further, to stabilize instance-level learning, we introduce a Hungarian matching strategy that optimally aligns slots with ground-truth objects using spatial and boundary overlap. Coupled with a numerically stable, confidence-aware mask fusion mechanism, SlotAVS robustly aggregates multi-source predictions. Extensive experiments on the AVSBench dataset demonstrate the efficacy of our approach, achieving 88.6% mIoU on the Single-Source (S4) split and 71.7% mIoU on the Multi-Source (MS3) split. These results show that explicit competitive binding is critical for complex audio-visual scene understanding and effectively leveraging foundation-model priors without relying solely on their capacity.

---


### 303. [Data-Centric Recursive Self-Improvement for Navigation via Policy-Synchronized Language-Action Dual Bootstrapping](https://arxiv.org/abs/2610.15782)

**<font color=#1a73e8>作者：</font>** Songze Li, Haoming Gu, Ziyang Gong 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language navigation requires agents to follow natural-language instructions to reach target locations, making high-quality language supervision essential. Since human annotation is costly, prior work has explored scalable data synthesis methods. However, existing methods typically either use separate models for navigation and instruction generation or couple the two tasks through task-specific components; most also annotate the full trajectory corpus with a fixed model before updating, which can cause generated supervision to lag behind the evolving policy. Therefore, we introduce RSI-Nav, a data-centric recursive self-improvement framework for navigation via policy-synchronized language-action dual bootstrapping, which unifies vision-language-to-action instruction following and vision-action-to-language instruction generation within a shared model. Specifically, after supervised fine-tuning establishes fundamental capabilities, RSI-Nav progressively processes unlabeled trajectories in small shards. The current model generates instructions for these trajectories, executes them to evaluate goal completion and path efficiency, retains qualified samples, and immediately updates itself before processing the next shard. This shard-wise update keeps newly generated supervision aligned with the evolving policy. We also incorporate spatial understanding data, since stronger spatial reasoning benefits navigation. Extensive experiments show that RSI-Nav reaches 68.6% SR on R2R-CE and 72.4% SR on RxR-CE, while providing stronger instruction-generation utility and modestly improved spatial understanding after recursive evolution.

---


### 304. [An Explainable System for Offensive Content Detection in Nastaliq Urdu: Corpus Curation, Transformer Benchmarking, and Word-Level Attribution](https://arxiv.org/abs/2610.15795)

**<font color=#1a73e8>作者：</font>** Muhammad Shahid Iqbal Malik  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated moderation systems are deployed at scale, yet they remain opaque to the users and moderators affected by their decisions, and their coverage is almost entirely confined to English. For Urdu written in the Nastaliq script, no such system exists, and the annotated resources it would be built on are drawn largely from Twitter/X, where character limits constrain how users write. Interpretability has received little attention, leaving it unclear what such models actually learn. This study addresses these gaps in three steps. First, we curate and publicly release a corpus of 7604 Nastaliq Urdu Facebook comments, extending an earlier corpus by correcting text-level inconsistencies and re-examining the original labels. Second, we fine-tune four Urdu-capable transformers under a common grid-search protocol and compare them against twelve feature-classifier baselines on identical data partitions. The best configuration, Multilingual Representations for Indian Languages (MuRIL), reaches 87.05% accuracy and 87.06% macro F1, improving on the strongest baseline by 5.52 percentage points, a margin that exceeds the 95% confidence interval on test accuracy; the two leading transformers differ by less than the test set can resolve, and performance is stable across five optimizers. Third, we compute word-level SHAP attributions adapted to right-to-left rendering. Attribution mass concentrates on high-frequency slurs but extends to syntactically neutral function words and to political vocabulary characteristic of the source pages, indicating that aggregate performance may rest partly on lexical and topical regularities rather than a generalizable representation of offensiveness.

---


### 305. [Passing Tests, Missing Semantics: Evidence of Interpretive Lock-In in Plan-Based DataFrame Code Generation](https://arxiv.org/abs/2610.15797)

**<font color=#1a73e8>作者：</font>** Jingjing, Dishu Yang, Hongbo Qin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Planning and revision are intended to bring generated code closer to the task specification. Yet a mistaken interpretation can persist across the plan, implementation, and tests - a pattern we call interpretive lock-in. We investigate this risk on 30 DataFrame tasks derived from TPC Benchmark DS, comparing Frozen One-Pass, Test-Guided Revision, and PlanAudit-Guided Revision. Test-pass counts rose from 22/30 to 29/30 and 30/30, yet no generated solution matched its stored reference output. Evaluator controls returned the expected outcome in 57/57 cases. Same-engine SQL re-execution reproduced 28/30 references; all 77 test-passing runs on these tasks still failed reference agreement. PlanAudit-Guided Revision improved code scores on 3/30 tasks and test coverage on 11/30, but the median paired change was zero for both measures. Failure analysis revealed tests that omitted requirements, adopted candidate-defined schemas, used nondiscriminating fixtures, or repeated the implementation's incorrect logic. Fresh generation on ten targeted tasks produced 0/30 reference matches and 25/25 false passes among test-passing runs. These findings are diagnostic rather than causal: the pipelines differ in feedback, grounding, call budgets, and editing permissions, and the study uses one model and one primary generation per eligible task. Because pre-adjudication human labels were not retained, inter-rater agreement cannot be reconstructed and the mechanism analyses remain exploratory. Overall, increasingly successful self-generated tests did not establish semantic correctness, even after excluding unreproduced references.

---


### 306. [FreeBrush: Motor Signals-Based Toothbrushing Monitoring System for Electric Toothbrushes](https://arxiv.org/abs/2610.15800)

**<font color=#1a73e8>作者：</font>** Pinhao Lin, Xuanyu Liu, Guoheng Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Oral health is vital for overall well-being, yet many users brush different tooth surfaces for insufficient or excessive durations. Toothbrushing monitoring systems can help improve brushing habits by reminding users of under-brushed and over-brushed surfaces, but existing approaches often rely on external sensors, increasing cost and reducing practicality. We observe that the intrinsic motor signals of electric toothbrushes can reflect the brushing surfaces and durations. When brushing different tooth surfaces, the brush head experiences different constraints from the surrounding oral cavity, changing the motor's driving currents and position feedback. Based on this observation, we propose FreeBrush, a toothbrushing monitoring system that uses the intrinsic motor signals of electric toothbrushes to recognize brushed tooth surfaces and estimate brushing durations without any external sensors. We prototype the system on a commercial off-the-shelf electric toothbrush and conduct a comprehensive evaluation with 18 participants. FreeBrush achieves 92.8% accuracy for 16-surface recognition and 92.0% accuracy for brushing duration estimation. The system further shows robustness across different toothpastes, brush heads, vibration modes, usage scenarios, and long-term use, and is capable of running on edge devices. By recognizing brushed tooth surfaces and estimating the brushing duration, FreeBrush can help users identify under-brushed and over-brushed surfaces and build balanced brushing habits.

---


### 307. [Reference-Efficient Multimodal Bitstream-Corrupted Video Recovery via Depth-Conditioned Adaptation](https://arxiv.org/abs/2610.15806)

**<font color=#1a73e8>作者：</font>** Tianyi Liu, Jiaojiao Wang, Ye Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering visually faithful content from damaged video bitstreams is important for reliable multimedia communication and storage. Existing methods exploit local residuals and non-local RGB references of the input video sequence, but both sources can become unreliable after decoding, while processing additional references increases receiver computation and memory. This paper studies multimodal bitstream-corrupted video recovery (MBSCVR) using RGB and depth information, where pre-transmission depth-based geometry aids reconstruction when the received appearance is corrupted. We propose a novel MBSCVR framework that selects and effectively utilizes a single selected non-local RGB reference per recovery window to achieve higher performance. It integrates a reliability-aware multimodal selector that combines valid appearance with depth compatibility before reference encoding. Depth-Conditioned Reference Adaptation (DCRA) introduces selected RGB evidence into feature completion and content generation, while frame-aligned depth conditions completion queries. On the complete BSCV benchmark with oracle masks, MBSCVR uses one selected reference to achieve 32.30 dB on YouTube-VOS and 28.93 dB on DAVIS, surpassing full-reference B2SCVR by 0.27 and 0.33 dB and improving SSIM on both subsets. Matched receiver-forward measurements show 36.8\% lower latency and 40.8\% lower peak memory. These results demonstrate how compact geometric guidance and adapted appearance processing improve the quality--resource trade-off of multimedia recovery.

---


### 308. [Totem: Object-Centric 3D Memory for World-Consistent Video Generation](https://arxiv.org/abs/2610.15807)

**<font color=#1a73e8>作者：</font>** Zichen Wan, Tianyu Huang, Fan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating coherent videos grounded in a unified underlying world remains a major challenge, particularly under large viewpoint changes, where existing methods often struggle to maintain stable representations of individual objects. To this end, we introduce Totem, an object-centric 3D memory framework for world-consistent video generation. Totem first represents each selected object as a persistent 3D memory aligned to a shared world frame, assigning it a dedicated state. Based on these memories, we design a dual-stream 3D conditioning architecture that combines object memories with scene geometry for target-view synthesis. Moreover, these object memories constrain the model's attention with 3D structural information, thereby preserving object surfaces and relative spatial layouts. Extensive experiments on world-generation and object-centric benchmarks demonstrate that Totem generates videos depicting a more object-consistent 3D world under challenging camera trajectories, while supporting versatile applications.

---


### 309. [ChangeT$^3$: Evaluating Vision Test-Time Training for Remote Sensing Change Detection](https://arxiv.org/abs/2610.15813)

**<font color=#1a73e8>作者：</font>** Sharukshan Niranjan, Oshadha Samarakoon, Nichula Wasalathilaka 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bitemporal remote sensing change detection requires representations that preserve spatial detail while capturing contextual information relevant to changes between acquisitions. Visual test-time training offers an alternative to explicit token-to-token attention by adapting a compact inner model to each image. This letter describes ChangeT$^3$, a vanilla Siamese configuration combining the existing hierarchical ViT$^3$-Tiny encoder with the multiscale ChangeFormer decoder. The two image streams share learned encoder parameters, while their fast weights are computed independently from their respective spatial features. Each encoder block retains the inherited global simplified SwiGLU and local adaptive depthwise-convolution branches. Temporal comparison is performed by the decoder through learned fusion of paired features at four resolutions, followed by coarse-to-fine aggregation and binary prediction. This separation provides a direct setting for examining image-conditioned inner updates without introducing an additional temporal interaction module. Trained from scratch on LEVIR-CD+ with the same decoder, recipe, and budget as a ChangeFormer control, ChangeT$^3$ reaches an F1 of 80.61$\pm$0.90 against 78.84$\pm$0.21 for ChangeFormer (three seeds each); as in the standard protocol for this dataset, checkpoints are selected on the test split. Trained with both inner updates disabled, the same encoder reaches 78.63$\pm$0.20. Neither model transfers zero-shot to SYSU-CD, DSIFN-CD, or WHU-CD, and ChangeT$^3$ is the slower of the two at small inputs despite similar parameter and operation counts.

---


### 310. [ML-CLAPPS: A Probabilistic Framework for Imbalanced Multilabel Learning under Class Prioritization](https://arxiv.org/abs/2610.15816)

**<font color=#1a73e8>作者：</font>** Priel Hazan, Nir Almog, Noam Keidar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world datasets often exhibit severe class imbalance, degrading the performance of deep learning models, particularly on rare classes. While imbalance is well studied in binary and multiclass settings, it is substantially more challenging in multilabel problems due to complex label co-occurrence. In clinical applications such as ECG classification, this challenge is coupled with a second critical challenge: the need to prioritize high-risk conditions, regardless of their prevalence, to mitigate the high cost of false negatives. We introduce the Multilabel Class-Prioritized Probabilistic Sampler (ML-CLAPPS), a learnable sampler that optimizes a distribution over training instances to control the model's exposure to different classes. This approach addresses multilabel imbalance while enabling prioritization of significant conditions via a user-defined importance vector (IV). Empirical evaluation on a real-world multilabel ECG image dataset demonstrates that ML-CLAPPS achieves state-of-the-art performance. We show that it aligns class exposure with the specified IV, and that increasing a class's importance leads to corresponding improvements in its classification performance, enabling explicit prioritization of clinically critical conditions.

---


### 311. [Benchmarking Deep Learning Models for Anomaly Detection in Real-World Cloud Telemetry](https://arxiv.org/abs/2610.15818)

**<font color=#1a73e8>作者：</font>** Sumit Dhyani, Sougata Mukherjea  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern cloud platforms generate high-dimensional, noisy telemetry from thousands of microservices. Unlike classical anomaly detection benchmarks, cloud anomalies are short-lived, irregular, and largely non-periodic, making timely detection challenging. We present an empirical benchmark of deep learning models for anomaly detection using a real-world IBM Cloud Console dataset. We evaluate GRU, Transformer, TimesNet, and Autoformer architectures using the Numenta Anomaly Benchmark (NAB), a timing-aware metric that accounts for early detection and false alarms. TimesNet achieves the highest NAB scores due to strong early-detection sensitivity. Transformer models also detect anomalies early but incur higher false-positive rates. An improved GRU autoencoder, incorporating robust scoring and persistence rules, achieves competitive performance with a more stable false-alarm profile. Overall, the modest performance differences suggest that real cloud anomalies are dominated by short-term deviations rather than persistent periodic structure, emphasizing the importance of timing-aware evaluation and robust post-processing.

---


### 312. [Guarded Block Transfers for Polytope Distance: Linear Convergence with Explicit Constants and Gap-Certified Screening for SVM Training](https://arxiv.org/abs/2610.15829)

**<font color=#1a73e8>作者：</font>** Mayank Gupta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hard-margin SVM training is the distance problem between two convex hulls, which the Triangle Algorithm (TA) solves with a certified duality gap. We propose \emph{guarded block transfers}: $k$ Mitchell--Demyanov--Malozemov (MDM) transfers per scan are aggregated into one exact line search, guarded by a comparison with the single best transfer at a cost independent of the number of points $n$, and replaced by an away step when the leading transfer is capacity-clipped. On the Minkowski-difference polytope, where the objective is $1$-strongly convex, we prove global linear convergence with explicit constants and no combinatorial swap-step bounds; the per-step contraction is $k$-independent and only the drop-count bound grows with $k$, so aggregation is provably safe while the saving in scans is measured, not proved. Since the TA certificate is the Frank--Wolfe gap divided by the current distance, gap-safe screening applies, and we bound the iteration after which it has removed every zero-weight point off the optimal faces by $O\!\left(\tfrac{k}{\rho}\log\tfrac{1}{\tau}\right)$ up to logarithmic factors in the geometry, $\rho$ the rate constant and $\tau$ the optimal-face margin. On five LIBSVM benchmarks, with fairer baselines than our submission, the solver matches the baselines to four or five digits wherever both converge, ties LIBSVM on sparse-support hard margins and beats our blended pairwise conditional gradients (BPCG). But our full-cache sequential minimal optimisation (SMO) code ties or beats it on kernel $L_2$ margins, LIBLINEAR's dual solver is up to $4.5\times$ faster on the separable $L_2$ margin, and our solver is one to three orders of magnitude slower than LIBLINEAR's Newton solver on dense-support $L_2$ margins and than LIBSVM on a nearly touching kernel hull. Its edge is the certificate, not speed.

---


### 313. [How Shared Representations Become Specialized: Formation, Maintenance, and Latent Susceptibility](https://arxiv.org/abs/2610.15830)

**<font color=#1a73e8>作者：</font>** Toru Takahashi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When several predictions use the same internal representation, information about some targets can remain easier to recover than information about others. We study how this specialization forms, persists, and changes in minimal artificial learners. With reconstruction errors weighted equally during learning, changing which target is observed precisely selects the favored target and redirects an already specialized learner. Removing current support can reduce a formed bias, whereas state-following update feedback can maintain it. We then compare learners formed through different observation and update conditions but matched on specified reconstruction measurements. Both change under the same brief opposing intervention, yet their responses differ. Resetting Adam largely removes the ten-update difference; exchanging its second moment reverses which route is more susceptible. New interventions show that equalizing the mean second-moment scaling reduces but does not remove the difference: its coordinate-wise pattern also matters. With fresh Adam or calibrated SGD, smaller route differences emerge later, whereas 500 common opposing updates bring the selected allocation endpoints close. A further control produces response differences with identical acquisition and equal mean loss weights but jointly different weight variability and realized sequence. Acquisition-selected formation also extends to a symmetric three-target setting. These interventions distinguish specialization's formation, present support, and time-dependent latent susceptibility.

---


### 314. [Binding Phoneme Identity to Position in Neural Models and the Human Brain](https://arxiv.org/abs/2610.15843)

**<font color=#1a73e8>作者：</font>** Nafiseh Momeni, Malo Renaudin, Itzhak Fried 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A fundamental challenge in cognitive science and neural computation is the binding problem. Compositional generalization can be achieved by factorizing representations into roles, the structural slots of a representation (e.g., serial position or syntactic function), and fillers, the contents occupying them (e.g., a phoneme or a word), which can be recombined freely to represent novel combinations. How neural systems implement role--filler binding, however, remains unknown. One of its simplest cases is phoneme sequencing, where phoneme identity (filler) must be bound to position (role) so that /gum/ and /mug/ are represented differently. A proposal from NLP, the `onion hypothesis' (Csordas et al., 2024), holds that the direction of the neural population state encodes token identity, while its magnitude encodes position. It was formulated for random token sequences; we extend it to natural language and test it in neural models and the human brain. We first evaluated it in an encoder-decoder trained to repeat English words, using representational geometry analyses and causal interventions. Magnitude alone proves incomplete: position is encoded by magnitude together with a systematic rotation of the state direction, a scheme we formalize as the `spiral hypothesis'. We then analyzed intracranial recordings from the auditory cortex of 20 participants listening to short sentences. Across superior temporal gyrus electrodes, the change in population response between consecutive phonemes decreases in magnitude as position advances, and its direction is aligned within consonants and within vowels but near orthogonal across the two classes, supporting the magnitude coding shared by both accounts. These results provide a geometric account of how neural systems bind phoneme identity to position, and show how neural-model hypotheses can yield testable predictions about human neural computation.

---


### 315. [Mobility Helps Learning: Unsupervised Model Adaptation for Object Recognition via Movement](https://arxiv.org/abs/2610.15846)

**<font color=#1a73e8>作者：</font>** Yanan Ma, Yihang Tao, Zhengru Fang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Movable agents, such as autonomous vehicles and robots, should be able to autonomously adapt their pre-trained object recognition models to new environments without human annotations. While existing test-time adaptation (TTA) methods address label-free model adaptation, they typically treat test data as independent snapshots, without constructively exploiting a rich, unique source of supervision: the significant variance in prediction quality as an agent observes the same object from different distances and viewpoints. To capitalize on this, we propose \texttt{MoCaFe}, a model-agnostic and hyperparameter-insensitive paradigm that leverages motion-induced prediction variance for unsupervised adaptation. Specifically, we first develop mobility-calibrated filtering of pseudo-labels, which constructs reliable pseudo-labels by fusing cross-view predictions using inverse-variance weights. The filtered pseudo-labels then guide the selection of ``hard samples'' for effective learning. To further suppress pseudo-label corruption, we introduce \texttt{p-MoCaFe}, an optional extension that uses a public dataset to assign weighting factors to data samples, yielding an estimator of the clean loss with bounded bias. Extensive experiments on autonomous driving (nuScenes, KITTI) and embodied-agent datasets show that \texttt{MoCaFe} significantly outperforms state-of-the-art TTA schemes, achieving up to approximately 20% accuracy gain.

---


### 316. [What Do Sparse Autoencoder Feature Discovery Scores Identify? From Activations to Interventions](https://arxiv.org/abs/2610.15850)

**<font color=#1a73e8>作者：</font>** Yifeng Guo, Yanran Li, Xiang Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoder (SAE) features are typically discovered from how their activations co-vary with behaviour, yet they are often used through interventions such as steering or ablation. We take intervention attribution, the first-order effect of a specified intervention on the model output, as our estimand. For a broad class of response functions, we show that observational feature-discovery evidence generally does not identify this attribution, and derive an exact gradient-based decomposition of the gap between linear-probe predictions and intervention attribution. Across four model-SAE pairs, median probe-to-attribution magnitude ratios range from tens to hundreds, while attributions closely track small-step steering. For single-latent ablations with nonzero effects, gradient predictions match the realized sign in 91-97% of cases, compared with 17-35% for probe-implied changes. Attribution-selected sets also produce larger absolute mean ablation effects on held-out prompts than sets selected by correlation, rank tests or probe coefficients. Together, these results establish intervention attribution as a principled, gradient-estimable target for selecting SAE features for intervention.

---


### 317. [GuidanceNFT: NFT-Based Reward Fine-Tuning of Guided Diffusion Models](https://arxiv.org/abs/2610.15856)

**<font color=#1a73e8>作者：</font>** Jiayin Liu, Zeyu Michael Li, Bingshuo Qian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> DiffusionNFT (NFT) fine-tunes diffusion models toward task-specific rewards, but optimizing these rewards does not guarantee fidelity to the full prompt. Although classifier-free guidance (CFG) strengthens prompt alignment, NFT is formulated as a CFG-free method, and applying CFG to the fine-tuned velocity field can reduce the optimized reward. This motivates optimizing rewards over the guided output distribution while seeking to retain its prompt alignment. However, applying standard NFT directly to guided samples can cause reward degradation or training collapse. We trace this failure to a mismatch between the reference velocity used in the NFT loss and the score of the guided sample distribution, which biases the improvement direction. We propose GuidanceNFT, which estimates the matching reference velocity through online flow matching on guided samples and uses it to correct both regression terms. With an exact reference, the corrected objective recovers NFT's intended update. In our experiments, the learned correction sustains reward improvement under both explicit and built-in guidance. On SD3.5-M, GuidanceNFT achieves higher optimized rewards than NFT with and without CFG across GenEval, text-rendering, and multi-reward objectives, together with better overall prompt alignment as measured by off-domain evaluation metrics. Experiments on models with built-in guidance, including Model Guidance and ELF, further demonstrate improved ImageNet generation, a better perplexity-entropy tradeoff on OpenWebText, and higher accuracy on GSM8K.

---


### 318. [A Hybrid Gaussian Process-Extreme Gradient Boosting Machine Learning Framework for Robust Knockdown Factor Prediction and Reliability-Based Design of Thin Spherical Shell Caps](https://arxiv.org/abs/2610.15862)

**<font color=#1a73e8>作者：</font>** Budhaditya De, Rohan Majumder, Devasmit Dutta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Elastic buckling remains a critical concern in the design of deep spherical shell caps, given that experiments reveal a significant reduction of critical loads from those predicted by linearized eigen-buckling analysis. This discrepancy has been attributed to initial geometric imperfections and is often reconciled through a dimensionless parameter, namely the knockdown factor (KDF). However, conventional KDFs (NASA SP-8007; Eurocode 3) are highly conservative, as they represent the lower bound of an extensive body of experimental data. This study aims to narrow the conservatism in the KDFs for spherical shell caps through machine learning (ML) regression models trained on experimental data on spherical shell buckling. A hybrid model is proposed by combining Gaussian Process Regression (GPR) with Extreme Gradient Boosting (XGBoost), and its improved performance is demonstrated over conventional ML algorithms, i.e., the Artificial Neural Network (ANN), Support Vector Regressor (SVR), Random Forest Regressor (RFR), and Histogram-based Gradient Boosting (HGBoost). Each of these models uses six input features and a single output, i.e., the KDF. The most critical feature affecting the KDF is ascertained through a sensitivity analysis. The study concludes with a reliability-based design framework that relies on the predictive ML model to obtain safety-consistent, yet less conservative, KDFs.

---


### 319. [Penetrating the Reality Wall: Long-Range and Through-Wall AR/VR Privacy Eavesdropping via Wireless Power Side Channel](https://arxiv.org/abs/2610.15865)

**<font color=#1a73e8>作者：</font>** Tao Ni, Zehua Sun, Yihe Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Over the past decade, Metaverse technology (AR/VR) has seen widespread adoption in numerous areas, including gaming, social networking, and online collaboration. Although recent studies have exposed vulnerabilities in VR systems, they often apply methods (e.g., pre-installed malicious apps or scripts) from conventional mobile platforms directly, demonstrating impractical attacks that fail to investigate unique privacy leakages specific to VR platforms. In this paper, we present an orthogonal attempt to analyze the attack surface of the power side channel on AR/VR's network connection by capturing the through-wall wireless power in the network transmission medium (e.g., Wi-Fi signals) non-intrusively in a comparatively long distance (e.g., 5.0m-8.0m) and further reconstructing multi-level privacy-aware user behaviors.
We propose MetaSpy to validate the feasibility and practicality of our disclosed wireless power-based traffic analysis attack. It first captures through-wall wireless power transmitted from the Wi-Fi router of an adjacent room, identifies the device type, then infers (i) user interactions such as browsing websites, running AR/VR apps, and performing various in-app activities, (ii) unseen VR-specific activities in VR games (e.g., Population: ONE), and (iii) avatar-based user re-identification and virtual keystroke inference corresponding to head movements. We evaluated the effectiveness of MetaSpy in four commercial-off-the-shelf (COTS) VR headsets, and the empirical results demonstrate its competitive accuracy in unveiling multi-level user privacy within virtual scenes in through-wall settings at a longer distance (1.8x-80x) than most of the recent studies, and it shows resilience to a series of external interference and impact factors. In addition, we also propose and evaluate effective countermeasures to protect data confidentiality in AR/VR wireless transmission.

---


### 320. [Comparative Study of Canvas- and Coordinate-Based Geometry-Conditioned Neural Networks for Real-Time Prediction of Indoor Environments with Varying Room Dimensions](https://arxiv.org/abs/2610.15885)

**<font color=#1a73e8>作者：</font>** Shaofan Wang, Philipp Geyer  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computational fluid dynamics (CFD) is computationally expensive for iterative building design. Deep learning surrogates offer faster predictions, but generalization across varying room dimensions remains challenging. This study compares two geometry-conditioned neural network surrogate models for rapid indoor airflow and temperature field prediction under varying room sizes. During the architectural design stage, this method is relevant for real-time assessment of whether conditioned supply air will effectively provide fresh and cool air throughout rooms with varying heights and lengths. The canvas-based neural network (CaNN) explicitly encodes room size by preserving different occupied regions within a fixed canvas, whereas the coordinate-based neural network (CoNN) uses normalized coordinate channels. Both employ U-Net autoencoders to separately predict airflow and temperature fields. Evaluation uses simplified rooms with varying heights and lengths as a controlled benchmark. The results show that CaNN achieves higher agreement with CFD results than CoNN, demonstrating its potential to support performance-driven building design.

---


### 321. [Learning Multimodal Sensor Fusion with JEPA Representations for Breathing Activity and Pose Recognition](https://arxiv.org/abs/2610.15891)

**<font color=#1a73e8>作者：</font>** Yunxiang Luo, Constantino Álvarez Casado, Xiaoting Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predictive video representations do not by themselves specify how a multimodal system should handle missing sensors. We transfer frozen V-JEPA2 features to a set of heterogeneous sensors comprised by RGB video, depth video, and radar time series. A shared fusion model uses modality queries, fixed sensor slots, and explicit availability to classify breathing activity and pose from all seven non-empty sensor subsets. The contribution is a controlled evaluation of subset supervision, pooling capacity, and representation transfer on 39 OMuSense-23 subjects with five subject-group folds and three seeds. With matched downstream parameter counts, the final model reaches recording-level activity macro-F1 of $75.23%\pm0.60$ averaged across seven subsets. Supervising all subsets in each batch improves the matched query-pooling control by 1.923 percentage points (conditional 95% subject-bootstrap interval [0.647, 3.209]), while query pooling shows no clear advantage over matched mean pooling under balanced supervision. Radar probes support transfer beyond pooled wavelet pixels, 64-token inference approximately preserves mean activity performance, and the tested Consensus-JEPA loss adds no measured benefit against its exact control.

---


### 322. [Gen Through the Lens: Camera-Controllable Video Generation via Cross-Coordinate Conditioning Fusion](https://arxiv.org/abs/2610.15900)

**<font color=#1a73e8>作者：</font>** Shuai Li, Jinxu Xiang, Xinyuan Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Gen Through the Lens, a camera-controllable image-to-video generation framework that synthesizes videos from a given reference image while enabling realistic and physically consistent camera operations. Unlike previous models that treat camera motion as abstract conditioning or rely on a single coordinate system, our approach explicitly decomposes and fuses control signals across three coordinate spaces: the camera coordinate (modeled by intrinsic parameters), the world coordinate (represented by spatial geometry hints), and the object coordinate (described by 3D bounding boxes of target subjects). Through cross-coordinate conditioning fusion, these heterogeneous cues are unified to guide the generative process, enabling precise control of camera motion, focus, and framing while preserving temporal and spatial coherence. Extensive experiments demonstrate that our method produces controllable and visually consistent results across diverse camera operations, outperforming existing approaches in both realism and editability.

---


### 323. [Forensic Text Recovery from Document Thumbnails Using Text-Aware U-Net](https://arxiv.org/abs/2610.15902)

**<font color=#1a73e8>作者：</font>** Mohit Ajaykumar Dhabuwala, Weifeng Xu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Forensic analysis of low-resolution Word thumbnails presents a significant challenge because these artifacts may constitute the only remaining visual evidence of deleted documents. Standard Optical Character Recognition (OCR) tools perform poorly on such severely degraded images, creating a critical bottleneck in forensic evidence recovery. Although deep learning architectures, such as U-Net, can improve visual image quality, models optimized solely using pixel-based loss functions tend to favor visual smoothness over the structural fidelity required for accurate text recognition. To address this limitation, we propose a text-aware restoration framework designed for forensic triage. The proposed approach employs a U-Net architecture guided by a hybrid optimization strategy that integrates pixel-level fidelity with machine-readable text constraints. Specifically, an OCR-based Normalized Levenshtein Distance (NLD) metric is used during model selection to prioritize the recovery of an accurate character topology. Experimental results demonstrate that the proposed method significantly reduces the NLD, enabling reliable recovery of machine-readable text from severely degraded thumbnails.

---


### 324. [RIVO: Lightweight Adaptive Rerouting for Deep Research Agents](https://arxiv.org/abs/2610.15910)

**<font color=#1a73e8>作者：</font>** Mingchen Li, Jiatan Huang, Hong Yu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deep Research agents rely on long-horizon reasoning and iterative tool use to solve complex information-seeking tasks. However, adaptive decision-making over these trajectories remains challenging, as agents may stop prematurely when further evidence is needed, continue unnecessarily after sufficient evidence has been gathered, or fail to redirect unproductive trajectories. Existing solutions either require costly model retraining and dense turn-level supervision, or rely on heuristic control rules that are not directly optimized for downstream research utility. This motivates a lightweight, utility-aware alternative for Deep Research control. We formulate adaptive rerouting in long-horizon Deep Research as a state-conditioned trajectory correction problem. Based on this view, we introduce RIVO, a lightweight plug-in framework for adaptive trajectory correction. The agent estimates its research state from lightweight signals and determines whether trajectory redirection is needed. Once triggered, the plug-in modifies the Host token logits to steer generation toward a more promising research direction. Theoretical analysis shows that, under a value-alignment condition and bounded local curvature, a sufficiently small logit intervention can locally improve expected downstream research utility. We further construct BrowseCore, a curated dataset with a paired local corpus, for efficient and controlled Deep Research experimentation. Building on this resource, the plug-in is trained from downstream outcomes, enabling it to learn corrections that improve subsequent research and final task performance. Extensive experiments across multiple Deep Research benchmarks and control settings demonstrate the effectiveness of our method, showing that lightweight logit intervention can improve long-horizon research without retraining the underlying Host model.

---


### 325. [VIEWCRAFT: Evolving What Multimodal Agents See and How They Read It](https://arxiv.org/abs/2610.15915)

**<font color=#1a73e8>作者：</font>** Binxiao Xu, Ruichuan An, Bocheng Zou 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reusable skills improve multimodal agents without updating model weights, but their effectiveness depends on both the evidence presented and the procedure used to read it. We introduce ViewCraft, which jointly evolves an executable evidence interface and its reading procedure. The interface selects, transforms, and organizes observations; the reader interprets the resulting views. Failure traces guide revisions, replay and paired evaluation retain useful changes, and interface projection recovers visual edits from eligible rejected joint proposals. Across eight benchmarks, ViewCraft improves over direct execution by an average of $6.1$ points in task score, with gains on every benchmark. The advantage persists at a matched input-token budget. On all five multi-source tasks, the learned interface uses 8%-15% fewer input tokens than Initial skill. The learned skills also transfer across executors and outperform direct execution in every evaluated transfer, supporting evidence construction and reading as a coupled, reusable skill.

---


### 326. [Sample-Optimal Multi-Group Learning with an ERM Oracle](https://arxiv.org/abs/2610.15916)

**<font color=#1a73e8>作者：</font>** Princewill Okoroafor  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In multi-group learning, a single predictor must perform nearly as well as the best hypothesis in a class on every group in a rich, possibly infinite and overlapping, collection of subpopulations. The known algorithms with the optimal sample complexity keep track of every pair of a group and a hypothesis, which is impossible for the large classes of interest, and the known oracle-based algorithms have a worse rate. We ask whether the optimal rate can be attained by a learner that accesses the classes only through an empirical risk minimization (ERM) oracle. We give an algorithm that uses $\tilde{O}((d_G+d_H)/\varepsilon^2)$ samples and polynomially many calls to a weighted ERM oracle over pairs of a group and a hypothesis, where $d_G$ and $d_H$ are the VC dimensions of the group and hypothesis classes and $\varepsilon$ bounds the excess risk on every group, weighted by its probability. We also show a matching lower bound of $\Omega((d_G+d_H)/\varepsilon^2)$ samples for every learner even with unlimited computation, so oracle efficiency costs no additional samples. We also consider a natural special case in which every input belongs to at most $k$ groups and these groups can be listed. In this case, an ERM oracle for the hypothesis class alone suffices, with $\tilde{O}((d_H+\log k)/\varepsilon^2)$ samples in the agnostic setting and $\tilde{O}((d_H+\log k)/\varepsilon)$ samples when every group has a hypothesis that is correct on it.

---


### 327. [Frequency-Step Cache: Separating Synchronization and Repair for Efficient Autoregressive Video Diffusion](https://arxiv.org/abs/2610.15922)

**<font color=#1a73e8>作者：</font>** Kerry Xu, Param Misra, Zachary Stenglein 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) video generation enables long-horizon synthesis but requires repeated forward passes through large diffusion transformers. Training-free caching reduces this cost by reusing intermediate computation, yet existing controllers often couple two decisions: when to synchronize the cache exactly and how much computation to repair between synchronizations. We introduce Frequency-Step Cache (FSC), which separates these roles. FSC schedules exact full-computation anchors on a dense-to-sparse trajectory, while a lightweight latent-space risk based on frequency-resolved drift and token age controls inter-anchor repair through whole-step replay, selective token recomputation, or full repair. On SkyReels-V2, whole-step reuse provides most of the acceleration, while selective token computation is most effective as fidelity repair. A controlled ablation shows that using one reactive signal for both synchronization and repair reduces fidelity at matched latency, with the same separation advantage observed on FramePack and Matrix-Game. Across multiple autoregressive video backbones, FSC improves speed-quality trade-offs. On SkyReels-V2, FSC-Speed reaches 2.36x speedup versus MotionCache's 2.275x while improving SSIM by 0.019 and PSNR by 0.5 dB. At MotionCache-matched speed, FSC-Quality improves SSIM by 0.031 and PSNR by 1.0 dB and lowers LPIPS by 0.024. Without retuning, FSC-Quality transfers to SkyReels-V2 14B at 2.12x speedup versus 1.79x for MotionCache.

---


### 328. [Multi-Horizon Explainable Queue Forecasting and Resource-Aware Decision Support for Intelligent Border Control Using LightGBM](https://arxiv.org/abs/2610.15930)

**<font color=#1a73e8>作者：</font>** Varvara Mama, Fani D. Christidi, Nikolaos C. Kapsalis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Border crossing points are stochastic service systems in which traffic demand, traveler categories, registration status, inspection requirements, staffing, and lane availability interact on multiple time scales. This paper extends an earlier multimodal queue-management framework by introducing an implementation-oriented, multi-horizon forecasting and decision-support architecture based on Light Gradient Boosting Machine (LightGBM) models. In contrast to a single forecasting block, the proposed approach constructs horizon-specific regressors for 15, 30, 60, and 120 min forecasts and jointly estimates future waiting time and queue lengths. The models operate on temporally lagged traffic, service, density, and queue features, while an operational layer incorporates lane compatibility, officer availability, possibly degraded resources, traveler category, preregistration information, and human-approval constraints. Quantile LightGBM models provide 95\% prediction intervals for waiting-time forecasts. Beyond prediction, the framework produces machine-readable recommendations, alerts, aggregate key performance indicators, confidence information, and integration outputs suitable for border resource-management and decision-support systems. The results establish a reproducible synthetic-data baseline and a practical interface for subsequent validation with operational border-crossing data.

---


### 329. [Mesh-Free Convolution: Learned Spectral Attenuation and Transport](https://arxiv.org/abs/2610.15931)

**<font color=#1a73e8>作者：</font>** Niloufar Zakariaei, Manav Manav, Eldad Haber  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning solution operators for partial differential equations (PDEs) requires models that can represent spatial structure across grids and scales. This becomes especially important in time-dependent problems, where the learned operator is often used autoregressively: each predicted state is fed back as input to predict future states. In this setting, small spatial errors can be repeatedly propagated through the learned dynamics, leading to instability and drift, vitiating long-term solution fidelity.
We propose Mesh-Free Convolutions (MFCs), filters defined in continuous space and discretized only at evaluation time. This allows the same learned filters to be applied across resolutions. Rather than imposing a grid-dependent stencil or a fixed spectral cutoff, MFCs learn smooth scale-dependent filtering and include directional terms for transport-like behavior.
Across fluid-dynamics and weather-forecasting benchmarks, MFC-based models produce stable long-horizon rollouts, transfer reliably across resolutions, and better preserve long-time statistics. These results suggest that continuous, mesh-free filtering is a useful inductive bias for PDE operator learning, especially in autoregressive prediction.

---


### 330. [DiffNash: Finding Nash Equilibrium in High-Dimensional Continuous Action Spaces with Diffusion Policies](https://arxiv.org/abs/2610.15932)

**<font color=#1a73e8>作者：</font>** Haichuan Wang, Anagha Satish, Jiale Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Computing equilibria in high-dimensional continuous games requires learning and representing rich, multi-modal strategy distributions, something conventional neural policies struggle to achieve. Diffusion models offer a natural solution, but standard diffusion training requires direct samples from a fixed target distribution, which are generally unavailable under iterative game-solving updates. We propose a diffusion-based framework for equilibrium computation that enables diffusion-based variants of Online Mirror Descent (OMD) and Fictitious Play (FP). Our approach derives a reweighted score-matching objective that trains diffusion policies without requiring direct samples from each updated policy. Our main method, DiffNash, combines the fast convergence of OMD with the sample efficiency of FP by reusing past actions through a replay buffer. To correct the resulting distribution shift from sample reuse, we derive an unbiased estimator of the difference between current and past policies' Evidence Lower Bounds, whose exponential provides a tractable proxy for the corresponding importance weight without evaluating diffusion likelihoods. We evaluate our approach on forest protection games and continuous Colonel Blotto games, reducing the Nash gap over the strongest baseline by 35.6% and 24.7%, respectively, with minimal hyperparameter tuning.

---


### 331. [Error-Based Bidirectional Predictive Coding Enables Deep, 4-Bit Predictive Coding Networks](https://arxiv.org/abs/2610.15933)

**<font color=#1a73e8>作者：</font>** Garrett Kinman, Zeljko Zilic  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive coding networks (PCNs) promise properties not offered by backpropagation-trained networks: learning from purely local information, a single network that both discriminates and generates, and flexible inference by energy minimization. However, their iterative inference is expensive, making hardware acceleration desirable, and a useful, efficient accelerator needs both depth and aggressive quantization. Canonical state-based PC delivers neither: its inference signal decays exponentially with depth, so deep models fail to train, and low precision makes it worse. We show that pairing two recent methods carries the full PCN property set into the deep, 4-bit regime: bidirectional PC (bPC), which unifies discrimination and generation, and the error-based reparameterization (ePC), which optimizes prediction errors rather than states during inference. Error optimization delivers the output signal to every layer in a single backward pass, removing the signal decay; one additional element, global-norm clipping of the error gradients, stabilizes the error dynamics at depth. The resulting ePC+bPC model trains stably up to at least eight layers and retains its full-precision accuracy and clean class-conditional generation under W4A4E4 quantization-aware training, across FP4 and three posit formats. On six-layer networks, where state-based bPC collapses to chance, ePC+bPC classifies more than 50 accuracy points above it after one epoch of training, with class-conditional generations 5-9x better in RMSE. 4-bit quantization is nearly free: full-precision and 4-bit accuracies differ by at most ~5 points, and by under two in the best-performing formats. We characterize the two failure modes the method overcomes, bounded signal decay in state-based PC and error divergence in unregularized error optimization, and discuss implications for a 4-bit-native PCN accelerator.

---


### 332. [Natural Language Processing for Aligning Readings with Learning Objectives and Assessing Topic Balance in Dental Education](https://arxiv.org/abs/2610.15941)

**<font color=#1a73e8>作者：</font>** Farzana Yasmin, Tahereh Firoozi, Rojin Adabdokht  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Curriculum teams often lack time to check whether assigned readings support learning objectives (LOs) and whether topic coverage is balanced. We present a natural language processing (NLP) workflow to support evidence-informed curation of reading lists. The workflow combines PubMedBERT sentence embeddings and cosine similarity for retrieval, natural language inference (NLI) for evidence checking, and topic modeling for coverage analysis. We tested the approach in dental education using 13 course-level LOs and a PubMed-derived corpus of 3,837 LO-abstract pairs. Median cosine similarity ranged from 0.86 to 0.91 across the 13 LOs, showing generally high semantic similarity. Topic modeling showed broad but uneven coverage, with one or two dominant topics per domain. Similarity alone was not enough for selecting readings: among high-similarity pairs (cosine 0.90-1.00), 22.9% were classified by NLI as neutral or contradictory. In a 49-pair expert-labeled validation set, cosine-based retrieval (cosine >= 0.90) achieved 0.69 accuracy, while the combined cosine and NLI approach achieved 0.73 accuracy against expert alignment labels. Overall, the workflow shows how AI can support curriculum alignment by reducing false positives and helping select readings that better match intended LOs.

---


### 333. [Vision: "What Don't I Know About User's Preferences?" How Uncertainty Estimation Improves Proactive Assistant Alignment](https://arxiv.org/abs/2610.15948)

**<font color=#1a73e8>作者：</font>** Zhiyu An, Ziyi Xuan, Yu Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Proactive Smart Assistants (PSAs) increasingly use general knowledge, learned patterns from group-level data, patterns from individual user's data, and recent sensor observations to anticipate which action a user may prefer. Existing systems typically select actions from predicted user preference likelihoods, but these likelihoods alone do not reveal how reliable the prediction is, which evidence supports it, or why ambiguity remains. In this vision paper, we argue that uncertainty estimation can provide this missing information and substantially change appropriate downstream behavior. Using the example of a home assistant, we introduce the questions that uncertainty estimation aims to answer, i.e. how sure is the assistant about the predicted preference likelihood, whether the confidence come from group-level assumptions or individual's data, and whether likelihood ambiguity reflect the user's intrinsic preference variability or insufficient data for the particular situation. We further introduce uncertainty estimation applications in neighboring domains, such as human trajectory prediction, personalized activity recognition, information-collection, and model-based control. Finally, we draw on insights from neighboring domains to envision how future uncertainty-aware proactive assistants may address key challenges in proactive interaction.

---


### 334. [Hardware-Assisted Multi-Stage Ransomware Detection with Adaptive Machine Learning](https://arxiv.org/abs/2610.15951)

**<font color=#1a73e8>作者：</font>** Salma Aboelmagd, Md. Rakibul Ahasan, Zhixin Pan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Ransomware is a fast-escalating privacy threat causing significant financial and data losses worldwide. As attacks grow more sophisticated, traditional static signatures and dynamic behavior analysis struggle to defend. In this paper, we propose an novel framework that couples software-level scanning with hardware-level microprocessor activity monitoring to achieve efficient ransomware detection and mitigation. The contributions are threefold: (1) we employ adversarial training to harden static analysis against obfuscation and leverage hardware-assisted monitoring for real-time detection; (2) we integrate neural architecture search (NAS) to automatically tailor models for stronger generalizability; and (3) We validate the proposed approach through extensive experiments, demonstrating substantially improved detection accuracy and reduced latency compared with existing methods. Moreover, it provides trace-level interpretability that explains the underlying decision process.

---


### 335. [Instance-Adaptive Online Multiclass Multicalibration](https://arxiv.org/abs/2610.15954)

**<font color=#1a73e8>作者：</font>** Zhiming Huang, Jamie Morgenstern, Aaron Roth 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study online multiclass multicalibration over $T$ rounds, and give an algorithm with beyond-worst-case guarantees. With $n$ possible outcomes, forecasts lie in a simplex of dimension $d=n-1$. In the worst case, cumulative $\ell_1$ multicalibration error scales with $\widetilde\Theta(T^{(d+1)/(d+2)})$, which becomes untenable once $d$ exceeds a small constant. Our algorithm adapts to the geometry of the realized sequence: if the sequence of adversarially selected outcome means lies in an affine subspace of dimension $s$, it obtains error $\widetilde O(n^{1/(s+2)}T^{(s+1)/(s+2)})$ with high probability. The algorithm adapts to this structure without knowing the subspace or its dimension. For $T\ge n\ge2$, this rate is minimax optimal up to polylogarithmic factors. For a stochastic instance with a fixed conditional mean, the bound specializes to $\widetilde O(\sqrt{nT})$, giving a square-root dependence on the horizon.

---


### 336. [Scaling Repeated-Data Pretraining: Batch Size, Regularization, and GPU-Time Tradeoffs](https://arxiv.org/abs/2610.15965)

**<font color=#1a73e8>作者：</font>** Sewon Min  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study pretraining when compute is abundant but unique training data are finite, requiring repeated training on the same data. We first revisit infinite-compute pretraining (Kim et al. 2026) and show that its frontier depends critically on choices previously fixed or studied only in isolation. In particular, optimizing batch size together with epoch counts reveals a U-shaped relationship between validation loss and batch size, favoring smaller batches than typical pretraining, likely because small-batch gradient noise provides implicit regularization. We further find that training recipes, previously optimized under a single-pass assumption, can be tuned, e.g., repacking documents into new sequences every epoch, weight tying, and positive embedding weight decay.
We then relax the infinite-compute assumption. In particular, smaller-than-typical batch sizes can require prohibitively long sequential training, motivating to treat GPUs and time as separate resources. Tighter deadlines favor larger batches, and latency-oriented parallelism can trade additional GPUs for shorter training. Nevertheless, even under a fixed time budget, a smaller batch with fewer GPUs can achieve lower validation loss than a larger batch with more GPUs, challenging the common practice of increasing data parallelism to maximize GPU utilization under a deadline. Together, our results identify underexplored factors in repeated-data training and provide concrete guidance on how training recipes and resource allocation should change from single-pass pretraining.

---


### 337. [Softmax-Free Attention in Spiking Transformers as the Zero-Temperature Limit of Two-Level Systems](https://arxiv.org/abs/2610.15968)

**<font color=#1a73e8>作者：</font>** Roberto C. Sotero, Pouya Taghipour, Jose M. Sanchez-Bornot  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spiking Transformers achieve energy efficiency by discarding softmax normalization in favor of thresholded, binary attention. However, this removal breaks the thermodynamic framework used to analyze attention networks, as the normalized measure and partition function cease to exist. We restore this theoretical foundation by proving that softmax-free spiking attention operates exactly as the zero-temperature limit of a product of independent two-level systems. This correspondence places spiking attention strictly in the frozen ordered phase of the thermodynamic phase diagram for all inputs. Consequently, the entropic cost of organizing attention collapses, replaced by a Landauer-type physical floor governed by action-potential generation. Furthermore, this ordered-phase pinning mathematically explains the optimization difficulty caused by vanishing surrogate gradients. We validate this theory with forward-relaxation experiments, placing both standard and neuromorphic attention mechanisms on a unified thermodynamic axis.

---


### 338. [Mixed Feelings, Single Polarity](https://arxiv.org/abs/2610.15977)

**<font color=#1a73e8>作者：</font>** Emily Öhman, Saif Mohammad  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emotion datasets are routinely mapped onto positive and negative valence, by assigning each emotion category one polarity. We test where this works and where it fails, using SemEval-2018 Affect in Tweets (English, Arabic, Spanish), Affective Text aligned with EmoBank, raw GoEmotions annotations, naturalistic hashtag corpora, and a controlled annotation study. Fixed projection works well when a text carries labels of one valence. It fails on a subset identifiable from the labels alone: tweets whose emotion labels point in opposite directions. These are 9.0% of polar SemEval test tweets but cause 54.8% of the polarity errors of a learned projection, are more than twice as likely to receive a neutral-or-mixed gold label, and are not rescued by modeling the full label set. Annotators produce such configurations routinely: 16.3% of multilabel GoEmotions judgments combine emotions from the dataset's own positive and negative parents. In a controlled study holding word and reader constant, context changes the coarse valence judgment in 56.8% of cases, against 19.9% for controls. We recommend projecting label configurations rather than labels, abstaining or keeping a mixed class where labels conflict, and reporting coverage alongside accuracy.

---


### 339. [Probabilistic Forecasting of Wildfire Size Using Conditional Flow Matching](https://arxiv.org/abs/2610.15983)

**<font color=#1a73e8>作者：</font>** Isaac Lee, Bryan Shaddy, Assad Oberai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work we present a probabilistic model for predicting the temporal evolution of wildfire size using conditional generative algorithms, namely flow matching. Rather than predicting spatially resolved fire progression, the proposed model forecasts a time series of fire acreage, substantially reducing computational cost and enabling efficient integration with downstream applications such as early warning systems and risk assessment tools. Given estimates of the fire size at the current and previous forecasting steps, alongside spatially averaged weather conditions, terrain characteristics, and fuel composition, the model predicts the change in fire area over a 3-hour interval. Training data are drawn from 140 coupled atmosphere-wildfire simulations generated using WRF-SFIRE, paired with weather data from the North American Mesoscale (NAM) model. Sensitivity analysis demonstrates that the model captures physically-consistent responses to variations in wind speed, temperature, and relative humidity. Model performance is evaluated against reference solutions from WRF-SFIRE. For single-step predictions, the model achieves a symmetric mean absolute percentage error (sMAPE) of 0.39 relative to the reference WRF-SFIRE solutions. Recursive multi-step predictions over 24 hours are performed for 12 held-out test cases, where the flow matching model achieves a final fire area sMAPE of 0.39 while further providing meaningful quantification of forecast uncertainty.

---


### 340. [A Mechanomyography-Based Integrated Sensing-Stimulation System for Fatigue-Aware Neuromuscular Therapy](https://arxiv.org/abs/2610.15987)

**<font color=#1a73e8>作者：</font>** Xiao Jin, Cong Liu, Zhenhua Yu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Muscle fatigue limits the effectiveness of functional electrical stimulation (FES), yet fatigue monitoring during active stimulation remains challenging because electromyography (EMG) is severely contaminated by stimulation artifacts. To address this issue, this study proposes an integrated mechanomyography-based sensing framework (MMG-FES) for artifact-resistant fatigue monitoring during stimulation. Fatigue states were first characterized during voluntary movement using established EMG spectral indicators, including median frequency (MF) and mean power frequency (MPF), and then linked to MMG-derived features, including high-frequency energy ratio (HFER) and spectral bandwidth (BW), for fatigue recognition under stimulation conditions. Experimental results showed consistent fatigue-related trends, with EMG spectral features decreasing and MMG features exhibiting coordinated spectral redistribution across repeated contractions. Using these features, the proposed framework achieved fatigue-state recognition accuracies of 0.93 and 0.96 with logistic regression and random forest, respectively. These findings support MMG as a physiologically meaningful and stimulation-compatible modality for fatigue-aware closed-loop neuromuscular stimulation.

---


### 341. [Dissipative Lagrangian Neural Networks for the Interpretable Modelling of Passive Mechanical Systems](https://arxiv.org/abs/2610.15996)

**<font color=#1a73e8>作者：</font>** Rob Seabourne, Alice Cicirello  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose the Dissipative Lagrangian Neural Network (dLNN), a continuous-time system identification technique that separately learns the conservative and dissipative dynamics of a mechanical system directly from data. A key contribution is a novel parametrisation of dissipative forces that (i) is structurally constrained to be dissipative, enforcing passivity of the learned model, (ii) cannot absorb conservative mechanics, and (iii) retains sufficient expressivity to represent a broad family of state-dependent damping and regularised friction forces. The model is validated on prediction tasks on two real-world mechanical systems: trajectory prediction of a chaotic double pendulum and inverse-dynamics modelling of a six-degree-of-freedom industrial robot. Across these tasks, the dLNN demonstrates improved predictive performance over existing Lagrangian architectures while remaining competitive with a black-box neural model. The imposed physical structure also improves generalisation to unseen states, with the benefits becoming particularly pronounced when training data is limited. Finally, we introduce a symbolic distillation procedure that extracts closed-form expressions from the learned physical components. Applied to the industrial robot, this produces interpretable symbolic models that retain high predictive accuracy while reducing the computational overhead associated with evaluating neural Lagrangian models.

---


### 342. [Representational Difference Distillation](https://arxiv.org/abs/2610.15997)

**<font color=#1a73e8>作者：</font>** Abdulkarim Mugisha, Divin Irakiza  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation transfers representational knowledge from a large teacher network to a compact student. Existing relational and contrastive distillation methods treat all samples uniformly, spending equal gradient on well-matched and poorly-matched regions of the representation space alike. We propose Representational Difference Distillation (RDD), which diagnoses where teacher and student representations structurally disagree and concentrates the distillation signal on those regions. RDD uses two asymmetric affinity matrices that capture opposing directions of misalignment: one identifies samples the student incorrectly considers similar, the other identifies teacher relationships the student has yet to learn. These affinities determine which sample pairs the distillation loss aligns and how strongly it corrects each misaligned sample. On CIFAR-100 with resnet32x4 to resnet8x4, RDD reaches 75.58% test accuracy in our runs, on par with CRD (75.45%) and above KD and RKD. We additionally explore curriculum-based and sampling-based variants, finding that weighting the loss is more effective than filtering the data.

---


### 343. [A 4-Qubit Variational Quantum Classifier for Sequence-Specific Classification of DNMT3A and DNMT3B Flanking Methylation Preferences](https://arxiv.org/abs/2610.15998)

**<font color=#1a73e8>作者：</font>** Murat Isik, Yusuf Moinuddin, Humaira Gowher 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> DNA methylation is a critical epigenetic modification that regulates gene expression and genome stability, primarily catalyzed by the DNA methyltransferase 3 (DNMT3) family of enzymes. Distinguishing precise sequence-specific flanking preferences between DNMT3A and DNMT3B remains computationally challenging due to the complex and high-dimensional nature of biochemical sequence data. In this study, we propose a novel Quantum Machine Learning (QML) approach to classify DNA methylation preferences, leveraging a Variational Quantum Classifier (VQC). Using experimentally derived deep enzymology data, we constructed a dataset containing 4,096 unique NNNCGNNN motifs. We evaluated a four-qubit VQC using a custom NumPy exact-statevector simulator. The described two-layer circuit contains 24 trainable rotations, eight CNOT gates, and eight input-encoding rotations, totaling 40 gates before measurement. Across five initialization seeds, the revised VQC evaluation achieved a ROC-AUC of 0.661 pm 0.009, where variability denotes sample standard deviation. The held-out test partition is approximately balanced, containing 200 DNMT3A-labeled motifs and 210 DNMT3B-labeled motifs. An always-DNMT3B predictor achieves 51.2% accuracy and a balanced accuracy of 0.500 on this test partition. This proof-of-concept establishes a foundation for utilizing near-term quantum architectures in complex epigenetic classification tasks, paving the way for hybrid quantum-classical pipelines in bioinformatics.

---


### 344. [Adversarial Robustness of Camera-Radar Sensor Fusion for Autonomous Driving](https://arxiv.org/abs/2610.16012)

**<font color=#1a73e8>作者：</font>** Ce Zhou, Yubo Wu, Khang Nguyen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous driving (AD) relies on multi-sensor perception to interpret the surrounding environment. However, the robustness of camera--radar fusion under adversarial conditions remains largely unexplored. This paper presents a systematic measurement study of the robustness of camera--radar sensor fusion in AD. We construct a unified evaluation pipeline on the nuScenes dataset that simulates attacks on both sensing modalities, including eight camera-image perturbations and three radar point-cloud perturbations. We evaluate five camera--radar fusion algorithms across two perception tasks, 3D object detection and depth estimation, and quantify their performance under clean and attacked inputs using standard metrics. Our evaluation reveals a clear asymmetry in the robustness of fusion systems. Camera perturbations substantially degrade both object detection and depth estimation, and moderate attack strengths are already sufficient to cause severe performance degradation. In contrast, the evaluated radar perturbations produce smaller and task-dependent effects, with object-detection models showing particularly limited degradation. Our analysis attributes this difference to the strong dependence of existing fusion architectures on dense camera features, together with the filtering, association, and confidence-weighting mechanisms commonly applied to sparse radar measurements. These results demonstrate that sensor fusion does not inherently guarantee robustness and that the contribution and reliability of each sensing modality must be explicitly considered under adversarial conditions. Based on four empirical findings, we derive measurement-guided design implications for future robust camera--radar fusion, including modality-specific reliability estimation, cross-modal consistency checking, adaptive fusion, and graceful failover under severe sensor degradation.

---


### 345. [Certified Robustness via Sparse Second-Order Cone Relaxations](https://arxiv.org/abs/2610.16016)

**<font color=#1a73e8>作者：</font>** Mohammadreza Maleki, Daniel Sadig, Rushendra Sidibomma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Certified robustness is critical for deploying neural networks in safety-sensitive settings, but computing exact certificates typically requires solving nonconvex optimization problems. Practical verifiers use convex relaxations: linear programming (LP) relaxations are scalable but often too conservative, whereas semidefinite programming (SDP) relaxations can be substantially tighter but are computationally expensive. We introduce a hierarchy of second-order cone programming (SOCP) relaxations that provide stronger certificates than LP while avoiding the cost of global positive-semidefinite constraints. Our construction combines convex-hull relaxations of ReLU activations, selective McCormick lifting over certified variable bounds, and second-order cone constraints induced by 2-by-2 principal minors. Adding these constraints progressively yields a monotone hierarchy of increasingly tight bounds with a controllable computation-tightness trade-off. On fully connected and convolutional networks on MNIST and CIFAR-10, SOCP-based verification improves certified robust accuracy over LP-based verification and is competitive with alpha,beta-CROWN, while remaining orders of magnitude faster than SDP-based verification. These results position selective second-order constraints as a practical middle ground between scalable LP-based and tight SDP-based certification. Finally, we introduce class-optimized robust evaluation (CORE), which applies tighter relaxations only to target classes not certified by cheaper ones. On the fully connected MNIST benchmark, CORE variants match SDP-cert's certified robust accuracy while reducing average verification time by up to 86.30%.

---


### 346. [When Does Compensating Inherited Quantization Error Help? Mean-Square Guarantees for Layer-Wise Quantization and Their Limits](https://arxiv.org/abs/2610.16020)

**<font color=#1a73e8>作者：</font>** Tianhao Guo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Layer-wise post-training quantization methods let each layer compensate for the quantization error inherited from earlier layers. We ask under what assumptions such compensation guarantees a network output error no larger than without it. For linear networks of any depth, with the required calibration Gram matrices invertible, if the rounding error of each layer has zero conditional mean and a deterministic second-moment map common to both schemes, as under subtractive dither on an unbounded grid, then compensation with strengths in $[0,1]$ fixed in advance gives a mean-square output error no larger than no compensation, each scheme being followed along its own trajectory. The exact gain separates error removed directly from reduced excitation of later rounding noise. Outside this setting the comparison can fail. With rectified linear activations it fails for two independent reasons: noise changes activation states, and, even when no state changes, the correction moves error from samples on which a unit is inactive to samples on which it is active. With stable activations, commutators between the calibration projection and the activation patterns bound the excess. With a bounded codebook, even unique exact layer-wise minimizers with no overload can give a larger output error. For fixed rounding errors it already fails for two scalar linear layers, refuting a published universal guarantee. An exact residual identity gives the necessary and sufficient condition on a common layer input. All these comparisons hold the calibration input fixed. On two 8B models at 4 bits, fixed half-strength compensation beat uncompensated rounding in every model, text and draw tested, yet no rule for choosing the strength beat a layer-wise rule consistently, and lowering the full-network loss on the data used to choose did not reliably lower it on new text.

---


### 347. [Removing the Compute Bottleneck for Event-based Visual Place Recognition with Spiking Neural Networks](https://arxiv.org/abs/2610.16022)

**<font color=#1a73e8>作者：</font>** Somayeh Hussaini, Tobias Fischer, Michael Milford  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neuromorphic sensing and computing promise low latency and high energy efficiency for robotics, yet most event-based visual place recognition (VPR) pipelines reintroduce dense, frame-like computation downstream of an inherently sparse sensor, forfeiting the sensor's latency advantage. In this paper, we address the problem of resolving an event-based VPR query in tens of microseconds on a commodity CPU. We train a two-layer spiking neural network (SNN) with additive spike-timing-dependent plasticity (STDP), which drives the learned weight matrix towards a strongly bimodal distribution, amenable to aggressive magnitude pruning. At inference, our pipeline exploits this sparsity by reading only the pruned weights corresponding to the query's active pixels. As surviving weights share a near-uniform magnitude, each neuron's score reduces to an integer count of matching synapses instead of a weighted sum, lowering per-query latency. This computation is small enough to remain resident in a CPU's fast on-chip cache. On three event-based VPR benchmarks, our sparse SNN exceeds the recall of LENS, an existing event-based SNN, while reducing per-query latency by 5.5-6.2x to tens of microseconds. It matches the recall of a dense variant of our network and of the sum-of-absolute-differences (SAD) baseline, while reading 10x fewer weights than the dense variant. We further characterise how recall and latency scale with the number of active pixels and reference places. These results suggest that the sparsity of both event-based input and learned weights can already be exploited for low-latency inference on conventional processors.

---


### 348. [Of Errors and Echoes: Responsibility-Aware Credit Assignment for Tool-Use Agents](https://arxiv.org/abs/2610.16027)

**<font color=#1a73e8>作者：</font>** Xingjian Diao, Tianyu Yang, Wenjun Huang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning improves tool-use agents, yet fine-grained credit assignment remains challenging even with step-level feedback. An observed error may be inherited from an earlier decision, while multiple responsible decisions may share the same downstream consequence or participate in later recovery. We introduce Error-Chain-Aware Optimization (ECHO), a responsibility-aware credit assignment framework that separates responsibility identification from credit allocation. A frozen judge combines retrospective trajectory analysis with decision-time assessment from the policy-visible prefix to distinguish newly introduced errors, inherited consequences, missed corrections, and successful corrections. ECHO then counts shared downstream consequences once across responsible decisions and constrains rewards for repairing self-induced errors through source-funded recovery, producing bounded action-level supervision alongside terminal supervision. Experiments on six diverse tool-use benchmarks at both 4B and 8B scales show strong and consistent improvements over the compared baselines, with ECHO achieving the highest score on five of six benchmarks at each scale. These results support decision responsibility as a useful basis for fine-grained credit assignment in tool-use agents. Our code is available at this https URL.

---


### 349. [Backward Conformal Prediction under Covariate Shift](https://arxiv.org/abs/2610.16048)

**<font color=#1a73e8>作者：</font>** Amin Meghrazi, Yuanyuan Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Backward conformal prediction (BCP) fixes the size of a prediction set and estimates its miscoverage, but assumes calibration and test data are exchangeable. We extend BCP to covariate shift through importance weighting, preserving its guarantees when the density ratio is known. We show that BCP's tight miscoverage report depends only on the relative weight assigned to missed calibration examples, explaining why a better domain classifier can sometimes produce a worse estimate. Motivated by the fact that BCP depends only on nonconformity scores, we propose estimating density ratios on sorted score vectors rather than high-dimensional inputs. We prove that this approach recovers the same report asymptotically under an interpretable condition and characterize the resulting bias otherwise. Experiments with simulated and benchmark distribution shifts show that the proposed method improves BCP's miscoverage estimates, while score-based weighting consistently yields more accurate estimates than embedding-based weighting.

---


### 350. [From Failure Prediction to Component Selection in Semantic Segmentation](https://arxiv.org/abs/2610.16058)

**<font color=#1a73e8>作者：</font>** Minhui Kang, Yiyao Zhang, Peizhe Long 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable scene understanding requires deciding which predictions to trust, retain, or inspect. In semantic segmentation, component failure predictors support these decisions, but their predictive performance does not fully describe the value of the resulting selection. We develop a decision-centered evaluation framework that connects three questions: what an available score predicts, what can be learned from its existing fields, and what its ranking delivers. Across three segmentation systems on Cityscapes and ACDC at 90% retention, adapted MetaSeg reduces retained failure relative to forecast entropy in all twelve architecture-population comparisons, but does not establish a failure advantage over direct probability ranking. Image-nested source experiments reveal a different opportunity: reusing the full field set improves predictive and retained-loss performance under both learners in all three systems, while the raw OCRNet probe improves prediction with unresolved selective gains. Mapping a fixed prediction pair to conditional log-loss risk produces mixed selection effects, which we examine through the components exchanged by the two rankings. These findings distinguish the performance of a fitted score from the value obtainable from its inputs and the consequences of its use. The framework provides a practical basis for deciding whether to adopt an additional score, relearn existing fields, or revise a selection rule, and for explaining the gains and failures of component-level reliability methods.

---


> [!TIP]
> 当前位于：**301-350**（第 7/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
