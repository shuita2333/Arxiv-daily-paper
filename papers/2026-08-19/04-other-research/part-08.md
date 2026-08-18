# 📦 其他研究 | 2026年08月19日

> 本类共 **435** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-400**（第 8/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-435](./part-09.md)

---

### 351. [DriveCache: Action-Aware Caching for Driving World Model Inference](https://arxiv.org/abs/2608.16354)

**<font color=#1a73e8>作者：</font>** Jianchun Yang, Jian Liang, Xianda Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Driving video generation models support autonomous-driving development by predicting controllable future scenes for simulation, planning evaluation, and offline data generation. Diffusion-based driving generators repeatedly evaluate large backbones across denoising steps, which limits generation throughput. Existing diffusion acceleration methods reduce this cost, but general-purpose designs omit driving signals available before generation, such as ego speed and planned trajectories. Experiments across driving motions show that cache tolerance varies with ego translation and rotation, denoising progress, and consecutive reuse length. We propose DriveCache, a training-free, action-aware controller that uses planned motion to allocate reuse across scenes and dynamic programming to place it across denoising steps under a calibrated response budget. A causal drift check refreshes features and replans the remaining schedule when generation departs from calibration. Across three generator configurations, DriveCache improves the overall fidelity-efficiency trade-off over evaluated cache methods. Our code will be publicly available.

---


### 352. [Depth-Dominant Skeleton Detection for Natural Scenes](https://arxiv.org/abs/2608.16367)

**<font color=#1a73e8>作者：</font>** Chengkun Rao, Yixuan Deng, Min Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> To date, all natural scene skeleton detection follows the paradigm of taking RGB images as the sole input; despite notable progress, methods under this paradigm suffer significant performance degradation on complex-content images. We observe that depth images are inherently insensitive to color and texture, and can provide clear regional contours and inter-region spatial relationships, which naturally alleviates the difficulty of skeleton detection in complex scenarios. Motivated by this observation, this paper proposes for the first time a novel skeleton detection paradigm where depth images serve as the dominant modality and RGB images act as the auxiliary, and accordingly presents a model DDSkel (short for Depth-Dominant Skeleton Detection) under this paradigm. DDSkel employs an asymmetric encoder design to fuse RGB information into depth features, with the RGB modality branch having only 12% the parameters of the depth modality branch. DDSkel has a simple structure without intricate designs. Nevertheless, with only 36% of the trainable parameters of the current best method, DDSkel outperforms all state-of-the-art approaches on SymPASCAL, the most challenging dataset with a large volume of complex images.

---


### 353. [OceanDepths: A Global Dataset of Paired Subsurface and Surface Ocean Observations](https://arxiv.org/abs/2608.16373)

**<font color=#1a73e8>作者：</font>** Simon Donike, Ruben Cartuyvels, Antonino Ian Ferola 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite comprising over 70\% of its surface, the world's oceans are critically underobserved compared to the land surface or the this http URL the global ocean requires jointly observing its surface and subsurface structure, yet no standardized, high-resolution dataset couples satellite surface fields to co-located \emph{in situ} depth profiles in an AI-ready this http URL resources either consist of model-reconstructed gridded products rather than observations, cover only a single variable or basin, or operate at resolutions too coarse for mesoscale this http URL introduce \textsc{OceanDepths}, the first open, global, regridded AI-ready dataset that pairs satellite-derived sea surface temperature (SST), sea surface salinity (SSS), and sea surface height (SSH) L4 products with co-located EN4 subsurface temperature and salinity profiles, complemented by matched GLORYS12 ocean reanalysis data to support comparisons or multi-stage this http URL dataset spans 2000--2024 at \SI{0.1}{\degree}$\times$\SI{0.1}{\degree} spatial resolution and at weekly temporal resolution, covering the entire globe's sea surface and with over 9.5 million paired profiles interpolated to 50 standardized depth this http URL provide a configurable system to split the globe in equally sized spatial this http URL 4D multivariate structure, high resolution, long temporal extent, and extreme sparsity of subsurface observations (${\sim}$0.01\% per depth level) make \textsc{OceanDepths}a challenging testbed for novel AI this http URL demonstrate subsurface state reconstruction as an example task with simple baseline models, but also envision \textsc{OceanDepths}to support the development of observation-based forecast methods and other related tasks.\added{Available at: this https URL.}

---


### 354. [Coverage-Maximizing Multinomial Subset Routing under Operational Constraints](https://arxiv.org/abs/2608.16375)

**<font color=#1a73e8>作者：</font>** Quan Zhou, Yiyan Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Multinomial Subset Routing (MSR), a new online routing framework over $K$ experts in which the learner keeps a multinomial routing policy instead of a deterministic subset of experts. At each round, the learner samples $M$ experts i.i.d. from the multinomial policy, and the resulting set of distinct sampled experts forms the routed subset.
The reward depends only on the best-performing expert(s) in the routed subset. This reward structure arises naturally in routing across specialized models but is not captured by standard combinatorial bandits or subset-selection methods, which optimize deterministic subsets and typically assume additive rewards. We require the selection to satisfy several long-term, two-sided operational constraints under bandit feedback, observing only the winner's reward each round. We propose OMD-Approachability, combining online mirror descent with Blackwell's Approachability, and prove it achieves $O(1/\sqrt{T})$ regret in both reward and constraint violation. We ground the framework in practical application domains and validate it empirically on a real-world crowdsourcing dataset.

---


### 355. [Adaptive Post-Processing Drives Instance-Level Detection in Stroke Lesion Segmentation](https://arxiv.org/abs/2608.16377)

**<font color=#1a73e8>作者：</font>** Qinghui Liu, Jon André Ottesen, Atle Bjørnerud 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instance-level lesion detection has been an increasingly larger focal point in medical image segmentation besides the more standard voxel-level overlap. Still, most pipelines are trained and post-processed for voxel overlap alone. In particular, the mismatch is most pronounced for small lesions, where a near-miss prediction---substantial overlap that falls just short of the instance-matching threshold---scores the same as a complete miss. In our ISLES'26 submission, we found that closing this gap mattered far more in post-processing than in architecture design. Our Volume-Conditioned Adaptive Post-Processing (VCAP) scheme adjusts component-size thresholds to each case's predicted lesion burden, improving Lesion-F1 by 0.032 (unbiased cross-fold estimate)---approximately 6 times larger than any architectural change we tested. A resolution-aware attention architecture (Viola2Plus), designed for small-lesion segmentation, shows why the distinction matters: it left small-lesion Dice unchanged but raised small-lesion detection rate by 3.7\%, a real effect voxel-overlap metrics alone would have missed. Under 5-fold cross-validation on the 1,453-case training set, our post-processed two-architecture ensemble achieves Dice 0.651 and Lesion-F1 0.614, versus 0.644 and 0.573 for the unprocessed single-model baseline.

---


### 356. [Unadapted Multilingual ASR on a Garrusi Kurdish Evaluation Set: A Common-Reference Staged Normalization Analysis](https://arxiv.org/abs/2608.16379)

**<font color=#1a73e8>作者：</font>** Hiwa Asadpour  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating speech recognition for a Kurdish variety written in a Latin field orthography, using a model that outputs Arabic script, creates a measurement problem before a modelling one: direct scoring treats writing-system differences as recognition errors. Jointly normalizing reference and hypothesis avoids this, but also changes reference tokenization, mixing agreement gains with a change in the scoring denominator. I evaluate MMS-1B-all with the Central Kurdish (ckb) adapter, used as released without adaptation, on 1,722 Garrusi questionnaire segments from five speakers (9,763 reference word tokens; 117.9 minutes). I use a common-reference design: the reference is folded once and fixed at 9,763 tokens, while only the hypothesis representation varies. The raw Arabic-script hypothesis scores 111.70% WER and 100.92% CER, with zero exact word matches. Latin transliteration gives 102.36% WER and 57.89% CER; folding it into the reference's reduced orthography gives 97.85% and 51.20%. Thus RAW-to-FOLDED reduces measured WER by 13.85 points and CER by 49.72 points; folding alone accounts for 4.51 and 6.69 points. Substantial error remains: 14.53% of reference tokens are exact matches, edits are substitution-dominated, and per-segment WER is higher for shorter segments. A Southern Kurdish fine-tuned system (aranemini/southern-kurdish-asr), scored under the same design, performs worse on every speaker (1,703 segments), with 109.56% WER and 55.85% CER. However, 12,330 output characters fall outside the folding table, so these rates must be recomputed against the corrected fixed reference. The MMS output also contains 613 unconverted or unmapped characters, showing that part of the residual error reflects scoring-pipeline limits rather than recognition alone. I will release the fixed reference and segment-level results, subject to source-corpus sharing terms, to support independent checking.

---


### 357. [Synthetic Data Augmentation for Satellite-Based Analysis of Battle-Damaged Agricultural Fields in Ukraine](https://arxiv.org/abs/2608.16380)

**<font color=#1a73e8>作者：</font>** Marta Sumyk, Oleksandr Kosovan, Iryna Voitsitska  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monitoring war-induced damage to agricultural land in Ukraine is important for understanding threats to food security, environmental stability, and post-war recovery. However, the development of computer-vision systems for satellite-based damage analysis is limited by the scarcity of labeled imagery, especially for damaged agricultural fields. This work investigates synthetic data augmentation as a method for improving classification under limited and imbalanced training data. We train class-conditional Generative Adversarial Network (GAN) and Denoising Diffusion Probabilistic Model (DDPM) architectures on real satellite images and use them to generate additional bombed and not-bombed agricultural-field samples. The generated images are used only for training augmentation, while all downstream evaluation is performed on an exclusively real test set. A Vision Transformer classifier is trained under multiple real and synthetic data configurations to measure the practical utility of each generative approach. The best configuration, based on balanced DDPM augmentation, improves accuracy from 84\% to 88\%, balanced accuracy from 67\% to 81\%, macro F1 from 65\% to 78\%, and recall for the underrepresented not-bombed class from 41\% to 69\%. These results demonstrate the potential of synthetic satellite imagery for data-scarce geospatial applications in war-affected regions.

---


### 358. [AstronOS: A Unified Execution Model and Runtime for Long-Horizon Agentic Systems](https://arxiv.org/abs/2608.16381)

**<font color=#1a73e8>作者：</font>** Zhenhang Nie, Gui Zheng, Xudong Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic systems often organize execution and state around a single conversation, model invocation, or agent instance, even when real work spans many calls and stages. We introduce a unified execution model that maintains a work item's persistent identity and versioned authoritative state across calls. Each step receives input scoped to a specific state version and new material; a result advances state only after validation and recording. We implement selected paths of this model in AstronOS using Cases, Tasks, and Scenario Packs across central and local execution. We compare five complete strategies for carrying an established software-version update plan into a fresh model session: rereading original materials, replaying full history, deterministic text summary, deterministic JSON, and the AstronOS runtime-mediated handoff. Ten controlled tasks are run under all five strategies with three repetitions, yielding 150 included executions. On the single-stage reference family, strategies perform similarly. In the primary three-stage A-C batch, AstronOS passes the frozen scorer in 14 of 15 executions, compared with 0 of 15 for rereading and 2 of 15 for full-history replay; later non-interleaved summary and JSON batches each pass 0 of 15. AstronOS has lower attempt-accounted model-token cost per passing execution, while requiring more execution-window time per attempt. These results associate the complete AstronOS condition with higher end-to-end pass rates across fresh sessions in this benchmark, at a measurable time cost.

---


### 359. [FETERS: Few-Shot Early Time-Series Classification via Effective Ratio Selection](https://arxiv.org/abs/2608.16385)

**<font color=#1a73e8>作者：</font>** Chen-An Tai, Yujia Wu, Vincent S. Tseng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Early time-series classification (ETSC) aims to make accurate predictions from partially observed time series as early as possible. Although various stopping mechanisms and feature learning strategies have been developed for ETSC, most existing methods assume access to sufficient labeled training data, which may be unrealistic in applications with limited annotation. Under limited supervision, learning an additional sample-level stopping module and extracting effective classification features can both become challenging. In this paper, we propose FETERS, a few-shot ETSC framework that selects a dataset-level stopping ratio through class-wise leave-one-out (LOO) evaluation on the support set and uses a penalty-based reward function to manage the accuracy-earliness trade-off, thereby avoiding the need to train an additional stopping module. FETERS further combines Rocket-based features with frozen Chronos representations for classification. Extensive experiments on 69 public datasets spanning 14 domains show that FETERS achieves state-of-the-art (SOTA) performance in the 5-shot setting, with the highest average harmonic mean (HM) and the best HM on 38 datasets, while outperforming the current SOTA method on 44 datasets. FETERS also remains competitive in the full-shot setting, demonstrating its effectiveness in managing the accuracy-earliness trade-off.

---


### 360. [Counting Documents Is Not Counting Text: Unit Bias in Web-PDF Corpus Statistics](https://arxiv.org/abs/2608.16390)

**<font color=#1a73e8>作者：</font>** Luca Foppiano  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> PDF corpora advertise their size in tokens but compute every rate they publish (coverage, OCR routing, re-fetch recovery, language mix) per document, and none decomposes its token total. The two units diverge sharply. On CC-MAIN-2021-31-PDF-UNTRUNCATED (7.9M web PDFs, 32.6B tokens), 3.02% of text-bearing documents hold half the tokens (Gini 0.807); documents over 50 pages are 5.00% of the corpus but 53.53% of its text. The PDFs produced by a TeX{} toolchain are 1.66% of documents and 4.05% of the text. The clearest casualty is Common Crawl's truncation cap: it affected 23.06% of documents and 63.08% of the text. Reconstructing the truncated files and extracting both versions, two widely used libraries recover 11.4% and 1.4% of that text; between 72% and 97% of affected documents yield nothing; roughly 55--62% of the corpus's text is lost. Under the 5 MiB cap adopted in March 2025, 30.19% of tokens would still be truncated, and recovery on those documents rises only from 3.3% to 13.2%. We recommend that corpus statistics be reported in both units: documents and tokens.

---


### 361. [Recovering Process Variables from Industrial Network Traffic via Search-Based Optimization](https://arxiv.org/abs/2608.16403)

**<font color=#1a73e8>作者：</font>** Chuan Sheng, Shan Jiang, Xiaogang Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Process variables (PVs) provide the process evidence needed for process-aware security monitoring in industrial cyber-physical systems (CPSs). However, existing supervisory infrastructures expose only the subset of PV values recorded by historians, leaving many additional runtime PV values unobserved. To address this incomplete process visibility, we study the problem of recovering PV fields and their semantics directly from raw industrial network traffic through protocol reverse engineering (PRE). In this setting, existing PRE methods face two practical challenges: PV-carrying communication is mixed with heterogeneous runtime traffic, and PV-carrying payloads are often long and deployment-specific. Mixed runtime traffic obscures the PV-carrying communication paths, while long payloads create a vast segmentation space in which early segmentation errors can propagate and corrupt the recovery of later fields under sequential inference. In this paper, we formulate the recovery of PV fields from raw network traffic as a search-based optimization problem. Our key insight is that non-sequentially identifying correct segmentations in such a vast segmentation space can be cast as an optimization problem and addressed by searching for near-optimal solutions. We propose PVParser to approach this goal. PVParser first reduces the search space by identifying the PV-carrying payloads from network traffic via a periodic pattern detection mechanism. It then employs a modified Monte Carlo Tree Search to explore near-optimal segmentations, reducing error propagation from incorrect early boundary decisions. Experiments on three representative industrial CPS datasets demonstrate that PVParser achieves high accuracy and F1-score in PV-carrying payload localization and PV field inference, outperforming six state-of-the-art PRE approaches by a significant margin.

---


### 362. [Reasoning-supported Robustness Validation of Automotive E/E Components](https://arxiv.org/abs/2608.16421)

**<font color=#1a73e8>作者：</font>** Jan Novacek, Alexander Viehl, Oliver Bringmann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents an ontology-supported approach to tackle the complexity of the Robustness Validation (RV) process of automotive electrical/electronic (E/E) components. The approach uses formalized knowledge from the RV process and stress, operating, and load profiles, so-called Mission Profiles (MPs). In contrast to the error-prone industrially established manual procedure, we show how component characteristics are formalized in OWL in order to form the foundation of an efficient automated analysis selection and decision support during the RV process. The proposed approach is based on the idea of mapping MPs to an OWL representation so to allow to perform semantic queries against MP data to improve their integration into the RV process. The resulting ontology-supported application framework has been applied to an industrial use-case from automotive power electronics. We present experimental results showing that the RV process can be significantly improved in terms of reduced design time and increased exhaustiveness by automating the analyses selection step and the provisioning of all the relevant data to be used.

---


### 363. [Joint Flow Matching Enables Continuous Dose-Conditioned Cell Morphing](https://arxiv.org/abs/2608.16424)

**<font color=#1a73e8>作者：</font>** Lea Bogensperger, Manuela Merlo, Martin Baumgartner 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative modeling has shown increasing promise for predicting cellular perturbation effects under chemical compound treatments. Existing approaches either model perturbation as a distribution-to-distribution mapping without explicit concentration handling, or treat concentration as a discrete class label, precluding continuous dose control. We introduce a joint flow matching approach that simultaneously models cell latents and drug concentration via a dual-timestep formulation, enabling dose-conditioned single-cell morphing through the invertibility of flow matching. The joint formulation induces a monotonic dose-response geometry in latent space and additionally supports concentration estimation from cell morphology. As proof of concept, we further demonstrate generalization to an unseen dose held out during training. Empirically, our method achieves competitive or improved per-concentration metrics on two compounds compared with representative baselines, while enabling capabilities structurally unavailable to discrete-class methods.

---


### 364. [Visualizing Uncertainty-to-Action Composition for Human Oversight](https://arxiv.org/abs/2608.16428)

**<font color=#1a73e8>作者：</font>** Chisom Anyabolu, Akshat Dubey, Georges Hattab  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence systems often disclose uncertainty, yet they rarely make clear what response that uncertainty should trigger. Most uncertainty visualizations encode uncertainty in model outputs, leaving users to discern the most appropriate course of action. A second region of the design space--uncertainty in the decision process itself, including how multiple uncertainty conditions compose into an oversight response-- remains comparatively underexplored. We address this gap with two coupled contributions. First, we introduce an uncertainty-to-action binding framework that composes multiple uncertainty conditions into a single oversight response under a precedence policy with a contextual safety modifier. That response concerns whether and how an AI-supported decision may proceed, not the substantive domain decision itself. Second, we present ActionCue, a process-transparency visualization that renders that composition explicit. We demonstrate the approach through a three-way comparison with confidence-only and data-level uncertainty displays, using worked cases from healthcare, credit assessment, and disaster forecasting. Together, the framework specifies how uncertainty conditions are resolved into an oversight response, and the visualization makes that resolution inspectable rather than implicit.

---


### 365. [Drive, Pack, Fly: The Travelling Thief Problem with Drone](https://arxiv.org/abs/2608.16435)

**<font color=#1a73e8>作者：</font>** Kabir Murjani, Abhay Sobhanan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In collection operations, accumulating payload progressively slows the vehicle, imposing a cumulative penalty on routing efficiency. An onboard drone can offset this penalty by retrieving outlying items, thereby shortening the makespan and increasing operational profit. However, travel time remains load-dependent, and each item collected by the ground vehicle shifts the arrival times that govern the drone's launch and rendezvous points. This paper introduces the Travelling Thief Problem with Drone (TTP-D), which maximises the collected profit, net of a time-based rental cost, by jointly optimising item selection, vehicle routing, and flight synchronisation. We formulate a mixed-integer linear program that solves small instances to optimality, and develop both metaheuristics and an attention-based Deep Reinforcement Learning (DRL) policy for larger instances. We further propose a learner-initialised hybrid solver, in which the DRL policy constructs an initial solution that a short annealing run subsequently refines. On two benchmark sets, this hybrid recovers most of the metaheuristic baseline's quality at a fraction of its computational budget, although the largest instances still require the baseline at its full budget. Finally, a sensitivity analysis reveals that the rental ratio is the primary driver of profitability, whereas the fleet parameters affect profit only at the margin.

---


### 366. [Experimental Validation and Mitigation of RRC Storm Attacks in 5G Cellular Networks](https://arxiv.org/abs/2608.16441)

**<font color=#1a73e8>作者：</font>** Abdallah Abou Hasna, Ammar El Falou  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The initial access phase of the 5G system remains sensitive because the base station (gNB) must allocate radio resources before the user is fully authenticated. In particular, the random access channel (RACH) procedure can be abused to generate large numbers of incomplete connection attempts, creating a signaling storm that consumes gNB resources and prevents legitimate users from connecting successfully. In this paper, we implement this signaling storm attack using the OpenAirInterface project and validate it on a real testbed composed of software-defined radios and commercial phones. We then design and implement a lightweight mitigation technique that operates directly at the gNB by monitoring and acting on suspicious half-open connections. To make the system observable in practice, we also develop a network management interface that visualizes the network state in real time and highlights suspicious activity during the attack phase. Finally, the work is released as open source so that other researchers can reproduce our results, build on the implementation, and evaluate new mitigation strategies.

---


### 367. [Time to Reason: Scalable Neurosymbolic Learning for LTLf via Fuzzy Semantics](https://arxiv.org/abs/2608.16443)

**<font color=#1a73e8>作者：</font>** Riccardo Andreoni, Andrei Buliga, Alessandro Daniele 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neurosymbolic (NeSy) Artificial Intelligence aims to integrate Deep Learning (DL) architectures with symbolic reasoning. While initial NeSy approaches have targeted mainly symbolic reasoning in propositional and first-order logics, recent works have started to address the construction of neurosymbolic frameworks for Temporal Logics, and in particular for LTLf. These approaches have established temporal NeSy as a promising research direction, laying the foundations for learning under temporal constraints. Nonetheless, they leave many questions unanswered. From a theoretical perspective, several differentiable semantics for interpreting LTLf have been proposed but have not yet been formally and systematically defined within a unified framework. Moreover, existing approaches commonly rely on automata to represent temporal knowledge, resulting in limited scalability. Motivated by this research gap, this paper provides the following contributions: (i) formally defining different fuzzy semantics for LTLf, and systematically analysing theoretical properties regarding equivalences and dualities of temporal operators; (ii) showing how these semantics can be directly integrated within a novel NeSy framework, called DiffLTLf, enabling flexible and scalable learning without relying on the usage of automata; and (iii) introducing a novel evaluation protocol of increased complexity of learning tasks w.r.t. existing benchmarks. Our results show that the choice of fuzzy semantics has a significant impact on predictive performance. Moreover, DiffLTLf achieves performance on par with, and sometimes superior to, state-of-the-art probabilistic approaches while substantially improving scalability. Taken together, these results establish direct fuzzy interpretations as a competitive and scalable alternative to existing temporal NeSy frameworks.

---


### 368. [Contrastive Energy Fields for Inference-Time Procedure Planning in Instructional Videos](https://arxiv.org/abs/2608.16457)

**<font color=#1a73e8>作者：</font>** Mohamed Afham, Christoph Reich, Oliver Hahn 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Procedure planning seeks to estimate a sequence of actions to transition from an observed initial state to a given goal state. Current procedure planning approaches directly predict action sequences from latent representations using feed-forward neural networks or diffusion-based inference. These paradigms treat every action as plausible, lacking the ability to enforce task-specific logical constraints that render certain actions irrelevant or not plausible. We propose CEFITO, a procedure planning approach that learns a predictor to express an action-conditioned representation space. Based on this representation space, we formulate procedure planning as a task-constrained optimization problem. Unlike prior methods, CEFITO explicitly reasons over the action space by omitting irrelevant actions during inference-time planning. This reformulation enables effective procedure planning and achieves state-of-the-art accuracy on two established procedure planning benchmarks.

---


### 369. [Shared-Structure 4D Spectral Gaussian Representation for Sparse-View Spectral CT Reconstruction](https://arxiv.org/abs/2608.16463)

**<font color=#1a73e8>作者：</font>** Jiancheng Fang, Shaoyu Wang, Wenjun Xia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse-view spectral computed tomography (CT) reconstructs energy-resolved attenuation volumes from limited projection views, requiring simultaneous handling of angular undersampling and spectral coupling. We propose a SharedStructure 4D Spectral Gaussian Representation (4D-SG) that learns shared Gaussian geometry from full spectrum structural projections and uses a Gaussian-wise Spectral Density Curve Network (GSC-Net) to predict Gaussian raw density transformations. This factorization separates shared spatial structure from spectral attenuation variation, avoids independent channel geometry optimization, and establishes a continuous 4D-SG representation from discrete spectral measurements for unobserved spectral channel queries. Experiments on six synthesized, simulated projection, and real projection datasets with 50 views demonstrate the best average performance. Compared with the strongest Gaussian baseline, 4D-SG improves PSNR from 35.56 dB to 36.61 dB, increases SSIM from 0.909 to 0.914, and reduces LPIPS from 0.208 to 0.194, demonstrating its effectiveness for sparse-view spectral CT reconstruction.

---


### 370. [Sterilizable Scene Graph Generation for Operating Rooms](https://arxiv.org/abs/2608.16469)

**<font color=#1a73e8>作者：</font>** Nick Lemke, Ssharvien Kumar Sivakumar, Antoine P. Sanner 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scene graph generation from surgical video enables a holistic and structured understanding of surgical scenes by modeling objects and their semantic relationships. Despite recent advances, state-of-the-art approaches rely on large, parameter-heavy deep learning models that are impractical for deployment in the operating room (OR) due to hardware footprint, hygiene constraints, latency, and data privacy concerns. To the best of our knowledge, this is the first scene graph generation method built on NCAs and the first NCA framework capable of learning structured representations. We introduce SG-NCA, a lightweight scene graph generation framework based on Neural Cellular Automata (NCA), designed for inference in fanless devices critical for OR hygiene protocols. SG-NCA is the first scene graph generation combining NCA-based multiclass segmentation for efficient object detection and feature extraction with a lightweight relation predictor. We evaluate SG-NCA on videos of cataract surgery and cholecystectomy, demonstrating performance comparable to established baselines while requiring 55x fewer parameters. We showcase deployment on fanless edge devices better suited for the OR and demonstrate downstream applications such as surgical video captioning, highlighting SG-NCA's potential for affordable, privacy-preserving, and OR-ready intraoperative scene understanding.

---


### 371. [Reference-free logged energy-oracle recovery for neural approximations of symmetric coercive variational problems: conforming Riesz reconstruction and archive-level selection](https://arxiv.org/abs/2608.16473)

**<font color=#1a73e8>作者：</font>** Karim Bounja, Lahcen Laayouni, Boujemaa Achchab 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural PDE training yields a finite checkpoint archive, yet its logged energy errors are inaccessible without the exact solution, while loss-based selection does not necessarily recover the logged energy oracle. For admissible neural approximations of symmetric coercive variational problems, we introduce a reference-free selection rule based on minimizing a computable conforming Riesz monitor. The exact residual-energy identity and conforming projection make the monitor an unconditional lower bound converging monotonically to each logged energy error under nested conforming refinement; under saturation, hierarchical enrichment yields a computable upper estimate and hence a lower-upper bracket. A key finding is that archive selection is order-sensitive: unresolved checkpoint-dependent components can reverse the oracle-non-oracle ranking at finite resolution, so checkpointwise recovery alone is insufficient. For finite archives, we prove uniform recovery, yielding convergence to the logged-oracle error and, without saturation, logged-oracle selection at sufficiently fine auxiliary resolution. Under saturation, the bracket gives a computable near-oracle bound and certifies unique logged-oracle selection upon interval separation. We also bound logging-resolution loss and certify oracle inclusion over prescribed comparison trajectories. The resulting criterion replaces inaccessible exact-error minimization by computable, training-independent post-training selection on the intrinsic energy-error scale, requiring only the computed candidates and the variational problem. Experiments on diffusion and elasticity, including a non-manufactured perforated plate, demonstrate energy-scale calibration, oracle-level selection, and modest post-processing cost.

---


### 372. [Offline Reinforcement Learning for Hemodynamic Management of Sepsis in the ICU: a MIMIC-IV Study with Dual Off-Policy Evaluation](https://arxiv.org/abs/2608.16482)

**<font color=#1a73e8>作者：</font>** Marc Pérez-Roig, David Fernández-Narro, Carlos Sáez  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The dosing of intravenous fluids and vasopressors in sepsis is a sequential decision made under uncertainty and guided largely by clinical judgment, which makes it a natural target for reinforcement learning from historical care. Because a learned policy cannot be trialed on patients, its value must be estimated off-policy, and such estimates can be fragile and optimistic. This work advances the reliable evaluation of sepsis treatment policies by combining off-policy estimation, reliability diagnostics, and clinician-agreement analyses in a transparent validation framework. We modeled fluid and vasopressor dosing on a cohort of 36,872 septic ICU stays drawn from the MIMIC-IV critical-care database, as a discretized Markov decision process with 1,000 states and 25 actions, defined by a five-by-five grid of fluid and vasopressor levels and solved by policy iteration. The clinicians' behavior policy was estimated with a random forest, which mitigated the collapse of the Effective Sample Size (ESS 50.1 against 4.0 with smoothed counts) that otherwise destabilizes the importance-sampling estimate. The learned policy was evaluated with two estimators, weighted importance sampling (WIS) and fitted Q evaluation (FQE), with the ESS and clinician agreement as reliability checks. An empirical variable selection found that the composition of the state matters more than its size. Both estimators place the learned policy above the clinicians' return (WIS 50.8 and FQE 46.8 against 38.2, ESS 50.1), yet it departs only modestly from observed practice (total variation 0.18), favoring less intravenous fluid. These retrospective single-center off-policy results support the learned policy as a clinically plausible refinement of observed practice and motivate its further evaluation as a discordance-based clinical decision-support approach.

---


### 373. [HiFi-BRep: High-Fidelity Latent Representation for Robust B-Rep Generation](https://arxiv.org/abs/2608.16485)

**<font color=#1a73e8>作者：</font>** Junhao Hou, Chenqi Luo, Pufan Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Boundary representation (B-Rep) generation is a fundamental task in computer-aided design, yet the direct synthesis of high-fidelity and structurally valid B-Reps remains a major challenge. Existing deep generative methods suffer from two forms of brittleness: representation brittleness, caused by padding noise and feature contamination in the latent space, and generation brittleness, stemming from sequential error propagation and a train-inference mismatch due to non-differentiable validity enforcement. We propose HiFi-BRep, a novel framework that addresses these limitations through two synergistic contributions. First, a topology-aware encoder constructs a high-fidelity latent representation by eliminating padding via learnable queries and preventing feature contamination with topology-guided attention. Second, a single-stage decoder jointly predicts geometry and topology in parallel, embedding core manifold constraints as a differentiable learning objective. This design ensures mutual guidance between geometry and topology while avoiding cascaded errors. Extensive experiments show that HiFi-BRep significantly outperforms state-of-the-art methods in both structural validity and geometric fidelity, providing a robust solution for high-quality B-Rep synthesis. Code and models are publicly available at this https URL.

---


### 374. [Towards Real-Time and Adaptable LiDAR Scene Completion](https://arxiv.org/abs/2608.16490)

**<font color=#1a73e8>作者：</font>** Azhar Hussian, Martin Vossiek, Vasileios Belagiannis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDAR scene completion is a key component of 3D perception in autonomous driving, where the scene must be completed in real time to be usable in downstream tasks. Existing approaches typically follow an initialize-and-refine paradigm, in which a coarse initialization of the scene is first constructed, then refined into complete 3D geometry. Generative models are slower because they iteratively refine random Gaussian noise into the scene, while non-generative methods perturb the partial scene with a fixed noise scale, which limits coverage of large gaps and occluded regions and requires manual recalibration for each new sensor configuration. We present RapidLiDAR, a LiDAR scene completion method that treats the initialization itself as a learned, data-driven component. We propose an adaptive initialization module that predicts a spatially varying displacement for each partial input point, expanding the partial observations into a coarse scene initialization adapted to the local geometry, without requiring manual noise tuning. To refine this coarse initialization into a complete and coherent scene, we additionally propose a multi-scale reconstruction module that further refines point positions by querying multi-scale 3D voxel and 2D BEV feature maps constructed from the input scan. By replacing point-neighborhood operators such as farthest point sampling and $k$-nearest neighbor search with voxel- and BEV-based feature extraction, our architecture is faster and can handle different input resolutions by design. Experiments on SemanticKITTI and KITTI-360 show that our method achieves completion performance on par with the state of the art while completing a full scene in 0.1 seconds, which is 2.3 times faster than the fastest prior method. This matches the 10 Hz acquisition rate of typical automotive LiDAR sensors, taking a step toward real-time LiDAR scene completion.

---


### 375. [Graph Machine Learning: An Opportunity for Power Systems](https://arxiv.org/abs/2608.16494)

**<font color=#1a73e8>作者：</font>** Martin Sadric, Sebastian Pütz, Christian Nauck 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern power systems face growing operational complexity driven by the integration of renewable energy sources, decentralization, and the need for real-time decision-making across a wide range of timescales. Addressing these challenges traditionally relies on model-based methods that, while accurate, can be too slow for operational demands. Machine learning (ML) has therefore emerged as a faster, data-driven alternative. As grid topology plays a central role in power system operation, graph machine learning (GML) methods offer a natural framework for incorporating topological dependencies as an inductive bias. We survey nearly 800 papers at the intersection of GML and power systems, covering forecasting, state estimation, optimization, control, fault diagnosis, and cybersecurity. Power systems constitute an unusually rich benchmark setting for GML, as they combine hard physical constraints, multi-scale dynamics, safety-critical requirements, and scarce labeled data within a single, well-defined domain. Conversely, power systems can benefit from utilizing GML to complement classical solvers, as GML provide scalable, topology-aware approximations with promising generalization and computational efficiency. We identify open challenges, including limited real-world deployment and the need for interpretable models in safety-critical settings. Despite the rapidly growing number of publications, standardized benchmarks and open datasets remain scarce, leaving many results difficult to reproduce and undermining the long-term scientific credibility of the field. We further derive a structured requirements catalog for ML-ready power grid benchmarks, intended to guide future dataset development and improve reproducibility across studies. We call on the community to prioritize dedicated benchmark studies and the release of open datasets and models.

---


### 376. [When Tool-Backed Skill Retrieval Fails: Source-Style Collapse in Executable Capability Retrieval](https://arxiv.org/abs/2608.16502)

**<font color=#1a73e8>作者：</font>** Yiqi Liu, Joseph James, Yang Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale agents increasingly rely on retrieval to access external capabilities. We study this retrieval gate in structured tools and APIs, a measurable class of tool-backed executable skills that must be surfaced before an agent can plan, incorporate, or act. In this setting the retrieval layer can silently fail even when the capability corpus is fixed: on ToolRet, a retriever fine-tuned on one source-specific slice collapses on another source-specific slice of the same benchmark, with FT-1100 despite its higher lexical overlap with the gold tools. We call this failure mode source-style collapse. Query-side TF-IDF fingerprints flag source styles on which the fine-tuned retriever is likely to fail better than semantic or length-based proxies, giving a cheap signal for mismatch over a fixed tool corpus. We propose ToolScout, a source-aware routing method that uses this signal as a routing guard: on the mixed 4,996-query stream, TF-IDF-based routing raises coverage from 22.3% to 86.1%, and across five collapsed sources 20 matched examples raise the coverage-weighted global top-1 proxy from 1.3% to 53.9%. The same failure and routing behaviors persist when tools are rerendered as executable skill cards, which rules out raw API-schema format as the sole cause.

---


### 377. [FLEET: Token-Based Feature Extraction for Event Camera-based Reinforcement Learning](https://arxiv.org/abs/2608.16523)

**<font color=#1a73e8>作者：</font>** Tristan Gottwald, Maximilian Schier, Melanie Schaller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras generate asynchronous, high-frequency data streams offering spatially sparse information at lower latency than traditional this http URL principle, these properties should be ideal for the design of control this http URL, reinforcement learning research in this field remains limited as existing approaches fail to fully exploit the sensor's this http URL-based methods negate the sensors benefits by aggregating events into sparse grids. This couples compute cost to sensor resolution and blurs the temporal information. Meanwhile, existing generative baselines rely on the availability of trajectory data to pretrain the model. We propose FLEET (Feature Learning from Events via Efficient Tokenization), a feature extractor that processes event sequences directly. Leveraging random Fourier features and cross-attention, our architecture compresses variable streams into fixed-size latent representations. This decouples inference cost of the feature extractor's backbone from the sensor's resolution, enabling end-to-end learning without auxiliary losses. We validate FLEET on a new, high-throughput benchmark. The results demonstrate that our sequence-based approach surpasses SOTA performance and exhibits superior robustness to variations in observation frequencies.

---


### 378. [Automatic Cephalometric Landmark Localization on CBCT-Derived Digitally Reconstructed Radiographs for Skeletal Malocclusion Classification](https://arxiv.org/abs/2608.16535)

**<font color=#1a73e8>作者：</font>** Benjamin Hou, Konstantinia Almpani, Janice S. Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Manual cephalometric landmark annotation is important for craniofacial assessment but is labor-intensive and difficult to scale. We introduce CephViT, a Vision Transformer-based model for automated 2D lateral cephalometric landmark localization, and evaluate its use in downstream skeletal malocclusion classification. CephViT was trained and benchmarked on a public lateral cephalogram dataset, achieving a mean radial error of 1.28 +/- 1.42 mm and a successful detection rate of 92.0% at 3.0 mm. Because the private evaluation cohort consisted of 3D CBCT scans, lateral cephalogram-like digitally reconstructed radiographs (DRRs) were generated from each volume and used as 2D inputs to the landmark localization model. Landmark coordinates were normalized into a common coordinate frame, and skeletal malocclusion classification was performed using landmarks shared between the reference and DRR-based pipelines. Classification performance using DRR-localized landmarks was comparable to that obtained using manually annotated reference landmarks, with accuracies of 70.0% and 68.3%, respectively. These results support the feasibility of automated cephalometric analysis on CBCT-derived DRRs for skeletal malocclusion assessment.

---


### 379. [One Residual with Three Reuses: A Wristband Front End for Gesture Sensing](https://arxiv.org/abs/2608.16542)

**<font color=#1a73e8>作者：</font>** Sam Rifaki  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous wrist-worn hand sensing for gesture interfaces and motor symptom monitoring needs an always-on front end that fits inside a coin-cell power budget while pairing a micro-electro-mechanical-systems (MEMS) inertial measurement unit (IMU) with a 60 GHz frequency-modulated continuous-wave (FMCW) radar to stay robust under occlusion and on-body drift. We present a design study of such a wristband front end in which classifier wake-up gating, mmWave versus IMU routing, and innovation-based EKF measurement reweighting share a single on-chip residual generator. The shared generator occupies 14.4 KB of program memory and 278 B of state and runs at 110K multiply-accumulates (MACs) per frame on an Ambiq Apollo4 Blue Plus class edge microcontroller unit (MCU). Across four public sensor data corpora (IPN Hand, SHREC 2021, MiliPoint 60 GHz FMCW radar, EAT-Radar) the front end reaches detection probability $P_D = 0.72/0.80$ at a 1% false-alarm rate, sustains a 47% classifier invocation energy reduction at 90% gesture detection recall, and lowers pose tracking root-mean-square error by $4.6\times$ under measurement bias drift relative to an adaptive Kalman with $R$-inflation baseline. Measured silicon power and on-body capture are deferred to follow-on hardware; the contribution here is a design study.

---


### 380. [VCE-Skill: Enhancing Skill Self-Evolution with Version-Change Experience](https://arxiv.org/abs/2608.16544)

**<font color=#1a73e8>作者：</font>** Jianming Chen, Xuanbin Ye, Yawen Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Agents increasingly rely on reusable skills to encode task knowledge, tool-use procedures, and validation rules. Existing skill self-evolution methods primarily revise skills using execution trajectories collected from current tasks, leaving the evolution knowledge accumulated in public skill version histories largely untapped. Our pilot study reveals a clear complementarity between the two sources: public skill changes provide reusable evolution priors, whereas trajectories provide evidence grounded in the current task. Motivated by this, we propose VCE-Skill, which distills noisy and implementation-specific public skill changes into reusable, structured version-change experience and adaptively fuses it with trajectory-derived proposals from the base evolver, thereby exploiting external experience while retaining task-specific evidence. Extensive experiments demonstrate that VCE-Skill improves skill self-evolution, increasing mean scores by 3.20--4.98 points; transfer experiments further show that the resulting skills achieve stronger cross-model transfer performance. Our work highlights public skill version changes as a previously underexplored yet effective source of prior knowledge and advances trajectory-driven skill self-evolution.

---


### 381. [Supervising the Path to Fine Scales: GalerkinFlow for Scientific-Field and Image Super-Resolution](https://arxiv.org/abs/2608.16546)

**<font color=#1a73e8>作者：</font>** Zikang Zhan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most super-resolution models learn from paired data by supervising only the final high-resolution output. This provides little control over how the prediction should evolve between the downsampled observation and its fine target. We introduce GalerkinFlow, an equation-agnostic framework that turns each coarse--fine pair into supervision along an entire reconstruction path. At a random sample of intermediate states on the reconstruction path, the model predicts the coarse-to-fine residual velocity and uses coarse-anchor point to define a pseudo-endpoint. We show that the reconstruction loss of this pseudo-endpoint is exactly related to the intermediate velocity loss through a known time-dependent weight. Consequently, every intermediate state contributes supervision toward the same fine target, rather than serving only as an internal step toward an endpoint loss. Because intermediate states already reveal part of the missing fine-scale structure, we additionally supervise the coarse endpoint used during one-step inference. A finite-difference objective further constrains local spatial variation. GalerkinFlow combines convolutional features with scale-conditioned Galerkin operator mixing and requires no governing equation or physical metadata. It achieves the lowest raw-space errors among the evaluated equation-agnostic baselines on Navier--Stokes and Darcy Flow, while remaining competitive on DIV2K.

---


### 382. [DeepInsight II: One Trace from Benchmark to Robot](https://arxiv.org/abs/2608.16556)

**<font color=#1a73e8>作者：</font>** Siyi Li, Yuchen Kang, Wuliang Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Across a Physical AI stack, evaluation maturity is inversely aligned with deployment risk: foundation models enjoy mature, standardized harnesses, while the embodied layers on which deployment actually turns remain fragmented across benchmark-specific simulators, embodiments, and interfaces. The first DeepInsight report (v1) unified evaluation across this stack behind three abstractions---task, resource, and result---but its quantitative evidence centered on the foundation-model layer; navigation and manipulation (System 1) and whole-body control (System 0) remained simulation case studies, and physical execution was outside its empirical scope. DeepInsight II keeps that substrate fixed and quantifies the embodied half. First, it reproduces released-checkpoint references across two navigation and four manipulation benchmarks under their native protocols. Second, MotionBench places four released whole-body controllers under one workload and metric contract, then carries a qualified within-family cohort from parallel simulation to matched real-robot trials in which simulated and physical rollouts share a parent trace identity while retaining execution-domain-specific records, making the sim-to-real gap a native reduction rather than a reconciliation across toolchains. Third, a composed System 2--1--0 study extends trace localization into five evidence-grounded handoff labels, each mapped to a concrete repair action, with a measured repairability criterion and physical episodes testing the same attribution under hardware-observable state. The contribution is therefore not a new evaluation architecture, but empirical continuity from benchmark execution to matched robot evidence and repair-oriented diagnosis.

---


### 383. [CUBICS: Situation-aware performance estimation for safety-relevant ML components](https://arxiv.org/abs/2608.16564)

**<font color=#1a73e8>作者：</font>** Benjamin Herd, Jessica Kelly, Mario Trapp  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine learning (ML) is a key technology driving innovation today, but ensuring ML safety remains a major challenge for safety-related applications. A promising idea is to build proven-in-use arguments from field data, e.g. by running ML components (MLCs) in shadow mode or within safety envelopes so that their outputs can be monitored as 'safe probes' without affecting safety. These probes can then be used to build a statistical argument about field performance in a Bayesian way. However, many Bayesian field-data approaches in safety engineering model failures as a simple Bernoulli (or binomial) process with a single global failure probability and i.i.d. trials, which is rarely adequate for MLCs whose performance depends strongly on context. Statistical evidence is also about coverage of relevant situations, including edge cases, and building a single integrated statistical model for the entire system is usually not feasible. To address these challenges, this paper introduces CUBICS, a context-modular framework for per-component, situation-aware performance estimation of safety-relevant ML components. CUBICS partitions the operational design domain into situations and, for each safety-relevant component, defines a set of situation-specific assumptions and probabilistic guarantees that are represented and updated in a Bayesian manner using Subjective Logic (SL). By combining these guarantees with beliefs about how often each situation occurs, CUBICS derives an overall risk estimate for each component without requiring a monolithic system-level statistical model, and thus provides a building block for modular, field-data based safety assurance.

---


### 384. [Probabilistic Circuits as Reasoning Machines in Artificial Intelligence (Part I)](https://arxiv.org/abs/2608.16565)

**<font color=#1a73e8>作者：</font>** Robert Peharz  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This cumulative habilitation thesis studies probabilistic circuits (PCs) as a powerful and tractable framework for reasoning and learning under uncertainty in artificial intelligence (AI). It first advocates for probability as a core language for AI, emphasizing its connections to logic and information theory; the conceptual simplicity of probabilistic reasoning---based primarily on the sum and product rules; the parallels between probabilistic inference and human cognition; and the role of probability in optimal decision making. However, probability also faces significant computational challenges, as probabilistic inference is NP-hard in almost all probabilistic models. PCs address these challenges through structural constraints that ensure exact computation of a wide range of inference queries in polynomial time, such as marginals, conditionals, most probable explanations, expectations, and more advanced inference tasks. This thesis synthesizes a decade of research across foundations, algorithmic developments, and empirical validation of PCs. Key contributions highlighted in this work are foundational theory of PCs, Bayesian approaches for learning PCs, scalable implementations and integration with deep learning, hybrid models that combine PCs with intractable models, and connections with symbolic machine learning paradigms.
This is the first part of my Habilitation Thesis. The second part is omitted, as it comprises the cumulative part of the thesis and has been published at various venues (see Chapter 5).

---


### 385. [Learning Generalizable Reconstruction of High-Dimensional Neural Dynamics](https://arxiv.org/abs/2608.16569)

**<font color=#1a73e8>作者：</font>** Anima Kujur, Zahra Monfared  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate reconstruction of long-duration neural recordings is challenging because local field potentials (LFPs) are high-resolution, multichannel, transient, and variable across subjects. We present PCA-DMD, a scalable operator-theoretic framework that segments LFP recordings into overlapping windows, projects them into a compact PCA space, learns linear Koopman evolution in the latent space, and reconstructs continuous signals through inverse projection and overlap-add aggregation. On 200,000-sample hippocampal recordings, PCA-DMD outperformed Classical DMD, SpDMD, MrDMD, and HODMD, achieving KLD=0.0761 and HD=0.0847. In all-pair cross-subject zero-shot generalization at 300,000 samples, correlations were 0.9504-0.9800, with HD=0.0010-0.0072 and KLD=0.0005-0.0022, without target-subject fine-tuning. Out-of-sample temporal prediction showed close one-step agreement on temporally held-out LFP segments across the unseen interval and multiple channels. Scalability analysis from 400,000 to 900,000 samples showed stable zero-shot reconstruction, with mean correlation remaining about 0.965-0.968 while computational cost increased predictably. External validation on an independent 93-channel Allen Neuropixels recording yielded mean and median channel-wise correlations of 0.7427 and 0.7990, respectively. Koopman spectral and mode analyses revealed dominant eigenvalues concentrated near the unit circle. PCA-DMD therefore provides an interpretable, generalizable, and computationally scalable framework for reconstructing high-dimensional neural dynamics.

---


### 386. [SQuad: Sub-Quadratic Attention Distillation for Efficient Video Generation](https://arxiv.org/abs/2608.16585)

**<font color=#1a73e8>作者：</font>** Animesh Karnewar, Denis Korzhenkov, Amirhossein Habibian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Diffusion Transformers (DiTs) spend most of their compute inside the Self-Attention operation, whose cost grows quadratically, $\mathcal{O}(n^2)$, with the number of latent tokens $n$. For the task of video generation, the token count is large, so this term dominates runtime and memory, and thereby caps the resolution and duration we can generate. Linear $\mathcal{O}(n)$ and low-rank $\mathcal{O}(nk)$ surrogates of Self-Attention trade the full softmax $QK^T$ for cheaper kernels, but rarely recover the original's expressivity, leaving a stubborn quality gap. Motivated by this, we propose SQuad, a Sub-Quadratic Attention Distillation framework that achieves a complexity of $\mathcal{O}(n\sqrt{n})$ in the resulting distilled Attention, naturally balancing the efficiency v/s expressivity trade-off. Instead of training our own Video DiT from scratch, which is prohibitively expensive, we fit a pretrained full softmax Self-Attention DiT into our proposed SQuad-Attention one by distilling the former in two stages: Flow-Matching Supervised Fine-Tuning (SFT), followed by improved Distribution Matching Distillation (DMD2) which additionally makes the sampling more efficient. On the Wan~2.2 5B text-to-video model, SQuAD matches the quadratic teacher on VBench ($83.20$ v/s $83.08$) while cutting the per-step per-block attention FLOPs by $\sim$$67\times$ and attention latency by $\sim$$11\times$, and end-to-end DiT latency by 2$\times$, all while also generating a video in only $6$ Neural Functional Evaluations (NFEs) instead of the default $100$.

---


### 387. [Ultra: Unsupervised Cross-Task Optimization for Reliable Restoration Segmentation Collaboration under Adverse Weather](https://arxiv.org/abs/2608.16589)

**<font color=#1a73e8>作者：</font>** Shiqin Wang, Zhiqian Li, Haoyuan Du 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised Domain Adaptation for Adverse Weather Semantic Segmentation (UDA-ASS) aims to transfer semantic knowledge from labeled normal-weather images to unlabeled adverse environments. Existing approaches implicitly assume that restoration and segmentation provide mutually beneficial guidance. However, under severe degradation and without target-domain supervision, the validity of cross-task optimization directions becomes fundamentally unidentifiable, leading to hallucination-driven error propagation. In this work, we propose a novel Unsupervised Restoration-Segmentation Collaborative Learning Framework (Ultra), which reframes cross-task interaction as direction selection under uncertainty and causal effect estimation, enabling reliable collaboration through candidate direction generation and intervention-based filtering. In detail, we propose CTDN and CMIL. The former exploits complementary visual structures and semantic information to generate candidate optimization directions and performs cooperative direction selection between restoration and segmentation. The latter reformulates cross-task information transfer from correlation-based propagation into causal effect assessment, suppressing hallucination propagation. Extensive experiments on three widely used UDA-ASS benchmarks demonstrate state-of-the-art segmentation performance. Beyond segmentation, our framework achieves better unsupervised restoration results than existing UDA-ASS restoration methods and generalizes to unsupervised restoration and object detection collaboration tasks. Code and models will be available at this https URL.

---


### 388. [Towards Zero-Shot Domain Generalization for ID Cards Presentation Attack Detection](https://arxiv.org/abs/2608.16591)

**<font color=#1a73e8>作者：</font>** Mario Nieto-Hidalgo, Juan M. Espin, Juan E. Tapia  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Presentation-Attack Detection (PAD) for national ID cards is limited by the lack of publicly available genuine samples, making it difficult for systems to generalize across countries. This paper introduces two main innovations: (1) a Prototypical Network head using an EfficientNet-V2-b0 backbone that requires only four genuine samples per class to create reliable prototypes; and (2) an episodic training regime that keeps PAD classes fixed while varying the card domain, allowing the network to learn universal attack cues.
Evaluated on a large multi-country dataset and the public DLC-2021 benchmark, this method achieves an average Equal Error Rate of around 9\%, outperforming conventional softmax and CLIP zero-shot baselines even with data from a single source country. This approach provides accurate, privacy-preserving PAD while minimizing data collection, facilitating scalable cross-jurisdictional remote onboarding.

---


### 389. [Rigorous Statements and Proofs of the Lemmas in Simon's Algorithm for the Dihedral Coset Problem and Their Underlying Hypothesis](https://arxiv.org/abs/2608.16598)

**<font color=#1a73e8>作者：</font>** Yuchen Guo, Shuo Yang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In a recent preprint, Simon proposed a polynomial-time quantum algorithm for the Dihedral Coset Problem and rested the analysis on four lemmas. Three of them carry only proof sketches, and this paper gives each of those three a statement that admits a single reading together with a complete proof. Lemma 1 follows from an exact second-moment computation for the subset-sum counts, and it holds with probability tending to one in place of the constant originally claimed. The amplitude bound of Lemma 3 follows from an exact Parseval identity on the cube of measurement outcomes and holds at every threshold with no well-behavedness hypothesis, so that predicate leaves the argument entirely. For Lemma 4, we compute both balls-in-bins covariances exactly and find that the second carries a term a fixed ball count leaves out. The assumption that the distinguished group contains no faulty samples can also be dropped. The two branch amplitudes share a signed prefactor, so the counting estimates control their difference and not the ratio the lemma states. We prove the additive form and show that the closing argument consumes nothing more than that. A single hypothesis survives all of this. It asks that the partition into the two sides be fixed independently of the measured string, and the rule the algorithm gives for choosing that partition does not supply it. Establishing these four lemmas therefore does not by itself establish the correctness of the algorithm.

---


### 390. [GeoPose: Patient-agnostic CTA-to-DSA registration through projection-space calibration](https://arxiv.org/abs/2608.16600)

**<font color=#1a73e8>作者：</font>** Rudolf L. M. van Herten, Robert Graf, Paula Feldman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aligning intraoperative biplanar digital subtraction angiography (DSA) to pre-procedural computed tomography angiography (CTA) requires rapid and accurate 3D-to-2D registration. Optimization-based methods are sensitive to initialization and may require hundreds of iterations, whereas learning-based approaches commonly rely on patient-specific training. We propose GeoPose, a population-trained framework that estimates the C-arm pose in a learned canonical frame and transfers it to the native frame of an unseen CTA through projection-space calibration and transform composition. A population-trained residual network refines the pose, followed optionally by low-budget image-driven optimization. GeoPose requires neither patient-specific adaptation nor explicit inter-volume preregistration. On 80 DSA observations from 20 held-out patients, optimization-free GeoPose achieved a carotid mean projected centerline distance (mPCD) of 5.8 mm and a clDice of 0.45, compared with 14.5 mm and 0.28 for the best-performing baseline, while requiring only 0.15 s. After 25 optimization iterations, GeoPose reached an mPCD of 4.6 mm and a clDice of 0.58 in approximately two seconds. Under the same budget, native-initialized optimization achieved 14.6 mm and 0.15, respectively. GeoPose thus provides rapid native-frame registration with fixed population-level weights and the geometric correspondence required for downstream biplanar 3D vascular reconstruction.

---


### 391. [Variational Outlier-Robust Gaussian Process Regression with Generative Modeling](https://arxiv.org/abs/2608.16606)

**<font color=#1a73e8>作者：</font>** Arslan Majal, Aamir Hussain Chughtai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Outliers can substantially distort Gaussian process regression (GPR) due to its conventional Gaussian observation likelihood, leading to inaccurate model learning and prediction. To address this limitation, this article introduces a generative GPR model that captures observation-specific contamination and adaptively mitigates the influence of outliers. Subsequently, a variational generalized expectation-maximization procedure is used to learn the latent variables and GPR model parameters. Experiments on synthetic and real datasets under different contamination settings demonstrate that the proposed method remains competitive with-and in several cases outperforms-robust GPR baselines in prediction accuracy. Moreover, the proposed method shares the cubic computational scaling of the compared GPR methods.

---


### 392. [Interactive Whole Slide Images for RL-based Tumour Segmentation](https://arxiv.org/abs/2608.16607)

**<font color=#1a73e8>作者：</font>** Mohamad Mohamad, Francesco Ponzio, Maxime Gassier 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole-slide image (WSI) analysis remains computationally challenging due to the extremely large spatial resolution of slides and the sparse distribution of tumour regions. We propose an end-to-end reinforcement learning framework for sequential tumour segmentation directly on WSIs. Instead of treating the slide as a predefined collection of candidate patches, we formulate the WSI itself as a hierarchical multi-resolution environment through which an agent navigates using movement, zooming, and tumour selection actions. The agent jointly processes local observations and a global thumbnail representation within an actor-critic architecture trained using proximal policy optimization (PPO). Experiments on pulmonary adenocarcinoma WSIs demonstrate the feasibility of direct sequential tumour segmentation on full slides, achieving comparable coarse segmentation quality relative to patch-based approaches operating at similar magnification levels, while reducing inference time to a few seconds per slide. We further analyse the impact of environment design and action-space granularity. Our results suggest that modelling WSIs as interactive environments provides a promising direction for RL-based computational pathology

---


### 393. [Cost Scales with Change, Not Corpus Size: Incrementally Maintaining an Evolving Semantic Substrate](https://arxiv.org/abs/2608.16621)

**<font color=#1a73e8>作者：</font>** Yusuke Takahashi, Kyle Wild, Asako Uraki  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented and agentic question-answering systems increasingly re-derive the meaning of a corpus at query time. Put plainly, instead of re-deriving what a corpus means on every question, the work is done once when a document arrives and is thereafter merely consulted -- a compiler, not an interpreter, of meaning. An alternative is to compile that meaning once, at ingest time, into a compact, queryable semantic substrate and maintain it as the corpus evolves. The central objection is maintenance cost: rebuilding a truncated singular value decomposition (SVD) on every change appears prohibitive, and a change of embedding model seems to force a full re-embedding. We argue and show empirically that maintenance cost scales with the amount of change, not corpus size. On a controlled synthetic pilot (dimension 256, rank 32, a corpus grown from 3,000 to 9,000 documents over 50 update events), incremental low-rank updates were 33.7 times cheaper per update than full re-SVD and 23.8 times cheaper cumulatively, while the incremental subspace tracked the full recomputation to within floating-point precision (maximum principal-angle drift below 1e-11 degrees; recall@10 = 1.0). An orthogonal Procrustes virtual axis update recovered 0.95 mean cosine to truly re-embedded vectors by re-embedding only about 10 percent of the corpus. The results support maintaining, rather than repeatedly reconstructing, a semantic substrate.

---


### 394. [A Shop Floor Production Scheduling Case based on RFID-supported Smart Factory](https://arxiv.org/abs/2608.16626)

**<font color=#1a73e8>作者：</font>** Zhihui Chen, Yize Sun, Yuhao Dong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Radio frequency identification (RFID) technology has been widely implemented for real-time data collection in manufacturing shop floors, which, in turn, can be used to support dynamic shop floor production planning and scheduling. Within such an environment, uncertainty in operation and production processes collectively contribute to the dynamicity in manufacturing, thereby hampering the scheduling system from achieving maximal utility. To highlight the importance of handling such uncertainty, this paper addresses the problem of dynamic shop floor scheduling for a real-life case smart factory equipped with RFID technology. Feasible production sequence mining and real-time processing rate estimation are conducted on RFID-collected production data to quantify the operation and production uncertainties. A deep reinforcement learning approach based on the RFID data analysis is then presented for shop floor production scheduling. Simulation studies based on real-life case data have demonstrated the feasibility and practicality of the proposed dynamic production scheduling framework. Specifically, it is observed that the proposed framework outperforms existing dispatch methods in terms of minimizing operation makespan, including first in first out (FIFO), last in first out (LIFO) and deep Q network (DQN).

---


### 395. [DRAFE: Domain-Robust Asymmetric Fusion of Heterogeneous Detection Transformers for Cross-City Fine-Grained Traffic Object Detection](https://arxiv.org/abs/2608.16632)

**<font color=#1a73e8>作者：</font>** Divine Yao Agbobli, Geoffery Eyram Agorku, Israel Afriyie 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning-based object detectors are fundamental to intelligent transportation systems, enabling traffic monitoring, vehicle analytics, and infrastructure management. However, achieving both fine-grained vehicle recognition and robust cross-city domain generalization remains challenging. We present the Domain-Robust Asymmetric Fusion Ensemble (DRAFE), which combines independently trained LW-DETR and RF-DETR detectors for cross-city fine-grained traffic object detection. DRAFE employs a two-stage training strategy that first pretrains complementary detectors on diverse public traffic datasets using pseudo-label expansion and human-in-the-loop annotation refinement, producing a curated corpus of 6,049 images and 203,619 annotations, before challenge-compliant fine-tuning on the Project Hafnia Track 6 dataset. At inference, DRAFE applies anchor-conditioned class-consistent matching, reliability-weighted coordinate fusion, agreement-aware confidence recalibration, and complementary hypothesis recovery. On AI City Challenge 2026 Track 6, DRAFE achieves 0.4022 mAP, ranks sixth among 25 participating teams, and improves by 0.0553 mAP over a preliminary ensemble evaluated under identical benchmark conditions.

---


### 396. [Love in the Age of AI: An Integrative Process Model of Romantic Human-Chatbot Relationships](https://arxiv.org/abs/2608.16633)

**<font color=#1a73e8>作者：</font>** Natalia Szymczyk, Paula Ebner, Jessica M. Szczuka  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The increasing ability of social chatbots to form deep and even romantic Human-Chatbot Re lationships (HCRs) has drawn growing academic attention. Yet, existing research remains fragmented, often examining individual stages such as initiation or dissolution in isolation, without tracing the full relational trajectory. Such fragmentation, however, hinders a holistic understanding of the interplay between the unique psychological and social drivers, relational dynamics, and profound emotional stakes, particularly obscuring the elements unique to ro mantic bonding. This paper addresses this gap by introducing the first empirically grounded integrative process model of the romantic HCR lifecycle. A qualitative secondary analysis of 73 user experiences, drawn from two datasets of qualitative interviews and surveys, provides the basis for a three-phase model that synthesizes established theoretical frameworks related to user needs and gratifications, HCR development, and relationship dissolution. The model demonstrates that the Initiation phase is driven by specific psychological and social determi nants that shape the needs and gratifications sought by the user. The Relationship Building phase progresses through explorative, affective and stable stages, in which users develop gen uine romantic feelings and a deeply integrated bond with the chatbot. Finally, the Ending phase reveals that when dissolution occurs, it elicits emotional and physical responses com parable to human breakups but generates unique, technology-mediated coping mechanisms, potentially leading to a recursive cycle of re-engagement.

---


### 397. [Training-Free Reconstruction-Based AI-Generated Image Detectors Are Inherently Vulnerable to Adversarial Examples](https://arxiv.org/abs/2608.16646)

**<font color=#1a73e8>作者：</font>** Roman Demchenko, Jonas Ricker, Asja Fischer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The impressive visual quality and ubiquity of AI-generated images call for reliable and robust detection methods. Reconstruction-based detectors have emerged as a promising direction for transparent and training-free identification of synthetic images. However, due to their fundamentally different mode of operation (compared to standard, classifier-based methods), little is known about their adversarial robustness. In this work, we propose two novel attack methods targeted at detectors that leverage autoencoder reconstruction error. We find that by constructing imperceptible adversarial examples, the distance between original and reconstruction can be artificially increased, causing fake images to be wrongly classified as real. Our evaluation including images from three state-of-the-art generators and three detectors demonstrates that detection performance is significantly decreased, even if attacked images additionally undergo real-world degradations. Critically, our adversarial examples naturally transfer across detectors, as they all share the same principle, pointing towards an inherent vulnerability of reconstruction-based detectors.

---


### 398. [X$^2$Localizer: Cross-grained Alignment for Progressive Cross-view Video Geo-localization](https://arxiv.org/abs/2608.16658)

**<font color=#1a73e8>作者：</font>** Zichao Zeng, Weijia Fan, Yufan Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-view Video Geo-localization (CVG) aims to localize ground-view videos by retrieving their corresponding geo-tagged aerial images. However, CVG approaches rely on fixed-length inputs and post-hoc refinement, hindering online-oriented localization under partial or dynamic observations. In this work, we formulate Progressive Cross-view Video Geo-localization (PCVG) as a deployment-oriented extension and evaluation protocol of CVG, enabling localization under varying temporal budgets, prefix-based inference, random-start evaluation, and long-range localization with interruptions. To explore PCVG, we introduce X$^2$Localizer, a cross-grained alignment framework that jointly supervises global prefix-to-aerial retrieval and token-aggregated frame--aerial-tile matching with a budget-dependent asymmetric objective. Furthermore, we introduce a Sliding-Window Re-Localization (SWRL) strategy that dynamically refreshes candidate regions for failure recovery and long-range deployment without full-sequence reprocessing. Extensive experiments show that X$^2$Localizer preserves conventional full-video performance, with marginal gains of +0.1 Recall@1 and +0.3 Recall@10, while substantially improving early localization. In the challenging single-frame setting, X$^2$Localizer improves coarse retrieval by +4.7 Recall@1 and +11.5 Recall@10 over the previous state-of-the-art method. With SWRL, our approach further enables robust progressive localization under random-start and long-distance scenarios, narrowing the gap between benchmark evaluation and real-world deployment.

---


### 399. [Hoeffding adaptive splitting trees for data stream classification with concept drift and ensemble learning](https://arxiv.org/abs/2608.16659)

**<font color=#1a73e8>作者：</font>** Daniel Nowak Assis, Jean Paul Barddal, Fabrício Enembreck  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ensembles of decision trees are well-established methods for data stream classification. In ensemble learning, Hoeffding Trees are widely adopted as base learners, performing periodic split attempts according to the Hoeffding bound. Recent studies, however, indicate that this standard splitting mechanism lacks adaptability, while adaptive trees that trigger splits in response to performance degradation have achieved superior results. In this paper, we identify limitations in the use of adaptive-splitting decision trees as ensemble base learners, showing that change detectors often fail to promote sufficient diversity within ensembles. To address this issue, we propose two novel decision tree models, termed Hoeffding Adaptive Splitting Trees. These models combine the periodic splitting strategy of Hoeffding Trees, which fosters ensemble diversity, with adaptive splitting mechanisms that employ change detection algorithms to identify performance decay and determine split points. Experimental results demonstrate that Hoeffding Adaptive Splitting Trees enhance ensemble performance and achieve state-of-the-art results across a comprehensive evaluation, including benchmark comparisons, computational cost analysis, and concept drift adaptation.

---


### 400. [Turning spectra into images improves plant trait retrieval with 2D-CNNs](https://arxiv.org/abs/2608.16661)

**<font color=#1a73e8>作者：</font>** Javier Lopatin, Teja Kattenborn, Eya Cherif 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral reflectance spectroscopy enables non-destructive estimation of plant functional traits, yet current deep learning approaches process spectra as one-dimensional sequences, which limits how they capture long-range inter-band dependencies. We asked whether transforming 1D spectra into 2D image representations improves multi-trait prediction with convolutional neural networks (CNN). We compared nine transformations using EfficientNet-B0 on the GreenHyperSpectra dataset (7,897 labeled spectra, eight traits, 400-2450 nm), benchmarked against published 1D CNN results on the same split. Trained from scratch, the simplest transformation, a direct Reshape of the spectrum into a 2D grid, performed best ($R^2 = 0.684 \pm 0.001$) and improved on the state-of-the-art 1D baseline ($R^2 = 0.587$, $+0.097$). We then pretrained a 2D masked autoencoder (MAE-2D) on 139,000 unlabeled spectral images. Linear probing, which freezes the encoder and trains only a multilayer perceptron head, reached $R^2 = 0.646$ and exceeded every 1D self-supervised counterpart, including the fine-tuned MAE-1D ($R^2 = 0.641$). Under cross-dataset evaluation all models lost most of their accuracy and none beat the 1D baseline significantly. To identify which wavelengths drive each prediction, we applied Integrated Gradients and Grad-CAM and unfolded band importance back to the spectral axis. Protein ($r = 0.45$) and leaf water ($r = 0.33$) agreed with sensitivities simulated by the PROSAIL radiative-transfer model, while carotenoids ($r = 0.06$) and leaf area index ($r = -0.11$) did not, showing that the model reads established leaf chemistry for traits with sharp absorption features. The representational advantage of 2D spectral images, rather than architectural complexity or ImageNet pretraining, drives the gain over 1D approaches.

---


> [!TIP]
> 当前位于：**351-400**（第 8/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-435](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
