# 📦 其他研究 | 2026年09月21日

> 本类共 **247** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-247**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-247**

---

### 201. [WeVisDoc: From Coverage to Capability for Robust End-to-End Document Parsing](https://arxiv.org/abs/2609.20423)

**<font color=#1a73e8>作者：</font>** Hao Yu, Kang Liu, Linnan Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Document parsing converts document images into structured content and requires reliable performance across diverse layouts and acquisition conditions. Yet training corpora are biased toward common document types and clean digital pages, while expanding coverage alone does not specify how to address a parser's remaining weaknesses. We present WeVisDoc, a two-stage data-centric framework for robust end-to-end document parsing. Stage I broadens semantic, structural, and appearance coverage through heterogeneous data and structure-preserving degradation synthesis. Stage II uses a held-out probe to measure the Stage I parser's residual errors within fixed visual-structural clusters. These diagnostics guide targeted data construction and reallocation of the target-token budget. WeVisDoc-4B achieves an Overall score of 95.38 on OmniDocBench v1.6 and a mean Overall score of 75.54 across the three PureDocBench tracks, ranking first among the compared end-to-end parsers in all four settings. Compared with Stage I, Stage II improves Overall scores for the 2B and 4B models on both benchmarks, with larger gains on the degraded PureDocBench tracks, including a 4.03-point gain for the 4B model on the Real Degraded track.

---


### 202. [When Do Language-Grounded Explanations Help? A Graph-Bottleneck for Farm Monitoring Interpretable Sheep Facial Pain](https://arxiv.org/abs/2609.20427)

**<font color=#1a73e8>作者：</font>** Alam Noor, Miguel Guti'errez Gait'an  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated pain recognition from facial expression could make continuous welfare assessment practical in sheep, but adoption depends on trust: a stockperson cannot act on a score that arrives without justification. We ground a model in the Sheep Pain Facial Expression Scale (SPFES) by letting each detected facial region attend over text embeddings of the clinical descriptors and then test whether the resulting explanations mean anything. They do not. Ablating an entire descriptor changes the predicted logit by about $10^{-4}$, and the most-attended cue agrees with the predicted pain level in only $32.6\%$ of regions, although the attention maps, the learned gate, and the generated text all proposed otherwise. We therefore remove the appearance bypass with a concept bottleneck whose classifier reads only SPFES concept scores, supervised by per-region state annotations that image-level pipelines discard. This costs $0.05$--$0.10$ in Cohen's $\kappa$ but yields concepts that are demonstrably learned: minority pain-indicating states are recovered at $3.5$--$8.3\times$ their base rates, and the ear and eye severity orderings emerge without severity supervision. Removing the supervision alone leaves $\kappa$ unchanged while concept accuracy falls to $0.109$, showing that architectural necessity does not imply semantic validity. We also show that pooled concept accuracy is misleading under clinical imbalance and provide a cross-validated, protocol-matched benchmark of seven methods on this dataset.

---


### 203. [The Organization of Inference: Information, Resource Constraints, and AI Production](https://arxiv.org/abs/2609.20449)

**<font color=#1a73e8>作者：</font>** Yukun Zhang, Kemu Xu, Yishen Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The economic value of inference depends on how capacity and task information are distributed across stages of AI production. We study these organizational margins using controlled workflow experiments on externally verified software-engineering tasks. In two matched resource panels, direct execution records the same success rate of 59.6 percent at logical-token ceilings of 12,000 and 24,000, while success under information-constrained planning rises from 36.2 to 51.2 percent. The planning disadvantage narrows by 15.0 percentage points (95 percent task-cluster bootstrap interval: 4.2 to 25.8). A strict read-only planning campaign varies whether the planner sees the task issue. At 12,000 tokens, issue access raises success by about 16 percentage points over issue-hidden planning. Compared with direct execution, task-informed planning is about 10 points lower at 12,000 tokens; at 24,000 tokens, it shows a 29.6-point advantage. In the resource panels, direct execution uses substantially less than either ceiling, while the planning workflow's binding rate falls from 46.2 to 0.8 percent and downstream execution accounts for 89.9 percent of the increase in total use. Scale determines the capacity available to a system; workflow and information structure shape the productive value

---


### 204. [Seismic Site Response Prediction from Sparse Observations Using Finite-Element-Pretrained Latent Dynamics](https://arxiv.org/abs/2609.20451)

**<font color=#1a73e8>作者：</font>** Yi Zhu, Su Chen, Xiaojun Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Numerical site-response predictions often deviate from observations, yet correcting these discrepancies is difficult because records are limited in both sensor coverage and number of events. This study proposes the Transfer-Enabled Forced Latent Autoencoder for Response Equations (FLARE-T) to improve these predictions by learning and calibrating low-dimensional latent dynamics that connect the base acceleration input to acceleration outputs at multiple depths. FLARE-T learns a low-dimensional response manifold and input-driven dynamics from dense finite-element simulations. It then trains a sparse encoder to map simulated sensor responses into the learned coordinates and uses limited records to calibrate the dynamics within them. A short response window initializes each prediction, while the complete base motion drives the response. The framework was evaluated using a layered-soil centrifuge test and the Lotung field vertical array. Test-set results show that FLARE-T improved multi-depth acceleration histories and 5%-damped pseudoacceleration response spectra relative to the original finite-element models, reducing errors at every evaluated sensor for motions of different intensities and, at Lotung, for both horizontal components. Two Lotung source models with different constitutive parameters achieved comparable test-set accuracy, indicating reduced dependence on precise prior calibration. FLARE-T therefore provides a data-efficient means of combining dense numerical response information with limited field records to improve future site-response predictions.

---


### 205. [Training Neural Networks to Approach the Optimum Bayes Estimator in Dense Multi-Emitter Localization](https://arxiv.org/abs/2609.20465)

**<font color=#1a73e8>作者：</font>** Yi Sun, Mona Sharifi, Muzna Yumman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We train neural networks on synthesized frames to approach the optimum Bayes estimator for dense emitter localization. The result justifies the future work on training neural networks to achieve high-throughput large-FOV super spatiotemporal resolution SMLM.

---


### 206. [Deep Learning-Based Classification of Cognitive and Resting States Using Electroencephalography Signals](https://arxiv.org/abs/2609.20467)

**<font color=#1a73e8>作者：</font>** K. A. Januka S. Fernando, Harshit Srivastava  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The categorization of cognitive and resting states derived from electroencephalography (EEG) signals is crucial for comprehending fluctuations in brain activity linked to various mental states. EEG provides a non-intrusive approach for documenting brain function in both resting and task-oriented cognitive conditions, whilst deep learning techniques enable the automatic extraction of significant patterns from intricate EEG data. This study presents a deep learning framework to distinguish between resting and cognitive states through EEG records. The proposed framework integrates a Convolutional Neural Network (CNN) stacked with a Gated Recurrent Unit (GRU) for the extraction of features from EEG signals. Time-frequency analysis is conducted to explore the salient aspects of signals, and the derived features are then assessed utilizing conventional deep learning and machine learning classifiers, including the suggested 2D-Net architecture. The proposed approach and feature extraction strategy outperform the evaluated comparative methods, achieving accuracies of 83.177% for resting-versus-mathematical task classification, 76.107% for resting-versus-memory task classification, and 83.432% for resting-versus-music task classification. The findings illustrate the efficacy of integrating signal processing with deep learning methodologies to discriminate resting from cognitive states utilizing EEG signals.

---


### 207. [SenseFuse: Label-Free Fusion of Image and Shape Encoders for Open-Vocabulary 3D Instance Segmentation](https://arxiv.org/abs/2609.20475)

**<font color=#1a73e8>作者：</font>** Euiseok Han, Tri Ton, Hwanhee Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary scene understanding is fundamental for robotics, laying the groundwork for spatial reasoning and object manipulation. While closed-vocabulary 3D instance segmentation heavily leverages 3D shape information, state-of-the-art open-vocabulary methods remain predominantly restricted to 2D image features or image-distilled representations during mask labeling. In this paper, we propose SenseFuse, a label-free fusion method that balances 2D image and 3D shape encoders for robust open-vocabulary 3D instance segmentation, refining only the mask-labeling stage of existing pipelines. We reveal that 2D image and 3D shape encoders exhibit largely disjoint failure patterns and rarely share identical wrong labels, whereas two 2D image encoders frequently repeat the same errors. This distinct behavior makes the 2D and 3D pair inherently complementary. We introduce an adaptive mechanism that selects a scene-level fusion weight to maximize a label-free sensitivity measure, estimated directly from a single scene's unlabeled proposals in milliseconds. SenseFuse improves labeling accuracy in every evaluated setting across ScanNet200, Replica, and ScanNet++, recovering 67-100% (median 93%) of the gain achievable with an oracle weight, and it raises instance AP in 21 of 22 reported settings. Code is available at this https URL.

---


### 208. [TeamCAMS: An Open-Source Research Platform for Studying Human Behaviour in Human-AI Teams](https://arxiv.org/abs/2609.20490)

**<font color=#1a73e8>作者：</font>** Amos Brocco, Alain Chavaillaz, Andreas Sonderegger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In this article, we present TeamCAMS (Cabin Air Management System), a collaborative work environment for simulating human-AI (artificial intelligence) interaction for scientific research. The article outlines how several psychological theories guided the development of this multiple-task simulation. Modelling a process control environment, previous versions of TeamCAMS have already been used in empirical studies to address a wide range of research questions (e.g., comparing different forms of automation, evaluating impact of automation reliability, effects of stress on multiple-task performance). Outlining the technical possibilities offered by TeamCAMS, the article points out how its latest version offers researchers the possibility of addressing a set of new research questions including problems associated with teamwork (e.g., within-team conflict, distributed teamwork) and human-AI interaction. Finally, we will outline how this simulation environment can be enhanced further still to address research questions in new fields (e.g., automation of leadership). To promote transparency, reproducibility, and further development, TeamCAMS is made available to the research community under an open-source license.

---


### 209. [Distributionally Robust Federated Learning with Multi-Source Data](https://arxiv.org/abs/2609.20501)

**<font color=#1a73e8>作者：</font>** Yingzhu Liu, Zhongkui Li, Pengcheng You 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning trains a shared model from private client data. In practice, data-generating distributions may differ, and the true mixture across clients is often unknown, making the underlying group distribution difficult to specify. Existing approaches address cross-client mixture uncertainty by optimizing against the worst-case mixture, yet assume accurate client-wise distribution estimates. However, these estimates can be unreliable when based on finite samples. To handle both cross-client mixture uncertainty and within-client distributional ambiguity, we construct a global ambiguity set as the union of admissible mixtures of local ambiguity sets. The construction allows client-specific ambiguity radii and admits a client-wise separable reformulation. Leveraging this structure, we establish a high-probability out-of-sample performance guarantee. We further develop a federated algorithm for a penalty-based reformulation and prove its convergence under milder regularity conditions. Simulations validate the algorithm's effectiveness.

---


### 210. [Radio Frequency Detection and Classification of Microplastics in Water](https://arxiv.org/abs/2609.20507)

**<font color=#1a73e8>作者：</font>** Jaden Tolbert, Md Saiful Islam, Pingshan Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Micro- and nano-plastic particles (MPs/NPs) are ubiquitous environmental contaminants whose increasing abundance and potential health impacts have created an urgent need for rapid, label-free detection methods. As particle size decreases to the low-micrometer range, conventional optical and spectroscopic techniques become increasingly challenging because of limited throughput and/or complex sample preparation. In this work, we present a machine learning (ML)-assisted radio-frequency (RF) dielectric spectroscopic cytometry (DiSC) platform for the label-free detection and classification of MPs. Eight types of $ 10 $ {\mu}m nominal-diameter MP particles suspended in deionized (DI) water were characterized at four frequencies spanning $ 0.2\text{-}9\text{ GHz} $. The measured alterations in RF scattering parameters (S-parameters), referenced to the carrier medium, were used to train supervised ML models for material classification, including the identification of MPs in mixed samples and saline-water environments. For eight MP classes suspended in DI water, the proposed method achieved macro-average F1-score, precision, and recall values exceeding $ 0.71 $. Furthermore, PET classification performance was largely maintained in saline carrier media containing $3.3\% $ and $ 6.6\% $ sea salt. These results demonstrate the feasibility of ML-assisted RF DiSC for rapid, single-particle MP classification in aqueous environments. Future work will focus on improving classification performance through enhanced RF calibration, increased spectral coverage, larger training datasets, and validation using environmentally aged and biologically contaminated microplastics.

---


### 211. [Grounded Product Understanding in Livestream Videos](https://arxiv.org/abs/2609.20508)

**<font color=#1a73e8>作者：</font>** Xinyu Zhang, Junjie Chen, Jiawei Ge 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> E-commerce livestreams have emerged as an important channel for presenting products to online consumers, containing multiple products whose information is scattered in different moments. This poses significant challenges for downstream product understanding applications, such as product-centric livestream clipping, where models need to identify the product and its relevant segments for information gathering. However, existing benchmarks for general product understanding typically evaluate product retrieval and temporal localization in isolation, leaving the critical correspondence between product identity and temporal evidence largely unassessed. To address this limitation, we introduce GPUB, a large-scale benchmark comprising 3,000 livestream instances with quality-controlled multi-moment temporal annotations and a catalog of over 31K fashion products. GPUB supports three evaluation tasks: the main task Grounded Product Understanding (GPrU) requires jointly identifying the target product and localizing its supporting moments from a livestream video and a candidate product set; Product Retrieval and Product Moment Localization serve as two complementary subtasks. Evaluation of existing multimodal models shows that GPrU remains highly challenging, with the best-performing baseline achieving only 10.13% Pair mAP@.3. To narrow the performance gap, we further develop UniPro, a unified product understanding model that derives product-aligned and temporally structured representations from shared multimodal encoding, improving Pair mAP@.3 to 21.53% while achieving 37.23% Joint R@1@.3 on GPrU.

---


### 212. [Automated Goldsmith's Mark Retrieval in Silverware](https://arxiv.org/abs/2609.20509)

**<font color=#1a73e8>作者：</font>** Atmik Tiwari, Vincent Christlein, Mark Fichtner 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> For art historians, goldsmith marks play a critical role in the identification and dating of artifacts. In practice, experts must manually compare a query mark against hundreds of documented examples, a process that is both tedious and highly dependent on specialist knowledge. To address this, we present an AI-assisted retrieval pipeline that combines mark localization with metric-learning fine-tuning across three backbone architectures: an ImageNet-pretrained ResNet-50, a supervised ViT-S/16, and a self-supervised DINOv2 ViT-S/14. We conduct a systematic evaluation of cropping strategies, where we measure the impact of no cropping, manual ground-truth cropping, and learned detection-based cropping, and assess their interaction with each backbone. Our strongest configuration, DINOv2 ViT-S/14 with manual crop and metric-learning fine-tuning, achieves an mAP of 62.63% and a Top-1 accuracy of 73.74%. Our experiments show that self-supervised pretraining and mark localization are the two most impactful factors, with learned cropping recovering the majority of the gain from manual cropping without requiring ground-truth annotations at inference time. To enable reproducibility and adoption in the digital humanities, we release our manually annotated dataset and codebase, and deploy the system via a public web interface.

---


### 213. [Refuse, Decompose, Refresh: A Claim-Safe Protocol for Closed-Loop AI Evaluation](https://arxiv.org/abs/2609.20538)

**<font color=#1a73e8>作者：</font>** Peiying Zhu, Sidi Chang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An AI evaluation can be perfectly reproducible and still support the wrong claim. This risk is acute in closed-loop systems: policy determines visited states, observable components, and which failures leave a measurable trace. We propose a claim-safe protocol with three actions. Refuse: abstain when a clean reference stream or matched runtime comparison lacks support. Decompose: report protocol execution, operational false admission, and structural hypotheses separately rather than as one PASS/FAIL label. Refresh: treat distribution-shift alarms as requests to invalidate and recompute a reference map, not as fault evidence. We instantiate the protocol in an aggregate-only simulator with 24 policy components, three demand regimes, two fault-mask families, and independent development and heldout seeds. The preregistered heldout contains 1,440 cases and 21,600 partition rows. Only 55/72 regime-component units were reference-admitted and 54/55 remained runtime-admitted, making abstention part of the result. Stable false admission was 0/20 represented components, with a one-sided exact 95% upper bound of 0.1391 under a frozen 0.20 rule. Within admitted units, affected clean traffic outpredicted nominal fault-cell fraction: across 540 unit-arm rows nested in 20 component clusters, the cell-minus-traffic negative-log-likelihood difference was 0.1264 nats per row, with a 95% component-cluster interval of [0.0593, 0.1918]. A drift log shows why "null" must be reference-relative: clean fault-null streams triggered 15/15, 0/15, and 14/15 alarms across three regimes, while only the middle regime matched the frozen detector reference. Rather than a universal threshold, we contribute an executable contract linking observable support, statistical calibration, and justified claims.

---


### 214. [Mitigating Retaliatory Algorithmic Collusion in Repeated Games](https://arxiv.org/abs/2609.20548)

**<font color=#1a73e8>作者：</font>** Karthik Sivachandran, Rohan Paleja  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning agents trained to maximize their own reward in repeated interactions can converge to supra-competitive outcomes resembling explicit collusion, without communication or shared design. Existing mitigation approaches are largely tied to specific economic settings, like two-sided platforms and auctions, leaving open how to design interventions for general repeated games. We address this gap by formalizing the connection between empirical observations from prior work on Q-learning collusion and classical theory of Simple Penal Codes (SPCs). We show any non-trivial SPC induces a quantifiable conditional dependence in agents' policies, detectable via the total variation distance between an agent's action distributions across cooperation and defection histories. Building on this connection, we propose CURB (Collusion Unwinding via Reward shaping and Belief injection), a reward-shaping framework that penalizes this Total Variation (TV) distance signal during Q-learning and is guaranteed to convert any SPC fixed point of the dynamics into a trivial one, thus precluding collusive equilibria sustained by punishment threats. Empirically, CURB substantially reduces collusion by Q-learning agents in both Bertrand and Cournot Competition Repeated Games. We further demonstrate that CURB extends to deep Q-network agents in Bertrand competition, suggesting the mechanism generalizes beyond tabular Q-learning.

---


### 215. [Empirical Analysis of Randomness Quality in Differential Privacy Mechanisms](https://arxiv.org/abs/2609.20561)

**<font color=#1a73e8>作者：</font>** Cesare Gerolimetto Fabrello, Valeria Rossi, Alberto Trombetta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Differential Privacy (DP) relies on carefully calibrated random noise to protect individual privacy in statistical analyses. While theoretical work has analyzed DP under weakened randomness assumptions, the practical consequences of entropy degradation remain poorly understood. We present a systematic empirical investigation of how randomness quality affects differential privacy mechanisms using IBM's DiffPrivLib. We introduce progressively degraded entropy sources characterized by established test suites, starting from high-quality quantum True Random Number Generators (TRNGs) and cryptographically secure Pseudo-Random Number Generators (PRNGs) down to systematically manipulated sources with controlled entropy degradation. Through repeated experiments over one million queries on a reference database and complementary statistical tests, we directly analyze empirical Privacy Loss Random Variable distributions. Our results demonstrate that DP mechanisms reliably detect deviations when approximately 1 bit in every 8 to 16 is manipulated, with detection sensitivity varying significantly between bit-level biases and temporal correlations. We demonstrate that statistical detection of distributional anomalies does not necessarily correspond to actual privacy guarantee violations.

---


### 216. [A Dual-Stream Regulated Reconstruction and Segmentation Network with Hierarchical Artifact-Prior Modeling for Ultra-Low-Field Pediatric Neuroimaging](https://arxiv.org/abs/2609.20562)

**<font color=#1a73e8>作者：</font>** Bahram Jafrasteh, Leo Milecki, Qingyu Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated quality assessment, enhancement, and segmentation of multiple structures in $0.064\,\mathrm{T}$ ultra-low-field pediatric MRI are limited by a low signal-to-noise ratio, weak anatomical boundaries, and frequent artifacts. We present a unified framework for the LISA 2026 Challenge that performs all three tasks together within one inference pipeline. A network with two coupled streams, built on a 3D U-Net, first reconstructs an enhanced uLF volume and then combines the original and enhanced images for subcortical segmentation. To improve boundary stability, we add an auxiliary class covering brain tissue outside the target structures, derived from whole brain masks. A head conditioned on an artifact graph predicts the seven artifact ratings from reconstruction residuals and frozen segmentation features. We address the scarcity of dense annotations using diffeomorphic registration from atlas to target for label propagation and to regularize anatomical reconstruction. We report validation results across all three tasks.

---


### 217. [Limits of Confidence in Diffusion](https://arxiv.org/abs/2609.20581)

**<font color=#1a73e8>作者：</font>** Russ Webb, Amitis Shidani, Alice Bizeul 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion, including remasking and uniform-state samplers, generate a sequence by writing multiple token positions per step, drawing each from a per-position distribution and choosing which positions to write from those same distributions. For domains of general interest (pixels, phonemes, or words) there are inherent dependencies between tokens. We show that a step matches the training distribution only when the positions it writes are conditionally independent given the tokens already fixed, that no product of per-position distributions can match a dependent group, and that per-position distributions do not determine whether a group is dependent: two joint distributions can have identical per-position marginals while differing in which combinations of values occur. On ScanAndAdd, a synthetic task whose joint distribution is available in closed form, we verify that every group of two or more undetermined positions a confidence ranking writes is dependent, and measure the generated distribution to be $29\times$ the sampling-noise floor total variation while per-sample metrics are $1.0$.

---


### 218. [RawSLAM: Online HDR Gaussian SLAM from Linear Radiance](https://arxiv.org/abs/2609.20589)

**<font color=#1a73e8>作者：</font>** Marina Orozco González, Luis Merino  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current dense visual SLAM systems rely almost exclusively on 8-bit tonemapped Low Dynamic Range (LDR) inputs, limiting their robustness in extreme lighting where shadows and highlights trigger tracking drift and mapping collapse. Conversely, existing raw and High Dynamic Range (HDR) reconstruction pipelines operate strictly offline. They depend on Structure-from-Motion preprocessing and are not suited for large inter-frame motion. We present, to the best of our knowledge, the first online Gaussian SLAM framework that tracks and maps directly on single-exposure 16-bit linear HDR imagery. Our method rests on three core components: an architecture-agnostic HDR Gaussian Splatting module featuring an MLP-free logarithmic parameterization of Gaussian color features; a Reinhard range-compressed photometric objective; and structure-guided spatial gradient weighting. Combined, these components allow our approach to outperform a direct HDR adaptation of MonoGS in both trajectory and reconstruction accuracy, while rendering natively in linear scene radiance for post-rendering processing. The same formulation runs unchanged on standard 8-bit inputs, roughly halving the MonoGS baseline error. Furthermore, our HDR Gaussian module transfers seamlessly to SplaTAM, Gaussian SLAM, and DROID-W, eliminating all tracking failures these systems suffer on challenging illumination sequences. To enable this research, we introduce RawSLAM: a dataset of 10 real-world indoor sequences featuring 16-bit RAW imagery, aligned depth, IMU measurements, and external OptiTrack poses. Code and dataset will be made publicly available soon.

---


### 219. [CrystalMO-TuRBO: Multi-Objective Trust-Region Bayesian Optimization for High-precision Joint Crystal Structure Refinement](https://arxiv.org/abs/2609.20592)

**<font color=#1a73e8>作者：</font>** Joseph Agada, Yishu Wang, Arpan Biswas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Crystal structure refinement is a fundamental inverse problem in materials characterization, where structural parameters are optimized to reproduce experimental diffraction data. Conventional approaches, such as least-squares and likelihood-based optimization, rely on local search and often struggle with non-convex, noisy, and highly correlated parameter landscapes, particularly when integrating multiple diffraction modalities. Joint refinement of X-ray and neutron data is especially challenging due to their complementary but competing sensitivities, which are typically combined through scalarized objectives requiring manual weighting and leading to suboptimal solutions. We propose CrystalMO-TuRBO, a multi-objective trust region Bayesian optimization architecture for joint crystal structure refinement. The method models X-ray and neutron discrepancies as separate objectives and transforms the problem into a normalized maximization setting. A two-phase optimization strategy is introduced: Phase 1 performs global exploration using parallel trust-region Bayesian optimization across multiple scalarizations to identify promising regions of the parameter space, while Phase 2 conducts localized refinement within a shrinking region to achieve high-precision solutions. This design explicitly separates global search from fine-grained optimization, addressing the unique accuracy requirements of refinement tasks. We evaluate the proposed method on experimentally collected X-ray and neutron diffraction data from single-crystal Ho2Ti2O7. Results demonstrate improved convergence, robustness, and parameter precision compared to classical refinement methods and Bayesian optimization baselines on refinement of a single-crystal pyrochlore material system.

---


### 220. [Recursive Quantum Long Short-Term Memory for Stable Short-Horizon Temperature Forecasting](https://arxiv.org/abs/2609.20594)

**<font color=#1a73e8>作者：</font>** Mu-En Lee, Yen-Ku Liu, Samuel Yen-Chi Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantum long short-term memory (QLSTM) models extend recurrent sequence learning with variational quantum circuits, but their optimization behavior can vary substantially across random initializations and temporal contexts. This paper evaluates a recursive QLSTM architecture against a standard QLSTM for one-step-ahead prediction of daily minimum and maximum temperature. Using daily weather observations from Toronto and identical training settings, we compare convergence, predictive accuracy, and generalization across input windows of 8, 16, and 32 days over 20 random seeds. The recursive model consistently reaches a near-optimal test loss earlier, reduces mean absolute error and root mean squared error, and exhibits a smaller generalization gap. These results indicate that recursive quantum feature transformations can improve stability and out-of-sample performance for compact hybrid quantum--classical temporal models.

---


### 221. [COIN-GP: Cooperative Online Learning in Networked Distributed Systems with Partial Measurements via Gaussian Process Regression](https://arxiv.org/abs/2609.20598)

**<font color=#1a73e8>作者：</font>** Zewen Yang, Xiaobing Dai, Zhenxiao Yin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we tackle the problem of jointly estimating the system states and partially unknown dynamics within distributed sensor-equipped networks, particularly in scenarios where only partial state observations are available. To address this issue, we propose an observer-based dynamic cooperative learning framework incorporating online distributed Gaussian Process (GP) regression, which enables accurate estimation despite incomplete in measurements and deficient GP models. In addition, a novel data collection strategy is introduced, with theoretical conditions ensuring feasible data acquisition. Moreover, we also derive an error upper bound encompassing state estimation and model estimation, leveraging the deterministic error bounds of GPs. Empirical simulations demonstrate the superiority of our approach compared to existing distributed GP-based methods.

---


### 222. [Weather Data Spoofing Attacks on Rain-Adaptive Millimeter-Wave Frequency Selection in V2X Communication Networks](https://arxiv.org/abs/2609.20601)

**<font color=#1a73e8>作者：</font>** Rasheed Bello, Idreez Yusuf, Justice Adjei Owusu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Connected vehicles use millimeter-wave (mmWave) sidelinks for the data rates cooperative driving demands, and emerging designs select the carrier band from sensed rainfall. We show that this weather awareness is an attack surface: an adversary who spoofs only the rainfall input dictates the victim's carrier frequency, and through it its communication range, without transmitting on the channel. We evaluate the attack in MilliCar, an ns-3 module that runs the selected band as the real 3GPP NR V2X carrier with per-band propagation, beamforming, and blockage. Forcing the band up to 73 GHz holds an eight-vehicle platoon's reliable range at 38 m while the honest baseline doubles it to 82 m; forcing it down to 5 GHz sustains 97% long-range reception but collapses the transport block to a third and quadruples long-range latency to 12.5 ms. We then implement the defense the mechanism implies. Rain loss grows linearly with distance while path loss grows logarithmically, so a receiver that tests measured SINR against the attenuation its reported weather predicts flags force-up with 98% probability within 1.5 s at a 1% false-alarm rate, and re-selection then restores long-range reception from 60% to 75%. The same test is structurally blind to force-down, because the 5 GHz fallback is nearly rain-immune. An advecting rain cell that swings the local rate from 15 to 81 mm/h leaves every result unchanged. Weather-aware band selection therefore requires an authenticated meteorological input; physical cross-checking covers one half of the threat.

---


### 223. [Inference-Engine Fingerprinting Attacks are Practical: Exploring Model-Driven Environmental Discovery, Exploitation, and Escape](https://arxiv.org/abs/2609.20614)

**<font color=#1a73e8>作者：</font>** Sarah Radway, Andrew Cheng, Vijay Janapa Reddi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Frontier AI models are rapidly gaining the ability to exploit vulnerabilities in complex pieces of software. The risk is not theoretical, as evidenced by recent sandbox escapes performed by frontier models at OpenAI and Anthropic. Discussions of how to sandbox inference stack components often focus on components other than the inference engine itself (e.g., network proxies or code execution environments). However, the inference engine is an attractive target for a misaligned model. For example, if a model can trigger exploits in that engine merely by generating specially-crafted output tokens, the model can initiate a multi-step, to-the-bare-metal exploit chain in the engine, without relying on vulnerabilities in other components of the inference stack, and without assistance from externally-provided, maliciously-crafted input tokens.
In this paper, we show that a misaligned model can perform inference engine fingerprinting to determine the specific engine (e.g., vLLM, SGLang) which executes the model. Once the engine has been fingerprinted, the model can leverage engine-specific exploits to take control of the engine using only carefully-selected output tokens. We provide concrete examples of model fingerprints in five popular engines, and demonstrate how realistic agentic harnesses allow a model to leverage those fingerprints to identify the local engine. We also describe a proof-of-concept, to-the-bare-metal exploit chain that originates from a fingerprinted (and subsequently compromised) inference engine. We conclude by discussing several ways that inference engines could be changed to make fingerprinting attacks more difficult.

---


### 224. [PhGS: Post-Hoc Pruning and Refinement of Single-View Feed-Forward 3D Gaussian Reconstructions](https://arxiv.org/abs/2609.20623)

**<font color=#1a73e8>作者：</font>** Rinto Yagawa, Han Cheng, Dieter Schmalstieg 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent single-view feed-forward 3D Gaussian Splatting (3DGS) generation predicts a fixed number of Gaussians per camera ray, introducing severe spatial redundancy. Most existing compaction strategies target multi-view setups to exploit cross-view consistency and are incompatible with single-image models. Instead of retraining the base feed-forward network to directly output compact representations, our insight is to keep the base models frozen and apply post-hoc pruning and recurrent refinement to the generated Gaussians. Consequently, we propose a backbone-agnostic compaction pipeline for single-view feed-forward 3DGS that couples an importance-score-based pruning mechanism with a trainable, lightweight recurrent refinement module, which iteratively updates the surviving primitives to restore image quality. Our results demonstrate seamless integration with existing baselines while preserving novel-view rendering fidelity and achieving high memory reduction. Furthermore, our method supports flexible inference-time keep ratios for application needs.

---


### 225. [Refinement Is Inherently Editable: Training-Free Prompt-to-Prompt Image Editing with Generative Refinement Network](https://arxiv.org/abs/2609.20633)

**<font color=#1a73e8>作者：</font>** Yulong Chen, Ziqian Zhang, Haoyu Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-guided image editing must introduce the requested changes while preserving unrelated source content. Diffusion-based editors rely on spatial controls whose inaccuracies can leave edits incomplete or alter unrelated regions. Causal autoregressive editors face a further constraint: their fixed decoding order limits revision of earlier decisions. We introduce RefineEdit, a training-free prompt-to-prompt image editing framework built on a Generative Refinement Network. Our key idea is to couple edit localization with content generation through the global refinement of binary image codes, allowing editing evidence to be reassessed as the image evolves. RefineEdit initializes an editing branch from an intermediate source state, reusing the emerging layout. We compare the probabilities assigned by the two branches to the same source-sampled bits, using their signed differences to select editable positions and bits. Selected bits follow editing refinement, while the remaining bits copy the evolving source state. To stabilize editing across refinement steps, adaptive spatial freezing limits unnecessary mask expansion, while finite bit locking keeps recently selected bits editable. The framework requires no additional training, external masks, or attention control. Across nine editing categories of PIE-Bench, RefineEdit achieves the best background-preservation scores in PSNR, LPIPS, MSE and SSIM, together with the highest whole-image and edited-region CLIP scores among the evaluated methods.

---


### 226. [PAA: The Probabilistic Allen Algebra: A Generative and Complete Probabilistic Extension of Allen's Interval Relations](https://arxiv.org/abs/2609.20634)

**<font color=#1a73e8>作者：</font>** Julian Eggert  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Allen's interval algebra is a qualitative calculus for temporal relations, but its thirteen base relations are crisp predicates over exact interval boundaries. This is inadequate for temporal information from language, perception, databases, or uncertain histories, where times, durations, and boundaries are uncertain and expressions such as "just before" or "roughly during" have graded meaning. We develop the probabilistic Allen algebra (PAA): a generative and complete extension in which relation probabilities are derived from distributions over interval boundaries rather than assigned as scores. Time points are Gaussian; intervals have Gaussian midpoints and truncated-Gaussian durations. Every relation is a boundary-ordering predicate in one common probability space: point-point relations reduce to error functions, and point-interval and interval-interval relations to multivariate Gaussian orthant probabilities induced by linear inequalities. Contact relations (meets, starts, finishes, equals) receive positive measure through a tolerance band, and under a single tolerance the thirteen relations form a true partition that recovers crisp Allen as the tolerance vanishes. The construction derives Allen's taxonomy rather than positing it: coarse predicates such as precedence, overlap, and containment are unions of leaves whose probabilities are leaf sums, and this hierarchy is preserved as intervals collapse to points and thirteen relations reduce to five and then three. Each relation further decomposes into correlation-aware temporal primitives in the spirit of CIDOC CRM. The algebra is scale-invariant and separates graded expressions such as "shortly before" from contact relations. All results are Monte-Carlo validated and shipped as an open, tested Python package.

---


### 227. [Stereotypically Yours: Portrayal and Perception of Race-Coded AI Companions](https://arxiv.org/abs/2609.20637)

**<font color=#1a73e8>作者：</font>** Wang Claire, Jiayue Melissa Shi, Agam Goyal 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI companions can purportedly adopt racial personas, raising questions about how they represent identity and how users interpret these portrayals. We combined an algorithmic audit of race-coded AI personas with interviews with 12 companion users who interacted with a probe. Our audit revealed systematic differences, such as Asian-coded male personas receiving higher submissiveness scores than White counterparts, and Black, Hispanic, and Indigenous male personas receiving higher aggression scores than their White counterparts in open-weight models. Interviews revealed that participants envisioned AI companions as offering cultural familiarity and outside perspectives, but differed in which portrayals they considered meaningful or stereotypical. Some rejected overt racial signaling while still expecting culturally distinctive responses. Triangulating these findings with theory, we highlight how social norms and cultural expectations complicate efforts to support meaningful racial representation without reproducing stereotypes. We discuss how companion personalization should be evaluated beyond user satisfaction to account for broader representational harms.

---


### 228. [PROVIA: Procedure State Tracking for Online Mistake Detection in Egocentric Videos](https://arxiv.org/abs/2609.20638)

**<font color=#1a73e8>作者：</font>** Di Wen, Kailun Yang, Jimmy Weissert 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An assistant watching egocentric video should notice a mistake from past frames alone, before the next step begins, and keep working once the person recovers. A mistake changes the state of the work, so every later step has to be read against what was done rather than against the plan. The first-mistake protocol that current online methods report on cuts each recording at its first mistake, so a fixed-time rule that never looks at the video is right on every case. We evaluate on complete trials, where mistakes and recoveries arise naturally, under a validation false-alarm budget and against controls that use timing alone. PROVIA keeps two records apart: a factual state, a learned summary of the steps each actor performed, mistakes included, and the accepted progress, an exact posterior over the state of an automaton induced from correct demonstrations by Bayesian state merging and over the execution status of each actor. Procedure-state transitions occur only in the correct-status branch; the mistake and correction branches retain the source state. A sequential test turns the per-frame mistake probability into alarms. With one filter and one optimization rule, PROVIA ranks mistakes best among the evaluated controlled baselines on CaptainCook4D, IndustReal, HoloAssist and IMPACT-ego. At a validation budget of 0.1 false alarms per minute it recalls .154 against .128 on CaptainCook4D and .034 against .015 on HoloAssist, where it leads at every budget. The pipeline runs at 58-70 frames per second. The source code is available at this https URL.

---


### 229. [Multi-center Medical Data Mining with FL-Net - A One-stop Shop for Federated Learning](https://arxiv.org/abs/2609.20650)

**<font color=#1a73e8>作者：</font>** Simon Süwer, Julian Klemm, Elisa Acitelli 等 41 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning enables collaborative training without sharing patient-level data, but most studies remain simulations. Based on five requirements derived from the literature, we analyzed 14 FL frameworks and found that none fully satisfied these requirements. We present FL-Net, a novel federated clinical research framework to fulfill all requirements. It integrates modular data harmonization, data discovery, disclosure control, securely built versioned FL-Net-Tools and containerized federated workflow execution into a persistent network. It enables the re-use of harmonized data and workflows across studies. FL-Net's end-to-end capabilities were evaluated through harmonization, cross-study patient discovery across MIMIC and US-130, and reproducible, audited federated workflows with up to 50 concurrent clients. FL-Net is being developed within the dAIbetes and Microb-AI-ome EU projects and will cover over 800,000 patients across 10 hospitals in 9 countries covering longitudinal and single point in time data, FL-Net provides a practical foundation for interoperable, reproducible, and privacy-preserving multicenter clinical research.

---


### 230. [Ownership in AI-Assisted Everyday Tasks](https://arxiv.org/abs/2609.20658)

**<font color=#1a73e8>作者：</font>** Megan Wei, Melanie Subbiah, Audrey Lee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When does work done with AI still feel like ours? As AI becomes woven into everyday tasks, we must examine what happens to our sense of ownership and contribution when a machine shares in producing what we make. We report an exploratory qualitative survey in which participants were asked to describe two recent, self-selected tasks completed with AI: one that felt like their own and one that did not. We find that felt ownership depends on the process of collaboration: people disown work when they merely approve AI's suggestions, but retain ownership when they lead, iterate, or rewrite. Ownership can also extend to settings where people own the vision for a project but not the execution; respondents reported high ownership on tasks they could not have completed without AI. Loss of personal voice and a lack of comprehension of the output both erode ownership. Finally, willingness to disclose AI use is often decoupled from actual pride or ownership, and instead shaped by community norms and fear of credit erasure. We propose several research directions as a result of these findings to promote AI development that supports people's sense of authorship over their own lives.

---


### 231. [Earth Surface Immune System for Rapid Monitoring of Unknown Anomalies](https://arxiv.org/abs/2609.20662)

**<font color=#1a73e8>作者：</font>** Jingtao Li, Qian Zhu, Xinyu Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Earth surface anomalies, driven by escalating climate change, and expanding human activities, are increasing in both frequency and diversity, yet their limited historical data and unpredictability make them fundamentally different from conventional remote sensing targets. Existing methods address specific anomaly categories or stop at localization, leaving a gap between detection and actionable information. Here we present ESIA, an Earth Surface Immune System whose architecture is constrained by three principles from the biological immune system, refined over millions of years against equally diverse and uncertain threats. A non-specific innate immune stage treats anomalies as unobserved changes in time-series satellite imagery, generating binary localization maps at 14.51 km2/s without assuming any anomaly category, surpassing the strongest general baseline by 37% in F1. A specific adaptive immune stage applies negative selection to filter text prompts and matches surviving prompts with localized image patches through a multi-modal foundation model, enabling open-vocabulary recognition of unknown anomaly attributes including category, affected area, and damage severity, with recognition F1 exceeding 80%. A mutation mechanism tunes minimal embeddings at test time, adapting to each scene in 3.26s using a single reference image pair. We validate ESIA on a global-scale dataset covering 19,801.60 km2 across six anomaly categories, comparing against 22 models, and further apply it to quantify degraded farmland in the Dnipro Delta following the Kakhovka Dam collapse and assess burn severity from 2025 Palisades Fire in Los Angeles. This unprecedented flexibility in handling unknown anomalies opens new avenues for real-time disaster response and environmental surveillance.

---


### 232. [FunArt: Decoding Functional Structure and Articulation from Generative 3D Latents](https://arxiv.org/abs/2609.20673)

**<font color=#1a73e8>作者：</font>** Dennis Rotondi, Abdelrhman Werby, Kai O. Arras  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> To operate effectively in human environments, robots must identify articulated objects, segment their movable and interactive parts, and estimate their kinematic models. Existing articulated scene representations typically recover kinematics from observed interactions, while methods operating on static scans often decouple articulation from functional interactive elements. We present FunArt, a framework that constructs articulation-aware functional 3D scene graphs from posed RGB-D observations captured in a single static configuration. FunArt reconstructs object instances, converts their fused geometry directly into the O-Voxel representation of TRELLIS.2, and exploits its frozen, sparse-compression VAE as a structural prior. A lightweight query-based decoder combines compact object-level latents with dense, surface-aligned features to jointly segment movable parts and functional interactive elements while estimating motion type, axis, origin, and range. On the Articulate3D dataset, FunArt achieves state-of-the-art performance across movable-part segmentation, articulation estimation, and functional-element segmentation, both with and without ground-truth object input. In the end-to-end setting, it outperforms the strongest baselines by 1.5 AP_{50} points for movable parts, 2.8 AP_{50} points under joint origin-and-axis constraints, and 6.7 AP_{50} points for functional elements. These results demonstrate that generative 3D latents encode actionable structural cues that can initialize robotic perception and planning before physical interaction.

---


### 233. [Epidemiological Causal Graph Identification: Challenges, Identifiability and Algorithms](https://arxiv.org/abs/2609.20676)

**<font color=#1a73e8>作者：</font>** Sambit Mishra, Yingying Wang, Christine K. Johnson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal discovery from observational data is fundamental to statistics and machine learning, yet determining causal direction without interventions necessitates structural assumptions. Existing identifiability research primarily focuses on continuous variables under additive noise models, often neglecting mixed datasets containing ordinal scales, counts, and continuous measurements. This paper investigates causal discovery in Directed Acyclic Graphs (DAGs) where nodes follow either an ordinal distribution (via an ordered logit model) or a regular one-parameter exponential family distribution. We prove that the edge direction between an ordinal and an exponential family node is distributionally identifiable for generic parameter values. Our findings generalize previous Ordinal-Poisson results to the broader exponential family. Computationally, we introduce a score-based exhaustive search and a masked continuous optimization framework using DAGMA for larger graphs. Numerical results validate the theory, recovering edge orientations within a Markov equivalence class that are unidentifiable under classical structural equation models.

---


### 234. [RISC-V and machine learning: a survey](https://arxiv.org/abs/2609.20677)

**<font color=#1a73e8>作者：</font>** Shriman Keshri, Apparna Singh, Chinmaya Kumar Palo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The intersection of open-source processor architectures and machine learning is driving the demand for customizable, efficient, and accessible hardware. This survey examines the state of the RISC-V ISA in machine learning applications, analyzing current capabilities, challenges, and future directions based on recent research. The analysis covers academic and commercial implementations, software frameworks, and real-world applications. The RISC-V machine learning ecosystem is evaluated, from instruction set extensions and core implementations to compiler optimizations and deployment strategies. Key contributions include a unified taxonomy of RISC-V ML implementations, a comparative analysis of performance and design trade-offs, an evaluation of software toolchain maturity, and the identification of emerging trends in instruction set extensions and specialized accelerators. Findings reveal progress in energy efficiency, specialized instruction development, and framework integration, while highlighting challenges in standardization, verification complexity, and ecosystem fragmentation. The analysis proposes four research directions to address current limitations: specialized neural processing extensions, adaptive and modular processor architectures, security frameworks, and energy-efficient multi-domain architectures. These directions provide a roadmap for advancing RISC-V as a foundational platform for next-generation machine learning systems.

---


### 235. [Should This Case Be Adapted? Prediction Fragmentation Controls Test-Time Adaptation](https://arxiv.org/abs/2609.20700)

**<font color=#1a73e8>作者：</font>** Lili Wang, Jing Li, Xiaowen Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Episodic test-time adaptation resets a frozen segmenter to source weights $M_0$ on each case and adapts for a fixed step count. A fixed horizon conflates a cohort-level question, how far to adapt, with an irreducibly per-case one, whether this case should be adapted at all. Cohort means hide that decision: on cross-vendor cardiac MRI the mean $\Delta$Dice from adaptation is statistically indistinguishable from zero while 58.7% of cases are individually made worse. We quantify this harm as harmful accepted area (HA), the harmful fraction of the edited area a controller deploys. Held-out tuning gives a stronger baseline than a fixed horizon, but the budget it selects transfers on neither of the two main medical benchmarks, and no global budget can condition on the case. We show that prediction fragmentation---the disagreement geometry between $M_0$ and the adapted mask $M_k$---predicts HA with no labels or extra backward passes at decision time, comparably on three benchmarks (Spearman $\rho$ 0.50--0.60), at a quarter of gradient-norm's latency. A case-level router built on it cuts HA from 0.228 to 0.139 on a benchmark that took no part in its design, with the design frozen and only cut-points recalibrated there. On the cardiac benchmark the design was selected on, the router cuts HA from 0.129 to 0.013 at matched Dice and 1.10 deployed updates, against the retrospective-best budget found post hoc on evaluation labels, and reduces that 58.7% to 20.0%, an upper bound we quantify. Where the retained cases are not net-helped (as on prostate), the router still cuts HA but concedes accuracy, a boundary we report. Thresholds are fit once on a labeled split disjoint from evaluation; decisions use no labels or gradients. The template ports across architecture and domain (nnU-Net$\to$SegFormer, Cityscapes$\to$ACDC) with coordinate, thresholds and per-bucket actions instantiated per domain.

---


### 236. [Ageing, Digital Literacy, and Interaction Modality in Immer-sive Virtual Reality: Psychomotor Performance, Cognitive Flexibility, and Their Processing-Speed Association](https://arxiv.org/abs/2609.20719)

**<font color=#1a73e8>作者：</font>** Panagiotis Kourtesis, Katerina Denaxa, Lydia Asimakopoulo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Extended reality (XR) increasingly supports training and cognitive assessment, yet the age sensitivity of its interaction techniques is unclear. This study examined age, digital literacy, and interaction modality as correlates of psychomotor and cognitive-flexibility performance in immersive virtual reality (VR). Two hundred and two adults (19-90 years) completed a five-mode Fitts' law task (eye-gaze, head-gaze, controller ray-casting, virtual finger, and controller direct touch), the Trail Making Test in VR (TMT-VR), and a digital-literacy questionnaire. Age was associated with slower task times across modes, but controller direct touch carried the steepest relative age gradient yet remained among the fastest in absolute terms; technique altered relative age sensitivity without determining absolute efficiency. Higher digital literacy was associated with faster TMT-VR completion but not Fitts task times. A Fitts-derived speed score predicted TMT-VR performance beyond age and partly accounted for its age association, consistent with shared processing-speed variance; an exploratory full-battery extension confined the Fitts-score association to completion-time and error-adjusted-time indices and the digital-literacy association to error-adjusted-time indices, not wrong-target errors, mean selection distance, or relative Part B indices. Age-inclusive XR assessment should standardise interaction modality, evaluate rather than exclude mid-air direct selection, and interpret cognitive scores alongside digital literacy and psychomotor speed.

---


### 237. [Calibrated RF-Fingerprinting Under Interference With Heterogeneous Transmission Protocols](https://arxiv.org/abs/2609.20765)

**<font color=#1a73e8>作者：</font>** Tariq Abdul-Quddoos, Xiangfang Li, Lijun Qian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Radio Frequency(RF)-Fingerprinting is a spectrum monitoring technique that identifies specific transmitters based on hardware impairments imprinted within the emitted signal. Although widely researched, studies almost exclusively consider scenarios where only one transmitter is emitting at a time, limiting real world applicability. In this work, we further the study of RF-Fingerprinting by considering co-channel interference, with multiple emitted signals interfering with each other, overlapping in time and frequency. Specifically, we formulate this problem as a multi-label classification problem and employ a 1D convolutional neural network (CNN). Furthermore, the models are calibrated such that the confidence thresholds for the label probabilities are derived, with guarantees on the upper bound on the average number of False Negatives, providing a degree of confidence in not missing a true spectrum policy violation. The proposed method is validated using real world data from the POWDER 5G testbed on devices transmitting 802.11a(Wi-Fi), 4G LTE, and 5G NR waveforms. The results show accuracy as high as 97% and as low as 73% after calibration depending on channel conditions. Also calibrating for various average false negatives upper bounds achieves micro recall scores of approximately (1 - calibrated false negatives) with the calibration robust to out-of-distribution interference, demonstrating the potential of the proposed method in a realistic high contention wireless environment

---


### 238. [Semantic Action Graph: A Shared Representation for Agent Grounding and Human Interpretation of Sports Highlights](https://arxiv.org/abs/2609.20768)

**<font color=#1a73e8>作者：</font>** Tica Lin, Deepak Chandran, Gauri Jagatap 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative agents are increasingly used to select and narrate video highlights, but they typically operate over unstructured or frame-level representations. Their output is consequently difficult for a viewer to verify and steer toward individual preferences. We present the semantic action graph, a lightweight domain schema that represents a sports match as performer, action, recipient, moment, and state nodes connected by role, temporal, and outcome edges. The schema demonstrates three key properties: 1) connected event sequences, 2) a shared, closed vocabulary, and 3) frame-addressable moments, making it suitable to serve two consumers at once: an agentic pipeline that composes narrated highlights, and a visual interface through which viewers query and inspect the same structure. We instantiate it in SportSAGE, a design probe pairing a four-module highlight pipeline with a graph interface, and report feedback from 12 soccer fans. Participants were satisfied with the quality of the generated highlights and narratives, and used the graph interface to search, navigate, and interpret the match highlights. These results provide early evidence that one small, human-readable schema can ground agent generation and support human interpretation at the same time.

---


### 239. [FlowSGS: Improving Flow Matching Priors for Inverse Imaging with Stochastic Interpolants](https://arxiv.org/abs/2609.20769)

**<font color=#1a73e8>作者：</font>** Tianao Li, Xinhui Qian, Emma Alexander  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow matching has emerged as the state-of-the-art generative model and has been used for plug-and-play (PnP) priors to solve inverse problems in computational imaging. However, existing flow-based inverse solvers assume linear forward models and/or make simplifying approximations in posterior sampling. To circumvent these problems, we introduce FlowSGS, a flow-based posterior sampling method using Split Gibbs Sampling (SGS) to decompose the posterior into a likelihood step and a prior step. Specifically, we sample from the likelihood step using Langevin dynamics and leverage the Stochastic Interpolants (SI) framework to integrate a pretrained flow model into the prior step. We provide a form for the prior step that uses SI's reverse-time SDE, and show connections to previous PnP methods. Moreover, with the aid of the flow prior's straight probability paths and a novel timestep correction technique for the reverse-time SDE, FlowSGS requires fewer network evaluations in its prior step than plug-and-play diffusion samplers. Our experiments show state-of-the-art performance on a range of inverse problems. For the first time, we provide an experiment on a nonlinear inverse problem (Fourier phase retrieval) for flow-based inverse solvers.

---


### 240. [The Data Hospital: A Workflow-Based Concept for Explainable Research Data Quality Assistance](https://arxiv.org/abs/2609.20782)

**<font color=#1a73e8>作者：</font>** Lennard Scheurer, Robert Porzel, Vinicius Carrillo Beber 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Research data quality is multidimensional and purpose-dependent: it emerges from the interplay of data, intended use, contextual knowledge, documentation, intervention decisions, and traceability. This concept paper presents the Data Hospital, a human-in-the-loop control and interaction model for research data quality. Using a hospital metaphor, datasets are admitted, contextualized, assessed, reviewed in specialized stations, modified only through approved interventions, validated, documented, and made replayable where interventions are sufficiently specified. The concept combines deterministic profiling and inspectable evidence with optional evidence-bound explanation by Dr. Data and explicit user decisions. Preserved Raw Data and controlled working states separate observation from intervention. The contribution is not a new cleaning or imputation algorithm, but a ten-stage workflow that makes assessability, uncertainty, intervention authority, provenance, and process reproducibility visible. The prototype is an implementation-backed demonstrator rather than a released research artifact and illustrates selected parts of the concept through representational standardization, imputation, Patient File documentation, and replay. The paper concludes with a staged agenda for subsequent technical and user-centered evaluation.

---


### 241. [PosteriorBench: From Point Estimates to Posterior Matching in Evaluating Generative Inverse Solvers](https://arxiv.org/abs/2609.20794)

**<font color=#1a73e8>作者：</font>** Jiachen Yao, Zi-Siang Hsu, Xi Deng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models are increasingly used to solve scientific inverse problems, but existing evaluations still focus primarily on whether a method can produce a single plausible reconstruction. This is insufficient for ill-posed problems, where multiple solutions may be consistent with the same sparse or noisy observations. In these settings, a method can achieve strong pointwise accuracy while still failing to capture the true posterior through mode collapse, overconfident uncertainty, or averaging incompatible solutions. We introduce PosteriorBench, a benchmark for evaluating the distributional accuracy of generative inverse solvers. PosteriorBench evaluates four physics-based inverse problems: Darcy flow inversion, Poisson source recovery, carbon capture and storage, and light transport material inference. For each task, we construct high-fidelity reference posteriors using computationally heavy but established procedures such as rejection sampling and Markov chain Monte Carlo, enabling direct assessment of whether solvers recover the full set of solutions rather than the single best sample. We pair these references with a five-metric posterior evaluation suite: posterior-mean error, posterior-standard-deviation error, maximum mean discrepancy, sliced Wasserstein distance, and radially averaged power-spectrum error. These metrics assess pointwise accuracy, marginal uncertainty, distributional alignment, and global frequency fidelity. The benchmark spans sparse sensing, low-resolution observations, nonlinear forward models, varying noise levels, and multimodal priors, with a unified pipeline for distribution matching and uncertainty quantification. Our experiments reveal substantial distribution-matching gaps across current solvers, while showing that neural operators improve resolution robustness, and guidance weights and generation noise are key to posterior-variance calibration.

---


### 242. [JEPA-Anything: Learning Predictive Models across Different Worlds](https://arxiv.org/abs/2609.20800)

**<font color=#1a73e8>作者：</font>** Taoyong Cui, Zhongyao Wang, Xinyue Xu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> World modeling enables intelligence to anticipate consequences, guide interventions, and learn from interaction. Yet predictive models remain domain-specific: can a common learning principle support world modeling across radically different systems? We introduce JEPA-Anything, a domain-agnostic framework based on orthogonal predictive factorization (OPF). Extending joint-embedding predictive architectures, OPF decomposes latent targets into complementary factors, learns them through dedicated pathways, and recombines them within a shared predictive design. We evaluate JEPA-Anything across seven domains: vision, biology, clinical trajectories, control, molecular dynamics, physical fields, and weather. Experiments span representation learning, intervention prediction, out-of-distribution generalization, and long-horizon dynamics, including 10 matched dynamics tasks, forecasting of over 1,000 clinical events, and 100-step molecular rollouts across four systems. Against matched JEPA baselines, JEPA-Anything improves reported metrics on all 10 dynamics tasks and reduces single-intervention prediction error on Interventional Pong by 34.8%. It achieves the lowest one-step and 100-step molecular errors among compared methods in all four systems. Beyond prediction, a factor-nominated biological intervention receives experimental support in cell co-cultures, patient-derived organoids, tumor fragments, and mice; latent orbital modes recover the Keplerian scaling exponent with a fitted slope of -1.4991. These results support a common factorized predictive principle across heterogeneous worlds, connecting world modeling with intervention and experimentally grounded scientific discovery. Code: this https URL

---


### 243. [Unifying Models of Intergroup Hostility in Online Discourse](https://arxiv.org/abs/2609.20808)

**<font color=#1a73e8>作者：</font>** Patrick Gerard, Julia Mendelsohn, Kristina Lerman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hostile rhetoric toward social groups can normalize exclusion and justify mistreatment, as well as contribute to rising polarization and political violence. Efforts to moderate hostile rhetoric in online speech draw on foundational theories in social and moral psychology, and political science. However, these theories were developed largely in parallel, often propose different and sometimes conflicting accounts of how hostility develops, and have rarely been tested against each other in real discourse. The result is a fragmented understanding of the rhetorical mechanisms of hostility, without a clear sense of how they appear, and relate to each other, in real-world discourse. Using 2.86 million posts from TikTok, Truth Social, and Twitter/X during the 2024 U.S. presidential election, we model the mechanisms of six foundational theories of intergroup hostility -- boundary construction, threat construction, scapegoating, negative evaluation, dehumanization, and action orientation -- within a common empirical framework to recover the broader organization of intergroup hostility rhetoric. Structurally, we find that boundary construction and threat construction anchor the system; temporally, we find that these mechanisms tend to follow a regular ordering: boundary construction, derogation, and action orientation tend to appear early; dehumanization and threat construction later; scapegoating latest. Mapping how these theoretical frameworks actually manifest in discourse bridges longstanding divisions across social science traditions and presents computational social science with a clearer empirical foundation for modeling intergroup hostility rhetoric beyond single-label detection.

---


### 244. [ERCPMP-Gx: Endoscopic Image and Video Dataset for Morphological, Histopathological, and Genomic Characterization of Colorectal Polyposis](https://arxiv.org/abs/2609.20815)

**<font color=#1a73e8>作者：</font>** Zahra Ghaffari, Massih Bahar, Mojgan Forootan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hereditary polyposis syndromes can be precursor lesions to colorectal cancer and are associated with a broad spectrum of extracolonic tumors. Early identification and accurate classification of these syndromes are essential for timely diagnosis, individualized patient management, and targeted surveillance strategies for affected families. However, public endoscopic datasets are largely organized around the individual sporadic polyp, and none links the polyposis phenotype to histopathology and germline findings at the patient level. Here, we present ERCPMP-Gx, an endoscopic, histopathological, and genomic dataset developed to support the application of artificial intelligence (AI) in the recognition, characterization, and classification of colorectal polyposis. Most procedures were performed using the Olympus EVIS X1 system with white-light endoscopy (WLE), narrow-band imaging (NBI), magnifying NBI (M-NBI), and NBI with near focus modes, yielding 160 images and accompanying video clips. Approximately eighty percent of cases represent clinically and/or genetically confirmed hereditary polyposis syndromes (PG), including familial adenomatous polyposis (FAP), Peutz-Jeghers syndrome (PJS), juvenile polyposis syndrome (JPS), and ganglioneuroma syndrome (GNS), while the remaining twenty percent comprise non-hereditary polyps and polyp-mimicking lesions with overlapping morphological features (Non-PG), included to support differential classification. Each released record is linked, where available, to standardized endoscopic annotations, representative histopathology, and clinically reported germline findings, forming an AI-ready, patient-level annotation framework. The dataset is publicly accessible at Mendeley (this https URL). For the latest updates and further information, readers are referred to the DataBioX website: this https URL.

---


### 245. [FAMOS: Feed-Forward 3D Articulation Modeling from Sparse Observations](https://arxiv.org/abs/2609.20817)

**<font color=#1a73e8>作者：</font>** Kevin Qu, Tao Sun, Massimiliano Viola 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modeling articulated objects from sparse monocular views is challenging because each observation reveals only partial geometry and motion evidence. Most feed-forward methods infer articulation from a single observation and therefore rely heavily on learned category-level shape priors. We present FAMOS, a feed-forward model that predicts movable-part segmentation and joint parameters from a sparse, unordered set of partial point clouds. Our model jointly reasons over multiple observations and naturally supports a variable number of inputs, including a single view. To aggregate articulation cues across observations, we introduce a Multi-state Articulation Transformer with alternating state-wise and global attention. We further propose an observed articulation span objective that supervises the motion range each part exhibits across the input observations, encouraging the model to leverage the full observation set. To overcome the limited scale and diversity of existing datasets, we introduce a procedural data generator that synthesizes self-annotated assets during training. Experiments on PartNet-Mobility, ACD, and ArtiCraft-10K demonstrate consistent improvements over both feed-forward and optimization-based baselines. Project page: this https URL

---


### 246. [SplashSplat: Reconstructing Splashing Liquids from Real-World Multi-View Videos](https://arxiv.org/abs/2609.20818)

**<font color=#1a73e8>作者：</font>** Peiyu Liu, Dingxi Zhang, Federico Tombari 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A splash lives for a fraction of a second: sheets tear into ligaments and droplets, appearance is view-dependent and nearly textureless, and little persists long enough to track. Reconstruction research has consequently focused on smoke, synthetic liquids, or gently deforming surfaces. To our knowledge, no synchronized multi-view dataset of splashing liquids exists. We therefore introduce a benchmark of 20 real scenes, from coherent streams to violent splashes, captured by seven synchronized, calibrated 4K cameras at 60 fps, with manually refined per-view liquid and container masks and fixed evaluation splits. We further present SplashSplat, built on a single principle: impose physical structure only where the observations can constrain it. Per-frame liquid SDFs fused from the masks provide the geometry, level-set transport between consecutive SDFs yields a coarse velocity field, and Lagrangian carriers advected along this flow, corrected against each new observation and reseeded where coverage is lost, decode local Gaussians for differentiable rendering. SplashSplat outperforms state-of-the-art dynamic Gaussian splatting methods on our real captures and on a synthetic benchmark, with physically more plausible motion and a lower training cost. The same representation supports temporal interpolation and style transfer without re-optimization.

---


### 247. [Embedding Models Measure in Peculiar Ways](https://arxiv.org/abs/2609.20821)

**<font color=#1a73e8>作者：</font>** Juri Opitz, Andrianos Michail  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Embedding spaces define notions of semantic similarity and distance. We study whether those embeddings reflect physical measurements of mass, distance, time and volume, which admit a unique, objective notion of semantic equivalence and distance. We find that physical measurement is only weakly modeled in the embedding space, and that instead quite peculiar measurement patterns can be observed. Further analysis indicates that embedding representations of physical measurements are strongly influenced by superficial string similarity, and recalibration of similarity does not substantially improve the alignment.

---


> [!TIP]
> 当前位于：**201-247**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-247**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
