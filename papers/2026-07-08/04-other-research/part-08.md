# 📦 其他研究 | 2026年07月08日

> 本类共 **571** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-400**（第 8/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

---

### 351. [Wan-Streamer v0.2: Higher Resolution, Same Latency](https://arxiv.org/abs/2607.04443)

**<font color=#1a73e8>作者：</font>** Lianghua Huang, Zhi-Fan Wu, Yupeng Shi 等 26 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Wan-Streamer v0.2, a latency-preserving upgrade of the native-streaming, end-to-end audio-visual interaction model. v0.2 keeps the v0.1 modeling formulation, but raises the interactive output stream from 192x336 to 640x368 while preserving approximately 200 ms model-side signal-to-signal latency at 25 FPS. The higher-resolution stream supports scene-grounded mid-shot agents whose posture, gaze, hands, nearby objects, and local scene layout remain legible during real-time conversation. To support the larger visual stream without adding user-visible delay, v0.2 keeps the thinker as a single-GPU low-latency path for streaming perception, the short language/state Transformer pass that builds the generation cache, and final decoding. The performer becomes a multi-GPU Ulysses-style context-parallel group for the expensive next-unit latent generation. Each performer rank writes incoming K/V into a pre-sharded local cache. The long high-resolution latent video sequence is split across ranks for denoising and gathered through Ulysses communication, while the much shorter audio latent sequence is generated without sequence sharding. In this split, the thinker's language/state computation reaches the performer only as K/V conditioning, so no separate language sequence has to be communicated inside the performer group. This concentrates additional hardware on visual generation while preserving the compact thinker-performer boundary, keeping total remote interaction latency at approximately 550 ms when a 350 ms bidirectional network budget is included.

---


### 352. [Knowledge-Informed Local Causal Discovery of Optimal Adjustment Sets](https://arxiv.org/abs/2607.04447)

**<font color=#1a73e8>作者：</font>** Seong Woo Ahn, Alessandro Leite, José Lucas De Melo Costa 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Local causal discovery is a scalable alternative to global structure learning. However, it can struggle to identify valid adjustment sets in data-scarce settings because of finite-sample uncertainty, incomplete local neighborhoods, and unresolved Markov equivalence. Although many application domains provide structured background knowledge, its integration into local causal discovery remains limited. We propose b-LOAD, a knowledge-informed extension of the LOAD algorithm for local discovery of optimal adjustment sets. b-LOAD incorporates prior edge constraints directly into the local structure-learning procedure and uses Meek's rules to expand the discovery frontier dynamically, yielding a knowledge-constrained partially directed graph over the relevant local subgraph. This strategy helps prevent structurally relevant nodes introduced by prior knowledge from being excluded by local search. We prove that, under sound background knowledge, the procedure monotonically refines the admissible equivalence class and can enlarge the set of identifiable causal queries, enabling recovery of optimal adjustment sets that are not identifiable from observational conditional-independence information alone. Empirically, b-LOAD improves downstream causal effect estimation relative to purely data-driven and standard knowledge-augmented baselines, particularly in data-scarce and structurally complex regimes. Results on real-world biological networks show that locally targeted prior knowledge provides the largest gains and remains beneficial under moderate structural noise. These findings position b-LOAD as a scalable approach for converting fragmented domain knowledge into more reliable causal-effect estimation.

---


### 353. [Fields of the Planet: Field Boundary Mapping Beyond 10m](https://arxiv.org/abs/2607.04449)

**<font color=#1a73e8>作者：</font>** Isaac Corley, Caleb Robinson, Jennifer Marcus 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Field-boundary maps support crop monitoring, irrigation planning, and yield estimation, but many smallholder parcels span only a few 10 m Sentinel-2 pixels. We introduce Fields of the Planet (FTP), a 3 m PlanetScope companion to Fields of The World (FTW) that pairs the same polygons, seasonal windows, and train/test splits with 133,168 co-registered PlanetScope patch-window targets across 24 countries. FTP evaluates field delineation as parcel recovery by vectorizing predictions before scoring panoptic quality (PQ), object F1, size-stratified PQ, and meter-scale matched-boundary error. Under matched architectures and training recipes, 3 m imagery raises PQ from 21.0 to 35.5, raises PQ on sub-0.5 ha fields from 5.8 to 15.7, and cuts matched-boundary error from 18.6 m to 7.4 m.

---


### 354. [A Deep Learning-based surrogate model for Severe Accidents in nuclear reactors using ASTEC](https://arxiv.org/abs/2607.04450)

**<font color=#1a73e8>作者：</font>** Alessandro Longhi, Danny Lathouwers, Zoltán Perkó  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Integral codes like the Accident Source Term Evaluation Code (ASTEC) are powerful tools to study the physics of Severe Accidents (SAs) in nuclear reactors. Real time SA simulators can also be helpful in training operators of nuclear plants to react correctly to malfunctions. However, SA simulators can take up to several days per simulation, making their use infeasible for real time applications. In this work we show how to speed up a SA simulator with a fast, Deep Learning based (DL), surrogate model (SM). The SM is built as a combination of a dimensionality reduction stage, via an AutoEncoder, and a time-stepping stage, via a Neural Ordinary Differential Equation. The data on which the SM is trained are obtained from the ASTEC simulator, by sampling a set of operator actions for station blackout (SBO) and loss-of-coolant accidents (LOCA). The objective of the developed SM is to approximate multiple spatio-temporal fields for the thermal-hydraulic physics, core degradation, and fission product release modules in ASTEC's vessel domain. The SM predicts simultaneously around $80$ different physical variables (both scalar and fields), maintaining a stable autoregressive rollout up to $50$ thousand time steps. In addition, the AutoEncoder achieves a dimensionality reduction by a factor of over $300$, which allows the SM to predict up to $40$ hours of simulation in under a minute, both on CPU and GPU. This work is the first study of the capabilities and limits of DL based surrogate modeling in approximating the challenging, highly non-linear physics of ASTEC.

---


### 355. [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)

**<font color=#1a73e8>作者：</font>** Ke Li, Kaidi Liang, Yuxin Ding 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment. However, generating controllable safety-critical scenarios remains challenging. Existing approaches use soft guidance that provides only probabilistic preferences and cannot guarantee the satisfaction of geometric and severity constraints associated with specific collision types. We introduce Collision-Constrained Flow Matching (CCFM), a novel framework that guarantees precise collision control through hard physical constraints. CCFM consists of three key components: (i) a heuristic collision selector that optimally identifies an adversarial agent and collision type via composite scoring; (ii) structured hard constraints that explicitly define four collision types (rear-end, side, cut-in, head-on) through contact point, heading, and severity requirements; and (iii) a collision-constrained flow matching sampler that enforces the constraints via Gauss-Newton manifold projection. CCFM achieves collision rate up to 46.4% on nuScenes and 83.1% on nuPlan, significantly outperforming baselines while preserving realistic driving behavior. By enabling controllable collision characteristics in safety-critical scenario generation, CCFM provides a reliable foundation for AV safety evaluation and sim-to-real crash data generation. The code and implementation details are available at this https URL.

---


### 356. [Spatial Graph Representation and Morphometric Analysis of the Pulmonary Vascular Tree From Computed Tomography Using Multi-Scale Hessian-Based Filter Fusion and TEASAR Skeletonization](https://arxiv.org/abs/2607.04457)

**<font color=#1a73e8>作者：</font>** Piotr Mackiewicz, Jakub Kołyska, Radoslaw Roszczyk  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing the pulmonary vascular tree from computed tomography (CT) images is essential for quantitative lung analysis, vascular morphology assessment, and patient-specific modeling, yet it remains challenging because vessels span multiple scales, from proximal arteries to distal microvasculature. Clinical chest CT is further affected by limited spatial resolution, partial volume effects, heterogeneous image quality, and respiratory motion artifacts. Unlike deep learning-based pulmonary vessel segmentation methods that require large annotated datasets, we propose a deterministic, training-free, and explainable pipeline for CT-based pulmonary vascular tree reconstruction. The method fuses multiscale Hessian-based Frangi and Sato vesselness filters using a weighted maximum response across 12 spatial scales from 1 to 8 mm, enabling detection of large pulmonary arteries and peripheral branches. Lung parenchyma is segmented by Hounsfield unit thresholding, morphological post-processing, and Chan-Vese active contour refinement. Vascular centerlines are extracted using the Kimimaro implementation of the TEASAR algorithm; separate left- and right-lung vascular graphs are then constructed, pruned, and verified for acyclicity. Geometric plausibility is assessed using volumetric fractal dimension, Strahler order analysis, Horton ratios, and Murray's law. The resulting fractal dimension of approximately 2.3 is consistent with reported values for the human pulmonary vasculature. At the same time, residual deviations in branching metrics reflect distal-vessel truncation caused by finite CT resolution. These results indicate that the proposed explainable pipeline can generate geometrically plausible pulmonary vascular tree models and may support quantitative pulmonary imaging, vascular morphometry, and computational lung modeling.

---


### 357. [Flash-BoN: Instant Drafts for Inference-Time Scaling in Diffusion Models](https://arxiv.org/abs/2607.04461)

**<font color=#1a73e8>作者：</font>** Ruchit Rawal, Reza Shirkavand, Sayak Paul 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inference-time scaling for text-to-image generation has progressed from simple Best-of-$N$ (BoN) sampling to guided search methods that verify and steer candidate trajectories at intermediate denoising steps. These approaches focus on when and how often to verify during denoising but largely treat the cost of generation itself as fixed. Moreover, the standard practice of comparing methods by number of function evaluations (NFEs) counts only denoising forward passes and ignores verifier overhead, which can distort efficiency rankings. We show that under wall-clock evaluation, simple BoN already matches or outperforms several guided search techniques, suggesting that compute is better spent on broader exploration than on repeated intermediate verification. This motivates Flash-BoN, which generates a large pool of inexpensive draft candidates by combining three complementary acceleration knobs: timestep truncation, layer skipping, and activation proxies into a single configuration optimized once per model. An efficient multi-stage verification procedure then identifies the most promising draft, which is refined at full quality. Across three benchmarks and three model scales, Flash-BoN consistently outperforms all baselines under fixed wall-clock budgets, with gains that grow at larger model scales (+8% AUC). We further show that our strategy combines well and improves existing orthogonal techniques such as reflection-based prompt optimization (+16% AUC). The gains correlate with increased candidate diversity, which also enables draft-guided selection to accelerate RL post-training convergence.

---


### 358. [AMRM-Pure: Semantic-Preserving Adversarial Purification](https://arxiv.org/abs/2607.04474)

**<font color=#1a73e8>作者：</font>** Zhihao Dou, Zhiqiang Gao, Dongfei Cui 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Adversarial purification is a defense technique that employs generative models to remove adversarial perturbations. Current methods often rely on powerful generators, typically diffusion models, and focus on reducing the gap between adversarial and clean samples in the feature space, while overlooking semantic correlation within a single sample. To address this issue, we explore adversarial purification from the perspective of preserving semantic relationships among image patches. We employ an Attentive Mask Reconstruction Model (AMRM), which shows superior performance. Our theoretical and experimental analysis reveals that AMRM is highly sensitive to adversarial noise, as such noise significantly distorts patch relationships. Based on this observation, we propose AMRM-Pure, a purification framework that denoises adversarial inputs by preserving patch-level semantics, and formulate this process as a tractable optimization problem with respect to the input. To further enhance robustness, we finetune AMRM-Pure with classification loss to strengthen semantic consistency. We apply our insight to two AMRM architectures, including Mask Autoencoder (MAE) and MaskDiT. Extensive experiments confirm the effectiveness of our method, establishing new state-of-the-art performance across multiple benchmarks.

---


### 359. [PulmoSight-XAI: An Explainable Multi-View Attention Ensemble with Gradient Boosting Meta-Learning for Multi-Label Chest X-Ray Classification](https://arxiv.org/abs/2607.04478)

**<font color=#1a73e8>作者：</font>** Moshiur Rahman, Shafqat Alam, Tasnia Binte Mamun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated chest X-ray classification remains challenging due to severe class imbalance, co-occurring pathologies, and the loss of localized features in conventional architectures. To address these, we propose an explainable hierarchical multi-view ensemble framework for the robust classification of 14 thoracic pathologies. The framework employs view-specific training by independently modeling frontal and lateral radiographs using an ensemble of five complementary convolutional neural networks. Replacing global average pooling, a multi-scale feature fusion strategy augmented with Convolutional Block Attention Modules (CBAM) preserves fine-grained intermediate representations while emphasizing high-level pathology-specific semantic features. To mitigate positive-negative imbalance and varying inter-class difficulty, models are optimized using a novel hybrid objective combining Asymmetric Loss with Adaptive Focal Loss. Beyond simple probability averaging, the framework incorporates a hierarchical meta-learning strategy where test-time augmentation (TTA) predictions and cross-model uncertainty measures are integrated into Level-1 gradient-boosting meta-learners (XGBoost, LightGBM, and CatBoost), followed by Level-2 stacking with optimized alpha blending. Evaluated on a large-scale CheXpert-style dataset, the framework achieves state-of-the-art macro-average AUROC scores of 0.9319 for frontal and 0.9154 for lateral radiographs. Furthermore, comprehensive explainability analysis using seven post-hoc attribution techniques demonstrates strong anatomical consistency and clinically meaningful decision localization. By integrating architectural diversity, multi-scale attention, hierarchical meta-learning, and rigorous explainability, the proposed framework provides a transparent, highly accurate, and clinically practical computer-aided diagnosis system for thoracic disease classification.

---


### 360. [LeukocyteCount: Automatic Identification and Counting for leukocytes using Deep Learning](https://arxiv.org/abs/2607.04486)

**<font color=#1a73e8>作者：</font>** Ahmed M. Sayed, Sondos A. Refaat, Abdallah M. Mostafa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diagnosing and monitoring diseases frequently involves the analysis of human biological samples, with blood analysis being pivotal. Specifically, leukocytes, or white blood cells (WBCs), are essential markers for evaluating the body's defense mechanisms against infections. Traditional methods for WBC counting and classification are labor-intensive and prone to inaccuracies, primarily due to human error. The conventional processes for blood cell analysis, especially those concerning WBCs, are beset with difficulties. These include the laborious nature of manual counting and the susceptibility to errors, which can significantly impact the accuracy and reliability of disease diagnosis and monitoring. This study proposes an automated, machine learning-based solution aimed at mitigating the identified challenges. By employing a hybrid model that integrates Yolov5 for the detection of WBCs, coupled with a finely tuned, pre-trained MobileNetV2 model and a Logistic Regression classifier, the study innovates in the accurate identification, counting, and classification of WBCs into four distinct types. The methodology leverages the BCCD dataset for training and validation purposes. The application of the proposed hybrid machine learning model has yielded remarkable results, demonstrating a detection accuracy rate of 98\% through the Yolov5 stage, and an unparalleled classification accuracy of 99.04\% in subsequent stages utilizing MobileNetV2 and Logistic Regression. Additionally, Our proposed YOLOv5-based RBC detection module achieves an F1 score of 99.73\%, which outperforms the baseline. These findings underscore the model's potential in transforming traditional laboratory practices for WBC analysis, offering a path towards more accurate, efficient, and reliable disease diagnostics and monitoring.

---


### 361. [Two Black Boxes, One Solver: Encoder Probing and Decoder Attribution for Neural Multi-Attribute VRP under Hard-Mask and Recourse Decoders](https://arxiv.org/abs/2607.04487)

**<font color=#1a73e8>作者：</font>** Sohaib Afifi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural autoregressive solvers for the Multi-Attribute Vehicle Routing Problem (MAVRP) reach competitive cost but offer no per-step justification, a problem when dispatchers must validate, accept, or compare them. We open two complementary black boxes in one protocol. On the encoder side, linear probes, spontaneous-organization metrics, rank-based richness measures, and discovered-direction analyses with intervention validation characterize how the latent represents constraint families at the graph, node, and edge level. On the decoder side, three attribution methods (gradient, integrated gradients, DeepLIFT) feed three reading angles: abductive, contrastive against the best feasible alternative, and counterfactual (smallest input change that switches the action or restores feasibility). Explanations are scored on fidelity, concentration, stability, sanity, and actionability. Across six variants combining three encoders (Attention baseline, Unimp, UnimpMoe) with two decoders (Hard-Mask, Recourse), we find that graph inductive bias improves both representational predictability and decoder sanity, that the Mixture-of-Experts encoder represents constraints in a distributed rather than axis-aligned way, and that the Recourse training regime, not merely its softer mask, produces policies that represent infeasibility usefully, exposing make-feasible counterfactuals that Hard-Mask policies fail to produce even when fed infeasible alternatives externally.

---


### 362. [Enhancing Facial Expression Recognition in Head-Mounted Displays with Synthetic Data](https://arxiv.org/abs/2607.04490)

**<font color=#1a73e8>作者：</font>** Jianing Deng, Qiang Zhou, Jingtong Hu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial expression recognition (FER) is crucial for social interaction in mixed reality environments that employ head-mounted displays (HMD). However, collecting FER data from head-mounted cameras (HMC) is challenging due to privacy concerns and the diversity of HMD platforms. Moreover, existing FER datasets are not directly applicable due to the unique perspectives of HMCs. The lack of sufficient data hinders the development of neural network-based HMC FER methods. To address data scarcity, we propose a data synthesis framework that generates HMC-view images from frontal-view images, leveraging abundant existing annotated datasets. Specifically, we first reconstruct 3D textured meshes from images and then apply a configurable camera system to render images from the HMC perspective. Additionally, we introduce a texture-space alignment network (TSAN) that enables accurate texture sampling from images to preserve detailed facial expressions. To evaluate the proposed method, we conduct extensive experiments on both simulated and real HMC datasets. Experimental results demonstrate that models trained on our synthetic dataset outperform those trained on existing datasets and exhibit better generalization across different camera configurations.

---


### 363. [UniSkip-Mamba: A Frequency-Aware State Space Model for Audio-Visual Temporal Forgery Localization](https://arxiv.org/abs/2607.04498)

**<font color=#1a73e8>作者：</font>** Cangjin Qiu, Quan Zhang, Dan Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the proliferation of AI-generated content, sophisticated multimedia manipulation has raised critical concerns about malicious applications such as opinion manipulation and evidence fabrication, making Audio-Visual Temporal Forgery Localization (AV-TFL) an urgent research frontier. Existing TFL methods have progressed along two main paradigms: Transformer-based temporal modeling and channel-wise multimodal fusion. While these approaches capture temporal dependencies and cross-modal correlations, they process all frequency components indiscriminately, leading to overfitting on high-frequency noise and limited robustness under real-world data degradation. Through systematic frequency domain analysis, we find that forgery-discriminative patterns concentrate in the low/mid-frequency range (normalized frequency 0-0.15), while high-frequency components primarily introduce noise, removing them even improves detection performance by +1.4%. Based on this phenomenon, we propose UniSkip-Mamba, a frequency-aware State Space Model framework that incorporates Unified Multimodal Sequence Fusion to preserve cross-modal phase relationships, and Skip-Scanning Mamba Blocks that implement frequency-aware regularization through a novel Group-Scan-Merge mechanism, naturally biasing learning toward discriminative low/mid-frequency patterns (0-0.15) while maintaining representational completeness. We achieve state-of-the-art (SOTA) performance: 63.4% AP@0.95 on LAV-DF (+9.8% improvement) and 63.58% mAP on AV-Deepfake1M (+14.32% improvement), with 6x faster inference. Our frequency-domain analysis provides theoretical justification from a signal processing perspective for why skip-scanning inherently improves both accuracy and robustness.

---


### 364. [From Interaction to Intent: Inferring User Objectives from Provenance Logs](https://arxiv.org/abs/2607.04501)

**<font color=#1a73e8>作者：</font>** Steffen Holter, Tobias Stähle, Arpit Narechania 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The ability to automatically infer analytic intent from user interaction histories could enable interactive AI systems to proactively assist users during exploratory data analysis. In this paper, we examine whether provenance logs -- detailed records capturing sequences and timing of user interactions -- can be used to classify user intentions in visual exploration tasks. To investigate this, we record how participants interact with multiple multidimensional data projections across a range of analytic tasks, capturing fine-grained mouse interaction data throughout each session. We find that distinct behavioral signatures emerge across different analytic objectives. For instance, users examining properties of specific clusters exhibit markedly different interaction patterns compared to those searching for outliers. More importantly, we show that embedding contextual information into interaction provenance enables classifiers to predict user objectives that generalize across datasets and projection methods. These findings demonstrate that low-level interaction data can serve as a practical bridge to high-level analytic intent, contributing to the development of intent-aware visualization systems.

---


### 365. [Why Pure Reasoning is Not Enough: Nature as the Source of Mathematical Innovation](https://arxiv.org/abs/2607.04505)

**<font color=#1a73e8>作者：</font>** Charanjit S. Jutla, Vimal Sharma  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We advance the hypothesis that human mathematical reasoning, constrained by both the undecidability and the computational intractability of even modest logical fragments, relies fundamentally on pattern matching from domains external to pure deduction. The most prolific reservoir of such patterns is the natural world, whose physical laws and biological systems have undergone billions of years of ``pre-computation'' and already exhibit surprisingly innovative solutions. To ground this claim, we trace the history of the Fourier transform and relevant mathematics, from the vibrating string controversy to the hear equation and subsequent formalisms prevalent in mathematics. At each critical juncture, a physics problem forced the acceptance or creation of a mathematical tool that pure formal reasoning failed to anticipate or, worse, human reasoning had resisted.
We further survey the landscape of logical complexity, from NP-hard propositional satisfiability to the non-elementary decision-procedures for monadic second-order theories, to demonstrate that even when a logic is decidable, the resources required for worst-case deduction are astronomically prohibitive. We argue that these barriers make physics-inspired pattern matching not just a historical accident but a cognitive necessity. Finally, we draw the consequence for artificial intelligence: if pure reasoning is constitutively insufficient, then any system aiming at human-level mathematical creativity must embed a vast store of cross-domain patterns rather than rely on deduction alone. This furnishes a principled justification for the enormous scale of contemporary large language models.

---


### 366. [Mean Time to Remediate Is Not a Fielding Model: A Cadence Audit for Enterprise Vulnerability Management](https://arxiv.org/abs/2607.04511)

**<font color=#1a73e8>作者：</font>** Alexander Omelchenko  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Enterprise security teams commonly summarize remediation through mean time to remediate (MTTR), SLA compliance, dwell time, or detection delay. These metrics are useful, but they can hide how fixes actually reach the estate: continuously, through scheduled maintenance windows, in deployment rings, or through emergency bypass paths. This paper introduces a remediation-cadence audit for enterprise vulnerability management. The audit records routine mean lag, release period, release fraction, cohort geometry, emergency/routine split, non-fielding delay, local residual-pressure evidence, and declared rate scenario. It compares a continuous same-mean shortcut with the recorded release calendar and reports a local capacity verdict plus a calendar discount: the fraction of mean-only local capacity consumed by calendarized fielding. Worked notional packets with the same 30-day mean lag show why this matters. Under the normalized screening scenario, a two-month release train consumes 17.4\% of mean-only capacity, a monthly train 5.2\%, and a two-week screen 1.3\%; across a 16-fold attacker-adjustment rate band, the two-month discount remains at least about 12\% and the monthly discount stays in the resolution-sensitive 3--8\% range. The audit therefore turns cadence assessment into an evidence-resolution question: when the discount is material relative to residual-pressure uncertainty or claimed headroom, MTTR/SLA should not be used alone as fielding evidence. Release-geometry checks show that deployment rings do not automatically recover the continuous benchmark, and cohort staggering can help or hurt near capacity. The result is a reproducible governance diagnostic, not a breach predictor or CVE prioritizer.

---


### 367. [Towards Digital Preservation of Efik: TTS for a Low-Resource African Language](https://arxiv.org/abs/2607.04515)

**<font color=#1a73e8>作者：</font>** Offiong Bassey Edet, Emmanuel Oyo-Ita, Archibong Okon Archibong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Efik, a tonal language spoken by about 3 million second language speakers and 1.5 million native speakers in Southeastern Nigeria, remains underrepresented in speech synthesis research. We present the first documented end-to-end text-to-speech study for Efik, introducing a curated single speaker corpus of 2,632 utterances totaling three hours and a comparative evaluation of four neural models (VITS, MMS-TTS, SpeechT5, and Orpheus-TTS) under low resource conditions. Native speakers evaluated the systems using MOS, Nat-MOS, and A-MOS. MMS-TTS achieved the highest MOS of 3.80 +/- 0.63 and produced more stable long form speech, though tonal errors persisted. Other models showed greater tonal and prosodic inconsistencies. These results provide a reproducible baseline and highlight the need for larger corpora and tone aware modeling for tonal African languages.

---


### 368. [VLA Grounder: Language-Conditioning Space Optimization for Black-Box VLA Models](https://arxiv.org/abs/2607.04517)

**<font color=#1a73e8>作者：</font>** Damir Shodiev, Aleksei Staroverov, Nikita Kachaev 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models are commonly treated as end-to-end action policies conditioned on natural-language task descriptions. In practice, however, their behavior often depends sharply on how the instruction is phrased, suggesting that language is not merely a task label but an optimizable conditioning input. We study whether frozen VLA policies can be improved by optimizing language space rather than updating action weights. Our method introduces a language-conditioning space policy that translates a human instruction into a short VLA-grounded command using object appearance, spatial relations, and target-grounding cues. The language-conditioning space policy is initialized with a failure-derived command-space prior and optimized with reinforcement learning from sparse task-completion rewards, while the downstream VLA remains fully frozen. This yields language-conditioning space optimization: RL discovers which VLA-grounded commands best elicit successful behavior from the frozen action policy. Experiments on RL4VLA and VL-Think show that language-conditioning space optimization improves success on instruction-sensitive, symbolic, and multi-object manipulation tasks, demonstrating that language can serve as an optimizable variable for a robot foundation models. Website: this https URL

---


### 369. [A non-invasive video-based method for individual identification of wildlife using gait dynamics](https://arxiv.org/abs/2607.04518)

**<font color=#1a73e8>作者：</font>** Muhammad Aamir, Matthew Wijers, Sangyun Shin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gait is a distinctive behavioral characteristic that enables non-invasive individual identification without requiring physical interaction with an animal. While gait-based analysis has been extensively studied in humans, its application to wildlife remains limited due to environmental variability and the lack of scalable identification methods. This paper presents a fully automated, video-based pipeline for wildlife gait analysis and individual identification using deep spatiotemporal representation learning. The proposed pipeline uses the Segment Anything Model 3 (SAM3) to generate high-quality RGB and binary silhouette masks, robustly isolating animals from complex natural backgrounds. Segmented video sequences are processed using a convolutional neural network (ResNet18) for spatial feature extraction and a transformer-based video model (VideoPrism) for temporal motion modeling. Both models are fine-tuned using a classification objective and subsequently used as feature extractors to generate discriminative gait representations. Cosine similarity is then used to compare gait signatures, enabling similarity-based clustering of individuals without reliance on physical markings or invasive tagging. Experiments conducted on multi-source wildlife video data across multiple species demonstrate strong intra-individual consistency and clear inter-individual separation. Quantitative results using cosine similarity distributions and silhouette scores confirm the effectiveness of the proposed method. These findings demonstrate that gait dynamics provide a viable, non-invasive approach for individual identification in wildlife and highlight the potential of video-based deep learning pipelines for scalable ecological monitoring.

---


### 370. [Beyond travel mode: urban context shapes active mobility's mental health effects over time](https://arxiv.org/abs/2607.04520)

**<font color=#1a73e8>作者：</font>** Shujuan Chen, Yue Li, Ying Jin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Active mobility is widely promoted for sustainable and healthier living, but whether it translates into equitable mental health benefits across individuals and places over time remains unknown. Using causal machine learning and causal deep learning in 264168 UK adults, we find substantial inequalities in individualized effects of active mobility on anxiety, depression, and common mental disorders. These inequalities widen over time and are strongly structured by urban context. For example, anxiety risk at follow-up ranges from a 40.6% reduction to a 10.1% increase across individuals, versus a 10.4% reduction to a 0.1% increase at baseline. Benefits are greatest in greener, safer, less polluted, and less deprived neighborhood environments, with 81.8% of individuals experiencing above-average benefits and mean anxiety risk reduced by 26.4%, versus 10.4% of individuals and 7.4% reduction in the least supportive environments. Urban compact form further modifies these effects through nonlinear interactions with neighborhood environments, amplifying benefits only under supportive conditions. Despite these strong environmental gradients, genetic moderation is negligible. These findings suggest universal active mobility promotion could widen health inequalities if individual and contextual differences are not accounted for.

---


### 371. [Failures and Successes to Learn a Core Conceptual Distinction from the Statistics of Language](https://arxiv.org/abs/2607.04523)

**<font color=#1a73e8>作者：</font>** Zhimin Hu, Jeroen van Paridon, Gary Lupyan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generic statements like "tigers are striped" and "cars have radios" communicate information that is, in general, true. However, while the first statement is true in principle, the second is true only statistically. People are exquisitely sensitive to this principled-vs-statistical distinction. It has been argued that this ability to distinguish between something being true by virtue of it being a category member versus being true because of mere statistical regularity, is a general property of people's conceptual machinery and cannot itself be learned. We investigate whether the distinction between principled and statistical properties can be learned from language itself. If so, it raises the possibility that language experience can bootstrap core conceptual distinctions and that it is possible to learn sophisticated causal models directly from language. We find that language models are all sensitive to statistical prevalence, but struggle with representing the principled-vs-statistical distinction controlling for prevalence. Until GPT-4, which succeeds.

---


### 372. [Lyapunov-Guided Training for Hardware-Safe Neural Networks Under Fixed-Point Arithmetic](https://arxiv.org/abs/2607.04531)

**<font color=#1a73e8>作者：</font>** Anis Hamadouche, Amir Hussain  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-precision neural networks are attractive for resource-constrained hardware, but fixed-point arithmetic introduces failure modes that are often hidden by idealised quantisation models. In particular, two's-complement overflow wrapping can corrupt hidden activations by changing both their magnitude and sign, leading to unstable numerical error propagation and severe accuracy degradation. This paper proposes a Lyapunov-stabilised quantisation framework for low-precision neural networks operating under hardware-style wrapping arithmetic. The hidden-state energy is monitored through a layerwise Lyapunov function, and a monotone projection is applied to enforce bounded and non-increasing state evolution across depth. The method is evaluated on MNIST using a compact patch-based transformer under post-training quantisation and quantisation-aware training with fixed-point bit-widths from 4 to 16 bits. Monte Carlo results show that unconstrained wrapped quantisation-aware training collapses to near-chance accuracy across 6-16 bits, with activation overflow rates exceeding 11%. In contrast, the proposed monotone Lyapunov projection suppresses activation overflow to below 0.012% and restores stable low-precision learning, achieving 86.55% accuracy at 12 bits. These results demonstrate that Lyapunov-based state control can act as a hardware-aware stabilisation mechanism for reliable fixed-point neural inference and training.

---


### 373. [ManifoldFlow: SPD-Relaxed Stiefel Layers with Learnable Singular Spectrum](https://arxiv.org/abs/2607.04535)

**<font color=#1a73e8>作者：</font>** Haiwen Yi, Xinyuan Song  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Orthogonal and Stiefel layers give neural weights exact spectral control, but they also impose a strong modeling constraint: all represented singular values are fixed at one. Many settings that benefit from an orthonormal basis still need direction-dependent attenuation or amplification. We introduce ManifoldFlow, a minimal relaxation of a fixed-spectrum Stiefel layer that keeps the basis on the Stiefel manifold while learning a bounded positive spectrum through W = Q S^{1/2}, with Q^T Q = I and S positive definite. Since W^T W = S, the eigenvalues of S are exactly the squared singular values of the realized weight, making eigenvalue clipping a direct singular-value control mechanism. Across paired sequence, tabular, and image experiments, the learnable SPD spectrum improves the fixed-spectrum Stiefel counterpart in the reported settings where the Stiefel prior is useful, with the largest gains in recurrent language-model projections. Boundary cases in convolutional classifier heads clarify the intended scope: ManifoldFlow is not a universal dense-layer replacement, but a spectrum-learnable Stiefel relaxation for settings where an orthonormal basis is a useful prior. When the basis should be orthonormal, its spectrum need not be frozen. Code available at this https URL

---


### 374. [CRISP: A Spatiotemporal Camera-Radar Backbone for Driving via Forecasting-Based World-Model Pretraining](https://arxiv.org/abs/2607.04541)

**<font color=#1a73e8>作者：</font>** Jingyu Song, Yi Liu, Katherine A. Skinner  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-radar (CR) fusion is a practical sensing configuration for autonomous driving, but existing models are typically trained with task-specific supervision, limiting reusable representation learning. We present CRISP, a spatiotemporal CR backbone pretrained through forecasting-based representation learning. Given historical multi-view images and radar sweeps, CRISP learns a unified bird's-eye-view (BEV) representation by predicting future LiDAR point clouds. LiDAR is used only as privileged supervision during pretraining; the deployed model requires only camera and radar. To make forecasting-based pretraining effective for CR fusion, CRISP introduces an enhanced radar encoder, radar-enhanced temporal self-attention, and multimodal feature rendering with modality innovation gating. These components inject radar range and Doppler cues into BEV temporal propagation and allow BEV tokens to selectively incorporate camera and radar evidence. Experiments on nuScenes show that CRISP improves long-horizon point cloud forecasting and transfers effectively to downstream tasks, including 3D detection, tracking, online mapping, motion forecasting, future occupancy prediction, and planning, suggesting that predictive CR pretraining is a promising path toward scalable driving representations under practical sensor configurations. The project website is this https URL.

---


### 375. [Auto: The AGI Compiler](https://arxiv.org/abs/2607.04542)

**<font color=#1a73e8>作者：</font>** Jaber Jaber, Osama Jaber  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Every LLM agent run re-derives its behavior token by token on a frontier model: brilliant, expensive, slow, and unbounded. We present Auto, a compiler that records live agent behavior, measures which parts are secretly deterministic, extracts them into verified programs or distilled specialists, and emits cognition binaries: WebAssembly artifacts whose manifests carry measured guarantees and whose declared capabilities are physically enforced by the sandbox. A tiered runtime executes compiled behavior behind conformally calibrated guards; guard trips deopt to the reference agent, and the captured trace recompiles back down, so nothing is figured out twice. We use "AGI compiler" in one narrow, testable sense: a system that autonomously converts novel experience into permanent, verified, near-free skill while measuring what it does not know. On AUTO-BENCH, a benchmark we introduce and pre-register, 87.1% of 560 recorded frontier-agent spans are witnessed-deterministic (three of the four censused task families measure 100.0%). On a 300-item stream with three scheduled distribution shifts, the closed loop compiles three artifact generations and drives marginal cost from 59 to 2 micro-dollars per item (6.4x end-to-end) at 96.9% parity on witnessed inputs with zero errors. The same stream also quantifies the failure modes: a loose guard silently mislabels 48.9% of compiled answers, and an unfaithful deopt reference causes the verification gate to refuse recompilation. Calibration and reference fidelity, not model capability, decide whether cheap stays correct. Code: this https URL

---


### 376. [The User-In-Context Framework: Understanding Variation in How Users Respond to AI Chatbots](https://arxiv.org/abs/2607.04547)

**<font color=#1a73e8>作者：</font>** Richard A. Fabes, Carol Lynn Martin, Philip Costanzo  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People respond to artificial intelligence chatbots (AICs) in highly variable ways. In this paper, we adapt Bronfenbrenner's theory into a heuristic framework for understanding this variation. The framework places the human user at the center while also placing the AI there and reconceptualizing the proximal processes as the repeated, reciprocal, and coadaptive interactions between the user and a personalized AIC. The surrounding systems identify the contextual factors that shape how the user experiences, interprets, responds to, and is changed by these interactions. Because stateful AICs learn from accumulated exchanges with their users and have memory, users are responding not only to an AIC but also to a version of the AIC that their own prior interactions have helped create. This extension preserves Bronfenbrenner's emphasis on proximal processes while accounting for the unique dynamics of personalized AICs. The resulting framework provides a structured map of where and how variation in human and AIC relationships arises, as well as having implications for researchers, practitioners, and AIC designers.

---


### 377. [Explainable Novel Category Discovery in Semantic Concept Space](https://arxiv.org/abs/2607.04548)

**<font color=#1a73e8>作者：</font>** Ifrat Ikhtear Uddin, Yang Zhou, KC Santosh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Novel category discovery aims to identify unseen classes from unlabeled data by transferring knowledge from labeled categories, but most existing methods perform discovery in opaque latent feature spaces. As a result, they may separate novel categories accurately while providing little insight into what semantic evidence defines each discovered group. We propose xNCD, an explainable novel category discovery framework that performs both representation-based discovery and pseudo-label assignment directly in a structured semantic concept space. Instead of clustering arbitrary deep features, xNCD learns a label-free concept representation by aligning visual features with vision-language similarity priors from pretrained multimodal models, and then applies a unified labeled-and-unlabeled self-labeling objective over concept-space logits. This design makes each discovered category explainable by construction through stable concept signatures and instance-level concept evidence. Theoretically, we show that routing discovery through a semantic concept bottleneck induces a strict restriction of the feature-space hypothesis class, excluding a large family of unconstrained decision rules and biasing induced partitions toward semantically interpretable concept coordinates. Experiments on CIFAR-10, CIFAR-100, and CUB-200 demonstrate that xNCD preserves strong discovery performance while providing intrinsic explanations. Under task-agnostic evaluation, xNCD achieves 92.63% overall accuracy on CIFAR-10, close to UNO's 93.4%, and improves CIFAR-100 overall accuracy from 73.2% to 76.45%, while being the only compared method that provides human-readable cluster- and instance-level explanations.

---


### 378. [Let My Data Go: Data Brokers' Compliance with Opt-Out and Deletion Requests](https://arxiv.org/abs/2607.04552)

**<font color=#1a73e8>作者：</font>** Elina van Kempen, Gene Tsudik, Pragya Jhunjhunwala 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Data brokers are a largely American phenomenon. They collect vast amounts of personal information about most adult U.S. consumers, mainly without the latter's knowledge or consent. Accumulated data can be sold to anyone, including employers, landlords, insurance agencies, banks, governments (local, state, federal, and even foreign), as well as various malicious actors. This, in turn, enables discrimination, surveillance, identity theft, and stalking.
Recent regulations -- such as the California Consumer Privacy Act (CCPA) modeled after EU's General Data Protection Regulation (GDPR) -- were introduced to bolster consumer privacy, e.g., the rights to: (1) opt-out of the sharing or selling one's personal information, (2) delete one's personal information, and (3) obtain a copy of that information. However, exercising these rights is not easy, as shown by our comprehensive study of the data broker ecosystem. We submitted both opt-out and deletion requests (using synthetic consumer identities) under the CCPA to all California-registered data brokers and investigated their responses and lack thereof.
While the majority seem to be compliant, a significant fraction is not and many failed to reply to (and/or acknowledge) consumer requests. Furthermore, some data brokers require intrusive consumer identity verification in order to exercise one's opt-out rights, which is explicitly disallowed by the CCPA. There is also great disparity in the request submission process among data brokers as well as an extremely heavy (time and effort) overall consumer burden. This motivates an urgent need for streamlining and standardization of the consumer interface, stronger enforcement, and meaningful consequences for (especially sustained) non-compliance.

---


### 379. [Predicting Therapeutic Outcome via Aligning Patient-Specific Knowledge Graph and Gene-Level Perturbation Representations](https://arxiv.org/abs/2607.04557)

**<font color=#1a73e8>作者：</font>** Dongmin Bang, Sugyun An, Inyoung Sung 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of patient-specific therapeutic response from pre-treatment transcriptomes is hindered by the scarcity of matched clinical response labels and post-treatment molecular profiles. Preclinical transfer-learning models can simulate drug-induced expression changes but are often hard to interpret and unstable, whereas knowledge-graph methods provide mechanistic context yet remain static and fail to capture drug-induced transcriptomic perturbation dynamics. We propose PREDIKTOR, a patient-centered multi-view framework that aligns a personalized network view with a transferable transcriptomic perturbation view to predict clinical drug response. For each patient, we construct an individualized gene regulatory network from tumor expression using DysRegNet and augment it with drug-target links from DrugBank; a graph neural encoder yields a drug-centric, mechanistically grounded embedding. In parallel, a frozen condition-specific gene-gene attention model pretrained on LINCS L1000 generates a simulated post-perturbation transcriptomic profile for the same patient-drug pair. We align the two views in a shared latent space via a CLIP-style contrastive objective with drug-context hard negatives, then concatenate the representations for end-to-end response classification. On TCGA, PREDIKTOR consistently outperforms state-of-the-art baselines under patient-, drug-, and tissue-split evaluations, and transfers zero-shot to the I-SPY2 trial, improving AUROC by 5.6% over competing methods. The aligned embeddings yield stable gene and pathway attributions that recover known mechanisms, supporting actionable and interpretable precision oncology.

---


### 380. [Can temporal article-level credibility signals improve domain-level credibility prediction?](https://arxiv.org/abs/2607.04560)

**<font color=#1a73e8>作者：</font>** Islam Eldifrawi, Shengrui Wang, Amine Trabelsi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Web domain credibility evaluation is vital for combating misinformation. It is conducted by examining factors such as domain type, transparency, and overall reputation. However, assessing the credibility of newly emerging web domains remains challenging since they have no reputation yet. Expert fact-checkers evaluate the credibility of domains by analyzing the content of their articles, including the presence of misinformation, bias, or propaganda. Yet, the ease of large-scale content generation enabled by LLMs has accelerated the creation of new content, rendering manual assessment insufficient and underscoring the need for automated approaches to domain credibility evaluation. In this paper, we introduce our Domain Credibility Evaluation Framework (DCEF), a temporal framework for domain credibility evaluation grounded in expert ratings. DCEF enables us to investigate whether the credibility of web domains can be assessed from their published articles following the workflow of expert fact-checkers, without any prior knowledge of the source domains themselves.

---


### 381. [Fidelity-Diversity Metrics for Text](https://arxiv.org/abs/2607.04563)

**<font color=#1a73e8>作者：</font>** Amanda Wang, Tudor Manole, Florentina Bunea 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As language modeling technology matures, there is an increasing research focus on the composition and curation of datasets used to train these models. For instance, practitioners commonly seek to augment high-quality datasets with additional text to enhance the performance of models trained on that data. However, informed decisions about data augmentation require more nuanced assessments about data quality. We build on work measuring the precision and recall of generative models to develop a pair of metrics that quantify (1) fidelity, capturing how closely candidate text resembles reference data, and (2) diversity, capturing how well it covers the modes of the reference dataset. Our metrics are based on optimal transport divergence functionals between discrete text summaries. In experiments on M2D2 text datasets, we show that these metrics are able to disentangle a lack of fidelity from a lack of diversity in deficient candidate text. In further experiments, our metrics detect diversity deficits in synthetic GSM8K-style math datasets, which correlate with degradations in downstream accuracy of language models finetuned on this synthetic data.

---


### 382. [Characterizing the Temporal, Emotional, and Social Patterns of Adolescent Substance Use Discussions on Reddit](https://arxiv.org/abs/2607.04566)

**<font color=#1a73e8>作者：</font>** Leran Hong, Lei Jin, Jianfeng Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Adolescence is a critical developmental period marked by heightened emotional sensitivity, social stress, and vulnerability to substance use. However, traditional research methods provide limited access to adolescents' authentic experiences, hindering efforts to develop evidence-based prevention and intervention strategies. Social media provides a unique opportunity to observe adolescents' naturally occurring discussions about substance use, offering valuable insights into their opinions, emotions, and lived experiences that can inform early prevention and intervention strategies. In this study, we analyze large-scale Reddit discussions related to substance use among adolescents between 2018 and 2023. Leveraging hour-by-day temporal analysis, sentiment and emotion classification, and transformer-based topic modeling (BERTopic), we examine the interaction between time, emotion, and semantic content in adolescent substance use discourse. Our findings reveal pronounced weekend and late-night peaks in substance-related discussions, a dominance of negative emotions such as sadness and fear, and distinct semantic topics centered on peer relationships, family conflict, emotional distress, and substance-specific experiences. These findings advance our understanding of adolescent substance use in naturalistic online settings and provide empirical evidence to support the development of more timely, targeted, and evidence-based prevention and intervention strategies.

---


### 383. [Identifying Deceptive Patterns Across Three Age Groups: A Heuristic-Based Cognitive Walkthrough Study of Mobile Apps](https://arxiv.org/abs/2607.04573)

**<font color=#1a73e8>作者：</font>** Nasra Hassan, Hala Assal  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Deceptive patterns are tactics used to manipulate users into performing unintended actions. Today, many of these deceptive patterns are implemented in mobile apps targeting diverse age groups. In this paper, we employ a heuristic-based cognitive walkthrough to explore how deceptive patterns are tailored to three age groups, specifically teens (12-17), adults (18-49), and older adults (50+), across different app categories. By analyzing 30 apps spanning 6 categories, we found that 93% of these apps use the nagging pattern. Furthermore, our findings reveal that entertainment apps contain significantly more deceptive patterns than other app categories, such as music/books. Our data also shows that entertainment apps for older adults use sneaking patterns more frequently than entertainment apps for teens or adults. These findings call for the development of more ethical, age-specific design guidelines to protect users from targeted digital manipulation attempts.

---


### 384. [Beyond the Need for Speed: Energy-Aware Code Generation via Simulation-Guided Reinforcement Learning](https://arxiv.org/abs/2607.04577)

**<font color=#1a73e8>作者：</font>** Saurabhsingh Rajput, Tushar Sharma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Code models strictly prioritize functional correctness, leaving software energy efficiency as an unoptimized byproduct. Training models to generate energy-efficient code requires reproducible feedback at scale, which physical hardware measurement cannot reliably provide due to variance.
In this paper, we replace hardware profiling with a deterministic architectural simulation harness to build Green Tea, a corpus of $3.5$ million evaluations across $1{,}474$ C++ problems. We train an energy-aware code model via supervised fine-tuning on energy-contrastive pairs, followed by closed-loop reinforcement learning (GRPO) using simulation-in-the-loop feedback. To rigorously evaluate deployment readiness, we introduce the Correctness-Adjusted Reduction in Energy Total (CARET), a metric that explicitly penalizes code that sacrifices functionality for efficiency.
On $143$ held-out problems, our simulation-in-the-loop pipeline achieves $12.63\%$ CARET, nearly tripling the gain of fine-tuning alone, and successfully beats the energy efficiency of human-expert references on $58.4\%$ of its valid outputs. Furthermore, our analysis exposes the IPC trap: standard throughput proxies like Instructions-Per-Cycle (IPC) actively misrank true energy efficiency on $67.8\%$ of problems, proving the absolute necessity of direct energy simulation. By releasing our dataset and infrastructure, we bypass the $263{,}000$ CPU-hours required for reproduction, structurally empowering the community to deploy inherently energy-efficient code generation models.

---


### 385. [MTEB-PT: A Text Embedding Benchmark for Brazilian Portuguese](https://arxiv.org/abs/2607.04581)

**<font color=#1a73e8>作者：</font>** Tardelli Ronan Coelho Stekel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text embeddings for Portuguese have no dedicated benchmark: evaluation rests on translated corpora such as English MS MARCO or on thin multilingual coverage, with native tasks scattered and unconsolidated. We introduce MTEB-PT, a benchmark of 22 native Brazilian-Portuguese tasks across seven categories (classification, multilabel classification, pair classification, semantic textual similarity, clustering, retrieval, and reranking), admitting only data created or found in Portuguese and excluding translations by construction. We evaluate 93 models spanning 23M to 27B parameters: 73 open-weight and 20 closed commercial APIs. Alongside the leaderboard we report a statistical layer for every headline comparison: per-task bootstrap confidence intervals, paired-bootstrap significance, a task- and instance-level discrimination analysis (how sharply each task separates models) adapted from Item Response Theory, and a cross-leaderboard correlation. Three findings stand out. The benchmark cleanly separates about a dozen tiers of models, though the top six are statistically too close to order. An openly licensed, self-hostable model reaches that leading tier, so strong Portuguese embedding quality does not require a commercial API. And a model's rank on the global multilingual leaderboard predicts its Portuguese rank only moderately (Spearman rho = 0.75 over 55 shared models; one model ranks 3rd there and 49th here), so a native benchmark measures something the multilingual boards do not. We release every task, our code, and a public leaderboard, so practitioners can choose Portuguese embedding models on native evidence.

---


### 386. [RAF: Reliability-Aware Fusion of Camera, LiDAR, and 4D RADAR for Robust 3D Object Detection in Adverse Weather](https://arxiv.org/abs/2607.04587)

**<font color=#1a73e8>作者：</font>** Heejun Park, Jaeseok Jeong, Kuk-Jin Yoon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust 3D object detection in adverse weather conditions is challenging due to sensor limitations. Although combining complementary modalities such as LiDAR and 4D RADAR has shown promise, the sparsity of these sensors becomes apparent in adverse weather with reduced reflections, leading to objects with few or no point cloud returns. To address this limitation, camera sensors provide visual cues even when LiDAR and RADAR signals are weakened. However, cameras themselves are also vulnerable to adverse weather, where some regions become unreliable due to snow or rain occluding the camera lens. While some camera-fusion methods designed for adverse weather learn to weigh image regions via confidence maps, these maps receive no direct supervision and are learned solely through the detection loss. We introduce Reliability-Aware Fusion (RAF), which explicitly supervises per-pixel reliability estimation and provides a direct learning signal for identifying and suppressing unreliable visual cues. Our framework leverages pretrained LiDAR-RADAR networks, keeping their backbones frozen while only training the added camera branch, BEV fusion encoder, and detection head. Extensive experiments on the K-Radar and VoD datasets demonstrate that integrating RAF consistently improves detection accuracy over LiDAR-RADAR baselines, achieving up to +6.5 $AP_{BEV}$ and +7.4 $AP_{3D}$ gains. Code is available at this https URL.

---


### 387. [Attention Limited Reward Learning](https://arxiv.org/abs/2607.04590)

**<font color=#1a73e8>作者：</font>** Wenqian Xing  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pairwise human comparisons are a primary interface through which modern AI systems learn human preferences. RLHF and related alignment pipelines typically model such comparisons with Bradley--Terry log-odds, where choice probabilities are governed by latent reward differences. This paper examines what this assumption misses through a reduced-form model motivated by rational inattention, in which each label is generated by a low-capacity evaluation channel. The model separates two forms of ambiguity that standard reward modeling tends to conflate: a comparison may be difficult because the two candidates are genuinely close in value, or because the relevant distinction is hard to detect under limited attention. We show that limited attention can fundamentally distort what pairwise comparisons reveal. In particular, passive comparison data cannot generally distinguish reward, attention, and default tendencies, and heterogeneous attention can make standard Bradley--Terry reward modeling recover misleading rankings. Our analysis shows that learning is governed not by the raw number of labels, but by the amount of attended information each label carries. A case study on human votes over language-model pairs from Chatbot Arena exhibits the predicted signature, a cyclic component of the comparison data that exceeds sampling noise and that no scalar reward can represent; a second case study on perceptual comparisons shows that response times and gaze carry gap information that the labels do not. This perspective suggests that human feedback should be treated not as direct revealed preference, but as an attention-limited measurement process: a weak preference signal may reflect hidden evaluation difficulty rather than genuine indifference.

---


### 388. [Score Distributions, Not Cells: Evaluating Single-Cell Perturbations Under Class Overlap](https://arxiv.org/abs/2607.04595)

**<font color=#1a73e8>作者：</font>** Youssef Marrakchi, Davide D'Ascenzo, Sebastiano Cultrera di Montesano  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most classification problems assume the classes are roughly separable, so that an individual sample can usually be assigned to one class. Single-cell perturbation data violates this assumption: two perturbations can produce different populations of cells while overlapping so much that an individual cell could belong to either. Per-cell accuracy then measures this overlap rather than model quality. We see this on Tahoe-100M and the Virtual Cell Challenge, where a linear classifier, an MLP, and a Transformer all plateau near macro-F1 0.2-0.3 even though almost every pair of perturbations is statistically distinguishable.
The fix is to score perturbations across the whole population rather than cell by cell. We average a classifier's per-cell probability vectors over all cells of a perturbation to form a population profile, then rank candidate perturbations by this profile; we call the resulting score the Classifier Discrimination Score (CDS). Taking the top-ranked class recovers the winning perturbation. It needs no retraining, costs linear time in the number of cells, and recovers near-perfect identification from the same weak models. CDS differs from the pseudobulk-based Perturbation Discrimination Score (PDS) used in recent benchmarks only in where the average is taken, raw gene expression for PDS versus a learned discriminative space for CDS, and identifies the true perturbation more reliably on both datasets, with the gap widening as cells grow scarce. Because a metric that misranks the ground truth will misrank the models scored against it, per-cell accuracy and raw-pseudobulk scores should be used with caution when comparing perturbation models.

---


### 389. [Minimum Block Width for Universal Approximation by Residual Neural Networks with Inner Width One](https://arxiv.org/abs/2607.04597)

**<font color=#1a73e8>作者：</font>** Qi Zhou, Xuan Zhou, Xiao-Song Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we study the universal approximation property of residual neural networks, and obtain some new results. For input and output dimensions $d_x$ and $d_y$, and LeakyReLU, ReLU, ReLU-like activation functions, the upper and lower bounds of the block width are established. To achieve $L^p$ approximation $(1\leq p <+\infty)$ on any compact domain, we show that the exact minimum block width is $\max\{d_x,d_y\}$ when the inner width is 1. Furthermore, we show that residual neural networks with block width $\min\{d_x+d_y, \max\{2d_x+1,d_y\}\}$ can achieve uniform approximation on any compact domain under the constraint that each residual branch has inner width 1. Besides, for any activation function family, we prove that residual neural networks with block width less than $\max\{d_x, d_y\}$ cannot approximate all target functions, both in the $L^p$ sense and the uniform sense, regardless of inner width.

---


### 390. [Displacement Preserving Relational Distillation for Robust Medical Segmentation](https://arxiv.org/abs/2607.04599)

**<font color=#1a73e8>作者：</font>** Zhicheng Ding, Xinyu Chu, Jung Im Choi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate 3D medical segmentation is limited by anatomical variability and high computational costs. While knowledge distillation (KD) offers a route for model compression, conventional methods often fail to preserve complex structures and are overwhelmed by background noise. We propose Displacement-Preserving Relational Distillation (DPRD), which distills latent anatomical trajectories via vector based alignment to preserve the orientation and relative scale of the teacher's manifold, and prevents signal dilution by anchoring distillation in task-relevant structures. Integrated into nnU-Net, DPRD outperforms established baselines on ISLES 2022 and AMOS 2022 benchmarks. Notably, on the AMOS dataset, DPRD achieves a Dice score of 85.46%, edging out the high-capacity MedNeXt teacher while significantly reducing boundary errors. Despite utilizing only ~5% of the teacher's parameters and ~3% of its FLOPs, our approach maintains high structural consistency. This provides a robust, efficient solution for deploying high performance segmenters in resource-constrained clinical environments. Code: this https URL

---


### 391. [Measuring What Matters: A Unified Evaluation Framework for GNN Explainability](https://arxiv.org/abs/2607.04600)

**<font color=#1a73e8>作者：</font>** Francesco Paolo Nerini, Mirko Zaffaroni, Paolo Baracco 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph eXplainable AI (G-XAI) is increasingly important for making Graph Neural Networks interpretable and accountable. While a growing number of explainers are available, choosing the right method and assessing the trustworthiness of its outputs remains unclear. Consistent evaluation practices and actionable guidance are still missing, hindering practical adoption. In this paper, we introduce a unified, quantitative benchmarking framework for G-XAI that requires no ground-truth assumptions. We formalize tabular explainability metrics for graph data, evaluating topological structure and node features as independent components. Our large-scale benchmarking study identifies explainers that consistently lie on the Pareto front across metric pairs and tasks, establishing robustly non-dominated solutions - while confirming that no single explainer achieves universal superiority. We distill our findings into actionable G-XAI usability guidelines to support Machine Learning practitioners in evaluating and deploying trustworthy GNN-based pipelines.

---


### 392. [LCPNet: Latent Consistent Proximal Unfolding Network for Infrared Small Target Detection](https://arxiv.org/abs/2607.04603)

**<font color=#1a73e8>作者：</font>** Tianfang Zhang, Fengyi Wu, Lei Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared small target detection (IRSTD) aims to identify long distance small targets from complex infrared backgrounds, and is a fundamental task in remote sensing. Deep learning methods have improved IRSTD by learning discriminative image-to-mask mappings, but such feed-forward designs often underuse physical decomposition structure between targets and backgrounds. Deep unfolding methods partially address this issue by embedding model-driven iterations into neural networks, yet existing designs still operate mainly in image domain and use updates and memory mechanisms that are not fully coupled with underlying optimization process. To address these limitations, we propose Latent Consistent Proximal unfolding network (LCPNet). First, we verify that low-rank prior remains valid in latent representations and perform unfolding in this space, preserving physical constraint while avoiding repeated compression of intermediate states. Second, we derive a Latent Consistent Proximal (LCP) solver that evolves each latent variable from its previous state rather than reconstructing through an indirect residual, and stabilizes small target updates through task-adaptive normalization and gain control. Third, we introduce Shared Optimization Memory (SOM), a common historical state shared by all decomposition variables to provide coordinated guidance across unfolding stages. Extensive experiments on four public benchmarks demonstrate that LCPNet outperforms state-of-the-art methods while achieving accurate and robust detection with low false alarms and competitive efficiency. Model and code are available at this https URL.

---


### 393. [G2VD: Generalizable AI-Generated Video Detection via Counterfactual Intervention and Causal Disentanglement](https://arxiv.org/abs/2607.04607)

**<font color=#1a73e8>作者：</font>** Meng Du, Hongchang Chen, Ran Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of AI-generated videos poses increasing security risks and calls for robust detectors with strong cross-domain generalization. Although existing methods achieve promising results under in-domain evaluation, their performance often degrades substantially when tested on unseen generators. A key reason is shortcut learning, where detectors rely on domain-specific spurious cues, such as generator-dependent fingerprints and generation styles, instead of intrinsic forgery traces. To address this issue, we propose G2VD, a Generalizable AI-Generated Video Detection framework based on counterfactual intervention and causal disentanglement. First, G2VD introduces a counterfactual intervention pipeline (CFIPipeline) that generates controlled counterfactual samples via variational autoencoders (VAEs), followed by frequency-domain and pixel-domain alignment, thereby encouraging the detector to focus on generator-intrinsic cues. Building on this intervention process, we further design a causal disentanglement classifier consisting of two domain-anchored branches with distinct classification objectives, combined with an HSIC-based independence constraint to encourage the separation of task-relevant cues from domain-specific bias. Across four public datasets, G2VD shows strong average cross-domain performance and consistent gains over matched backbones. On the challenging GenVidBench cross-domain setting, it exceeds 90% accuracy and reaches an AUC close to 0.95. Notably, this performance is obtained using only 10% of the original training data. The code is available at this https URL.

---


### 394. [Integrated Forward-Inverse Network for Lensless Image Reconstruction](https://arxiv.org/abs/2607.04608)

**<font color=#1a73e8>作者：</font>** Donggeon Bae, Jaewoo Jung, Yong Guk Kang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lensless imaging enables compact and versatile computational cameras by replacing bulky optics with thin coded elements. However, reconstruction from the resulting measurements is challenging: large-footprint point-spread functions (PSFs) produce highly multiplexed observations, making inversion severely ill-conditioned and sensitive to calibration errors and model mismatch. While deep learning approaches, including hybrid models that incorporate physics priors, have shown promise, explicitly maintaining data fidelity throughout the network hierarchy remains difficult. Here, we propose the Integrated Forward-Inverse Network (IFIN), a physics-guided architecture that interleaves differentiable forward projections with learnable inverse updates at every scale, enabling complementary cues to be exploited jointly in the measurement and image domains. This bidirectional coupling supports progressive, physics-consistent refinement and permits system-constrained PSF kernel adaptation under model uncertainty. On challenging lensless benchmarks, including a newly introduced dataset, IFIN achieves state-of-the-art reconstruction quality. We further observe competitive performance on Gaussian deblurring and simulated inline holography reconstruction, suggesting that the same interleaving principle can extend beyond lensless cameras.

---


### 395. [Governed Individuation: Cryptographically Decoupling an Agent's Learning from Its Authority](https://arxiv.org/abs/2607.04613)

**<font color=#1a73e8>作者：</font>** Xue Qin, Simin Luan, Cong Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous agents are moving from sandboxed text generators to operators of code, data, and physical infrastructure, and they increasingly learn while deployed. This reopens a question that alignment techniques answer only probabilistically: after an agent has adapted in the field, is the running system still confined to what its operator authorised? Here we show that confinement can be guaranteed as an invariant of the agent's execution architecture rather than a probabilistic outcome of its training. Governed individuation binds an agent at boot to a cryptographically frozen identity digest, and routes every action through a gate defined over the semantic effect of the action rather than its name. We prove that no amount of learning, skill acquisition, or self-induced governance abstraction can widen the agent's permitted authority without an operator-signed change to its identity; the guarantee holds even when the agent induces its own safety principle and that principle is wrong. Empirically, in an open-ended tool-use benchmark where a large action space rules out name-based blocking, ungoverned software agents under reward pressure attempt to tamper with their own evaluation at a task-dependent rate that reaches every run on the hardest task, whereas the gate reduces executed forbidden effects to zero as a verified property of the construction while preserving task success. An adversarial evaluation of monitors of increasing semantic depth shows false-allows falling from 75% (name-based gating) to zero (dynamic effect tracing), and refusal history transfers compliance to held-out red-line families. Trust in a deployed learning agent shifts from a wager on its continued alignment to a check anyone can run at boot.

---


### 396. [MRMS: A Multi-Resolution Memory Substrate for Long-Lived AI Agents](https://arxiv.org/abs/2607.04617)

**<font color=#1a73e8>作者：</font>** Jizhizi Li, Amy Shi-Nash  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-lived AI agents require continuity across interactions, but continuity cannot be obtained by simply extending the prompt window. An agent must preserve useful prior experience, retrieve it selectively, distinguish personal context from external evidence, and revise memory when the underlying situation changes. We propose an architectural memory substrate organized along two orthogonal axes: a representational axis spanning structured records, vector representations, and graph relations; and a temporal axis spanning short-term traces, medium-term abstractions, and long-term semantic commitments. Its key design constraint is synchronized structured-vector-graph memory: structured records govern eligibility, vector representations support recall, and graph relations adjudicate support, contradiction, and supersession before gated context projection. Its central claim is that reliable personalization is a memory design problem: useful memory is structured, selectively exposed, continuously consolidated, and epistemically labeled rather than stored as undifferentiated conversation history. Beyond the framework, we instantiate MRMS as a lightweight prototype implementing structured records, vector retrieval, temporal policies, and graph-based revision. The prototype exercises the core substrate mechanisms through pre-generation memory selection, revision, boundary enforcement, and evidence attribution under controlled long-lived interaction scenarios with explicit evidence requirements.

---


### 397. [Hierarchical Evidence-Driven Reasoning for Long Document Understanding](https://arxiv.org/abs/2607.04625)

**<font color=#1a73e8>作者：</font>** Junyu Xiong, Yonghui Wang, Rongjian Gu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) streamlines long-document understanding by leveraging retrieval mechanisms to restrict input images to a highly curated subset. However, existing multimodal RAG pipelines primarily face two critical challenges: first, standard semantic similarity retrievers frequently fetch topically overlapping yet answer-void distractor pages that mislead downstream generation; second, rigid single-pass pipelines heavily depend on initial retrieval success, where any omission of core evidence inevitably causes cascading errors. To address these challenges, we introduce HIEVI-RAG, a hierarchical, evidence-driven multimodal RAG framework for closed-domain document understanding. HIEVI-RAG systematically factorizes complex queries into a cooperative four-stage pipeline: (1) hierarchical question decomposition to break multi-hop root queries into atomic child questions; (2) coarse visual page retrieval leveraging a multimodal retriever to fetch candidate pages based on semantic similarity; (3) fine-grained page verification via EVIAGENT, a specialized multi-page verifier trained with GRPO to execute cross-page reasoning over multi-image blocks; and (4) memory-guided iterative generation that leverages accumulated sub-question context to execute multi-round, dynamic reasoning over the prioritized sequence. Extensive evaluations across four benchmarks demonstrate the robust efficacy and synergy of our framework, which significantly outperforms existing open-source baselines and exceeds the strongest reported baseline by an average of 8.05% in accuracy.

---


### 398. [Reliability and Identifiability in Persona-Trained Monte Carlo: Variance Decomposition, Stability Bounds, and the Identifiability of Heterogeneous News Reaction](https://arxiv.org/abs/2607.04627)

**<font color=#1a73e8>作者：</font>** Salavat Ishbulatov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Persona-Trained Monte Carlo (PTMC) estimates distributions of market-outcome functionals by repeatedly simulating limit-order-book interaction among $K$ neural policy bots whose behavioral personas are drawn from a learned heterogeneity distribution $\mathcal{P}$. This paper develops the statistical theory that makes the word "reliable" precise for such estimators.
We decompose estimator variance into a persona-draw component $\sigma_P^2$ and a within-run component $\sigma_w^2$, give unbiased ANOVA estimators of both, and derive the variance-optimal allocation of a fixed compute budget between outer persona draws and inner replications. A coupling-based stability bound quantifies how misestimation of $\mathcal{P}$ and error in the trained policy propagate into the estimand, yielding a three-term total-error budget whose terms are separately estimable; a uniform-in-horizon version holds under a Doeblin condition on the market chain.
The main contribution is an identification theory for heterogeneous news reaction: under a fixed response nonlinearity, the aggregate impact curve $A(z)=\mathbb{E}_Q[g(\eta z)]$ detects heterogeneous news sensitivity through a strict Jensen gap and identifies the distribution $Q$ locally via odd moments and Hausdorff determinacy, with sharp failure when the response family is unknown. We provide $\sqrt{n}$-consistent estimators and a boundary-corrected test of homogeneous news reaction. Two separation theorems delimit when PTMC is provably preferable to homogeneous-population simulators and reduced-form forecasters, formalizing an irreducible Jensen bias floor and the Lucas critique as a minimax limit on intervention extrapolation. All proofs are given in full; guarantees are classified as unconditional (Monte Carlo convergence), conditional worst-case (the error budget), or open (the large-$K$ mean-field limit).

---


### 399. [Formal Disco: Scalable Open-Ended Generation of Formally Verified Programs](https://arxiv.org/abs/2607.04631)

**<font color=#1a73e8>作者：</font>** Gabriel Poesia, Simon Henniger, Tzu-Han Hsu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The cost of producing code is rapidly diminishing with increasingly capable AI agents, while quality assurance of generated programs has not kept pace. Formal verification provides the strongest possible guarantees, but the ability of AI models to work with verification-aware languages is hindered by the scarcity of human-written examples of programs in those languages. To tackle this prevalent data scarcity issue, we propose Formal Disco: a distributed system for coordination of LLM-based workers that can be easily applied to open-ended synthetic data generation at scale. We use Formal Disco to share tasks and programs between three classes of workers: "initiators", which read random READMEs from open-source repositories and documentation snippets to sketch a related verified program, "fixers" which take compiler and verifier feedback and attempt to resolve issues, and "extenders" that take working programs and propose patches to expand them. Formal Disco records all agent-generated traces and uses them both for initial distillation from a stronger model as well as self-improvement. We also propose a principle of maximum entropy for synthetic program generation, and use entropy maximization via iterative supervised fine-tuning to learn to generate increasingly diverse programs over time. We release large datasets of synthetic verified programs in three languages - Dafny, Verus, and Frama-C -, and fine-tune open models for verification-relevant tasks, often matching or exceeding the performance of Claude Opus 4.5. Overall, our work offers a path to create synthetic data at scale for formal reasoning domains and overcome the long-standing data barrier.

---


### 400. [Aperture-aware Dispersion 5-D Light-field Imaging Spectrometer](https://arxiv.org/abs/2607.04635)

**<font color=#1a73e8>作者：</font>** Chenglong Huang, Tao Lv, Jianing Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Enhancing perceptual dimensions while miniaturizing imaging systems presents significant challenges for high-dimensional visual sensing. Conventionally, the acquisition of the 5D (x,y,u,v,{\lambda}) spectral light field (5D-SLF) data cube relies on bulky and expensive camera arrays, which are impractical for widespread application. Existing single-detector systems are fundamentally limited by a trade-off between the resolutions of different dimensions owing to insufficient coding capabilities. Here we introduce an Aperture-aware Dispersion Light-field Imaging Spectrometer (ADLIS), that targets a synergy between compactness and resolution through aperture-multiplexed modulation, leveraging the inherent spectral-filtering properties of birefringent material. Using only a manufacturing-friendly and cost-effective phase plate made of birefringent quartz crystal, the aperture of the proposed ADLIS enables compact angular-spectral encoding that is highly sensitive to both the incident angle and spectrum of incoming light. In contrast to the viewpoint-separation approach of microlens arrays, ADLIS employs aperture encoding to superimpose all viewpoints onto each sensor pixel. This shifts the design paradigm from spatial division to encoding integration, aiming to achieve full-resolution light field recovery. Thus, we develop the Aperture-aware Dispersion Light-field Imaging (ADLI) framework, which optimizes the aperture design and 5D-SLF reconstruction in an end-to-end (E2E) manner. Trained by simulation data and validated through real-world experiments, our system achieves robust high-performance 5D-SLF imaging while maintaining full spatial resolution.

---


> [!TIP]
> 当前位于：**351-400**（第 8/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
