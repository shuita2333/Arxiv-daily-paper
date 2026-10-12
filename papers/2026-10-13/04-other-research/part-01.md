# 📦 其他研究 | 2026年10月13日

> 本类共 **244** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-244](./part-05.md)

---

### 1. [Faithfulness Without Anchors: A Position Paper on the Structural Misalignments of Explainable AI Faithfulness Metrics for Feature Importance](https://arxiv.org/abs/2610.12493)

**<font color=#1a73e8>作者：</font>** Marco Zullich, Emily Schiller, Ivan Gentile 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Explainable Artificial Intelligence (XAI) tools have often been presented as methods to increase trust in machine learning models by making aspects of their algorithms more human-understandable. However, evidence accumulated over the last decade points to an overall failure of this objective, instead promoting overreliance on incorrect predictions, which can subsequently lead to algorithmic aversion. Rather, XAI appears to function primarily as a debugging tool, useful for obtaining anecdotal insights into, for example, features learned by the model. One of the main issues underlying this limitation is that XAI methods often oversimplify the inner workings of the model, resulting in misalignment between the explanation and the model itself - a behavior referred to as unfaithfulness or infidelity. Faithfulness can be interpreted as the degree of approximation between an explanation and the model. Computing faithfulness in a rigorous manner would thus make it possible to quantify one of the various elements of trustworthiness of an explanation. However, existing metrics present significant limitations, making this quantification either infeasible or computationally expensive. In this position paper, we outline five major shortcomings of current faithfulness metrics and propose four possible avenues for research to bolster their reliability.

---


### 2. [An Input-Dependent Readout Phase for Resonant Sequence Models](https://arxiv.org/abs/2610.12496)

**<font color=#1a73e8>作者：</font>** Shivesh Rane  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sequence models with a fixed-size state avoid the quadratic cost of attention, but face a design choice. An input-dependent state transition gives content-dependent memory at the cost of FFT-based training, while a fixed transition keeps the O(T log T) convolutional path but reads memory the same way for every input. ResonatorLM, a recent model of the second kind, reads a bank of damped complex oscillators through a fixed learned phase per head. We make that readout phase a function of the current token, which adds input dependence to the read only, keeps the convolution exact, and costs 0.2 percent more parameters. An analysis of the untrained bank shows that phase does encode elapsed time, but an ordinary token falls below the background within 2-8 steps and no choice of damping extends linear reconstruction beyond about 16 tokens. In 6M-parameter character-level models on WikiText-2, the input-dependent phase matches the original at the training length and removes its failure beyond it: trained on 256 tokens and tested on 1024, perplexity falls from 12.81 to 3.76. We trace the failure to long-memory heads that accumulate more history than training exposed them to. The learned phase tracks the current character rather than distance and does not improve retrieval.

---


### 3. [CircuitTree: Composing Circuits into A Syllable Transcriber](https://arxiv.org/abs/2610.12520)

**<font color=#1a73e8>作者：</font>** Jiankun Wei, Ewan Dunbar, Gerald Penn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The goal of circuit discovery is to decompose a monolithic neural network into tiny modular subnetworks which are interpretable in the sense that each does an identifiable subtask. We develop a practical method for composing arbitrarily many circuits into a single model. We propose a greedy, density-scaled composition algorithm that overcomes limitations of previous attempts to compose circuits by naive union, then generalize it to $N$ circuits via CircuitTree, a new data structure built on a $\Theta(N\log N)$ tree-compose schedule. We compose circuits pruned from HuBERT for classifying individual phonemes into a syllable classifier, a capability none of the 39 phoneme circuits has individually. Chaining CircuitTrees into a hierarchy-of-circuits pipeline, we transcribe open syllables at 64.8\% accuracy, within 1.2 points of a 66.0\% ceiling that shares no circuitry at all, with 99.5\% of circuit components shared.

---


### 4. [Behind-the-Meter Photovoltaic Visibility from Net Smart Meters: Deployment Regimes and Operational Insights](https://arxiv.org/abs/2610.12527)

**<font color=#1a73e8>作者：</font>** Jack Zheng, Hao Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distribution operators need visibility of behind-the-meter photovoltaic (PV) generation, yet most residential customers are observed only through net smart meters. Deep-learning-based PV disaggregation can restore this visibility, but its operational value depends on whether the model serves known customers, new customers, future periods, or new regions. We quantify this dependence using four deployment regimes that separate household transfer from temporal extrapolation, applied to Ausgrid smart-meter data with cross-dataset adaptation to the Pecan Street data. Using a fixed training protocol, we benchmark representative deep sequence architectures for PV disaggregation under regime-matched evaluation. At a fixed 48-hour context length, daylight mean absolute error (MAE) of the best model rises from 0.104~kW on seen households in the future test period to 0.185~kW on unseen households over the same period, and under a fixed training contract the deployment regime explains far more of the error variation than model choice. Under target-domain normalization, fine-tuning on five target-region households reduces source-model transfer error by 28\%--36\%. Long input windows help known-customer extrapolation, while their new-customer benefits vary by model. These findings suggest regime-matched error budgets, limited target supervision for model adaptation in new regions, and use-case-dependent context selection for energy data analytics.

---


### 5. [GlucoPRISM: Protocol-Supervised Pretraining for Cross-Cohort Glucose Transfer](https://arxiv.org/abs/2610.12528)

**<font color=#1a73e8>作者：</font>** Adinath Madhavrao Dukre, Abdullah Mohammad, Yifan Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous glucose monitoring (CGM) foundation models encode each day as one vector that mixes who the person is, what happened that day and how the sensor measured it, so measurement differences travel with the representation into new cohorts. We ask whether pretraining can place the measurement component that harms transfer in known coordinates, so that deployment drops them with a fixed projection and no target data. GlucoPRISM supervises a GlucoFM backbone with response contracts, rules for how each part of the representation should change when only the day or only the sensor changes: a 64-dimensional Trait band should change with neither, a 48-dimensional State band only across days, and a 16-dimensional Sensor band should track the device. Synthetic sensor views calibrated on paired Dexcom and Libre recordings, different-day pairs and glucose-summary targets supply this supervision without clinical labels. Across twelve cross-cohort directions, dropping the Sensor band from the same frozen encoder raises mean transfer AUROC from 68.75 to 73.57, against 69.3 for GlucoFM. The gain has two parts. Into CGMacros, the one target cohort recorded with two sensor types, filtering adds 11 to 19 points, and this holds when the generator is recalibrated on half of the participants and scored on the other half. On the other eight directions filtering is neutral and the encoder itself exceeds GlucoFM by 3.5 points. The device remains linearly decodable after filtering, so the filter removes a device-related component that harms transfer rather than all measurement information. The retained bands improve window AUROC on thirteen of fourteen public task--cohort cells (Holm-adjusted p=0.031) and correlation on fourteen of fifteen clinical endpoints in an external cohort of 9,303 participants.

---


### 6. [CacheScope: Exact-Compute Allocation for Training-Free Diffusion Acceleration](https://arxiv.org/abs/2610.12530)

**<font color=#1a73e8>作者：</font>** Qinhan Lyu, Jusheng Zhang, Zhixing Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training-free feature reuse accelerates diffusion transformer inference by replacing full denoising computation at selected steps with cached approximations. Existing methods mainly improve the reconstruction of skipped features, but we find that once a stable first-order reconstructor is used, increasing reconstruction complexity brings limited gains, whereas the placement of exact-computation steps has a much larger effect on fidelity. More importantly, absolute shallow-probe variation is jointly affected by input-trajectory displacement and network response strength, and therefore does not directly reflect cache risk. We address this confounding by normalizing probe-output variation with the corresponding input displacement, yielding a directional gain per unit trajectory movement. Based on this signal, we propose CacheScope, which identifies high-risk reuse steps online and selectively falls back to full denoising computation while leaving the underlying cache reconstructor unchanged. CacheScope requires no additional training, gradients, auxiliary networks, or prompt-specific offline schedule optimization. Across FLUX.1-dev, Wan2.1-T2V-1.3B, and Open-Sora 1.2, CacheScope achieves up to 3.57x acceleration and reduces median LPIPS by up to 70.1% over the strongest probe-based baseline.

---


### 7. [SoK: Privacy-Preserving Order Matching](https://arxiv.org/abs/2610.12535)

**<font color=#1a73e8>作者：</font>** Prerna Arote, Adrian Saiz, Lucianna Kiffer  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Privacy-preserving order matching enables traders to discover and execute compatible orders while limiting disclosure of sensitive trading information. Existing systems span financial markets and blockchain-based asset exchanges and employ diverse market structures, privacy mechanisms, and trust assumptions, making their privacy guarantees difficult to compare. We present a systematization of privacy-preserving order matching covering 22 protocol families. We organize the order lifecycle into four phases: order representation and submission, order discovery and collection, order-matching, and settlement, and characterize each phase by protected and exposed information, access roles, privacy mechanisms, and trust assumptions. Our analysis shows that privacy is not a single protocol-level property: protecting selected order attributes or individual phases does not necessarily prevent leakage elsewhere in the lifecycle. We identify recurring trade-offs among privacy, functionality, trust, and verifiability, highlighting the challenge of achieving end-to-end privacy across the complete order lifecycle.

---


### 8. [Efficient Learning of Survival Analysis Models Under Outcome-Dependent Truncation and Censoring](https://arxiv.org/abs/2610.12538)

**<font color=#1a73e8>作者：</font>** Itai Zilberstein, Ioannis Anagnostides, Arman Kilic 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern machine learning models are typically trained on data assumed to be representative of the predictive tasks the model will face in the future, but practical datasets violate this assumption. We focus on outcome-dependent truncation in which an observation appears in the training data depending on its label. Our work connects two largely distinct literatures: efficient learning under truncation and survival analysis. Existing methods for truncated survival analysis do not characterize the optimization landscape and instead rely on iterative procedures such as expectation maximization. We address this gap and prove that Cox regression can be efficiently learned under truncated and right-censored data using first-order optimization when the baseline hazard is known (despite nonconvexity). In contrast, when the baseline hazard is learned jointly, we construct identifiable and correctly specified models whose negative log-likelihood contains strict suboptimal local minima. On experiments with four survival datasets, we show that accounting for truncation reduces the prediction bias induced by naive Cox regression and extends to neural networks. We also show orders of magnitude speedups compared to standard expectation maximization.

---


### 9. [Organizational Context for the Enterprise Security Brain](https://arxiv.org/abs/2610.12540)

**<font color=#1a73e8>作者：</font>** Eden Yavin, Ariel Zadok, Gal Engelberg 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agents that investigate and decide on enterprise security reason over a machine-readable view of the environment: its assets, identities, configurations, relations, and findings. The correct judgment about an asset also depends on what the organization knows about it: who owns it, what business function it serves, which policy governs it, and which risks were accepted. Part of this knowledge can be inferred from machine state, such as an ownership tag; most of it is recorded by people in policies, audit reports, architecture diagrams, tickets, and conversations, outside machine state. We call this distance the organizational context gap. Closing it poses four challenges: extracting the right claims from heterogeneous organizational data and, at inference time, detecting claims made stale by live state, checking live state against the governing policy, and binding architecture diagrams, which carry the business logic, to live resources. We introduce organizational context as a layer of the enterprise security brain and define it with a taxonomy and six properties its representation must preserve. We then define a context model in which a claim carries one meaning, an attestation records each source that asserts it, strength is derived from live evidence at read time, and claims resolve onto the entities of the asset graph. On a production environment spanning AWS, Okta, Google Workspace, and GitHub, extraction recovers 0.80 of a pooled 1,355-claim ground truth at 0.87 precision, with 0.5% of extracted claims unsupported by their source. An agent reasoning over live state and resolved context raises the conflict in 0.97 of stale-finding tasks, and reaches answer correctness of 0.83 on policy-alignment tasks and 0.86 on architecture tasks.

---


### 10. [Enriched Holomorphic Neural Networks for 2D and 3D Laplace Problems](https://arxiv.org/abs/2610.12541)

**<font color=#1a73e8>作者：</font>** Kalp Shah, Andrei Vlad Nicula, Mihnea Andrei Bârsan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Boundary-value problems for the Laplace equation develop singular behaviour near corners, edges and junctions that smooth approximators resolve poorly. We combine holomorphic neural networks with singular functions derived from the local geometry and boundary conditions. The representation is harmonic by construction, so no interior residual is needed: the network fits the smooth remainder from boundary data alone, and the enrichment terms capture the singular behaviour. Singular exponents are trainable, so the construction also applies when the local expansion is not known in advance. We extend the approach to three dimensions using independent networks evaluated along complex null directions. The enriched model is the most accurate tested method on every problem. Its margin is several orders of magnitude where the enrichment captures the singularity exactly, and a factor of about 1.7-2.1 over the next-best method on a CdZnTe radiation detector with many singular sites, in both two and three dimensions.

---


### 11. [Equal-Budget Monte Carlo Tree Search versus Randomized-Restart List Scheduling for DAG Workflows: A Controlled Equal-Budget Computational Study](https://arxiv.org/abs/2610.12542)

**<font color=#1a73e8>作者：</font>** Yuyu Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Monte Carlo Tree Search (MCTS) is often proposed for scheduling directed-acyclic-graph (DAG) workflows, yet most studies never run the comparison that could refute it - giving a much simpler method the same search effort. We run that comparison under a controlled protocol. All arms receive an identical budget - the same number of candidate schedules built and evaluated: an MCTS scheduling method, preregistered as the main arm; a randomized-restart list scheduler with no search tree as the control; and a textbook-UCT MCTS arm as a registered follow-up on the same domain. The analysis plan was locked before data collection; an independent checker confirmed all 768 confirmation-stage schedules valid with correct finish times. At the main budget of 2048 evaluated schedules, MCTS is 2.88% worse than the restarts (95% CI [-3.62%,-2.15%]; the 72 of 96 held-out instances with positive baseline-relative headroom). The deficit is not budget starvation: on the separate exploration pool restarts self-improve by 1.85% where MCTS gains 0.24%, and 700 of 720 of MCTS's first results are merely the warm start it was handed. The studied selection rule locks deterministically onto the first-expanded child, keeping its trials correlated while restarts draw gains from the tails; the causal link to makespan remains an inference. A structural map locates where the tree stops paying: restarts win on sparse irregular workflows, no difference is detectable on regular layered ones, and dense ones leave no room to improve. Swapping the rule for textbook UCT removes most of the deficit (-0.26%, 95% CI [-0.71%,+0.23%]) without reversing its sign. Results are confined to a controlled synthetic domain (N in {8,16,32} tasks, 2-8 processors, budgets up to 2048); we make no claim about larger budgets.

---


### 12. [Transformer-Based Masked Diffusion Models Provably Learn Distributions with Latent Structure](https://arxiv.org/abs/2610.12544)

**<font color=#1a73e8>作者：</font>** Jingda Wu, Changxiao Cai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked diffusion models (MDMs) generate discrete data by iteratively unmasking multiple tokens in parallel using a learned mask predictor. Their output carries two errors: parallelization error due to parallel sampling, and estimation error from the mask predictor learned with finite samples. Existing theory treats these errors separately, and the available statistical bounds typically scale with the number $V^L$ of length-$L$ sequences over a vocabulary of size $V$, suffering from the curse of dimensionality. In this work, we establish end-to-end statistical guarantees showing that transformer-based MDMs learn structured distributions with a sample complexity governed by their latent structure. Specifically, we model this structure through mixtures of hidden Markov trees, which capture latent dependencies within components and heterogeneity across components. When the data distribution is well approximated by such a mixture, a transformer-based MDM with parallel unmasking schedules achieves $\varepsilon$-accurate sampling in KL divergence with $\widetilde{O}(LK_{\mathrm{par}}/\varepsilon)$ training samples, where $K_{\mathrm{par}}$ is polynomial in $L$, $V$, the number of hidden states, and the number of mixture components. The transformer network and sampling procedure require no knowledge of the tree topologies or component parameters, thereby adapting to the unknown latent structure automatically. Overall, our results provide theoretical justification for the empirical effectiveness of MDMs on real-world data.

---


### 13. [MIRAGE: Metric Inference and Reliability-Aware Gaussian Estimation from Feed-Forward Vision](https://arxiv.org/abs/2610.12568)

**<font color=#1a73e8>作者：</font>** Xinzhe Wang, Changjian Jiang, Kaiwen Song 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D priors enable high-quality reconstruction from image streams but often lack reliable metric scale and suffer from long-term trajectory drift. In contrast, LiDAR--inertial estimation provides metrically accurate motion but lacks the image-space consistency needed for high-fidelity reconstruction. We propose $MIRAGE$, which anchors feed-forward visual geometry to LiDAR--IMU metric motion and regulates online pose corrections according to correspondence support and cross-modal agreement, jointly enabling accurate metric pose estimation and high-fidelity Gaussian reconstruction. Experiments on Oxford Spires, M2DGR and INS show that MIRAGE achieves accurate metric trajectory estimation, outperforming COLMAP, a widely used but computationally expensive reference for vision-only benchmarks. Motivated by the scarcity of long-horizon monocular benchmarks for large-scale indoor reconstruction, we further build a multimodal data-collection platform and use MIRAGE to establish accurate 6-DoF reference trajectories for a new vision-only benchmark. We benchmark recent monocular large-scale reconstruction methods on this dataset, providing a systematic evaluation of their performance in long-horizon indoor scenes.

---


### 14. [CLUE: A Contrastive Learning Framework for Unsupervised Event Type Induction and Annotation](https://arxiv.org/abs/2610.12580)

**<font color=#1a73e8>作者：</font>** Pratik Maitra, Lauren Kwon, Qi Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Event ontology is the foundational framework for defining events in a dataset. Event type induction generally involves domain experts who define guidelines for creating event types and their names based on the dataset's domain and scope. However, this process is resource-intensive in terms of annotation costs and is prone to human biases. To alleviate the need for manual event ontology creation, we propose the CLUE framework for event type induction, naming, and annotation. Our main contributions in this work are: 1) designing a novel joint embedding representation for expressing both the verb-centric view and the semantic view of events; 2) event type induction using contrastive loss guided clustering; 3) event naming and refinement. Experiments demonstrate the effectiveness of our method. Our code is available at this https URL.

---


### 15. [Realism VS Accuracy: Event Sequence Forecasting from a Generative Modeling Perspective](https://arxiv.org/abs/2610.12586)

**<font color=#1a73e8>作者：</font>** Dmitry Osin, Egor Surkov, Petr Mokrov 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Event sequences are chains of random events, each described by heterogeneous (numerical and categorical) features. The problem of event sequence forecasting occurs in finance, healthcare, business process intelligence, and other fields. In this work, we study multi-horizon forecasting of event sequences as a conditional generative modeling problem. We evaluate forecasts not only for prediction accuracy, but also for distributional realism. To this end, we present a benchmark comprising metrics for both quality aspects, strong statistical baselines, recent models adapted from adjacent fields, and curated real-world datasets. Careful evaluation reveals that no method excels at both accuracy and realism, highlighting a fundamental trade-off between the two. Finally, we introduce Wasserstein BaryBooster, an algorithm that aggregates samples from a realism-strong diffusion model into a state-of-the-art predictor, demonstrating that distributional realism can be converted into prediction accuracy. Code is available at this https URL.

---


### 16. [HOMARD: Hammering Off-chip Memory via Aggregate power Rail Disclosure](https://arxiv.org/abs/2610.12621)

**<font color=#1a73e8>作者：</font>** Eliott Quéré, Li-Chung Chiang, Carina Fiedler 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Software-based microarchitectural attacks have mainly exploited timing differences to infer information from DRAM. However, defenses and optimizations can prevent timing-based approaches from resolving precise microarchitectural behaviors. We show that unprivileged millisecond- and milliampere-resolution power sensors on modern Arm SoCs can recover DRAM mapping functions and reveal the data dependence of memory accesses without timers. We present HOMARD, a methodology that reads DRAM activity from this telemetry, and two attack primitives. HOMARD-RE is a hierarchy-aware linear-algebraic method that reverse-engineers DRAM addressing functions from power alone. HOMARD-DATA recovers the Hamming weight of a fetched cache line through joint-power rail templating and secret byte values through correlation power analysis on the same rails. Across an AMD ZCU102, a Raspberry Pi 5, and a multi-chip-based LPDDR4 NVIDIA Jetson TX2, HOMARD-RE succeeds where row-buffer timing methods fail. On the Pi 5, HOMARD-DATA classifies 9 Hamming-weight levels at 81.5% accuracy and recovers secret bytes in minutes by correlating rail current with data-dependent bit toggling between neighbors in a row. Both primitives work with an architectural load or a mispredicted Spectre-RSB path on which no value is architecturally read. These results establish unprivileged power telemetry as an independent side channel for profiled microarchitectural attacks, particularly when timing falls silent.

---


### 17. [MemReg: Streaming Outdoor LiDAR Point Cloud Registration with Hybrid Memory Buffers](https://arxiv.org/abs/2610.12624)

**<font color=#1a73e8>作者：</font>** Jiuming Liu, Mengmeng Liu, Guangming Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prior outdoor LiDAR registration works are commonly limited by the pair-wise input paradigm, which neglects temporal correlations inherent within streaming sequences. In this paper, we propose a novel multi-frame outdoor point cloud registration network for streaming LiDAR scans enhanced with pose-related memory buffers. The key observation is that long-term temporal LiDAR sequences can provide rich global contextual information to complete sparse measurements, filter outliers, and address low-overlap problems, thereby boosting registration performance. Specifically, two hybrid memory buffers are designed, including an implicit memory feature buffer and an explicit memory pose buffer, to store and dynamically update pose-related temporal features. Moreover, a novel dynamic history weighting module is developed to adaptively fuse current and history pose-related features. Extensive experiments on three outdoor datasets, including KITTI, nuScenes, and Apollo-Southbay, demonstrate state-of-the-art performance of MemReg, surpassing all previous pair-wise methods and also multi-frame SLAM systems. Our method also generalizes surprisingly well to multiview indoor registration scenarios with rather competitive performance on 3DMatch, 3DLoMatch, and ScanNet. Code will be released at this https URL.

---


### 18. [ForcingBooster: Adaptive Patch-wise Denoising for Fast Autoregressive Video Diffusion](https://arxiv.org/abs/2610.12625)

**<font color=#1a73e8>作者：</font>** Zekai Gu, Peng Wang, Jiahao Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video diffusion models have become a leading approach to real-time interactive video generation and video world modeling. However, existing methods typically allocate computation uniformly across space when generating the next video chunk, updating all patches with the same denoising schedule and number of function evaluations. This ignores the spatial heterogeneity of video content: static, simple, or recurring regions are often easier to denoise, while other regions require further refinement or additional context. A uniform budget thus leads to redundant computation on easy patches, whereas reducing the fixed step count can leave difficult patches insufficiently refined. We introduce \methodname{}, a general framework that dynamically allocates denoising steps to individual patches: easy patches stop early to improve efficiency, while difficult patches receive more refinement steps. This design accelerates generation with negligible quality degradation. Our method is compatible with most existing few-step autoregressive diffusion models, requiring only a lightweight routing module with modest training. Experiments demonstrate that \methodname{} reduces the total number of denoising steps applied across video patches by about 50\% while maintaining visual quality comparable to the four-step baseline.

---


### 19. [Data-driven Optimal Sensor Placement for Aerosol Monitoring in the UK](https://arxiv.org/abs/2610.12658)

**<font color=#1a73e8>作者：</font>** Talha Ansar, Waqar Muhammad Ashraf, Alejandro Coca-Castro 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop a data-driven sensor-placement framework and apply it to aerosol monitoring in the United Kingdom (UK). A trained convolutional Gaussian neural process is embedded within the DeepSensor optimisation framework. Genetic optimisation with lazy evaluation and caching reduces mean computational time by 60\% (10$\pm$3 versus 25$\pm$7 minutes) while producing sequential placement performance comparable to the greedy solver. Using the CAMS reference field to construct a retrospective oracle benchmark, Joint NLL improves by about 22\% for Joint-MI-driven genetic placement after five locations for aerosol stations are identified. Seasonal and wind-regime analyses show that agreement between model-based criteria and oracle benchmarks varies with meteorological transport conditions. These results show a computationally efficient approach for data-informed expansion of environmental observing systems.

---


### 20. [WoodBR-Cross: A public wood-image dataset and individual-tree-disjoint benchmark for species identification](https://arxiv.org/abs/2610.12676)

**<font color=#1a73e8>作者：</font>** Daniel Casanova, Alexandre Bahia Gontijo, Arnaldo Candido Junior 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wood-image benchmarks can yield optimistic estimates when images from the same tree occur in both training and test sets. WoodBR-Cross contains 4,875 transverse-surface images in 38 operational taxonomic classes, linked to 303 distinct trees identified by numeric catalogue witness codes (codigos-testemunho) in the Brazilian Forest Service collection. A species-level subset comprises 3,406 images, 20 classes and 214 trees. Three tasks compare duplicate-aware image partitions for all classes (A), image partitions for the species subset (B1), and individual-tree-disjoint partitions for that subset (B2). In B2, all images from each tree are kept together, so no tree is shared across training, validation or test within a fold. ResNet-50, ConvNeXt-Tiny and ViT-B/16 were evaluated with three outer folds, internal validation and five training seeds. Handcrafted and frozen-feature baselines complement border-only and randomized-label controls. Validation-selected ConvNeXt-Tiny achieved B2 tree-level macro-F1 of 0.8621 +/- 0.0317; frozen DINOv2 features yielded 0.9000 +/- 0.0722. Values are means and standard deviations across three seed-averaged fold means. Results estimate performance on previously unseen trees from this collection.

---


### 21. [Amortised Inference through One-Step Implicit Sampling](https://arxiv.org/abs/2610.12679)

**<font color=#1a73e8>作者：</font>** Vincent Pauline, Kirill Tamogashev, Arran Carter 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficient sampling from Bayesian posterior distributions in high dimensions remains a hard problem, despite advances in theory and algorithms. Multiple steps are usually required to draw unbiased samples, for example, iterations of an MCMC algorithm or integration steps in a diffusion-based amortised sampler. However, scalable one-step amortised inference remains a challenging open problem. In this work, we build upon recent progress in data-driven generative modelling to offer a possible solution for one-step amortised sampling. Our one-step implicit sampler (OSIS) uses short-time MCMC dynamics to define a local target for the evolution of an implicitly modelled distribution. In the asymptotic limit, the modelled distribution is a fixed point of the MCMC kernel and thus samples from the target. We analyse the convergence properties of OSIS and show connections with other generative modelling and sampling algorithms. We study various design choices and show that OSIS performs well compared to multi-step amortised samplers and non-amortised MCMC baselines while being far more efficient at sampling time.

---


### 22. [Expert-level detection of low-voltage intervals in EEG as a robust biomarker of neonatal encephalopathy](https://arxiv.org/abs/2610.12680)

**<font color=#1a73e8>作者：</font>** John M. O'Toole, Sean R. Mathieson, Aurel Luca 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Background: Discontinuity in neonatal EEG is a critical marker of brain dysfunction but can be difficult to quantify visually. Inter-burst intervals (IBIs) are a key characteristic of discontinuity, yet their definition does not easily translate to AI detection. Objectives: To introduce low-voltage intervals (LVIs), defined exclusively by amplitude and duration, as a context-independent alternative to IBIs, develop an AI detection method for LVIs, and assess their clinical utility as a marker of brain injury. Methods: We developed a ConvNeXt model to detect LVIs and compared its performance with existing methods. We then tested the clinical relevance of detected LVIs across four applications: 1) grading background EEG abnormalities on an open benchmark dataset, 2) classifying clinical hypoxic-ischaemic encephalopathy (HIE) grades and comparing with a normal EEG dataset, 3) seizure prediction, and 4) association with seizure burden. Results: For training and validation, 654 hours of per-channel EEG from 123 neonates were reviewed and 51,162 LVIs were annotated. On held-out validation, ConvNeXt had an AUC of 0.996 and a Matthews correlation coefficient of 0.926. Model-reader agreement exceeded inter-reader agreement ($\Delta \kappa = 0.025$, 95% CI: 0.007 to 0.045, $p<0.001$), attaining expert-level equivalence. On a combined dataset of 444 neonates, percentage LVI showed a strong association with EEG grades (Spearman's $\rho=0.801$), a moderate association with HIE grades ($\rho=0.384$), a weaker association with seizure burden ($\rho=0.244$), and a strong seizure prediction capacity (AUC $=0.872$). Conclusion: AI detection of LVIs achieves expert-level equivalence, whereas quantitative features do not. Automated LVI quantification provides a robust clinical biomarker of neonatal encephalopathy associated with background EEG activity, HIE severity, and seizure risk.

---


### 23. [Critical Mass: Structure-Disjoint Splits Drift With the Libraries They Are Built On](https://arxiv.org/abs/2610.12694)

**<font color=#1a73e8>作者：</font>** Tomo Oga, Devesh Shah, Cailum M. K. Stienstra 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular machine learning evaluates out-of-distribution performance with structure disjoint splits, a construction rule fixed once at the scale its library happened to have: threshold a pairwise distance, then assign whole connected components to folds. For predicting structures from mass spectra, the field has converged on single-linkage clustering under the myopic Maximum Common Edge Subgraph (MCES) distance at a threshold of 10. This convention was set on 29,000 molecules but public libraries now hold 227,690 molecules. MCES is NP-hard per pair over a quadratically growing set, and so the criterion has never been evaluated at that scale. We propose an optimized version of this criterion, allowing for computationally feasible application on the public libraries: Admissible bounds and a union-find skip reduce $2.6 \times 10^{10}$ molecular pairs to only $1.15 \times 10^{7}$ integer programs, a $2{,}259\times$ saving, while provably producing the lossless partition. We find that at this scale the graph percolates. A single component holds $95.5\%$ of the library, capping any test set at $4.5\%$. What remains is not merely smaller, but systematically different: a held-out compound outweighs a training compound 88.1\% of the time, because a fixed absolute budget is a tighter relative tolerance on a larger molecule. Large library benchmarks using this splitting rule naively therefore conflate structural novelty with extrapolation to larger, more complex chemistry.

---


### 24. [Enabling Extended SGX Enclaves inside Confidential Virtual Machines](https://arxiv.org/abs/2610.12695)

**<font color=#1a73e8>作者：</font>** Pamenas Kariuki, Dong Yiliang, Quoc Do Le 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Confidential Virtual Machines (CVMs), such as AMD SEV-SNP, and process enclaves, such as Intel SGX, provide workload protection against cloud threats. However, they strongly differ in TCB, deployment cost and speed, peer workload protection, resource sharing, fine-grained isolation and attestation, and programming capabilities. Nesting process enclaves within CVMs offers an optimal solution and an opportunity to address long-standing SGX limitations: lack of intra-enclave protection, expensive transitions and exception paths, slow enclave cloning, and a restricted programming model that limits Library Operating Systems (LibOS).
This paper introduces TEEVisor, a CVM-resident architecture consisting of a security monitor and a kernel driver that leverages AMD SEV-SNP Virtual Machine Privilege Levels (VMPLs) to build hardware-protected, process-level enclaves inside a guest CVM with two modes: (1) an SGX binary compatibility mode to run unmodified SGX applications; and (2) a novel extended SGX~(eSGX) mode optimizing slow execution paths and offering richer enclave programming capabilities. On commercial AMD EPYC hardware, against native CVM execution, TEEVisor incurs under 5% overhead on compute- and memory-bound workloads, around 12% on I/O-heavy applications, and accelerates enclave cloning to a rate of 93~$\mu$s/MB of enclave size, demonstrating that eSGX semantics inside a CVM are practical for production use.

---


### 25. [Primal-Dual Flow Matching for Sample-Wise Constrained Generation](https://arxiv.org/abs/2610.12699)

**<font color=#1a73e8>作者：</font>** Zhengyan Huan, Peter Y. Lu, Shuchin Aeron  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the problem of learning to generate data while satisfying a prescribed \emph{sample-wise} constraint with a user-specified probability of constraint satisfaction. Starting with a population-level constrained negative log-likelihood minimization and using a flow-matching (FM) parameterization, under regularity assumptions and sufficient expressivity of the velocity field family, we derive guarantees on the probability of constraint satisfaction for the corresponding primal-dual optimization algorithm. We provide a practical implementation of this approach, called Primal-Dual Flow Matching (PDFM), which has direct control over constraint satisfaction rate and requires only binary membership oracle feedback for constraint satisfaction, avoiding the need for differentiable distances, projections, or special structure of the constraint set, such as convexity. We show that PDFM improves constraint satisfaction over vanilla FM and achieves competitive performance against constraint-aware baselines while maintaining distributional fidelity. Our code is available at this https URL.

---


### 26. [Activating the Annotator: Operationalising Lived Experience in Data Annotation](https://arxiv.org/abs/2610.12701)

**<font color=#1a73e8>作者：</font>** Sheza Munir, Ramaravind Kommiya Mothilal, Syed Ishtiaque Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Perspectivist NLP has established that annotator positionality shapes labels for subjective tasks, but the field still lacks methods for operationalising it. Positionality is typically operationalised as a demographic form completed at recruitment: a static attribute recorded once and treated as a covariate, on the assumption that the knowledge it indexes is active when the annotator reads an item. This paper treats that assumption as a design problem and asks whether lived experience can instead be primed by the task itself. We introduce AXLE, a pre-annotation stage in which a scenario vignette anchors a short, axis-guided conversation that is synthesised into a first-person micro-narrative and returned to the annotator before labelling begins. In a 2x2 between-subjects study (104 annotators, 30 items, 1,040 annotations) on ambiguous hate speech spanning immigration, religion and gender, elicitation was associated with higher identity resonance and higher sensitivity to harm. It also increased label entropy and lowered inter-annotator agreement: the stage appears to surface plurality rather than manufacture consensus, which distinguishes it from annotator training, whose success criterion is convergence.

---


### 27. [Bridging Human and Model Attention: Explainability Analysis of CNN, Mamba, and ViT Architectures with Gaze-Based Validation](https://arxiv.org/abs/2610.12703)

**<font color=#1a73e8>作者：</font>** Marco Stefani, Edoardo Parpaiola, Matteo Bino 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-risk applications of deep learning require precise characterization of model decision-making. We conduct a systematic explainability evaluation across Convolutional Neural Networks (CNNs), Vision Transformers (ViTs), and Vision Mamba (ViM). Unlike predominantly qualitative studies, we quantify the alignment between model attention and human visual perception using eye-tracking ground truth. We formalize this comparison via a standardized normalization pipeline mapping post-hoc attribution maps and gaze heatmaps onto spatial probability distributions. Alignment is evaluated across fine-grained classification, medical imaging, and emotion recognition using architecture-specific XAI methods. We measure fidelity using Jensen-Shannon similarity, Chi-square similarity, and Pearson correlation, three complementary estimators capturing support overlap, mass discrepancy, and structural co-variation. Our results reveal distinct attention dynamics: CNNs tend to exhibit a more global focus, with spatially more diffuse saliency maps that correlate well with human perception in general contexts, while ViTs demonstrate fine-grained, patch-level attention, often focused on discriminative microfeatures. The Mamba architecture shows biased behavior: it achieves strong explainability in medical tasks but exhibits divergent intensity distributions in natural images; our analytical characterization of the metrics makes this dissociation explicit, since near-unit support overlap is attained simultaneously with a vanishing linear correlation. We further analyze the effect of backbone freezing and ensemble strategies on model interpretability. The results highlight how architectural and training choices influence the alignment between model saliency and human visual attention.

---


### 28. [PVBRF-ID: Private, Verifiable and Byzantine-Robust Federated Intrusion Detection for Oilfield Enterprise Networks](https://arxiv.org/abs/2610.12704)

**<font color=#1a73e8>作者：</font>** Mustafa S. Aljumaily, Ali Ataeemh Allami, Mustafa N. Mnati 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated learning allows dispersed oilfield sites to train a shared intrusion detector without pooling network traffic, yet its aggregation step forces a choice between privacy and robustness. Byzantine-robust rules must read each update in the clear, whereas secure aggregation hides updates from the checks that detect poisoning. We present PVBRF-ID, a two-server protocol in which sites secret-share their updates and the servers jointly test each update's norm and its cosine similarity to a reference computed on a small clean root set, revealing one accept bit per site. Commitments, Merkle roots and a homomorphic audit make the inclusion of accepted updates publicly verifiable. On a 15-class Edge-IIoTset task with ten sites holding differently distributed data and ten random seeds, PVBRF-ID matched FedAvg on clean data (macro-F1 0.708 vs. 0.706) and withstood sign-flip attacks (0.696 vs. 0.091). Against an adaptive attacker controlling 30% of sites, PVBRF-ID with secure clipping reached 0.641, whereas FedAvg fell to 0.046; plaintext multi-Krum remained higher by 0.052. An update-inference attacker recovered each site's class mix from plaintext updates (Spearman correlation 0.81) but not from one server's view. Backdoors passed the filter, and noise-based mitigation gave only heuristic protection. The implementation uses Python 3.13, NumPy 2.3, 30 rounds and 10 seeds.

---


### 29. [Better Batches, Better Privacy: Random Allocation for DP-BandMF](https://arxiv.org/abs/2610.12712)

**<font color=#1a73e8>作者：</font>** Ryan McKenna, Arun Ganesh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The current state of the art for batch selection and noise addition in differentially private training is a combination of DP-BandMF (informally, DP-SGD where the noise added in two different steps can be correlated if the steps are within $b$ of each other) and privacy amplification by sampling via Monte Carlo accounting. First, whereas prior batch selection strategies for DP-BandMF were inspired by Poisson sampling, random allocation is known to outperform Poisson sampling for DP-SGD. We therefore propose and analyze new batch selection strategies for DP-BandMF inspired by random allocation, improving RMSE by up to $1.85\times$ over previous work. Second, Monte Carlo accounting typically requires drawing $\Omega(1/\delta)$ samples from a privacy loss distribution, making accounting costly. We increase sampling and scoring throughput by two orders of magnitude through a carefully optimized GPU implementation. Finally, previous work chose the DP-BandMF strategy matrix and the batch selection strategy independently. We give a simple framework for choosing these parameters jointly, reducing RMSE by up to $13.4\%$ over fixed strategy matrices.

---


### 30. [AssemblyLens: Exploring the Role of Structural Roadmaps and Strategies of Furniture Assembly Used by Blind and Low Vision Individuals](https://arxiv.org/abs/2610.12717)

**<font color=#1a73e8>作者：</font>** Bo Liu, Gene S-H Kim, Franklin Mingzhe Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Instructions to assemble flat-packed furniture rely on visuals, making them inaccessible to Blind and Low Vision (BLV) individuals. Consequently, BLV individuals depend on caregivers or external services (e.g., Be My Eyes), limiting their autonomy. We explore how to empower them to assemble such furniture themselves, by providing eight BLV participants in our study with accessible instructions consisting of a high-level roadmap and stepwise procedural guidance. We use a technology probe, AssemblyLens, which converts visual assembly instructions into screen-reader-accessible text. We derive insights into converting instructions, empirical observations of BLV assembly strategies, and the role the roadmap played in them. Our observations yield three themes: spatial cognition and mental mapping, embodied ergonomics and kinetic semantics, and assembly workflow and user agency. We present eight design recommendations for instruction system design. Our findings are a step toward an agenda for inclusive instruction in physical tasks.

---


### 31. [Spatial Context or Memory? Sizing the Inputs of Neural Surrogates for Partially Observed Fields](https://arxiv.org/abs/2610.12723)

**<font color=#1a73e8>作者：</font>** Ruige Kong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural surrogates that forecast a physical field from sparse, noisy sensors read a window of nearby sensors and a history of past snapshots. Practitioners choose both by comparing fitted models with each other. Such comparisons cannot tell a model's shortfall from missing information. We measure the trade-off between window and history against the Bayes-optimal error of the same readings. An exact Gaussian analysis shows that noisy or sparse observation of a field with local dynamics makes the optimal forecast read distant sensors only through spatial correlation. On a forced linear field with a known optimum, trained models that read only the window come within 1% of it. We then train such models on viscous Burgers flow and the chaotic Kuramoto-Sivashinsky (KS) equation, with every deciding comparison fixed before any test evaluation. In every field except KS, eight snapshots remove a smaller fraction of the one-snapshot error as the lead time, the number of steps to the forecast target, grows. In KS, for windows up to one correlation length, they remove a larger fraction. This lead-time inversion persists across sensor densities, three architectures and a two-dimensional domain. It shrinks as damping lowers the Lyapunov exponent. Damping also removes the linear instability of KS. We therefore tie the inversion to instability and leave chaos and linear amplification unseparated. For surrogate design the results give two rules. Size the window in correlation lengths of the field. Split a fixed input budget between window and history for the lead time the model will serve, because the best split moves toward wider windows as the lead time grows. In Burgers flow the split chosen at lead time one ends with 13.5 times the best error at lead time eight.

---


### 32. [A Categorical Atlas of Parameter-Efficient Fine-Tuning: Cones, Orbits, and Gauges](https://arxiv.org/abs/2610.12728)

**<font color=#1a73e8>作者：</font>** Xiaoyu Li, Zhizhou Sha, Chiwun Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning has hundreds of methods, usually compared by parameter count and benchmark score. We compare them as maps. A pretrained checkpoint is a base point in weight space, and a weight-space method is a smooth map from a small parameter space that starts at that point. These maps form a slice category in which the frozen model is initial and full fine-tuning terminal. Three invariants of the map do most of the work. Its image near the base point governs expressivity, through the first-order image, the dimension, a min-cut bound on rank and whether that point is smooth or an apex. Its fibres, with the optimizer's metric, govern training dynamics. Base change moves the base point and covers splitting initialisations, quantisation, restarts and merging. We prove, for example, that zero-initialised LoRA, and Householder reflection adaptation at its default start under stated rank and parity conditions, begin at the apex of a cone; that no exact initialisation lets LoRA reach an update of rank above twice its own; that exactly orthogonal methods never change a weight's singular values in exact arithmetic, however often they are merged; that under Adam with no epsilon, weight decay or clipping and one shared schedule, LoRA+ from the standard zero initialisation follows exactly the trajectory of plain LoRA with its scale multiplied by the learning-rate ratio; that Adam with shared hyperparameters respects only the signed permutations inside LoRA's continuous symmetry group of full-rank factors; and that the activation function decides when a scaling adapter folds into preceding weights. We classify 382 methods from 138 papers by seven coordinates read off their formulas, with 403 simulation arrows and 485 obstructions. Every numbered result is proved in full, and results due to others are credited where we re-derive them.

---


### 33. [Reference-Free Food Volume Estimation from Egocentric Stereo Video](https://arxiv.org/abs/2610.12735)

**<font color=#1a73e8>作者：</font>** Vivan Kumar, Gautham Vinod, Fengqing Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current stereo vision-based approaches for food portion estimation are hindered by the user burden of using a mobile phone to capture multiple images or placing a reference object in the scene for scale calibration. As a step towards passive dietary intake monitoring, we introduce a method that uses stereo video from a wearable egocentric device to reconstruct food items in true physical scale to accurately estimate volume. By utilizing FoundationStereo for zero-shot stereo matching, SAM 2 for food segmentation, and TSDF fusion over a set of keyframes, our method yields a visually and metrically accurate 3D mesh of any plated food item from a single stereo recording. We leverage the unique offerings of wearables, such as a factory-calibrated stereo baseline and camera poses estimated on-device via visual-inertial odometry (VIO), to perform fully automatic reconstruction without a scale reference object in the scene. We show strong initial volume estimation results across five recorded food items, achieving a mean absolute percentage error of 9.1%.

---


### 34. [Kernelized Parameter Sensitivity Atlases for Amortized Conditional Interpretability](https://arxiv.org/abs/2610.12737)

**<font color=#1a73e8>作者：</font>** Davide Wiest, Ahanaf Hasan Ariq, Abdul Monaf Chowdhury  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gradient-based attribution provides input-specific information about model parameters, but computing it via backpropagation for many samples is expensive, while static importance scores discard input dependence. We derive KPSA (Kernelized Parameter Sensitivity Atlas) from a block decomposition of the empirical neural tangent kernel. It measures normalized parameter-group sensitivity, embeds those sources in an explicit query space, and uses a lightweight kernel to estimate sensitivities for unseen inputs. We derive bounds that separate finite-source from irreducible representation error and give margin-based top-$k$ recovery. This paper studies two interpretability applications. Firstly, KPSA identifies parameter groups with high susceptibility to perturbations across vision, forecasting, and protein-modeling setups. Across a fivefold range of parameter budgets ($0.02$-$0.1\%$), its selected groups attain $39$-$85\%$ of the perturbation susceptibility of a first-order backpropagation oracle. In vision and forecasting, these parameter groups form sparse sensitivity circuits that extend across depth and vary systematically with the input. Secondly, we use KPSA on an activation-attribution problem for MLP features in transformers. It retains $81\%$ of the gap between a backpropagation oracle and a constant-sensitivity baseline on vision while increasing batched query-time throughput from 551 to 2,041 images/s and reducing peak GPU memory from 4.55 to 0.44GB. On the protein-modeling task, it recovers $68\%$ of this gap. An ablation of KPSA's kernel aggregation shows that nearest-neighbor retrieval in KPSA space can remain competitive. The empirics show that compact kernel atlases can store useful input-dependent parameter sensitivity while amortizing repeated gradient attribution, a step toward scalable conditional interpretability. Code can be found at this https URL .

---


### 35. [KITE: A Knowledge-Injected Temporal Encoder for Time-Series Event Forecasting](https://arxiv.org/abs/2610.12738)

**<font color=#1a73e8>作者：</font>** Jonas Petersen, Pratik Jawahar, Riccardo Maggioni 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forecasting rare, high-cost events in multivariate time-series systems is hard because their precursors are seldom observed, so a purely data-driven model has little to learn from. The engineers who run these systems, however, hold knowledge that precedes such events, information absent from the scarce labels. We call this a semantic prior and inject it into a self-supervised event forecaster through two switchable mechanisms, a covariate mechanism and an attention-bias mechanism, each the identity at its null, so one architecture serves every prior type with no per-dataset architecture search. A prior helps when it supplies information the observed window does not already contain: in a short context an informative prior beats no prior in-domain (pooled h-AUROC over the no-prior baseline: a periodicity clock +14%, p<0.001; a conservation residual +47% at a 0.25 label fraction), and a working prior transfers out-of-domain (+53%), substituting for feature transfer, while priors the window already recovers stay inert and the attention-bias mechanism shows no measurable gain. KITE is a switchable, attributable route to contextual conditioning, and a substrate for scaling toward cross-domain, pretrained time-series foundation world models that carry their governing structure explicitly.

---


### 36. [NV-Tesseract-AD: Curriculum-Enhanced Conditional Diffusion for Multivariate Time-Series Anomaly Detection](https://arxiv.org/abs/2610.12754)

**<font color=#1a73e8>作者：</font>** Aditi Gautam, Manikandan Ravikiran, Saira Qureshi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose NV-Tesseract-AD, a curriculum learning-enhanced conditional diffusion framework for multivariate time-series anomaly detection. Our central hypothesis is that reconstruction difficulty can be explicitly structured along two complementary axes, masking severity and diffusion noise level, and that training from easier to harder tasks along both axes simultaneously stabilizes optimization and improves residual discriminability. We integrate a Transformer-based diffusion backbone with a three-stage dual curriculum over masking ratios and diffusion timesteps, retaining anomalous samples throughout training and relying on structured corruption to drive self-supervised representation learning. We evaluate NV-Tesseract-AD under two regimes: in-distribution training on the TSB-UAD-M corpus and strict zero-shot transfer to ten EasyTSAD benchmark families without per-dataset tuning. The dual-axis curriculum produces masking-invariant reconstruction, confirmed by a near-zero loss gap between complementary masking strategies within the first training stage, and yields an approximately 3.7-fold improvement in F1 and a 56 percent reduction in MSE relative to a non-curriculum baseline. Zero-shot performance reaches F1 = 0.984 on NAB and F1 = 0.948 on NormA. Weaker results on heterogeneous families are traced to unsupervised threshold calibration rather than reconstruction quality, identifying calibration as the dominant remaining detection bottleneck. Accelerated inference via DPM-Solver++ reduces sampling cost by a factor of 3.5 to 5.7 at the dataset level but couples to thresholding behavior, establishing that the sampler and threshold must be validated jointly. Together, these findings demonstrate that aligning diffusion denoising difficulty with curriculum learning principles provides a principled and practical approach for robust anomaly detection in complex multivariate time series.

---


### 37. [MADS: Multi-Agent Dialog Simulation for Robust Conversational Agents](https://arxiv.org/abs/2610.12757)

**<font color=#1a73e8>作者：</font>** Arkajyoti Chakraborty, Adam Zernik, Ishika Kulkarni 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Task-oriented conversational agents remain fragile under realistic conditions, especially when users exhibit non-cooperative behavior. Existing function-calling benchmarks underrepresent adversarial conversation trajectories, thereby limiting the training resources available for developing robust agents. We present MADS (Multi-Agent Dialog Simulation), a synthetic data generation pipeline that produces structured, diverse dialogue trajectories. We inject adversarial conversation, producing validated conversation trajectories that capture realistic, unhappy paths. Using MADS, we construct MADS-Bench: a benchmark spanning six domains, 55 personas, and 1095 conversations, with approximately 66% of conversations containing failure-prone conversation scenarios. We evaluate the robustness of the trained models using a two-stage training approach that combines supervised fine-tuning (SFT) and reinforcement learning with verifiable rewards (RLVR).

---


### 38. [Onions in the ATmosphere: Decentralizing Trust in Identity](https://arxiv.org/abs/2610.12764)

**<font color=#1a73e8>作者：</font>** Paul Syverson, Nick Gerakines  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multiple approaches have been implemented for identities that associate meaningful identifiers, such as domain names, with self-authenticating identifiers, such as onion addresses. While these approaches offer various advantages both from identifier meaningfulness and from identifier self-authentication, identifier association itself is subject to blocking, hijack, fingerprinting, and other forms of surveillance and manipulation. So too are the resources associated with an identity comprising a meaningful identifier and a self-authenticating identifier. This paper describes ongoing work on two such approaches to self-authenticating meaningful identity (SAMI): associating a registered domain name with an onion address (onion association) and associating an atproto handle with a decentralized identifier (DID association). We present both the application of already implemented and published means of secure onion association to DID association and the combination of both in a single identity. Finally, we describe grounding identity association and integrity in contextual trust, wherein trusting attestations of identity relies on contextual relevance of an attestor to the identity rather than relying only on structural authority, for example as embodied in the traditional centralized infrastructure.

---


### 39. [Provenance-grouped protocol for evaluating machine learning in perovskite photovoltaics](https://arxiv.org/abs/2610.12766)

**<font color=#1a73e8>作者：</font>** Qiwei Han, Chi Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine-learning models for perovskite solar cells are typically evaluated using random data splits, which we show systematically leak information through massive internal duplication. Because nearly two-thirds of curated devices share their exact recipe with another, random splits primarily reward the mere recall of historical data rather than testing true physical generalisation. To solve this, we mapped the institutional provenance of the Perovskite Database and established a rigorous hierarchy of grouped splits that progressively isolate duplicate devices, publications, and institutions. Benchmarking thirteen models establishes new state-of-the-art performance across all splits and reveals a critical regime shift: while tree ensembles dominate random splits by recognising familiar recipes, their ranking collapses on genuinely unseen institutions and future discoveries, where composition-aware neural architectures excel. Furthermore, feature importance demonstrates that the device architecture and fabrication methodology dictate final efficiency just as strongly as the absorber chemistry. This standardised protocol empowers the community to separate memorisation from true physical discovery.

---


### 40. [Coordinate-Free Automatic Differentiation](https://arxiv.org/abs/2610.12776)

**<font color=#1a73e8>作者：</font>** Alex Guerra, Joshua Aduol, Yaqian Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automatic differentiation (AD) is a cornerstone of modern machine learning. Since all AD frameworks implicitly fix a basis of Euclidean space to define gradients and Jacobians, they natively process mathematical objects that are arrays of a fixed set of coordinates. This makes it awkward to express objects such as rotations, volume forms, and curvatures that arise, for example, in applications of AI to science. Bespoke workarounds lack reusability. We show that (i) a single, basis-independent derivative operator can represent many geometric differential operations, and (ii) this operator can be expressed entirely in terms of existing AD primitives. This reusable transformation can be composed with JAX batching, compilation, and hardware acceleration. Geometry enters as algebraic data. We experimentally demonstrate its reuse across different manifold operators, its composition through a spacetime inverse-problem pipeline, and its use in optimization over different rotor subgroups.

---


### 41. [Representation Alignment from a Few Paired Data via Distilled Optimal Transport](https://arxiv.org/abs/2610.12781)

**<font color=#1a73e8>作者：</font>** Julien Kordes, Reuben Dorent  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Aligning two independently pretrained unimodal encoders typically demands millions of paired examples. In this paper, we study the regime where only $N \sim 100$--$500$ pairs are available, while unpaired data on either side is abundant. Our method expresses every representation by its similarities to the $N$ paired anchors, which places both modalities in a common coordinate system; matches the two point clouds with a single entropic optimal transport problem solved over the entire pool, whose marginal constraints counteract the hubness that defeats nearest-neighbor matching; and distills the resulting plan into two lightweight encoders, so that the correspondence becomes inductive. We additionally put this marginal constraint in relation with the one-step hub corrections of the bilingual lexicon induction literature. Pairing is required only for the anchors: the unpaired collections may be drawn independently from the two marginals, so that no item outside the anchor set needs to have both of its modalities observed. We evaluate on image-text and molecule-text alignment, where our method outperforms existing approaches at the same anchor budget on Flickr30k, MS-COCO and ChEBI-20.

---


### 42. [Shift-Aware Identity-Guided Latent Refinement for Referring Audio--Visual Segmentation](https://arxiv.org/abs/2610.12783)

**<font color=#1a73e8>作者：</font>** Kun Li, Sami Sebastian Brandt, Michael Ying Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring Audio--Visual Segmentation (Ref-AVS) is an emergent multimodal task requiring the precise identification and segmentation of a specific object based on a natural language expression grounded in both visual and auditory cues. Unlike traditional AVS, which segments generic sound sources, or referring video object segmentation (Ref-VOS), which relies solely on visual--textual grounding, Ref-AVS necessitates fine-grained tri-modal interaction across vision, audio, and language. However, existing methods often fail to maintain consistency when subjected to target shift, a phenomenon where the model erroneously transfers its focus between objects due to transient occlusions, acoustic fading, or identity ambiguities. To address this, we propose a novel Shift-Aware Identity-guided Latent (SAIL) refinement framework. It introduces a dual-token strategy that decouples frame-level dynamics from a global semantic anchor to explicitly model target-shift cues. We design a shift-aware refinement module that rectifies drift by aligning tokens with domain-specific evidence. Finally, we leverage a decoder that integrates the refined embeddings with a continuous memory update to maintain spatio-temporal coherence and identity consistency throughout the video sequence. Extensive experiments conducted on two Ref-AVS benchmarks demonstrate the effectiveness of our proposed method, significantly outperforming existing AVS, Ref-VOS, and Ref-AVS approaches. The code will be released after publication.

---


### 43. [Domain Adaptation of SAM 2.1 for Building-Component Segmentation in Image-Based 3D Reconstruction](https://arxiv.org/abs/2610.12786)

**<font color=#1a73e8>作者：</font>** Ehsan Agha Ebrahimi, Yong-Cheol Lee, Keith G. Mills  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D reconstruction of building components using image-based scanning requires appropriate segmentation of the objects in the 2D building images. In order to benefit from consistent grouping of the 2D masks in 3D environments, vision foundation models such as the Segment Anything Model have been utilized by Group Anything with Radiance Fields (GARField) to perform 3D segmentation. This study fine-tuned SAM 2.1 on the HBD dataset, consisting of 2,679 annotated images from 42 buildings, to enhance multi-class segmentation of 2D building images, covering 11 classes (Wall, Window, Ceiling, Door, Column, Beam, Floor, Opening, Curtain Wall, Roof, and Lift). The model was evaluated using per-class IoU, Dice, and mIoU metrics, and the results show an improvement in mIoU from 49.9% to 69.6%, indicating a meaningful improvement in class segmentation and providing a more accurate model for distilling the masks in 3D. SegFormer was then used as a baseline, generating per-class masks for comparison with SAM 2.1, which indicates improvement in some object classes with larger surface area. The masks in the building images were grouped in the neural radiance field, and the pretrained SAM 2.1 was compared with the fine-tuned SAM 2.1 in the newly rendered images. This comparison shows that fine-tuning improves the grouping of building components at a user-selected grouping scale. This advances the application of Group Anything with Radiance Fields (GARField) in 3D, enabling better segmentation of building structures for 3D auto-reconstruction.

---


### 44. [Power, Performance, and Area of HPC-Based Malware Detectors: An FPGA and Open-PDK ASIC Study](https://arxiv.org/abs/2610.12795)

**<font color=#1a73e8>作者：</font>** Alireza Abolhasani Zeraatkar, Parnian Shabani Kamran, Parsa Mirfasihi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hardware malware detectors (HMDs) classify programs as benign or malicious based on hardware performance counter (HPC) data. Previous studies have shown that ensemble classifiers outperform other classifiers on detection metrics. However, the area, power, and timing costs of HMDs remain open questions. We address these questions across a comprehensive design space comprising multiple classifier families, variable HPC sets, and ensemble learning methods. We designed a pipeline to reconstruct selected trained models, generate synthesizable register-transfer-level (RTL) implementations, validate each design against a bit-accurate golden model, and evaluate the implementations. The results show that tree- and rule-based detectors achieve the highest detection performance with nearly an order of magnitude less area and several times lower energy than function-based classifiers. Reducing the number of HPC inputs to fit a processor's concurrent-counter limit preserves detection performance while substantially reducing area, power, and delay.

---


### 45. [The Expressive Power of Random-Feature MPNNs Across Graph Sizes](https://arxiv.org/abs/2610.12809)

**<font color=#1a73e8>作者：</font>** Robert R. Nerem, Mitchell Black, Antonis Vasileiou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous random node features increase the expressivity of message-passing neural networks (MPNNs), but existing theoretical analyses are not fine-grained enough to capture their limitations, particularly in approximating functions across graph sizes or under a fixed number of random bits. We develop a population-level framework for size-uniform approximation. For MPNNs with a graph-size-independent Lipschitz bound in their initial features, including standard mean, max, and order-normalized sum architectures, we show that continuous random features can be quantized to finitely many colors with arbitrarily small uniform error in expected output. This reduction lets us transfer limitations on finite-color distinguishability to limitations on size-uniform approximation with continuous random features. We use this framework to prove that these MPNNs are not size-uniformly universal, analyze the expressivity gains from colors and independent trials, and establish incomparability between random-color MPNNs and higher-order Weisfeiler-Leman methods. We also give finite-color MPNN constructions for tree subgraph isomorphism via color coding and a local MST task.

---


### 46. [Spend Where It Matters: Particle Search with MH Refinement for Budget-Constrained Audio-Visual Alignment](https://arxiv.org/abs/2610.12811)

**<font color=#1a73e8>作者：</font>** Shivanshu Shekhar, Raghavendra Addanki, Tong Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reward-guided inference-time alignment can improve joint audio-visual generation, but optimizing multiple alignment objectives requires many expensive model evaluations, making existing methods costly under limited compute. Particle-based search enables global exploration but incurs estimation error with a finite population, while Metropolis-Hastings (MH) can refine candidates locally but benefits from a strong initialization. We introduce \textbf{S}pend \textbf{W}here \textbf{I}t \textbf{M}atters (\modelname), a two-stage, training-free, reward-agnostic framework that combines particle search with MH refinement under a fixed compute budget. In the first stage, we adaptively allocate particles across denoising checkpoints using online variance estimates, minimizing estimation variance while concentrating compute where it is most useful. This search provides a promising candidate for MH refinement, which uses local noise-and-denoise proposals on completed outputs to further improve reward. By starting from a strong candidate, MH can recover additional reward without requiring a larger particle population or costly global exploration. We show that, at matched compute, combining particle search with MH refinement achieves higher rewards than either approach alone. On \textsc{JavisBench-Mini}, at closely matched compute, \modelname achieves mean relative gains across seven metrics of $30.7\%$ over BoN and $14.1\%$ over EvoSearch with JavisDiT++, and $9.2\%$ over BoN and $17.0\%$ over EvoSearch with LTX-2. Beyond joint audio-visual generation, we also demonstrate the benefits of adaptive particle allocation on SD1.5 image generation, improving AestheticScore by $2.2\%$ and ImageReward by $6.0\%$ over uniform allocation.

---


### 47. [Deploying RDMA for Large-Scale Inference and Training Workloads](https://arxiv.org/abs/2610.12815)

**<font color=#1a73e8>作者：</font>** Yibo Huang, Yi Cui, Yukai Huang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> RDMA can reduce communication overhead in distributed machine learning systems, but realizing these benefits in production requires more than replacing TCP. Variable-size messages, concurrent connections, bursty incasts, and service failures introduce challenges that hardware offload alone cannot address. This paper reports our experience deploying ByteExpress, a software communication layer over hardware RDMA, in ByteDance's parameter-server-based inference and training systems. We present three lessons from the deployment: efficient RDMA requires buffer management across application and transport layers; scalable communication requires coordinated management of connections, receive capacity, and outstanding data; and service availability requires recovery above the transport layer. ByteExpress combines an RDMA-aware allocator, zero-copy transfers, QP multiplexing, receive-credit flow control, a software send window, and RPC-assisted recovery. In production inference, ByteExpress reduces mean and P99 model parameter fetch latency by 35.7% and 43.7%, respectively, and total CPU usage by 10.69% compared with kernel TCP. In training, ByteExpress reduces P99 model parameter push latency by up to 74.0% compared with TCP, with no PFC pauses observed at runtime.

---


### 48. [Inverse Synthesis of Shock Time Series from Shock Response Spectra Using Ensembles of Conditional Variational Autoencoders](https://arxiv.org/abs/2610.12820)

**<font color=#1a73e8>作者：</font>** Adam Watts, Charles Young, Ryan Bowering 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The shock response spectrum (SRS) characterizes the peak responses of single-degree-of-freedom systems to transient acceleration. Because the mapping from an acceleration time series (waveform) to its SRS is many-to-one, inverse synthesis seeks candidate waveforms consistent with a prescribed spectrum. We extend an earlier conditional variational autoencoder (CVAE) framework with a recurrent decoder that predicts multiscale wavelet coefficients and reconstructs waveforms through an inverse discrete wavelet transform. Individual models exhibit limited variability under latent sampling, motivating an ensemble of independently trained models spanning different mother wavelets and decomposition levels. Each member produces a separate candidate waveform for the same target SRS. Evaluation on four held-out benchmark datasets shows lower mean and median spectral errors for the illustrated wavelet model than for the earlier direct time-domain CVAE and a sum-of-decayed-sinusoids (SDS) baseline. A conditioning study examines frequency-grid and encoding choices. Comparisons with published inverse-SRS methods demonstrate superior performance across four holdout benchmark datasets (two operational shock datasets, one earthquake dataset, and one synthetic shock dataset) and competitive performance on synthetic targets reported by Brake. Single-model inference requires approximately 0.1-0.6 ms per waveform during batched inference compared with 5-8 s for SDS, excluding offline training. This low inference cost enables rapid generation of distinct SRS-compatible candidate waveforms across the ensemble, although their physical suitability requires assessment beyond spectral agreement.

---


### 49. [Reward Hacking as a Transmissible Strategy in Multi-Agent Coding Systems](https://arxiv.org/abs/2610.12822)

**<font color=#1a73e8>作者：</font>** Yuepeng Hu, Pegah Ghahremani, Reza Aghajani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems are increasingly used to solve coding tasks by coordinating agents that share code and plans. These agents are often optimized with reinforcement learning (RL) using automated evaluators, but bypassing evaluation can earn reward without producing a genuine solution. Prior work has largely treated reward hacking as a single-agent failure. In this work, we show that a reward-hacking strategy elicited in one agent can propagate to others and affect system coordination. Across four open-weight backbones, coding RL elicits and amplifies reward hacking in two settings: explicit mechanism descriptions in the system prompt and mid-training that models upstream exposure to facts about the coding environment. Using post-RL agents from the mid-training setting as sources, we observe propagation through code and shared memory, and across roles through natural-language plans. Even agents based on small open-weight models induce reward hacking in stronger closed-weight targets. On hard tasks, propagation can intensify along a transmission chain after the original source leaves as the code acquires more persuasive justifications. We also theoretically analyze conditions under which reward hacking amplifies, persists, or decays across agent interactions. Beyond propagation, reward hacking can bias task routing toward reward-hacking agents and survive candidate aggregation. As potential mitigations, we evaluate code review by the coder or a separate verifier, both of which reduce delivered hacks. Together, these results establish reward hacking as a transmissible strategy whose effects extend beyond the agent in which it first emerges.

---


### 50. [When Charts Deceive Web Agents: A Paired Benchmark for Misleading Visualization-Grounded Tasks](https://arxiv.org/abs/2610.12823)

**<font color=#1a73e8>作者：</font>** Yisheng Li, Dongming Han, Hongkun Pan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Web agents increasingly browse, interpret, and act on web content on behalf of users. In many realistic workflows, however, the visual evidence they consume is not neutral: charts and dashboards can be misleading, shaping judgments without issuing any explicit malicious instruction. Unlike chart question answering, Web Agents treat charts as intermediate evidence whose misinterpretation can propagate into concrete downstream actions --- a reliability risk that remains underexplored. We introduce MisVisAgentBench, the first paired executable benchmark for evaluating how misleading visualizations affect Web Agent execution. It comprises 280 task instances in matched clean--misleading pairs that differ only in chart evidence. We further provide a diagnostic framework that isolates misleading-induced failures from baseline task difficulty (Zhu et al., 2025) and captures execution-level effects such as extra browsing steps and decision hesitation. Across thirteen vision-language Web Agents, replacing clean charts with misleading counterparts reduces the average task success rate by more than 34 percentage points. Moreover, these failures predominantly follow the targeted misleading action branch, suggesting that deceptive charts systematically redirect rather than randomly disrupt agent decisions. These results reveal that visualization robustness is a critical yet understudied dimension of Web Agent safety and reliability.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-244](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
